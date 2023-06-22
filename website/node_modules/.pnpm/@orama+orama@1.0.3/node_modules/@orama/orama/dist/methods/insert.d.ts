import { Document, Orama } from '../types.js';
export declare function insert(orama: Orama, doc: Document, language?: string, skipHooks?: boolean): Promise<string>;
export declare function insertMultiple(orama: Orama, docs: Document[], batchSize?: number, language?: string, skipHooks?: boolean): Promise<string[]>;
export declare function innerInsertMultiple(orama: Orama, docs: Document[], batchSize?: number, language?: string, skipHooks?: boolean): Promise<string[]>;
