import os
import zipfile
from PIL import Image
import os
from PIL import Image
import os
import zipfile
from PIL import Image

def compress_and_convert_images(directory, output_zip):
    with zipfile.ZipFile(output_zip, "w") as zipf:
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".jpeg"):
                filepath = os.path.join(directory, filename)
                
                # Open the image file
                image = Image.open(filepath)
                
                # Compress and convert to JPEG
                image = image.convert("RGB")
                image.save(filepath, "JPEG", optimize=True, quality=50)
                
                # Add the modified image to the ZIP archive
                zipf.write(filepath, arcname=os.path.basename(filepath))
                
                print(f"Compressed and converted: {filepath}")
    
    print(f"All images compressed and converted. ZIP archive created: {output_zip}")

# Example usage:
directory = './compressed_paintings'
output_zip = './compressed_paintings.zip'
output_image_format = 'JPEG'
compress_and_convert_images(directory, output_zip)

