package main

import (
	"log"
	"bytes"
	"io/ioutil"
)

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	tot := 0
	for _, group := range bytes.Split(c, []byte("\n\n")) {
		//rune is a unicode point in Go. Represents a single char. 
		// empty struct as using map as a set as set is not in standard lib
		qs := make(map[rune]struct{})
		for _, line := range bytes.Split(group, []byte("\n")) {
			for _, c := range string(line) {
				// empty struct as effecient way to represent a value of no size
				qs[c] = struct{}{}
			}
		}
		tot += len(qs)
	}
	log.Println(tot)
}


