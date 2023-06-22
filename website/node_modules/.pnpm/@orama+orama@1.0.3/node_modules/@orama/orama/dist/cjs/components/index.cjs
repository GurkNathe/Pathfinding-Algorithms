"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
function _export(target, all) {
    for(var name in all)Object.defineProperty(target, name, {
        enumerable: true,
        get: all[name]
    });
}
_export(exports, {
    create: ()=>create,
    insert: ()=>insert,
    remove: ()=>remove,
    search: ()=>search,
    searchByWhereClause: ()=>searchByWhereClause,
    getSearchableProperties: ()=>getSearchableProperties,
    getSearchablePropertiesWithTypes: ()=>getSearchablePropertiesWithTypes,
    load: ()=>load,
    save: ()=>save,
    createIndex: ()=>createIndex
});
let _esmCreate;
let _esmInsert;
let _esmRemove;
let _esmSearch;
let _esmSearchByWhereClause;
let _esmGetSearchableProperties;
let _esmGetSearchablePropertiesWithTypes;
let _esmLoad;
let _esmSave;
let _esmCreateIndex;
async function create(...args) {
    if (!_esmCreate) {
        const imported = await import('../../components/index.js');
        _esmCreate = imported.create;
    }
    return _esmCreate(...args);
}
async function insert(...args) {
    if (!_esmInsert) {
        const imported = await import('../../components/index.js');
        _esmInsert = imported.insert;
    }
    return _esmInsert(...args);
}
async function remove(...args) {
    if (!_esmRemove) {
        const imported = await import('../../components/index.js');
        _esmRemove = imported.remove;
    }
    return _esmRemove(...args);
}
async function search(...args) {
    if (!_esmSearch) {
        const imported = await import('../../components/index.js');
        _esmSearch = imported.search;
    }
    return _esmSearch(...args);
}
async function searchByWhereClause(...args) {
    if (!_esmSearchByWhereClause) {
        const imported = await import('../../components/index.js');
        _esmSearchByWhereClause = imported.searchByWhereClause;
    }
    return _esmSearchByWhereClause(...args);
}
async function getSearchableProperties(...args) {
    if (!_esmGetSearchableProperties) {
        const imported = await import('../../components/index.js');
        _esmGetSearchableProperties = imported.getSearchableProperties;
    }
    return _esmGetSearchableProperties(...args);
}
async function getSearchablePropertiesWithTypes(...args) {
    if (!_esmGetSearchablePropertiesWithTypes) {
        const imported = await import('../../components/index.js');
        _esmGetSearchablePropertiesWithTypes = imported.getSearchablePropertiesWithTypes;
    }
    return _esmGetSearchablePropertiesWithTypes(...args);
}
async function load(...args) {
    if (!_esmLoad) {
        const imported = await import('../../components/index.js');
        _esmLoad = imported.load;
    }
    return _esmLoad(...args);
}
async function save(...args) {
    if (!_esmSave) {
        const imported = await import('../../components/index.js');
        _esmSave = imported.save;
    }
    return _esmSave(...args);
}
async function createIndex(...args) {
    if (!_esmCreateIndex) {
        const imported = await import('../../components/index.js');
        _esmCreateIndex = imported.createIndex;
    }
    return _esmCreateIndex(...args);
}

//# sourceMappingURL=index.js.map