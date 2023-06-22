import { createError } from '../errors.js';
import { uniqueId, formatNanoseconds } from '../utils.js';
export { getDocumentProperties } from '../utils.js';
export async function formatElapsedTime(n) {
    return {
        raw: Number(n),
        formatted: await formatNanoseconds(n)
    };
}
export async function getDocumentIndexId(doc) {
    if (doc.id) {
        if (typeof doc.id !== 'string') {
            throw createError('DOCUMENT_ID_MUST_BE_STRING', typeof doc.id);
        }
        return doc.id;
    }
    return await uniqueId();
}
export async function validateSchema(doc, schema) {
    for (const [prop, type] of Object.entries(schema)){
        const value = doc[prop];
        const typeOfValue = typeof value;
        if (typeOfValue === 'undefined') {
            continue;
        }
        const typeOfType = typeof type;
        if (typeOfType === 'string' && isArrayType(type)) {
            if (!Array.isArray(value)) {
                return prop;
            }
            const expectedType = getInnerType(type);
            const valueLength = value.length;
            for(let i = 0; i < valueLength; i++){
                if (typeof value[i] !== expectedType) {
                    return prop + '.' + i;
                }
            }
            continue;
        }
        if (typeOfType === 'object') {
            if (!value || typeOfValue !== 'object') {
                return prop;
            }
            const subProp = await validateSchema(value, type);
            if (subProp) {
                return prop + '.' + subProp;
            }
            continue;
        }
        if (typeOfValue !== type) {
            return prop;
        }
    }
    return undefined;
}
const IS_ARRAY_TYPE = {
    string: false,
    number: false,
    boolean: false,
    'string[]': true,
    'number[]': true,
    'boolean[]': true
};
const INNER_TYPE = {
    'string[]': 'string',
    'number[]': 'number',
    'boolean[]': 'boolean'
};
export function isArrayType(type) {
    return IS_ARRAY_TYPE[type];
}
export function getInnerType(type) {
    return INNER_TYPE[type];
}

//# sourceMappingURL=defaults.js.map