import { Interests, States } from "../components/Panel";
import { PriorityQueue, getNeighbors, heuristic, reconstructPath } from "./helper";

export default function gbfs(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let queue: PriorityQueue = new PriorityQueue();
    queue.enqueue(endPoints.start, heuristic("manhattan", grid, endPoints.start, endPoints.end), 0);

    let count: number = 0;
    let found: boolean = false;

    let previous: any = {};

    while (!queue.isEmpty() && !found) {
        let [y, x] = queue.dequeue();

        if (grid[y][x] === "red") {
            continue;
        }

        if (grid[y][x] !== "orange" && grid[y][x] !== "blue") {
            grid[y][x] = "red";
        }

        for (const neighbor of getNeighbors(grid, [y,x])) {
            let [ny, nx] = neighbor;
            if (grid[ny][nx] !== "red") {
                if (grid[ny][nx] === "blue") {
                    previous[`${ny}-${nx}`] = [y, x];
                    found = true;
                    reconstructPath(grid, previous, endPoints.end);
                    break;
                }
                
                if (grid[ny][nx] !== "orange") {
                    grid[ny][nx] = "green";
                }
                
                count++;
                let distance: number = heuristic("manhattan", grid, neighbor, endPoints.end);
                
                previous[`${ny}-${nx}`] = [y, x];
                queue.enqueue(neighbor, distance, count);
            }
        }

        setGrid(grid);
    }
}