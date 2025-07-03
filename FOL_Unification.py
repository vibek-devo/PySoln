def unify(x, y, subs={}):
    # Base case: If both terms are the same, return current substitutions
    if x == y:
        return subs

    # If one of the terms is a variable (lowercase string), unify it with the other term
    if isinstance(x, str) and x.islower():
        return unify_var(x, y, subs)
    if isinstance(y, str) and y.islower():
        return unify_var(y, x, subs)

    # If both terms are tuples and the first elements match (predicate names)
    if isinstance(x, tuple) and isinstance(y, tuple) and x[0] == y[0]:
        # Recursively unify the rest of the arguments in the predicates
        for a, b in zip(x[1:], y[1:]):
            subs = unify(a, b, subs)
            if subs is None:  # If unification fails, return None
                return None
        return subs  # Return the resulting substitutions

    return None  # If terms cannot be unified, return None

def unify_var(var, x, subs):
    # If the variable is already substituted, continue unification
    if var in subs:
        return unify(subs[var], x, subs)
    # If the term x is already substituted, continue unification
    elif x in subs:
        return unify(var, subs[x], subs)
    else:
        # If no prior substitution exists, create a new substitution
        subs[var] = x
        return subs

# Function to get user input and unify terms
def get_input():
    print("Unification of FOL terms")
    print("Example format: ('predicate', 'arg1', 'arg2')")

    # Take user input for two logical terms
    term1_input = input("Enter first term (e.g., ('knows', 'john', 'X')): ")
    term2_input = input("Enter second term (e.g., ('knows', 'john', 'mary')): ")

    # Convert input strings to tuples (parse arguments)
    term1 = eval(term1_input)
    term2 = eval(term2_input)

    # Perform unification
    print("\nAttempting to unify the terms:")
    print("Term 1:", term1)
    print("Term 2:", term2)
    
    subs = unify(term1, term2)
    
    if subs is not None:
        print("Unification result:", subs)
    else:
        print("Unification failed. The terms cannot be unified.")

# Function for resolving clauses based on unification
def resolve_clause(clause1, clause2):
    # Unify the two clauses
    print("\nAttempting resolution between clauses:")
    print("Clause 1:", clause1)
    print("Clause 2:", clause2)

    subs = unify(clause1, clause2)
    if subs is not None:
        print("Resolution successful. Substitution:", subs)
    else:
        print("Resolution failed. The clauses cannot be resolved.")

# Run the unification and resolution process
def main():
    get_input()
    
    # Example for resolution: Two clauses
    clause1 = ('knows', 'john', 'X')
    clause2 = ('knows', 'john', 'mary')
    
    resolve_clause(clause1, clause2)

# Run the program
main()
