package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Hello, World!")
	// replacer()
	// inputReader()
	// printFileStats()
	// grader()
	guessingGame()
}

func replacer() {
	str := "Adh#r A#ma"
	fmt.Println(strings.Replace(str, "#", "i", -1))
}

func inputReader() {
	fmt.Print("Enter a sentence: ")
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	fmt.Println("You entered:", input)
}

func printFileStats() {
	fileInfo, err := os.Stat("hello.go")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("File:", fileInfo)
}

func grader() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Enter Marks:")

	marks, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}

	marks = strings.TrimSpace(marks)

	marksFloat, err := strconv.ParseFloat(marks, 64)
	var grade string
	if marksFloat > 90 && marksFloat <= 100 {
		grade = "A+-Grade"
	} else if marksFloat > 85 && marksFloat <= 90 {
		grade = "A-Grade"
	} else if marksFloat > 75 && marksFloat <= 85 {
		grade = "B-Grade"
	} else if marksFloat > 60 && marksFloat <= 75 {
		grade = "C-Grade"
	} else {
		grade = "D-Grade"
	}
	fmt.Println("Grade:", grade)
}

func guessingGame() {
	target := rand.Intn(100) + 1

	fmt.Println("Number generated, start guessing!")
	reader := bufio.NewReader(os.Stdin)
	for i := 10; i >= 1; i-- {
		fmt.Print("Make a guess: ")
		guess, _ := reader.ReadString('\n')
		guessInt, _ := strconv.Atoi(strings.TrimSpace(guess))
		if guessInt == target {
			fmt.Println("You guessed right!!!")
			return
		} else if guessInt < target {
			fmt.Println("You guessed low. You now have", i-1, "chances remaining")
			continue
		} else {
			fmt.Println("You guessed high. You now have", i-1, "chances remaining")
			continue
		}
	}
	fmt.Println("Sorry you ran out of chances, the number was", target)
}
