import { Orama, Result, Results, SearchParams } from '../types.js';
export declare function search<AggValue = Result[]>(orama: Orama, params: SearchParams<AggValue>, language?: string): Promise<Results<AggValue>>;
