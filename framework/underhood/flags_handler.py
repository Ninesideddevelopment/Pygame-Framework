
def return_flags(flags: str) -> list[str]:
    """
    Returns a list of flags from a string.
    
    Args:
        flags (str): A string containing flags separated by '|'.
    
    Returns:
        list[str]: A list of flags.
    """
    return [flag.strip() for flag in flags.split('|') if flag.strip()] if flags else []