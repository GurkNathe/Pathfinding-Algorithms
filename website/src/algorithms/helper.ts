import { States } from "../components/Panel";

export function getNeighbors(grid: States[][], pos: [number, number]) {
    let [i, j] = pos;

    let neighbors : [number, number][] = [];

    if (i - 1 >= 0 && grid[i - 1][j] !== "black") {
        neighbors.push([i - 1, j]);
    }
    if (j - 1 >= 0 && grid[i][j - 1] !== "black") {
        neighbors.push([i, j - 1]);
    }
    if (i + 1 < grid.length && grid[i + 1][j] !== "black") {
        neighbors.push([i + 1, j]);
    }
    if (j + 1 < grid[0].length && grid[i][j + 1] !== "black") {
        neighbors.push([i, j + 1]);
    }

    return neighbors;
}

export function reconstructPath(grid: States[][], path: any, current: [number, number])  {
    while (path.hasOwnProperty(`${current[0]}-${current[1]}`)) {
        if (grid[current[0]][current[1]] !== "orange") {
            current = path[`${current[0]}-${current[1]}`]
            if (grid[current[0]][current[1]] !== "orange") {
                grid[current[0]][current[1]] = "purple";
            }
        } else {
            break;
        }
    }
}

function manhattan(grid: States[][], node1: [number, number], node2: [number, number]) {
    let [y1, x1] = node1;
    let [y2, x2] = node2;

    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}

export function heuristic(type: string, grid: States[][], start: [number, number], end: [number, number]) {
    switch(type) {
        case "manhattan":
            return manhattan(grid, start, end);
        default:
            return manhattan(grid, start, end);
    }
}

class QElement {
    element: any;
    priority: number;
    count: number;

    constructor(element : any, priority: number, count: number) {
        this.element = element;
        this.priority = priority;
        this.count = count;
    }
}

export class PriorityQueue {
    items: QElement[];

    constructor() {
        this.items = [];
    }

    size() {
        return this.items.length;
    }

    resize(size: number) {
        this.items = this.items.slice(0, size);
    }

    contains(element: [number, number]) {
        return this.items.some((item) => {
            return JSON.stringify(item.element) === JSON.stringify(element);
        });
    }

    enqueue(element: [number, number], priority: number, count: number) {
        const qElement = new QElement(element, priority, count);
        let contain = false;

        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].priority > qElement.priority) {
                this.items.splice(i, 0, qElement);
                contain = true;
                break;
            } else if (this.items[i].priority === qElement.priority) {
                if (this.items[i].count < qElement.count) {
                    this.items.splice(i + 1, 0, qElement);
                } else {
                    this.items.splice(i, 0, qElement);
                }
                contain = true;
                break;
            }
        }

        if (!contain) {
            this.items.push(qElement);
        }
    }

    dequeue() {
        if (this.isEmpty()) {
            return;
        }

        return this.items.shift()!.element;
    }

    isEmpty() {
        return this.items.length === 0;
    }
}