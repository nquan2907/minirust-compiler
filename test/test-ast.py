import sys
import os
import inspect
from antlr4 import *

# Add source directory to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from TestUtils import TestAST

def check_ast(input_str, expected_str):
    func_name = inspect.stack()[1].function
    test_num = func_name.split('_')[1]
    TestAST.checkAST(input_str, expected_str)

def test_300():
    # Sample test: Minimum program
    check_ast(
        "fn main() { print_i32(1); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(print_i32), [IntLiteral(1)]))]))])"
    )

# TODO: Add more test cases (from test_301 to test_399) to complete the 100 test suite
# after extending the grammar (MiniRust.g4) and the ASTGenerator.py.

def test_301():
    # test_1: Khai báo hàm không có kiểu trả về (VoidType) và không tham số
    check_ast(
        "fn init() {}",
        "Program([FuncDecl(Id(init), [], VoidType, Block([]))])"
    )

def test_302():
    # test_2: Khai báo hàm có kiểu trả về tường minh (i32) và trả về một định danh
    check_ast(
        "fn identity(x: i32) -> i32 { return x; }",
        "Program([FuncDecl(Id(identity), [VarDecl(Id(x), IntType, None, False)], IntType, Block([Return(Id(x))]))])"
    )

def test_303():
    # test_3: Khai báo hàm có nhiều tham số với các kiểu dữ liệu khác nhau
    check_ast(
        "fn process(id: i32, rate: f32, active: bool) -> void {}",
        "Program([FuncDecl(Id(process), [VarDecl(Id(id), IntType, None, False), VarDecl(Id(rate), FloatType, None, False), VarDecl(Id(active), BoolType, None, False)], VoidType, Block([]))])"
    )

def test_304():
    # test_4: Định nghĩa Struct cơ bản chứa các trường dữ liệu nguyên thủy
    check_ast(
        "struct Point { x: i32, y: i32 }",
        "Program([StructDecl(Id(Point), [VarDecl(Id(x), IntType, None, False), VarDecl(Id(y), IntType, None, False)])])"
    )

def test_305():
    # test_5: Định nghĩa Struct phức tạp chứa kiểu mảng và kiểu struct khác
    check_ast(
        "struct Mesh { vertices: Point, Matrix: [f32; 16] }",
        "Program([StructDecl(Id(Mesh), [VarDecl(Id(vertices), StructType(Id(Point)), None, False), VarDecl(Id(Matrix), ArrayType(FloatType, 16), None, False)])])"
    )

def test_306():
    # test_6: Khai báo biến bất biến (immutable let) có kèm kiểu dữ liệu
    check_ast(
        "fn main() { let x: i32 = 42; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(x), IntType, IntLiteral(42), False)]))])"
    )

def test_307():
    # test_7: Khai báo biến có thể thay đổi (mutable let mut) có kèm kiểu dữ liệu
    check_ast(
        "fn main() { let mut scale: f32 = 1.5; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(scale), FloatType, FloatLiteral(1.5), True)]))])"
    )

def test_308():
    # test_8: Suy luận kiểu dữ liệu cục bộ (Local type inference - không ghi rõ kiểu)
    check_ast(
        "fn main() { let msg = \"hello\"; let mut count = 0; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(msg), None, StringLiteral(\"hello\"), False), VarDecl(Id(count), None, IntLiteral(0), True)]))])"
    )

def test_309():
    # test_9: Khai báo biến mutable không khởi tạo giá trị (Mutable uninitialized variable)
    check_ast(
        "fn main() { let mut buffer: [i32; 100]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(buffer), ArrayType(IntType, 100), None, True)]))])"
    )

# ==========================================
# CONTROL FLOW STRUCTURES (test_310 - test_322)
# ==========================================

def test_310():
    # test_10: Return trả về trực tiếp, toán tử '>' dùng nháy đơn
    check_ast(
        "fn main() { if x > 0 { return 1; } else { return 0; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([If(BinaryOp('>', Id(x), IntLiteral(0)), Block([Return(IntLiteral(1))]), Block([Return(IntLiteral(0))]))]))])"
    )

def test_311():
    # test_11: Return ở các nhánh lồng nhau đều trả về trực tiếp, toán tử '==' dùng nháy đơn
    check_ast(
        "fn main() { if x == 1 { return 10; } else if x == 2 { return 20; } else { return 30; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([If(BinaryOp('==', Id(x), IntLiteral(1)), Block([Return(IntLiteral(10))]), If(BinaryOp('==', Id(x), IntLiteral(2)), Block([Return(IntLiteral(20))]), Block([Return(IntLiteral(30))])))]))])"
    )

