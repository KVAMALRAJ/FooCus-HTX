# DeepSeek System Prompt & Expanded Prompt Display - Feature Summary

## Overview

Added two new features to enhance the External LLM (DeepSeek) prompt expansion:

1. **Editable System Prompt** - Customize how DeepSeek expands your prompts
2. **Expanded Prompt Display** - See the actual expanded prompt used for generation

## What Was Added

### 1. Configurable System Prompt

**UI Changes:**
- Added accordion in Advanced tab: "DeepSeek System Prompt"
- Editable text area with 10 lines for system prompt
- "Save System Prompt" button
- "Reset to Default" button
- Status message display

**Backend Changes:**
- Added `deepseek_system_prompt` to config.py
- Modified `llm_expansion.py` to use configurable system prompt
- Added methods: `set_system_prompt()`, `get_system_prompt()`
- System prompt persists in config.txt

### 2. Expanded Prompt Viewer

**UI Changes:**
- Added collapsible accordion below prompt input: "📝 Extended Prompt (from DeepSeek LLM)"
- Shows automatically after generation if External LLM was used
- Displays all expanded prompts (numbered if multiple)
- Non-editable display field

**Backend Changes:**
- Added `expanded_prompts` list to AsyncTask
- Modified async_worker.py to capture expanded prompts
- Updated generate_clicked() to show/hide accordion based on availability
- Expanded prompts stored during generation process

## Files Modified

### Core Files
1. **modules/config.py**
   - Added `deepseek_system_prompt` configuration field with default value

2. **extras/llm_expansion.py**
   - Added `system_prompt` attribute
   - Added `last_expanded_prompt` tracking
   - Modified `expand_prompt()` to use configurable system prompt
   - Added methods to get/set system prompt

3. **modules/async_worker.py**
   - Added `expanded_prompts` list to AsyncTask
   - Capture expanded prompts during generation
   - Store for later display

4. **webui.py**
   - Added system prompt editor UI in Advanced tab
   - Added expanded prompt display accordion
   - Added callback functions for save/reset
   - Updated generate_clicked() to handle expanded prompt display
   - Updated generate button outputs to include new fields

### Documentation
5. **CUSTOM_SYSTEM_PROMPT.md** (new)
   - Complete guide to customizing system prompts
   - Examples for different use cases
   - Tips and best practices

6. **config_sample_with_llm.txt**
   - Added `deepseek_system_prompt` field

## How It Works

### System Prompt Flow
```
1. User edits system prompt in UI
2. Clicks "Save System Prompt"
3. Saved to config.txt
4. Runtime config updated
5. ExternalLLMExpansion instance updated
6. Next generation uses new system prompt
```

### Expanded Prompt Display Flow
```
1. User enters prompt: "a cat"
2. External LLM expansion enabled
3. DeepSeek expands using system prompt
4. Expanded prompt stored in task.expanded_prompts
5. Image generated using expanded prompt
6. After generation, accordion shows with expanded text
7. User can see: "a highly detailed cat, professional photography..."
```

## Usage Examples

### Example 1: View Default Expansion

**Input:** "a mountain landscape"

**System Prompt:** (default)

**Expanded (visible after generation):**
```
a mountain landscape, highly detailed, professional landscape photography, 
dramatic lighting, golden hour, epic scenery, 8k resolution, masterpiece quality, 
wide angle composition, sharp focus, natural colors, atmospheric perspective, 
majestic peaks, detailed textures
```

### Example 2: Custom System Prompt for Anime

**Custom System Prompt:**
```
You are an expert in anime art styles. Focus on anime-specific details,
character designs, and illustration techniques. Include quality markers
like "anime style", "detailed illustration", etc.
```

**Input:** "a girl with blue hair"

**Expanded (visible after generation):**
```
a girl with blue hair, anime style, detailed illustration, shoujo art style,
expressive eyes, flowing hair animation, vibrant colors, cel shading,
high quality anime, detailed character design, soft lighting, kawaii aesthetic
```

## Benefits

### For Users
1. **Transparency** - See exactly what prompt was used
2. **Learning** - Understand effective prompt patterns
3. **Control** - Customize expansion behavior
4. **Flexibility** - Different system prompts for different projects

### For Quality
1. **Consistency** - Same system prompt = similar expansions
2. **Optimization** - Tune system prompt for your style
3. **Debugging** - Identify why results vary
4. **Improvement** - Learn from good expansions

## Configuration

### In config.txt:
```json
{
  "deepseek_system_prompt": "Your custom instructions here...",
  "deepseek_api_key": "sk-your-key",
  "deepseek_api_base": "https://api.deepseek.com",
  "default_use_external_llm_expansion": true
}
```

### In UI:
1. **Advanced Tab** → "DeepSeek System Prompt"
2. Edit, save, or reset
3. **Main Tab** → Generate images
4. **Below prompt** → View expanded prompt

## Technical Details

### System Prompt Storage
- Stored as string in config.txt
- Loaded during initialization
- Can be updated at runtime
- No restart required

### Expanded Prompt Capture
- Captured in async_worker during generation
- Stored in task.expanded_prompts list
- One entry per image generated
- Displayed after generation completes

### UI Updates
- Accordion visibility controlled by availability
- Shows/hides automatically
- Multiple prompts shown numbered
- Non-editable display field

## Testing

To test the features:

### Test System Prompt
```bash
1. Open Fooocus
2. Go to Advanced tab
3. Expand "DeepSeek System Prompt"
4. Edit the prompt
5. Click "Save System Prompt"
6. Generate an image
7. Verify expansion matches new instructions
```

### Test Expanded Prompt Display
```bash
1. Enable "Use External LLM for Prompt Expansion"
2. Enter simple prompt: "a cat"
3. Click Generate
4. After generation, expand "Extended Prompt" accordion
5. Verify you see the expanded prompt
```

## Migration Notes

### Existing Users
- Default system prompt applied automatically
- No action required
- Existing config.txt will be updated on first run

### New Users
- Default system prompt provided
- Works out of the box
- Can customize immediately

## Future Enhancements

Potential improvements:
- Save multiple system prompt presets
- Quick-switch between presets
- System prompt templates library
- A/B testing different system prompts
- Statistical analysis of expansions
- Export expanded prompts to file

## Related Documentation

- [EXTERNAL_LLM_EXPANSION.md](EXTERNAL_LLM_EXPANSION.md) - Main LLM setup
- [CUSTOM_SYSTEM_PROMPT.md](CUSTOM_SYSTEM_PROMPT.md) - Detailed guide
- [QUICK_START_LLM_EXPANSION.md](QUICK_START_LLM_EXPANSION.md) - Quick start

## Support

If you encounter issues:
1. Check console for error messages
2. Verify API key is valid
3. Test with default system prompt
4. Check config.txt format
5. Restart Fooocus if needed
