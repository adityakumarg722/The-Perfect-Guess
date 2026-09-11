import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("guesse the number: "))
    if(a>n):
        print("lower number please")
    else:
        print("higher number please")
print(f"you have guessed the number {n} correctly in {guesses} attempt")