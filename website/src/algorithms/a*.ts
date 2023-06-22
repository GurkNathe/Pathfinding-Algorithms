import { Interests, States } from "../components/Panel"
import { PriorityQueue, getNeighbors, heuristic, reconstructPath } from "./helper";

export default function astar(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid = [...colorGrid];
    let count: number = 0;
    let openSet: PriorityQueue = new PriorityQueue();
    openSet.enqueue(endPoints.start, 0, count);
    let previous : any = {};

    let gscore : any = {};
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            gscore[`${i}-${j}`] = Infinity;
        }
    }
    gscore[`${endPoints.start[0]}-${endPoints.start[1]}`] = 0;

    while (!openSet.isEmpty()) {
        let [y, x] = openSet.dequeue();
        
        if (grid[y][x] === "blue") {
            reconstructPath(grid, previous, [y, x]);
            break;
        }

        let temp_gscore = gscore[`${y}-${x}`] + 1;
        for (const neighbor of getNeighbors(grid, [y, x])) {
            let [ny, nx] = neighbor;

            if (temp_gscore < gscore[`${ny}-${nx}`]) {
                previous[`${ny}-${nx}`] = [y, x];
                gscore[`${ny}-${nx}`] = temp_gscore;

                if (!openSet.contains([ny, nx])) {
                    let fscore = temp_gscore + heuristic("manhattan", grid, neighbor, endPoints.end); // + heuristic
                    count++;
                    openSet.enqueue(neighbor, fscore, count);
                    if (!(grid[ny][nx] === "orange" || grid[ny][nx] === "blue")) {
                        grid[ny][nx] = "green";
                    }
                }
            }

        }

        if (grid[y][x] !== "orange") {
            grid[y][x] = "red";
        }

        setGrid(grid);
    }

}