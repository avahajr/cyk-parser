from grammar import Pcfg
from cky import *
import os


def test_verify_grammar():
    # Test 1: Valid PCFG Grammar
    with open("test_grammars/toy_grammar.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)

        if grammar.verify_grammar():
            print("Test 1: Valid PCFG Grammar - Passed")
            # [print(str(key) + ":", val) for key, val in grammar.rhs_to_rules.items()]
        else:
            print("Test 1: Valid PCFG Grammar - Failed")

    with open("test_grammars/toy.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)

        if grammar.verify_grammar():
            print("Test 2: Another Valid PCFG Grammar - Passed")
            # [print(str(key) + ":", val) for key, val in grammar.rhs_to_rules.items()]
        else:
            print("Test 2: Another Valid PCFG Grammar - Failed")

    # Test 2: Invalid PCFG Grammar
    with open("test_grammars/invalid_grammar.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)

    if not grammar.verify_grammar():
        print("Test 3: Invalid PCFG Grammar - Passed")
    else:
        print("Test 3: Invalid PCFG Grammar - Failed")


def test_cky_algo():
    with open("test_grammars/toy_grammar.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)
        parser = CkyParser(grammar)
        if parser.is_in_language("she saw the cat with glasses".split()):
            print("Test 4: Language membership - Passed")
        else:
            print("Test 4: Language membership - Failed")
    with open("test_grammars/toy.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)
        parser = CkyParser(grammar)
        if parser.is_in_language("she saw the cat with glasses".split()):
            print("Test 5: Language membership - Passed")
        else:
            print("Test 5: Language membership - Failed")


def test_backpointers(testfiles):
    for i, filename in enumerate(testfiles, start=6):
        with open(filename, "r") as grammar_file:
            grammar = Pcfg(grammar_file)
            if grammar.verify_grammar():
                parser = CkyParser(grammar)
                table, probs = parser.parse_with_backpointers(
                    "she saw the cat with glasses".split()
                )
                if check_probs_format(probs):
                    print("Test {}.1: Probs format ({}) - Passed".format(i, filename))
                else:
                    print(
                        "** ERR - Test {}.1: Probs format ({}) - FAILED".format(
                            i, filename
                        )
                    )
                    exit(1)
                if check_table_format(table):
                    print("Test {}.2: Table format ({}) - Passed".format(i, filename))
                else:
                    print(
                        "** ERR - Test {}.2: Table format ({}) - FAILED".format(
                            i, filename
                        )
                    )
                    exit(1)
            else:
                print("Test {}: Invalid grammar ({})".format(i, filename))


if __name__ == "__main__":
    test_files = map(lambda x: "test_grammars/" + x, os.listdir("test_grammars"))
    print(test_files)
    test_verify_grammar()
    test_cky_algo()
    test_backpointers(test_files)
    print("All unit tests passed.")
