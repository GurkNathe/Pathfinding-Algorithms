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
    get: ()=>get,
    getMultiple: ()=>getMultiple,
    store: ()=>store,
    remove: ()=>remove,
    count: ()=>count,
    load: ()=>load,
    save: ()=>save,
    createDocumentsStore: ()=>createDocumentsStore
});
let _esmCreate;
let _esmGet;
let _esmGetMultiple;
let _esmStore;
let _esmRemove;
let _esmCount;
let _esmLoad;
let _esmSave;
let _esmCreateDocumentsStore;
async function create(...args) {
    if (!_esmCreate) {
        const imported = await import('../../components/documents-store.js');
        _esmCreate = imported.create;
    }
    return _esmCreate(...args);
}
async function get(...args) {
    if (!_esmGet) {
        const imported = await import('../../components/documents-store.js');
        _esmGet = imported.get;
    }
    return _esmGet(...args);
}
async function getMultiple(...args) {
    if (!_esmGetMultiple) {
        const imported = await import('../../components/documents-store.js');
        _esmGetMultiple = imported.getMultiple;
    }
    return _esmGetMultiple(...args);
}
async function store(...args) {
    if (!_esmStore) {
        const imported = await import('../../components/documents-store.js');
        _esmStore = imported.store;
    }
    return _esmStore(...args);
}
async function remove(...args) {
    if (!_esmRemove) {
        const imported = await import('../../components/documents-store.js');
        _esmRemove = imported.remove;
    }
    return _esmRemove(...args);
}
async function count(...args) {
    if (!_esmCount) {
        const imported = await import('../../components/documents-store.js');
        _esmCount = imported.count;
    }
    return _esmCount(...args);
}
async function load(...args) {
    if (!_esmLoad) {
        const imported = await import('../../components/documents-store.js');
        _esmLoad = imported.load;
    }
    return _esmLoad(...args);
}
async function save(...args) {
    if (!_esmSave) {
        const imported = await import('../../components/documents-store.js');
        _esmSave = imported.save;
    }
    return _esmSave(...args);
}
async function createDocumentsStore(...args) {
    if (!_esmCreateDocumentsStore) {
        const imported = await import('../../components/documents-store.js');
        _esmCreateDocumentsStore = imported.createDocumentsStore;
    }
    return _esmCreateDocumentsStore(...args);
}

//# sourceMappingURL=documents-store.js.map