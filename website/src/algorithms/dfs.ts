import { Interests, States } from "../components/Panel"
import { getNeighbors, reconstructPath } from "./helper";

export default function dfs(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let stack: [number, number][] = [];
    let previous : any = {};

    stack.push(endPoints.start);
    
    let found: boolean = false;
    
    while (stack.length > 0 && !found) {
        let [y, x] = stack.pop()!;

        if (grid[y][x] === "red") {
            continue;
        }

        if (grid[y][x] !== "orange") {
            grid[y][x] = "red";
        }

        for (const neighbor of getNeighbors(grid, [y, x])) {
            let [ny, nx] = neighbor;
            if (grid[ny][nx] !== "red") {
                if (grid[ny][nx] === "blue") {
                    previous[`${ny}-${nx}`] = [y,x];
                    found = true;
                    reconstructPath(grid, previous, endPoints.end);
                    break;
                } else {
                    previous[`${ny}-${nx}`] = [y,x];
                    stack.push(neighbor);

                    if (grid[ny][nx] !== "orange") {
                        grid[ny][nx] = "green"
                    }
                }
            }
        }
        setGrid(grid)
    }
}