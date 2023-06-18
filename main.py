import lexical_analyzer as lex
import parser as par

def main():
    with open("input.txt", "r") as file:
        for words in file.readlines():
            print(words[:-2], "========")
            for word in words.split():
                correct, ptr = lex.analyze(word)
                if not(correct):
                    print(f"{word}")
                    print(f"{' '*(ptr)}^--- Typo here, please check your spelling!")
            print("DONE ========\n")

if __name__ == "__main__":
    main()
