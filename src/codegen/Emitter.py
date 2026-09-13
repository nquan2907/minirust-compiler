"""
Emitter class for MiniRust JVM code generation.
High-level code emission with type conversion, constant loading, variable operations.

NOTE ON ASSUMPTIONS: JasminCode.py was not shared, so the following JasminCode
method names are ASSUMED to exist (based on naming convention of the ones already
used in the given skeleton). If your JasminCode.py uses different names, rename
the calls below accordingly:
    emitNEWARRAY(type_str), emitANEWARRAY(class_name)
    emitIALOAD/emitFALOAD/emitAALOAD, emitIASTORE/emitFASTORE/emitAASTORE
    emitARRAYLENGTH
    emitATTRIBUTE(name, descriptor)   -> ".field public <name> <descriptor>"
    emitINVOKEVIRTUAL(lexeme, descriptor)
"""

import os
from typing import List, Optional, Union
from codegen.JasminCode import JasminCode
from codegen.Error import IllegalOperandException
from utils.AST import (
    IntType, FloatType, BoolType, StringType, VoidType, StructType,
    IntLiteral, FloatLiteral, StringLiteral
)
from codegen.Utils import FunctionType, StructType as CodeGenStructType

# Helper functions for MiniRust type checking
def is_int_type(in_type):
    """Check if type is int."""
    return type(in_type) is IntType

def is_float_type(in_type):
    """Check if type is float."""
    return type(in_type) is FloatType

def is_bool_type(in_type):
    """Check if type is bool. (JVM represents bool as int 0/1.)"""
    return type(in_type) is BoolType

def is_string_type(in_type):
    """Check if type is string."""
    return type(in_type) is StringType

def is_void_type(in_type):
    """Check if type is void."""
    return type(in_type) is VoidType

def is_struct_type(in_type):
    """Check if type is struct."""
    return type(in_type) is StructType or type(in_type) is CodeGenStructType


