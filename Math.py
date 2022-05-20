while(True):
    
    
    import pyfiglet


    import math

    
    from colorama import Fore, Back, Style

    
    Logo = (pyfiglet.figlet_format("Math.py", font= "puffy"))
    
    
    print(Fore.CYAN,(Logo))
    
    
    print("[ ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 𝕄𝕒𝕙𝕕𝕚 𝔸𝕣𝕚𝕒 ]")
    
    
    print("\n")
    
    
    
    start = input("Baraye Start -s- ro feshar bedid : ")
    
    
    if start == "s":
        
        
        print("[ Bezan Berim ]")
        
        print("\n")
        
        
    else:
        
        
        print("Kellid Dorost Ro Bezan ")
        
        
        continue

    MathOP = input("Yeki az Gozine Haro Entekhab Konid : + jam + ® - menha - ® * zarb * ® / taqsim / ® √ jazr √ : ")
    
    print("\n")
    
    
    if MathOP == "jam":
        
        
        print("[ OK ]")
        
        
        print("\n")
        
        
        one = int(input("Adad Aval : "))
        two = int(input("Adad Dovom : "))
        
        
        print("\n")
        
        
        print(one + two)
        
        
    elif MathOP == "menha":
        
        
        print("\n")
        
        
        print("[ OK ]")
        
        
        print("\n")
        
        
        one2 = int(input("Adad Aval : "))
        two2 = int(input("Adad Dovom : "))
        
        print("\n")
        
        
        print(one2 - two2)
        
        
    elif MathOP == "zarb":
        
        
        print("\n")
        
        
        print("[ OK ]")
        
        
        print("\n")
        
        
        one3 = int(input("Adad Aval : "))
        two3 = int(input("Adad Dovom : "))
        
        
        print("\n")
        
        
        print(one3 * two3)
        
        
    elif MathOP == "taqsim":
        
        
        print("\n")
        
        
        print("[ OK ]")
        
        
        one4 = int(input("Adad Aval : "))
        two4 = int(input("Adad Dovom : "))
        
        
        print("\n")
        
        
        print(one4 / two4)
        
        
    elif MathOP == "jazr":
        
        
        print("\n")
        
        
        print("[ OK ]")
        
        
        print("\n")
        
        
        one5 = int(input("Adad ra Vared Konid : "))
        
        print("\n")
        
        
        print(math.sqrt(one5))
        
        
        print("\n")
        
        
    else:
        
        
        print(" Dorost Vared Konid ")
        
        print("\n")
        
        
    Edame = input("Edame Midi Aya : y/n : ")
    
    
    print("\n")
        
        
    if Edame == "y" or Edame == "yes":
            
            print("\n")
            
            
            print("Kheyli ham Khoub !!! ")
            
            
            continue

    elif Edame == "n" or Edame == "no":
            
            
            print("\n")
            
            
            print("[ Good Bye ] ")
            
            
            print("\n")
    
        
            break