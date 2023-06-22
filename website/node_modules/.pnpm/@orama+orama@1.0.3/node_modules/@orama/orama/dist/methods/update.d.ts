import { Document, Orama } from '../types.js';
export declare function update(orama: Orama, id: string, doc: Document, language?: string, skipHooks?: boolean): Promise<string>;
export declare function updateMultiple(orama: Orama, ids: string[], docs: Document[], batchSize?: number, language?: string, skipHooks?: boolean): Promise<string[]>;
