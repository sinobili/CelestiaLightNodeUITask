package main

import (
	"encoding/hex"
	"fmt"
	"math/rand"
)

// ATTENTION:
// In order to generate a random namespace ID and hex-encoded data, please enter a valid integer on Line 17 after the `:=`.
//
// Example: `seed := 5405`
func main() {
	// enter random integer on Line 17 after the `:=`
	seed := 1511

	rand.Seed(int64(seed))

	// generate a random namespace ID
	nID := generateRandHexEncodedNamespaceID()

	// generate a random hex-encoded message
	msg := generateRandMessage()

	fmt.Println(fmt.Sprintf("My hex-encoded namespace ID: %s\n\nMy hex-encoded message: %s", nID, msg))
}

// generateRandHexEncodedNamespaceID generates 8 random bytes and
// returns them as a hex-encoded string.
func generateRandHexEncodedNamespaceID() string {
	nID := make([]byte, 8)
	_, err := rand.Read(nID)
	if err != nil {
		panic(err)
	}
	return hex.EncodeToString(nID)
}

// generateRandMessage generates a message of an arbitrary length (up to 100 bytes)
// and returns it as a hex-encoded string.
func generateRandMessage() string {
	lenMsg := rand.Intn(100)
	msg := make([]byte, lenMsg)
	_, err := rand.Read(msg)
	if err != nil {
		panic(err)
	}
	return hex.EncodeToString(msg)
}
