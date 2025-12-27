# Product Requirements

## Problem Statement
The project is a version of Fooocus (FooCus-HTX) running on Google Colab. Recent updates to Gradio (v4.x) have caused compatibility issues with the custom component hijacks used in the project, specifically missing attributes in `gradio.processing_utils`.

## Functional Requirements
- Ability to generate images using SDXL models.
- Functional Gradio UI for interacting with the generation engine.
- Proper handling of images and masks in the UI.

## Non-Functional Requirements
- Compatibility with Google Colab environment.
- Compatibility with Gradio 4.44.1.

## Success Criteria
- The Gradio UI starts without errors.
- Image generation tasks complete and display images in the UI without `AttributeError`.
