'''        CRYPTOGRAPHY LINEAR ALGEBRA         '''

from multiprocessing import Value
from multiprocessing.managers import ValueProxy
import numpy as np 
import os
from numpy.random import randn
import pandas as pd



# MATRIX GENERATORS: Each sizes have corresponding values depending in its dimension.
def mtrx_2by2():
  rndm_2by2 = np.array([[12,34],[3,4]])
  return rndm_2by2
def mtrx_3by3():
  rndm_3by3 = np.array([[1,9,8],[20,40,2],[5,21,11]])
  return rndm_3by3  
def mtrx_4by4():
  rndm_4by4 = np.array([[10, 87, 3, 23],[1, 100, 34, 65],[66, 69, 5, 8],[90, 2, 45, 11]])
  return rndm_4by4 
def mtrx_5by5():
  rndm_5by5 = np.array([[66, 7, 78, 21, 43],[1, 99, 56, 34, 32],[7, 76, 23, 32, 98],[9, 66, 88, 12, 43], [6, 54, 76, 89, 13]])
  return rndm_5by5
def mtrx_6by6():
  rndm_6by6 = np.array([[99, 81, 2, 36, 17, 13],[1, 90, 65, 22, 34, 79],[3, 56, 87, 92, 13, 29],[46, 33, 72, 4, 6, 1], [23, 99, 12, 8, 28, 67],[88, 66, 9, 11, 83, 5]])
  return rndm_6by6
def mtrx_7by7():
  rndm_7by7 = np.array([[80, 12, 45, 23, 88, 6, 90],[1, 33, 78, 99, 34 , 56, 21],[9, 59, 32, 53 , 67, 75, 23],[6, 73, 84, 23, 12, 65, 87], [87, 34, 88, 43, 34, 11, 43],[82, 2, 56, 64, 75, 32, 4],[87, 43, 88, 99, 23, 54, 8]])
  return rndm_7by7
def mtrx_8by8():
  rndm_8by8 = np.array([[8, 13, 3, 29, 10, 21, 18, 1],[7, 22, 29, 20, 15, 22, 27, 12],[12, 28, 2, 33, 19, 23, 13, 10],[1, 21, 15, 23, 16, 22, 37, 28], [19, 28, 37, 14, 19, 26, 6, 14],[12, 2, 16, 24, 15, 2, 4, 12],[15, 17, 23, 28, 19, 23, 24, 8],[11, 25, 12, 16, 22, 28, 15, 23]])
  return rndm_8by8
def mtrx_9by9():
  rndm_9by9 = np.array([[29, 29, 6, 15, 18, 28, 23, 5, 9], [28, 27, 28, 5, 7, 21, 28, 6, 26], [14, 3, 8, 7, 12, 21, 18, 5, 20], [28, 4, 14, 5, 7, 4, 29, 13, 12], [8, 5, 23, 25, 26, 5, 13, 15, 3], [9, 27, 29, 8, 27, 10, 10, 29, 23], [2, 20, 9, 10, 25, 11, 24, 16, 23], [16, 8, 22, 18, 24, 19, 19, 19, 21], [6, 29, 22, 12, 25, 11, 27, 27, 6]]) 
  return rndm_9by9
def mtrx_10by10():
    rndm_10by10 = np.array([[22, 10, 17, 8, 29, 25, 2, 11, 21, 7],[24, 28, 12, 26, 2, 13, 21, 6, 27, 16],[27, 15, 23, 12, 10, 18, 29, 5, 11, 26],[5, 16, 11, 21, 15, 26, 8, 14, 29, 6], [21, 28, 12, 18, 7, 16, 28, 9, 24, 13],[26, 10, 15, 23, 19, 29, 3, 21, 11, 26],[10, 23, 19, 8, 13, 30, 26, 12, 20, 7],[27, 12, 20, 18, 11, 26, 23, 15, 6, 29],[6, 22, 14, 11, 16, 25, 8, 15, 29, 20], [14, 7, 29, 26, 25, 2, 3, 24, 18, 13]])
    return rndm_10by10


def csv(data_encode):
    csv_data_encode = pd.DataFrame(data_encode)
    csv_data_encode.to_csv('rsa.csv', mode = 'a', index=False, header=False)