def test_312():
    # test_12: Thêm dấu nháy đơn cho toán tử '<' và '+'
    check_ast(
        "fn main() { while i < 10 { i = i + 1; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([While(BinaryOp('<', Id(i), IntLiteral(10)), Block([ExprStmt(Assign(Id(i), BinaryOp('+', Id(i), IntLiteral(1))))]))]))])"
    )

def test_313():
    # test_13: Vòng lặp For-in (For khoảng giá trị từ start đến end)
    check_ast(
        "fn main() { for i in 0..10 { print(i); } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([For(Id(i), IntLiteral(0), IntLiteral(10), Block([ExprStmt(CallExpr(Id(print), [Id(i)]))]))]))])"
    )

def test_314():
    # test_14: Control action - Break trong vòng lặp while
    check_ast(
        "fn main() { while true { break; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([While(BoolLiteral(True), Block([Break()]))]))])"
    )

def test_315():
    # test_15: Control action - Continue trong vòng lặp for
    check_ast(
        "fn main() { for i in 1..5 { continue; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([For(Id(i), IntLiteral(1), IntLiteral(5), Block([Continue()]))]))])"
    )

def test_316():
    # test_16: Lệnh return không kèm biểu thức (Void Return)
    check_ast(
        "fn main() { return; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Return(None)]))])"
    )

def test_317():
    # test_17: Các khối lệnh lồng nhau (Nested lexical blocks `{ }`)
    check_ast(
        "fn main() { { let x = 1; { let y = 2; } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Block([VarDecl(Id(x), None, IntLiteral(1), False), Block([VarDecl(Id(y), None, IntLiteral(2), False)])])]))])"
    )

def test_318():
    # test_18: Fix ExprStmt bọc quanh Assign bên trong vòng lặp lồng
    check_ast(
        "fn main() { for i in 0..5 { while j < 2 { j = j + 1; } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([For(Id(i), IntLiteral(0), IntLiteral(5), Block([While(BinaryOp('<', Id(j), IntLiteral(2)), Block([ExprStmt(Assign(Id(j), BinaryOp('+', Id(j), IntLiteral(1))))]))]))]))])"
    )

def test_319():
    # test_19: If lồng bên trong khối Block con
    check_ast(
        "fn main() { { if active { return; } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Block([If(Id(active), Block([Return(None)]), None)])]))])"
    )

def test_320():
    # test_20: Vòng lặp For chứa If-Else (Break/Continue là statement gốc, không bị bọc ExprStmt)
    # Tuy nhiên, cần kiểm tra kỹ i % 2 == 0 có được parse đúng độ ưu tiên toán tử không
    check_ast(
        "fn main() { for i in 1..100 { if i % 2 == 0 { continue; } else { break; } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([For(Id(i), IntLiteral(1), IntLiteral(100), Block([If(BinaryOp('==', BinaryOp('%', Id(i), IntLiteral(2)), IntLiteral(0)), Block([Continue()]), Block([Break()]))]))]))])"
    )

def test_321():
    # test_21: Tổ hợp While vô hạn chứa các khối lệnh rỗng lồng nhau
    check_ast(
        "fn main() { while true { { { } } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([While(BoolLiteral(True), Block([Block([Block([])])]))]))])"
    )

def test_322():
    # test_22: If-Else lồng cực sâu (Deeply nested conditional branching)
    check_ast(
        "fn main() { if a { if b { if c { return 1; } } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([If(Id(a), Block([If(Id(b), Block([If(Id(c), Block([Return(IntLiteral(1))]), None)]), None)]), None)]))])"
    )


# ==========================================
# SWITCH STATEMENT (C-style) (test_323 - test_327)
# ==========================================

def test_323():
    # test_23: Return nằm trong Case của Switch trả về trực tiếp, toán tử '&&' dùng nháy đơn
    check_ast(
        "fn main() { switch (x && y) { case 1: return 10; default: return 0; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Switch(BinaryOp('&&', Id(x), Id(y)), [Case(IntLiteral(1), [Return(IntLiteral(10))]), Case(None, [Return(IntLiteral(0))])])]))])"
    )

