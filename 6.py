#Using try..except book

print("Practicing for try block")

try:
    numerator=50
    denom=int(input("Enter the denominotor"))
    quotient=(numerator/denom)
    print(quotient)
    print("Division performed successfully")

except ZeroDivisionError :
    if ZeroDeno==0:
        print("Denominator as Zero....not sllowed")
    else:
        print("OUTSIDE try..except block")

