import unittest
from code_optimizer import CodeOptimizer

class TestCodeOptimizer(unittest.TestCase):
    def test_constant_folding(self):
        input_code = [
            "x = 2 + 3",
            "y = 10 * 5",
            "print(x, y)"
        ]
        optimizer = CodeOptimizer(input_code)
        optimizer.constant_folding()
        self.assertEqual(optimizer.code, [
            "x = 5",
            "y = 50",
            "print(x, y)"
        ])

    def test_dead_code_elimination(self):
        input_code = [
            "a = 10",
            "b = 20",
            "print(a)",
            # 'b' is never used after assignment
        ]
        optimizer = CodeOptimizer(input_code)
        optimizer.dead_code_elimination()
        self.assertEqual(optimizer.code, [
            "a = 10",
            "print(a)",
        ])

    def test_strength_reduction(self):
        input_code = [
            "x = x * 2",
            "y = y / 2",
            "z = 10 * 2 + 4"
        ]
        optimizer = CodeOptimizer(input_code)
        optimizer.strength_reduction()
        self.assertEqual(optimizer.code, [
            "x = x << 1",
            "y = y >> 1",
            "z = 10 << 1 + 4"
        ])

    def test_optimize(self):
        input_code = [
            "a = 2 + 2",
            "b = 4 * 2",
            "c = 10",
            "print(a, b)",
            # 'c' is never used
        ]
        optimizer = CodeOptimizer(input_code)
        optimized = optimizer.optimize()
        self.assertEqual(optimized, [
            "a = 4",
            "b = 8",
            "print(a, b)",
        ])

if __name__ == '__main__':
    unittest.main()
