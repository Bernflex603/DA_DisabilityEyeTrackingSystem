
def pickOption(content: str) -> str:
    match content:
        case "1": return "Option1"
        case "2": return "Option2"
        case "3": return "Option3"
        case "4": return "Option4"
    return "defaultOption"