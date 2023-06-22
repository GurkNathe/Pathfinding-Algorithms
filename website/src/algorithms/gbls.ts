import { Interests, States } from "../components/Panel"
import { PriorityQueue, getNeighbors, heuristic, reconstructPath } from "./helper";

export default function gbls(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let queue: PriorityQueue = new PriorityQueue();
    queue.enqueue(endPoints.start, heuristic("manhattan", grid, endPoints.start, endPoints.end), 0);

    let count: number = 0;
    let found: boolean = false;

    let previous: any = {};
    let lastdir: [number, number] = [-1, -1];

    while (!queue.isEmpty() && !found) {
        let [y, x] = queue.dequeue();

        if (grid[y][x] === "red") {
            continue;
        }

        if (grid[y][x] !== "orange" && grid[y][x] !== "blue") {
            grid[y][x] = "red";
        }

        let neighbors: [number, number][] = getNeighbors(grid, [y,x]);

        if (lastdir[0] !== -1) {
            let tempNeighbors = neighbors.filter((n) => (n[0] - y === lastdir[0]) && (n[1] - x === lastdir[1]));
            for (const n of neighbors) {
                let i = tempNeighbors.findIndex(item => item[0] === n[0] && item[1] === n[1]);
                if (i === -1) {
                    tempNeighbors.push(n);
                }
            }
            neighbors = tempNeighbors;
        }

        for (const neighbor of neighbors) {
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

                lastdir = [ny - y, nx - x];
            }
        }

        setGrid(grid);
    }
}