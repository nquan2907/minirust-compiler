import pytest
from TestUtils import TestParser

def test_201():
    # Empty structure (Must contain at least one field)
    TestParser.checkParser("struct EmptyBoy {} fn main() { return; }", 1)

def test_202():
    # Missing colon between field name and type
    TestParser.checkParser("struct MissingColon { id i32, salary: f32 } fn main() { return; }", 1)

def test_203():
    # Using semicolon instead of comma to separate fields
    TestParser.checkParser("struct SemicolonSeparator { x: i32; y: i32 } fn main() { return; }", 1)

def test_204():
    # Trailing comma at the end of field declarations
    TestParser.checkParser("struct TrailingComma { name: string, age: i32, } fn main() { return; }", 1)

def test_205():
    # Missing closing brace for struct block
    TestParser.checkParser("struct MissingClosingBrace { id: i32, active: bool fn main() { return; }", 1)

def test_206():
    # Missing opening brace for struct block
    TestParser.checkParser("struct MissingOpeningBrace x: i32, y: i32 } fn main() { return; }", 1)

def test_207():
    # Invalid identifier for field name (using a literal number instead of an ID)
    TestParser.checkParser("struct InvalidFieldName { 123: i32, y: f32 } fn main() { return; }", 1)

def test_208():
    # Missing struct name identifier
    TestParser.checkParser("struct { x: i32, y: f32 } fn main() { return; }", 1)

def test_209():
    # Using 'struct' keyword inside the struct body (invalid member definition syntax)
    TestParser.checkParser("struct NestedStructError { struct: i32 } fn main() { return; }", 1)

def test_210():
    # Missing type declaration entirely (only field name provided)
    TestParser.checkParser("struct MissingType { id: i32, status, score: f32 } fn main() { return; }", 1)

def test_211():
    # Missing function name identifier
    TestParser.checkParser("fn () -> void { return; }", 1)

def test_212():
    # Missing parameter list opening parenthesis
    TestParser.checkParser("fn main) -> void { return; }", 1)

def test_213():
    # Missing parameter list closing parenthesis
    TestParser.checkParser("fn main(val: i32 -> void { return; }", 1)

def test_214():
    # Missing return type arrow '->' when a type is specified
    TestParser.checkParser("fn add(x: i32) i32 { return x; }", 1)

def test_215():
    # Invalid return type indicator (using colon instead of arrow)
    TestParser.checkParser("fn main(): void { return; }", 1)

def test_216():
    # Missing function body block opening brace
    TestParser.checkParser("fn main() -> void return; }", 1)

def test_217():
    # Missing function body block closing brace
    TestParser.checkParser("fn main() -> void { return;", 1)

def test_218():
    # Missing parameter type declaration (only name provided)
    TestParser.checkParser("fn process(data) -> void { return; }", 1)

def test_219():
    # Missing colon between parameter name and type
    TestParser.checkParser("fn process(data i32) -> void { return; }", 1)

def test_220():
    # Missing comma separator between multiple parameters
    TestParser.checkParser("fn add(x: i32 y: i32) -> i32 { return x + y; }", 1)

def test_221():
    # Trailing comma in parameter list (MiniRust grammar says "separated by commas")
    TestParser.checkParser("fn add(x: i32, y: i32,) -> i32 { return x + y; }", 1)

def test_222():
    # Invalid parameter name (using a literal number instead of an identifier)
    TestParser.checkParser("fn update(123: i32) -> void { return; }", 1)

def test_223():
    # Invalid nested structure: 'fn' statement inside a function body block
    TestParser.checkParser("fn outer() -> void { fn inner() -> void { return; } return; }", 1)

def test_224():
    # Invalid nested structure: 'struct' statement inside a function body block
    TestParser.checkParser("fn main() -> void { struct Point { x: i32 } return; }", 1)

def test_225():
    # Missing statement semicolon inside the function body block
    TestParser.checkParser("fn main() -> void { let mut x = 5 x = 10; return; }", 1)

def test_226():
    # Missing variable name identifier after 'let'
    TestParser.checkParser("fn main() { let : i32 = 10; }", 1)

def test_227():
    # Missing semicolon at the end of an explicitly typed declaration
    TestParser.checkParser("fn main() { let x: i32 = 10 }", 1)

def test_228():
    # Multiple comma-separated declarations (Forbidden in MiniRust)
    TestParser.checkParser("fn main() { let x, y = 5; }", 1)

