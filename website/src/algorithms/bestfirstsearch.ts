import { Interests, States } from "../components/Panel"
import { PriorityQueue, genKey, getNeighbors, heuristic } from "./helper";

export default function bestfirstsearch(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let queue = new PriorityQueue();
    let count = 0;
    let costs: any = {};

    const getChecked = (grid: States[][], node: [number, number]) => {
        let list: [number, number][] = [];
        for (const neighbor of getNeighbors(grid, node)) {
            let [ny, nx] = neighbor;
            if (grid[ny][nx] === "red" || grid[ny][nx] === "orange") {
                list.push(neighbor);
            }
        }
        return list;
    }

    const reconstructPath = (grid: States[][], costs: any, current: [number, number]) => {
        while (grid[current[0]][current[1]] !== "orange") {
            current = getChecked(grid, current).reduce((min, key) => {
                if (costs[genKey(key)] < costs[genKey(min)]) {
                    return key;
                }
                return min;
            });

            if (grid[current[0]][current[1]] === "orange") {
                break;
            }

            grid[current[0]][current[1]] = "purple";
        }
    }

    costs[genKey(endPoints.start)] = 0;
    queue.enqueue(endPoints.start, 0, 0);

    while (!queue.isEmpty()) {
        let [y, x] = queue.dequeue();

        let color = grid[y][x];

        if (color === "blue") {
            reconstructPath(grid, costs, endPoints.end);
            break;
        }

        if (color !== "orange") {
            grid[y][x] = "red";
        }

        for (const neighbor of getNeighbors(grid, [y,x])) {
            let [ny, nx] = neighbor;
            let cost = costs[`${y}-${x}`] + 1;

            if (!Object.keys(costs).includes(`${ny}-${nx}`) || cost < costs[`${ny}-${nx}`]) {
                costs[`${ny}-${nx}`] = cost;
                count++;
                queue.enqueue(neighbor, cost + heuristic("manhattan", grid, neighbor, endPoints.end), count);

                if (grid[ny][nx] !== "orange" && grid[ny][nx] !== "blue") {
                    grid[ny][nx] = "green";
                }
            }
        }

        setGrid(grid);
    }
}