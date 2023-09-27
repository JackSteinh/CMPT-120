def main():
  
  #set this to any double
  doubleValue = 6.5
  
  #set this to any int
  intValue = 8
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue+intValue)
  print(doubleValue-intValue)
  print(doubleValue*intValue)
  print(doubleValue/intValue)
  
  
  #populate this list
  myFriends = ["Ryan", "Connor", "James", "Griffin"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  #populate this list with five numbers
  fiveNumbers = [12, 16, 420, 12000, 74]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0]+fiveNumbers[1])
  print(fiveNumbers[2]-fiveNumbers[3])
  print(fiveNumbers[4]*fiveNumbers[1])
  print(fiveNumbers[2]/fiveNumbers[4])
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[3] = 91
  fiveNumbers[4] = 99
  #print out the list
  print(fiveNumbers)
  
main()