class Matrix_inverse():

    def __init__(self):

        first_char = np.array(['$']) # filler/placeholder character
        alphabet = np.array(['a','b','c','d','e','f','g','h','i','j',
                                    'k','l','m','n','o','p','q','r','s','t',
                                    'u','v','w','x','y','z','_'])

        self.alphabet = np.concatenate((first_char, np.tile(alphabet, 10))) # used to join the first character array with 10 copies of the alphabet array. This results in an array of 260 characters (26 letters + 1 underscore) repeated 10 times, with $ as the first character.
       
#---------------------------------------------------------------------------------
    def process_encode(self, matrix_size, matrix_basis): # ENCODING PROCESS
      os.system('cls')
      print(f"NOTE:\n    The number of characters/value must be equal to the number of elements of the array size that you chose.\n\tEx. {matrix_size} x {matrix_size} ({matrix_size ** 2} LETTERS characters only)")
      print(f"\n    Matrix Size: {matrix_size} x {matrix_size}\n")
      
      while True:
          encode_word = input("\nEncoding Word: ")

          if len(encode_word) != matrix_size ** 2 or encode_word.isalpha == False:
            print("\nERROR:\n    It must be a letter from ENGLISH alphabet and must have the same character length as the dimension of the matrix size you chose.\n ")
            print(f"    Character Length of Encoded Word: {len(encode_word)}\n")
          else:
              break
       
      encode_chars = np.array(list(encode_word.replace(' ','_').lower())) # Separates the encoded word by characters in lowercase and replaces whitespace with a specific character
      copy_encode_chars = encode_chars.copy()
      orig_indices = self.alphabet.argsort() # Returns the indices that would sort the alphabet array
      basis_matrix = orig_indices[np.searchsorted(self.alphabet[orig_indices], copy_encode_chars)] # Makes the array 1D : used to find the indices where elements in copy_encode_chars should be inserted into the sorted array

  
      # Reshaping the Basis 1D Matrix:
      basis_matrix1d = basis_matrix.reshape((matrix_size, matrix_size)) # Reshapes the matrix into a specified dimension depending on the indicated size of the user.
      transposed_mtrx = basis_matrix1d.T  # TRANSPOSE
        
      # Performing Dot Product
      encoding_mtrx = matrix_basis # Fetched from the MATRIX GENERATORS 
      resulting_mtrx = np.dot(encoding_mtrx ,transposed_mtrx) # Finds the dot product of the encoding matrix and basis matrix.
        
      # Converts the Resulting Matrix into 1D:
      linear_form = np.reshape(resulting_mtrx, -1, order='F') # Reads 2D array column by column and create 1D array from it
      
      # Appending the data into a CSV file:
      data_encode = {"Method": 'Encode', '|': '|', "Word/Values": [encode_word],'Data': ':','Decoded/Encoded Words/Values': [linear_form]}
      csv(data_encode)
      

      print(f"\n\tCharacters: {encode_chars}")
      print(f"\n\tBasis 1D Matrix: {basis_matrix}")
      print(f"\n\nReshaped Basis Matrix:\n{transposed_mtrx}")
      print(f"\nEncoding Matrix:\n{encoding_mtrx}\n\n")
      print(f"\n\tMultiplying the Matrices: \n{transposed_mtrx} \n    x \n{encoding_mtrx}")
      print(f"\n\nResulting Matrix:\n{resulting_mtrx}\n\n")
      print(f"Encoded Message in Linear Form:\n{linear_form}")

