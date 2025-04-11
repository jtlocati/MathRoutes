import time
import random
import math

class NoteSpaceBioM:
    @staticmethod
    def main(args=None):
        # Create an instance of NoteSpaceBioM (though not used later, preserved from original)
        player = NoteSpaceBioM()
        # Scanner sc = new Scanner(System.in); is replaced by direct use of input() in Python
        ContFunc = True
        seperator = "................................"
        while(ContFunc == True):
            print("______")
            print("biomed test 3.1 -> 3.3")
            print("(1)flow of blood through the body")
            print("(2)Conduction system")
            print("(3)EKG components")
            print("(4)Equastions")
            print("(5)")
            print("(6)Force Flood")
            print("(7)Force Quit")
            print(">", end="")
            chooser = int(input())
            if(chooser == 7):
                print("QUITTING....")
                time.sleep(0.2)
                for i in range(30):
                    print(" ")
                print("____________________")
                ContFunc = False
            elif(chooser == 6):
                print("IMPORTANT:\n to retun back to NERVcalc enter passkey\n there will be no prompt")
                time.sleep(4)
                for i in range(20):
                    Scabies = int(random.random() * 5) + 0
                    if(Scabies == 1):
                        print("123/45\n" + seperator)
                        print("                           2.733")
                        print(seperator)
                    elif(Scabies == 2):
                        print("124+34\n" + seperator)
                        print("                            158")
                        print(seperator)
                    elif(Scabies == 3):
                        print("10 x 6 + 10\n" + seperator)
                        print("                            " + str(10*6+10))
                        print(seperator)
                    elif(Scabies == 4):
                        print("12 + 67\n" + seperator)
                        print("                              " + str(12 + 67))
                        print(seperator)
                    elif(Scabies == 5):
                        print("log(20)\n" + seperator)
                        print("                              1.3")
                        print(seperator)
                cont = int(input())
                if(cont == 4922):
                    print("USER IMP REC...")
                    time.sleep(0.2)
                    print("REDIRECTING...")
                    time.sleep(2)
                    print("__________")
                else:
                    print("this aint it fam")
            elif (chooser == 1):
                print(seperator)
                print("Right Atrum => Tricuspid valve")
                print("Right ventrical => Pulmanary val")
                print("pulmanary art => lungs => O2 <-> co2")
                print("Pulmanary vein => left atrium")
                input()
                print("Mitral => Left Ven => Aortic ven")
                print("Arota => Systemic Artaoies ")
                print("Systemic capill => O2 <-> Co2")
                print("Systemic ven => Systemic veins")
                print("vana cava")
                print("enter any number to see functions")
                input()
                print("Right Atrium")
                print("Receives deoxygenated blood from the body")
                input()
                print("Tricuspid Valve")
                print("Prevents backflow into right atrium")
                input()
                print("Right Ventricle")
                print("Pumps blood to lungs")
                input()
                print("Pulmonary Valve")
                print("Controls blood flow into pulmonary artery")
                input()
                print("Pulmonary Artery")
                print("Carries deoxygenated blood to lungs")
                input()
                print("Lungs")
                print("Exchange CO₂ for O₂")
                input()
                print("Pulmonary Vein")
                print("Returns oxygenated blood to heart")
                input()
                print("Left Atrium")
                print("Receives oxygenated blood from lungs")
                input()
                print("Mitral (Bicuspid) Valve")
                print("Prevents backflow into left atrium")
                input()
                print("Left Ventricle")
                print("Pumps oxygenated blood to the body")
                input()
                print("Aortic Valve")
                print("Controls blood flow into aorta")
                input()
                print("Aorta")
                print("Distributes oxygenated blood to body")
                input()
                print("Systemic Arteries")
                print("Carry oxygen-rich blood to tissues")
                input()
                print("Systemic Arterioles")
                print("Regulate blood flow to capillaries")
                input()
                print("Systemic Capillaries")
                print("Exchange oxygen and nutrients with cells")
                input()
                print("Systemic Venules")
                print("Collect deoxygenated blood from tissues")
                input()
                print("Systemic Veins")
                print("Return blood to the heart")
                input()
                print("Inferior/Superior Vena Cava")
                print("Bring deoxygenated blood to right atrium")
                input()
            elif(chooser == 2):
                print(seperator)
                print("SA Node => AV Node")
                print("Bundle of His => Right Bundle Branch")
                print("Left Bundle Branch => Purkinje Fibers")
                input()
            elif(chooser == 3):
                print("___/\\__u/\\u__/\\")
                print("   P    Q R S   T")
                input()
        # In Python, there's no need to close an input scanner.
        
# For TI-84 ce plus python calculator compatibility, the main() function is defined below.
def main():
    NoteSpaceBioM.main()
    
# Calling main() if this script is run directly.
if __name__ == "__main__":
    main()

