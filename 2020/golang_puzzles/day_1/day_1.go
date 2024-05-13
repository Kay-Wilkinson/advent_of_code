package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strconv"
)

func main() {
	// first load list into map (for 0(n))
	// for each item y in the map 0(n)
	// x = 2020-y
	// if x in the map 0(1) return x*y
	
	d, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	
	m := make(map[int]int, 0)
	for _, line := range bytes.Split(d, []byte("\n")) {
		n, err := strconv.Atoi(string(line))
		if err != nil {
			log.Println(err)
			continue
		}
		m[n]++
	}
	for y, _ := range m {
		x := 2020-y
		if _, ok := m[x]; ok {
			log.Printf("%d+%d=2020 / %d*%d=%d", x, y, x, y, x*y)
			return
		}	
	}
}