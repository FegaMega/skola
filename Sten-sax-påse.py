import random 

def CheckChoice(Valids: list, choice: str):
  #Returns 1 if choice is invalid
  #Returns 0 if choice is valid
  for Valid in Valids:
    if Valid == choice:
      return 0
  return 1

dator_poäng = 0
spelare_poäng = 0
val = ["sten", "sax", "påse"]

print("Välkommen till sten sax påse")
print("Din poäng är ", spelare_poäng)
print("datorns poäng är ", dator_poäng)

while dator_poäng < 3 and spelare_poäng < 3:
  dator_val = random.choice(val)
  spelare_val=input("\nSten, sax eller påse? ").lower()
  while CheckChoice(val, spelare_val) == 1:
    print("\nFelstavat svar")
    spelare_val=input("Sten, sax eller påse? ").lower()
  

  print("\nDatorn valde " + dator_val)
  # Dålig kod #
  if dator_val == spelare_val: 
    print("Ni valde samma! Kör igen.")
  
  elif ( 
        (spelare_val == "sten" and dator_val == "sax") or 
        (spelare_val == "sax" and dator_val == "påse") or 
        (spelare_val == "påse" and dator_val == "sten")
        ):
    spelare_poäng += 1
    print("\nDu fick poäng!\n")
  
  else:
    dator_poäng += 1
    print("\nDatorn fick poäng!\n")
    
  print("Din poäng är ", spelare_poäng)
  print("Datorns poäng är ", dator_poäng)
if dator_poäng > spelare_poäng:
  print("\nDatorn vann spelet!")
else:
  print("\nDu vann spelet! Bra jobbat")