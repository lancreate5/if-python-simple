import parser as par
import lexical_analyzer as lex

def analyze(words):
    # Start lexical analyzing
    problems = []
    for word in words.split():
        lex_correct, wrong_pos = lex.analyze(word)
        
        if not(lex_correct):
            problems.append(f"{word}\n{' '*(wrong_pos)}^--- Typo here, please check your spelling!")

    print("LEXICAL ANALYSIS REPORT ========")
    if len(problems) == 0:
        print("All clear! No problem detected")
    else:
        print("Looks like there are several problems with your input")
        for problem in problems:
            print(problem)
    print("LEXICAL ANALYSIS DONE!\n")


    # Start grammar parsing
    print("GRAMMAR ANALYSIS REPORT ========")
    par.parse(words.split())
    print("GRAMMAR ANALYSIS DONE!")

def main():
    with open("input.txt", "r") as file:
        for words in file.readlines():
            print("========", "VERIFYING", f"\"{words[:-1]}\"", "========")
            analyze(words)
            print("======== VERIFICATION DONE! ===========\n")

if __name__ == "__main__":
    main()
