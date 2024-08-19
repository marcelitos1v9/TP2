letra = str(input("Digite a letra para saber se é vogal ou consoante"))

match (letra.lower()):
    case 'a','e','i','o','u':
        print(f"{letra} é uma vogal")
    case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z':
        print(f"{letra} é uma consoante")
    
    