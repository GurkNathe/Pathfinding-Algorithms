import { Interests, States } from "../components/Panel"
import { PriorityQueue, getNeighbors } from "./helper";

export default function flood_fill(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid = [...colorGrid];

    let distances : any = {};
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            distances[`${i}-${j}`] = Infinity;
        }
    }
    distances[`${endPoints.end[0]}-${endPoints.end[1]}`] = 0;

    let openSet: PriorityQueue = new PriorityQueue();
    openSet.enqueue(endPoints.end, 0, 0);

    while (!openSet.isEmpty()) {
        let item = openSet.p_dequeue();

        let distance = item![0];
        let [y, x] = item![1];

        if (grid[y][x] === "red") {
            continue;
        }

        if (grid[y][x] === "orange") {
            break;
        }

        if (grid[y][x] !== "blue") {
            grid[y][x] = "red";
        }

        for (const neighbor of getNeighbors(grid, [y, x])) {
            let [ny, nx] = neighbor;

            if (grid[ny][nx] !== "red") {
                distances[`${ny}-${nx}`] = distance + 1;
                openSet.enqueue(neighbor, distance + 1, 0);
                if (!(grid[ny][nx] === "orange" || grid[ny][nx] === "blue")) {
                    grid[ny][nx] = "green";
                }
            }
        }
    }

    if (distances[`${endPoints.start[0]}-${endPoints.start[1]}`] !== Infinity) {
        let current = endPoints.start;
        let found = false;
        let best : [number, [number, number] | undefined] = [Infinity, undefined];
        while (!found) {
            for (const neighbor of getNeighbors(grid, current)) {
                let [ny, nx] = neighbor;
                if (grid[ny][nx] === "blue") {
                    found = true;
                    break;
                }
                if (distances[`${ny}-${nx}`] < best[0]) {
                    best = [distances[`${ny}-${nx}`], neighbor];
                }
            }
            if (!found) {
                let [ny, nx] = best[1]!;
                grid[ny][nx] = "purple";
                current = best[1]!;
            }
        }
    }

    setGrid(grid);
}