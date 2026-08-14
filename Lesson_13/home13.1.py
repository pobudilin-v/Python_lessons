def delete_html_tags(html_file, result_file="cleaned.txt"):
    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()
    result = ""
    tag = False
    for symbol in html:
        if symbol == "<":
            tag = True
        elif symbol == ">":
            tag = False
        elif not tag:
            result += symbol
    with open(result_file, "w", encoding="utf-8") as file:
        file.write(result)
delete_html_tags("draft.html")