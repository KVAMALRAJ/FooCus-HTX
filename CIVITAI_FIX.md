# CivitAI Downloader - Bug Fix Summary

## Issue
The initial implementation was getting 404 and 400 errors when trying to download models from CivitAI.

## Root Cause
The CivitAI API has two different types of endpoints:
1. **Metadata endpoints** (v1 API): `/api/v1/models/{id}` and `/api/v1/model-versions/{id}`
2. **Download endpoint**: `/api/download/models/{versionId}?token={api_key}`

The original implementation tried to use the metadata endpoints to get download URLs, which was causing errors.

## Solution
Changed to use CivitAI's **direct download endpoint** format, which matches the working wget commands:

```bash
# User's working wget command format:
wget -c 'https://civitai.com/api/download/models/2391289?token=API_KEY' -O CyberRealystic.safetensors
```

### Key Changes

#### 1. Updated `civitai_manager.py`
- Modified `download_model()` to construct direct download URLs
- Changed format to: `https://civitai.com/api/download/models/{version_id}?token={api_key}`
- Added support for custom filenames
- Improved version ID handling (tries version ID first, falls back to model ID)

#### 2. Updated `webui.py` UI
- Changed label from "Model ID or Version ID" to "Version ID (from CivitAI)"
- Added separate "Filename (optional)" field
- Updated instructions to clarify version ID usage
- Modified callback to pass both version ID and filename

#### 3. Updated Documentation
- Clarified that **Version ID** is required (not model ID)
- Added examples showing how to find version IDs
- Included wget command format reference

## Testing

### Test Cases
The implementation now handles the exact examples from the user:

**Checkpoint:**
- Version ID: `2391289`
- Filename: `CyberRealystic.safetensors`
- URL: `https://civitai.com/api/download/models/2391289?token=YOUR_KEY`

**LoRA:**
- Version ID: `2267500`
- Filename: `Indian_Clothing.safetensors`
- URL: `https://civitai.com/api/download/models/2267500?token=YOUR_KEY`

### Test Script
Created `test_civitai_download.py` to validate both downloads work correctly.

## How Users Should Use It Now

1. **Find the Version ID:**
   - Go to CivitAI model page
   - Click on specific version you want
   - Copy the version ID from URL: `?modelVersionId=2391289` → use `2391289`

2. **In Fooocus UI:**
   - Paste version ID into "Version ID" field
   - (Optional) Enter custom filename
   - Click Download

3. **The model automatically:**
   - Downloads using direct CivitAI endpoint
   - Determines correct folder (checkpoint/lora/etc)
   - Saves with correct filename
   - Shows download progress

## API Flow

### Before (Not Working):
```
1. GET /api/v1/models/{id} → 404/400 errors
2. Parse response for download URL
3. Download from parsed URL
```

### After (Working):
```
1. Try GET /api/v1/model-versions/{version_id} for metadata (for type detection)
2. Construct direct download URL: /api/download/models/{version_id}
3. Download directly with streaming
```

## Benefits of This Approach

1. **More Reliable**: Uses the same endpoint as wget/browser downloads
2. **Simpler**: Direct download without complex API parsing
3. **Flexible**: Supports custom filenames
4. **Consistent**: Matches how users already download via terminal
5. **Better Error Messages**: Clear indication of what went wrong

## Files Modified

- `modules/civitai_manager.py` - Core download logic
- `webui.py` - UI and callbacks
- `CIVITAI_MODEL_MANAGER.md` - Documentation
- `test_civitai_download.py` - Test script (new)

## Backward Compatibility

The implementation still supports:
- Version IDs (primary use case)
- Model IDs (automatically gets latest version)
- With or without API key
- Automatic model type detection
- Progress callbacks
