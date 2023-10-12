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

function d_manhattan(grid: States[][], node1: [number, number], node2: [number, number]) {
    let m = manhattan(node1, node2);

    let neighbors: [number, number][] = getNeighbors(grid, node1);
    let penalty = neighbors.length;
    for (const node of neighbors) {
        if (grid[node[0]][node[1]] !== "red" && grid[node[0]][node[1]] !== "green") {
            penalty--;
        }
    }

    return m - penalty;
}

function manhattan(node1: [number, number], node2: [number, number]) {
    let [y1, x1] = node1;
    let [y2, x2] = node2;

    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}

export function heuristic(type: string, grid: States[][], start: [number, number], end: [number, number]) {
    switch(type) {
        case "d_manhattan":
            return d_manhattan(grid, start, end);
        case "manhattan":
            return manhattan(start, end);
        default:
            return manhattan(start, end);
    }
}

export function getUnvisitedNodes(grid: States[][], start: [number, number]) {
    let queue = new Queue();
    let queuehash: [number, number][] = [start];
    queue.enqueue(start);

    while (!queue.isEmpty) {
        let current: [number, number] = queue.dequeue() as [number, number];

        for (const neighbor of getNeighbors(grid, current)) {
            if (!queuehash.some(node => {
                return node[0] === neighbor[0] && node[1] === neighbor[1];
            })) {
                queue.enqueue(neighbor);
                queuehash.push(neighbor);
            }
        }
    }

    return queuehash;
}

export function containsPos(list: [number, number][], target: [number, number]) {
    return list.some((pos) => {
        return pos[0] === target[0] && pos[1] === target[1];
    })
}

export function findPos(list: [number, number][], target: [number, number]) {
    let index = -1;
    for (const [i, node] of list.entries()) {
        if (node[0] === target[0] && node[1] === target[1]) {
            index = i;
            break;
        }
    }
    return index;
}

export function genKey(node: [number, number]) {
    return `${node[0]}-${node[1]}`;
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
    private items: QElement[];

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

    p_dequeue() {
        if (this.isEmpty()) {
            return;
        }

        const element = this.items.shift();

        return [element?.priority, element?.element];
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

class Queue<T> {
    private elements: { [key: number]: T };
    private head: number;
    private tail: number;

    constructor() {
        this.elements = {};
        this.head = 0;
        this.tail = 0;
    }

    enqueue(element: T): void {
        this.elements[this.tail] = element;
        this.tail++;
    }

    dequeue(): T | undefined {
        const item = this.elements[this.head];
        delete this.elements[this.head];
        this.head++;
        return item;
    }

    peek(): T | undefined {
        return this.elements[this.head];
    }

    get length(): number {
        return this.tail - this.head;
    }

    get isEmpty(): boolean {
        return this.length === 0;
    }
}
