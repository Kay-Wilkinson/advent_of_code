package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	// count num of valid passports if all 8 expected fields are present
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	passports := make([]map[string]string, 0)
	// process input data from lines, etc to get all field key value pairs
	for _, line := range bytes.Split(c, []byte("\n\n")) {
		if len(line) == 0 {
			continue
		}
		p := make(map[string]string)
		for _, subline := range bytes.Split(line, []byte("\n")) {
			if len(subline) == 0 {
				continue
			}
			for _, kv := range bytes.Split(subline, []byte(" ")) {
				parts := strings.Split(string(kv), ":")
				p[parts[0]] = parts[1]
			}
		}
		passports = append(passports, p)
	}
	valid := 0
	for _, p := range passports {
		_, isCIDPresent := p["cid"]
		if len(p) == 8 || (len(p) == 7 && !isCIDPresent) {
			valid++
		}
	}
	log.Println(valid)
}