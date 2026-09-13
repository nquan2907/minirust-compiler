import pytest
from checker.StaticChecker import StaticChecker
from checker.StaticError import *
from TestUtils import TestChecker
from utils.AST import *


def test_1():
    source = "fn main() { x = 10; }"
    TestChecker.checkChecker(source, "UndeclaredIdentifier(x)")

def test_2():
    source = "fn main() { foo(); }"
    TestChecker.checkChecker(source, "UndeclaredFunction(foo)")

def test_3():
    source = "fn main() { let x: Person; }"
    TestChecker.checkChecker(source, "UndeclaredStruct(Person)")

def test_4():
    source = "struct Point { x: i32; } struct Point { y: i32; } fn main() {}"
    TestChecker.checkChecker(source, "Redeclared(Struct, Point)")

def test_5():
    # Sửa: Bỏ lặp tên field trong struct
    source = "struct Point { x: i32, x: f32 } fn main() {}"
    TestChecker.checkChecker(source, "Redeclared(Member, x)")

def test_6():
    source = "fn foo() {} fn foo() {} fn main() {}"
    TestChecker.checkChecker(source, "Redeclared(Function, foo)")

def test_7():
    source = "fn foo(a: i32, a: i32) {} fn main() {}"
    TestChecker.checkChecker(source, "Redeclared(Parameter, a)")

def test_8():
    source = "fn main(x: i32) { let x: i32 = 5; }"
    TestChecker.checkChecker(source, "Redeclared(Variable, x)")

def test_9():
    source = "fn main() { let mut a: i32 = 1; let mut a: i32 = 2; }"
    TestChecker.checkChecker(source, "Redeclared(Variable, a)")

def test_10():
    source = "fn main() { let mut x: i32 = 1; { let mut x: f32 = 2.0; } print_i32(y); }"
    TestChecker.checkChecker(source, "UndeclaredIdentifier(y)")

def test_11():
    source = "fn main() { { let mut inner: i32 = 10; } print_i32(inner); }"
    TestChecker.checkChecker(source, "UndeclaredIdentifier(inner)")

def test_12():
    source = "fn main() { print_i32(a); let mut a: i32 = 5; }"
    TestChecker.checkChecker(source, "UndeclaredIdentifier(a)")

def test_13():
    source = "fn foo(x: i32) -> void {} fn main() { foo(x); }"
    TestChecker.checkChecker(source, "UndeclaredIdentifier(x)")

def test_14():
    # Sửa: Khai báo hai biến trùng tên trong cùng một Scope (trong thân vòng lặp for)
    source = "fn main() { for i in 0..10 { let mut x: i32 = 1; let mut x: i32 = 2; } }"
    TestChecker.checkChecker(source, "Redeclared(Variable, x)")

def test_15():
    source = "struct Node { next: Unknown; } fn main() {}"
    TestChecker.checkChecker(source, "UndeclaredStruct(Unknown)")

def test_16():
    source = "fn main() { print_unknown(); }"
    TestChecker.checkChecker(source, "UndeclaredFunction(print_unknown)")

def test_17():
    source = "struct A { x: i32; } struct B { a: A; } fn main() { let mut b: C; }"
    TestChecker.checkChecker(source, "UndeclaredStruct(C)")

def test_18():
    source = "fn foo(a: Unknown) {} fn main() {}"
    TestChecker.checkChecker(source, "UndeclaredStruct(Unknown)")

def test_19():
    source = "fn foo() -> Unknown {} fn main() {}"
    TestChecker.checkChecker(source, "UndeclaredStruct(Unknown)")

def test_20():
    source = "fn main() { let mut x: [Unknown; 5]; }"
    TestChecker.checkChecker(source, "UndeclaredStruct(Unknown)")

# --- Type Mismatch Errors (test_21 - test_35) ---

def test_21():
    # Return mismatch: Trả về BoolLiteral(True) trong hàm kiểu f32
    source = "fn foo() -> f32 { return true; } fn main() {}"
    TestChecker.checkChecker(source, "TypeMismatchInStatement(Return(BoolLiteral(True)))")

def test_22():
    # Điều kiện While không phải BoolType
    source = "fn main() { while 10 {} }"
    TestChecker.checkChecker(source, "TypeMismatchInStatement(While(IntLiteral(10), Block([])))")

