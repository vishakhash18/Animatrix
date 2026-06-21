<img width="1090" height="627" alt="image" src="https://github.com/user-attachments/assets/4ad4558d-63c3-4c20-8586-702b19958f88" /># Auto-Anim Engine: LLM-Driven Mathematical Visualization & Analysis

## Project Overview
This repository explores the capabilities and limitations of automated code generation using large language models, specifically focusing on the Google Generative AI (Gemini) API. The core objective is to programmatically generate mathematical animations via Manim, execute them locally to identify syntax errors or architectural flaws, apply rigorous structural refactoring, and document the debugging pipeline.

The study centers on two foundational mathematical principles:
1. **The Pythagorean Theorem ($a^2 + b^2 = c^2$):** A geometric breakdown that constructs a right-angled triangle, dynamically labels its boundaries, and overlays filled boundary squares to visually validate area equivalence.
2. **Fourier Series Synthesis:** A dynamic plotting canvas illustrating the step-by-step assembly of a square wave by calculating and combining individual harmonic sine functions ($n=1, 3, 5, 7, 9$) with high-contrast color indexing.

---

## Directory Architecture
The workspace rejects a flat structure in favor of a highly modular, decoupled directory layout:

```text
manim-genai-assignment/
├── .gitignore                  # Exclusions for Python runtimes & virtual environments
├── requirements.txt            # System environment packages (manim, numpy, google-generativeai)
├── README.md                   # Core documentation & engineering post-mortem
├── task1_pythagoras/
│   ├── generate_scene.py       # API configuration & prompt engineering execution
│   └── pythagoras.py           # Refactored, production-ready Manim script
└── task2_fourier/
    ├── generate_scene.py       # API configuration & prompt engineering execution
    └── fourier_series.py       # Refactored, production-ready Manim script

