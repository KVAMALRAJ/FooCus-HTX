# Project Memory Bank

## Project Context
- **Name**: FooCus-HTX
- **Purpose**: A fork of Fooocus optimized for Google Colab with custom enhancements.
- **Tech Stack**: Python, Gradio (v4.44.1), PyTorch, SDXL.

## Session History
- **Session 1 (2025-12-27)**:
  - **Focus**: Fixing Gradio `AttributeError` in Colab.
  - **Completed Tasks**:
    - Initial codebase exploration and creation of spec files.
    - Patched `gradio.processing_utils` in `modules/gradio_hijack.py` to restore `encode_pil_to_base64`, `decode_base64_to_image`, and `resize_and_crop` for Gradio 4.x compatibility.
    - Updated `patched_get_api_info` to handle Gradio 4.x `Blocks` structure (using `fns` instead of `dependencies`).
  - **Decisions**: Use internal patches in `gradio_hijack.py` to ensure compatibility across Gradio versions without changing the main application logic.
  - **Next Goals**: Final verification and reporting to user.

- **Session 2 (2025-12-27)**:
  - **Focus**: Fixing AssertionError in image prompt and Advanced tab visibility.
  - **Completed Tasks**:
    - Fixed Developer Debug Mode visibility by relocating `dev_tools` to Advanced tab scope in `webui.py`.
    - Resolved `AssertionError` in `modules/gradio_hijack.py` by making `preprocess` robust to Gradio 4.x dictionary inputs (handling paths, urls, and base64).
  - **Decisions**: Adopted a robust image loading strategy in `gradio_hijack.py` to support diverse input formats from newer Gradio versions.
  - **Next Goals**: Complete verification and summarize for user.

## Active Context
- **Current Task**: Fixing `AttributeError: module 'gradio.processing_utils' has no attribute 'encode_pil_to_base64'`.
- **Blockers**: None.
- **Recent Changes**: Added `AGENTS.md`, `SPEC.md`, `PLANS.md`, `ARCHITECTURE.md`, `CODING-GUIDELINE.md`, `MEMORY_BANK.md`.

## Key Decisions Registry
- **2025-12-27**: Adopt Spec-Driven Development for the project.
