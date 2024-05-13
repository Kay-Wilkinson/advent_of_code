package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
}

func processData(input string) []string {
	return strings.Split(input, "\n")
}

sumIntegersAndNums(lines string) int {
	var sum int
	return sum
}
