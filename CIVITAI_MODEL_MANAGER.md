# CivitAI Model Manager for Fooocus

Download models, checkpoints, LoRAs, and more directly from CivitAI into Fooocus with automatic organization.

## Features

- ✅ **Direct Downloads** - Download models directly from CivitAI using model IDs
- ✅ **Automatic Organization** - Files are automatically placed in the correct folders
- ✅ **Progress Tracking** - Real-time download progress with size information
- ✅ **File Management** - View all downloaded models organized by type
- ✅ **API Key Support** - Optional CivitAI API key for accessing early-access models
- ✅ **Smart Detection** - Automatically detects model type (checkpoint, LoRA, embedding, etc.)

## Quick Start

### 1. Open CivitAI Models Tab

1. Launch Fooocus
2. Navigate to the **CivitAI Models** tab in the right panel

### 2. Download a Model

1. Go to [CivitAI](https://civitai.com/) and find a model you want
2. Click on the specific **version** you want to download
3. Copy the **Version ID**:
   - From URL: `https://civitai.com/models/123456?modelVersionId=2391289` → use `2391289`
   - Or look for the version ID on the version's page
4. Paste the **Version ID** into the "Version ID (from CivitAI)" field
5. (Optional) Enter a custom filename like `CyberRealystic.safetensors`
6. Click **Download**
7. Wait for the download to complete (progress shown in status box)

**Important:** Use the **Version ID**, not the model ID. Each model can have multiple versions.

### 3. Use Your Downloaded Model

Models are automatically placed in the correct folders:
- **Checkpoints** → `models/checkpoints/`
- **LoRAs** → `models/loras/`
- **Embeddings** → `models/embeddings/`
- **VAE** → `models/vae/`
- **ControlNet** → `models/controlnet/`
- **Upscale Models** → `models/upscale_models/`

After downloading, refresh the model list in the respective tab (Style, LoRA, etc.) to use your new model.

## Configuration

### CivitAI API Key (Optional)

An API key is **not required** for downloading public models, but provides benefits:

**Benefits of using an API key:**
- Access to early-access models
- Higher download priority
- No rate limiting
- Access to NSFW models (if enabled in your CivitAI account)

**To get your API key:**
1. Visit [CivitAI Account Settings](https://civitai.com/user/account)
2. Navigate to "API Keys" section
3. Generate a new API key
4. Copy the key

**To configure:**
1. In Fooocus, go to **CivitAI Models** tab
2. Scroll to "CivitAI API Key Configuration"
3. Paste your API key
4. Click **Save API Key**

The key is saved to your `config.txt` file:
```json
{
  "civitai_api_key": "your_api_key_here"
}
```

## Model Types Supported

The manager automatically detects and organizes these model types:

| CivitAI Type | Fooocus Folder | Description |
|--------------|----------------|-------------|
| Checkpoint | `models/checkpoints/` | Base SDXL models |
| LoRA | `models/loras/` | LoRA fine-tuning models |
| LoCon | `models/loras/` | LoCon models (treated as LoRAs) |
| TextualInversion | `models/embeddings/` | Embedding/textual inversion |
| VAE | `models/vae/` | VAE models |
| ControlNet | `models/controlnet/` | ControlNet models |
| Upscaler | `models/upscale_models/` | Upscaling models |

## Managing Downloaded Models

### View Downloaded Models

1. Go to **CivitAI Models** tab
2. Scroll to "Downloaded Models" section
3. Use the dropdown to filter by type:
   - **all** - Show all model types
   - **checkpoints** - Only checkpoints
   - **loras** - Only LoRAs
   - **embeddings** - Only embeddings
   - etc.

### Refresh Model List

Click the **🔄 Refresh List** button to update the list of downloaded files.

### Model Information Displayed

- **Category** - Model type (Checkpoints, LoRAs, etc.)
- **Filename** - Full filename with extension
- **Size** - File size in MB

## Usage Examples

### Example 1: Downloading a Checkpoint

1. Visit https://civitai.com/models/133005/juggernaut-xl
2. Click on a specific version (e.g., "V9")
3. Copy the version ID: Let's say it's `2391289`
4. Paste `2391289` into the Version ID field
5. Enter filename: `CyberRealystic.safetensors`
6. Click Download
7. Model appears in `models/checkpoints/`
8. Select it from the Model dropdown in Style tab

### Example 2: Downloading a LoRA

1. Visit https://civitai.com/models/124347/detail-tweaker-xl
2. Click on the version you want
3. Copy the version ID from the URL (e.g., `2267500`)
4. Paste `2267500` and optionally enter `Indian_Clothing.safetensors`
5. Download
6. Model appears in `models/loras/`
7. Enable it in the LoRA tab

### Example 3: Using wget Command Format

If you have a wget command like:
```bash
wget -c 'https://civitai.com/api/download/models/2391289?token=YOUR_TOKEN' -O CyberRealystic.safetensors
```

Just use:
- **Version ID**: `2391289`
- **Filename**: `CyberRealystic.safetensors`

## Troubleshooting

### "Failed to fetch model information"

**Causes:**
- Invalid model ID
- Model is deleted or private
- Network connection issue
- CivitAI API is down

**Solutions:**
- Verify the model ID is correct
- Check if model is still available on CivitAI
- Try again later
- Add API key if model requires authentication

### "Download timeout"

**Causes:**
- Large file size (>5GB)
- Slow internet connection
- Server issues

**Solutions:**
- Check your internet connection
- Try downloading during off-peak hours
- For very large models, consider manual download

### "File already exists"

The file is already downloaded. If you want to re-download:
1. Go to the appropriate models folder
2. Delete the existing file
3. Try downloading again

### "Authentication required" / 401 Error

**Solutions:**
- Model requires API key - add one in the API Key Configuration section
- Your API key may be invalid - generate a new one
- Model may be restricted (NSFW, early access) - check your CivitAI account settings

### Download Progress Not Showing

The progress updates every few MB. For small files (<100MB), it may complete quickly without showing detailed progress.

### Downloaded Model Not Appearing

**Solutions:**
1. Click the refresh button in the relevant tab (Model dropdown, LoRA list, etc.)
2. Restart Fooocus
3. Check the correct folder in your file system
4. Verify the download actually completed successfully

## Technical Details

### Files Modified/Created

**New Files:**
- `modules/civitai_manager.py` - Core CivitAI integration
- `CIVITAI_MODEL_MANAGER.md` - This documentation

**Modified Files:**
- `modules/config.py` - Added `civitai_api_key` configuration
- `webui.py` - Added CivitAI Models tab with UI

### API Endpoints Used

- `GET /api/v1/models/{modelId}` - Get model information
- `GET /api/v1/model-versions/{versionId}` - Get version information
- `GET /api/download/models/{versionId}` - Download model file

### File Organization Logic

The manager uses CivitAI's model type metadata to determine the correct folder:

```python
type_mapping = {
    'checkpoint': 'checkpoints',
    'lora': 'loras',
    'locon': 'loras',
    'textualinversion': 'embeddings',
    'embedding': 'embeddings',
    'vae': 'vae',
    'controlnet': 'controlnet',
    'poses': 'controlnet',
    'upscaler': 'upscale_models'
}
```

### Download Process

1. Fetch model metadata from CivitAI API
2. Determine model type and target folder
3. Get download URL (with API token if available)
4. Stream download with progress tracking
5. Save to appropriate folder
6. Verify file integrity

## Security & Privacy

- **API Key Storage**: Keys are stored in `config.txt` in plain text
- **HTTPS**: All API communication uses HTTPS
- **Local Files**: All downloads are stored locally
- **No Telemetry**: No usage data is sent anywhere

**Important:** Keep your `config.txt` secure and never share it publicly if it contains API keys.

## Limitations

- **File Size**: Very large files (>10GB) may timeout on slow connections
- **Concurrent Downloads**: One download at a time
- **Delete Function**: Currently viewing only, delete manually from file system
- **Version Selection**: Defaults to latest version if not specified

## Future Enhancements

Potential improvements for future versions:
- Batch downloading multiple models
- Queue system for multiple downloads
- Integrated model preview/thumbnails
- Search and browse CivitAI within Fooocus
- Download history and management
- Automatic model updates
- Pause/resume downloads

## Support

If you encounter issues:
1. Check this documentation first
2. Verify your model ID is correct
3. Try with an API key if not using one
4. Check CivitAI's status page
5. Report issues with console logs

## Credits

- **CivitAI**: Model hosting platform - https://civitai.com/
- **Fooocus**: Base application
- **Integration**: Custom extension for Fooocus

## License

Same as Fooocus main project.
