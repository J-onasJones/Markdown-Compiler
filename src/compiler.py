import markdown, os

import file_fetch

def markdown_to_html(input, output=None, svelte=False):
    """
    Converts a Markdown file to HTML.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str, optional): The path to the output HTML file. If None, the HTML content is returned as a string.
        svelte (bool, optional): Whether to compile to Svelte components or not.

    Returns:
        str: The HTML content as a string (if output_file is None).
    """
    if os.path.isdir(input) and os.path.isdir(output):
        files = file_fetch.get_files_by_extension(input, '.md')
        print(files)

        for file in files:
            # for the output, take the output folder path and append the directories and file name
            nested_file = file.replace(input, '')
            output_file = output + nested_file.replace('.md', '.svelte') if svelte else output + nested_file.replace('.md', '.html')
            # create the folder
            try:
                os.makedirs(os.path.dirname(output_file.replace(output_file.split('/')[-1], "")))
            except FileExistsError:
                pass
            markdown_to_html(file, output_file, svelte)
        return
    output = output.replace('.md', '.svelte') if svelte else output.replace('.md', '.html')

    print("Converting " + input + " to " + output)


    with open(input, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_text)

    if output:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(html_content)
    else:
        return html_content

# Example usage:
# Convert a Markdown file to HTML and save it to an HTML file
# markdown_to_html('input.md', 'output.html')

# Or, convert a Markdown file to HTML and get the HTML content as a string
# html_content = markdown_to_html('input.md')
# print(html_content)