class Emitter:
    """
    Emitter class to generate JVM bytecode instructions for MiniRust.

    Attributes:
        filename (str): Name of the output file
        buff (List[str]): Buffer to store generated code
        jvm (JasminCode): JasminCode instance for JVM instruction generation
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "runtime", filename
        )
        self.buff: List[str] = []
        self.jvm = JasminCode()

    def get_jvm_type(self, in_type) -> str:
        """
        Convert MiniRust AST type to JVM type descriptor.
        """
        if type(in_type).__name__ == 'StringArrayType' or (hasattr(in_type, '__class__') and 'StringArray' in str(type(in_type))):
            return "[Ljava/lang/String;"  # String[] in JVM (main method args)

        if is_int_type(in_type):
            return "I"
        elif is_float_type(in_type):
            return "F"
        elif is_bool_type(in_type):
            return "Z"
        elif is_string_type(in_type):
            return "Ljava/lang/String;"
        elif is_void_type(in_type):
            return "V"
        elif is_struct_type(in_type):
            struct_name = in_type.name if hasattr(in_type, 'name') else in_type.struct_name
            struct_name = struct_name if type(struct_name) is str else struct_name.name
            return "L" + struct_name + ";"
        elif type(in_type).__name__ == 'ArrayType':
            return "[" + self.get_jvm_type(in_type.element_type)
        elif type(in_type) is FunctionType:
            return (
                "("
                + "".join(list(map(lambda x: self.get_jvm_type(x), in_type.param_types)))
                + ")"
                + self.get_jvm_type(in_type.return_type)
            )
        else:
            raise IllegalOperandException(f"Unknown type: {type(in_type)}")

    def emit_push_null(self, frame) -> str:
        frame.push()
        return self.jvm.emitPUSHNULL()

    def emit_push_iconst(self, in_: Union[int, str], frame) -> str:
        frame.push()
        if type(in_) is int:
            i = in_
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(str(i))
        elif type(in_) is str:
            if in_ == "true":
                return self.emit_push_iconst(1, frame)
            elif in_ == "false":
                return self.emit_push_iconst(0, frame)
            else:
                return self.emit_push_iconst(int(in_), frame)

    def emit_push_fconst(self, in_: str, frame) -> str:
        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0000" or rst == "1.0000" or rst == "2.0000":
            return self.jvm.emitFCONST(rst[:3])
        else:
            return self.jvm.emitLDC(rst)

    def emit_push_const(self, in_: str, typ, frame) -> str:
        if is_int_type(typ) or is_bool_type(typ):
            return self.emit_push_iconst(in_, frame)
        elif is_string_type(typ):
            frame.push()
            escaped = in_.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')
            return self.jvm.emitLDC(f'"{escaped}"')
        else:
            raise IllegalOperandException(f"Unsupported constant type: {type(typ)}")

    def emit_var(self, in_: int, var_name: str, in_type, from_label: int, to_label: int) -> str:
        return self.jvm.emitVAR(in_, var_name, self.get_jvm_type(in_type), from_label, to_label)

    def emit_read_var(self, name: str, in_type, index: int, frame) -> str:
        frame.push()
        if is_int_type(in_type) or is_bool_type(in_type):
            return self.jvm.emitILOAD(index)
        elif is_float_type(in_type):
            return self.jvm.emitFLOAD(index)
        elif is_string_type(in_type) or is_struct_type(in_type) or type(in_type).__name__ == 'ArrayType':
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(f"Unsupported variable type: {type(in_type)}")

    def emit_write_var(self, name: str, in_type, index: int, frame) -> str:
        frame.pop()
        if is_int_type(in_type) or is_bool_type(in_type):
            return self.jvm.emitISTORE(index)
        elif is_float_type(in_type):
            return self.jvm.emitFSTORE(index)
        elif is_string_type(in_type) or is_struct_type(in_type) or type(in_type).__name__ == 'ArrayType':
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(f"Unsupported variable type: {type(in_type)}")

    def emit_get_field(self, lexeme: str, in_, frame) -> str:
        frame.pop()
        frame.push()
        return self.jvm.emitGETFIELD(lexeme, self.get_jvm_type(in_))

    def emit_put_field(self, lexeme: str, in_, frame) -> str:
        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.get_jvm_type(in_))

    def emit_invoke_static(self, lexeme: str, in_, frame) -> str:
        typ = in_
        list(map(lambda x: frame.pop(), typ.param_types))
        if not is_void_type(typ.return_type):
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.get_jvm_type(in_))

    def emit_neg_op(self, in_, frame) -> str:
        if is_int_type(in_):
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emit_add_op(self, lexeme: str, in_, frame) -> str:
        frame.pop()
        if lexeme == "+":
            if is_int_type(in_):
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if is_int_type(in_):
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    def emit_mul_op(self, lexeme: str, in_, frame) -> str:
        frame.pop()
        if lexeme == "*":
            if is_int_type(in_):
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if is_int_type(in_):
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emit_mod(self, frame) -> str:
        frame.pop()
        return self.jvm.emitIREM()

    def emit_iinc(self, index: int, amount: int, frame) -> str:
        return self.jvm.emitIINC(index, amount)

    def emit_and_op(self, frame) -> str:
        frame.pop()
        return self.jvm.emitIAND()

    def emit_or_op(self, frame) -> str:
        frame.pop()
        return self.jvm.emitIOR()

    def emit_re_op(self, op: str, in_, frame) -> str:
        """
        Emit relational operation (returns int: 0 for false, non-zero for true).
        Numeric/bool types use IF_ICMPxx / FCMPL; strings use String.equals via
        INVOKEVIRTUAL (ASSUMPTION: JasminCode.emitINVOKEVIRTUAL exists).
        """
        if is_string_type(in_):
            frame.pop()
            frame.pop()
            code = self.jvm.emitINVOKEVIRTUAL(
                "java/lang/String/equals", "(Ljava/lang/Object;)Z"
            )
            frame.push()
            if op == "!=":
                label_f = frame.get_new_label()
                label_o = frame.get_new_label()
                frame.pop()
                code += self.jvm.emitIFNE(label_f)
                code += self.emit_push_iconst(1, frame)
                code += self.emit_goto(label_o, frame)
                code += self.emit_label(label_f, frame)
                code += self.emit_push_iconst(0, frame)
                code += self.emit_label(label_o, frame)
            return code

        result = list()
        label_f = frame.get_new_label()
        label_o = frame.get_new_label()

        frame.pop()
        frame.pop()
        if is_int_type(in_) or is_bool_type(in_):
            if op == ">":
                result.append(self.jvm.emitIFICMPLE(label_f))
            elif op == ">=":
                result.append(self.jvm.emitIFICMPLT(label_f))
            elif op == "<":
                result.append(self.jvm.emitIFICMPGE(label_f))
            elif op == "<=":
                result.append(self.jvm.emitIFICMPGT(label_f))
            elif op == "!=":
                result.append(self.jvm.emitIFICMPEQ(label_f))
            else:  # op == "=="
                result.append(self.jvm.emitIFICMPNE(label_f))
        else:  # float
            result.append(self.jvm.emitFCMPL())
            if op == ">":
                result.append(self.jvm.emitIFLE(label_f))
            elif op == ">=":
                result.append(self.jvm.emitIFLT(label_f))
            elif op == "<":
                result.append(self.jvm.emitIFGE(label_f))
            elif op == "<=":
                result.append(self.jvm.emitIFGT(label_f))
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(label_f))
            else:  # op == "=="
                result.append(self.jvm.emitIFNE(label_f))

        result.append(self.emit_push_iconst(1, frame))
        result.append(self.emit_goto(label_o, frame))
        result.append(self.emit_label(label_f, frame))
        result.append(self.emit_push_iconst(0, frame))
        result.append(self.emit_label(label_o, frame))
        return "".join(result)

    def emit_method(self, lexeme: str, in_type, is_static: bool) -> str:
        return self.jvm.emitMETHOD(lexeme, self.get_jvm_type(in_type), True)

    def emit_end_method(self, frame) -> str:
        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.get_max_op_stack_size()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.get_max_index()))
        buffer.append(self.jvm.emitENDMETHOD())
        return "".join(buffer)

    def emit_if_true(self, label: int, frame) -> str:
        frame.pop()
        return self.jvm.emitIFGT(label)

    def emit_if_false(self, label: int, frame) -> str:
        frame.pop()
        return self.jvm.emitIFLE(label)

    def emit_dup(self, frame) -> str:
        frame.push()
        return self.jvm.emitDUP()

    def emit_dup_x1(self, frame) -> str:
        frame.push()
        return self.jvm.emitDUPX1()

    def emit_dup_x2(self, frame) -> str:
        frame.push()
        return self.jvm.emitDUPX2()

    def emit_pop(self, frame) -> str:
        frame.pop()
        return self.jvm.emitPOP()

    def emit_i2f(self, frame) -> str:
        return self.jvm.emitI2F()

    def emit_return(self, in_, frame) -> str:
        if is_int_type(in_) or is_bool_type(in_):
            frame.pop()
            return self.jvm.emitIRETURN()
        elif is_float_type(in_):
            frame.pop()
            return self.jvm.emitFRETURN()
        elif is_void_type(in_):
            return self.jvm.emitRETURN()
        elif is_string_type(in_) or is_struct_type(in_) or type(in_).__name__ == 'ArrayType':
            frame.pop()
            return self.jvm.emitARETURN()
        else:
            raise IllegalOperandException(f"Unsupported return type: {type(in_)}")

    def emit_new(self, lexeme: str, frame) -> str:
        frame.push()
        return self.jvm.emitNEW(lexeme)

    def emit_new_instance(self, class_name: str, frame) -> str:
        code = ""
        frame.push()
        code += self.jvm.emitNEW(class_name)
        frame.push()
        code += self.jvm.emitDUP()
        frame.pop()
        code += self.jvm.emitINVOKESPECIAL(class_name + "/<init>", "()V")
        return code

    def emit_label(self, label: int, frame) -> str:
        return self.jvm.emitLABEL(label)

    def emit_goto(self, label: int, frame) -> str:
        return self.jvm.emitGOTO(label)

    # ------------------------------------------------------------------
    # Array support (ASSUMES JasminCode has these instruction emitters)
    # ------------------------------------------------------------------

    def emit_new_array(self, elem_type, frame) -> str:
        """Pops size, pushes new array reference."""
        frame.pop()
        frame.push()
        if is_int_type(elem_type) or is_bool_type(elem_type):
            return self.jvm.emitNEWARRAY("int")
        elif is_float_type(elem_type):
            return self.jvm.emitNEWARRAY("float")
        elif is_string_type(elem_type):
            return self.jvm.emitANEWARRAY("java/lang/String")
        elif is_struct_type(elem_type):
            struct_name = elem_type.name if hasattr(elem_type, 'name') else elem_type.struct_name
            struct_name = struct_name if type(struct_name) is str else struct_name.name
            return self.jvm.emitANEWARRAY(struct_name)
        else:
            raise IllegalOperandException(f"Unsupported array element type: {type(elem_type)}")

    def emit_aload(self, elem_type, frame) -> str:
        """Pops arrayref, index; pushes the element value."""
        frame.pop()
        frame.pop()
        frame.push()
        if is_int_type(elem_type) or is_bool_type(elem_type):
            return self.jvm.emitIALOAD()
        elif is_float_type(elem_type):
            return self.jvm.emitFALOAD()
        else:
            return self.jvm.emitAALOAD()

    def emit_astore(self, elem_type, frame) -> str:
        """Pops arrayref, index, value."""
        frame.pop()
        frame.pop()
        frame.pop()
        if is_int_type(elem_type) or is_bool_type(elem_type):
            return self.jvm.emitIASTORE()
        elif is_float_type(elem_type):
            return self.jvm.emitFASTORE()
        else:
            return self.jvm.emitAASTORE()

    def emit_array_length(self, frame) -> str:
        frame.pop()
        frame.push()
        # JasminCode has no emitARRAYLENGTH helper; emit the raw instruction directly.
        return "\tarraylength\n"

    # ------------------------------------------------------------------
    # Struct class file support
    # ------------------------------------------------------------------

    def emit_attribute(self, name: str, in_type) -> str:
        """
        Emits a public field declaration for a struct class.
        JasminCode has no emitATTRIBUTE/field helper, so we emit the raw
        Jasmin `.field` directive directly: `.field public <name> <descriptor>`
        """
        return f".field public {name} {self.get_jvm_type(in_type)}\n"

    def emit_default_constructor(self) -> str:
        """Emits a no-arg constructor calling super()."""
        result = list()
        result.append(self.jvm.emitMETHOD("<init>", "()V", False))
        result.append(self.jvm.emitLIMITSTACK(1))
        result.append(self.jvm.emitLIMITLOCAL(1))
        result.append(self.jvm.emitALOAD(0))
        result.append(self.jvm.emitINVOKESPECIAL("java/lang/Object/<init>", "()V"))
        result.append(self.jvm.emitRETURN())
        result.append(self.jvm.emitENDMETHOD())
        return "".join(result)

    def emit_prolog(self, name: str) -> str:
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/lang/Object"))
        return "".join(result)

    def emit_epilog(self) -> None:
        file = open(self.filepath, "w")
        tmp = "".join(self.buff)
        file.write(tmp)
        file.close()

    def print_out(self, in_: str) -> None:
        self.buff.append(in_)

    def clear_buff(self) -> None:
        self.buff.clear()