def test_23():
    source = "fn main() { while (1.5) {} }"
    TestChecker.checkChecker(source, "TypeMismatchInStatement(While(FloatLiteral(1.5), Block([])))")

def test_24():
    source = "fn foo() -> i32 { return true; } fn main() {}"
    TestChecker.checkChecker(source, "TypeMismatchInStatement(Return(BoolLiteral(True)))")

def test_25():
    source = "fn foo() -> void { return 10; } fn main() {}"
    TestChecker.checkChecker(source, "TypeMismatchInStatement(Return(IntLiteral(10)))")

def test_26():
    # Return mismatch: Trả về IntLiteral(123) trong hàm kiểu string
    source = "fn foo() -> string { return 123; } fn main() {}"
    TestChecker.checkChecker(source, "TypeMismatchInStatement(Return(IntLiteral(123)))")

def test_27():
    # Gọi hàm builtin print_i32 nhưng truyền vào kiểu bool -> TypeMismatchInExpression
    source = "fn main() { print_i32(true); }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(CallExpr(Id(print_i32), [BoolLiteral(True)]))")

def test_28():
    # Truy cập phần tử mảng bằng chỉ số kiểu float (3.14) -> TypeMismatchInExpression
    source = "fn main() { let mut arr = [1, 2, 3]; print_i32(arr[3.14]); }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(ArrayCell(Id(arr), FloatLiteral(3.14)))")

def test_29():
    # Lỗi truy cập thuộc tính trên biến kiểu IntType thay vì StructType
    source = "fn main() { let x = 10; print_i32(x.value); }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(FieldAccess(Id(x), Id(value)))")

def test_30():
    source = "fn foo(x: i32) -> void {} fn main() { foo(3.14); }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(CallExpr(Id(foo), [FloatLiteral(3.14)]))")

def test_31():
    source = "fn main() { let arr = [1, 2, 3.5]; }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(ArrayLiteral([IntLiteral(1), IntLiteral(2), FloatLiteral(3.5)]))")

def test_32():
    # Index mảng là BoolLiteral(True)
    source = "fn main() { let mut arr = [1, 2]; print_i32(arr[true]); }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(ArrayCell(Id(arr), BoolLiteral(True)))")

def test_33():
    source = "fn main() { let x = 10; print_i32(x[0]); }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(ArrayCell(Id(x), IntLiteral(0)))")

def test_34():
    # Khai báo biến không kiểu từ hàm void -> TypeCannotBeInferred(CallExpr)
    source = "fn void_fn() -> void {} fn main() { let x = void_fn(); }"
    TestChecker.checkChecker(source, "TypeCannotBeInferred(CallExpr(Id(void_fn), []))")

def test_35():
    source = "fn main() { let mut arr = []; }"
    TestChecker.checkChecker(source, "TypeCannotBeInferred(ArrayLiteral([]))")

# --- Assignment Errors (test_36 - test_45) ---

def test_36():
    # Gán giá trị cho biến hằng (let không có mut)
    source = "fn main() { let x: i32 = 10; x = 20; }"
    TestChecker.checkChecker(source, "CannotAssignToConstant(Id(x))")

def test_37():
    # Gán giá trị cho tham số hàm (mặc định là immutable)
    source = "fn foo(x: i32) -> void { x = 100; } fn main() {}"
    TestChecker.checkChecker(source, "CannotAssignToConstant(Id(x))")

def test_38():
    # Gán giá trị cho phần tử mảng hằng (arr không có mut)
    source = "fn main() { let arr: [i32; 2] = [1, 2]; arr[0] = 5; }"
    TestChecker.checkChecker(source, "CannotAssignToConstant(ArrayCell(Id(arr), IntLiteral(0)))")

def test_39():
    # Gán giá trị cho thuộc tính của Struct hằng (p không có mut)
    source = "struct Point { x: i32, y: i32 } fn main() { let p = Point{x: 1, y: 2}; p.x = 10; }"
    TestChecker.checkChecker(source, "CannotAssignToConstant(FieldAccess(Id(p), Id(x)))")

def test_40():
    # Gán giá trị cho biến đếm của vòng lặp for (biến đếm là immutable)
    source = "fn main() { for i in 0..10 { i = 5; } }"
    TestChecker.checkChecker(source, "CannotAssignToConstant(Id(i))")

