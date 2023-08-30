import { Interests, States } from "../components/Panel";
import { PriorityQueue, getNeighbors, reconstructPath } from "./helper";

export default function fmm(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid = [...colorGrid];

    let costs : any = {};
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            costs[`${i}-${j}`] = Infinity;
        }
    }
    costs[`${endPoints.start[0]}-${endPoints.start[1]}`] = 0;

    let far : any = [];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] !== "black" && grid[i][j] !== "orange") {
                far.push([i, j]);
            }
        }
    }

    let considered: PriorityQueue = new PriorityQueue();
    considered.enqueue(endPoints.start, 0, 0);

    let previous : any = {};

    while (!considered.isEmpty()) {
        let item = considered.p_dequeue();

        let ccost : number = item![0];
        let [y, x] : [number, number] = item![1];

        if (grid[y][x] === "blue") {
            reconstructPath(grid, previous, [y, x]);
            break;
        }

        if (grid[y][x] !== "orange") {
            grid[y][x] = "red";
        }

        for (const neighbor of getNeighbors(grid, [y, x])) {
            let [ny, nx] = neighbor;

            if (!considered.contains([y, x]) && grid[ny][nx] !== "red") {
                let cost : number = ccost + 1;

                if (cost < costs[`${ny}-${nx}`]) {
                    costs[`${ny}-${nx}`] = cost;
                    previous[`${ny}-${nx}`] = [y, x];

                    if (!!far.find((i : [number, number]) => i[0] === ny && i[1] === nx)) {
                        considered.enqueue(neighbor, cost, 0);
                        const index = far.findIndex((i : [number, number]) => i[0] === ny && i[1] === nx);

                        if (index > -1) {
                            far.splice(index, 1);
                        }

                        if (grid[ny][nx] !== "orange" && grid[ny][nx] !== "blue") {
                            grid[ny][nx] = "green";
                        }
                    }
                }
            }
        }
        setGrid(grid);
    }
}