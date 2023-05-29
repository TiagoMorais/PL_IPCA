# eval

import re
from tree_node import TreeNode


class Eval:

    symbols = {}

    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "block": lambda args: args,
        "instruction": lambda args: args,
        "assign": lambda args: Eval._attrib(args),
        "print": lambda args: Eval._print(args),
        "for_loop": lambda args: Eval._for_loop(args),
        "var_lookup": lambda args: Eval._var_lookup(args),
    }

    @staticmethod
    def _var_lookup(args):
        var = args[0]
        if var in Eval.symbols:
            return Eval.symbols[var]
        raise Exception(f"error: '{var}' undeclared (first use in this function)")
    

    @staticmethod
    def _print(args: TreeNode):
        print(args[0])
        return args

    @staticmethod
    def _attrib(args): # A:=10   {'op':'atr'  args: [ "A", 10 ]} 
        value = args[1]
        Eval.symbols[args[0]] = value
        return f'{args[0]} = {args[1]}'
    
    def _for_loop(args):
        print(args)
        cycle = args.args[1]
        pattern = r'\[(\d+)\.\.(\d+)\]'
        matches = re.search(pattern, cycle)
        if matches:
            inicio = int(matches.group(1))
            fim = int(matches.group(2))
            #print(inicio, fim)
        else:
            raise Exception(f"error: range invalid syntax")
        
        for i in range(inicio,fim):
            Eval._attrib([args.args[0],i])
            Eval._eval_operator(args.args[2])

    
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
        raise Exception(f"Unknown AST type")
        
    @staticmethod
    def _eval_operator(ast: TreeNode):
        
        op = ast.op
            
        args = [Eval.evaluate(a) for a in ast.args]
       
        if op in Eval.operators:
            func = Eval.operators[op]
            if op is "for_loop":
                return func(ast)
            else:    
                
                return func(args)
        else:
            raise Exception(f"{op} operation not found")
        
        
        # if 'op' in ast:
        #     op = ast["op"]
        #     args = [Eval.evaluate(a) for a in ast['args']]
        #     if op in Eval.operators:
        #         func = Eval.operators[op]
        #         return func(args)
        #     else:
        #         raise Exception(f"Unknown operator {op}")
            
        # if 'var' in ast:
        #     varid = ast["var"]
        #     if varid in Eval.symbols:
        #         return Eval.symbols[varid]
        #     raise Exception(f"error: '{varid}' undeclared (first use in this function)")
    
        raise Exception('Undefined AST')

