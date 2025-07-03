class CSP:
    def __init__(self, variables, domains, constraints):
        """
        Initialize a CSP problem
        
        Args:
            variables: List of variables in the problem
            domains: Dictionary mapping variables to their possible values
            constraints: Dictionary mapping variables to their constraints
        """
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}  # Current assignment of values
        self.backtrack_count = 0  # Count of backtrack operations
        
    def is_complete(self):
        """Check if the current assignment is complete"""
        return len(self.assignment) == len(self.variables)
    
    def is_consistent(self, variable, value):
        """Check if assigning value to variable is consistent with current assignment"""
        # Check all constraints involving variable
        for constraint in self.constraints.get(variable, []):
            neighbor = constraint['neighbor']
            if neighbor in self.assignment:
                # If the constraint is violated, return False
                if not constraint['check'](value, self.assignment[neighbor]):
                    return False
        return True
    
    def select_unassigned_variable(self):
        """Select an unassigned variable - using minimum remaining values (MRV) heuristic"""
        # Find unassigned variables
        unassigned = [v for v in self.variables if v not in self.assignment]
        
        if not unassigned:
            return None
        
        # Use MRV heuristic - select variable with smallest domain
        return min(unassigned, key=lambda var: len(self.get_remaining_values(var)))
    
    def get_remaining_values(self, variable):
        """Get domain values that are still valid for variable"""
        return [value for value in self.domains[variable] 
                if self.is_consistent(variable, value)]
    
    def backtracking_search(self):
        """Backtracking search algorithm"""
        return self._backtrack()
    
    def _backtrack(self):
        """Recursive backtracking search"""
        if self.is_complete():
            return self.assignment
        
        # Select unassigned variable
        var = self.select_unassigned_variable()
        
        # Try each value in the domain
        for value in self.domains[var]:
            # Check if the value is consistent with current assignment
            if self.is_consistent(var, value):
                # Assign value to variable
                self.assignment[var] = value
                
                # Recursively continue
                result = self._backtrack()
                if result:
                    return result
                
                # If no solution, backtrack
                self.backtrack_count += 1
                del self.assignment[var]
        
        return None


