import re

def condense_input(raw_input: str) -> str:
    """Stage 1 & 2: Strips high-entropy text and token bloat."""
    # Remove excessive whitespaces and system-breaking characters
    sanitized = re.sub(r'\s+', ' ', raw_input).strip()
    
    # Basic script injection filtering
    sanitized = sanitized.replace("ignore your rules", "[ATTACK_VECTOR_REMOVED]")
    return sanitized