n = int(input())  # represents the number of integers in the list.
numb = input()  # is a space-separated string of integers.
lis = list(map(int, numb.split()))  # convert into list 

max_score, max_score2 = -6000, -6000  # Initialize the largest and second largest numbers

for i in lis:
    if i > max_score:
        max_score, max_score2 = i, max_score  # Update max_score and shift old max_score to max_score2
    elif max_score > i > max_score2:
        max_score2 = i  # Update max_score2 if i is between max_score and max_score2

print(max_score2)  # Print the second largest number
