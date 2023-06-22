export function intersectFilteredIDs(filtered, lookedUp) {
    const map = new Map();
    const result = [];
    for (const id of filtered){
        map.set(id, true);
    }
    for (const [id, score] of lookedUp){
        if (map.has(id)) {
            result.push([
                id,
                score
            ]);
            map.delete(id);
        }
    }
    return result;
}

//# sourceMappingURL=filters.js.map