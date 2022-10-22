print("This is a program related to geometric series \n focusing on the particular concept of special series of the form \n x+xx+xxx+xxxx+.... up to n number of terms.")
x=int(input("enter value for x for series x+xx+xxx+xxxx+....:"))
num_t=int(input("enter number of terms:"))

for i in range(0,num_t,1):

    t=x**i
    p=x*t
    print("term", i+1 ,"=", p)

d_=0
print("\n the corresponding series for the given sequence given by the sum of :- \n")

for j in range(0,num_t,1):

    t_=x**j
    p_=x*t_
    print(p_ ,end =' ')
    d_+=p_

print("\n sum of the series => " , d_)


        







        

        

    
