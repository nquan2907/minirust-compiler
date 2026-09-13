import pytest
from TestUtils import TestLexer

def test_101():
    # MiniRust Variable and Function keywords
    TestLexer.checkLexer("let mut fn struct", "let, mut, fn, struct")

def test_102():
    # MiniRust Control flow keywords
    TestLexer.checkLexer("if else", "if, else")

def test_103():
    # MiniRust Switch-Case control flow keywords
    TestLexer.checkLexer("switch case default", "switch, case, default")

def test_104():
    # MiniRust Iteration keywords
    TestLexer.checkLexer("while for in", "while, for, in")

def test_105():
    # MiniRust Jump statements
    TestLexer.checkLexer("break continue return", "break, continue, return")

def test_106():
    # MiniRust Numeric type keywords
    TestLexer.checkLexer("i32 f32", "i32, f32")

def test_107():
    # MiniRust Primitive type keywords
    TestLexer.checkLexer("bool void string", "bool, void, string")

def test_108():
    # MiniRust Boolean literals
    TestLexer.checkLexer("true false", "true, false")

def test_109():
    # Mixed MiniRust keywords sequence
    TestLexer.checkLexer("void string switch case", "void, string, switch, case")

def test_110():
    # Full minimum program token sequence using correct MiniRust keywords
    # (Đổi print thành một identifier bình thường vì print không phải keyword của MiniRust)
    TestLexer.checkLexer("fn main() { let x = true; }", "fn, main, (, ), {, let, x, =, true, ;, }")

def test_111():
    # Identifiers: Basic lower-case and upper-case single character names
    TestLexer.checkLexer("x Y z A", "x, Y, z, A")

def test_112():
    # Identifiers: Basic alphanumeric names starting with letters
    TestLexer.checkLexer("var123 counter2026", "var123, counter2026")

def test_113():
    # Identifiers: Internal underscores (Tận dụng ý tưởng test_102 cũ của bạn nhưng đổi tên cho đúng nhóm)
    TestLexer.checkLexer("main print total_sum", "main, print, total_sum")

def test_114():
    # Identifiers: Starting with a single underscore
    TestLexer.checkLexer("_temp _count _x", "_temp, _count, _x")

def test_115():
    # Identifiers: Ending with an underscore
    TestLexer.checkLexer("result_ shadow_ status_", "result_, shadow_, status_")

def test_116():
    # Identifiers: Complex mixed casing, multiple underscores, and numbers
    TestLexer.checkLexer("my_awesome_var_99_updated", "my_awesome_var_99_updated")

def test_117():
    # Shadowing keywords: Identifier contains a keyword as a prefix
    # (letting -> bắt đầu bằng 'let', function -> bắt đầu bằng 'fn')
    TestLexer.checkLexer("letting function if_stmt", "letting, function, if_stmt")

def test_118():
    # Shadowing keywords: Identifier contains a keyword as a suffix
    TestLexer.checkLexer("is_true count_fn endwhile", "is_true, count_fn, endwhile")

def test_119():
    # Shadowing keywords: Keyword wrapped completely inside the identifier
    TestLexer.checkLexer("shifted mutating submatch", "shifted, mutating, submatch")

def test_120():
    # Identifiers: Sequence of diverse valid distinct formatting styles
    TestLexer.checkLexer("a_1 _b_2 c3_ d4", "a_1, _b_2, c3_, d4")

def test_121():
    # Unsigned integers: Single digit
    TestLexer.checkLexer("0 7 9", "0, 7, 9")

def test_122():
    # Unsigned integers: Multi-digit
    TestLexer.checkLexer("42 100 9999", "42, 100, 9999")

def test_123():
    # Signed integers: Explicit positive sign (+)
    TestLexer.checkLexer("+5 +88", "+, 5, +, 88")

def test_124():
    # Signed integers: Negative sign (-)
    TestLexer.checkLexer("-9 -765", "-, 9, -, 765")

def test_125():
    # Unsigned float literals: Basic fractions
    TestLexer.checkLexer("3.14159 0.005", "3.14159, 0.005")

def test_126():
    # Signed float literals: Positive (+)
    TestLexer.checkLexer("+1.25 +0.0", "+, 1.25, +, 0.0")

