import { Interests, States } from "../components/Panel"
import { containsPos, getNeighbors, getUnvisitedNodes, findPos } from "./helper";

export default function floydwarshall(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let nodes: [number, number][] = getUnvisitedNodes(grid, endPoints.start);
    let V: number = nodes.length;

    const reconstructPath = (grid: States[][], nodes: [number, number][], distances: number[][]) => {
        let [u, v] = [findPos(nodes, endPoints.start), findPos(nodes, endPoints.end)];

        let path: [number, number][] = [];
        let left: number[] = [];
        let right: number[] = [];
        let current: number = v;

        for (let k = V - 1; k >= 0; k--) {
            if (distances[u][v] === distances[u][k] + distances[k][v]) {
                if (grid[nodes[k][0]][nodes[k][1]] !== "orange" &&
                    grid[nodes[k][0]][nodes[k][1]] !== "blue" &&
                    !left.includes(distances[u][k]) &&
                    !right.includes(distances[k][v])) {
                    path.push(nodes[k]);
                    left.push(distances[u][k]);
                    right.push(distances[k][v]);
                }
                current = k;
            }
        }

        let curr: [number, number] = endPoints.end;

        while (grid[curr[0]][curr[1]] !== "orange") {
            for (const node of getNeighbors(grid, curr)) {
                let [ny, nx] = node;

                if (grid[ny][nx] === "orange") {
                    curr = endPoints.start;
                    break;
                }

                if (containsPos(path, node)) {
                    grid[ny][nx] = "purple";
                    path = path.filter((val) => {
                        return !(val[0] === ny && val[1] === nx);
                    });
                    curr = node;
                }
                setGrid(grid);
            }
        }
    }

    let distance: number[][] = [];

    for (let v = 0; v < V; v++) {
        distance[v] = [];
        for (let w = 0; w < V; w++) {
            distance[v][w] = Infinity;
        }
    }

    for (let i = 0; i < V; i++) {
        for (let j = 0; j < V; j++) {
            if (containsPos(getNeighbors(grid, nodes[j]), nodes[i])) {
                distance[i][j] = 1;
            }
        }
    }

    for (let i = 0; i < V; i++) {
        distance[i][i] = 0;
    }

    let checked: [number, number][] = [endPoints.start];

    for (let k = 0; k < V; k++) {
        for (let i = 0; i < V; i++) {
            for (let j = 0; j < V; j++) {
                if (distance[i][j] > distance[i][k] + distance[k][j]) {
                    distance[i][j] = distance[i][k] + distance[k][j];

                    let iCol = grid[nodes[i][0]][nodes[i][1]];
                    let jCol = grid[nodes[j][0]][nodes[j][1]];
                    let kCol = grid[nodes[k][0]][nodes[k][1]];

                    if (iCol !== "orange" && iCol !== "blue" &&
                        jCol !== "orange" && jCol !== "blue" &&
                        kCol !== "orange" && kCol !== "blue") {
                        checked.push(nodes[i]);
                        checked.push(nodes[j]);
                        checked.push(nodes[k]);
                        grid[nodes[i][0]][nodes[i][1]] = "red";
                        grid[nodes[j][0]][nodes[j][1]] = "red";
                        grid[nodes[k][0]][nodes[k][1]] = "red";
                    }
                }

                setGrid(grid);
            }
        }
    }

    if (containsPos(nodes, endPoints.end)) {
        reconstructPath(grid, nodes, distance);
    }
}