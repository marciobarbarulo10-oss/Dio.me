linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)