def test_229():
    # Explicitly typed, uninitialized variable but missing 'mut' modifier
    TestParser.checkParser("fn main() { let x: i32; }", 1)

def test_230():
    # Missing 'let' keyword when declaring a new variable with explicit type
    TestParser.checkParser("fn main() { mut count: i32 = 0; }", 1)

def test_231():
    # Wrong position of 'mut' modifier (must be 'let mut', not 'mut let')
    TestParser.checkParser("fn main() { mut let count = 0; }", 1)

def test_232():
    # Missing type name after the colon in explicit declaration
    TestParser.checkParser("fn main() { let x: = 10; }", 1)

def test_233():
    # Missing assignment operator '=' in initialized declaration
    TestParser.checkParser("fn main() { let x: i32 10; }", 1)

def test_234():
    # Empty static array type size (missing integer literal)
    TestParser.checkParser("fn main() { let arr: [i32; ] = [1, 2]; }", 1)

def test_235():
    # Static array type using comma instead of semicolon as separator
    TestParser.checkParser("fn main() { let arr: [i32, 5] = [1, 2, 3, 4, 5]; }", 1)

def test_236():
    # Static array size specifier is a negative integer literal (Syntax handles as Unary minus + Literal, invalid size token)
    TestParser.checkParser("fn main() { let arr: [i32; -5]; }", 1)

def test_237():
    # Static array size specifier is a floating-point literal instead of an i32 literal
    TestParser.checkParser("fn main() { let arr: [i32; 3.5]; }", 1)

def test_238():
    # Missing index expression entirely within array indexing brackets
    TestParser.checkParser("fn main() { let mut arr = [10, 20]; let x = arr[]; }", 1)

def test_239():
    # Semicolon missing at the end of an assignment expression statement
    TestParser.checkParser("fn main() { let mut x = 5; x = 10 }", 1)

def test_240():
    # Variable declaration with type inference but missing initial expression
    TestParser.checkParser("fn main() { let mut x = ; }", 1)

def test_241():
    # Invalid LValue in assignment: trying to assign a value to a literal constant
    TestParser.checkParser("fn main() { 5 = 10; }", 1)

def test_242():
    # Invalid expression: Using range operator '..' outside of a 'for' loop context
    TestParser.checkParser("fn main() { let x = 0..10; }", 1)

def test_243():
    # Missing expression statement semicolon after a function call
    TestParser.checkParser("fn main() { println_i32(42) return; }", 1)

def test_244():
    # Missing type name inside array literal elements (empty initialization with just type is invalid)
    TestParser.checkParser("fn main() { let arr = [i32; 3]; }", 1)

def test_245():
    # Array literal missing closing bracket
    TestParser.checkParser("fn main() { let arr = [1, 2, 3; }", 1)

def test_246():
    # Lỗi ở dòng 2: Thiếu ngoặc nhọn cho block của 'if'
    TestParser.checkParser("fn main() {\n if true count = count + 1;\n}", 2)

def test_247():
    # Lỗi ở dòng 2: Thiếu biểu thức điều kiện của 'if'
    TestParser.checkParser("fn main() {\n if {\n  count = 0;\n }\n}", 2)

def test_248():
    # Lỗi ở dòng 3: Nhánh 'else' thiếu dấu ngoặc nhọn
    TestParser.checkParser("fn main() {\n if true { return; }\n else return;\n}", 3)

def test_249():
    # Lỗi ở dòng 2: Vòng lặp while thiếu ngoặc nhọn body
    TestParser.checkParser("fn main() {\n while true count = count + 1;\n}", 2)

def test_250():
    # Lỗi ở dòng 2: Vòng lặp while thiếu hẳn biểu thức điều kiện
    TestParser.checkParser("fn main() {\n while {\n  return;\n }\n}", 2)

def test_251():
    # Lỗi ở dòng 3: Vòng lặp for thiếu từ khóa 'in'
    TestParser.checkParser("fn main() {\n  let mut x = 0;\n  for i 0..10 {\n   return;\n  }\n}", 3)

def test_252():
    # Lỗi ở dòng 3: Vòng lặp for thiếu toán tử khoảng '..'
    TestParser.checkParser("fn main() {\n  let mut x = 0;\n  for i in 0 10 {\n   return;\n  }\n}", 3)

