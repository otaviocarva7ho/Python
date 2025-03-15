# Fatiamento de Strings (Slicing)
s = "Manipulação"
print(s[0:4])   # Output: Mani
print(s[:5])    # Output: Manip
print(s[5:])    # Output: ulação
print(s[-3:])   # Output: ção

# Comprimento da String (len())
s = "Python"
print(len(s))  # Output: 6

# Conversão para Maiúsculas e Minúsculas
s = "Python"
print(s.upper())  # Output: PYTHON
print(s.lower())  # Output: python
print(s.title())  # Output: Python
print(s.capitalize())  # Output: Python

# Substituição de Parte do Texto (replace())
s = "Eu gosto de Java"
print(s.replace("Java", "Python"))  # Output: Eu gosto de Python

# Remoção de Espaços Extras (strip(), lstrip(), rstrip())
s = "  Python  "
print(s.strip())   # Output: "Python"
print(s.lstrip())  # Output: "Python  "
print(s.rstrip())  # Output: "  Python"

# Verificação de Prefixo e Sufixo (startswith(), endswith())
s = "programador.py"
print(s.startswith("pro"))  # Output: True
print(s.endswith(".py"))    # Output: True

# Separação e Junção de Strings (split(), join())
s = "Python é incrível"
palavras = s.split()  # Divide por espaço
print(palavras)  # Output: ['Python', 'é', 'incrível']

juncao = "-".join(palavras)
print(juncao)  # Output: Python-é-incrível

# Encontrar Substrings (find(), index())
s = "Programação Python"
print(s.find("Python"))  # Output: 13 (posição inicial)
print(s.index("Python")) # Output: 13 (igual ao find, mas gera erro se não achar)

# s = "Programação Python"
print(s.find("Python"))  # Output: 13 (posição inicial)
print(s.index("Python")) # Output: 13 (igual ao find, mas gera erro se não achar)

# Contagem de Ocorrências (count())
s = "banana"
print(s.count("a"))  # Output: 3

# Verificar se é Número, Letra ou Alfanumérico
print("12345".isdigit())  # Output: True
print("abc".isalpha())    # Output: True
print("abc123".isalnum()) # Output: True
print(" ".isspace())      # Output: True

