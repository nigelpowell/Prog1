'''
Assumptions
  * "DAT1.TXT" is properly formatted (grammatically)
  * "DAT1.TXT" words are all separated by spaces (' ')
  * The user types in the two integers (the left and right margins)
  * 1 inch = 12 characters (X) --> one inch contains 12 chars     **(might be irrelevant now)**
  * Line is max of 80 chars total
  
Requirements
  * Get margins from user
  * Read text from "DAT1.TXT"
  * Format text in accordance to user-set margins, spacing, etc.
  * Display edited text
  * Create a new textfile with the edited text ("DAT1_output.TXT")
  
Questions
  * What are "trailing blanks"?
  
Algorithm
  1. Prompt user to enter margins (left and right)
  2. Use margins to calculate how many characters should be on each line
  3. Read from file (one-word-at-a-time), making sure the number of
     characters in each word does NOT exceed the max number of characters
     "allowed" on each line
  4. If the word characters do not cause the line to exceed the max number
      of characters, add that word to the line. Otherwise, add that word to
      the next line and reset the count
  5. Repeat this process (3-4) until all the words in "DAT1.TXT" are read
  6. Close the outputted file ("DAT1_output.TXT"), read all the lines from
     it, and display it to the user
'''

def maxChars(m_left, m_right):          #calculates the maximum number of characters allowed per line
  numChars = 80 - (m_left + m_right)
  return numChars

def printToUser():                      #reads from output file and prints it to the user
  displayToUser = open("DAT1_output.TXT", 'r')
  for line in displayToUser:
    print(line)
  displayToUser.close()


def main():
  marg_left = int(input("Enter a left margin:\t"))          #get left margin from user
  marg_right = int(input("Enter a right margin:\t"))        #get right margin from user
  chars_per_line = maxChars(marg_left, marg_right)          #max characters allowed per line
  
  
  dataFile = open("DAT1.TXT", 'r')                          #opens file for READING only
  tmpStr = dataFile.read()                                  #reads entire file into a single string
  wordArray = tmpStr.split(' ')                             #creates array from string, separated by ' '
  dataFile.close()                                          #closes file
  
  
  leftSpace = ''                    #left space margin
  rightSpace = ''                   #right space margin
  for i in range(marg_left):
    leftSpace += '*'                #change this to ' ' later
  for i in range(marg_right):
    rightSpace += '*'               #change this to ' ' later

    
  outputFile = open("DAT1_output.TXT", 'w')                 #opens file to WRITE --> this is the output file
  charTotal = 0                                             #keeps track of the number of characters currently in the line
  outputFile.write(leftSpace)                               #writes left margin
  for word in wordArray:                                    #loops through every word in the array
    chars_in_word = 0                                       #stores characters in each word
    for char in word:
      chars_in_word += 1
    if (charTotal + chars_in_word + 1 <= chars_per_line):   #if the current word's characters don't exceed the max characters allowed, print word in that line
      charTotal += chars_in_word + 1
      remainingSpace_1 = chars_per_line - charTotal
      outputFile.write(word + ' ')
    else:                                                   #if the current word's characters do exceed the max characters allowed, fill the rest of the line w/ space && margins, then write word on the next line
      remainingSpace_2 = chars_per_line - charTotal
      charTotal = chars_in_word + 1
      for i in range(remainingSpace_2):
        outputFile.write(' ')
      outputFile.write(rightSpace + '\n' + leftSpace + word + ' ')
  
  for i in range(remainingSpace_1):                         #after the last word in last line, fill the line with spaces && write right margins
    outputFile.write(' ') 
  outputFile.write(rightSpace)
  outputFile.close()
  printToUser()



if __name__ == "__main__":
  main()