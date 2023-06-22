import { ArraySearchableType, Document, ElapsedTime, ScalarSearchableType, Schema, SearchableType } from '../types.js';
export { getDocumentProperties } from '../utils.js';
export declare function formatElapsedTime(n: bigint): Promise<ElapsedTime>;
export declare function getDocumentIndexId(doc: Document): Promise<string>;
export declare function validateSchema<S extends Schema = Schema>(doc: Document, schema: S): Promise<string | undefined>;
export declare function isArrayType(type: SearchableType): boolean;
export declare function getInnerType(type: ArraySearchableType): ScalarSearchableType;
