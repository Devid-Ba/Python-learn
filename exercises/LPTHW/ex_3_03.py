score = input("Enter Score: ")
try:
    sc = float(score)
except:
    print("error enter value between 0.0 and 1.0")

if sc >= 0.9 :
    print("A")
elif sc >= 0.8 :
    print("B")
elif sc >= 0.7 :
    print("c")
elif sc>= 0.6 :
    print("D")
elif sc < 0.6 :
    print("F")
elif sc >= 1.1 :
    print("error enter value between 0.0 and 1.0")
