import string as st 
import numpy as np  

letras = st.ascii_letters
numeros = st.digits 
caracteres = st.punctuation  
algarismos = letras+numeros+caracteres
senha = np.random.choice(list(algarismos),10)
print("".join (senha))