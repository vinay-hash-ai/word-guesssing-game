import random


list_easy=["cat","dog","sun","hat","pen","bag","rat","mat","sat","fat"]
list_medium=["cloud","fruit","chair","table","phone","mouse","house","tree","bike","fish"]
list_hard=["beautiful","certificate","dictionary","education","fascinating","phenomenon","quintessential","sophisticated","acknowledgment","disenfranchise"]

print("Welcome to the word guessing game.\nLet's start the game!!")


choose=input("Select any mode in the list[easy,medium,hard]:").strip().lower()

if choose=="easy":
    word=random.choice(list_easy)
    print("easy")
elif choose=="medium":
    word=random.choice(list_medium)
    print("medium")
elif choose=="hard":
    word=random.choice(list_hard)

else:
    print("The mode is invalid.Defaulying to easy mode")
    word=random.choice(list_easy)

print("The no.of letters in the word are ")
print(len(word))

n=1
count=0

for i in word:
    user_input=input("Let's see if can guess the 1st letter:").strip().lower()
    if i==word[0]:
        if user_input==i:
            print("wow your 1st guess is correct!!.You got the luck today")

            count+=1
        else:
            print("Lets make the game a little easier")
            print(f"The 1st letter of the word is {i}")
            
            count+=1
    break
for i in range(1,len(word)+1):
    if n==len(word):
        print(f"Hooray!!\nThe word is {word}")
        print(f"The total no.of guess are {count}")
        break
    while True:
        user_input2=input("Guess next the letter:").strip().lower()

        if user_input2==word[n]:
            print("Your guess is coorect !!.")
            n+=1
            count+=1
            break
        else:
            count+=1
            print("Your guess is incorrect.Guess agian")
