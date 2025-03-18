#while condition:
#   ...statements


i=1
while i<10:
    print("*"*i)
    i+=1

# secter_no=9
# guesses=0

# while guesses<3:
#     guess=int(input("GUESS: "))
#     if guess==secter_no:
#         print("you Won")
#         break
#     guesses+=1
# if guesses>=3:
#     print("you lost")


command=""
while True:
    command= input("> ").lower()
    if command=="start":
        print("car started")
    if command == "stop":
        print("car stopped")
    elif command == "":
        print("choose please")
    elif command == 'help':
        print("""
start
stop
quit
""")
    elif command == 'quit':
        break
    else:
        print("sorry we dont undrstand")
    ####it has some mistakes... some amendments are to be done to this before 
    ###the mistake is in the fact that we dont understand still appears initially on the run