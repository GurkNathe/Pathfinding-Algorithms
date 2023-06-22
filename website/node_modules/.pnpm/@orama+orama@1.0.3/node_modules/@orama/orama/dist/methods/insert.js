import { isArrayType } from '../components.js';
import { runMultipleHook, runSingleHook } from '../components/hooks.js';
import { trackInsertion } from '../components/sync-blocking-checker.js';
import { createError } from '../errors.js';
export async function insert(orama, doc, language, skipHooks) {
    const errorProperty = await orama.validateSchema(doc, orama.schema);
    if (errorProperty) {
        throw createError('SCHEMA_VALIDATION_FAILURE', errorProperty);
    }
    return innerInsert(orama, doc, language, skipHooks);
}
async function innerInsert(orama, doc, language, skipHooks) {
    const { index , docs  } = orama.data;
    const id = await orama.getDocumentIndexId(doc);
    if (typeof id !== 'string') {
        throw createError('DOCUMENT_ID_MUST_BE_STRING', typeof id);
    }
    if (!await orama.documentsStore.store(docs, id, doc)) {
        throw createError('DOCUMENT_ALREADY_EXISTS', id);
    }
    const docsCount = await orama.documentsStore.count(docs);
    if (!skipHooks) {
        await runSingleHook(orama.beforeInsert, orama, id, doc);
    }
    const indexableProperties = await orama.index.getSearchableProperties(index);
    const indexablePropertiesWithTypes = await orama.index.getSearchablePropertiesWithTypes(index);
    const indexableValues = await orama.getDocumentProperties(doc, indexableProperties);
    for (const [key, value] of Object.entries(indexableValues)){
        if (typeof value === 'undefined') {
            continue;
        }
        const actualType = typeof value;
        const expectedType = indexablePropertiesWithTypes[key];
        if (isArrayType(expectedType) && Array.isArray(value)) {
            continue;
        }
        if (actualType !== expectedType) {
            throw createError('INVALID_DOCUMENT_PROPERTY', key, expectedType, actualType);
        }
    }
    for (const prop of indexableProperties){
        var _orama_index, _orama_index_beforeInsert, _orama_index1, _orama_index_afterInsert;
        const value = indexableValues[prop];
        if (typeof value === 'undefined') {
            continue;
        }
        const expectedType = indexablePropertiesWithTypes[prop];
        await ((_orama_index_beforeInsert = (_orama_index = orama.index).beforeInsert) === null || _orama_index_beforeInsert === void 0 ? void 0 : _orama_index_beforeInsert.call(_orama_index, orama.data.index, prop, id, value, expectedType, language, orama.tokenizer, docsCount));
        await orama.index.insert(orama.index, orama.data.index, prop, id, value, expectedType, language, orama.tokenizer, docsCount);
        await ((_orama_index_afterInsert = (_orama_index1 = orama.index).afterInsert) === null || _orama_index_afterInsert === void 0 ? void 0 : _orama_index_afterInsert.call(_orama_index1, orama.data.index, prop, id, value, expectedType, language, orama.tokenizer, docsCount));
    }
    const sortableProperties = await orama.sorter.getSortableProperties(orama.data.sorting);
    const sortablePropertiesWithTypes = await orama.sorter.getSortablePropertiesWithTypes(orama.data.sorting);
    const sortableValues = await orama.getDocumentProperties(doc, sortableProperties);
    for (const prop of sortableProperties){
        const value = sortableValues[prop];
        if (typeof value === 'undefined') {
            continue;
        }
        const expectedType = sortablePropertiesWithTypes[prop];
        await orama.sorter.insert(orama.data.sorting, prop, id, value, expectedType, language);
    }
    if (!skipHooks) {
        await runSingleHook(orama.afterInsert, orama, id, doc);
    }
    trackInsertion(orama);
    return id;
}
export async function insertMultiple(orama, docs, batchSize, language, skipHooks) {
    if (!skipHooks) {
        await runMultipleHook(orama.beforeMultipleInsert, orama, docs);
    }
    // Validate all documents before the insertion
    const docsLength = docs.length;
    for(let i = 0; i < docsLength; i++){
        const errorProperty = await orama.validateSchema(docs[i], orama.schema);
        if (errorProperty) {
            throw createError('SCHEMA_VALIDATION_FAILURE', errorProperty);
        }
    }
    return innerInsertMultiple(orama, docs, batchSize, language, skipHooks);
}
export async function innerInsertMultiple(orama, docs, batchSize, language, skipHooks) {
    if (!batchSize) {
        batchSize = 1000;
    }
    const ids = [];
    await new Promise((resolve, reject)=>{
        let i = 0;
        async function _insertMultiple() {
            const batch = docs.slice(i * batchSize, (i + 1) * batchSize);
            i++;
            if (!batch.length) {
                return resolve();
            }
            for (const doc of batch){
                try {
                    const id = await insert(orama, doc, language, skipHooks);
                    ids.push(id);
                } catch (err) {
                    reject(err);
                }
            }
            setTimeout(_insertMultiple, 0);
        }
        setTimeout(_insertMultiple, 0);
    });
    if (!skipHooks) {
        await runMultipleHook(orama.afterMultipleInsert, orama, docs);
    }
    return ids;
}

//# sourceMappingURL=insert.js.map