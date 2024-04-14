import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def run_program():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(direction, text, shift)

def caesar(direction, text, shift):
  solved_text = ""
  if direction == "encode":
    for x in text:
      if x not in alphabet:
        new_text = x
      else:
        new_position = alphabet.index(x)+shift
        new_text = alphabet[new_position]
      solved_text += new_text
    print(f"The encoded text is {solved_text}")
  elif direction == "decode":
    for x in text:
      if x not in alphabet:
        new_text = x
      else:
        new_position = alphabet.index(x)-shift
        new_text = alphabet[new_position]
      solved_text += new_text
    print(f"The decrypted text is {solved_text}")
  restart = input("Do you want to try again? yes or no: ")
  if restart == "yes":
    run_program()

run_program() 