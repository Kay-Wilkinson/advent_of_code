package main
// binary search - an array of order items (num rows), follow decision tree to arrive at final single item
// front row is index 0. Final back row is index 127
// A seat might be specified like FBFBBFFRLR, where:
// 		"F" := "front", 
// 		"B" := "back"
// 		"L" := "left"
// 		"R" := "right"
// part2 - sort seats and find for any gap in the sequential list. This will be your seat

import (
	"log"
	"bytes"
	"io/ioutil"
	"sort"
)

func main() {
	// read from file
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	seats := []int{}
	for _, line := range bytes.Split(c, []byte("\n")) {
		// if empty line, just continue through the file
		if len(line) == 0 {
			continue
		}
		// arr = [ 1 2 3 4 5 6 ]
		// split arr in two halves. If right half is greater than left, than continue down right node
		// left = 0
		// right = len(arr)
		// middle point = (left + right + 1)/2
		// while left <= right; cont operation
		// operation is middle = (right+left+1)/2
		// if arr[middle] == n return n
		// if arr[middle] < n (n is left hand side of array)
		// then left = middle
		// if arr[middle] > n (then n is right hand side of array)
		// right = middle - 1
		lineStr := string(line)
		left := 0
		right := 127
		for _, c := range lineStr[:7] {
			middle := (right+left+1)/2
			if c == 'B' {
				left = middle
			} else {
				right = middle - 1
			}
		}
		row := left // last item in search
		left = 0
		right = 7
		for _, c := range lineStr[7:] {
			middle := (right+left+1)/2
			if c == 'R' {
				left = middle
			} else {
				right = middle -1
			}
		}
		col := left
		seatID := row*8 + col
		seats = append(seats, seatID)
	}
	sort.Ints(seats)
	// cehck item of seat and previous seat. If current item != item -1 then we have the missing seat
	prev := seats[0]
	for i := 1; i < len(seats); i++ {
		if seats[i] !=prev+1 {
			log.Println(prev+1)
			break
		}
		prev = seats[i]
	}
}