def test_41():
    # Lỗi L-Value: Gán giá trị cho một hằng số
    source = "fn main() { let a: i32 = 10; a = 20; }"
    TestChecker.checkChecker(source, "CannotAssignToConstant(Id(a))")

def test_42():
    # Lỗi L-Value: Gán giá trị cho tham số hàm (tham số mặc định là constant)
    source = "fn foo(a: i32) -> void { a = 10; } fn main() {}"
    TestChecker.checkChecker(source, "CannotAssignToConstant(Id(a))")

def test_43():
    # Lỗi L-Value: Gán giá trị vào phần tử của mảng hằng (arr không mut)
    source = "fn main() { let arr: [i32; 2] = [1, 2]; arr[0] = 10; }"
    TestChecker.checkChecker(source, "CannotAssignToConstant(ArrayCell(Id(arr), IntLiteral(0)))")

def test_44():
    # Gán sai kiểu dữ liệu cho biến mut (IntType = FloatType không hỗ trợ gán ngược lại nếu không coercible)
    source = "fn main() { let mut x: i32 = 10; x = 3.14; }"
    TestChecker.checkChecker(source, "TypeMismatchInExpression(Assign(Id(x), FloatLiteral(3.14)))")

def test_45():
    # Lỗi L-Value: Gán vào field lồng nhau của Struct hằng
    source = "struct Inner { val: i32 } struct Outer { inner: Inner } fn main() { let o = Outer{inner: Inner{val: 1}}; o.inner.val = 5; }"
    TestChecker.checkChecker(
        source,
        "CannotAssignToConstant(FieldAccess(FieldAccess(Id(o), Id(inner)), Id(val)))"
    )

# --- Struct Instantiation Errors (test_46 - test_57) ---

def test_46():
    # Khởi tạo Struct chưa được khai báo
    source = "fn main() { let p = Point{x: 1, y: 2}; }"
    TestChecker.checkChecker(source, "UndeclaredStruct(Point)")

def test_47():
    # Thừa field không tồn tại 'z' làm set(given_names) != set(decl_fields)
    source = "struct Point { x: i32; y: i32; } fn main() { let p = Point{x: 1, y: 2, z: 3}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1)), FieldInit(Id(y), IntLiteral(2)), FieldInit(Id(z), IntLiteral(3))]))"
    )

def test_48():
    # Thừa trường (extra field 'z')
    source = "struct Point { x: i32; y: i32; } fn main() { let p = Point{x: 1, y: 2, z: 3}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1)), FieldInit(Id(y), IntLiteral(2)), FieldInit(Id(z), IntLiteral(3))]))"
    )

def test_49():
    # Sai tên trường (trường 'z' thay cho 'y')
    source = "struct Point { x: i32; y: i32; } fn main() { let p = Point{x: 1, z: 2}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1)), FieldInit(Id(z), IntLiteral(2))]))"
    )

def test_50():
    # Sai kiểu dữ liệu của trường (x truyền FloatLiteral thay vì IntType)
    source = "struct Point { x: i32; y: f32; } fn main() { let p = Point{x: 1.5, y: 2.0}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), FloatLiteral(1.5)), FieldInit(Id(y), FloatLiteral(2.0))]))"
    )

def test_51():
    # Sai kiểu dữ liệu của trường (y truyền IntLiteral thay vì BoolType)
    source = "struct Point { x: i32; y: bool; } fn main() { let p = Point{x: 1, y: 10}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1)), FieldInit(Id(y), IntLiteral(10))]))"
    )

def test_52():
    # Trường x là f32 nhưng truyền i32 (vì _assignable yêu cầu kiểu chính xác, không cho coercion)
    source = "struct Point { x: f32; } fn main() { let p = Point{x: 1}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1))]))"
    )

def test_53():
    # Sai tên field ('a' thay vì 'val') làm set(given_names) != set(decl_fields)
    source = "struct Node { val: i32; } fn main() { let n = Node{a: 10}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Node), [FieldInit(Id(a), IntLiteral(10))]))"
    )

def test_54():
    # Khởi tạo Struct với giá trị kiểu FloatLiteral(1.5) cho trường IntType ('val') -> _assignable trả về False
    source = "struct Item { val: i32; } fn main() { let i = Item{val: 1.5}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Item), [FieldInit(Id(val), FloatLiteral(1.5))]))"
    )