def test_324():
    # test_24: Case fall-through chuỗi (Logic grammar của bạn gom cụm statement list, case trống sẽ trả về list rỗng)
    check_ast(
        "fn main() { switch x { case 1: case 2: return 20; default: return 0; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Switch(Id(x), [Case(IntLiteral(1), []), Case(IntLiteral(2), [Return(IntLiteral(20))]), Case(None, [Return(IntLiteral(0))])])]))])"
    )

def test_325():
    # test_25: Default clause chứa các khối lệnh lồng nhau (Nested block in default)
    check_ast(
        "fn main() { switch x { case 1: return 5; default: { let a = 1; } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Switch(Id(x), [Case(IntLiteral(1), [Return(IntLiteral(5))]), Case(None, [Block([VarDecl(Id(a), None, IntLiteral(1), False)])])])]))])"
    )

def test_326():
    # test_26: Switch với case đa kiểu dữ liệu (bool) và return trong từng case
    check_ast(
        "fn main() { switch status { case true: return 1; case false: return 0; default: return -1; } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Switch(Id(status), "
        "[Case(BoolLiteral(True), [Return(IntLiteral(1))]), "
        "Case(BoolLiteral(False), [Return(IntLiteral(0))]), "
        "Case(None, [Return(UnaryOp('-', IntLiteral(1)))])])]))])"
    )

def test_327():
    # test_27: C-style Switch lồng nhau phức tạp bên trong một vòng lặp
    check_ast(
        "fn main() { while true { switch x { case 1: break; default: continue; } } }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([While(BoolLiteral(True), Block([Switch(Id(x), [Case(IntLiteral(1), [Break()]), Case(None, [Continue()])])]))]))])"
    )

# ==========================================
# ARRAYS & STRUCT INSTANTIATION (test_328 - test_337)
# ==========================================

def test_328():
    # test_28: Khai báo mảng 1 chiều có khởi tạo giá trị (Array Literal)
    check_ast(
        "fn main() { let arr = [1, 2, 3]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(arr), None, ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), False)]))])"
    )

def test_329():
    # test_29: Khai báo mảng đa chiều (Multidimensional array literal)
    check_ast(
        "fn main() { let matrix = [[1, 2], [3, 4]]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(matrix), None, ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])]), False)]))])"
    )

def test_330():
    # test_330: Khai báo biến với kiểu mảng nhiều chiều cụ thể ([[i32; 2]; 3]) không khởi tạo
    check_ast(
        "fn main() { let mut grid: [[i32; 2]; 3]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(grid), ArrayType(ArrayType(IntType, 2), 3), None, True)]))])"
    )

def test_331():
    # test_31: Khởi tạo Struct cơ bản (Struct Init Syntax)
    check_ast(
        "fn main() { let p = Point { x: 1, y: 2 }; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(p), None, StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1)), FieldInit(Id(y), IntLiteral(2))]), False)]))])"
    )

def test_332():
    # test_32: Khởi tạo Struct lồng nhau (Nested struct initialization)
    check_ast(
        "fn main() { let line = Line { start: Point { x: 0, y: 0 }, end: p }; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(line), None, StructInit(Id(Line), [FieldInit(Id(start), StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(0)), FieldInit(Id(y), IntLiteral(0))])), FieldInit(Id(end), Id(p))]), False)]))])"
    )

def test_333():
    # test_33: Truy xuất trường dữ liệu của Struct (Field Access) - Bọc trong ExprStmt vì là biểu thức đơn
    check_ast(
        "fn main() { p.x; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(FieldAccess(Id(p), Id(x)))]))])"
    )

def test_334():
    # test_34: Truy xuất phần tử mảng (Array Indexing / ArrayCell)
    check_ast(
        "fn main() { arr[0]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(Id(arr), IntLiteral(0)))]))])"
    )

def test_335():
    # test_35: Truy xuất mảng đa chiều phức tạp kết hợp biểu thức chỉ số
    check_ast(
        "fn main() { grid[1][i + 1]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(ArrayCell(Id(grid), IntLiteral(1)), BinaryOp('+', Id(i), IntLiteral(1))))]))])"
    )

def test_336():
    # test_36: Phép gán giá trị cho Array Cell sử dụng cấu trúc Assign(ArrayCell, expr) -> Bọc bởi ExprStmt
    check_ast(
        "fn main() { arr[i] = 100; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(ArrayCell(Id(arr), Id(i)), IntLiteral(100)))]))])"
    )

