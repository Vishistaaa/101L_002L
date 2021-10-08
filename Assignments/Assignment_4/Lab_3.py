import random
global spin
spin=0
def play_again():
  global play
  thing=True
  while thing:
    # Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes 
    play = input("Do you want to play again? ==> ")
    if play.upper()=='Y' or play.upper()=='YES': 
      return True
      break
    if play.upper()=='N'or play.upper()=='NO':
      return False
      break
    else:
        print("You must enter Y/Yes/N/NO to countinue.")
     
def get_wager(bank):
  global chips
  #Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have
  that=True
  while that:
   chips= int(input("How many chips do you want to wager? ==> "))
   if 0<chips<=bank:
     return chips
     break
   elif chips<0:
      print("The wager amount must be greater than 0. Please enter again.")
   elif chips>bank:
      print("The wager amount cannot be greater than how much you have.",bank)  
  chips= int(input("How many chips do you want to wager? ==> "))      

def get_slot_results():
    #Returns the result of the slot pull
    r1= random.randint(1,10)
    r2= random.randint(1,10)
    r3= random.randint(1,10)
    return r1,r2,r3

def get_matches(reela, reelb, reelc):
    #Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike.
    global match
    match=0
    if reela==reelb:
      match+=1
    if reela==reelc:
      match+=1
    if reelb==reelc:
      match+=1
    if match==2:
      return 3
    elif match== 1:
      return 2
    else:
      return 0

def get_bank():
  global n_chips
    #Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 10
  n_chips= int(input("How many chips do you want to start with? ==> "))
  word= True
  while word:
    if n_chips<101 and n_chips>0:
      return n_chips
      break
    if n_chips<0:
      print("Too low a value, you can only choose 1-100 chips")
    elif n_chips>=100:
      print("Too high a value, you can only choose 1-100 chips")
    n_chips= int(input("How many chips do you want to start with? ==> "))
    
def get_payout(wager, matches):
  global payout
  payout=0
    # Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match
  if matches==3:
    payout=10 * wager
  elif matches==2:
    payout=3 * wager
  else:
    payout= wager * -1 
  return payout    


if __name__ == "__main__":

    playing = True
    bank=get_bank()
    listy=[]
    listy.append(bank)
    while playing:
        # Replace with condition for if they still have money.
            
            wager = get_wager(bank)
            spin+=1

            t = get_slot_results()

            matches = get_matches(t[0],t[1],t[2])
            variable=" ".join(map(str,(t[0],t[1],t[2])))
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", variable)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            listy.append(bank)
            print()
            if bank<=0:
             print("You lost all", random.randint(1,10), "in", spin, "spins")
             print("The most chips you had was", max(listy))
             play_again()
            if play_again()== False:
              break
            print()