def test_55():
    # Trùng lặp trường khi khởi tạo (lặp lại 'x' thay vì 'y')
    source = "struct Point { x: i32; y: i32; } fn main() { let p = Point{x: 1, x: 2}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Point), [FieldInit(Id(x), IntLiteral(1)), FieldInit(Id(x), IntLiteral(2))]))"
    )

def test_56():
    # Sai kiểu chuỗi (name truyền IntLiteral)
    source = "struct Person { name: string; age: i32; } fn main() { let p = Person{name: 123, age: 20}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Person), [FieldInit(Id(name), IntLiteral(123)), FieldInit(Id(age), IntLiteral(20))]))"
    )

def test_57():
    # Khởi tạo trường dạng mảng sai kích thước/kiểu
    source = "struct Container { data: [i32; 2]; } fn main() { let c = Container{data: [1, 2, 3]}; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(StructInit(Id(Container), [FieldInit(Id(data), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))"
    )

# --- Field Access Errors (test_58 - test_65) ---

def test_58():
    # Truy cập trường 'z' không tồn tại trong struct Point (dùng let mut để đảm bảo StructInit hợp lệ)
    source = "struct Point { x: i32; y: i32; } fn main() { let mut p: Point; print_i32(p.z); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(Id(p), Id(z)))"
    )

def test_59():
    # Truy cập thuộc tính trên biến kiểu IntType (x.value)
    source = "fn main() { let x: i32 = 10; print_i32(x.value); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(Id(x), Id(value)))"
    )

def test_60():
    # Truy cập thuộc tính trên kiểu ArrayType (arr.length)
    source = "fn main() { let arr: [i32; 3] = [1, 2, 3]; print_i32(arr.length); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(Id(arr), Id(length)))"
    )

def test_61():
    # Truy cập trường không tồn tại 'unknown' trên biến Struct (tránh khởi tạo lồng nhau gây lỗi Parser)
    source = "struct Inner { val: i32; } fn main() { let mut in_obj: Inner; print_i32(in_obj.unknown); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(Id(in_obj), Id(unknown)))"
    )

def test_62():
    # Truy cập thuộc tính trên hằng BoolLiteral (true.flag)
    source = "fn main() { print_i32(true.flag); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(BoolLiteral(True), Id(flag)))"
    )

def test_63():
    # Truy cập trường 'y' không tồn tại của Struct A (nhưng 'y' thuộc Struct B khác)
    source = "struct A { x: i32; } struct B { y: i32; } fn main() { let a = A{x: 10}; print_i32(a.y); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(Id(a), Id(y)))"
    )

def test_64():
    # Truy cập thuộc tính trên trường dữ liệu dạng mảng bên trong Struct (c.items.sub)
    source = "struct Container { items: [i32; 3]; } fn main() { let c = Container{items: [1, 2, 3]}; print_i32(c.items.sub); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(FieldAccess(Id(c), Id(items)), Id(sub)))"
    )

def test_65():
    # Truy cập thuộc tính trên kết quả trả về của hàm không phải kiểu StructType (foo().field)
    source = "fn foo() -> i32 { return 10; } fn main() { print_i32(foo().field); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(FieldAccess(CallExpr(Id(foo), []), Id(field)))"
    )

# --- Loop Control Errors (test_66 - test_70) ---

def test_66():
    # Lỗi: break nằm trực tiếp trong hàm main (ngoài mọi vòng lặp/switch)
    source = "fn main() { break; }"
    TestChecker.checkChecker(source, "MustInLoop(Break())")

def test_67():
    # Lỗi: continue nằm trực tiếp trong hàm main (ngoài mọi vòng lặp)
    source = "fn main() { continue; }"
    TestChecker.checkChecker(source, "MustInLoop(Continue())")

def test_68():
    # Lỗi: continue nằm bên trong switch-case (switch chỉ chấp nhận break, không tính vào loop_depth)
    source = "fn main() { switch 1 { case 1: { continue; } } }"
    TestChecker.checkChecker(source, "MustInLoop(Continue())")

def test_69():
    # Lỗi: break nằm bên trong khối if (ngoài vòng lặp)
    source = "fn main() { if true { break; } }"
    TestChecker.checkChecker(source, "MustInLoop(Break())")