def test_337():
    # test_37: Phép gán kết hợp FieldAccess lồng ArrayCell phức tạp (e.g., polygon.points[0].x = 5)
    check_ast(
        "fn main() { mesh.vertices.x = 10; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(FieldAccess(FieldAccess(Id(mesh), Id(vertices)), Id(x)), IntLiteral(10)))]))])"
    )

# ==========================================
# LITERALS & ESCAPE SEQUENCES (test_338 - test_347)
# ==========================================

def test_338():
    # test_38: Boolean Literals (true) gán cho biến
    check_ast(
        "fn main() { let a = true; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(a), None, BoolLiteral(True), False)]))])"
    )

def test_339():
    # test_39: Boolean Literals (false) làm giá trị trả về
    check_ast(
        "fn main() { return false; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([Return(BoolLiteral(False))]))])"
    )

def test_340():
    # test_40: Floating-point với ký pháp khoa học e (Scientific notation - số dương)
    check_ast(
        "fn main() { let x = 1.23e4; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(x), None, FloatLiteral(12300.0), False)]))])"
    )

def test_341():
    # test_41: Floating-point với ký pháp khoa học e (Số mũ âm và chữ E hoa)
    check_ast(
        "fn main() { let y = 5.0E-3; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(y), None, FloatLiteral(0.005), False)]))])"
    )

def test_342():
    # test_42: String Literal cơ bản không chứa ký tự đặc biệt
    check_ast(
        "fn main() { let s = \"Hello\"; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(s), None, StringLiteral(\"Hello\"), False)]))])"
    )

def test_343():
    # test_43: Escape sequence xuống dòng (\n) bên trong chuỗi
    check_ast(
        "fn main() { let s = \"Line1\\nLine2\"; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(s), None, StringLiteral(\"Line1\\nLine2\"), False)]))])"
    )

def test_344():
    # test_44: Escape sequence tab (\t) bên trong chuỗi
    check_ast(
        "fn main() { let s = \"Col1\\tCol2\"; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(s), None, StringLiteral(\"Col1\\tCol2\"), False)]))])"
    )

def test_345():
    # test_45: Escape sequence dấu nháy kép (\") lồng bên trong chuỗi
    check_ast(
        "fn main() { let s = \"She said \\\"Yes\\\"\"; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(s), None, StringLiteral(\"She said \\\"Yes\\\"\"), False)]))])"
    )

def test_346():
    # test_46: Escape sequence dấu gạch chéo ngược (\\)
    check_ast(
        "fn main() { let s = \"C:\\\\User\\\\Rust\"; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(s), None, StringLiteral(\"C:\\\\User\\\\Rust\"), False)]))])"
    )

def test_347():
    # test_47: Tổ hợp nâng cao chứa nhiều loại escape sequences lồng nhau (\n, \t, \", \\)
    check_ast(
        "fn main() { let s = \"Data:\\t\\\"Value\\\"\\nPath:\\\\root\"; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([VarDecl(Id(s), None, StringLiteral(\"Data:\\t\\\"Value\\\"\\nPath:\\\\root\"), False)]))])"
    )

# ==========================================
# FUNCTION CALLS & RETURN (test_348 - test_352)
# ==========================================

def test_348():
    # test_48: Gọi hàm không có đối số (User/Library function invocation mà không có tham số)
    # Vì đứng độc lập làm câu lệnh nên CallExpr được bọc bởi ExprStmt
    check_ast(
        "fn main() { clear_cache(); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(clear_cache), []))]))])"
    )

def test_349():
    # test_49: Gọi hàm có truyền nhiều đối số từ đơn giản (Literal, Id) đến phức tạp
    check_ast(
        "fn main() { update_score(player_id, 100); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(update_score), [Id(player_id), IntLiteral(100)]))]))])"
    )

def test_350():
    # test_50: Lệnh return mang kết quả là một biểu thức số học phức tạp (Complex arithmetic results)
    # Toán tử hai ngôi sử dụng dấu nháy đơn, Return trả về trực tiếp không bọc ExprStmt
    check_ast(
        "fn compute(a: i32, b: i32) -> i32 { return (a + b) * 2; }",
        "Program([FuncDecl(Id(compute), [VarDecl(Id(a), IntType, None, False), VarDecl(Id(b), IntType, None, False)], IntType, Block([Return(BinaryOp('*', BinaryOp('+', Id(a), Id(b)), IntLiteral(2)))]))])"
    )

