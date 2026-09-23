class testclass1():
    def Subfields():
        List=["Machine Learning","Neural Networks","Vision Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:",)
        for Subfields in List:
            print(Subfields)
        return List
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even number")
            message="Even number"
        else:
            print(num,"is Odd number")
            message="Odd number"
        return message
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        for Eligible in Gender,Age:
            if(Gender=="Male" and Age>21):
                print("Eligible")
                Eligible="Eligible"
            elif(Gender=="Female"and Age>18):
                print("Eligible")
                Eligible="Eligible"
            else:
                print("Not Eligible")
                Eligible="Not Eligible"
            return Eligible
    def percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
        total=S1+S2+S3+S4+S5
        percentage=(total/500)*100
        print("Total:",total)
        print("Percentage:",percentage)
        return total,percentage
    def triangle():
        Height=32
        Breadth=34
        Area=(Height*Breadth)/2
        print("Height:",Height)
        print("Breadth:",Breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", Area)
        Height1=2
        Height2=4
        Breadth=4
        Perimeter=Height1+Height2+Breadth
        print("Height1:",Height1)
        print("Height2:",Height2)
        print("Breadth:",Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter)
        return Area,Perimeter