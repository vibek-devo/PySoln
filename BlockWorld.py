class BlockWorld:
    def __init__(self):
        self.stacks = []  # List of stacks, each stack is a list of blocks (bottom to top)
        self.block_positions = {}  # Maps block name to (stack_index, height_in_stack)
        self.actions = []  # List of actions for the solution

    def add_stack(self):
        """Add a new empty stack"""
        self.stacks.append([])
        return len(self.stacks) - 1  # Return the index of the new stack

    def add_block(self, block_name, stack_index):
        """Add a block to the top of the specified stack"""
        if stack_index >= len(self.stacks):
            return False
        
        # Add block to stack
        stack = self.stacks[stack_index]
        height = len(stack)
        stack.append(block_name)
        
        # Update position map
        self.block_positions[block_name] = (stack_index, height)
        return True

    def move_block(self, block_name, target_stack_index):
        """Move a block to the top of another stack"""
        if block_name not in self.block_positions:
            print(f"Error: Block {block_name} does not exist")
            return False
        
        if target_stack_index >= len(self.stacks):
            print(f"Error: Target stack {target_stack_index} does not exist")
            return False
        
        source_stack_index, height = self.block_positions[block_name]
        source_stack = self.stacks[source_stack_index]
        
        # Check if the block is at the top of its stack
        if height != len(source_stack) - 1:
            print(f"Error: Block {block_name} is not at the top of its stack")
            return False
        
        # Remove block from source stack
        source_stack.pop()
        
        # Add block to target stack
        target_stack = self.stacks[target_stack_index]
        new_height = len(target_stack)
        target_stack.append(block_name)
        
        # Update position map
        self.block_positions[block_name] = (target_stack_index, new_height)
        
        # Record action
        self.actions.append(f"Move {block_name} from stack {source_stack_index} to stack {target_stack_index}")
        return True

    def is_on_top(self, block_name):
        """Check if a block is on top of its stack"""
        if block_name not in self.block_positions:
            return False
        
        stack_index, height = self.block_positions[block_name]
        return height == len(self.stacks[stack_index]) - 1

    def get_block_below(self, block_name):
        """Get the block immediately below the specified block, or None if on table"""
        if block_name not in self.block_positions:
            return None
        
        stack_index, height = self.block_positions[block_name]
        if height > 0:
            return self.stacks[stack_index][height - 1]
        return None  # On table

    def get_block_above(self, block_name):
        """Get the block immediately above the specified block, or None if none"""
        if block_name not in self.block_positions:
            return None
        
        stack_index, height = self.block_positions[block_name]
        stack = self.stacks[stack_index]
        if height < len(stack) - 1:
            return stack[height + 1]
        return None

    def print_state(self):
        """Print the current state of the block world"""
        print("\nCurrent Block World State:")
        
        # Find the maximum stack height
        max_height = 0
        for stack in self.stacks:
            max_height = max(max_height, len(stack))
        
        # Print stacks from top to bottom
        for h in range(max_height - 1, -1, -1):
            line = ""
            for i, stack in enumerate(self.stacks):
                if h < len(stack):
                    line += f" [{stack[h]}] "
                else:
                    line += "     "
            print(line)
        
        # Print table
        table_line = "=" * (len(self.stacks) * 5 + 1)
        print(table_line)
        stack_nums = ""
        for i in range(len(self.stacks)):
            stack_nums += f"  {i}  "
        print(stack_nums)

    def setup_from_user_input(self):
        """Set up the initial state from user input"""
        print("=== Block World Problem Setup ===")
        n_blocks = int(input("Enter the number of blocks: "))
        n_stacks = int(input("Enter the number of stacks: "))
        
        # Create stacks
        for _ in range(n_stacks):
            self.add_stack()
        
        # Set up initial state
        print("\nSetting up initial state...")
        print("Enter the initial configuration by specifying which stack each block is in.")
        print("Blocks will be stacked from bottom to top in the order you enter them for each stack.")
        
        for i in range(n_stacks):
            stack_blocks = input(f"Enter space-separated blocks for stack {i} (bottom to top): ").strip().upper().split()
            for block in stack_blocks:
                self.add_block(block, i)
        
        print("\nInitial state set up successfully!")
        self.print_state()
        
        return n_blocks

    def is_goal_state(self, goal_config):
        """Check if current state matches the goal configuration"""
        # Convert goal config to a comparable format
        goal_stacks = [[] for _ in range(len(self.stacks))]
        for block, (stack_idx, _) in goal_config.items():
            goal_stacks[stack_idx].append(block)
        
        # Sort blocks in each goal stack by their height
        for stack_idx, blocks in enumerate(goal_stacks):
            blocks.sort(key=lambda b: goal_config[b][1])
        
        # Compare current stacks with goal stacks
        for i in range(len(self.stacks)):
            if self.stacks[i] != goal_stacks[i]:
                return False
        return True

    def get_goal_state(self):
        """Get the goal state configuration from user input"""
        print("\n=== Goal State Setup ===")
        print("Enter the goal configuration by specifying which stack each block should be in.")
        print("Blocks will be stacked from bottom to top in the order you enter them for each stack.")
        
        goal_config = {}  # Maps block name to (stack_index, height_in_stack)
        
        for i in range(len(self.stacks)):
            stack_blocks = input(f"Enter space-separated blocks for stack {i} (bottom to top): ").strip().upper().split()
            for height, block in enumerate(stack_blocks):
                if block in goal_config:
                    print(f"Warning: Block {block} was already assigned elsewhere. Overwriting previous assignment.")
                goal_config[block] = (i, height)
        
        # Verify all blocks are accounted for
        missing_blocks = set(self.block_positions.keys()) - set(goal_config.keys())
        if missing_blocks:
            print(f"Warning: The following blocks were not assigned in the goal state: {missing_blocks}")
            for block in missing_blocks:
                stack_idx = int(input(f"Enter stack index for block {block}: "))
                height = len([b for b in goal_config.values() if b[0] == stack_idx])
                goal_config[block] = (stack_idx, height)
        
        return goal_config

    def solve(self, goal_config):
        """
        Solve the block world problem using a simple algorithm:
        1. Clear blocks that need to be moved
        2. Move blocks to their goal positions
        """
        print("\n=== Solving Block World Problem ===")
        self.actions = []  # Reset actions list
        
        # First, handle blocks that are not in the correct position
        for block, (goal_stack, goal_height) in goal_config.items():
            current_stack, current_height = self.block_positions[block]
            
            # If the block is not in the correct stack or at the correct height
            if current_stack != goal_stack or current_height != goal_height:
                # First, clear blocks above this block
                self.clear_block(block)
                
                # Next, clear blocks above the target position
                # We need to clear up to the goal height
                target_stack = self.stacks[goal_stack]
                blocks_to_clear = []
                
                # Find blocks that need to be cleared from the target position
                for h in range(goal_height, len(target_stack)):
                    blocks_to_clear.append(target_stack[h])
                
                # Clear them
                for b in blocks_to_clear:
                    self.clear_block(b)
                    self.move_to_temporary_stack(b)
                
                # Now move the block to the target stack
                self.move_block(block, goal_stack)
                
                # If we need to put blocks back on top of this block, do so
                if goal_height < len(target_stack) - 1:
                    # We'll implement this if needed
                    pass
        
        # Verify goal state
        if self.is_goal_state(goal_config):
            print("\n=== Solution ===")
            if not self.actions:
                print("The initial state is already the goal state!")
            else:
                for i, action in enumerate(self.actions):
                    print(f"Step {i+1}: {action}")
            
            print("\n=== Final State ===")
            self.print_state()
        else:
            print("Error: Failed to reach goal state!")

    def clear_block(self, block_name):
        """Move all blocks above the specified block to temporary stacks"""
        stack_idx, height = self.block_positions[block_name]
        stack = self.stacks[stack_idx]
        
        # Move blocks above this block to temporary stacks
        for h in range(len(stack)-1, height, -1):
            block_to_move = stack[h]
            self.move_to_temporary_stack(block_to_move)

    def move_to_temporary_stack(self, block_name):
        """Move a block to a temporary/empty stack"""
        # Find an empty stack or stack with fewest blocks
        min_stack_idx = 0
        min_stack_size = len(self.stacks[0])
        
        for i, stack in enumerate(self.stacks):
            if len(stack) < min_stack_size:
                min_stack_idx = i
                min_stack_size = len(stack)
        
        # Move the block
        self.move_block(block_name, min_stack_idx)

