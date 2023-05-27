import os

def get_image_paths(directory):
    image_paths = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_paths.append(os.path.join(root, file))
    
    return image_paths

def generate_html_snippet(image_paths):
    html = '<script>\n'
    html += 'var imageArray = [\n'
    
    for path in image_paths:
        html += f'  "{path}",\n'
    
    html += '];\n'
    html += '</script>'
    
    return html

# Specify the directory path
directory = './'

# Get the image paths
image_paths = get_image_paths(directory)

# Generate the HTML snippet
html_snippet = generate_html_snippet(image_paths)

# Output the HTML snippet
print(html_snippet)

