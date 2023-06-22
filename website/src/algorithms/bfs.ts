import { Interests, States } from "../components/Panel"
import { getNeighbors, reconstructPath } from "./helper";

export default function bfs(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid = [...colorGrid];
    let nodes: [number, number][] = [];
    nodes.push(endPoints.start)

    let previous : any = {};

    let found : boolean = false;
    while (nodes.length > 0 && !found) {
        let [i, j] = nodes.shift()!;

        if (grid[i][j] === "red") {
            continue;
        }

        if (grid[i][j] !== "orange") {
            grid[i][j] = "red";
        }

        for (const neighbor of getNeighbors(grid, [i,j])) {
            let [ni, nj] = neighbor;
            let nColor : States = grid[ni][nj];
            if (nColor !== "red") {
                if (nColor === "blue") {
                    previous[`${ni}-${nj}`] = [i,j];
                    found = true;
                    reconstructPath(grid, previous, endPoints.end);
                    break;
                } else {
                    previous[`${ni}-${nj}`] = [i,j];
                    nodes.push(neighbor);
                    
                    if (nColor !== "orange") {
                        grid[ni][nj] = "green";
                    }
                }
            }
        }

        setGrid(grid);
    }
}