import { Interests, States } from "../components/Panel"
import { genKey, getNeighbors, heuristic } from "./helper";

function reconstructPath(grid: States[][], path: any, current: [number, number])  {
    while (path.hasOwnProperty(`${current[0]}-${current[1]}`)) {
        if (grid[current[0]][current[1]] !== "orange") {
            current = path[`${current[0]}-${current[1]}`][1]
            if (grid[current[0]][current[1]] !== "orange") {
                grid[current[0]][current[1]] = "purple";
            }
        } else {
            break;
        }
    }
}

export default function fringe(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid = [...colorGrid];
    
    let fringe = [endPoints.start];
    let cache : any = {};
    cache[genKey(endPoints.start)] = [0, null];

    let f_limit = heuristic("manhattan", grid, endPoints.start, endPoints.end);

    let found = false;

    while (!found && fringe.length > 0) {
        let f_min = Infinity;

        for (let node of fringe) {
            let g = cache[genKey(node)][0];

            let f = g + heuristic("manhattan", grid, node, endPoints.end);

            if (f > f_limit) {
                f_min = Math.min(f, f_min);
                continue;
            }
            if (grid[node[0]][node[1]] === "blue") {
                reconstructPath(grid, cache, node);
                found = true;
                break;
            }

            if (!(grid[node[0]][node[1]] === "orange")) {
                grid[node[0]][node[1]] = "red";
            }

            for (let neighbor of getNeighbors(grid, node)) {
                let g_neighbor = g + 1;

                if (Object.keys(cache).includes(genKey(neighbor))) {
                    let g_cache = cache[genKey(neighbor)][0];

                    if (g_neighbor >= g_cache) {
                        continue;
                    }
                }

                if (fringe.some(a => a.every((val, i) => val === neighbor[i]))) {
                    fringe = fringe.filter(a => !(a.every((val, i) => val === neighbor[i])));
                }

                fringe.push(neighbor);

                cache[genKey(neighbor)] = [g_neighbor, node];

                if (!(grid[neighbor[0]][neighbor[1]] === "orange" || grid[neighbor[0]][neighbor[1]] === "blue")) {
                    grid[neighbor[0]][neighbor[1]] = "green";
                }
            }
            fringe = fringe.filter(a => !(a.every((val, i) => val === node[i])));
        }
        f_limit = f_min;
        setGrid(grid);
    }
}