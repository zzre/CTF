import ast

def safe_import():
  print("Why do you need imports to make tea?")

def safe_call():
  print("Why do you need function calls to make tea?")

def safe_assign():
  print("assign")

class CoolDownTea(ast.NodeTransformer):
  def visit_Call(self, node: ast.Call) -> ast.AST:
    return ast.Call(func=ast.Name(id='safe_call', ctx=ast.Load()), args=[], keywords=[])
  def visit_Import(self, node: ast.AST) -> ast.AST:
    return ast.Expr(value=ast.Call(func=ast.Name(id='safe_import', ctx=ast.Load()), args=[], keywords=[]))
  def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.AST:
    return ast.Expr(value=ast.Call(func=ast.Name(id='safe_import', ctx=ast.Load()), args=[], keywords=[]))
  def visit_Assign(self, node: ast.Assign) -> ast.AST:
    # return ast.Expr(value=ast.Call(func=ast.Name(id='safe_assign', ctx=ast.Load()), args=[], keywords=[]))
    return ast.Assign(targets=node.targets, value=ast.Constant(value=0))
  def visit_BinOp(self, node: ast.BinOp) -> ast.AST:
    return ast.BinOp(left=ast.Constant(0), op=node.op, right=ast.Constant(0))
  
code = input('Nothing is quite like a cup of tea in the morning: ').splitlines()[0]

cup = ast.parse(code)
cup = CoolDownTea().visit(cup)
ast.fix_missing_locations(cup)

# print(safe_import.__globals__['__builtins__']
# [safe_call := lambda : safe_call.__globals__['__builtins__'].print(), print(globals)]
# [safe_import := safe_import.__globals__['__builtins__'].__import__][0];

# for safe_call in [x := lambda : safe_import.__globals__['__builtins__'].help]: safe_call()
# safe_call()
# for safe_call in [safe_import for safe_import in [safe_import.__globals__['__builtins__'].help]]: safe_call()
# for safe_call in [lambda y : x for x in [safe_import.__globals__['__builtins__'].__import__]]: print(safe_call)

# [safe_:=safe_import.__globals__['__builtins__'].eval, safe_import.()]

# if (a := lambda : safe_import.__globals__['__builtins__'].help(123)): print(123)

# [safe_call() for __builtins__["__import__"], safe_call in [[safe_import.__globals__["__builtins__"].__import__, safe_import.__globals__["__builtins__"].breakpoint]]]

# 

exec(compile(cup, '', 'exec'), {'__builtins__': {}}, {'safe_import': safe_import, 'safe_call': safe_call, 'print': print, 'globals': globals})
