# eval

import re
from tree_node import TreeNode
import secrets


class Eval:

    symbols = {}
    func_symbols = {}

    operators = {
        "+": lambda args, ast: args[0] + args[1],
        "-": lambda args, ast: args[0] - args[1],
        "*": lambda args, ast: args[0] * args[1],
        "block": lambda args, ast: args,
        "instruction": lambda args, ast: args,
        "assign": lambda args, ast: Eval._attrib(args,ast),
        "print": lambda args, ast: Eval._print(args),
        "for_loop": lambda args, ast: Eval._for_loop(args,ast),
        "var_lookup": lambda args, ast: Eval._var_lookup(args,ast),
        "return": lambda args, ast: args,
        "func": lambda args, ast: Eval._create_func(args),
        "param": lambda args, ast: args,
        "arguments": lambda args, ast: args,
        "func_call": lambda args, ast:Eval._call_func(args,ast)
    }

    @staticmethod
    def _call_func(args,ast):
        func_name = args[0]
        scope = func_name+"___"+secrets.token_hex(nbytes=16)
        ast.scope[:0]=[scope]
        if func_name in Eval.func_symbols:
            for idx,argument in enumerate(Eval.func_symbols[func_name]['params_list']):
                Eval._attrib([argument,args[1][idx]], ast)
            func_ast: TreeNode = Eval.func_symbols[func_name]["ast"]
            func_ast.scope[:0]=[scope]
            Eval._eval_operator(func_ast)
            

    @staticmethod
    def _create_func(args):
        value = args[1]
        Eval.func_symbols[args[0]]={
            "params_list":args[1].args,
            "ast":args[2]
        }

    @staticmethod
    def _var_lookup(args,ast):
        scope = Eval._get_scope(ast.scope)
        var = args[0]
        for scope in ast.scope:
            if var in Eval.symbols[scope]:
                return Eval.symbols[scope][var]
        raise Exception(f"error: '{var}' undeclared (first use in this function)")
    
    @staticmethod
    def _print(args: TreeNode):
        print(args[0])
        return args

    @staticmethod
    def _attrib(args,ast): 
        value = args[1]
        scope = Eval._get_scope(ast.scope[0])
        if scope not in Eval.symbols:
            Eval.symbols[scope] = {}
        Eval.symbols[scope][args[0]] = value
        return f'{args[0]} = {args[1]}'
    
    def _for_loop(args,ast):
        scope = "_FOR___"+secrets.token_hex(nbytes=16)
        cycle = args[1]
        pattern = r'\[(\d+)\.\.(\d+)\]'
        matches = re.search(pattern, cycle)
        if matches:
            inicio = int(matches.group(1))
            fim = int(matches.group(2))
            #print(inicio, fim)
        else:
            raise Exception(f"error: range invalid syntax")
        ast = args[2]
        ast.scope[:0]=[scope]
        for i in range(inicio,fim):
            Eval._attrib([args[0],i],ast)
            Eval._eval_operator(ast)

    
    @staticmethod
    def evaluate(ast):
        if type(ast) is TreeNode:
            return Eval._eval_operator(ast)
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict: # { 'op': ... , 'args': ...}
            return Eval._eval_operator(ast)
        if type(ast) is str: 
            return ast
        print(ast)
        raise Exception(f"Unknown AST type")
        
    @staticmethod
    def _eval_operator(ast: TreeNode):
        
        op = ast.op
        if op == "for_loop":
            ast.args[2].scope=ast.scope
            return Eval.operators["for_loop"](ast.args,ast)
        if op == "func":
            return Eval.operators["func"](ast.args,ast)

        #args = [Eval.evaluate(a) for a in ast.args]
        args = []
        for a in ast.args:
            if type(a) is TreeNode:          
                a.scope[:0] = ast.scope
                a.scope = list(dict.fromkeys(ast.scope))
            args.append(Eval.evaluate(a))
        if op in Eval.operators:
            func = Eval.operators[op]
            return func(args,ast)
        else:
            raise Exception(f"{op} operation not found")

    
        raise Exception('Undefined AST')

    @staticmethod
    def _get_scope(scope):
        return scope if scope is not None else 'global'

