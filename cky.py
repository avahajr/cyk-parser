"""
COMS W4705 - Natural Language Processing - Fall 2023
Homework 2 - Parsing with Probabilistic Context Free Grammars 
Daniel Bauer
"""
import math
import sys
from collections import defaultdict
import itertools
from grammar import Pcfg


### Use the following two functions to check the format of your data structures in part 3 ###
def check_table_format(table):
    """
    Return true if the backpointer table object is formatted correctly.
    Otherwise return False and print an error.
    """
    if not isinstance(table, dict):
        sys.stderr.write("Backpointer table is not a dict.\n")
        return False
    for split in table:
        if (
            not isinstance(split, tuple)
            and len(split) == 2
            and isinstance(split[0], int)
            and isinstance(split[1], int)
        ):
            sys.stderr.write(
                "Keys of the backpointer table must be tuples (i,j) representing spans.\n"
            )
            return False
        if not isinstance(table[split], dict):
            sys.stderr.write(
                "Value of backpointer table (for each span) is not a dict.\n"
            )
            return False
        for nt in table[split]:
            if not isinstance(nt, str):
                sys.stderr.write(
                    "Keys of the inner dictionary (for each span) must be strings representing nonterminals.\n"
                )
                return False
            bps = table[split][nt]
            if isinstance(bps, str):  # Leaf nodes may be strings
                continue
            if not isinstance(bps, tuple):
                sys.stderr.write(
                    "Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Incorrect type: {}\n".format(
                        bps
                    )
                )
                return False
            if len(bps) != 2:
                sys.stderr.write(
                    "Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Found more than two backpointers: {}\n".format(
                        bps
                    )
                )
                return False
            for bp in bps:
                if not isinstance(bp, tuple) or len(bp) != 3:
                    sys.stderr.write(
                        "Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Backpointer has length != 3.\n".format(
                            bp
                        )
                    )
                    return False
                if not (
                    isinstance(bp[0], str)
                    and isinstance(bp[1], int)
                    and isinstance(bp[2], int)
                ):
                    print(bp)
                    sys.stderr.write(
                        "Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Backpointer has incorrect type.\n".format(
                            bp
                        )
                    )
                    return False
    return True


def check_probs_format(table):
    """
    Return true if the probability table object is formatted correctly.
    Otherwise return False and print an error.
    """
    if not isinstance(table, dict):
        sys.stderr.write("Probability table is not a dict.\n")
        return False
    for split in table:
        if (
            not isinstance(split, tuple)
            and len(split) == 2
            and isinstance(split[0], int)
            and isinstance(split[1], int)
        ):
            sys.stderr.write(
                "Keys of the probability must be tuples (i,j) representing spans.\n"
            )
            return False
        if not isinstance(table[split], dict):
            sys.stderr.write(
                "Value of probability table (for each span) is not a dict.\n"
            )
            return False
        for nt in table[split]:
            if not isinstance(nt, str):
                sys.stderr.write(
                    "Keys of the inner dictionary (for each span) must be strings representing nonterminals.\n"
                )
                return False
            prob = table[split][nt]
            if not isinstance(prob, float):
                sys.stderr.write(
                    "Values of the inner dictionary (for each span and nonterminal) must be a float.{}\n".format(
                        prob
                    )
                )
                return False
            if prob > 0:
                sys.stderr.write("Log probability may not be > 0.  {}\n".format(prob))
                return False
    return True


class CkyParser(object):
    """
    A CKY parser.
    """

    def __init__(self, grammar):
        """
        Initialize a new parser instance from a grammar.
        """
        self.grammar = grammar

    def is_in_language(self, tokens):
        """
        Membership checking. Parse the input tokens and return True if
        the sentence is in the language described by the grammar. Otherwise
        return False
        """
        n = len(tokens)

        pi = [[set() for _ in range(n + 1)] for _ in range(n + 1)]
        # Base case: all terminals
        for i in range(n):
            for rule in self.grammar.rhs_to_rules[(tokens[i],)]:
                pi[i][i + 1].add(rule[0])

        # pi now contains the symbols that are derived by all others
        for l in range(2, n + 1):  # l is the length (# tokens) of the subspan
            # print("=" * 50, "\nl =", l)
            # print(" i | k | j ")
            # print("-" * len(" i | j | k "))
            for i in range(n - l + 1):
                j = i + l
                for k in range(i + 1, j):
                    # print(" {} | {} | {} ".format(i, k, j))
                    for left_var in pi[i][k]:
                        for right_var in pi[k][j]:
                            if (
                                left_var,
                                right_var,
                            ) in self.grammar.rhs_to_rules.keys():  # check to avoid keyerror
                                for rule in self.grammar.rhs_to_rules[
                                    (left_var, right_var)
                                ]:
                                    pi[i][j].add(rule[0])  # add the lhs

        return self.grammar.startsymbol in pi[0][-1]

    def parse_with_backpointers(self, tokens):
        """
        Parse the input tokens and return a parse table and a probability table.
        """
        # TODO, part 3
        table = None
        probs = None
        return table, probs


def get_tree(chart, i, j, nt):
    """
    Return the parse-tree rooted in non-terminal nt and covering span i,j.
    """
    # TODO: Part 4
    return None


if __name__ == "__main__":
    with open("atis3.pcfg", "r") as grammar_file:
        grammar = Pcfg(grammar_file)
        parser = CkyParser(grammar)
        toks = ["flights", "from", "miami", "to", "cleveland", "."]
        # print(parser.is_in_language(toks))
        # table,probs = parser.parse_with_backpointers(toks)
        # assert check_table_format(chart)
        # assert check_probs_format(probs)
