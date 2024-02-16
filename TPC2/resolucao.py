import sys

# transforms markdown to html

# # -> <h1>, ## -> <h2>, ### -> <h3>, ** -> <b>, * -> <i>, ordered list -> <li>, unordered list -> <ul>, link -> <a>, image -> <img>

def markdown_to_html(markdown, template_page):
    # read the file through the stdin
    list = False

    for line in markdown:
        
        # Handle titles
        if line.startswith('#'):
            level = line.count('#')
            if level == 1:
                template_page += f"<h{level} class=\"bg-slate-200 py-4 text-3xl font-semibold text-white\" style=\"background-color: #6a0303;\">{line[level+1:]}</h{level}>"
            else:
                template_page += f"<h{level} class=\"pt-16 pb-6 text-3xl font-semibold\" style=\"color: #6a0303; text-align: center;\">{line[level+1:]}</h{level}>"


        # Handle bold
        elif '**' in line:
            parts = line.split('**')
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    template_page += part
                else:
                    template_page += f"<b>{part}</b>"

        # Handle italic
        elif '*' in line:
            parts = line.split('*')
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    template_page += part
                else:
                    template_page += f"<i>{part}</i>"

        # Handle unordered lists
        elif line.startswith('-') or line.startswith('+') or line.startswith('*'):

            if not list:
                template_page += "<ul>"
                list = True

            template_page += f"<li>{line[1:].strip()}</li>"
        
        # Handle ordered lists
        elif line[0].isdigit():

            if not list:
                template_page += "<ol>"
                list = True

            template_page += f"<li>{line[2:].strip()}</li>"

        # Handle images
        elif '!' in line and '[' in line and ']' in line and '(' in line and ')' in line:
            parts = line.split('[')
            for i, part in enumerate(parts):
                # do nothing with the first part
                if i % 2 == 0:
                    template_page += ""
                else:
                    text, link = part.split('](')
                    index = link.find(')')
                    link = link[:index]
                    
                    template_page += f"<img src='{link}' alt='{text}'>"

        # Handle links
        elif '[' in line and ']' in line and '(' in line and ')' in line:
            parts = line.split('[')
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    template_page += part
                else:
                    text, link = part.split('](')
                    index = link.find(')')
                    link = link[:index]

                    if index + 1 < len(link):
                        alt = link[index+1:]
                        link = link[:index]
                        template_page += f"<a href='{link}' alt='{alt}'>{text}</a>"
                    else:
                        template_page += f"<a href='{link}'>{text}</a>"
                                      

        else:
            template_page += line

        if list:
            template_page += "</ol>"
            list = False
    
    # create the html file
            
    with open('Markdown.html', 'w') as file:
        file.write(template_page)
        file.write("</body></html>")


def main():
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
    markdown_to_html(sys.stdin.readlines(), template_page)


if __name__ == "__main__":
    main()

        
