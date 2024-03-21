package main

import (
	"crypto/aes"
	"crypto/cipher"
	"fmt"
	"encoding/hex"
)

func main() {
	// x86-64
	flag_enc_hex := "83f3487dd71182d26b77697980e1f1239cf1f49026d1f6d49bed2021a8cb4fa684ec3e7a6a78cfc80ac4446f1111a92feaf636c82b68"
	flag_enc, err := hex.DecodeString(flag_enc_hex)

	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// arm64
	key1_hex := "506422ba994951c2b76063e89f1a1660c5674a192b91b4bcf14fd163ba213019"
	key1, err := hex.DecodeString(key1_hex)

	if err != nil {
		fmt.Println("Error:", err)
		return
	}
 
	// get key
	block1, err := aes.NewCipher(flag_enc[len(flag_enc)-16:])
	stream1 := cipher.NewCFBDecrypter(block1, key1[:16])
	key2 := make([]byte, 16)
	stream1.XORKeyStream(key2, key1[16:])

	// get flag
	block2, err := aes.NewCipher(key2)
	stream2 := cipher.NewCFBDecrypter(block2, flag_enc[:16])
	buf := make([]byte, len(flag_enc))

	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	stream2.XORKeyStream(buf, flag_enc[16:])
	fmt.Printf("Flag: %s\n", buf)
}