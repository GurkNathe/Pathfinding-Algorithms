import type { Orama, TokenScore, GroupByParams, GroupResult } from '../types.js';
export declare function getGroups<AggValue>(orama: Orama, results: TokenScore[], groupBy: GroupByParams<AggValue>): Promise<GroupResult<AggValue>>;
