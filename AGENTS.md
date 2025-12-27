# Operational Rules

## Setup Commands
- `pip install -r requirements_versions.txt`
- `python entry_with_update.py --share --always-high-vram --debug-mode --always-offload-from-vram --disable-server-log` (Standard Colab run command)

## Test Commands
- No specific test suite found. Manual verification by running the app in Colab.

## Conventions
- Use `gradio_hijack.py` to modify Gradio components for compatibility.
- Follow Fooocus architecture for model management and UI.

## Quality Gates
- Code must be compatible with Gradio 4.44.1.
- Changes must not break SDXL model loading or image generation.
