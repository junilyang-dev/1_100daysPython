while(True):
  FirstNumber = int(input("Choose a number: \n"))
  SecondNumber = int(input("Choose another one: \n"))
  Operation = input("Choose an operation: \n\tOptions are: + , - , * or /.\nWhile you write the operation, please write it in lowercase.\n\tWrite 'exit' to finish.\n")
  # Addition
  if Operation == "+" :
    print("Result: ", FirstNumber + SecondNumber)
  # Subtraction
  elif Operation == "-" :
    print("Result: ", FirstNumber - SecondNumber)
  # Multiplication
  elif Operation == "*" :
    print("Result: ", FirstNumber * SecondNumber)
  # Division
  elif Operation == "/" :
    print("Result: ", FirstNumber / SecondNumber)
  # Exit
  elif Operation == "exit" :
    break