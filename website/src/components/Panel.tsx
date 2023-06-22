import { useEffect, useState } from "react";

import "../css/panel.css"

import astar from "../algorithms/a*";
import beamsearch from "../algorithms/beamsearch";
import bfs from "../algorithms/bfs";
import dfs from "../algorithms/dfs";
import dijkstra from "../algorithms/dijkstra";
import gbls from "../algorithms/gbls";

type Rows = {
    rows: number
    toSubmit: number
}

/**
 * Empty Node: white
 * Obstacle Node: black
 * Closed Node: red
 * Open Node: green
 * Start Node: orange
 * End Node: blue
 * Path Node: purple
 */
export type States = "white" | "black" | "red" | "green" | "orange" | "blue" | "purple";

export type Interests = {
    start: [number, number]
    end: [number, number]
}

export default function Panel() {
    const maxrows = 25;
    const [colorGrid, setColorGrid] = useState<States[][]>([]!);
    const [rows, setRows] = useState<Rows>({rows: maxrows, toSubmit: maxrows});
    const [width, setWidth] = useState<number>(30);
    const [interestPoints, setInterestPoints] = useState<Interests>({start: [-1, -1], end: [-1, -1]})
    const [alg, setAlg] = useState<string>("A*");


    const algorithms: string[] = [
        "A*", 
        "Beam Search",
        // "Bellman-Ford",
        // "Best First Search",
        "BFS", 
        "DFS",
        "Dijkstra",
        // "Floyd-Warshall",
        // "Greedy Best First Search",
        "Greedy Best Line Search",
        // "Iterative Deepening A*",
        // "Iterative Deepening DFS",
        // "Jump Point Search",
        // "Lexicographic BFS",
        // "Lifelong Planning A*",
        // "Random Search",
        // "Theta*",
    ]

    useEffect(() => {
        makeNewGrid(rows.rows);
    }, [rows.rows])

    const makeNewGrid = (rows: number) => {
        let tempColorRows : States[][] = [];

        for (let j = 0; j < rows; j++) {
            let tempColorRow : States[] = []; 
            for (let i = 0; i < rows; i++) {
                tempColorRow.push("white");
            }
            tempColorRows.push(tempColorRow);
        }

        setInterestPoints({start: [-1, -1], end: [-1, -1]});
        setColorGrid([...tempColorRows])
    }

    const changeRows = (newRows: string) => {
        if (isNaN(Number(newRows))) return;
        setRows({rows: rows.rows, toSubmit: Number(newRows) > maxrows ? maxrows : Number(newRows)})
    }

    const draw = (i: number, j: number, color: States, ctrl: boolean, button: boolean, event: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
        if (!button) {
            return;
        }

        setColorGrid((prev) => {
            const newColorGrid = [...prev];

            let newColor : States = 
                ctrl ? "white" : 
                interestPoints.start[0] === -1 ? "orange" :
                interestPoints.end[0] === -1 ? "blue" :
                color !== "orange" && color !== "blue" ? "black" : color;

            let newInterest : Interests = {...interestPoints};
            if (newColor === "orange") {
                newInterest.start = [i, j];
            } else if (newColor === "blue") {
                newInterest.end = [i, j];
            } else if (newColor === "white") {
                if (newInterest.start[0] === i && newInterest.start[1] === j) {
                    newInterest.start = [-1, -1];
                }else if (newInterest.end[0] === i && newInterest.end[1] === j) {
                    newInterest.end = [-1, -1];
                }
            }

            setInterestPoints(newInterest);

            newColorGrid[i][j] = newColor;

            return newColorGrid;
        })
    }

    const deleteWalls = (walls : [number, number][], selectedWall: [number, number]) => {
        return walls.filter(wall => {
            return !(wall[0] === selectedWall[0] && wall[1] === selectedWall[1]);
        });
    }

    const surroundingCells = (grid: States[][], y: number, x: number) => {
        let cells = 0;
        if (grid[y - 1][x] === "green") {
            cells++;
        }
        if (grid[y + 1][x] === "green") {
            cells++;
        }
        if (grid[y][x - 1] === "green") {
            cells++;
        }
        if (grid[y][x + 1] === "green") {
            cells++;
        }
        return cells;
    }
    
    const checkUp = (grid: States[][], walls: [number, number][], ry: number, rx: number) => {
        if (ry !== 0) {
            if (!(grid[ry - 1][rx] === "green")) {
                grid[ry - 1][rx] = "black";
            }
            if (!(walls.some(loc => loc[0] === ry - 1 && loc[1] === rx))) {
                walls.push([ry - 1, rx]);
            }
        }
    }

    const checkDown = (grid: States[][], walls: [number, number][], ry: number, rx: number, height: number) => {
        if (ry !== height - 1) {
            if (!(grid[ry + 1][rx] === "green")) {
                grid[ry + 1][rx] = "black";
            }
            if (!(walls.some(loc => loc[0] === ry + 1 && loc[1] === rx))) {
                walls.push([ry + 1, rx]);
            }
        }
    }

    const checkLeft = (grid: States[][], walls: [number, number][], ry: number, rx: number) => {
        if (rx !== 0) {
            if (!(grid[ry][rx - 1] === "green")) {
                grid[ry][rx - 1] = "black";
            }
            if (!(walls.some(loc => loc[0] === ry && loc[1] === rx - 1))) {
                walls.push([ry, rx - 1]);
            }
        }
    }

    const checkRight = (grid: States[][], walls: [number, number][], ry: number, rx: number, width: number) => {
        if (rx !== width - 1) {
            if (grid[ry][rx + 1] === "green") {

            }
            if (!(walls.some(loc => loc[0] === ry && loc[1] === rx + 1))) {
                walls.push([ry, rx + 1]);
            }
        }
    }

    const checkBorders = (dirs: string, grid: States[][], walls: [number,number][], ry: number, rx: number, width: number, height: number, selectedWall: [number, number]) => {
        let cells = surroundingCells(grid, ry, rx);
        if (cells < 2) {
            grid[ry][rx] = "green";

            if (dirs.includes("u")) {
                checkUp(grid, walls, ry, rx);
            }
            if (dirs.includes("d")) {
                checkDown(grid, walls, ry, rx, height);
            }
            if (dirs.includes("l")) {
                checkLeft(grid, walls, ry, rx);
            }
            if (dirs.includes("r")) {
                checkRight(grid, walls, ry, rx, width);
            }
        }

        return deleteWalls(walls, selectedWall);
    }

    const genMaze = () => {
        let grid : States[][] = [];

        for (let j = 0; j < rows.rows; j++) {
            let tempColorRow : States[] = []; 
            for (let i = 0; i < rows.rows; i++) {
                tempColorRow.push("white");
            }
            grid.push(tempColorRow);
        }

        let height = grid.length;
        let width = grid[0].length;

        let start_height = Math.floor(Math.random() * (height - 2) + 1);
        let start_width = Math.floor(Math.random() * (width - 2) + 1);

        let walls : [number, number][] = [];

        grid[start_height][start_width] = "green";

        walls.push([start_height - 1, start_width])
        walls.push([start_height, start_width - 1])
        walls.push([start_height, start_width + 1])
        walls.push([start_height + 1, start_width])

        for (const node of walls) {
            grid[node[0]][node[1]] = "black";
        }

        while (walls.length > 0) {
            let randWall : [number, number] = walls[Math.floor(Math.random() * walls.length + 1) - 1];
            let [ry, rx] = randWall;
            
            if (rx !== 0) {
                if (grid[ry][rx - 1] === "white" && grid[ry][rx + 1] === "green") {
                    walls = checkBorders("udl", grid, walls, ry, rx, width, height, randWall);
                    continue;
                }
            }
            if (ry !== 0) {
                if (grid[ry - 1][rx] === "white" && grid[ry + 1][rx] === "green") {
                    walls = checkBorders("ulr", grid, walls, ry, rx, width, height, randWall);
                    continue;
                }
            }
            if (ry !== height - 1) {
                if (grid[ry + 1][rx] === "white" && grid[ry - 1][rx] === "green") {
                    walls = checkBorders("dlr", grid, walls, ry, rx, width, height, randWall);
                    continue;
                }
            }
            if (rx !== width - 1) {
                if (grid[ry][rx + 1] === "white" && grid[ry][rx - 1] === "green") {
                    walls = checkBorders("udr", grid, walls, ry, rx, width, height, randWall);
                    continue;
                }
            }

            walls = deleteWalls(walls, randWall);
        }

        for (let i = 0; i < grid.length; i++) {
            for (let j = 0; j < grid[0].length; j++) {
                if (grid[i][j] === "white") {
                    grid[i][j] = "black";
                }
            }
        }

        let newInterests: Interests = { start: [-1, -1], end: [-1, -1]};

        while (true) {
            let node = Math.floor(Math.random() * (height - 1) + 1)

            if (grid[node][1] === "green") {
                newInterests.start = [node, 0];
                grid[node][0] = "orange";
                break;
            }
        }

        while (true) {
            let node = Math.floor(Math.random() * (height - 1) + 1)

            if (grid[node][width - 2] === "green") {
                newInterests.end = [node, width - 1];
                grid[node][width - 1] = "blue";
                break;
            }
        }

        for (let i = 0; i < grid.length; i++) {
            for (let j = 0; j < grid[0].length; j++) {
                if (grid[i][j] === "green") {
                    grid[i][j] = "white";
                }
            }
        }

        setInterestPoints(newInterests);
        setColorGrid(grid);
    }

    const removeMarkup = () => {
        let tempGrid: States[][] = [...colorGrid];
        for (let j = 0; j < rows.rows; j++) {
            for (let i = 0; i < rows.rows; i++) {
                if (tempGrid[j][i] === "red" || 
                    tempGrid[j][i] === "green" ||
                    tempGrid[j][i] === "purple") {
                    tempGrid[j][i] = "white";
                }
            }
        }

        setColorGrid(tempGrid);
    }

    const run = () => {
        if (interestPoints.start[0] === -1 || interestPoints.end[0] === -1) return;

        removeMarkup();

        switch(alg) {
            case "A*":
                astar(colorGrid, setColorGrid, interestPoints);
                break;
            case "Beam Search":
                beamsearch(colorGrid, setColorGrid, interestPoints);
                break;
            case "BFS":
                bfs(colorGrid, setColorGrid, interestPoints);
                break;
            case "DFS":
                dfs(colorGrid, setColorGrid, interestPoints);
                break;
            case "Dijkstra":
                dijkstra(colorGrid, setColorGrid, interestPoints);
                break;
            case "Greedy Best Line Search":
                gbls(colorGrid, setColorGrid, interestPoints);
                break;
            default:
                astar(colorGrid, setColorGrid, interestPoints);
                break;
        }
    }

    return(
        <div className="panel">
            <div className="options">
                <div>
                    <span>Rows: </span>
                    <input 
                        value={rows.toSubmit} 
                        type="number"
                        onChange={(event) => changeRows(event.target.value)}
                        onKeyDown={(event) => {
                            if (event.key === "Enter") {
                                setRows({rows: rows.toSubmit, toSubmit: rows.toSubmit})
                                makeNewGrid(rows.toSubmit)
                            }
                        }}
                    />
                </div>
                <div>
                    <span>Cell Width: </span>
                    <input 
                        value={width} 
                        type="number"
                        onChange={(event) => setWidth(Number(event.target.value))}
                        onKeyDown={(event) => {
                            if (event.key === "Enter") {
                                setRows({rows: rows.toSubmit, toSubmit: rows.toSubmit})
                                makeNewGrid(rows.toSubmit)
                            }
                        }}
                    />
                </div>
                <div>
                    <span>Algorithm: </span>
                    <select onChange={(event) => setAlg(event.target.value)}>
                        {algorithms.map((func, index) => {
                            return <option value={func} key={index}>{func}</option>
                        })}
                    </select>
                </div>
                <button onClick={() => {
                    makeNewGrid(rows.rows)
                    genMaze()
                }}>
                    Generate Maze
                </button>
                <button onClick={() => makeNewGrid(rows.rows)}>Clear Grid</button>
                <button onClick={() => removeMarkup()}>Clear Markup</button>
                <button onClick={() => run()}>Run</button>
            </div>
            <div className="grid" onDragStart={(e)=>e.preventDefault()} onDrop={(e)=>e.preventDefault()}>
                <div style={{ display: 'grid', gridTemplateColumns: `repeat(${rows.rows}, 1fr)` }}>
                    {colorGrid?.map((colors, i) => {
                        return colors.map((color, j) => {
                            return (
                                <div
                                    onClick={(event) => {
                                        removeMarkup()
                                        draw(i,j,color, event.nativeEvent.ctrlKey, event.nativeEvent.button === 0, event);
                                    }}
                                    onMouseOver={(event) => {
                                        if (event.buttons === 1) {
                                            removeMarkup()
                                        }
                                        draw(i,j,color, event.ctrlKey, event.buttons === 1, event);
                                    }}
                                    style={{
                                        width: `${width}px`,
                                        height: `${width}px`,
                                        backgroundColor: color,
                                        outline: "solid"
                                    }}
                                    key={`${j}-${i}`}
                                />
                            )
                        })
                    })}
                </div>
            </div>
        </div>
    );
}