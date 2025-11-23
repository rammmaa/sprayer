def change_name(s:str) -> str:
    return s.replace("&", r"\&").replace("-", " ").replace(r"\-", "-")
