import { Components, Orama, Schema, SorterConfig, ProvidedTypes } from '../types.js';
interface CreateArguments<P extends ProvidedTypes> {
    schema: Schema;
    sort?: SorterConfig;
    language?: string;
    components?: Components<P>;
    id?: string;
}
export declare function create<P extends ProvidedTypes>({ schema, sort, language, components, id, }: CreateArguments<P>): Promise<Orama<P>>;
export {};
