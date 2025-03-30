import string

stringText = """The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."""

tabela = str.maketrans("", "", string.punctuation)
lista = stringText.translate(tabela).lower().split()

listaSeparada = [i for i in lista if len(i) > 4 and any(char in i for char in "python")]

print(listaSeparada)