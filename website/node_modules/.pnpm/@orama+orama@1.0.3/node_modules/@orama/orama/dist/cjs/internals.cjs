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
    boundedLevenshtein: ()=>boundedLevenshtein,
    formatBytes: ()=>formatBytes,
    formatNanoseconds: ()=>formatNanoseconds,
    getNanosecondsTime: ()=>getNanosecondsTime,
    uniqueId: ()=>uniqueId
});
let _esmBoundedLevenshtein;
let _esmFormatBytes;
let _esmFormatNanoseconds;
let _esmGetNanosecondsTime;
let _esmUniqueId;
async function boundedLevenshtein(...args) {
    if (!_esmBoundedLevenshtein) {
        const imported = await import('../internals.js');
        _esmBoundedLevenshtein = imported.boundedLevenshtein;
    }
    return _esmBoundedLevenshtein(...args);
}
async function formatBytes(...args) {
    if (!_esmFormatBytes) {
        const imported = await import('../internals.js');
        _esmFormatBytes = imported.formatBytes;
    }
    return _esmFormatBytes(...args);
}
async function formatNanoseconds(...args) {
    if (!_esmFormatNanoseconds) {
        const imported = await import('../internals.js');
        _esmFormatNanoseconds = imported.formatNanoseconds;
    }
    return _esmFormatNanoseconds(...args);
}
async function getNanosecondsTime(...args) {
    if (!_esmGetNanosecondsTime) {
        const imported = await import('../internals.js');
        _esmGetNanosecondsTime = imported.getNanosecondsTime;
    }
    return _esmGetNanosecondsTime(...args);
}
async function uniqueId(...args) {
    if (!_esmUniqueId) {
        const imported = await import('../internals.js');
        _esmUniqueId = imported.uniqueId;
    }
    return _esmUniqueId(...args);
}

//# sourceMappingURL=internals.js.map