def test_253():
    # Lỗi ở dòng 3: Vòng lặp for thiếu giá trị kết thúc sau '..'
    TestParser.checkParser("fn main() {\n  let mut x = 0;\n  for i in 0.. {\n   return;\n  }\n}", 3)

def test_254():
    # Lỗi ở dòng 3: Vòng lặp for thiếu ngoặc nhọn body block
    TestParser.checkParser("fn main() {\n  let mut x = 0;\n  for i in 0..10 return;\n}", 3)

def test_255():
    # Lỗi ở dòng 5: Parser quét qua 'break' ở dòng 4, lên dòng 5 gặp '}' mới phát hiện thiếu ';'
    TestParser.checkParser("fn main() {\n while true {\n  let mut a = 1;\n  break\n }\n}", 5)

def test_256():
    # Lỗi ở dòng 5: Tương tự, gặp '}' ở dòng 5 mới biết lệnh 'continue' ở dòng 4 thiếu ';'
    TestParser.checkParser("fn main() {\n while true {\n  let mut a = 1;\n  continue\n }\n}", 5)

def test_257():
    # Lỗi ở dòng 4: Lệnh 'return' ở dòng 3 thiếu ';', lên dòng 4 gặp '}' mới báo lỗi
    TestParser.checkParser("fn main() {\n  let mut x = 5;\n  return\n}", 4)

def test_258():
    # Lỗi ở dòng 4: Lệnh 'return 42' ở dòng 3 thiếu ';', sang dòng 4 gặp '}' mới báo lỗi
    TestParser.checkParser("fn add() -> i32 {\n  let mut x = 5;\n  return 42\n}", 4)

def test_259():
    # Lỗi ở dòng 2: Biểu thức logic trong 'if' bị viết lỗi cú pháp
    TestParser.checkParser("fn main() {\n if true && {\n  return;\n }\n}", 2)

def test_260():
    # Lỗi ở dòng 2: Dùng từ khóa 'else' bơ vơ không có 'if' trước đó
    TestParser.checkParser("fn main() {\n else {\n  return;\n }\n}", 2)

def test_261():
    # Lỗi ở dòng 3: Thiếu dấu ngoặc nhọn mở '{' cho toàn bộ body block của switch
    TestParser.checkParser("fn main() {\n switch count\n  case 0:\n   break;\n }\n}", 3)

def test_262():
    # Lỗi ở dòng 6: Thiếu dấu ngoặc nhọn đóng '}' để kết thúc khối lệnh switch
    TestParser.checkParser("fn main() {\n switch count {\n  case 0:\n   break;\n\n fn test() -> void {}", 6)

def test_263():
    # Lỗi ở dòng 3: Thiếu biểu thức điều kiện điều khiển (controlling expression) của switch
    TestParser.checkParser("fn main() {\n switch {\n  case 0:\n   break;\n }\n}", 2)

def test_264():
    # Lỗi ở dòng 4: Thiếu dấu hai chấm ':' sau giá trị của hằng số 'case'
    TestParser.checkParser("fn main() {\n switch count {\n  case 0\n   break;\n }\n}", 4)

def test_265():
    # Lỗi ở dòng 3: Thiếu giá trị hằng số literal đứng sau từ khóa 'case'
    TestParser.checkParser("fn main() {\n switch count {\n  case :\n   break;\n }\n}", 3)

def test_266():
    # Lỗi ở dòng 4: Thiếu dấu hai chấm ':' sau từ khóa 'default'
    TestParser.checkParser("fn main() {\n switch count {\n  default\n   break;\n }\n}", 4)

def test_267():
    # Lỗi ở dòng 3: Sử dụng biểu thức phức tạp thay vì một hằng số hằng literal trong mệnh đề 'case'
    TestParser.checkParser("fn main() {\n switch count {\n  case (1 + 2):\n   break;\n }\n}", 3)

def test_268():
    # Lỗi ở dòng 4: Viết một câu lệnh lơ lửng ngay khi mở block switch mà không nằm trong 'case' hay 'default' nào
    TestParser.checkParser("fn main() {\n switch count {\n  let x = 5;\n  case 0:\n   break;\n }\n}", 3)

def test_269():
    # Lỗi ở dòng 5: Thiếu dấu chấm phẩy ';' sau câu lệnh 'break' nằm trong mệnh đề 'case' (Lỗi dòng 5 do gặp 'case' tiếp theo)
    TestParser.checkParser("fn main() {\n switch count {\n  case 0:\n   break\n  case 1:\n   break;\n }\n}", 5)

