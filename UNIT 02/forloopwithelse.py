for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")

print("\nWhile loop")
# else executes when loop finishes loop doesnot breaks
i = 0
while i < 7 :
    print(i)
    if i == 3:
        break
    i = i + 1

else:
    print("Sucessfully exited")