package main

import (
	"fmt"
	"math"
)

// calculate the compound interest with formula from Wikipedia
// https://en.wikipedia.org/wiki/Compound_interest#Calculation_of_compound_interest

func compoundInterest(principal float64, interestRate float64, frequencyPerYear float64, overYears int) float64 {

	// (1 + interestRate / frequencyPerYear)
	block := 1 + (interestRate / float64(frequencyPerYear))

	// frequencyPerYear * overYears
	exponent := frequencyPerYear * float64(overYears)

	compoundInterest := principal * math.Pow(block, float64(exponent))

	return compoundInterest
}

func main() {

	wikiExample := compoundInterest(1500, 0.043, 4, 6)
	fmt.Println(wikiExample)

	var p, rate, freq float64
	var time int

	fmt.Println("Enter the principal : ")
	fmt.Scanf("%f", &p)

	fmt.Println("Enter the interest rate : ")
	fmt.Scanf("%f", &rate)

	fmt.Println("Enter the compounding frequency per year : ")
	fmt.Println("[1 for yearly, 4 for quarterly and 12 for monthly]")
	fmt.Scanf("%f", &freq)

	fmt.Println("Enter the duration in years : ")
	fmt.Scanf("%d", &time)

	result := compoundInterest(p, rate, freq, time)
	fmt.Println(result)
}
