print("shreeyash Hello")
def chatbot():
  print("chatbot: hello!!!how can 9i help you ?\n")

while True:
  user = input ("you:").lower()

  if user="exit":
    print("invalid error try again")
  elif "help" in user:
    print("what typeof help i can do?")
chatbot()
