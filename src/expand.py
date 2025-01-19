def expand_spaces(orig: set) -> set:

    expanded_set = set()
    
    for line in orig:
        # Convert to lowercase
        line_lower = line.lower()
        
        # Add original space-separated version
        expanded_set.add(line_lower)
        
        # Only process further if the line contains spaces
        if ' ' in line_lower:
            words = line_lower.split()
            # Add underscore-joined version
            expanded_set.add('_'.join(words))
            # Add version with no spaces
            expanded_set.add(''.join(words))
    
    return expanded_set