package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strconv"
)

func main() {
	// x+z=s
	// s - z = x 
	// first load the list into a map 0(n), for each item
	// s = 2020-y
	// for each item x in the map
	// z = s-x
	// if z in the map 0(1) return z*y*z

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
		s := 2020 - y
		for x, _ := range m {
			z := s - x
			if _, ok := m[z]; ok {
				log.Printf("%d+%d+%d=2020 / %d*%d*%d", x, y, z, x, y, z, x*y*z)
				return
			}
		}
	}
}
