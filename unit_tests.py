from grammar import Pcfg

def test_verify_grammar():
    # Test 1: Valid PCFG Grammar
    with open('unit_tests/toy_grammar.pcfg', 'r') as grammar_file:
        grammar = Pcfg(grammar_file)
    
    if grammar.verify_grammar():
        print("Test 1: Valid PCFG Grammar - Passed")
    else:
        print("Test 1: Valid PCFG Grammar - Failed")

    # Test 2: Invalid PCFG Grammar
    with open('unit_tests/invalid_grammar.pcfg', 'r') as grammar_file:
        grammar = Pcfg(grammar_file)
    
    if not grammar.verify_grammar():
        print("Test 2: Invalid PCFG Grammar - Passed")
    else:
        print("Test 2: Invalid PCFG Grammar - Failed")

if __name__ == '__main__':
    test_verify_grammar()