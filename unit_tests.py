from grammar import Pcfg
from cky import *


def test_verify_grammar():
    # Test 1: Valid PCFG Grammar
    with open("test_grammars/toy_grammar.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)

    if grammar.verify_grammar():
        print("Test 1: Valid PCFG Grammar - Passed")
        [print(str(key) + ":", val) for key, val in grammar.rhs_to_rules.items()]
    else:
        print("Test 1: Valid PCFG Grammar - Failed")

    # Test 2: Invalid PCFG Grammar
    with open("test_grammars/invalid_grammar.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)

    if not grammar.verify_grammar():
        print("Test 2: Invalid PCFG Grammar - Passed")
    else:
        print("Test 2: Invalid PCFG Grammar - Failed")


def test_cky_algo():
    with open("test_grammars/toy_grammar.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)
        parser = CkyParser(grammar)
        if parser.is_in_language("she saw the cat with glasses".split()):
            print("Test 3: Language membership - Passed")
        else:
            print("Test 3: Language membership - Failed")


if __name__ == "__main__":
    test_verify_grammar()
    test_cky_algo()
