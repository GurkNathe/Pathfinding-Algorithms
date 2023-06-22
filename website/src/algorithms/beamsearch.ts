import { Interests, States } from "../components/Panel"
import { PriorityQueue, getNeighbors, heuristic, reconstructPath } from "./helper";

export default function beamsearch(colorGrid: States[][], setGrid: React.Dispatch<React.SetStateAction<States[][]>>, endPoints: Interests) {
    let grid: States[][] = [...colorGrid];
    let beam = new PriorityQueue();
    let beamsize = 50;
    beam.enqueue(endPoints.start, 0, 0);

    let previous: any = {};
    previous[`${endPoints.start[0]}-${endPoints.start[1]}`] = endPoints.start;

    while (beam.size() > 0) {
        let [y, x] = beam.dequeue();

        if (grid[y][x] === "blue") {
            reconstructPath(grid, previous, [y, x]);
            break;
        }

        if (grid[y][x] !== "orange") {
            grid[y][x] = "red";
        }

        let children = getNeighbors(grid, [y, x]);
        children = children.filter((e) => {
            return !(e[0] === previous[`${y}-${x}`][0] && e[1] === previous[`${y}-${x}`][1]);
        })

        for (const child of children) {
            let [cy, cx] = child;

            if (grid[cy][cx] !== "red") {
                previous[`${cy}-${cx}`] = [y, x];
                beam.enqueue(child, heuristic("manhattan", grid, child, endPoints.end), 0);

                if (grid[cy][cx] !== "orange" && grid[cy][cx] !== "blue") {
                    grid[cy][cx] = "green";
                }
            }
        }

        beam.resize(beamsize)
    }
}