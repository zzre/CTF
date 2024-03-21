package main

import (
	"fmt"
	"hash/crc32"
	"math/rand"
	"github.com/itchyny/maze"
)

func main() {
	var input string
	fmt.Scanln(&input)
	input += "\n"
	inputBytes := []byte(input)
	
	hash := crc32.ChecksumIEEE(inputBytes)
	rand.Seed(int64(hash))

	m := maze.NewMaze(25, 50)
	m.Generate()
	m.Solve()
    fmt.Println(m.String(maze.Default))
}