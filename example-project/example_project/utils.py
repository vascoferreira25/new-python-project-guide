def greet(greeting: str, name: str) -> str:
    """Greet a name.

    This function returns a string with a greeting to a name.

    Args:
        greeting (str): the greeting.
        name (str): the name.

    Returns:
        str: the greeting and name concatenated.

     Examples:
        ```python
        # Run the function
        from . import utils
        greeting = utils.greet("Hello", "World")
        # returns "Hello, World!"
        ```
    """
    return f"{greeting}, {name}!"