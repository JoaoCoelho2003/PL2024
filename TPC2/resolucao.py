import sys
import re

def markdown_to_html(markdown, template_page):

    # regular expressions for each markdown element
    header_regex = re.compile(r'^(#{1,6})\s(.*)$')
    bold_regex = re.compile(r'\*\*(.*?)\*\*')
    italic_regex = re.compile(r'\*(.*?)\*')
    ul_regex = re.compile(r'^[\*\-\+] (.*)$')
    ol_regex = re.compile(r'^\d+\.\s(.*)$')
    img_regex = re.compile(r'!\[(.*?)\]\((.*?)\)')
    link_regex = re.compile(r'\[(.*?)\]\((.*?)\)')

    list_open = False
    list_passed = False
    type_list = ""

    for line in markdown:

        # Handle headers
        match = header_regex.match(line)
        if match:
            level = len(match.group(1))
            if level == 1:
                template_page += f"<h{level} class=\"bg-slate-200 py-4 text-3xl font-semibold text-white\" style=\"background-color: #6a0303;\">{match.group(2)}</h{level}>\n"
                continue
            else:
                template_page += f"<h{level} class=\"pt-16 pb-6 text-3xl font-semibold\" style=\"color: #6a0303; text-align: center;\">{match.group(2)}</h{level}>\n"
                continue

        # Handle bold
        line = bold_regex.sub(r'<b>\1</b>', line)
        
        # Handle italic
        line = italic_regex.sub(r'<i>\1</i>', line)

        # Handle unordered lists
        match = ul_regex.match(line)
        if match:
            if not list_open:
                template_page += "<ul class=\"list-disc pl-4\">\n"
                list_open = True
                list_passed = True
                type_list = "ul"

            template_page += f"<li>{match.group(1)}</li>\n"
            continue
        else:
            list_passed = False

        # Handle ordered lists
        match = ol_regex.match(line)
        if match:
            if not list_open:
                template_page += "<ol class=\"list-decimal pl-4\">\n"
                list_open = True
                type_list = "ol"
                list_passed = True

            template_page += f"<li>{match.group(1)}</li>\n"
            continue
        else:
            list_passed = False

        # Handle images
        line = img_regex.sub(r'<img src="\2" alt="\1">', line)

        # Handle links
        line = link_regex.sub(r'<a href="\2" alt="\1">\1</a>', line)

        if not list_passed and list_open:
            template_page += f"</{type_list}>\n"
            list_open = False


        template_page += line

    # Write to HTML file
    with open('Markdown.html', 'w') as file:
        file.write(template_page)

def main():

    # Template for the HTML page
    template_page = """
    <!DOCTYPE html>
    <html lang="pt-pt">
    <head>
        <title>Markdown</title>
        <meta charset="UTF-8">
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
    """
    
    # Read the markdown from stdin
    markdown_to_html(sys.stdin.readlines(), template_page)

    # Close the HTML page
    template_page += "</body>\n</html>"

if __name__ == "__main__":
    main()