def test_127():
    # Signed float literals: Negative (-)
    TestLexer.checkLexer("-0.75 -99.99", "-, 0.75, -, 99.99")

def test_128():
    # Scientific notation: lower 'e' with positive exponent
    TestLexer.checkLexer("1e10 2.5e3", "1e10, 2.5e3")

def test_129():
    # Scientific notation: upper 'E' with positive exponent
    TestLexer.checkLexer("4E5 9.99E2", "4E5, 9.99E2")

def test_130():
    # Scientific notation: lower 'e' with negative exponent
    TestLexer.checkLexer("5e-3 0.1e-5", "5e-3, 0.1e-5")

def test_131():
    # Scientific notation: upper 'E' with negative exponent
    TestLexer.checkLexer("6E-4 12.3E-2", "6E-4, 12.3E-2")

def test_132():
    # Scientific notation: explicit plus sign in exponent
    TestLexer.checkLexer("1e+5 3.14E+2", "1e+5, 3.14E+2")

def test_133():
    # Complex signed float with scientific notation
    TestLexer.checkLexer("-5.2e-3 +1.0e+4", "-, 5.2e-3, +, 1.0e+4")

def test_134():
    # Zero representations: Integer variations
    TestLexer.checkLexer("0 000 +0 -0", "0, 000, +, 0, -, 0")

def test_135():
    # Zero representations: Float variations
    TestLexer.checkLexer("0.0 -0.0 0e0 0.0e-0", "0.0, -, 0.0, 0e0, 0.0e-0")

def test_136():
    # Boundary integers (large digit sequences)
    TestLexer.checkLexer("2147483647 9223372036854775807", "2147483647, 9223372036854775807")

def test_137():
    # Continuous valid number sequence inside expression lookalike
    TestLexer.checkLexer("10 + 20 - 30", "10, +, 20, -, 30")

def test_138():
    # Floats with multiple trailing zeros in decimal part
    TestLexer.checkLexer("5.0000 123.450", "5.0000, 123.450")

def test_139():
    # Scientific notation with zero base or zero exponent
    TestLexer.checkLexer("0e10 5e0 0.0E0", "0e10, 5e0, 0.0E0")

def test_140():
    # Large sequence of mixed valid numbers
    TestLexer.checkLexer("123 +45.6 -7e8 0.0", "123, +, 45.6, -, 7e8, 0.0")

def test_141():
    TestLexer.checkLexer("1.2.3", "1.2, ., 3")

def test_142():
    TestLexer.checkLexer("0..5", "0, .., 5")

def test_143():
    TestLexer.checkLexer("2e", "2, e")

def test_144():
    TestLexer.checkLexer("5.5E-", "5.5, E, -")

def test_145():
    TestLexer.checkLexer("10e+", "10, e, +")

def test_146():
    TestLexer.checkLexer("123a45", "123, a45")  # a45 là ID hợp lệ!

def test_147():
    TestLexer.checkLexer("2e3e4", "2e3, e4")

def test_148():
    TestLexer.checkLexer("1e2.5", "1e2, ., 5")

def test_149():
    TestLexer.checkLexer("5.", "5, .")
    
def test_150():
    TestLexer.checkLexer("4.2e+", "4.2, e, +")

def test_151():
    # Valid Strings: Empty string literal (Bỏ nháy kép -> chuỗi rỗng)
    TestLexer.checkLexer(r'""', r'')

def test_152():
    # Valid Strings: Basic string with normal ASCII characters
    TestLexer.checkLexer(r'"hello"', r'hello')

def test_153():
    # Valid Strings: String containing spaces and common punctuations
    TestLexer.checkLexer(r'"hello, world!"', r'hello, world!')

def test_154():
    # Valid Strings: Escape sequence for newline (\n)
    # Sau giải mã, \n biến thành ký tự xuống dòng thực tế
    TestLexer.checkLexer(r'"line1\nline2"', "line1\nline2")

def test_155():
    # Valid Strings: Escape sequence for horizontal tab (\t)
    # Sau giải mã, \t biến thành ký tự tab thực tế
    TestLexer.checkLexer(r'"column1\tcolumn2"', "column1\tcolumn2")

