package main

import (
	"bytes"
	"io/ioutil"
	"log"
)

// start by counting all the trees you would encounter for the slope right 3, down 1:

// could gen a matrix in mem and traverse the matrix but this is too intensive and slow
// use a map instead

func main() {
	// load file and error handle
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	m := make([][]rune, 0)
	for _, line := range bytes.Split(c, []byte("\n")) {
		if len(line) == 0 {
			continue
		}
		row := make([]rune, 0)
		// convert rune line to string obj
		for _, c := range string(line) {
			row = append(row, c)
		}
		m = append(m, row)
		total := 0
		right := 3
		down := 1
		for down < len(m) {
			row := m[down]
			if row[right%len(row)] == '#' {
				total++
			}
			down++
			right +=3
		}
		log.Println(total)
	}

}