from flask import Flask, render_template

app = Flask(__name__)

def generate_blog_post(title, content):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{title}</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <header>
        <h1>MADECC Construction Company Blog</h1>
      </header>
      <div class="container">
        <aside>
          <h2>Categories</h2>
          <ul>
            <li>Projects</li>
            <li>Industry News</li>
            <li>Tips & Tricks</li>
          </ul>
        </aside>
        <main>
          <article>
            <h2>{title}</h2>
            {content}
          </article>
        </main>
      </div>
      <footer>
        <p>&copy; 2024 MADECC Construction Company. All rights reserved.</p>
      </footer>
    </body>
    </html>
    """
    with open(f"templates/{title.replace(' ', '_').lower()}.html", "w") as file:
        file.write(html_template)

@app.route('/generate_blog_post')
def generate_blog_post_route():
    title = "10 Essential Construction Safety Tips"
    content = """
    <p>Construction sites can be hazardous places, but following safety guidelines can help prevent accidents. Here are 10 essential safety tips to keep in mind:</p>
    <ol>
      <li>Always wear appropriate personal protective equipment (PPE), including hard hats, safety glasses, and steel-toed boots.</li>
      <li>Inspect all tools and equipment before use to ensure they are in good working condition.</li>
      <li>Follow proper lifting techniques to avoid strain and injury.</li>
      <li>Use caution when working at heights and always use fall protection systems.</li>
      <li>Keep work areas clean and organized to prevent trips and falls.</li>
      <li>Stay alert and aware of your surroundings at all times.</li>
      <li>Communicate effectively with coworkers and supervisors.</li>
      <li>Follow all safety procedures and protocols established by the company.</li>
      <li>Report any hazards or unsafe conditions immediately.</li>
      <li>Participate in regular safety training sessions to stay up-to-date on best practices.</li>
    </ol>
    """
    generate_blog_post(title, content)
    return "Blog post generated successfully!"

if __name__ == '__main__':
    app.run(debug=True)