def test_351():
    # test_51: Lệnh gọi hàm lồng nhau (Call expression làm đối số cho một Call expression khác)
    check_ast(
        "fn main() { print_i32(get_next_id(offset)); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(print_i32), [CallExpr(Id(get_next_id), [Id(offset)])]))]))])"
    )

def test_352():
    # test_52: Lệnh return mang kết quả là một lệnh gọi hàm khác (Return carrying a call expression)
    check_ast(
        "fn get_data() -> i32 { return fetch_from_db(10, true); }",
        "Program([FuncDecl(Id(get_data), [], IntType, Block([Return(CallExpr(Id(fetch_from_db), [IntLiteral(10), BoolLiteral(True)]))]))])"
    )

# ==========================================
# OPERATORS & PRECEDENCE (test_353 - test_381)
# ==========================================

def test_353():
    # test_53: Toán tử một ngôi (UnaryOp) có độ ưu tiên cao hơn toán tử nhân chia
    check_ast(
        "fn main() { -a * !b; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('*', UnaryOp('-', Id(a)), UnaryOp('!', Id(b))))]))])"
    )

def test_354():
    # test_54: Phép nhân chia và chia dư (Multiplicative: *, /, %) cùng cấp độ ưu tiên, kết hợp trái
    check_ast(
        "fn main() { a * b / c % d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('%', BinaryOp('/', BinaryOp('*', Id(a), Id(b)), Id(c)), Id(d)))]))])"
    )

def test_355():
    # test_55: Toán tử multiplicative (*, /, %) có độ ưu tiên cao hơn additive (+, -)
    check_ast(
        "fn main() { a + b * c - d / e; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('-', BinaryOp('+', Id(a), BinaryOp('*', Id(b), Id(c))), BinaryOp('/', Id(d), Id(e))))]))])"
    )

def test_356():
    # test_56: Toán tử cộng trừ (Additive: +, -) kết hợp trái
    check_ast(
        "fn main() { a - b + c - d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('-', BinaryOp('+', BinaryOp('-', Id(a), Id(b)), Id(c)), Id(d)))]))])"
    )

def test_357():
    # test_57: Toán tử Additive có độ ưu tiên cao hơn toán tử Relational (<, <=, >, >=)
    check_ast(
        "fn main() { a + b < c - d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('<', BinaryOp('+', Id(a), Id(b)), BinaryOp('-', Id(c), Id(d))))]))])"
    )

def test_358():
    # test_58: Toán tử quan hệ (Relational: <=) so với toán tử nhân cộng
    check_ast(
        "fn main() { a * b >= c + d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('>=', BinaryOp('*', Id(a), Id(b)), BinaryOp('+', Id(c), Id(d))))]))])"
    )

def test_359():
    # test_59: Phép so sánh bằng (Equality: ==) có độ ưu tiên thấp hơn toán tử quan hệ (Relational: >)
    check_ast(
        "fn main() { a > b == c <= d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('==', BinaryOp('>', Id(a), Id(b)), BinaryOp('<=', Id(c), Id(d))))]))])"
    )

def test_360():
    # test_60: Phép so sánh không bằng (Equality: !=) so với các phép toán additive
    check_ast(
        "fn main() { a + b != c - d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('!=', BinaryOp('+', Id(a), Id(b)), BinaryOp('-', Id(c), Id(d))))]))])"
    )

def test_361():
    # test_61: Toán tử so sánh bằng có độ ưu tiên cao hơn toán tử logic AND (&&)
    check_ast(
        "fn main() { a == b && c != d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('&&', BinaryOp('==', Id(a), Id(b)), BinaryOp('!=', Id(c), Id(d))))]))])"
    )

def test_362():
    # test_62: Toán tử logic AND (&&) có độ ưu tiên cao hơn toán tử logic OR (||)
    check_ast(
        "fn main() { a || b && c; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('||', Id(a), BinaryOp('&&', Id(b), Id(c))))]))])"
    )

def test_363():
    # test_63: Phép logic OR (||) kết hợp trái
    check_ast(
        "fn main() { a || b || c || d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('||', BinaryOp('||', BinaryOp('||', Id(a), Id(b)), Id(c)), Id(d)))]))])"
    )

