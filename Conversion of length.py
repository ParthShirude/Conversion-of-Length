class Length:

    def __init__(self,value,choice):
        self.value = value
        self.choice = choice

    def Meter(self):
        if self.choice == 1:
            print(f"\nConversion of {self.value} Meter to Centimeter is: {self.value * 100:.3f} cm")
            print(line)

        else:
            print(f"\nCnversion of {self.value} Meter to Millimeter is: {self.value * 1000:.3f} mm")
            print(line)

    def Centimeter(self):
        if self.choice == 3:
            print(f"\nConversion of {self.value} Centimeter to Meter is: {self.value * 0.01:.3f} m")
            print(line)

        else:
            print(f"\nConversion of {self.value} Centimeter to Millimeter is: {self.value * 10:.3f} mm")
            print(line)

    def Millimeters(self):
        if self.choice == 5:
            print(f"\nConversion of {self.value} Millimeter to Centimeter is: {self.value * 0.1:.3f} cm")
            print(line)

        else:
            print(f"\nConversion of {self.value} Millimeter to Meter is: {self.value * 0.001:.3f} m")
            print(line)

def Main():
    while True:

        try:
            print("\nMenu")
            print("1.Meter to Centimeter")
            print("2.Meter to Millimeter")
            print("3.Centimeter to Meter")
            print("4.Centimeter to Millimeter")
            print("5.Millimeter to Centimeter")
            print("6.Millimeter to Meter")
            print("7.Exit")
            
            choice = int(input("\nEnter your choice of conversion: "))

            if choice in [1,2,3,4,5,6]:
                try:
                    value = float(input("\nEnter the value you want to convert to m,cm,mm: "))
                    value = round(value,3)
                    
                    Conversion = Length(value,choice)

                except ValueError:
                    print("\nPlease Enter Integer or float value..........")
                    print(line)
                    continue

            if choice in [1,2]:
                Conversion.Meter()

            elif choice in [3,4]:
                Conversion.Centimeter()

            elif choice in [5,6]:
                Conversion.Millimeters()

            elif choice == 7:
                print("\nThank You!!! For using us for Conversion.........")
                print(line)
                break

            else:
                print("\nInvalid choice!!!!! Please try again..........")
                print(line)

        except ValueError:
            print("\nPlease Enter Integer Value............")
            print(line)


line = "-" * 100
print("Welcome to Length Convertor........")
print("We can convert any integer or float value to m,cm and mm as per your requirement.")
print("NOTE: ")
print("The float Value answers through this program will be only till 3 Decimal places.")
print("The Input will also consider value till 3 decimal places.")
print(line)

Main()

        
