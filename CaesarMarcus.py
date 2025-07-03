# Knowledge Base for the Marcus and Caesar problem
# Implementation of Knowledge Representation Schemes – Use Case 

class KnowledgeBase:
    def __init__(self):
        # Store facts and rules
        self.facts = {
            'Marcus_is_a_man': True,
            'Marcus_is_a_Pompeian': True,
            'All_Pompeians_are_Romans': True,
            'Caesar_is_a_ruler': True,
            'All_Romans_are_loyal_or_hate_Caesar': True,
            'Everyone_is_loyal_to_someone': True,
            'People_try_assassinate_rulers_they_are_not_loyal_to': True,
            'Marcus_tried_assassinate_Caesar': True
        }
        self.inference_rules = [
            self.is_person,  # Marcus is a person
            self.is_roman,   # Marcus is a Roman
            self.is_loyal_or_hates,  # Marcus is either loyal to Caesar or hates him
            self.try_assassinate,  # Marcus tried to assassinate Caesar
            self.hates_caesar  # Did Marcus hate Caesar?
        ]

    def is_person(self):
        # If Marcus is a man, then Marcus is a person
        if self.facts['Marcus_is_a_man']:
            print("Marcus is a person.")
            self.facts['Marcus_is_a_person'] = True
            return True
        return False

    def is_roman(self):
        # If Marcus is a Pompeian, then Marcus is a Roman
        if self.facts['Marcus_is_a_Pompeian'] and self.facts['All_Pompeians_are_Romans']:
            print("Marcus is a Roman.")
            self.facts['Marcus_is_a_Roman'] = True
            return True
        return False

    def is_loyal_or_hates(self):
        # All Romans are either loyal to Caesar or hate Caesar
        if self.facts['Marcus_is_a_Roman'] and self.facts['All_Romans_are_loyal_or_hate_Caesar']:
            print("Marcus is either loyal to Caesar or hates Caesar.")
            self.facts['Marcus_is_loyal_or_hate'] = True
            return True
        return False

    def try_assassinate(self):
        # If Marcus tried to assassinate Caesar, then Marcus is not loyal to Caesar
        if self.facts['Marcus_tried_assassinate_Caesar']:
            print("Marcus is not loyal to Caesar.")
            self.facts['Marcus_is_not_loyal_to_Caesar'] = True
            return True
        return False

    def hates_caesar(self):
        # If Marcus is not loyal to Caesar, then by the rule, Marcus must hate Caesar
        if self.facts.get('Marcus_is_not_loyal_to_Caesar', False):
            print("By inference, Marcus must hate Caesar.")
            self.facts['Marcus_hates_Caesar'] = True
            return True
        return False

    def perform_inference(self):
        # Go through the rules and apply them
        for rule in self.inference_rules:
            rule()

    def conclusion(self):
        # Final conclusion: Does Marcus hate Caesar?
        if self.facts.get('Marcus_hates_Caesar', False):
            print("Conclusion: Yes, Marcus hated Caesar.")
        else:
            print("Conclusion: No, Marcus did not hate Caesar.")


# Initialize Knowledge Base and Perform Inference
kb = KnowledgeBase()
kb.perform_inference()
kb.conclusion()