def test_364():
    # test_64: Phép logic AND (&&) kết hợp trái
    check_ast(
        "fn main() { a && b && c && d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('&&', BinaryOp('&&', BinaryOp('&&', Id(a), Id(b)), Id(c)), Id(d)))]))])"
    )

def test_365():
    # test_65: Cặp ngoặc tròn (LPAREN/RPAREN) thay đổi độ ưu tiên: Ep buộc OR thực hiện trước AND
    check_ast(
        "fn main() { (a || b) && c; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('&&', BinaryOp('||', Id(a), Id(b)), Id(c)))]))])"
    )

def test_366():
    # test_66: Cặp ngoặc tròn ép buộc phép cộng thực hiện trước phép nhân
    check_ast(
        "fn main() { (a + b) * c; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('*', BinaryOp('+', Id(a), Id(b)), Id(c)))]))])"
    )

def test_367():
    # test_67: Phép gán cơ bản (Assignment) có độ ưu tiên thấp nhất
    check_ast(
        "fn main() { x = a + b * c; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(x), BinaryOp('+', Id(a), BinaryOp('*', Id(b), Id(c)))))]))])"
    )

def test_368():
    # test_68: Phép gán kết hợp phải (Right-associative Assignment: a = b = c)
    check_ast(
        "fn main() { a = b = c; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(a), Assign(Id(b), Id(c))))]))])"
    )

def test_369():
    # test_69: Chuỗi phép gán kết hợp phải dài hơn (a = b = c = d)
    check_ast(
        "fn main() { a = b = c = d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(a), Assign(Id(b), Assign(Id(c), Id(d)))))]))])"
    )

def test_370():
    # test_70: Phép gán cho phần tử mảng kết hợp phải ở vế phải (arr[i] = x = 1)
    check_ast(
        "fn main() { arr[i] = x = 1; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(ArrayCell(Id(arr), Id(i)), Assign(Id(x), IntLiteral(1))))]))])"
    )

def test_371():
    # test_71: Tổ hợp toán tử: Phép chia dư (%) kết hợp toán tử một ngôi (-)
    check_ast(
        "fn main() { a % -b; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('%', Id(a), UnaryOp('-', Id(b))))]))])"
    )

def test_372():
    # test_72: Phép toán so sánh phức tạp kết hợp toán tử logic (a < b && c > d || !e)
    check_ast(
        "fn main() { a < b && c > d || !e; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('||', BinaryOp('&&', BinaryOp('<', Id(a), Id(b)), BinaryOp('>', Id(c), Id(d))), UnaryOp('!', Id(e))))]))])"
    )

def test_373():
    # test_73: Dấu ngoặc lồng nhau nhiều tầng thay đổi hoàn toàn cục diện precedence
    check_ast(
        "fn main() { a / ((b - c) * d); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('/', Id(a), BinaryOp('*', BinaryOp('-', Id(b), Id(c)), Id(d))))]))])"
    )

def test_374():
    # test_74: Kết hợp logic phức tạp với dấu ngoặc tròn
    check_ast(
        "fn main() { !(a && (b || c)); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(UnaryOp('!', BinaryOp('&&', Id(a), BinaryOp('||', Id(b), Id(c)))))]))])"
    )

def test_375():
    # test_75: Biểu thức số học phức tạp làm index cho mảng (ArrayCell)
    check_ast(
        "fn main() { arr[a + b * c]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(Id(arr), BinaryOp('+', Id(a), BinaryOp('*', Id(b), Id(c)))))]))])"
    )

def test_376():
    # test_76: Biểu thức số học phức tạp bên trong lệnh gọi hàm (CallExpr argument)
    check_ast(
        "fn main() { foo(a - b / c); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(foo), [BinaryOp('-', Id(a), BinaryOp('/', Id(b), Id(c)))]))]))])"
    )

def test_377():
    # test_77: Phép gán cho thuộc tính struct với biểu thức logic (obj.field = a == b)
    check_ast(
        "fn main() { obj.field = a == b; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(FieldAccess(Id(obj), Id(field)), BinaryOp('==', Id(a), Id(b))))]))])"
    )

def test_378():
    # test_78: Kiểm tra độ ưu tiên của toán tử chia (/) so với toán tử một ngôi logic (!)
    check_ast(
        "fn main() { !a / b; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('/', UnaryOp('!', Id(a)), Id(b)))]))])"
    )