class MapColoringCSP:
    def __init__(self):
        self.regions = []
        self.colors = []
        self.neighbors = {}
        self.csp = None
    
    def setup_from_user_input(self):
        """Set up the map coloring problem from user input"""
        print("=== Map Coloring CSP Setup ===")
        
        # Get regions
        print("\nEnter the regions/countries to color (separated by spaces):")
        self.regions = input("> ").strip().split()
        
        # Get colors
        print("\nEnter the available colors (separated by spaces):")
        self.colors = input("> ").strip().split()
        
        # Get adjacency information
        print("\nNow specify which regions are adjacent to each other.")
        print("For each region, enter the adjacent regions separated by spaces.")
        
        self.neighbors = {}
        for region in self.regions:
            print(f"\nRegions adjacent to {region}:")
            adjacent = input("> ").strip().split()
            self.neighbors[region] = adjacent
        
        # Set up domains - all regions can have any color initially
        domains = {region: self.colors.copy() for region in self.regions}
        
        # Set up constraints - adjacent regions must have different colors
        constraints = {}
        for region, adjacent_regions in self.neighbors.items():
            if region not in constraints:
                constraints[region] = []
            
            for adj in adjacent_regions:
                # Skip if not in our regions list
                if adj not in self.regions:
                    continue
                
                # Add constraint: adjacent regions must have different colors
                constraints[region].append({
                    'neighbor': adj,
                    'check': lambda x, y: x != y
                })
                
                # Add the reverse constraint as well
                if adj not in constraints:
                    constraints[adj] = []
                constraints[adj].append({
                    'neighbor': region,
                    'check': lambda x, y: x != y
                })
        
        # Create the CSP
        self.csp = CSP(self.regions, domains, constraints)
        
        print("\nMap Coloring CSP set up successfully!")
        self.print_map_info()
    
    def print_map_info(self):
        """Print information about the map"""
        print("\n=== Map Information ===")
        print(f"Regions: {', '.join(self.regions)}")
        print(f"Colors: {', '.join(self.colors)}")
        print("\nAdjacency Information:")
        for region, adjacent in self.neighbors.items():
            print(f"  {region} is adjacent to: {', '.join(adjacent)}")
    
    def solve(self):
        """Solve the map coloring problem"""
        print("\n=== Solving Map Coloring Problem ===")
        
        if not self.csp:
            print("Error: CSP not set up yet!")
            return
        
        # Solve using backtracking
        solution = self.csp.backtracking_search()
        
        if solution:
            print("\n=== Solution Found! ===")
            print("\nColor assignments:")
            for region, color in solution.items():
                print(f"  {region}: {color}")
            
            print(f"\nBacktracks: {self.csp.backtrack_count}")
            
            # Check if the solution is valid
            self.verify_solution(solution)
        else:
            print("\nNo solution found! This map cannot be colored with the given colors.")
    
    def verify_solution(self, solution):
        """Verify that the solution is valid (no adjacent regions have same color)"""
        is_valid = True
        violations = []
        
        for region, adjacent in self.neighbors.items():
            for adj in adjacent:
                if adj in self.regions and solution.get(region) == solution.get(adj):
                    is_valid = False
                    violations.append((region, adj))
        
        if is_valid:
            print("\nVerification: The solution is valid! ✓")
        else:
            print("\nVerification: The solution has conflicts! ✗")
            print("Conflicts:")
            for r1, r2 in violations:
                print(f"  {r1} and {r2} have the same color: {solution.get(r1)}")
    
    def provide_example(self):
        """Set up an example map coloring problem"""
        print("\n=== Setting up Example Map Coloring Problem ===")
        
        # Australia map coloring example
        self.regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
        self.colors = ['red', 'green', 'blue']
        
        self.neighbors = {
            'WA': ['NT', 'SA'],
            'NT': ['WA', 'SA', 'Q'],
            'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
            'Q': ['NT', 'SA', 'NSW'],
            'NSW': ['Q', 'SA', 'V'],
            'V': ['SA', 'NSW'],
            'T': []  # Tasmania is an island
        }
        
        # Set up domains - all regions can have any color initially
        domains = {region: self.colors for region in self.regions}
        
        # Set up constraints - adjacent regions must have different colors
        constraints = {}
        for region, adjacent_regions in self.neighbors.items():
            constraints[region] = []
            for adj in adjacent_regions:
                constraints[region].append({
                    'neighbor': adj,
                    'check': lambda x, y: x != y
                })
        
        # Create the CSP
        self.csp = CSP(self.regions, domains, constraints)
        
        print("Example set up: Australia map coloring problem")
        self.print_map_info()


def main():
    print("Constraint Satisfaction Problem Solver: Map Coloring")
    print("1. Set up your own map coloring problem")
    print("2. Use an example map coloring problem (Australia)")
    
    choice = input("\nSelect an option (1 or 2): ")
    
    map_csp = MapColoringCSP()
    
    if choice == '1':
        map_csp.setup_from_user_input()
    else:
        map_csp.provide_example()
    
    print("\nReady to solve? (press Enter)")
    input()
    
    map_csp.solve()

if __name__ == "__main__":
    main()

















#     Constraint Satisfaction Problem Solver: Map Coloring
# 1. Set up your own map coloring problem
# 2. Use an example map coloring problem (Australia)

# Select an option (1 or 2): 2

# === Setting up Example Map Coloring Problem ===
# Example set up: Australia map coloring problem

# === Map Information ===
# Regions: WA, NT, SA, Q, NSW, V, T
# Colors: red, green, blue

# Adjacency Information:
#   WA is adjacent to: NT, SA
#   NT is adjacent to: WA, SA, Q
#   SA is adjacent to: WA, NT, Q, NSW, V
#   Q is adjacent to: NT, SA, NSW
#   NSW is adjacent to: Q, SA, V
#   V is adjacent to: SA, NSW
#   T is adjacent to: 

# Ready to solve? (press Enter)

# === Solving Map Coloring Problem ===

# === Solution Found! ===

# Color assignments:
#   WA: red
#   NT: green
#   SA: blue
#   Q: red
#   NSW: green
#   V: red
#   T: red

# Backtrack operations: 0

# Verification: The solution is valid! ✓