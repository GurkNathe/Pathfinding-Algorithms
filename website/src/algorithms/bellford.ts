import { Interests, States } from "../components/Panel"
import { getNeighbors, getUnvisitedNodes, reconstructPath } from "./helper";

export default function bellmanford(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests){
    let grid: States[][] = [...colorGrid];
    let accuracy = 1;

    let nodes: [number, number][] = getUnvisitedNodes(grid, endPoints.start);
    let previous : any = {};
    let distance : any = {};

    for (const node of nodes) {
        distance[`${node[0]}-${node[1]}`] = Infinity;
    }

    distance[`${endPoints.start[0]}-${endPoints.start[1]}`] = 0;

    let counter: number = Math.floor((nodes.length - 1) * accuracy);

    while (counter >= 0) {
        for (const node of nodes) {
            let [y, x] = node;

            let color = grid[y][x];

            if (color !== "orange" && color !== "blue") {
                grid[y][x] = "red";
            }

            for (const neighbor of getNeighbors(grid, node)) {
                let [ny, nx] = neighbor;
                if (distance[`${y}-${x}`] + 1 < distance[`${ny}-${nx}`]) {
                    distance[`${ny}-${nx}`] = distance[`${y}-${x}`] + 1;
                    previous[`${ny}-${nx}`] = node;

                    if (grid[ny][nx] !== "orange" && grid[ny][nx] !== "blue") {
                        grid[ny][nx] = "green";
                    }
                }
            }
        }

        counter--;
        setGrid(grid);
    }

    reconstructPath(grid, previous, endPoints.end);
}