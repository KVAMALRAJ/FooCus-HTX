# System Design

## Component Structure
- `entry_with_update.py`: Entry point for Colab, handles updates and starts the app.
- `launch.py`: Main application launcher.
- `modules/gradio_hijack.py`: Hijacks Gradio's `Image` component to add custom functionality or fix version-specific issues.
- `modules/model_management.py`: Handles loading and offloading of models (SDXL, LoRAs, etc.).

## Design Decisions
- **Gradio Hijacking**: Used to extend Gradio's base components to support specific Fooocus features like complex image/mask processing that isn't natively supported or needs modification for the specific workflow.

## Integration Points
- Gradio UI integrates with the Fooocus backend for image generation.
- Google Colab environment provides the GPU and execution context.
