class Emp:
    def __init__(self,name,salary,sft):
        self.name=name 
        self.salary=salary 
        self.sft=sft
    def show(self):
         
        if self.sft<1000 :
            print("!!!SORRY ",self.name," YOU CANT HAVE ANY BONUS THIS MONTH TRY AGAIN NEXT MONTH!!!")
        elif self.sft>=1000 and self.sft<=10000 :
            print("***WELL DONE",self.name,"YOU WILL GET ",self.salary,"PLUS BONUS OF 2000 MEANS YOUR SALARY IS ",self.salary+1000 ,"***")
        elif self.sft>=10000 and self.sft<=20000:
            print("***WELL DONE",self.name,"YOU WILL GET ",self.salary,"PLUS BONUS OF 2000 MEANS YOUR SALARY IS ",self.salary+2000 ,"***")    
        elif self.sft>=20000 and self.sft<=40000 :
            print("***WELL DONE",self.name,"YOU WILL GET ",self.salary,"PLUS BONUS OF 2000 MEANS YOUR SALARY IS ",self.salary+4000 ,"***")
        elif self.sft>=40000 and self.sft<=60000 :
            print("***WELL DONE",self.name,"YOU WILL GET ",self.salary,"PLUS BONUS OF 2000 MEANS YOUR SALARY IS ",self.salary+6000 ,"***")
        elif self.sft>=60000 and self.sft<=80000 :
            print("***WELL DONE",self.name,"YOU WILL GET ",self.salary,"PLUS BONUS OF 2000 MEANS YOUR SALARY IS ",self.salary+8000 ,"***")     
        elif self.sft>=80000 and self.sft<=100000 :
            print("***WELL DONE",self.name,"YOU WILL GET ",self.salary,"PLUS BONUS OF 2000 MEANS YOUR SALARY IS ",self.salary+10000, "***")    
        elif self.sft>100000:
            print("**CONTACT TO MANAGER MR. ",self.name," FOR THAT MUCH SALES ",self.sft," ***")    
while True:
    print("*****CREATED BY FATHERPRINCE*****")
    o=int(input('''
     PRESS 1 TO KNOW YOUR THIS MONTH BONUS 
     PRESS 2 FOR EXIT\n'''))
    if o==1:
        n=input("ENTER YOUR NAME\n")
        n=n.capitalize()
        s=int(input("ENTER SALARY\n"))
        sft=int(input("ENTER THiS MONTH SALE THIS CANT BE EMPTY IF ZERO INPUT 0\n"))
        emp=Emp(n,s,sft)
        emp.show()
    else:
        break
        
    
    
   
    