# Projet-2-2019-DP--CreditCard
Vérification d'un numéro de carte bancaire et son type
  ## Carte Bancaire
  Ce projet est un module de python capable valider et determiner le format des numéros des cartes bancaire 
 à l'aide de l'algorithme de luhn
   ## Detail du projet 
 Ce projet comporte 5 classes : Verificateur, carteVisa, MarterCard, AmercianEpxpress et Banque
  ### La classe Verificateur
 Elle es une interface qui a la methode Verifier_numero_carte(numeros) avec comme paramètre numeros
  ### les classes carteVisa, MarterCard, AmercianEpxpress
 Ces classes heritent l'interface Verificateur pour implémenter la méthode verifier_numero_carte(numeros)
   #### verifier_numero_carte(numeros)
Cette méthode est utilisée pour valider des cartes de crédit et calculer le chiffre de contrôle Luhn pour un numéro donné.
Une fois que ce numéro correspond au numéro de carte de crédit, elle vérifie la longueur et les deux premiers chiffre qui
qui le commencent afin de donner le type de carte s'agit il.
 --> Si elle retourne marterCard çaa signifie que les deux chiffres de commencement sont compris en 51 et 56 et que la 
 longueur ne dépasse pas l'intervalle 16 eT 19.
 --> Si elle retourne Visa çaa signifie que les deux chiffres de commencement sont compris en 41 et 41 et que la 
 longueur ne dépasse pas l'intervalle 13 eT 16.
 --> Si elle retourne marterCard ça a signifie que les deux chiffres de commencement sont compris en 30 et 39 et que la 
 longueur ne dépasse pas l'intervalle 16 eT 17.
 
 Dans le cas contraire c'est-à-dire le numéro ne verifie pas l'algorithme de Luhn et ne respecte la longueur ce chaque 
 alors programme s'arrete en affichant le message:" Le numéro de cette carte ne vérifie pas l'algorithme de Luhn donc il est incorrect" 
   #### strings_entre(a,b)
  cette methode permet de verifier l'intervalle d'appartenance des deux premiers chiffres qui commencent le numéro
  
  ### la classe Banque
 C'est cette classe qui fournit le numéro des cartes et elle possedent un attribit de type verificateur
   
  ### Importation
 Pour importer un module en python, on écrit : import verificateur qui signifie que la classe veirificateur est importer dans la classe Banque si cette expression est ajoutée dans cette dernière 
