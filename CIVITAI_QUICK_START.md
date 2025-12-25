# Quick Start: CivitAI Model Downloader

## Finding Version IDs on CivitAI

### Method 1: From Model Page
1. Go to any CivitAI model page (e.g., https://civitai.com/models/133005)
2. **Click on the specific version** you want (e.g., "V9", "V10", etc.)
3. Look at the URL bar: `?modelVersionId=2391289`
4. Copy the number after `modelVersionId=` → **2391289**

### Method 2: From Download Button
1. Right-click the "Download" button on CivitAI
2. Select "Copy Link Address"
3. You'll get something like: `https://civitai.com/api/download/models/2391289?token=...`
4. Copy the number after `/models/` → **2391289**

## Using in Fooocus

### Simple Download (Auto Filename)
1. Open Fooocus → Go to **CivitAI Models** tab
2. Paste version ID: `2391289`
3. Leave filename blank
4. Click **Download**

### Custom Filename Download
1. Open Fooocus → Go to **CivitAI Models** tab
2. Paste version ID: `2391289`
3. Enter filename: `CyberRealystic.safetensors`
4. Click **Download**

## Examples

### Example 1: Checkpoint Model
```
Version ID: 2391289
Filename: CyberRealystic.safetensors
Result: Downloads to models/checkpoints/CyberRealystic.safetensors
```

### Example 2: LoRA Model
```
Version ID: 2267500
Filename: Indian_Clothing.safetensors
Result: Downloads to models/loras/Indian_Clothing.safetensors
```

### Example 3: Auto-detect Filename
```
Version ID: 2391289
Filename: (leave blank)
Result: Uses original CivitAI filename automatically
```

## Terminal/Wget Alternative

If you prefer terminal, these are equivalent:

**Fooocus UI:**
```
Version ID: 2391289
Filename: CyberRealystic.safetensors
```

**Terminal:**
```bash
wget -c 'https://civitai.com/api/download/models/2391289?token=YOUR_API_KEY' \
  -O CyberRealystic.safetensors
```

## API Key Setup (Optional)

### When Do You Need It?
- Early access models
- NSFW models (if enabled in your CivitAI account)
- Avoiding rate limits
- Private models

### How to Set It Up
1. Get API key: https://civitai.com/user/account
2. In Fooocus → **CivitAI Models** tab
3. Scroll to "CivitAI API Key Configuration"
4. Paste your key
5. Click **Save API Key**

## Model Types Detected Automatically

| Model Type | Folder Location |
|------------|----------------|
| Checkpoint | models/checkpoints/ |
| LoRA | models/loras/ |
| LoCon | models/loras/ |
| Embedding | models/embeddings/ |
| TextualInversion | models/embeddings/ |
| VAE | models/vae/ |
| ControlNet | models/controlnet/ |
| Upscaler | models/upscale_models/ |

## Troubleshooting

### "Failed to fetch model information"
- ✓ Verify version ID is correct (not model ID)
- ✓ Check internet connection
- ✓ Try adding an API key if model requires authentication

### "File already exists"
- ✓ File was already downloaded
- ✓ Delete from folder manually if you want to re-download

### Download stuck or slow
- ✓ Large files (>2GB) take time
- ✓ Check your internet speed
- ✓ Try during off-peak hours

### "Authentication required"
- ✓ Model requires API key
- ✓ Add your API key in configuration section

## Tips

1. **Always use Version ID**, not model ID
2. **Custom filenames** help you organize models better
3. **API key** is optional for public models
4. **Progress** shows in real-time during download
5. **Auto-detection** places models in correct folders
6. **Refresh** model lists in UI after downloading

## Support

For more details, see: [CIVITAI_MODEL_MANAGER.md](CIVITAI_MODEL_MANAGER.md)
