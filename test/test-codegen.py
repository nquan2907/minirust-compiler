import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from utils.AST import *
from TestUtils import CodeGenerator

def test_001():
    """Test 1: Minimal main printing an integer primitive"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_i32", [IntLiteral(42)]))
            ])
        )
    ])
    expected = "42\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test 2: Printing float and boolean primitives"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_f32", [FloatLiteral(3.14)])),
                ExprStmt(CallExpr("println_bool", [BoolLiteral(True)]))
            ])
        )
    ])
    expected = "3.14\ntrue\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_003():
    """Test 3: Variable declaration and reading variable"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(100)),
                ExprStmt(CallExpr("println_i32", [Id("x")]))
            ])
        )
    ])
    expected = "100\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test 4: Basic arithmetic operations precedence (+ and *)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl(
                    "a",
                    IntType(),
                    BinaryOp("+", IntLiteral(10), BinaryOp("*", IntLiteral(20), IntLiteral(3)))
                ),
                ExprStmt(CallExpr("println_i32", [Id("a")]))
            ])
        )
    ])
    expected = "70\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test 5: Implicit type coercion (int to float in binary op)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl(
                    "res",
                    FloatType(),
                    BinaryOp("+", IntLiteral(5), FloatLiteral(2.5))
                ),
                ExprStmt(CallExpr("println_f32", [Id("res")]))
            ])
        )
    ])
    expected = "7.5\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test 6: Variable reassignment statement"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(1)),
                ExprStmt(Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(10)))),
                ExprStmt(CallExpr("println_i32", [Id("x")]))
            ])
        )
    ])
    expected = "11\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test 7: Simple void function call without arguments"""
    ast = Program([
        FuncDecl(
            "greet",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("Hello MiniRust")]))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("greet", []))
            ])
        )
    ])
    expected = "Hello MiniRust\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_008():
    """Test 8: Function call with parameters and integer return"""
    ast = Program([
        FuncDecl(
            "add",
            [VarDecl("a", IntType()), VarDecl("b", IntType())],
            IntType(),
            Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_i32", [CallExpr("add", [IntLiteral(5), IntLiteral(7)])]))
            ])
        )
    ])
    expected = "12\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_009():
    """Test 9: Implicit int-to-float coercion when passing arguments to a function"""
    ast = Program([
        FuncDecl(
            "print_half",
            [VarDecl("val", FloatType())],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_f32", [BinaryOp("/", Id("val"), FloatLiteral(2.0))]))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("print_half", [IntLiteral(10)]))
            ])
        )
    ])
    expected = "5.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_010():
    """Test 10: Nested function calls combined with unary negation operation"""
    ast = Program([
        FuncDecl(
            "square",
            [VarDecl("x", IntType())],
            IntType(),
            Block([
                Return(BinaryOp("*", Id("x"), Id("x")))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(
                    CallExpr(
                        "println_i32",
                        [CallExpr("square", [UnaryOp("-", IntLiteral(4))])]
                    )
                )
            ])
        )
    ])
    expected = "16\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Basic Switch Branching & Default Clauses (test_011 - test_015)
# ==============================================================================

def test_011():
    """Test 11: Basic switch matching first case with break"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(1)),
                Switch(
                    Id("x"),
                    [
                        Case(IntLiteral(1), [ExprStmt(CallExpr("println_string", [StringLiteral("one")])), Break()]),
                        Case(IntLiteral(2), [ExprStmt(CallExpr("println_string", [StringLiteral("two")])), Break()]),
                        Case(None, [ExprStmt(CallExpr("println_string", [StringLiteral("default")])), Break()])
                    ]
                )
            ])
        )
    ])
    expected = "one\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_012():
    """Test 12: Switch matching middle case"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(2)),
                Switch(
                    Id("x"),
                    [
                        Case(IntLiteral(1), [ExprStmt(CallExpr("println_i32", [IntLiteral(10)])), Break()]),
                        Case(IntLiteral(2), [ExprStmt(CallExpr("println_i32", [IntLiteral(20)])), Break()]),
                        Case(IntLiteral(3), [ExprStmt(CallExpr("println_i32", [IntLiteral(30)])), Break()])
                    ]
                )
            ])
        )
    ])
    expected = "20\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_013():
    """Test 13: Switch with no match falling through to explicit default clause"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(99)),
                Switch(
                    Id("x"),
                    [
                        Case(IntLiteral(1), [ExprStmt(CallExpr("println_i32", [IntLiteral(1)])), Break()]),
                        Case(IntLiteral(2), [ExprStmt(CallExpr("println_i32", [IntLiteral(2)])), Break()]),
                        Case(None, [ExprStmt(CallExpr("println_string", [StringLiteral("unknown")])), Break()])
                    ]
                )
            ])
        )
    ])
    expected = "unknown\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_014():
    """Test 14: Switch without default clause and no matching cases (should do nothing)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                Switch(
                    Id("x"),
                    [
                        Case(IntLiteral(1), [ExprStmt(CallExpr("println_i32", [IntLiteral(10)])), Break()]),
                        Case(IntLiteral(2), [ExprStmt(CallExpr("println_i32", [IntLiteral(20)])), Break()])
                    ]
                ),
                ExprStmt(CallExpr("println_string", [StringLiteral("done")]))
            ])
        )
    ])
    expected = "done\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_015():
    """Test 15: Switch expression evaluation with complex arithmetic expression"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(2)),
                VarDecl("b", IntType(), IntLiteral(3)),
                Switch(
                    BinaryOp("*", Id("a"), Id("b")),  # 2 * 3 = 6
                    [
                        Case(IntLiteral(5), [ExprStmt(CallExpr("println_string", [StringLiteral("five")])), Break()]),
                        Case(IntLiteral(6), [ExprStmt(CallExpr("println_string", [StringLiteral("six")])), Break()]),
                        Case(None, [ExprStmt(CallExpr("println_string", [StringLiteral("other")])), Break()])
                    ]
                )
            ])
        )
    ])
    expected = "six\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Basic While & Range-based For Loops (test_016 - test_020)
# ==============================================================================

def test_016():
    """Test 16: Basic while loop counting from 1 to 3"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(1)),
                While(
                    BinaryOp("<=", Id("i"), IntLiteral(3)),
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("i")])),
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "1\n2\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_017():
    """Test 17: Basic range-based for loop (start..end with end exclusive)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(0),
                    IntLiteral(4),  # Runs for i = 0, 1, 2, 3
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "0\n1\n2\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_018():
    """Test 18: While loop with condition initially false (0 iterations)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                While(
                    BoolLiteral(False),
                    Block([
                        ExprStmt(CallExpr("println_string", [StringLiteral("unreachable")]))
                    ])
                ),
                ExprStmt(CallExpr("println_string", [StringLiteral("done")]))
            ])
        )
    ])
    expected = "done\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_019():
    """Test 19: For loop with empty range where start >= end (0 iterations)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(5),
                    IntLiteral(5),  # 5..5 is empty range
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                ),
                ExprStmt(CallExpr("println_string", [StringLiteral("empty")]))
            ])
        )
    ])
    expected = "empty\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_020():
    """Test 20: Accumulating values inside a for loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("sum", IntType(), IntLiteral(0)),
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(6),  # Sum of 1..5 = 15
                    Block([
                        ExprStmt(Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i"))))
                    ])
                ),
                ExprStmt(CallExpr("println_i32", [Id("sum")]))
            ])
        )
    ])
    expected = "15\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