def test_70():
    # Lỗi: continue nằm ngoài vòng lặp (vòng lặp while đã kết thúc ở khối lệnh trước)
    source = "fn main() { while true {} continue; }"
    TestChecker.checkChecker(source, "MustInLoop(Continue())")

# --- Sửa đổi test_71 đến test_80 ---

def test_71():
    # Biểu thức switch là FloatLiteral
    source = "fn main() { switch 1.5 {} }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(FloatLiteral(1.5), []))"
    )

def test_72():
    # Thêm dấu " " xung quanh hello
    source = 'fn main() { switch "hello" {} }'
    TestChecker.checkChecker(
        source, 
        'TypeMismatchInStatement(Switch(StringLiteral("hello"), []))'
    )

def test_73():
    # Trùng lặp giá trị case (case 1 xuất hiện 2 lần với body rỗng)
    source = "fn main() { switch 1 { case 1: case 1: } }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(IntLiteral(1), [Case(IntLiteral(1), []), Case(IntLiteral(1), [])]))"
    )

def test_74():
    # Trùng lặp giá trị case boolean (case true xuất hiện 2 lần)
    source = "fn main() { switch true { case true: case true: } }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(BoolLiteral(True), [Case(BoolLiteral(True), []), Case(BoolLiteral(True), [])]))"
    )

def test_75():
    # Case value (BoolLiteral) không khớp với switch expr (IntLiteral)
    source = "fn main() { switch 10 { case true: } }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(IntLiteral(10), [Case(BoolLiteral(True), [])]))"
    )

def test_76():
    # Case value (FloatLiteral) không khớp với switch expr (IntLiteral)
    source = "fn main() { switch 10 { case 2.5: } }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(IntLiteral(10), [Case(FloatLiteral(2.5), [])]))"
    )

def test_77():
    # Case value (IntLiteral) không khớp với switch expr (BoolLiteral)
    source = "fn main() { switch false { case 0: } }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(BoolLiteral(False), [Case(IntLiteral(0), [])]))"
    )

def test_78():
    # Trùng lặp case ở vị trí sau
    source = "fn main() { switch 5 { case 1: case 2: case 2: } }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(IntLiteral(5), [Case(IntLiteral(1), []), Case(IntLiteral(2), []), Case(IntLiteral(2), [])]))"
    )

def test_79():
    # Biểu thức switch là kiểu ArrayType
    source = "fn main() { let mut arr = [1, 2]; switch arr {} }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Switch(Id(arr), []))"
    )

def test_80():
    # Thêm dấu " " xung quanh chuỗi "a" trong StringLiteral
    source = 'fn main() { switch 1 { case 1: case "a": } }'
    TestChecker.checkChecker(
        source, 
        'TypeMismatchInStatement(Switch(IntLiteral(1), [Case(IntLiteral(1), []), Case(StringLiteral("a"), [])]))'
    )

# --- Function Call Errors (test_81 - test_88) ---

def test_81():
    # Lỗi Arity: Truyền thiếu đối số cho hàm (hàm foo nhận 2 tham số, chỉ truyền 1)
    source = "fn foo(a: i32, b: i32) -> void {} fn main() { foo(10); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [IntLiteral(10)]))"
    )

def test_82():
    # Lỗi Arity: Truyền thừa đối số cho hàm (hàm foo nhận 1 tham số, truyền 2)
    source = "fn foo(a: i32) -> void {} fn main() { foo(10, 20); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [IntLiteral(10), IntLiteral(20)]))"
    )

def test_83():
    # Lỗi Arity: Gọi hàm không tham số nhưng truyền vào 1 đối số
    source = "fn foo() -> void {} fn main() { foo(1); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [IntLiteral(1)]))"
    )

def test_84():
    # Lỗi Type Mismatch: Tham số kiểu i32 nhưng truyền đối số kiểu bool
    source = "fn foo(a: i32) -> void {} fn main() { foo(true); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [BoolLiteral(True)]))"
    )

def test_85():
    # Lỗi Type Mismatch: Tham số kiểu i32 nhưng truyền đối số kiểu float
    source = "fn foo(a: i32) -> void {} fn main() { foo(3.14); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [FloatLiteral(3.14)]))"
    )

def test_86():
    # Lỗi Type Mismatch: Tham số thứ 2 bị sai kiểu (hàm nhận (i32, string), truyền (i32, i32))
    source = 'fn foo(a: i32, b: string) -> void {} fn main() { foo(1, 2); }'
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [IntLiteral(1), IntLiteral(2)]))"
    )

