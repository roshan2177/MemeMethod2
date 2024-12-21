import re

class CodeOptimizer:
    def __init__(self, code):
        self.code = code

    def constant_folding(self):
        """Simplify constant expressions."""
        optimized_code = []
        for line in self.code:
            # Look for simple patterns: number operator number
            match = re.search(r'\b(\d+)\s*([+\-*/])\s*(\d+)\b', line)
            if match:
                a, operator, b = match.groups()
                # Evaluate and replace
                try:
                    result = eval(f"{a}{operator}{b}")
                    line = line.replace(match.group(0), str(result))
                except Exception:
                    pass  # In case eval fails, just skip
            optimized_code.append(line)
        self.code = optimized_code

    def dead_code_elimination(self):
        """Remove unused assignments.
           This is a simplistic approach:
           1. Identify lines that have an assignment.
           2. Check if the assigned variable is used in any other line.
        """
        live_code = []
        all_lines = self.code
        for i, line in enumerate(all_lines):
            if "=" in line:
                var_name = line.split("=")[0].strip()
                # Check for usage in other lines
                if any(var_name in other and i != idx for idx, other in enumerate(all_lines)):
                    live_code.append(line)
            else:
                live_code.append(line)
        self.code = live_code

    def strength_reduction(self):
        """Replace * 2 with << 1 and / 2 with >> 1 for optimization."""
        optimized_code = []
        for line in self.code:
            line = line.replace("* 2", "<< 1")
            line = line.replace("/ 2", ">> 1")
            optimized_code.append(line)
        self.code = optimized_code

    def loop_unrolling(self):
        """Stub function for loop unrolling."""
        # As no loops are handled here, just return the current code.
        self.code = self.code

    def optimize(self):
        self.constant_folding()
        self.dead_code_elimination()
        self.strength_reduction()
        self.loop_unrolling()
        return self.code