#---------------------------------------------------------------------------------
    def decode_process(self, matrix_size, matrix_basis):
      os.system('cls')
      print(f"Enter Elements(Only Positive Integers) | Matrix Size: {matrix_size} x {matrix_size} | Required Number of Values: {matrix_size ** 2} \n")
      list_matrix = []  # Here we define an empty list.
    
      i = 0
      while len(list_matrix) < matrix_size ** 2:
        try:
            i = i + 1
            values = int(input(f'   Enter Value {i}: '))
            list_matrix.append(values)
        except ValueError:
            print("\nInvalid input. Please enter an integer value.\n")
      
      
      orig_matrix = np.array(list_matrix) # turning the list into a numpy array so that it can be subscriptable
      mtrix_encoded= orig_matrix.reshape(matrix_size, matrix_size).T # Reshapes the current dimension depending on the size chosen by the user.
      
      decoding_mtrx = matrix_basis # Fetched from the MATRIX GENERATORS 
      inverse_decoding_mtrx = np.linalg.inv(decoding_mtrx) # Finds the inverse of the decoding matrix.

      resulting_mtrx = np.dot(inverse_decoding_mtrx, mtrix_encoded).T # It calculates the dot product of the encoding and decoding matrix.

      decoded_linearForm = np.array(resulting_mtrx.reshape(((int(resulting_mtrx.size/resulting_mtrx.size)), resulting_mtrx.size)))
      finalDecoded = (np.rint(decoded_linearForm)).astype(int) # CONVERTS FLOAT TYPE TO INTEGER
      decodedChar = self.alphabet[finalDecoded] # Each value loops through the alphabet list
      
      data_encode = {"Method": 'Decode', '|': '|', "Word/Values": [orig_matrix],'Data': ':','Decoded/Encoded Words/Values': [decodedChar]}
      csv(data_encode) # function for the csv file

      print(f"\nEncoding Matrix: \n{mtrix_encoded}")
      print(f"Decoding Matrix: \n {decoding_mtrx}")
      print(f"\nInverse Encoding Matrix: \n{inverse_decoding_mtrx}")
      print("\nMULTIPLY DECODING AND INV ENCODING MATRICES")
      print(f"Product: {resulting_mtrx}")
      print(f"\nDecoded Matrix: \n{finalDecoded}")
      print (f"\n\tDecoded Characters: {decodedChar}")

# ---------------------------------------------------------------------------------------------------------------------------------------------

def main_matrix_inverse():

    def select_size():
        print("Choose Size of the Matrix:")
        print("\t2). 2 x 2\n\t3). 3 x 3\n\t4). 4 x 4\n\t5). 5 x 5\n\t6). 6 x 6\n\t7). 7 x 7\n\t8). 8 x 8\n\t9). 9 x 9\n\t10).10 x 10\n")
        
        while True:

            try:
                matrix_size = int(input("\tEnter Here: "))

                if (matrix_size) == 2:
                    matrix_basis =  mtrx_2by2() # fetched from Matrix Generators
                    break

                if (matrix_size) == 3:
                    matrix_basis = mtrx_3by3()
                    break

                if (matrix_size) == 4:
                    matrix_basis =  mtrx_4by4()
                    break

                if (matrix_size) == 5:
                    matrix_basis =  mtrx_5by5()
                    break

                if (matrix_size) == 6:
                    matrix_basis =  mtrx_6by6()
                    break

                if (matrix_size) == 7:
                    matrix_basis =  mtrx_7by7()
                    break

                if (matrix_size) == 8:
                    matrix_basis =  mtrx_8by8()
                    break

                if (matrix_size) == 9:
                    matrix_basis =  mtrx_9by9()
                    break

                if (matrix_size) == 10:
                    matrix_basis =  mtrx_10by10()
                    break

            except ValueError:
                print("\nInvalid Input\n")

        return matrix_size, matrix_basis

    def Encoding_process():
        matrix_size, basis_matrix = select_size()
        encoding_object = Matrix_inverse()
        encoding_object.process_encode(matrix_size, basis_matrix)

    def Decoding_process():
        matrix_size, basis_matrix = select_size()
        decoding_object = Matrix_inverse()
        decoding_object.decode_process(matrix_size, basis_matrix )

    def main_home():
        print("CHOOSE ACTION:\n    1: ENCODE\n    2: DECODE\n    3: HISTORY")
    
        while True:
            try:
                user_action = int(input("\n    Enter Here: "))

                if user_action == 1:
                    os.system('cls')
                    Encoding_process()
                    go_home()

                elif user_action == 2:
                    os.system('cls')
                    Decoding_process()
                    go_home()

                elif user_action == 3:
                    os.system('cls')
                    dataset = pd.read_csv('rsa.csv')
                    print(dataset)
                    go_home()
        
            except ValueError:
                print("Invalid Input")
                go_home()

    def go_home():
        print("\n1: Home ")
        while True:
            try:
                user_home = int(input("   Enter: "))
                if user_home == 1:
                    os.system('cls')
                    main_home()
                break

            except ValueError:
                print("Invalid Input")

    main_home()


main_matrix_inverse()