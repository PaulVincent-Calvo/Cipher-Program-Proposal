import os
import CiphersForCipherLock

class CipherLock_main():
    def __init__(self):
        pass
    
    def print_choices(self):
        choices = ["Encrypt", "Decrypt", "Return to Main Menu"]

        for index, choice in enumerate(choices):
            print (f"[{index + 1}] {choice}")
        
    def shift_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*33 + "Shift Cipher" + "\n" + "="*80)
        self.print_choices()
        
        shift_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while shift_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            shift_choice = input("Please input the number beside the action that you'd like to do: ")
        
        shift_choice = int(shift_choice)
        
        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Shift Cipher Menu", "Return to Main Menu", "Exit the Program"]

        if shift_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Shift Cipher" + "\n" + "="*80)
            user_message = input("\nPlease enter the message that you want to encrypt: ")

            while True:
                cipher_key = input("Please enter the key you'd like to use: ")
                try:
                    cipher_key = int(cipher_key)
                    # the cipher key must be positive and lower than 95 because if the value is above or equal to the length of the list of characters then it won't shift
                    if cipher_key > 0 and cipher_key < 95:
                        break
                    else:
                        print("Invalid input. Please enter a positive integer between 1 and 94.")
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

            cipher_obj = CiphersForCipherLock.shift_cipher(user_message, cipher_key)
            encrypted_message = cipher_obj.shift_cipher_encryption(user_message)

            print (f"\nEncrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while shift_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            shift_choice2 = int(shift_choice2)

            if shift_choice2 == 1:
                self.shift_chosen()
            
            elif shift_choice2 == 2:
                self.main()

            else:
                self.terminate()

        elif shift_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Shift Cipher" + "\n" + "="*80)
            user_message = input("\nPlease enter the message that you want to decrypt: ")

            while True:
                cipher_key = input("Please enter the key you'd like to use: ")
                try:
                    cipher_key = int(cipher_key)
                    # the cipher key must be positive and lower than 95 because if the value is above or equal to the length of the list of characters then it won't shift
                    if cipher_key > 0 and cipher_key < 95:
                        break
                    else:
                        print("Invalid input. Please enter a positive integer between 1 and 93.")
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

            cipher_obj = CiphersForCipherLock.shift_cipher(user_message, cipher_key)
            decrypted_message = cipher_obj.shift_cipher_decryption(user_message)

            print (f"\nDecrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while shift_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            shift_choice2 = int(shift_choice2)

            if shift_choice2 == 1:
                self.shift_chosen()
            
            elif shift_choice2 == 2:
                self.main()

            else:
                self.terminate()
        else:
            self.main()

    def caesar_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*37 + "Caesar Cipher" "\n" + "="*80)
        self.print_choices()
        
        caesar_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while caesar_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            caesar_choice = input("Please input the number beside the action that you'd like to do: ")
        
        caesar_choice = int(caesar_choice)

        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Caesar Cipher Menu", "Return to Main Menu", "Exit the Program"]

        if caesar_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*37 + "Caesar Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to encrypt: ")
            
            cipher_obj = CiphersForCipherLock.caesar_cipher(user_message)
            encrypted_message = cipher_obj.shift_cipher_encryption(user_message)

            print (f"Encrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while caesar_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            caesar_choice2 = int(caesar_choice2)

            if caesar_choice2 == 1:
                self.caesar_chosen()
            
            elif caesar_choice2 == 2:
                self.main()

            else:
                self.terminate()

        elif caesar_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*37 + "Caesar Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to decrypt: ")
            
            cipher_obj = CiphersForCipherLock.caesar_cipher(user_message)
            decrypted_message = cipher_obj.shift_cipher_decryption(user_message)

            print (f"Decrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while caesar_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            caesar_choice2 = int(caesar_choice2)

            if caesar_choice2 == 1:
                self.caesar_chosen()
            
            elif caesar_choice2 == 2:
                self.main()

            else:
                self.terminate()

        else:
            self.main()

    def vigenere_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*33 + "Vigenere Cipher" "\n" + "="*80)
        self.print_choices()

        vigenere_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while vigenere_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            vigenere_choice = input("Please input the number beside the action that you'd like to do: ")
        
        vigenere_choice = int(vigenere_choice)

        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Vigenere Cipher Menu", "Return to Main Menu", "Exit the Program"]       

        if vigenere_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Vigenere Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to Encrypt: ")
            cipher_obj = CiphersForCipherLock.vigenere_cipher(user_message)

            encrypted_message = cipher_obj.vigenere_cipher_encryption(user_message)

            print (f"Encrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while vigenere_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            vigenere_choice2 = int(vigenere_choice2)

            if vigenere_choice2 == 1:
                self.vigenere_chosen()
            
            elif vigenere_choice2 == 2:
                self.main()

            else:
                self.terminate()

        elif vigenere_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Vigenere Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to decrypt: ")
            cipher_obj = CiphersForCipherLock.vigenere_cipher(user_message)

            decrypted_message = cipher_obj.vigenere_cipher_decryption(user_message)

            print (f"Decrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while vigenere_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            vigenere_choice2 = int(vigenere_choice2)

            if vigenere_choice2 == 1:
                self.vigenere_chosen()
            
            elif vigenere_choice2 == 2:
                self.main()

            else:
                self.terminate()
        
        else:
            self.terminate()

    def hill_chosen(self):
        pass

    def matrix_inverse_chosen(self):
        pass

    def rsa_chosen(self):
        pass

    def base64_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*37 + "Base64 Cipher" "\n" + "="*80)

    def terminate (self):
        pass

    def main(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*35 + "CipherLock" + "\n" + "-"*80 + "\n" + " "*36 + "Main Menu" + "\n" + "="*80)
        print ("Please choose a Cipher.")
        options = ["Shift", "Caesar", "Vigenere", "Hill", "Matrix Inverse", "RSA", "Base64", "Exit"]
        
        for index, option in enumerate (options):
            if index < len(options) - 1:
                print (f"[{index + 1}] {option} Cipher")
            else:
                print (f"[{index + 1}] {option}")
        
        user_choice = input("\nPlease input the number beside the Cipher that you want to use: ")

        while user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid input. Please try again.")
            user_choice = input("Please input the number beside the Cipher that you want to use: ")

        user_choice = int(user_choice)

        if user_choice == 1:
            self.shift_chosen()

        elif user_choice == 2:
            self.caesar_chosen()

        elif user_choice == 3:
            self.vigenere_chosen()

        elif user_choice == 4:
            pass

        elif user_choice == 5:
            pass

        elif user_choice == 6:
            pass

        elif user_choice == 7:
            pass

        else:
            pass

obj1 = CipherLock_main()
obj1.main()