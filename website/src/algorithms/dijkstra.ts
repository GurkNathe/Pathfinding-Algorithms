import { Interests, States } from "../components/Panel"
import { PriorityQueue, genKey, getNeighbors, reconstructPath } from "./helper";

export default function dijkstra(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let queue: PriorityQueue = new PriorityQueue();

    let gscore: any = {};
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            gscore[`${i}-${j}`] = Infinity;
        }
    }
    gscore[genKey(endPoints.start)] = 0;

    let previous: any = {};

    queue.enqueue(endPoints.start, 0, 0);

    let count: number = 0

    while(!queue.isEmpty()) {
        let [y, x] = queue.dequeue();

        if (grid[y][x] === "blue") {
            reconstructPath(grid, previous, [y, x]);
            break;
        }

        if (grid[y][x] !== "orange") {
            grid[y][x] = "red";
        }

        for (const neighbor of getNeighbors(grid, [y, x])) {
            let [ny, nx] = neighbor;
            if (grid[ny][nx] !== "red") {
                let temp_gscore = gscore[`${y}-${x}`] + 1;
                
                if (temp_gscore < gscore[`${ny}-${nx}`]) {
                    gscore[`${ny}-${nx}`] = temp_gscore;
                    previous[`${ny}-${nx}`] = [y, x];

                    count++;
                    queue.enqueue(neighbor, temp_gscore, count);

                    if (grid[ny][nx] !== "orange" && grid[ny][nx] !== "blue") {
                        grid[ny][nx] = "green";
                    }
                }
            }
        }

        setGrid(grid);
    }
}