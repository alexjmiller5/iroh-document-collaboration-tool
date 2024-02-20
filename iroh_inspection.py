import inspect
import iroh

def print_module_info(module):
    print(f"Inspecting module: {module.__name__}\n")

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            print(f"Class: {name}")
            print_class_info(obj)
        elif inspect.isfunction(obj):
            print(f"Function: {name}")
            print_function_info(obj)
        # You can add more conditions here for other types like methods, properties, etc.

def print_class_info(cls):
    print(f"  Docstring: {inspect.getdoc(cls)}")
    print("  Attributes and Methods:")
    for name, obj in inspect.getmembers(cls):
        if not name.startswith('_'):  # Skipping private attributes and methods
            if inspect.isfunction(obj) or inspect.ismethod(obj):
                print(f"    Method: {name}")
                print_function_info(obj, indent=6)
            else:
                print(f"    Attribute: {name}")
    # print()

def print_function_info(func, indent=4):
    signature = inspect.signature(func)
    docstring = inspect.getdoc(func)
    indent_str = ' ' * indent
    # print(f"{indent_str}Signature: {func.__name__}{signature}")
    if docstring:
        print(f"{indent_str}Docstring: {docstring.splitlines()[0]}")
    # print()

if __name__ == "__main__":
    print_module_info(iroh)