def test_270():
    # Lỗi ở dòng 3: Khối lệnh switch trống rỗng (Đặc tả: "contains one or more case clauses and an optional default clause")
    TestParser.checkParser("fn main() {\n switch count {\n }\n}", 3)

def test_271():
    # Lỗi ở dòng 4: Sang dòng 4 gặp ';' mới phát hiện biểu thức cộng ở dòng 3 bị bỏ lửng
    TestParser.checkParser("fn main() {\n  let mut x = 5;\n  x = 10 +\n  ;\n}", 4)

def test_272():
    # Lỗi ở dòng 2: Hai toán tử nhị phân liên tiếp không có toán hạng ở giữa
    TestParser.checkParser("fn main() {\n  let x = 5 * * 2;\n}", 2)

def test_273():
    # Lỗi ở dòng 2: Sử dụng sai vị trí toán tử phủ định logic (phải viết là !true chứ không phải true!)
    TestParser.checkParser("fn main() {\n  let x = true!;\n}", 2)

def test_274():
    # Lỗi ở dòng 2: Thiếu biểu thức bên trong dấu ngoặc đơn (Cặp ngoặc trống)
    TestParser.checkParser("fn main() {\n  let x = 5 * ();\n}", 2)

def test_275():
    # Lỗi ở dòng 2: Gặp ngay dấu ';' ở dòng 2 khi biểu thức ngoặc '(' chưa được đóng
    TestParser.checkParser("fn main() {\n  let x = (5 + 3;\n}", 2)

def test_276():
    # Lỗi ở dòng 2: Chaining comparisons không có dấu ngoặc đơn (Đặc tả: Chaining a < b < c là Syntax Error)
    TestParser.checkParser("fn main() {\n  let res = 1 < 2 < 3;\n}", 2)

def test_277():
    # Lỗi ở dòng 2: Chaining equality comparisons không có dấu ngoặc đơn (Đặc tả: a == b != c là Syntax Error)
    TestParser.checkParser("fn main() {\n  let res = 1 == 1 != 2;\n}", 2)

def test_278():
    # Lỗi ở dòng 2: Viết liền 2 toán tử logic (&& ||) hợp lệ nhưng sai cú pháp
    TestParser.checkParser("fn main() {\n  let res = true && || false;\n}", 2)

def test_279():
    # Lỗi ở dòng 2: Biểu thức logic kết thúc bằng toán tử (||) thiếu toán hạng phải
    TestParser.checkParser("fn main() {\n  let res = true || ;\n}", 2)

def test_280():
    # Lỗi ở dòng 4: Sang dòng 4 gặp ';' mới phát hiện toán tử '%' ở dòng 3 thiếu toán hạng phải
    TestParser.checkParser("fn main() {\n  let mut x = 10;\n  x = x %\n  ;\n}", 4)

def test_281():
    # Lỗi ở dòng 2: Dấu ngoặc đơn đóng dư thừa không hợp lệ
    TestParser.checkParser("fn main() {\n  let x = (5 + 2));\n}", 2)

def test_282():
    # Lỗi ở dòng 3: Hai toán tử gán '=' liên tiếp đứng cạnh nhau ở dòng 3 làm gãy cú pháp phép gán
    TestParser.checkParser("fn main() {\n  let mut x = 0;\n  x = = 5;\n}", 3)

def test_283():
    # Lỗi ở dòng 2: Thừa toán tử nhị phân ở đầu biểu thức vế phải
    TestParser.checkParser("fn main() {\n  let x = / 5;\n}", 2)

def test_284():
    # Lỗi ở dòng 4: Sang dòng 4 gặp ';' mới phát hiện toán tử Unary '-' ở dòng 3 không có toán hạng đi kèm
    TestParser.checkParser("fn main() {\n  let mut x = 5;\n  x = -\n  ;\n}", 4)

def test_285():
    # Lỗi ở dòng 2: Viết liền hai biểu thức sơ cấp (Primary Expression) mà không có toán tử phân tách
    TestParser.checkParser("fn main() {\n  let x = 5 10;\n}", 2)

def test_286():
    # Lỗi ở dòng 3: Thiếu dấu phẩy phân tách giữa các phần tử trong Array Literal (gặp '3' ở dòng 3)
    TestParser.checkParser("fn main() {\n  let arr = [1, 2\n  3, 4];\n}", 3)

