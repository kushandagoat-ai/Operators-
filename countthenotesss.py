Amount=int(input("enter the amount"))
note1=(Amount//100)
note2=(Amount%100)//50
note3=(Amount%100%50)//10
print("100 rupee notes is equal to not", note1)
print("50 rupee notes is equal to not", note2)
print("10 rupee notes is equal to not", note3)