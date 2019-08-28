'''
Assumptions
  * "DAT1.TXT" is properly formatted (grammatically)
  * "DAT1.TXT" words are all separated by spaces (' ')
  * The user types in the two integers (the left and right margins)
  * 1 inch = 12 characters (X) --> one inch contains 12 chars
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




def main():
  marg_left = int(input("Enter a left margin:\t"))
  marg_right = int(input("Enter a right margin:\t"))
  chars_per_line = maxChars(marg_left, marg_right)
  
  dataFile = open("DAT1.TXT", 'r')
  tmpStr = dataFile.read()
  wordArray = tmpStr.split(' ')
  dataFile.close()
  
  charTotal = 0

  for word in wordArray:
    chars_in_word = 0
    for char in word:
      chars_in_word += 1
    if (charTotal + chars_in_word)


if __name__ == "__main__":
  main()