def test_287():
    # Lỗi ở dòng 3: Dấu phẩy dư thừa ở cuối Array Literal (MiniRust không hỗ trợ trailing comma)
    TestParser.checkParser("fn main() {\n  let arr = [1, 2, 3,\n  ];\n}", 3)

def test_288():
    # Lỗi ở dòng 4: Qua dòng 4 đụng ngay ']' mới biết biểu thức chỉ số mảng ở dòng 3 bị bỏ trống
    TestParser.checkParser("fn main() {\n  let mut arr = [10, 20];\n  let x = arr[\n  ];\n}", 4)

def test_289():
    # Lỗi ở dòng 4: Qua dòng 4 gặp ';' mới biết phép truy cập trường '.' ở dòng 3 bị bỏ lửng
    TestParser.checkParser("fn main() {\n  let p = Point { x: 1, y: 2 };\n  let val = p.\n  ;\n}", 4)

def test_290():
    # Lỗi ở dòng 3: Dùng sai ký tự truy cập trường (MiniRust dùng '.', dùng '->' là sai cú pháp)
    TestParser.checkParser("fn main() {\n  let p = Point { x: 1, y: 2 };\n  let val = p->\n  x;\n}", 3)

def test_291():
    # Lỗi ở dòng 3: Gọi hàm thiếu dấu phẩy phân tách giữa các đối số (Arguments)
    TestParser.checkParser("fn main() {\n  print_i32(42\n  100);\n}", 3)

def test_292():
    # ANTLR phát hiện lỗi ngay tại '{' line 2 do không match cấu trúc struct initializer hợp lệ
    TestParser.checkParser("fn main() {\n  let p = Point { x\n  10, y: 20 };\n}", 2)

def test_293():
    # Lỗi ở dòng 3: Khởi tạo Struct thiếu dấu phẩy phân tách giữa các trường initializers
    TestParser.checkParser("fn main() {\n  let p = Point { x: 10\n  y: 20 };\n}", 3)

def test_294():
    # ANTLR phát hiện lỗi ngay tại '{' line 2 do danh sách initializers bị trống rỗng
    TestParser.checkParser("fn main() {\n  let p = Point {\n  };\n}", 2)

def test_295():
    # Lỗi ở dòng 3: Khởi tạo Struct có dấu phẩy dư thừa ở cuối danh sách initializers (Trailing comma)
    TestParser.checkParser("fn main() {\n  let p = Point { x: 10, y: 20,\n  };\n}", 3)

def test_296():
    # Lỗi ở dòng 1: Khai báo biến 'let' ở phạm vi toàn cục (Global Scope) là sai cú pháp.
    # MiniRust chỉ cho phép struct và fn ở cấp độ toàn cục.
    TestParser.checkParser("let GLOBAL_VAL: i32 = 100;\nfn main() {\n  return;\n}", 1)

def test_297():
    # Lỗi ở dòng 2: Định nghĩa hàm lồng trong một hàm khác (Nested function definition)
    # ANTLR đụng 'fn' ở dòng 2 bên trong block của main sẽ báo lỗi ngay tại đây.
    TestParser.checkParser("fn main() {\n  fn inner() -> void {\n    return;\n  }\n}", 2)

def test_298():
    # Lỗi ở dòng 2: Định nghĩa struct lồng trong body của hàm (Nested struct definition)
    # Cấu trúc struct phải nằm ở phạm vi toàn cục, gặp 'struct' ở dòng 2 là lỗi cú pháp.
    TestParser.checkParser("fn main() {\n  struct LocalPoint { x: i32 }\n  return;\n}", 2)

def test_299():
    # Lỗi ở dòng 1: Sai thứ tự từ khóa định nghĩa hàm ('main fn()' thay vì 'fn main()')
    # Parser mong đợi một định danh sau 'fn' hoặc từ khóa 'struct', gặp 'main' ở đầu là gãy ngay.
    TestParser.checkParser("main fn() -> void {\n  return;\n}", 1)

def test_300():
    # Lỗi ở dòng 3: Viết câu lệnh thực thi (Statement) lơ lửng ở phạm vi toàn cục
    # Toàn cục chỉ nhận struct/fn, gặp 'count = 5;' ở dòng 3 là lỗi cú pháp tại token 'count'.
    TestParser.checkParser("struct Dummy { x: i32 }\n\ncount = 5;\n\nfn main() {\n  return;\n}", 3)