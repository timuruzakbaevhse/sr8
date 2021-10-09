a=int(input("Введите ваше число:" ))
n=int(input("Введите целевую систему счисления:"))

def hw(a,n):
    s = ""
    while a > 0:
        s = str(a % n) + s
        a //= n
    return s
print("Ответ:",a,"->",hw(a,n))    

  
