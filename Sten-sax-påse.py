import random 

dator_poäng = 0
spelare_poäng = 0
val = ["Sten", "Sax", "Påse"]

print("Välkommen till sten sax påse")
print("Din poäng är ", spelare_poäng)
print("datorns poäng är ", dator_poäng)

while dator_poäng < 3 and spelare_poäng < 3:
  dator_val = random.choice(val)
  spelare_val=input("\nSten, sax eller påse? ")

  print("Datorn valde " + dator_val)
  # Dålig kod #
  if dator_val == spelare_val: 
    print("Ni valde samma! Kör igen.")
  
  elif ( 
        (spelare_val == "sten" and dator_val == "Sax") or 
        (spelare_val == "sax" and dator_val == "Påse") or 
        (spelare_val == "påse" and dator_val == "Sten")
        ):
    spelare_poäng += 1
    print("Du fick poäng!")
  
  else:
    dator_poäng += 1
    print("Datorn fick poäng!")
    
  print("Din poäng är ", spelare_poäng)
  print("Datorns poäng är ", dator_poäng)
if dator_poäng > spelare_poäng:
  print("\nDatorn vann spelet!")
else:
  print("\nDu vann spelet! Bra jobbat")