def test_156():
    # Valid Strings: Escape sequence for double quote (\")
    # Sau giải mã, \" biến thành dấu nháy kép đơn độc '"'
    TestLexer.checkLexer(r'"she said \"hi\""', 'she said "hi"')

def test_157():
    # Valid Strings: Escape sequence for backslash (\\)
    # Sau giải mã, \\ biến thành một dấu backslash đơn '\'
    TestLexer.checkLexer(r'"path\\to\\file"', 'path\\to\\file')

def test_158():
    # Valid Strings: Mixing multiple valid escape sequences
    # Tổng hợp giải mã: \" -> ", \t -> ký tự tab, \\ -> \
    TestLexer.checkLexer(r'"Point \"A\"\tValue\\Path"', 'Point "A"\tValue\\Path')

def test_159():
    # Valid Strings: Consecutive distinct string literals
    TestLexer.checkLexer(r'"str1" "str2"', r'str1, str2')

def test_160():
    # Valid Strings: Keywords inside string literal treated as plain text
    TestLexer.checkLexer(r'"let mut fn while"', r'let mut fn while')

def test_161():
    # Unclosed String: Missing closing quote at the end of the line
    TestLexer.checkLexer(r'"this is unclosed', r'Unclosed String: this is unclosed')

def test_162():
    # Unclosed String: Chuỗi kết thúc đột ngột cuối dòng khi đang gán giá trị cho biến
    TestLexer.checkLexer('let x = "unclosed_variable', r'let, x, =, Unclosed String: unclosed_variable')

def test_163():
    # Illegal Escape: \a is not supported in MiniRust
    TestLexer.checkLexer(r'"invalid \a escape"', r'Illegal Escape In String: invalid \a')

def test_164():
    # Illegal Escape: \x is not supported in MiniRust
    TestLexer.checkLexer(r'"invalid \x escape"', r'Illegal Escape In String: invalid \x')

def test_165():
    # Illegal Escape: Backslash followed by a space character
    TestLexer.checkLexer(r'"invalid \ escape"', r'Illegal Escape In String: invalid \ ')

def test_166():
    # Unclosed String: A single isolated double quote character
    TestLexer.checkLexer(r'"', r'Unclosed String: ')

def test_167():
    # Unclosed String: Closing quote is escaped, so it reaches EOF without a real closure
    TestLexer.checkLexer(r'"escaped quote at end\"', r'Unclosed String: escaped quote at end\"')

def test_168():
    # Illegal Escape: Triggers at the first illegal sequence encountered
    TestLexer.checkLexer(r'"triple \\\a"', r'Illegal Escape In String: triple \\\a')

def test_169():
    # Unclosed String: Appears right after a valid token sequence
    TestLexer.checkLexer(r'let x = "bad string', r'let, x, =, Unclosed String: bad string')

def test_170():
    # Illegal Escape: Appears at the very beginning of the string literal
    TestLexer.checkLexer(r'"\y error"', r'Illegal Escape In String: \y')

def test_171():
    # Illegal Escape: Backslash followed by a numeric digit (\1)
    TestLexer.checkLexer(r'"error \1"', r'Illegal Escape In String: error \1')

def test_172():
    # Unclosed String: Contains valid escape sequences before failing at EOF
    TestLexer.checkLexer(r'"valid \n and \t but unclosed ', r'Unclosed String: valid \n and \t but unclosed ')

def test_173():
    # Illegal Escape: Uppercase letter inside escape sequence (\N)
    TestLexer.checkLexer(r'"wrong \N sequence"', r'Illegal Escape In String: wrong \N')

def test_174():
    # Unclosed String: Inside brackets
    TestLexer.checkLexer(r'[ "incomplete string ]', r'[, Unclosed String: incomplete string ]')

def test_175():
    # Complex String Error: Gặp lỗi Illegal escape (\z) trước khi chuỗi bị unclosed
    TestLexer.checkLexer(r'"\z and forgotten quote', r'Illegal Escape In String: \z')

def test_176():
    # Error Tokens: Unrecognized isolated character @
    TestLexer.checkLexer("@", "Error Token @")

def test_177():
    # Error Tokens: Unrecognized isolated character #
    TestLexer.checkLexer("#", "Error Token #")