# ==============================================================================
# Break, Continue, and Boundary Evaluation (test_021 - test_025)
# ==============================================================================

def test_021():
    """Test 21: Early exit using break in a while loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(1)),
                While(
                    BinaryOp("<=", Id("i"), IntLiteral(10)),
                    Block([
                        If(
                            BinaryOp("==", Id("i"), IntLiteral(3)),
                            Break(),
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")])),
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "1\n2\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_022():
    """Test 22: Skipping iterations using continue in a while loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                While(
                    BinaryOp("<", Id("i"), IntLiteral(4)),
                    Block([
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))),
                        If(
                            BinaryOp("==", Id("i"), IntLiteral(2)),
                            Continue(),
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n3\n4\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_023():
    """Test 23: Continue inside a For loop (must jump to the increment phase)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(5),  # i = 1, 2, 3, 4
                    Block([
                        If(
                            BinaryOp("==", Id("i"), IntLiteral(3)),
                            Continue(),  # Skips printing 3, but continues with 4
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n2\n4\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_024():
    """Test 24: Single evaluation of end-bound expression in For loop"""
    # Verify that the end bound expression is evaluated ONCE before the loop starts
    ast = Program([
        FuncDecl(
            "get_limit",
            [],
            IntType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("eval_limit")])),
                Return(IntLiteral(3))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(0),
                    CallExpr("get_limit", []),  # Should only print "eval_limit" once
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "eval_limit\n0\n1\n2\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_025():
    """Test 25: For loop with negative ranges or start larger than end"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    UnaryOp("-", IntLiteral(2)),  # -2
                    IntLiteral(2),                # 2 -> -2, -1, 0, 1
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "-2\n-1\n0\n1\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Basic Break & Continue in Single Loops (test_026 - test_034)
# ==============================================================================

def test_026():
    """Test 26: Break immediately on first iteration of while loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                While(
                    BoolLiteral(True),
                    Block([
                        ExprStmt(CallExpr("println_string", [StringLiteral("start")])),
                        Break(),
                        ExprStmt(CallExpr("println_string", [StringLiteral("unreachable")]))
                    ])
                ),
                ExprStmt(CallExpr("println_string", [StringLiteral("end")]))
            ])
        )
    ])
    expected = "start\nend\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_027():
    """Test 27: Continue skips rest of while loop body and re-evaluates condition"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                While(
                    BinaryOp("<", Id("i"), IntLiteral(3)),
                    Block([
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))),
                        ExprStmt(CallExpr("println_i32", [Id("i")])),
                        Continue(),
                        ExprStmt(CallExpr("println_string", [StringLiteral("never_printed")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n2\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_028():
    """Test 28: Break in range for-loop halts iteration immediately"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(10),  # Loop 1..9
                    Block([
                        If(
                            BinaryOp("==", Id("i"), IntLiteral(4)),
                            Break(),
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n2\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_029():
    """Test 29: Continue in range for-loop must still execute iinc step before next check"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(6),  # i = 1, 2, 3, 4, 5
                    Block([
                        If(
                            BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)),
                            Continue(),  # Skip even numbers
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n3\n5\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_030():
    """Test 30: Multiple breaks under different branches inside a while loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                While(
                    BoolLiteral(True),
                    Block([
                        If(
                            BinaryOp("<", Id("x"), IntLiteral(0)),
                            Break(),
                            If(
                                BinaryOp("==", Id("x"), IntLiteral(2)),
                                Break(),
                                None
                            )
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("x")])),
                        ExprStmt(Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "5\n4\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_031():
    """Test 31: Break inside nested if-else statements within a loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(5),
                    Block([
                        If(
                            BinaryOp(">", Id("i"), IntLiteral(2)),
                            Block([
                                ExprStmt(CallExpr("println_string", [StringLiteral("greater")])),
                                Break()
                            ]),
                            Block([
                                ExprStmt(CallExpr("println_i32", [Id("i")]))
                            ])
                        )
                    ])
                )
            ])
        )
    ])
    expected = "1\n2\ngreater\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_032():
    """Test 32: Continue inside a nested block in a while loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("n", IntType(), IntLiteral(0)),
                While(
                    BinaryOp("<", Id("n"), IntLiteral(3)),
                    Block([
                        ExprStmt(Assign(Id("n"), BinaryOp("+", Id("n"), IntLiteral(1)))),
                        Block([
                            If(
                                BinaryOp("==", Id("n"), IntLiteral(2)),
                                Continue(),
                                None
                            )
                        ]),
                        ExprStmt(CallExpr("println_i32", [Id("n")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_033():
    """Test 33: Break inside loop with variable mutations maintaining correct state"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("acc", IntType(), IntLiteral(0)),
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(10),
                    Block([
                        ExprStmt(Assign(Id("acc"), BinaryOp("+", Id("acc"), Id("i")))),
                        If(
                            BinaryOp(">=", Id("acc"), IntLiteral(10)),
                            Break(),
                            None
                        )
                    ])
                ),
                ExprStmt(CallExpr("println_i32", [Id("acc")]))
            ])
        )
    ])
    expected = "10\n"  # 1 + 2 + 3 + 4 = 10
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_034():
    """Test 34: Sequential loops with independent breaks"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(5),
                    Block([
                        If(BinaryOp("==", Id("i"), IntLiteral(2)), Break(), None),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                ),
                For(
                    "j",
                    IntLiteral(10),
                    IntLiteral(15),
                    Block([
                        If(BinaryOp("==", Id("j"), IntLiteral(12)), Break(), None),
                        ExprStmt(CallExpr("println_i32", [Id("j")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n10\n11\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Complex Loop Control Flow & Scope Shadowing (test_035 - test_040)
# ==============================================================================

def test_035():
    """Test 35: Nested while loops"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(1)),
                While(
                    BinaryOp("<=", Id("i"), IntLiteral(2)),
                    Block([
                        VarDecl("j", IntType(), IntLiteral(10)),
                        While(
                            BinaryOp("<=", Id("j"), IntLiteral(20)),
                            Block([
                                ExprStmt(CallExpr("println_i32", [BinaryOp("+", Id("i"), Id("j"))])),
                                ExprStmt(Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(10))))
                            ])
                        ),
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "11\n21\n12\n22\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_036():
    """Test 36: Break in inner loop does not break outer loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(3),  # i = 1, 2
                    Block([
                        For(
                            "j",
                            IntLiteral(10),
                            IntLiteral(25), # j = 10, 11, 12...
                            Block([
                                If(
                                    BinaryOp("==", Id("j"), IntLiteral(12)),
                                    Break(),  # Nhảy ra khỏi vòng lặp j khi j == 12
                                    None
                                ),
                                ExprStmt(CallExpr("println_i32", [Id("j")]))
                            ])
                        )
                    ])
                )
            ])
        )
    ])
    # i = 1: j chạy 10, 11 (dừng ở 12)
    # i = 2: j chạy 10, 11 (dừng ở 12)
    expected = "10\n11\n10\n11\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_037():
    """Test 37: Loop variable scope isolation in range for loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(99)),
                For(
                    "i",
                    IntLiteral(0),
                    IntLiteral(2),  # i = 0, 1 inside loop
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                ),
                # Outer 'i' should remain 99 after loop finishes
                ExprStmt(CallExpr("println_i32", [Id("i")]))
            ])
        )
    ])
    expected = "0\n1\n99\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_038():
    """Test 38: Continue in inner loop jumps to inner loop's increment only"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(3),  # i = 1, 2
                    Block([
                        For(
                            "j",
                            IntLiteral(1),
                            IntLiteral(4),  # j = 1, 2, 3
                            Block([
                                If(
                                    BinaryOp("==", Id("j"), IntLiteral(2)),
                                    Continue(),
                                    None
                                ),
                                ExprStmt(CallExpr("println_i32", [BinaryOp("+", BinaryOp("*", Id("i"), IntLiteral(10)), Id("j"))]))
                            ])
                        )
                    ])
                )
            ])
        )
    ])
    expected = "11\n13\n21\n23\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_039():
    """Test 39: Loop with condition containing function call side-effects"""
    ast = Program([
        FuncDecl(
            "check_count",
            [VarDecl("c", IntType())],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("check")])),
                Return(BinaryOp("<", Id("c"), IntLiteral(2)))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("count", IntType(), IntLiteral(0)),
                While(
                    CallExpr("check_count", [Id("count")]),
                    Block([
                        ExprStmt(Assign(Id("count"), BinaryOp("+", Id("count"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "check\ncheck\ncheck\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_040():
    """Test 40: While loop with multiple break conditions"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(0)),
                While(
                    BoolLiteral(True),  # Infinite loop breakable by conditions
                    Block([
                        ExprStmt(Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))),
                        If(
                            BinaryOp("==", Id("x"), IntLiteral(3)),
                            Break(),
                            None
                        )
                    ])
                ),
                ExprStmt(CallExpr("println_i32", [Id("x")]))
            ])
        )
    ])
    expected = "3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Fallthrough Behavior & Nested Switch Control Flow (test_041 - test_045)
