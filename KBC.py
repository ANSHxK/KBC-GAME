name = input(" Enter your name: ")
print("Hello",name,"\n Welocome to KBC! ")
print("Here you will have to give answers to 4 questions and you will win 1CR if all correct and will loose if any one of them is wrong")
Questions = [
     "First question\nWho is the king of the jungle?\n(price for this question 20lakhs)",
     "Second question\nWhich is the oldest country of the world\n(Price for this question 45lakhs)",
     "The third question\nWho is the rechest cricketer of india\n(Price for this question 70lakhs)",
     "Now the final question\nThe best profession of the world\n(Price for this question 1cr)"
]

#Option list
Options=[
      "A.Lion / B.Horse / C.Tiger / D.Cat",
      "A.India / B.Egipt / C.Iran / D.Russia",
      "A.MS Dhoni / B. Virat Kohil / C. Sachin Tendulkar / D.Ravindra Jadeja",
      "A.Fashion Desigener / B. Teacher / C. Pilot / D. Lawer"
]

#Answer list
Answers=["A","C","C","B"]

#Price list
Prices=[2000000,4500000,7000000,10000000]

price=0
i=input("Press enter to start \n")

if(i==""):
    for i in range(4):
        print(Questions[i])
        print("The options are: \n")
        print(Options[i])
        I= input("Enter your option: \n")
        if(I==Answers[i]):
            print(f"WOHOOO Correct Answer \n You won {Prices[i]} RUPEES")
            price=price+Prices[i]
        else:
            print("NICE TRY but your answer is wrong please TRY AGAIN \n The correct answer is:",Answers[i])
            break
    else:
        print("WOHOOOO YOU HAVE WON THE GAME \n")
        print(f"YOU WON TOTAL{(price/10000000)}RUPEES")

print("THANKS FOR PLAYING")
        