height=int(input('ENTER YOUR HEIGHT IN CENTIMETRES:'))
bill=0
if height>=120:
    print("PLEASE ENJOY YOUR RIDE")
    age=int(input('ENTER YOUR AGE:'))
    if age<12:
        bill=5
        print("YOUR TICKET PRICE IS $5")
    elif age<=18:
        bill=7
        print("YOUR TICKET PRICE IS $7")
    elif age<=60:
        bill=12
        print("YOUR TICKET PRICE IS $12")
wants_photo=input("do you want a photo taken? Y or N:")
if wants_photo=="Y":
    bill+=3
    print(f"your final bill is ${bill}")       
else:
    print("sorry,but you need to be taller")