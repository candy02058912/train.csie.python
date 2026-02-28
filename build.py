import os
import glob
import shutil
import json
import re
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def load_exercises():
    exercises = []
    exercise_files = glob.glob("exercises/ex*.py")
    exercise_files.sort()
    
    for idx, filepath in enumerate(exercise_files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse metadata from top-level docstring
        title_match = re.search(r"title:\s*(.+)", content)
        quest_match = re.search(r"quest_html:\s*(.+)", content)
        
        title = title_match.group(1).strip() if title_match else f"Exercise {idx + 1}"
        quest_html = quest_match.group(1).strip() if quest_match else ""
        
        # Split code sections
        parts = content.split("# ==== STARTER CODE ====")
        starter_and_test = parts[1] if len(parts) > 1 else ""
        
        code_parts = starter_and_test.split("# ==== TEST CODE ====")
        starter_code = code_parts[0].strip() if len(code_parts) > 0 else ""
        test_code = code_parts[1].strip() if len(code_parts) > 1 else ""
        
        # Determine ID from filename (e.g., ex001.py -> 1)
        filename = os.path.basename(filepath)
        id_str = str(int(re.search(r"\d+", filename).group()))
        
        exercises.append({
            "id": id_str,
            "title": title,
            "quest_html": quest_html,
            "starter_code": starter_code,
            "test_code": test_code
        })
        
    return exercises

def generate_html():
    os.makedirs("dist", exist_ok=True)
    
    # Copy scripts
    files = [os.path.basename(f) for f in glob.glob("scripts/*.py")]
    files.sort()
    for f in files:
        shutil.copy(os.path.join("scripts", f), os.path.join("dist", f))

    # Load exercises from directory
    exercises = load_exercises()

    # Setup Jinja2 Environment
    env = Environment(loader=FileSystemLoader('templates'))
    
    # Get GAS_URL from environment
    gas_url = os.environ.get("GAS_URL", "")

    # Render interactive exercises
    exercise_template = env.get_template('exercise.html')
    for ex in exercises:
        test_script_js_string_literal = json.dumps(ex["test_code"])
        html_content = exercise_template.render(
            ex=ex,
            test_code_json=test_script_js_string_literal,
            gas_url=gas_url
        )
        
        ex_filename = f"exercise_{ex['id']}.html"
        with open(f"dist/{ex_filename}", "w", encoding="utf-8") as file:
            file.write(html_content)

    # Render index.html
    index_template = env.get_template('index.html')
    index_html = index_template.render(
        exercises=exercises,
        scripts=files,
        gas_url=gas_url
    )
    
    with open("dist/index.html", "w", encoding="utf-8") as file:
        file.write(index_html)
        
    print(f"Generated index.html with {len(exercises)} exercises and {len(files)} scripts.")

if __name__ == "__main__":
    generate_html()
