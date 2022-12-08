######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########

sesliler = ['a', 'e', 'i', 'o', 'u']

kelime = "TechProeducation"

found = []

for harf in kelime :
    if harf in sesliler :
        if harf not in found :
            found.append(harf)

for sesli_harf in found :
    print(sesli_harf)

######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########

vowels=['a','e','i','o','u']
word=input("bir kelime giriniz")

found=[]

for letter in word.lower():

    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(found)