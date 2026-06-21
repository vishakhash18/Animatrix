import os
from google import genai

# Setup the Gemini API connection layer
ai_client = genai.Client()

# Assignment parameters bundled into a clean string layout
assignment_prompt = """
Write a complete, working Python script using the Manim Community library (`manim`).
The goal is to create a scene that visually proves the Pythagorean Theorem (a^2 + b^2 = c^2).

Requirements:
1. Create a right-angled triangle. Label its sides 'a', 'b', and 'c'.
2. Visually construct and shade three squares built on each of the three sides.
3. Clearly display the algebraic identity a^2 + b^2 = c^2 on screen.
4. Ensure appropriate use of self.play() and self.wait() calls to make the animation clean and readable.
5. Use proper color coding to link the side labels to their respective squares.

Return ONLY the raw executable Python code inside a single standard markdown code block. Do not include any extra introductory or concluding text.
"""

print("[System] Dispatching request to Gemini model engine...")

# Fetching the structural code block from the flash model
api_response = ai_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=assignment_prompt,
)

target_filepath = "task1_pythagoras/pythagoras.py"
raw_response_content = api_response.text

# Sanitizing text layout to isolate raw executable Python code
if "```python" in raw_response_content:
    extracted_source = raw_response_content.split("```python")[1].split("```")[0]
elif "```" in raw_response_content:
    extracted_source = raw_response_content.split("```")[1].split("```")[0]
else:
    extracted_source = raw_response_content

cleaned_source_code = extracted_source.strip()

# Writing the final refactored code output safely to disk
with open(target_filepath, "w", encoding="utf-8") as output_file:
    output_file.write(cleaned_source_code)

print(f"[Success] Local output file synced at: {target_filepath}")
