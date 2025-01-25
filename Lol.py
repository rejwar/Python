# The Code Detective: A Noir Tale

class Detective:
    def __init__(self, name):
        self.name = name
        self.case_open = True
        self.clues = []

    def investigate(self, evidence):
        print(f"{self.name}: Examining evidence...")
        if "encrypted" in evidence.lower():
            self.solve_puzzle(evidence)
        elif "dead code" in evidence.lower():
            self.track_bug(evidence)
        else:
            self.clues.append(evidence)
            print(f"{self.name}: Clue added, but it doesn't make sense yet.")

    def solve_puzzle(self, evidence):
        print(f"{self.name}: This one's locked tight. Time to decrypt...")
        decrypted = evidence.replace("encrypted", "plaintext")
        self.clues.append(decrypted)
        print(f"{self.name}: Deciphered evidence: {decrypted}")

    def track_bug(self, evidence):
        print(f"{self.name}: Dead code, huh? Bugs love hiding there.")
        print(f"{self.name}: Searching for the culprit...")
        print(f"{self.name}: Found it! A misplaced semicolon was causing trouble.")

    def close_case(self):
        if len(self.clues) > 2:
            print(f"{self.name}: With these clues, I can see the pattern.")
            print(f"{self.name}: Case closed. The culprit? It was bad logic all along.")
            self.case_open = False
        else:
            print(f"{self.name}: Not enough clues yet. The case remains open.")


# The City of Code
print("It was a dark and stormy night in the City of Code...")
det = Detective("Inspector Syntax")

# Case unfolds
det.investigate("encrypted message from the Bug Syndicate")
det.investigate("dead code fragment near the Debug District")
det.investigate("mysterious variable with no type")

# Wrapping up
det.close_case()

if not det.case_open:
    print(f"{det.name}: Another case solved. But in the City of Code, there's always another bug.")
