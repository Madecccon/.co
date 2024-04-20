from flask import Flask, render_template
import os

app = Flask(__name__)

def generate_gallery_items(directory):
    gallery_html = ""
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            gallery_html += f"""
            <div class="gallery-item">
                <img src="{os.path.join(directory, filename)}" alt="Gallery Image">
            </div>
            """
    with open("templates/gallery.html", "w") as file:
        file.write(gallery_html)

@app.route('/generate_gallery')
def generate_gallery():
    generate_gallery_items("gallery_images")
    return "Gallery generated successfully!"

if __name__ == '__main__':
    app.run(debug=True)