def test_178():
    # Error Tokens: Unrecognized isolated character $
    TestLexer.checkLexer("$", "Error Token $")

def test_179():
    # Error Tokens: Unrecognized isolated character ` (backtick)
    TestLexer.checkLexer("`", "Error Token `")

def test_180():
    # Error Tokens: Unrecognized character ? appearing inside a code sequence
    # Bộ Lexer sẽ quét 'let', 'x', '=', rồi dừng lại báo lỗi ngay tại '?'
    TestLexer.checkLexer("let x = ?", "let, x, =, Error Token ?")

def test_181():
    # Operators: Arithmetic operations (+, -, *, /, %)
    TestLexer.checkLexer("+ - * / %", "+, -, *, /, %")

def test_182():
    # Operators: Comparison operations (==, !=, <, <=, >, >=)
    TestLexer.checkLexer("== != < <= > >=", "==, !=, <, <=, >, >=")

def test_183():
    # Operators: Logical boolean operations and basic assignment
    TestLexer.checkLexer("&& || ! =", "&&, ||, !, =")

def test_184():
    # Punctuators: Range (..) and Arrow (->) symbols
    TestLexer.checkLexer(".. ->", ".., ->")

def test_185():
    # Punctuators: Structural delimiters and enclosures
    TestLexer.checkLexer("; , : .", ";, ,, :, .")

def test_186():
    # Punctuators: Parentheses, braces, and square brackets
    TestLexer.checkLexer("() {} []", "(, ), {, }, [, ]")

def test_187():
    # Maximal Munch: '==' should not be split into '=' and '='
    TestLexer.checkLexer("==", "==")

def test_188():
    # Maximal Munch: '<=' should stay together, not split into '<' and '='
    TestLexer.checkLexer("<=", "<=")

def test_189():
    # Maximal Munch Split: '->-' should split into '->' and '-'
    TestLexer.checkLexer("->-", "->, -")

def test_190():
    # Maximal Munch Split: '...=' should split into '..' and '.' and '='
    TestLexer.checkLexer("...=", ".., ., =")

def test_191():
    # Comments: Single-line comment at the end of a line (should be ignored entirely)
    TestLexer.checkLexer("let x = 5; // this is a comment", "let, x, =, 5, ;")

def test_192():
    # Comments: Multiple consecutive single-line comments
    TestLexer.checkLexer("// line 1\n// line 2\nfn main", "fn, main")

def test_193():
    # Comments: Block comment on a single line separating tokens
    TestLexer.checkLexer("let /* middle comment */ y = 10;", "let, y, =, 10, ;")

def test_194():
    # Comments: Multi-line block comment covering several lines
    TestLexer.checkLexer("/* line 1\n line 2\n line 3 */ mut void", "mut, void")

def test_195():
    # Comments: Block comments do not nest (Maximal munch terminates at first */)
    # Phần 'nested */' phía sau sẽ bị xem là các token rời rạc: ID(nested), *, /
    TestLexer.checkLexer("/* outer /* inner */ nested */", "nested, *, /")

def test_196():
    # Unclosed block comment at EOF splits into OPERATOR(/), OPERATOR(*), and ID(forgotten...)
    TestLexer.checkLexer("fn main() /* forgotten", "fn, main, (, ), /, *, forgotten")

def test_197():
    # Whitespaces: Handling horizontal spaces (spaces and tabs mixing)
    TestLexer.checkLexer("let \t\t mut    x   ;", "let, mut, x, ;")

def test_198():
    # Whitespaces: Handling vertical spaces (multiple newlines separating tokens)
    TestLexer.checkLexer("if\n\n\nelse\n\nswitch", "if, else, switch")

def test_199():
    # Mixed: Complex layout combining dense code, comments, tabs, and newlines
    TestLexer.checkLexer("  \t // initialization\n\tlet x = 1; /* break */ \n", "let, x, =, 1, ;")

def test_200():
    # Valid statement followed by unclosed comment splits into OPERATOR(/), OPERATOR(*), and ID(unclosed)
    TestLexer.checkLexer("x = 5; /* unclosed", "x, =, 5, ;, /, *, unclosed")