# ==============================================================================

def test_041():
    """Test 41: Fallthrough behavior (case without break continues execution into next case)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(1)),
                Switch(
                    Id("x"),
                    [
                        # No break here! Fallthrough to case 2 and default
                        Case(IntLiteral(1), [ExprStmt(CallExpr("println_i32", [IntLiteral(100)]))]),
                        Case(IntLiteral(2), [ExprStmt(CallExpr("println_i32", [IntLiteral(200)]))]),
                        Case(None, [ExprStmt(CallExpr("println_i32", [IntLiteral(300)]))])
                    ]
                )
            ])
        )
    ])
    expected = "100\n200\n300\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_042():
    """Test 42: Partial fallthrough (executes matched case and falls through until a break)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(2)),
                Switch(
                    Id("x"),
                    [
                        Case(IntLiteral(1), [ExprStmt(CallExpr("println_string", [StringLiteral("A")])), Break()]),
                        Case(IntLiteral(2), [ExprStmt(CallExpr("println_string", [StringLiteral("B")]))]), # Fallthrough
                        Case(IntLiteral(3), [ExprStmt(CallExpr("println_string", [StringLiteral("C")])), Break()]),
                        Case(None, [ExprStmt(CallExpr("println_string", [StringLiteral("D")])), Break()])
                    ]
                )
            ])
        )
    ])
    expected = "B\nC\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_043():
    """Test 43: Switch inside a For loop (ensuring break targets the switch, not the loop)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(4),  # Loop i = 1, 2, 3
                    Block([
                        Switch(
                            Id("i"),
                            [
                                Case(IntLiteral(1), [ExprStmt(CallExpr("println_string", [StringLiteral("one")])), Break()]),
                                Case(IntLiteral(2), [ExprStmt(CallExpr("println_string", [StringLiteral("two")])), Break()]),
                                Case(None, [ExprStmt(CallExpr("println_string", [StringLiteral("other")])), Break()])
                            ]
                        )
                    ])
                )
            ])
        )
    ])
    expected = "one\ntwo\nother\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_044():
    """Test 44: Nested switches (inner break must not break outer switch incorrectly)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("outer", IntType(), IntLiteral(1)),
                VarDecl("inner", IntType(), IntLiteral(10)),
                Switch(
                    Id("outer"),
                    [
                        Case(IntLiteral(1), [
                            Switch(
                                Id("inner"),
                                [
                                    Case(IntLiteral(10), [
                                        ExprStmt(CallExpr("println_string", [StringLiteral("inner_10")])),
                                        Break()
                                    ])
                                ]
                            ),
                            # This statement executes after the inner switch breaks
                            ExprStmt(CallExpr("println_string", [StringLiteral("outer_1")])),
                            Break()
                        ]),
                        Case(None, [
                            ExprStmt(CallExpr("println_string", [StringLiteral("default")])),
                            Break()
                        ])
                    ]
                )
            ])
        )
    ])
    expected = "inner_10\nouter_1\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_045():
    """Test 45: Switch with variable mutation inside cases"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("state", IntType(), IntLiteral(1)),
                VarDecl("acc", IntType(), IntLiteral(0)),
                Switch(
                    Id("state"),
                    [
                        Case(IntLiteral(1), [
                            ExprStmt(Assign(Id("acc"), BinaryOp("+", Id("acc"), IntLiteral(10)))),
                            Break()
                        ]),
                        Case(IntLiteral(2), [
                            ExprStmt(Assign(Id("acc"), BinaryOp("+", Id("acc"), IntLiteral(20)))),
                            Break()
                        ])
                    ]
                ),
                ExprStmt(CallExpr("println_i32", [Id("acc")]))
            ])
        )
    ])
    expected = "10\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Struct Instantiation & Basic Field Access (test_046 - test_052)
# ==============================================================================

def test_046():
    """Test 46: Basic struct declaration, instantiation and field reading"""
    ast = Program([
        StructDecl("Point", [VarDecl("x", IntType()), VarDecl("y", IntType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("p", StructType("Point"), StructInit("Point", [
                    FieldInit("x", IntLiteral(10)),
                    FieldInit("y", IntLiteral(20))
                ])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("p"), "x")])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("p"), "y")]))
            ])
        )
    ])
    expected = "10\n20\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_047():
    """Test 47: Mutating struct fields (Write field access)"""
    ast = Program([
        StructDecl("Counter", [VarDecl("val", IntType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("c", StructType("Counter"), StructInit("Counter", [
                    FieldInit("val", IntLiteral(0))
                ])),
                ExprStmt(Assign(FieldAccess(Id("c"), "val"), IntLiteral(42))),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("c"), "val")]))
            ])
        )
    ])
    expected = "42\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_048():
    """Test 48: Struct field name collision with Jasmin reserved keyword (e.g. 'inner', 'field')"""
    ast = Program([
        StructDecl("Wrapper", [VarDecl("inner", IntType()), VarDecl("field", FloatType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("w", StructType("Wrapper"), StructInit("Wrapper", [
                    FieldInit("inner", IntLiteral(100)),
                    FieldInit("field", FloatLiteral(2.5))
                ])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("w"), "inner")])),
                ExprStmt(CallExpr("println_f32", [FieldAccess(Id("w"), "field")]))
            ])
        )
    ])
    expected = "100\n2.5\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_049():
    """Test 49: Passing struct as parameter to function"""
    ast = Program([
        StructDecl("Person", [VarDecl("age", IntType())]),
        FuncDecl(
            "print_age",
            [VarDecl("p", StructType("Person"))],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("p"), "age")]))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("person", StructType("Person"), StructInit("Person", [
                    FieldInit("age", IntLiteral(25))
                ])),
                ExprStmt(CallExpr("print_age", [Id("person")]))
            ])
        )
    ])
    expected = "25\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_050():
    """Test 50: Function returning a struct instance"""
    ast = Program([
        StructDecl("Vec2", [VarDecl("x", FloatType()), VarDecl("y", FloatType())]),
        FuncDecl(
            "create_vec",
            [VarDecl("x", FloatType()), VarDecl("y", FloatType())],
            StructType("Vec2"),
            Block([
                Return(StructInit("Vec2", [
                    FieldInit("x", Id("x")),
                    FieldInit("y", Id("y"))
                ]))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("v", StructType("Vec2"), CallExpr("create_vec", [FloatLiteral(1.0), FloatLiteral(2.0)])),
                ExprStmt(CallExpr("println_f32", [FieldAccess(Id("v"), "x")])),
                ExprStmt(CallExpr("println_f32", [FieldAccess(Id("v"), "y")]))
            ])
        )
    ])
    expected = "1.0\n2.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_051():
    """Test 51: Struct field implicit type coercion (Int to Float on field init & field assignment)"""
    ast = Program([
        StructDecl("Data", [VarDecl("ratio", FloatType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                # IntLiteral(5) coerced to float on init
                VarDecl("d", StructType("Data"), StructInit("Data", [
                    FieldInit("ratio", IntLiteral(5))
                ])),
                ExprStmt(CallExpr("println_f32", [FieldAccess(Id("d"), "ratio")])),
                # IntLiteral(10) coerced to float on field assign
                ExprStmt(Assign(FieldAccess(Id("d"), "ratio"), IntLiteral(10))),
                ExprStmt(CallExpr("println_f32", [FieldAccess(Id("d"), "ratio")]))
            ])
        )
    ])
    expected = "5.0\n10.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_052():
    """Test 52: Nested struct field access (Struct within Struct)"""
    ast = Program([
        StructDecl("Point", [VarDecl("x", IntType()), VarDecl("y", IntType())]),
        StructDecl("Rectangle", [VarDecl("top_left", StructType("Point")), VarDecl("width", IntType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("rect", StructType("Rectangle"), StructInit("Rectangle", [
                    FieldInit("top_left", StructInit("Point", [
                        FieldInit("x", IntLiteral(5)),
                        FieldInit("y", IntLiteral(10))
                    ])),
                    FieldInit("width", IntLiteral(50))
                ])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(FieldAccess(Id("rect"), "top_left"), "x")])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(FieldAccess(Id("rect"), "top_left"), "y")])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("rect"), "width")]))
            ])
        )
    ])
    expected = "5\n10\n50\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_053():
    """Test 53: Short-circuit AND (false && expr -> right side side-effects MUST NOT execute)"""
    ast = Program([
        FuncDecl(
            "side_effect",
            [],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("SHOULD_NOT_PRINT")])),
                Return(BoolLiteral(True))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl(
                    "res",
                    BoolType(),
                    BinaryOp("&&", BoolLiteral(False), CallExpr("side_effect", []))
                ),
                ExprStmt(CallExpr("println_bool", [Id("res")]))
            ])
        )
    ])
    # Vế trái là False -> không gọi side_effect() -> kết quả là false
    expected = "false\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_054():
    """Test 54: Short-circuit OR (true || expr -> right side side-effects MUST NOT execute)"""
    ast = Program([
        FuncDecl(
            "side_effect",
            [],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("SHOULD_NOT_PRINT")])),
                Return(BoolLiteral(False))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl(
                    "res",
                    BoolType(),
                    BinaryOp("||", BoolLiteral(True), CallExpr("side_effect", []))
                ),
                ExprStmt(CallExpr("println_bool", [Id("res")]))
            ])
        )
    ])
    # Vế trái là True -> không gọi side_effect() -> kết quả là true
    expected = "true\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_055():
    """Test 55: Evaluates right side when short-circuit condition is NOT met"""
    ast = Program([
        FuncDecl(
            "check_right_and",
            [],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("eval_right_and")])),
                Return(BoolLiteral(True))
            ])
        ),
        FuncDecl(
            "check_right_or",
            [],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("eval_right_or")])),
                Return(BoolLiteral(True))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                # true && check_right_and() -> phai danh gia ve phai
                VarDecl("r1", BoolType(), BinaryOp("&&", BoolLiteral(True), CallExpr("check_right_and", []))),
                # false || check_right_or() -> phai danh gia ve phai
                VarDecl("r2", BoolType(), BinaryOp("||", BoolLiteral(False), CallExpr("check_right_or", [])))
            ])
        )
    ])
    expected = "eval_right_and\neval_right_or\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_056():
    """Test 56: Chained logical operations short-circuiting (A && B && C)"""
    ast = Program([
        FuncDecl(
            "fn1",
            [],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("fn1")])),
                Return(BoolLiteral(False))  # Intercepts chain here!
            ])
        ),
        FuncDecl(
            "fn2",
            [],
            BoolType(),
            Block([
                ExprStmt(CallExpr("println_string", [StringLiteral("fn2_unreachable")])),
                Return(BoolLiteral(True))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                # fn1() tra ve False -> ngung ngay tai fn1(), fn2() khong duoc goi
                VarDecl(
                    "res",
                    BoolType(),
                    BinaryOp("&&", CallExpr("fn1", []), CallExpr("fn2", []))
                ),
                ExprStmt(CallExpr("println_bool", [Id("res")]))
            ])
        )
    ])
    expected = "fn1\nfalse\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_057():
    """Test 57: Short-circuit prevents potential runtime errors (e.g., variable state check)"""
    ast = Program([
        FuncDecl(
            "mutate_val",
            [],
            BoolType(),
            Block([
                # Neu ham nay duoc goi, no se in "mutated"
                ExprStmt(CallExpr("println_string", [StringLiteral("mutated")])),
                Return(BoolLiteral(True))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(0)),
                # (x != 0) && mutate_val() -> vi x == 0 nen (x != 0) is False -> mutate_val() khong chay
                If(
                    BinaryOp("&&", BinaryOp("!=", Id("x"), IntLiteral(0)), CallExpr("mutate_val", [])),
                    ExprStmt(CallExpr("println_string", [StringLiteral("then_branch")])),
                    ExprStmt(CallExpr("println_string", [StringLiteral("else_branch")]))
                )
            ])
        )
    ])
    expected = "else_branch\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Advanced & Nested Loop Control Scenarios (test_058 - test_067)
# ==============================================================================

def test_058():
    """Test 58: Break in inner while loop jumps only out of inner loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(1)),
                While(
                    BinaryOp("<=", Id("i"), IntLiteral(2)),
                    Block([
                        VarDecl("j", IntType(), IntLiteral(10)),
                        While(
                            BoolLiteral(True),
                            Block([
                                ExprStmt(CallExpr("println_i32", [Id("j")])),
                                Break()
                            ])
                        ),
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "10\n10\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_059():
    """Test 59: Continue in inner while loop targets inner loop continue label"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(1)),
                While(
                    BinaryOp("<=", Id("i"), IntLiteral(2)),
                    Block([
                        VarDecl("j", IntType(), IntLiteral(0)),
                        While(
                            BinaryOp("<", Id("j"), IntLiteral(3)),
                            Block([
                                ExprStmt(Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))),
                                If(
                                    BinaryOp("==", Id("j"), IntLiteral(2)),
                                    Continue(),
                                    None
                                ),
                                ExprStmt(CallExpr("println_i32", [BinaryOp("+", BinaryOp("*", Id("i"), IntLiteral(10)), Id("j"))]))
                            ])
                        ),
                        ExprStmt(Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))))
                    ])
                )
            ])
        )
    ])
    expected = "11\n13\n21\n23\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_060():
    """Test 60: Nested for loops with break in outer loop based on inner loop result"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("found", BoolType(), BoolLiteral(False)),
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(4),  # i = 1, 2, 3
                    Block([
                        For(
                            "j",
                            IntLiteral(1),
                            IntLiteral(4),  # j = 1, 2, 3
                            Block([
                                If(
                                    BinaryOp("==", BinaryOp("*", Id("i"), Id("j")), IntLiteral(4)),
                                    Block([
                                        ExprStmt(Assign(Id("found"), BoolLiteral(True))),
                                        Break()
                                    ]),
                                    None
                                )
                            ])
                        ),
                        If(
                            Id("found"),
                            Block([
                                ExprStmt(CallExpr("println_i32", [Id("i")])),
                                Break()
                            ]),
                            None
                        )
                    ])
                )
            ])
        )
    ])
    expected = "2\n"  # i=2, j=2 gives 4 -> breaks inner then breaks outer
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_061():
    """Test 61: Continue in outer loop from within inner loop block (outside inner loop)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(4),  # i = 1, 2, 3
                    Block([
                        For(
                            "j",
                            IntLiteral(10),
                            IntLiteral(12),  # j = 10, 11
                            Block([
                                ExprStmt(CallExpr("println_i32", [Id("j")]))
                            ])
                        ),
                        If(
                            BinaryOp("==", Id("i"), IntLiteral(2)),
                            Continue(),  # Jumps outer loop to next iteration
                            None
                        ),
                        ExprStmt(CallExpr("println_string", [StringLiteral("outer_end")]))
                    ])
                )
            ])
        )
    ])
    expected = "10\n11\nouter_end\n10\n11\n10\n11\nouter_end\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_062():
    """Test 62: Deeply nested loops (3-levels) with break in innermost loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "a",
                    IntLiteral(1),
                    IntLiteral(2),
                    Block([
                        For(
                            "b",
                            IntLiteral(1),
                            IntLiteral(2),
                            Block([
                                For(
                                    "c",
                                    IntLiteral(10),
                                    IntLiteral(20),
                                    Block([
                                        ExprStmt(CallExpr("println_i32", [Id("c")])),
                                        Break()  # Always breaks c after 1st iteration
                                    ])
                                )
                            ])
                        )
                    ])
                )
            ])
        )
    ])
    expected = "10\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_063():
    """Test 63: Break inside a loop enclosed by a switch statement"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("mode", IntType(), IntLiteral(1)),
                Switch(
                    Id("mode"),
                    [
                        Case(IntLiteral(1), [
                            While(
                                BoolLiteral(True),
                                Block([
                                    ExprStmt(CallExpr("println_string", [StringLiteral("loop_in_switch")])),
                                    Break()  # Breaks WHILE loop, NOT switch!
                                ])
                            ),
                            ExprStmt(CallExpr("println_string", [StringLiteral("after_loop")])),
                            Break()  # Breaks SWITCH
                        ])
                    ]
                )
            ])
        )
    ])
    expected = "loop_in_switch\nafter_loop\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_064():
    """Test 64: Break inside a switch enclosed by a loop"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(3),  # i = 1, 2
                    Block([
                        Switch(
                            Id("i"),
                            [
                                Case(IntLiteral(1), [
                                    ExprStmt(CallExpr("println_string", [StringLiteral("case_1")])),
                                    Break()  # Breaks SWITCH, loop continues!
                                ])
                            ]
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "case_1\n1\n2\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_065():
    """Test 65: Continue inside a loop enclosed by a switch statement"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(4),  # i = 1, 2, 3
                    Block([
                        Switch(
                            Id("i"),
                            [
                                Case(IntLiteral(2), [
                                    Continue(),  # Continue MUST target the enclosing FOR loop
                                    Break()
                                ])
                            ]
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                )
            ])
        )
    ])
    expected = "1\n3\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_066():
    """Test 66: Loop break combined with early function return"""
    ast = Program([
        FuncDecl(
            "test_func",
            [],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(5),
                    Block([
                        If(
                            BinaryOp("==", Id("i"), IntLiteral(3)),
                            Return(None),  # Directly returns from function, bypassing loop break
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                ),
                ExprStmt(CallExpr("println_string", [StringLiteral("never_reached")]))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("test_func", []))
            ])
        )
    ])
    expected = "1\n2\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_067():
    """Test 67: While loop condition checking mutating local variables with break"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                While(
                    BinaryOp(">", Id("x"), IntLiteral(0)),
                    Block([
                        ExprStmt(Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(2)))),
                        If(
                            BinaryOp("==", Id("x"), IntLiteral(6)),
                            Continue(),
                            None
                        ),
                        If(
                            BinaryOp("<=", Id("x"), IntLiteral(2)),
                            Break(),
                            None
                        ),
                        ExprStmt(CallExpr("println_i32", [Id("x")]))
                    ])
                )
            ])
        )
    ])
    expected = "8\n4\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_068():
    """Test 68: Right-associative chained assignment (a = b = c = 10)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(0)),
                VarDecl("b", IntType(), IntLiteral(0)),
                VarDecl("c", IntType(), IntLiteral(0)),
                # a = (b = (c = 10))
                ExprStmt(Assign(Id("a"), Assign(Id("b"), Assign(Id("c"), IntLiteral(10))))),
                ExprStmt(CallExpr("println_i32", [Id("a")])),
                ExprStmt(CallExpr("println_i32", [Id("b")])),
                ExprStmt(CallExpr("println_i32", [Id("c")]))
            ])
        )
    ])
    expected = "10\n10\n10\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_069():
    """Test 69: Assignment expression evaluated inside an 'if' condition"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(0)),
                # if ((x = 5) > 0) -> x gets assigned 5, then 5 > 0 is True
                If(
                    BinaryOp(">", Assign(Id("x"), IntLiteral(5)), IntLiteral(0)),
                    ExprStmt(CallExpr("println_i32", [Id("x")])),
                    ExprStmt(CallExpr("println_string", [StringLiteral("false_branch")]))
                )
            ])
        )
    ])
    expected = "5\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_070():
    """Test 70: Assignment expression evaluated inside a 'while' loop condition"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("n", IntType(), IntLiteral(10)),
                # while ((n = n - 3) > 0) -> decrement and check condition in one expr
                While(
                    BinaryOp(">", Assign(Id("n"), BinaryOp("-", Id("n"), IntLiteral(3))), IntLiteral(0)),
                    Block([
                        ExprStmt(CallExpr("println_i32", [Id("n")]))
                    ])
                )
            ])
        )
    ])
    expected = "7\n4\n1\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_071():
    """Test 71: Chained member assignment with ArrayCell and FieldAccess"""
    ast = Program([
        StructDecl("Point", [VarDecl("x", IntType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("p", StructType("Point"), StructInit("Point", [FieldInit("x", IntLiteral(0))])),
                VarDecl("arr", ArrayType(IntType(), 2), ArrayLiteral([IntLiteral(0), IntLiteral(0)])),
                # p.x = arr[0] = 42
                ExprStmt(Assign(FieldAccess(Id("p"), "x"), Assign(ArrayCell(Id("arr"), IntLiteral(0)), IntLiteral(42)))),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("p"), "x")])),
                ExprStmt(CallExpr("println_i32", [ArrayCell(Id("arr"), IntLiteral(0))]))
            ])
        )
    ])
    expected = "42\n42\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_072():
    """Test 72: Assignment expression passed directly as function argument"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("val", IntType(), IntLiteral(0)),
                # println_i32(val = 100) -> prints 100 and updates val to 100
                ExprStmt(CallExpr("println_i32", [Assign(Id("val"), IntLiteral(100))])),
                ExprStmt(CallExpr("println_i32", [Id("val")]))
            ])
        )
    ])
    expected = "100\n100\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_073():
    """Test 73: Chained assignment with float implicit coercion (f = i = 5)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("f", FloatType(), FloatLiteral(0.0)),
                VarDecl("i", IntType(), IntLiteral(0)),
                # f = (i = 5) -> i gets 5 (int), then f gets 5.0 (float via i2f)
                ExprStmt(Assign(Id("f"), Assign(Id("i"), IntLiteral(5)))),
                ExprStmt(CallExpr("println_i32", [Id("i")])),
                ExprStmt(CallExpr("println_f32", [Id("f")]))
            ])
        )
    ])
    expected = "5\n5.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_074():
    """Test 74: Array cell mutation in assignment expression inside complex expression"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("arr", ArrayType(IntType(), 3), ArrayLiteral([IntLiteral(10), IntLiteral(20), IntLiteral(30)])),
                # sum = (arr[1] = 50) + arr[0] -> arr[1] becomes 50, sum becomes 50 + 10 = 60
                VarDecl("sum", IntType(), BinaryOp("+", Assign(ArrayCell(Id("arr"), IntLiteral(1)), IntLiteral(50)), ArrayCell(Id("arr"), IntLiteral(0)))),
                ExprStmt(CallExpr("println_i32", [ArrayCell(Id("arr"), IntLiteral(1))])),
                ExprStmt(CallExpr("println_i32", [Id("sum")]))
            ])
        )
    ])
    expected = "50\n60\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_075():
    """Test 75: Deeply chained assignments mixing local variables, array cells, and struct fields"""
    ast = Program([
        StructDecl("Box", [VarDecl("val", IntType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("b", StructType("Box"), StructInit("Box", [FieldInit("val", IntLiteral(0))])),
                VarDecl("arr", ArrayType(IntType(), 1), ArrayLiteral([IntLiteral(0)])),
                VarDecl("x", IntType(), IntLiteral(0)),
                # x = arr[0] = b.val = 999
                ExprStmt(Assign(Id("x"), Assign(ArrayCell(Id("arr"), IntLiteral(0)), Assign(FieldAccess(Id("b"), "val"), IntLiteral(999))))),
                ExprStmt(CallExpr("println_i32", [Id("x")])),
                ExprStmt(CallExpr("println_i32", [ArrayCell(Id("arr"), IntLiteral(0))])),
                ExprStmt(CallExpr("println_i32", [FieldAccess(Id("b"), "val")]))
            ])
        )
    ])
    expected = "999\n999\n999\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_076():
    """Test 76: Relational comparison operators on integers (<, <=, >, >=, ==, !=)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(5)),
                VarDecl("b", IntType(), IntLiteral(10)),
                ExprStmt(CallExpr("println_bool", [BinaryOp("<", Id("a"), Id("b"))])),   # 5 < 10 -> true
                ExprStmt(CallExpr("println_bool", [BinaryOp("<=", Id("a"), Id("a"))])),  # 5 <= 5 -> true
                ExprStmt(CallExpr("println_bool", [BinaryOp(">", Id("a"), Id("b"))])),   # 5 > 10 -> false
                ExprStmt(CallExpr("println_bool", [BinaryOp(">=", Id("b"), Id("a"))])),  # 10 >= 5 -> true
                ExprStmt(CallExpr("println_bool", [BinaryOp("==", Id("a"), Id("b"))])),  # 5 == 10 -> false
                ExprStmt(CallExpr("println_bool", [BinaryOp("!=", Id("a"), Id("b"))]))   # 5 != 10 -> true
            ])
        )
    ])
    expected = "true\ntrue\nfalse\ntrue\nfalse\ntrue\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_077():
    """Test 77: Floating point relational comparisons and coercion (int vs float comparison)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(5)),
                VarDecl("f", FloatType(), FloatLiteral(5.5)),
                # 5 < 5.5 -> (i2f(5) < 5.5) -> true
                ExprStmt(CallExpr("println_bool", [BinaryOp("<", Id("i"), Id("f"))])),
                # 5.5 == 5 -> false
                ExprStmt(CallExpr("println_bool", [BinaryOp("==", Id("f"), Id("i"))])),
                # 5.5 >= 5 -> true
                ExprStmt(CallExpr("println_bool", [BinaryOp(">=", Id("f"), Id("i"))]))
            ])
        )
    ])
    expected = "true\nfalse\ntrue\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_078():
    """Test 78: String equality (== and !=) via String.equals virtual method invocation"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("s1", StringType(), StringLiteral("hello")),
                VarDecl("s2", StringType(), StringLiteral("hello")),
                VarDecl("s3", StringType(), StringLiteral("world")),
                ExprStmt(CallExpr("println_bool", [BinaryOp("==", Id("s1"), Id("s2"))])), # true
                ExprStmt(CallExpr("println_bool", [BinaryOp("!=", Id("s1"), Id("s3"))])), # true
                ExprStmt(CallExpr("println_bool", [BinaryOp("==", Id("s1"), Id("s3"))]))  # false
            ])
        )
    ])
    expected = "true\ntrue\nfalse\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_079():
    """Test 79: Relational operations with logical NOT and boolean flags"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(15)),
                # !((x >= 10) && (x <= 20)) -> !(true && true) -> false
                VarDecl("out_of_bounds", BoolType(), UnaryOp("!", BinaryOp("&&", BinaryOp(">=", Id("x"), IntLiteral(10)), BinaryOp("<=", Id("x"), IntLiteral(20))))),
                ExprStmt(CallExpr("println_bool", [Id("out_of_bounds")]))
            ])
        )
    ])
    expected = "false\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_080():
    """Test 80: Complex nested conditional branching (if-else chain with relational operators)"""
    ast = Program([
        FuncDecl(
            "classify_score",
            [VarDecl("score", IntType())],
            VoidType(),
            Block([
                If(
                    BinaryOp(">=", Id("score"), IntLiteral(90)),
                    ExprStmt(CallExpr("println_string", [StringLiteral("A")])),
                    If(
                        BinaryOp(">=", Id("score"), IntLiteral(80)),
                        ExprStmt(CallExpr("println_string", [StringLiteral("B")])),
                        If(
                            BinaryOp(">=", Id("score"), IntLiteral(70)),
                            ExprStmt(CallExpr("println_string", [StringLiteral("C")])),
                            ExprStmt(CallExpr("println_string", [StringLiteral("F")]))
                        )
                    )
                )
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("classify_score", [IntLiteral(85)])),
                ExprStmt(CallExpr("classify_score", [IntLiteral(95)])),
                ExprStmt(CallExpr("classify_score", [IntLiteral(60)]))
            ])
        )
    ])
    expected = "B\nA\nF\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_081():
    """Test 81: Unary minus on integer and float literals/variables"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), UnaryOp("-", IntLiteral(42))),
                VarDecl("f", FloatType(), UnaryOp("-", FloatLiteral(3.14))),
                ExprStmt(CallExpr("println_i32", [Id("i")])),
                ExprStmt(CallExpr("println_f32", [Id("f")]))
            ])
        )
    ])
    expected = "-42\n-3.14\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_082():
    """Test 82: Double unary negation (canceling out negations)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                VarDecl("b", BoolType(), BoolLiteral(True)),
                # -(-10) -> 10
                ExprStmt(CallExpr("println_i32", [UnaryOp("-", UnaryOp("-", Id("x")))])),
                # !(!true) -> true
                ExprStmt(CallExpr("println_bool", [UnaryOp("!", UnaryOp("!", Id("b")))]))
            ])
        )
    ])
    expected = "10\ntrue\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_083():
    """Test 83: Logical NOT (!) on complex boolean expressions"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(5)),
                VarDecl("b", IntType(), IntLiteral(10)),
                # !(5 > 10) -> !False -> True
                VarDecl("cond1", BoolType(), UnaryOp("!", BinaryOp(">", Id("a"), Id("b")))),
                # !(5 == 5) -> !True -> False
                VarDecl("cond2", BoolType(), UnaryOp("!", BinaryOp("==", Id("a"), IntLiteral(5)))),
                ExprStmt(CallExpr("println_bool", [Id("cond1")])),
                ExprStmt(CallExpr("println_bool", [Id("cond2")]))
            ])
        )
    ])
    expected = "true\nfalse\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_084():
    """Test 84: Unary minus combined with arithmetic operators in expressions"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(10)),
                VarDecl("b", IntType(), IntLiteral(20)),
                # -a + (-b * 2) -> -10 + (-20 * 2) = -10 + (-40) = -50
                VarDecl("res", IntType(), BinaryOp("+", UnaryOp("-", Id("a")), BinaryOp("*", UnaryOp("-", Id("b")), IntLiteral(2)))),
                ExprStmt(CallExpr("println_i32", [Id("res")]))
            ])
        )
    ])
    expected = "-50\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_085():
    """Test 85: Logical NOT on boolean function return values and short-circuit conditions"""
    ast = Program([
        FuncDecl(
            "is_even",
            [VarDecl("n", IntType())],
            BoolType(),
            Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("num", IntType(), IntLiteral(7)),
                # if (!is_even(7)) -> !false -> true
                If(
                    UnaryOp("!", CallExpr("is_even", [Id("num")])),
                    ExprStmt(CallExpr("println_string", [StringLiteral("odd")])),
                    ExprStmt(CallExpr("println_string", [StringLiteral("even")]))
                )
            ])
        )
    ])
    expected = "odd\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_086():
    """Test 86: Floating-point arithmetic (+, -, *, /) with pure float literals and variables"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", FloatType(), FloatLiteral(10.5)),
                VarDecl("b", FloatType(), FloatLiteral(2.5)),
                ExprStmt(CallExpr("println_f32", [BinaryOp("+", Id("a"), Id("b"))])),  # 13.0
                ExprStmt(CallExpr("println_f32", [BinaryOp("-", Id("a"), Id("b"))])),  # 8.0
                ExprStmt(CallExpr("println_f32", [BinaryOp("*", Id("a"), Id("b"))])),  # 26.25
                ExprStmt(CallExpr("println_f32", [BinaryOp("/", Id("a"), Id("b"))]))   # 4.2
            ])
        )
    ])
    expected = "13.0\n8.0\n26.25\n4.2\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_087():
    """Test 87: Implicit coercion (i2f) in binary operations mixing Int and Float"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(10)),
                VarDecl("f", FloatType(), FloatLiteral(2.5)),
                # Int + Float -> i2f(i) + f = 12.5
                ExprStmt(CallExpr("println_f32", [BinaryOp("+", Id("i"), Id("f"))])),
                # Float * Int -> f * i2f(i) = 25.0
                ExprStmt(CallExpr("println_f32", [BinaryOp("*", Id("f"), Id("i"))])),
                # Int / Float -> i2f(i) / f = 4.0
                ExprStmt(CallExpr("println_f32", [BinaryOp("/", Id("i"), Id("f"))]))
            ])
        )
    ])
    expected = "12.5\n25.0\n4.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_088():
    """Test 88: Implicit coercion on variable declaration and reassignment (Int to Float)"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                # VarDecl with IntLiteral -> converted to FloatType
                VarDecl("x", FloatType(), IntLiteral(100)),
                ExprStmt(CallExpr("println_f32", [Id("x")])),
                # Assign IntLiteral to Float variable -> i2f generated
                ExprStmt(Assign(Id("x"), IntLiteral(42))),
                ExprStmt(CallExpr("println_f32", [Id("x")]))
            ])
        )
    ])
    expected = "100.0\n42.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_089():
    """Test 89: Implicit coercion on function return value (Int expression returned as Float)"""
    ast = Program([
        FuncDecl(
            "get_float_val",
            [],
            FloatType(),  # Function returns FloatType
            Block([
                VarDecl("a", IntType(), IntLiteral(7)),
                VarDecl("b", IntType(), IntLiteral(3)),
                # Returns Int expression (7 + 3) -> i2f inserted before return
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_f32", [CallExpr("get_float_val", [])]))
            ])
        )
    ])
    expected = "10.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_090():
    """Test 90: Mixed precision expressions in complex nested arithmetic"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(2)),
                VarDecl("b", FloatType(), FloatLiteral(1.5)),
                VarDecl("c", IntType(), IntLiteral(3)),
                # (a * b) + c -> (2.0 * 1.5) + 3.0 = 3.0 + 3.0 = 6.0
                VarDecl("res", FloatType(), BinaryOp("+", BinaryOp("*", Id("a"), Id("b")), Id("c"))),
                ExprStmt(CallExpr("println_f32", [Id("res")]))
            ])
        )
    ])
    expected = "6.0\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_091():
    """Test 91: Recursive Factorial calculation"""
    ast = Program([
        FuncDecl(
            "fact",
            [VarDecl("n", IntType())],
            IntType(),
            Block([
                If(
                    BinaryOp("<=", Id("n"), IntLiteral(1)),
                    Return(IntLiteral(1)),
                    Return(BinaryOp("*", Id("n"), CallExpr("fact", [BinaryOp("-", Id("n"), IntLiteral(1))])))
                )
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_i32", [CallExpr("fact", [IntLiteral(5)])])) # 5! = 120
            ])
        )
    ])
    expected = "120\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_092():
    """Test 92: Recursive Fibonacci calculation"""
    ast = Program([
        FuncDecl(
            "fib",
            [VarDecl("n", IntType())],
            IntType(),
            Block([
                If(
                    BinaryOp("<=", Id("n"), IntLiteral(1)),
                    Return(Id("n")),
                    Return(BinaryOp(
                        "+",
                        CallExpr("fib", [BinaryOp("-", Id("n"), IntLiteral(1))]),
                        CallExpr("fib", [BinaryOp("-", Id("n"), IntLiteral(2))])
                    ))
                )
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_i32", [CallExpr("fib", [IntLiteral(7)])])) # fib(7) = 13
            ])
        )
    ])
    expected = "13\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_093():
    """Test 93: Mutual recursion (is_even and is_odd calling each other)"""
    ast = Program([
        FuncDecl(
            "is_even",
            [VarDecl("n", IntType())],
            BoolType(),
            Block([
                If(
                    BinaryOp("==", Id("n"), IntLiteral(0)),
                    Return(BoolLiteral(True)),
                    Return(CallExpr("is_odd", [BinaryOp("-", Id("n"), IntLiteral(1))]))
                )
            ])
        ),
        FuncDecl(
            "is_odd",
            [VarDecl("n", IntType())],
            BoolType(),
            Block([
                If(
                    BinaryOp("==", Id("n"), IntLiteral(0)),
                    Return(BoolLiteral(False)),
                    Return(CallExpr("is_even", [BinaryOp("-", Id("n"), IntLiteral(1))]))
                )
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_bool", [CallExpr("is_even", [IntLiteral(4)])])), # true
                ExprStmt(CallExpr("println_bool", [CallExpr("is_odd", [IntLiteral(4)])]))    # false
            ])
        )
    ])
    expected = "true\nfalse\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_094():
    """Test 94: Nested block variable shadowing"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                Block([
                    VarDecl("x", IntType(), IntLiteral(20)), # Inner x shadows outer x
                    ExprStmt(CallExpr("println_i32", [Id("x")]))
                ]),
                ExprStmt(CallExpr("println_i32", [Id("x")])) # Outer x restored
            ])
        )
    ])
    expected = "20\n10\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_095():
    """Test 95: Variable shadowing inside If-Else branches"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("val", StringType(), StringLiteral("outer")),
                If(
                    BoolLiteral(True),
                    Block([
                        VarDecl("val", StringType(), StringLiteral("then_branch")),
                        ExprStmt(CallExpr("println_string", [Id("val")]))
                    ]),
                    Block([
                        VarDecl("val", StringType(), StringLiteral("else_branch")),
                        ExprStmt(CallExpr("println_string", [Id("val")]))
                    ])
                ),
                ExprStmt(CallExpr("println_string", [Id("val")]))
            ])
        )
    ])
    expected = "then_branch\nouter\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_096():
    """Test 96: Variable shadowing inside loop scopes"""
    ast = Program([
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("i", IntType(), IntLiteral(100)),
                For(
                    "i",
                    IntLiteral(1),
                    IntLiteral(3), # Loop i = 1, 2
                    Block([
                        VarDecl("i", IntType(), IntLiteral(999)), # Local i shadows loop counter i inside block
                        ExprStmt(CallExpr("println_i32", [Id("i")]))
                    ])
                ),
                ExprStmt(CallExpr("println_i32", [Id("i")])) # Outer i is 100
            ])
        )
    ])
    expected = "999\n999\n100\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_097():
    """Test 97: Deep recursion with local scope allocations"""
    ast = Program([
        FuncDecl(
            "sum_up_to",
            [VarDecl("n", IntType())],
            IntType(),
            Block([
                If(
                    BinaryOp("<=", Id("n"), IntLiteral(0)),
                    Return(IntLiteral(0)),
                    Block([
                        VarDecl("temp", IntType(), CallExpr("sum_up_to", [BinaryOp("-", Id("n"), IntLiteral(1))])),
                        Return(BinaryOp("+", Id("n"), Id("temp")))
                    ])
                )
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("println_i32", [CallExpr("sum_up_to", [IntLiteral(10)])])) # 1+..+10 = 55
            ])
        )
    ])
    expected = "55\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_098():
    """Test 98: Classic FizzBuzz algorithm (1 to 15)"""
    ast = Program([
        FuncDecl(
            "fizzbuzz",
            [VarDecl("n", IntType())],
            VoidType(),
            Block([
                For(
                    "i",
                    IntLiteral(1),
                    BinaryOp("+", Id("n"), IntLiteral(1)), # 1..15
                    Block([
                        VarDecl("div3", BoolType(), BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(3)), IntLiteral(0))),
                        VarDecl("div5", BoolType(), BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(5)), IntLiteral(0))),
                        If(
                            BinaryOp("&&", Id("div3"), Id("div5")),
                            ExprStmt(CallExpr("println_string", [StringLiteral("FizzBuzz")])),
                            If(
                                Id("div3"),
                                ExprStmt(CallExpr("println_string", [StringLiteral("Fizz")])),
                                If(
                                    Id("div5"),
                                    ExprStmt(CallExpr("println_string", [StringLiteral("Buzz")])),
                                    ExprStmt(CallExpr("println_i32", [Id("i")]))
                                )
                            )
                        )
                    ])
                )
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                ExprStmt(CallExpr("fizzbuzz", [IntLiteral(15)]))
            ])
        )
    ])
    expected = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