def test_379():
    # test_79: Hỗn hợp phép toán so sánh quan hệ khác loại liên tiếp trái qua phải
    check_ast(
        "fn main() { a < b == c > d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(BinaryOp('==', BinaryOp('<', Id(a), Id(b)), BinaryOp('>', Id(c), Id(d))))]))])"
    )

def test_380():
    # test_80: Phép gán lồng nhau sâu kết hợp các biến định danh ở cuối chuỗi
    check_ast(
        "fn main() { x = y = z = a + 1; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(x), Assign(Id(y), Assign(Id(z), BinaryOp('+', Id(a), IntLiteral(1))))))]))])"
    )

def test_381():
    # test_81: Dạng biểu thức logic dài tận cùng bằng một phép gán phức tạp (kiểm thử biên ưu tiên thấp nhất)
    check_ast(
        "fn main() { res = a && b || c && !d; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(res), BinaryOp('||', BinaryOp('&&', Id(a), Id(b)), BinaryOp('&&', Id(c), UnaryOp('!', Id(d))))))]))])"
    )

# ==========================================
# NESTED COMPLEX ACCESSES (test_382 - test_396)
# ==========================================

def test_382():
    # test_82: Phần tử mảng làm chỉ số cho chính mảng đó hoặc mảng khác (arr[arr[0]])
    check_ast(
        "fn main() { arr[arr[0]]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(Id(arr), ArrayCell(Id(arr), IntLiteral(0))))]))])"
    )

def test_383():
    # test_83: Ma trận đa chiều dùng chỉ số là phần tử của ma trận khác (matrix[row[0]][col[1]])
    check_ast(
        "fn main() { matrix[row[0]][col[1]]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(ArrayCell(Id(matrix), ArrayCell(Id(row), IntLiteral(0))), ArrayCell(Id(col), IntLiteral(1))))]))])"
    )

def test_384():
    # test_84: Truy xuất thuộc tính struct nằm trong một phần tử mảng (arr[0].x)
    check_ast(
        "fn main() { arr[0].x; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(FieldAccess(ArrayCell(Id(arr), IntLiteral(0)), Id(x)))]))])"
    )

def test_385():
    # test_85: Truy xuất phần tử mảng bên trong một thuộc tính struct (obj.data[1])
    check_ast(
        "fn main() { obj.data[1]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(FieldAccess(Id(obj), Id(data)), IntLiteral(1)))]))])"
    )

def test_386():
    # test_86: Chuỗi truy xuất thuộc tính liên tiếp lồng mảng đa chiều (mesh.faces[0].vertices[2].x)
    check_ast(
        "fn main() { mesh.faces[0].vertices[2].x; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id(mesh), Id(faces)), IntLiteral(0)), Id(vertices)), IntLiteral(2)), Id(x)))]))])"
    )

def test_387():
    # test_87: Lệnh gọi hàm trả về một đối tượng và truy xuất thuộc tính ngay lập tức (get_point().x)
    # Theo primary_expr: ctx.DOT() đi sau primary_expr (CallExpr)
    check_ast(
        "fn main() { get_point().x; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(FieldAccess(CallExpr(Id(get_point), []), Id(x)))]))])"
    )

def test_388():
    # test_88: Lệnh gọi hàm trả về một mảng và truy xuất chỉ số ngay lập tức (get_arr()[0])
    check_ast(
        "fn main() { get_arr()[0]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(CallExpr(Id(get_arr), []), IntLiteral(0)))]))])"
    )

def test_389():
    # test_89: Kết hợp phức tạp: Hàm trả về mảng chứa struct, lấy phần tử rồi truy xuất thuộc tính (func(a)[0].b)
    check_ast(
        "fn main() { func(a)[0].b; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(FieldAccess(ArrayCell(CallExpr(Id(func), [Id(a)]), IntLiteral(0)), Id(b)))]))])"
    )

def test_390():
    # test_90: Đối số của hàm là một chuỗi truy xuất thuộc tính và mảng lồng nhau (foo(obj.arr[i].val))
    check_ast(
        "fn main() { foo(obj.arr[i].val); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(foo), [FieldAccess(ArrayCell(FieldAccess(Id(obj), Id(arr)), Id(i)), Id(val))]))]))])"
    )

def test_391():
    # test_91: Đối số của hàm chứa một lệnh gọi hàm khác được truy xuất chỉ số mảng (foo(bar()[1]))
    check_ast(
        "fn main() { foo(bar()[1]); }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(CallExpr(Id(foo), [ArrayCell(CallExpr(Id(bar), []), IntLiteral(1))]))]))])"
    )

