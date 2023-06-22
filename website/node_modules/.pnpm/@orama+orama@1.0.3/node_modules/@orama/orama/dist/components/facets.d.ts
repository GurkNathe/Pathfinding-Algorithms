import type { FacetResult, FacetsParams, Orama, Schema, TokenScore } from '../types.js';
export declare function getFacets<S extends Schema>(orama: Orama<{
    Schema: S;
}>, results: TokenScore[], facetsConfig: FacetsParams): Promise<FacetResult>;