# ==============================================================================
# Comprehensive Struct Lifecycle Edge Cases (test_099)
# ==============================================================================

def test_099():
    """Test 99: Array of structs with field mutations inside a loop"""
    ast = Program([
        StructDecl("Item", [VarDecl("id", IntType()), VarDecl("score", IntType())]),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                # Array of Structs
                VarDecl("items", ArrayType(StructType("Item"), 2), ArrayLiteral([
                    StructInit("Item", [FieldInit("id", IntLiteral(1)), FieldInit("score", IntLiteral(100))]),
                    StructInit("Item", [FieldInit("id", IntLiteral(2)), FieldInit("score", IntLiteral(200))])
                ])),
                # Access and print first element field
                ExprStmt(CallExpr("println_i32", [FieldAccess(ArrayCell(Id("items"), IntLiteral(0)), "score")])),
                # Mutate field of second element in array
                ExprStmt(Assign(FieldAccess(ArrayCell(Id("items"), IntLiteral(1)), "score"), IntLiteral(999))),
                ExprStmt(CallExpr("println_i32", [FieldAccess(ArrayCell(Id("items"), IntLiteral(1)), "score")]))
            ])
        )
    ])
    expected = "100\n999\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_100():
    """Test 100: Greatest Common Divisor (GCD) using Euclidean Algorithm with shadowing"""
    ast = Program([
        FuncDecl(
            "gcd",
            [VarDecl("a", IntType()), VarDecl("b", IntType())],
            IntType(),
            Block([
                While(
                    BinaryOp("!=", Id("b"), IntLiteral(0)),
                    Block([
                        VarDecl("temp", IntType(), Id("b")), # Shadowing / Local var
                        ExprStmt(Assign(Id("b"), BinaryOp("%", Id("a"), Id("b")))),
                        ExprStmt(Assign(Id("a"), Id("temp")))
                    ])
                ),
                Return(Id("a"))
            ])
        ),
        FuncDecl(
            "main",
            [],
            VoidType(),
            Block([
                VarDecl("a", IntType(), IntLiteral(48)),
                VarDecl("b", IntType(), IntLiteral(18)),
                ExprStmt(CallExpr("println_i32", [CallExpr("gcd", [Id("a"), Id("b")])])) # GCD(48, 18) = 6
            ])
        )
    ])
    expected = "6\n"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"