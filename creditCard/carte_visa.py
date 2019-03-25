# coding: utf8
class carte_visa():

    
    def  Verifier_numero_carte(self,numeros):
        
        try:
            int(numeros)
        except ValueError:
            exit("La saisie n'est pas un nombre (sans espace) !")

        if len(numeros) != 15 and len(numeros) != 16:

            exit("La Longueur du numéro de la carte ne doit pas ni superieur ni inferieur à 15 et 16 !")

        sum = 0
        num_length = len(numeros)
        oddeven = num_length & 1

        for compteur in range(0, num_length):

            digit = int(numeros[compteur])

            if not ((compteur & 1) ^ oddeven):
                digit *= 2
            if digit > 9:
                digit -= 9

            sum += digit

            reste= sum % 10 
       
         
        ## Vérification avec la clé
        if reste == 0:
            print("Le numéro de cette carte vérifie l'algorithme de luhn , Correct !")
            if num_length>=13 and num_length<=16:
               if ''.join(numeros[:2]) in strings_entre(40,41):
                  print("elle est aussi une carte Visa")

               else: print("Mais elle n'est pas une carte Visa")
        else:
            
            print(" Le numéro de cette carte ne vérifie pas l'algorithme de Luhn donc il est incorrect ")
 
        
    
#cette fonction génére la liste de caractères des deux premiers
# Pour verifier s'il repecte la norme de commencement de chaque type 
#carte Bancaire

def strings_entre(a, b):
        """Générer la liste de sting entre a et b."""
        return list(map(str, range(a, b)))

carteVisa = carte_visa()
carteVisa.Verifier_numero_carte("4024007146302608")
