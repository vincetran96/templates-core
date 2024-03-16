> Namespaces are easy or not?

# Basic ideas
`simple_namespaces.py`
- The `dir` function
- The `locals` function
- The `globals` function
- How variables with the same name are used in different scopes

`modify_vars.py`
- Modify a list in-place from global scope

`import_modules.py`
- Modules that import from an upper dir must be imported and run in a top-level module (?)

# Mocking
- Namespaces and mocking for unittesting are discussed

# Best practices for namespaces:
- When a function modifies data outside the local scope, either with the global or nonlocal keyword or by directly modifying a mutable type in place, it’s a kind of side effect similar to when a function modifies one of its arguments. Widespread modification of global variables is generally considered unwise, not only in Python but also in other programming languages.
- All in all, modifying variables outside the local scope usually isn’t necessary. There’s almost always a better way, usually with function return values.
