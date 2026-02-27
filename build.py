import os
import glob
import shutil

def generate_html():
    os.makedirs("dist", exist_ok=True)
    files = [os.path.basename(f) for f in glob.glob("scripts/*.py")]
    files.sort()

    for f in files:
        shutil.copy(os.path.join("scripts", f), os.path.join("dist", f))

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Scripts Repository</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --accent: #38bdf8;
            --accent-hover: #7dd3fc;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 2rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }}
        h1 {{
            font-size: 3rem;
            margin-bottom: 2rem;
            background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            animation: fadeInDown 0.8s ease-out;
        }}
        .container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
            width: 100%;
            max-width: 1000px;
        }}
        .card {{
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            text-decoration: none;
            color: var(--text-color);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
            animation: fadeInUp 0.8s ease-out backwards;
            border: 1px solid transparent;
        }}
        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, transparent, rgba(56, 189, 248, 0.1));
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);
            border-color: var(--accent);
        }}
        .card:hover::before {{
            opacity: 1;
        }}
        .card:hover h2 {{
            color: var(--accent-hover);
        }}
        .card h2 {{
            font-size: 1.25rem;
            margin: 0;
            z-index: 1;
            transition: color 0.3s ease;
            word-break: break-all;
            text-align: center;
        }}
        .icon {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            z-index: 1;
            transition: transform 0.3s ease;
        }}
        .card:hover .icon {{
            transform: scale(1.1) rotate(5deg);
        }}
        
        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body>
    <h1>🚀 Python Playground</h1>
    <div class="container">
"""
    
    for i, f in enumerate(files):
        delay = i * 0.1
        html_content += f"""
        <a href="{f}" class="card" style="animation-delay: {delay}s">
            <div class="icon">🐍</div>
            <h2>{f}</h2>
        </a>"""

    html_content += """
    </div>
</body>
</html>"""

    with open("dist/index.html", "w", encoding="utf-8") as file:
        file.write(html_content)
        
    print(f"Generated index.html with {len(files)} links.")

if __name__ == "__main__":
    generate_html()
