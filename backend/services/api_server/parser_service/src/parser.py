import re

def parse_drugs(raw_text: str) -> list[str]:
    # Simple regex-based drug name extractor
    pattern = r"[A-Z][a-z]+(?: [A-Z][a-z]+)*"
    return re.findall(pattern, raw_text)