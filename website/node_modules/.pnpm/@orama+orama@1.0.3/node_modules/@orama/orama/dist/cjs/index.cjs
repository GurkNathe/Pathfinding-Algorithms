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
    count: ()=>count,
    create: ()=>create,
    getByID: ()=>getByID,
    insert: ()=>insert,
    insertMultiple: ()=>insertMultiple,
    load: ()=>load,
    remove: ()=>remove,
    removeMultiple: ()=>removeMultiple,
    save: ()=>save,
    search: ()=>search,
    update: ()=>update,
    updateMultiple: ()=>updateMultiple,
    components: ()=>_defaultsCjs,
    internals: ()=>_internalsCjs
});
const _defaultsCjs = /*#__PURE__*/ _interopRequireWildcard(require("./components/defaults.cjs"));
const _internalsCjs = /*#__PURE__*/ _interopRequireWildcard(require("./internals.cjs"));
function _getRequireWildcardCache(nodeInterop) {
    if (typeof WeakMap !== "function") return null;
    var cacheBabelInterop = new WeakMap();
    var cacheNodeInterop = new WeakMap();
    return (_getRequireWildcardCache = function(nodeInterop) {
        return nodeInterop ? cacheNodeInterop : cacheBabelInterop;
    })(nodeInterop);
}
function _interopRequireWildcard(obj, nodeInterop) {
    if (!nodeInterop && obj && obj.__esModule) {
        return obj;
    }
    if (obj === null || typeof obj !== "object" && typeof obj !== "function") {
        return {
            default: obj
        };
    }
    var cache = _getRequireWildcardCache(nodeInterop);
    if (cache && cache.has(obj)) {
        return cache.get(obj);
    }
    var newObj = {};
    var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor;
    for(var key in obj){
        if (key !== "default" && Object.prototype.hasOwnProperty.call(obj, key)) {
            var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null;
            if (desc && (desc.get || desc.set)) {
                Object.defineProperty(newObj, key, desc);
            } else {
                newObj[key] = obj[key];
            }
        }
    }
    newObj.default = obj;
    if (cache) {
        cache.set(obj, newObj);
    }
    return newObj;
}
let _esmCount;
let _esmCreate;
let _esmGetByID;
let _esmInsert;
let _esmInsertMultiple;
let _esmLoad;
let _esmRemove;
let _esmRemoveMultiple;
let _esmSave;
let _esmSearch;
let _esmUpdate;
let _esmUpdateMultiple;
async function count(...args) {
    if (!_esmCount) {
        const imported = await import('../methods/docs.js');
        _esmCount = imported.count;
    }
    return _esmCount(...args);
}
async function create(...args) {
    if (!_esmCreate) {
        const imported = await import('../methods/create.js');
        _esmCreate = imported.create;
    }
    return _esmCreate(...args);
}
async function getByID(...args) {
    if (!_esmGetByID) {
        const imported = await import('../methods/docs.js');
        _esmGetByID = imported.getByID;
    }
    return _esmGetByID(...args);
}
async function insert(...args) {
    if (!_esmInsert) {
        const imported = await import('../methods/insert.js');
        _esmInsert = imported.insert;
    }
    return _esmInsert(...args);
}
async function insertMultiple(...args) {
    if (!_esmInsertMultiple) {
        const imported = await import('../methods/insert.js');
        _esmInsertMultiple = imported.insertMultiple;
    }
    return _esmInsertMultiple(...args);
}
async function load(...args) {
    if (!_esmLoad) {
        const imported = await import('../methods/serialization.js');
        _esmLoad = imported.load;
    }
    return _esmLoad(...args);
}
async function remove(...args) {
    if (!_esmRemove) {
        const imported = await import('../methods/remove.js');
        _esmRemove = imported.remove;
    }
    return _esmRemove(...args);
}
async function removeMultiple(...args) {
    if (!_esmRemoveMultiple) {
        const imported = await import('../methods/remove.js');
        _esmRemoveMultiple = imported.removeMultiple;
    }
    return _esmRemoveMultiple(...args);
}
async function save(...args) {
    if (!_esmSave) {
        const imported = await import('../methods/serialization.js');
        _esmSave = imported.save;
    }
    return _esmSave(...args);
}
async function search(...args) {
    if (!_esmSearch) {
        const imported = await import('../methods/search.js');
        _esmSearch = imported.search;
    }
    return _esmSearch(...args);
}
async function update(...args) {
    if (!_esmUpdate) {
        const imported = await import('../methods/update.js');
        _esmUpdate = imported.update;
    }
    return _esmUpdate(...args);
}
async function updateMultiple(...args) {
    if (!_esmUpdateMultiple) {
        const imported = await import('../methods/update.js');
        _esmUpdateMultiple = imported.updateMultiple;
    }
    return _esmUpdateMultiple(...args);
}

//# sourceMappingURL=index.js.map