package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "strings"
    "strconv"
//     "bytes"
    "regexp"
)

func main() {
    data, err := ioutil.ReadFile("input.txt")
    if err != nil {
        log.Fatal(err)
    }
    lines := processData(string(data))
    sum := sumFirstLastIntegers(lines)
    fmt.Println(sum)
}

func processData(input string) []string {
    return strings.Split(input, "\n")
}

func sumFirstLastIntegers(lines []string) int {
    var sum int
    r := regexp.MustCompile(`\d+`)
    for _, line := range lines {
        matches := r.FindAllString(line, -1)
        if len(matches) > 0 {
            // extract the first digit of the first match
            firstDigit := matches[0][0:1]
            // extract the last digit of the last match
            lastMatch := matches[len(matches)-1]
            lastDigit := lastMatch[len(lastMatch)-1:]

            // combine first and last digit into a two-digit string
            twoDigitNumberStr := firstDigit + lastDigit
            // Then convert that string to an int
            twoDigitNumber, _ := strconv.Atoi(twoDigitNumberStr)
            sum += twoDigitNumber
        }
    }
    return sum
}

// 54573

