print(r'''
******************************************
           _.-,=_"""--,_
        .-" =/7"   _  .3#"=.
      ,#7  " "  ,//)#d#######=.
    ,/ "      # ,i-/###########=
   /         _)#sm###=#=# #######\
  /         (#/"_`;\//#=#\-#######\
 /         ,d####-_.._.)##P########\
,        ,"############\\##bi- `\| Y.
|       .d##############b\##P'   V  |
|\      '#################!",       |
|C.       \###=############7        |
'###.           )#########/         '
 \#(             \#######|         /
  \B             /#######7 /      /
   \             \######" /"     /
    `.            \###7'       ,'
      "-_          `"'      ,-'
         "-._           _.-"
             """"---""""
*********************************************      
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Where would you want to go: left or right. ").lower()
if direction == "right":
    print("Fall into a hole 🕳️🕳️🕳️. \nGame Over!")
elif direction == "left":
    between_river = input("You wanna swimm to reach Africa or wait for a Boat. Write swimm or wait: ").lower()
    if between_river == "swimm":
        print('''You are attacked by real Python 🐍🐍🐍.
                Gave Over.''')
    elif between_river == "wait":
        color_door = input("Which door you wanna go: red   blue   yellow :").lower()
        if color_door == "red":
            print("Burned by fire 🔥🔥🔥.\nGave Over!")
        elif color_door == "blue":
            print("Eaten by Dragon 🐲🐲🐲\nGame Over!")
        elif color_door == "yellow":
            print("Congratulation, You are welcome to Africa!💪💪💪💪")
        else:
            print("Gave Over")
    else:
        print("Your are Attacked by real Python! Gave End.")
else:
    print("Fall into a hole. Gave Over!")