def test_392():
    # test_92: Phép gán giá trị cho một cấu trúc lồng nhau cực sâu (matrix[arr[0]][obj.x] = 42)
    # Vì vế trái là ArrayCell nên hàm visitAssign_expr sẽ map thành Assign(ArrayCell, expr)
    check_ast(
        "fn main() { matrix[arr[0]][obj.x] = 42; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(ArrayCell(ArrayCell(Id(matrix), ArrayCell(Id(arr), IntLiteral(0))), FieldAccess(Id(obj), Id(x))), IntLiteral(42)))]))])"
    )

def test_393():
    # test_93: Phép gán giá trị cho thuộc tính của struct thu được từ phần tử mảng (cluster.nodes[i].status = true)
    # Vế trái kết thúc bằng thuộc tính nên visitAssign_expr xử lý nhánh gán FieldAccess
    check_ast(
        "fn main() { cluster.nodes[i].status = true; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(FieldAccess(ArrayCell(FieldAccess(Id(cluster), Id(nodes)), Id(i)), Id(status)), BoolLiteral(True)))]))])"
    )

def test_394():
    # test_94: Truy xuất chỉ số mảng đa chiều lồng chuỗi gọi hàm liên tục (get_matrix()[get_index(1)][0])
    check_ast(
        "fn main() { get_matrix()[get_index(1)][0]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(ArrayCell(CallExpr(Id(get_matrix), []), CallExpr(Id(get_index), [IntLiteral(1)])), IntLiteral(0)))]))])"
    )

def test_395():
    # test_95: Phép toán số học phức tạp nằm bên trong chỉ số mảng của thuộc tính một đối tượng (data.list[i + active_node.id * 2])
    check_ast(
        "fn main() { data.list[i + active_node.id * 2]; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(ArrayCell(FieldAccess(Id(data), Id(list)), BinaryOp('+', Id(i), BinaryOp('*', FieldAccess(Id(active_node), Id(id)), IntLiteral(2)))))]))])"
    )

def test_396():
    # test_96: Chuỗi hỗn hợp tối đa biên độ: Gọi hàm lấy struct, lấy mảng, gọi hàm trong index, lấy field (api().data[fetch_idx()].meta.id)
    check_ast(
        "fn main() { api().data[fetch_idx()].meta.id; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(FieldAccess(FieldAccess(ArrayCell(FieldAccess(CallExpr(Id(api), []), Id(data)), CallExpr(Id(fetch_idx), [])), Id(meta)), Id(id)))]))])"
    )

# ==========================================
# CHAINED ASSIGNMENT EXPRESSIONS (test_397 - test_400)
# ==========================================

def test_397():
    # test_97: Chuỗi phép gán kết hợp phải cơ bản với biến đơn (x = y = 5)
    # Được bọc bởi ExprStmt do đứng độc lập làm câu lệnh biểu thức
    check_ast(
        "fn main() { x = y = 5; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(x), Assign(Id(y), IntLiteral(5))))]))])"
    )

def test_398():
    # test_98: Phép gán chuỗi dài hơn kết hợp biến cục bộ (a = b = c = d = 10)
    check_ast(
        "fn main() { a = b = c = d = 10; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(Id(a), Assign(Id(b), Assign(Id(c), Assign(Id(d), IntLiteral(10))))))]))])"
    )

def test_399():
    # test_99: Phép gán chuỗi phức tạp với mục tiêu gán là thuộc tính struct (a.b = c.d = 1)
    # visitAssign_expr sẽ nhận diện nhánh gán FieldAccess cho cả 2 tầng gán
    check_ast(
        "fn main() { a.b = c.d = 1; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(FieldAccess(Id(a), Id(b)), Assign(FieldAccess(Id(c), Id(d)), IntLiteral(1))))]))])"
    )

def test_400():
    # test_100: Phép gán chuỗi hỗn hợp giữa phần tử mảng và thuộc tính cấu trúc (arr[0] = obj.x = val = 99)
    check_ast(
        "fn main() { arr[0] = obj.x = val = 99; }",
        "Program([FuncDecl(Id(main), [], VoidType, Block([ExprStmt(Assign(ArrayCell(Id(arr), IntLiteral(0)), Assign(FieldAccess(Id(obj), Id(x)), Assign(Id(val), IntLiteral(99)))))]))])"
    )