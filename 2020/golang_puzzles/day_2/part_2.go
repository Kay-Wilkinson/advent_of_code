package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	// 1-2 a: abc
	valid := 0
	for _, line := range bytes.Split(c, []byte("\n")) {
		parts := strings.Split(string(line), " ")
		if len(parts) < 3 {
			log.Println("parts less than 3 ", string(line))
			continue
		}
		lh := strings.Split(parts[0], "-")
		if len(lh) < 2 {
			log.Println("lh less than 2")
			continue
		}
		low, _ := strconv.Atoi(lh[0])
		high, _ := strconv.Atoi(lh[1])
		pattern := []rune(strings.ReplaceAll(parts[1], ":", ""))
		pwd := []rune(parts[2])

		// check if password position low-1 == pattern position 0
		if (pwd[low-1] == pattern[0]) != (pwd[high-1] == pattern[0]) {
			valid++
		}
		
	}
	log.Println(valid)
}