def test_87():
    # Lỗi Type Mismatch với Builtin function: println_i32 nhận i32 nhưng truyền string
    source = 'fn main() { println_i32("hello"); }'
    TestChecker.checkChecker(
        source, 
        'TypeMismatchInExpression(CallExpr(Id(println_i32), [StringLiteral("hello")]))'
    )

def test_88():
    # Lỗi Type Mismatch: Tham số nhận một Mảng kích thước 2, nhưng truyền Mảng kích thước 3
    source = "fn foo(arr: [i32; 2]) -> void {} fn main() { foo([1, 2, 3]); }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(CallExpr(Id(foo), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]))"
    )

# --- Other Semantic Errors (test_89 - test_100) ---

def test_89():
    # Main function check: Thiếu hàm main trong chương trình
    source = "fn foo() -> void {}"
    TestChecker.checkChecker(source, "UndeclaredFunction(main)")

def test_90():
    # main() có tham số -> TypeMismatchInStatement trên chính FuncDecl của main
    source = "fn main(x: i32) {}"
    TestChecker.checkChecker(
        source,
        "TypeMismatchInStatement(FuncDecl(Id(main), [VarDecl(Id(x), IntType, None, False)], VoidType, Block([])))"
    )

def test_91():
    # Main function có kiểu trả về khác VoidType -> TypeMismatchInStatement(main_fn)
    source = "fn main() -> i32 { return 0; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(FuncDecl(Id(main), [], IntType, Block([Return(IntLiteral(0))])))"
    )

def test_92():
    # TypeCannotBeInferred: Khai báo biến không truyền kiểu và gán từ hàm void
    source = "fn foo() -> void {} fn main() { let mut x = foo(); }"
    TestChecker.checkChecker(
        source, 
        "TypeCannotBeInferred(CallExpr(Id(foo), []))"
    )

def test_93():
    # Type inference failure: Khởi tạo biến từ hàm trả về VoidType (không thể suy luận kiểu)
    source = "fn foo() -> void {} fn main() { let x = foo(); }"
    TestChecker.checkChecker(
        source, 
        "TypeCannotBeInferred(CallExpr(Id(foo), []))"
    )

def test_94():
    # Return mismatch: Return rỗng trong hàm trả về i32 -> in ra Return(None)
    source = "fn foo() -> i32 { return; } fn main() {}"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Return(None))"
    )

def test_95():
    # Return mismatch: Hàm khai báo trả về void nhưng lại return một giá trị IntLiteral
    source = "fn foo() -> void { return 10; } fn main() {}"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Return(IntLiteral(10)))"
    )

def test_96():
    # Return mismatch: Hàm khai báo trả về bool nhưng return FloatLiteral không thể ép kiểu
    source = "fn foo() -> bool { return 3.14; } fn main() {}"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInStatement(Return(FloatLiteral(3.14)))"
    )

def test_97():
    # Struct đệ quy trực tiếp -> TypeMismatchInStatement trên VarDecl của field 'next'
    source = "struct Node { next: Node } fn main() {}"
    TestChecker.checkChecker(
        source,
        "TypeMismatchInStatement(VarDecl(Id(next), StructType(Id(Node)), None, False))"
    )

def test_98():
    # Type inference / Mismatch: Khai báo mảng rỗng [] không thể suy luận kiểu yếu phần tử
    source = "fn main() { let mut arr = []; }"
    TestChecker.checkChecker(
        source, 
        "TypeCannotBeInferred(ArrayLiteral([]))"
    )

def test_99():
    # Array Literal Type Mismatch: Các phần tử trong Mảng Literal không cùng kiểu dữ liệu (i32 và bool)
    source = "fn main() { let mut arr = [1, true]; }"
    TestChecker.checkChecker(
        source, 
        "TypeMismatchInExpression(ArrayLiteral([IntLiteral(1), BoolLiteral(True)]))"
    )
def test_100():
    # Mảng rỗng [] gán cho kiểu [i32; 5] (kích thước khai báo 5 != 0)
    source = "fn main() { let arr: [i32; 5] = []; }"
    TestChecker.checkChecker(
        source,
        "TypeMismatchInStatement(VarDecl(Id(arr), ArrayType(IntType, 5), ArrayLiteral([]), False))"
    )