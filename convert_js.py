import base64
from pathlib import Path

image_path = Path("Let_s_Talk_AI_Circle_Logo-removebg-preview.png")
output_path = Path("assets/lets-talk-ai-logo.js")

image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

output_path.write_text(
    f'window.letsTalkAiLogoData = "data:image/png;base64,{image_data}";\n',
    encoding="utf-8"
)

print(f"Created: {output_path}")