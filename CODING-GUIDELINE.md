# Learning Log

## Anti-patterns Discovered
- **Version Pinning Issues**: Relying on internal Gradio utilities (`processing_utils`) that change between major versions (v3 to v4).

## Correct Approaches
- Use `gradio.utils` or `gradio_client.utils` for base64 conversions in Gradio 4.x.
- For PIL to base64 conversion in Gradio 4:
  ```python
  import io
  import base64
  from PIL import Image
  
  def pil_to_base64(img):
      buffered = io.BytesIO()
      img.save(buffered, format="PNG")
      img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
      return f"data:image/png;base64,{img_str}"
  ```
- **Gradio 4 Blocks API**: In Gradio 4, `Blocks.dependencies` has been replaced by `Blocks.fns`. When patching `get_api_info`, check for both attributes to maintain compatibility.
- **Internal Utility Patches**: If relying on `gradio.processing_utils` methods that were removed in v4 (like `encode_pil_to_base64`, `decode_base64_to_image`, `resize_and_crop`), patch them back into the module if they are missing to minimize changes in the rest of the codebase.
