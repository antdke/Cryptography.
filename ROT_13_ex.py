# Anthony Dike Aug 15 2018
# rough idea of what the ROT-13 encryption principle is

# THE ENCRYPTION PROCESS
def ROT_13(phrase):

    def input_phrase(function_phrase):
        encrypted_phrase = ""
        for n in range(len(phrase)):
            letter = phrase[n]
            if letter == " ":
                encrypted_phrase += " "
                continue
            encrypted_phrase += letter_to_number(phrase[n])
        return encrypted_phrase

    def letter_to_number(letter):
        encrypted_letter = ""
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for n in range(len(alphabet)-1):
            if letter == alphabet[n]:
                if n > 12:
                    encrypted_letter = alphabet[n - 13]
                else:
                    encrypted_letter = alphabet[n + 13]
        return encrypted_letter

    return input_phrase(phrase)

# START
print("HELLO...")
print("\tI Am The ROT-13 Encryption Machine.\n")
print("\tTHIS IS HOW I WORK:")
print("\t\t...I Take A Letter In The Alphabet,")
print("\t\t   Then I Magically Turn It Into The")
print("\t\t   Letter 13 Slots Down In The Alphabet!\n\n")
print("\t\t   Isn't That Cool? :D\n\n")
print("\t\t   For Example:")
print("\t\t\t If You Gave Me Letter 'a' then")
print("\t\t\t I Would Turn It Into The Letter 'n'\n")
print("\t\t\t Or If You Gave Me Letter 'b' then")
print("\t\t\t I Would Turn It Into The Letter 'o'")
print("\t\t\t And So On!\n\n")
print("\t\t   If You Still Don't Understand, Don't Worry!")
print("\t\t   You Will When I Take Your Jo-")
print("\t\t   I Mean, You Will Eventually :)\n\n")
print("\t   Write Something Below To Experience How I Work...\n")


# ENCRYPTION TEST
phrase = input("Write Anything :) --> ")
print()
print("Now This Is Your Phrase Encrypted Using The ROT-13 Principle:")
print(">>>",ROT_13(phrase),"<<<")
print()

# DECODING TEST
print("Now I'm Going To Decode It Back To It's Original Form.")
encrypted_phrase = ROT_13(phrase)
print(">>>",ROT_13(encrypted_phrase),"<<<")
print()

print("It's Like Magic!")
print("I Hope You Enjoyed That Experience :D")
print("See You Next Time!!")
