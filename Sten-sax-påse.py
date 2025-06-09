import random , time

def scrollPrint(text, interval=.1, endline=True):
    listoftext = [*text]
    for i in listoftext:
        print(i, end="", flush=True)
        time.sleep(interval)
    if endline == True:
        print("")

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

scrollPrint("Välkommen till sten, sax, påse")
scrollPrint("Din poäng är " + str(spelare_poäng))

scrollPrint("Datorns poäng är " + str(dator_poäng))

while dator_poäng < 3 and spelare_poäng < 3:
  dator_val = random.choice(val)

  scrollPrint("\nSten, sax eller påse? ", endline=False)
  spelare_val=input().lower()

  while CheckChoice(val, spelare_val) == 1:
    scrollPrint("\nFelstavat svar")
    scrollPrint("Sten, sax eller påse? ", endline=False)
    spelare_val=input().lower()
  

  scrollPrint(("\nDatorn valde " + str(dator_val)))
  if dator_val == spelare_val: 
    scrollPrint("Ni valde samma! Kör igen.")
  
  elif ( 
        (spelare_val == "sten" and dator_val == "sax") or 
        (spelare_val == "sax" and dator_val == "påse") or 
        (spelare_val == "påse" and dator_val == "sten")
        ):
    spelare_poäng += 1
    scrollPrint("\nDu fick poäng!")
  
  else:
    dator_poäng += 1
    scrollPrint("\nDatorn fick poäng!")
    
  scrollPrint(("Din poäng är " + str(spelare_poäng)))
  scrollPrint(("Datorns poäng är " + str(dator_poäng)))
if dator_poäng > spelare_poäng:
  scrollPrint("\nDatorn vann spelet!")
else:
  scrollPrint("\nDu vann spelet! Bra jobbat")