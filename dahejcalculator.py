dowry = 0
print("welcome to dahej calculator , know your worth !")
dahej = input("do you want dahej? yes or no:")

if dahej == "yes":
    print("nark mei jaloge ,khair....")

    job = input("what sector do you work in? private or govt :")
    if job == "private":
        print("toh bhaiya bhul hi jao dahej ")
        dowry += 0
    elif job == "govt":

        dowry += 100000
        print("fortuner denge aapko ")

    cattle = int(input("how many cattles do you have?[range 0 - 1000] :"))
    if cattle > 100 :
        dowry += 0
        print("cycle milegi")
    elif cattle < 100 :
        dowry +=50000

    elif cattle >=500 and cattle <1000 :
        dowry += 100000

    land = int(input("how many acres of lands do you have?[range 1 - 100] :"))
    if land <1 :
        dowry +=80000
        print("ek tola sona ")
    elif land <10 :
        dowry +=800000
        print("10 tola sona ")
    elif land >=100 :
        dowry +=1200000
        print("saala free milega dhek bhaal ke liye")



print(dowry)
