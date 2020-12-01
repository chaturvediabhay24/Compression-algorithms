
"""
# **LEMPEL-ZIV CODING**

1. We will frist make the list of values and their ascii characters.
2. Then will traverse the string.
3. If the string is already present then the new character will be added to traversing string.
4. If the string is not present in ascii codes then we will find address of one step previous 
   string and will append the result of new string in our list of ascii values.
5. and will repeat the precess untill whole string is traversed.
6. Code is generated in ASCII values. To know the output bits used we have to convert ASCII into
   binary.
7. Compression ration is calculated taking the ration of input bits used and output bits used. 

"""

class LempelZivCoding:
    def __init__(self, s, bl=4):
      self.inputstring=s
      self.bit_length=bl
    def execute(self):
      self.ascii_values=self.get_ascii_values()
      self.results=self.get_results()
      self.result_in_binary=[self.to_binary(x) for x in self.results]
      self.input_length=self.get_input_length()
      self.output_length=self.get_output_length()
      self.print()
    def to_binary(self, n):                                   # Converts decimal to binary form
      if(n=="") :
        return ""
      return bin(int(n)).replace("0b", "")  


    def get_ascii_values(self):                                #get list of ascii values of all 256 characters
      # Initialise the table
      ascii_values = []
      for i in range(0,256):
          ascii_values.append(chr(i))
      return ascii_values

    def get_results(self):
      S = ""
      result = []

      for char in self.inputstring:
          SC = S + char    # Get input symbol while there are input symbols left
          if SC in self.ascii_values:       # SS is in the table
              S = SC
          else:
              result.append(self.ascii_values.index(S))     # Output the code for String
              self.ascii_values.append(S + char)
              S = char
      result.append(self.ascii_values.index(S))             # Output the String
      return result

    def get_input_length(self ):                            #return total no of input bits required
      input_length=0
      for i in [self.to_binary(ord(x)) for x in self.inputstring.strip()]:
        input_length=max(len(i), input_length)
      return input_length*len(self.inputstring)
    def get_output_length(self ):                           #return total no of output bits required
      output_length=0
      for i in self.result_in_binary:
        output_length=max(len(i), output_length)
      return output_length*len(self.result_in_binary)

    def print(self):                                        # utitlity function for printing the results
      print("Resultant ascii codes in ASCII:\n", self.results)
      print("Resultant ascii codes in BINARY:\n", self.result_in_binary)
      print("Compression Ratio: {}:{}".format(self.input_length, self.output_length))


# input_string="aababbbabaababbbabbabb"
input_string=input("Enter the input string : ")

obj=LempelZivCoding(input_string)
obj.execute()