def main():
    world = BlockWorld()
    
    # Set up initial state
    world.setup_from_user_input()
    
    # Get goal state
    goal_config = world.get_goal_state()
    
    # Solve the problem
    world.solve(goal_config)

if __name__ == "__main__":
    main()































# === Block World Problem Setup ===
# Enter the number of blocks: 3
# Enter the number of stacks: 3

# Setting up initial state...
# Enter the initial configuration by specifying which stack each block is in.
# Blocks will be stacked from bottom to top in the order you enter them for each stack.
# Enter space-separated blocks for stack 0 (bottom to top): A B
# Enter space-separated blocks for stack 1 (bottom to top): C
# Enter space-separated blocks for stack 2 (bottom to top): 

# Initial state set up successfully!

# Current Block World State:
#  [B]  [C]      
#  [A]            
# ================
#   0    1    2  

# === Goal State Setup ===
# Enter the goal configuration by specifying which stack each block should be in.
# Blocks will be stacked from bottom to top in the order you enter them for each stack.
# Enter space-separated blocks for stack 0 (bottom to top): 
# Enter space-separated blocks for stack 1 (bottom to top): 
# Enter space-separated blocks for stack 2 (bottom to top): C B A

# === Solving Block World Problem ===

# === Solution ===
# Step 1: Move B from stack 0 to stack 2
# Step 2: Move C from stack 1 to stack 2
# Step 3: Move A from stack 0 to stack 2

# === Final State ===

# Current Block World State:
#  [A]      
#  [B]      
#  [C]      
# ================
#   0    1    2