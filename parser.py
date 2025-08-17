import ast
import inspect

import app

source = inspect.getsource(app)
tree = ast.parse(source)

endpoints = []

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        # Get function's source code
        func_source = inspect.getsource(app.__dict__[node.name])

        for deco in node.decorator_list:
            if isinstance(deco, ast.Call) and getattr(deco.func, "attr", "") == "route":
                path = deco.args[0].s
                methods = []
                for kw in deco.keywords:
                    if kw.arg == "methods":
                        methods = [m.s for m in kw.value.elts]

                endpoints.append(
                    {
                        "func": node.name,
                        "path": path,
                        "methods": methods or ["GET"],
                        "code": func_source,  # Store the entire function code
                    }
                )

for e in endpoints:
    print(f"{e['methods']} {e['path']} -> {e['func']}()")
    print("Function Code:")
    print(e["code"])  # Display the function code
    print("-" * 50)
