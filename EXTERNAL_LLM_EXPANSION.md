# External LLM Prompt Expansion for Fooocus

This feature adds support for using external Large Language Models (LLMs) for advanced prompt expansion in Fooocus. Currently supports DeepSeek API.

## Features

- **Toggle between standard Fooocus expansion and external LLM expansion** - Use a simple checkbox in the UI
- **DeepSeek API integration** - Leverages DeepSeek's chat model for intelligent prompt enhancement
- **Automatic fallback** - Falls back to standard Fooocus expansion if API is unavailable
- **Secure configuration** - API keys stored in `.env` file (not committed to git)

## Setup

### 1. Install Dependencies

The `requests` library is already included in `requirements_versions.txt`. If you need to install it manually:

```bash
pip install requests==2.31.0
```

### 2. Get DeepSeek API Key

1. Visit [DeepSeek API Platform](https://platform.deepseek.com/)
2. Sign up for an account
3. Generate an API key from your dashboard

### 3. Configure API Key

Create a `.env` file in the Fooocus root directory (where `launch.py` is located):

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your DeepSeek API key:

```env
DEEPSEEK_API_KEY=your_actual_api_key_here
DEEPSEEK_API_BASE=https://api.deepseek.com
```

**Important:** The `.env` file should NOT be committed to git. It's already in `.gitignore` (if not, add it).

### 4. Enable in UI

1. Launch Fooocus normally
2. Navigate to the **Advanced** tab
3. Check the box **"Use External LLM for Prompt Expansion"**
4. Make sure you have a style that includes prompt expansion (like "Fooocus V2")

## Usage

### Basic Usage

1. Enter your prompt as usual
2. Enable external LLM expansion in Advanced settings
3. Generate images

The external LLM will expand your prompt with:
- Artistic and technical details (lighting, composition, style)
- Quality enhancers (highly detailed, masterpiece, 8k, etc.)
- Better context understanding and creative additions
- Maintains your original concept

### Example

**Input:** `a cat`

**Fooocus Standard Expansion:**
```
a cat, intricate, elegant, highly detailed, digital painting, artstation, concept art
```

**External LLM Expansion:**
```
a highly detailed cat, professional photography, natural lighting, detailed fur texture, 
sharp focus, high resolution, photorealistic, masterpiece quality, sitting pose, 
warm colors, soft bokeh background
```

## How It Works

### Architecture

1. **Configuration** - Settings stored in `modules/config.py`
2. **API Module** - `extras/llm_expansion.py` handles DeepSeek communication
3. **Pipeline Integration** - `modules/default_pipeline.py` manages both expansion engines
4. **Worker Logic** - `modules/async_worker.py` decides which expansion to use
5. **UI Control** - `webui.py` provides the toggle checkbox

### Decision Flow

```
User enters prompt → Enable expansion + External LLM checkbox?
  ├─ NO → Use standard Fooocus GPT-2 expansion
  └─ YES → Check API availability
      ├─ Available → Use DeepSeek API expansion
      └─ Unavailable → Fallback to Fooocus expansion
```

## Configuration Options

### In config.txt

Add to your `config.txt` to change the default behavior:

```json
{
  "default_use_external_llm_expansion": true
}
```

### Environment Variables

You can also set these via environment variables:

```bash
export DEEPSEEK_API_KEY="your_key_here"
export DEEPSEEK_API_BASE="https://api.deepseek.com"
```

## Troubleshooting

### "DEEPSEEK_API_KEY not found" Warning

**Solution:** Create a `.env` file with your API key (see Setup step 3)

### API Timeout or Connection Error

**Symptoms:** Console shows timeout errors, falls back to standard expansion

**Solutions:**
- Check your internet connection
- Verify API key is correct
- Check if DeepSeek API is accessible from your location
- Try increasing timeout in `extras/llm_expansion.py` (currently 30 seconds)

### Expansion Not Working

**Checklist:**
1. ✓ Checkbox "Use External LLM for Prompt Expansion" is enabled
2. ✓ Style with expansion is selected (e.g., "Fooocus V2")
3. ✓ `.env` file exists with valid DEEPSEEK_API_KEY
4. ✓ `requests` library is installed
5. ✓ Check console for error messages

### Standard Expansion Still Being Used

The system will automatically fall back to standard expansion if:
- API key is missing or invalid
- Network connection fails
- API request times out
- API returns an error

Check the console output for messages like:
```
[External LLM Expansion] Using external LLM expansion
```

If you don't see this, check the troubleshooting steps above.

## Cost Considerations

DeepSeek API usage is charged per request. The prompt expansion feature:
- Makes **1 API call per image** (when enabled)
- Uses approximately **50-100 tokens per request**
- Cost: Check [DeepSeek Pricing](https://platform.deepseek.com/pricing)

**Tip:** Toggle off when you don't need advanced expansion to save API credits.

## Advanced Customization

### Modify Expansion Prompt

Edit `extras/llm_expansion.py` to customize the system message that guides the LLM:

```python
system_message = """You are an expert at expanding stable diffusion prompts...
[Customize instructions here]
"""
```

### Change Model or Parameters

In `extras/llm_expansion.py`, modify the API request:

```python
data = {
    'model': 'deepseek-chat',  # Change model here
    'temperature': 0.7,         # Adjust creativity (0.0-1.0)
    'max_tokens': 200           # Maximum expansion length
}
```

## Technical Details

### Files Modified/Created

1. **Created:**
   - `extras/llm_expansion.py` - DeepSeek API integration
   - `.env.example` - Environment variable template
   - `EXTERNAL_LLM_EXPANSION.md` - This documentation

2. **Modified:**
   - `modules/config.py` - Added `default_use_external_llm_expansion` config
   - `modules/default_pipeline.py` - Added external expansion engine initialization
   - `modules/async_worker.py` - Added expansion selection logic
   - `webui.py` - Added UI checkbox control
   - `requirements_versions.txt` - Added `requests` dependency

### API Specification

**Endpoint:** `POST https://api.deepseek.com/v1/chat/completions`

**Request:**
```json
{
  "model": "deepseek-chat",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "Expand this image generation prompt: {prompt}"}
  ],
  "temperature": 0.7,
  "max_tokens": 200
}
```

**Response:**
```json
{
  "choices": [{
    "message": {
      "content": "expanded prompt text here..."
    }
  }]
}
```

## Future Enhancements

Potential future additions:
- Support for other LLM providers (OpenAI, Anthropic, local LLMs)
- Caching of expanded prompts
- Batch expansion for multiple prompts
- Custom expansion templates
- Prompt style presets (photographic, artistic, anime, etc.)

## Contributing

If you encounter issues or have suggestions:
1. Check existing issues on GitHub
2. Provide console logs when reporting bugs
3. Include your configuration (without API keys)

## License

Same as Fooocus main project.

## Credits

- Original Fooocus prompt expansion by Lvmin Zhang
- External LLM integration: Custom extension for Fooocus
- DeepSeek API: [DeepSeek](https://www.deepseek.com/)
