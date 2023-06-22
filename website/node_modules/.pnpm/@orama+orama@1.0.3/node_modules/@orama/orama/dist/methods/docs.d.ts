import { Document, Orama } from '../types.js';
export declare function getByID(db: Orama, id: string): Promise<Document | undefined>;
export declare function count(db: Orama): Promise<number>;
