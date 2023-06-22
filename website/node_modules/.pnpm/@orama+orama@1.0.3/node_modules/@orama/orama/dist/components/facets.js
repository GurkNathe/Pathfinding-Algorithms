import { getNested } from '../utils.js';
function sortingPredicate(order = 'desc', a, b) {
    if (order.toLowerCase() === 'asc') {
        return a[1] - b[1];
    } else {
        return b[1] - a[1];
    }
}
export async function getFacets(orama, results, facetsConfig) {
    const facets = {};
    const allIDs = results.map(([id])=>id);
    const allDocs = await orama.documentsStore.getMultiple(orama.data.docs, allIDs);
    const facetKeys = Object.keys(facetsConfig);
    const properties = await orama.index.getSearchablePropertiesWithTypes(orama.data.index);
    for (const facet of facetKeys){
        let values = {};
        // Hack to guarantee the same order of ranges as specified by the user
        // TODO: Revisit this once components land
        if (properties[facet] === 'number') {
            const { ranges  } = facetsConfig[facet];
            const tmp = [];
            for (const range of ranges){
                tmp.push([
                    `${range.from}-${range.to}`,
                    0
                ]);
            }
            values = Object.fromEntries(tmp);
        }
        facets[facet] = {
            count: 0,
            values
        };
    }
    const allDocsLength = allDocs.length;
    for(let i = 0; i < allDocsLength; i++){
        const doc = allDocs[i];
        for (const facet of facetKeys){
            const facetValue = facet.includes('.') ? await getNested(doc, facet) : doc[facet];
            const propertyType = properties[facet];
            switch(propertyType){
                case 'number':
                    {
                        const ranges = facetsConfig[facet].ranges;
                        calculateNumberFacet(ranges, facets[facet].values, facetValue);
                        break;
                    }
                case 'number[]':
                    {
                        const alreadyInsertedValues = new Set();
                        const ranges = facetsConfig[facet].ranges;
                        for (const v of facetValue){
                            calculateNumberFacet(ranges, facets[facet].values, v, alreadyInsertedValues);
                        }
                        break;
                    }
                case 'boolean':
                case 'string':
                    {
                        calculateBooleanOrStringFacet(facets[facet].values, facetValue, propertyType);
                        break;
                    }
                case 'boolean[]':
                case 'string[]':
                    {
                        const alreadyInsertedValues = new Set();
                        const innerType = propertyType === 'boolean[]' ? 'boolean' : 'string';
                        for (const v of facetValue){
                            calculateBooleanOrStringFacet(facets[facet].values, v, innerType, alreadyInsertedValues);
                        }
                        break;
                    }
            }
        }
    }
    for (const facet of facetKeys){
        // Count the number of values for each facet
        facets[facet].count = Object.keys(facets[facet].values).length;
        // Sort only string-based facets
        if (properties[facet] === 'string') {
            const stringFacetDefinition = facetsConfig;
            facets[facet].values = Object.fromEntries(Object.entries(facets[facet].values).sort((a, b)=>sortingPredicate(stringFacetDefinition.sort, a, b)).slice(stringFacetDefinition.offset ?? 0, stringFacetDefinition.limit ?? 10));
        }
    }
    return facets;
}
function calculateNumberFacet(ranges, values, facetValue, alreadyInsertedValues) {
    for (const range of ranges){
        const value = `${range.from}-${range.to}`;
        if (alreadyInsertedValues && alreadyInsertedValues.has(value)) {
            continue;
        }
        if (facetValue >= range.from && facetValue <= range.to) {
            if (values[value] === undefined) {
                values[value] = 1;
            } else {
                values[value]++;
                if (alreadyInsertedValues) {
                    alreadyInsertedValues.add(value);
                }
            }
        }
    }
}
function calculateBooleanOrStringFacet(values, facetValue, propertyType, alreadyInsertedValues) {
    // String or boolean based facets
    const value = (facetValue === null || facetValue === void 0 ? void 0 : facetValue.toString()) ?? (propertyType === 'boolean' ? 'false' : '');
    if (alreadyInsertedValues && alreadyInsertedValues.has(value)) {
        return;
    }
    values[value] = (values[value] ?? 0) + 1;
    if (alreadyInsertedValues) {
        alreadyInsertedValues.add(value);
    }
}

//# sourceMappingURL=facets.js.map