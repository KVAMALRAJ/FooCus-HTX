# Custom System Prompt for DeepSeek LLM Expansion

## Overview

You can now customize how DeepSeek expands your prompts by editing the system prompt. This allows you to tailor the expansion behavior to your specific needs.

## Features

### 1. Editable System Prompt
- Customize instructions for how DeepSeek should expand prompts
- Define specific styles, techniques, or quality markers to include
- Control the verbosity and format of expansions

### 2. View Expanded Prompts
- See the actual expanded prompt that was used for generation
- Understand what DeepSeek added to your original prompt
- Learn from the expansions to improve your prompting

## How to Use

### Edit System Prompt

1. Go to **Advanced** tab
2. Find the checkbox "Use External LLM for Prompt Expansion"
3. Below it, expand **"DeepSeek System Prompt"** accordion
4. Edit the system prompt text
5. Click **"Save System Prompt"** to save your changes
6. Click **"Reset to Default"** to restore the original prompt

### View Expanded Prompts

After generating an image with External LLM enabled:

1. Look below your prompt input box
2. Expand **"📝 Extended Prompt (from DeepSeek LLM)"** accordion
3. You'll see the full expanded prompt that was actually used

## Default System Prompt

```
You are an expert at expanding stable diffusion prompts. 
Your task is to take a short image generation prompt and expand it into a detailed, high-quality prompt that will generate better images.

Guidelines:
- Add artistic and technical details (lighting, composition, style, mood)
- Include quality enhancers (highly detailed, masterpiece, best quality, 8k, etc.)
- Maintain the core concept of the original prompt
- Keep it concise but descriptive (aim for 50-100 words)
- Use comma-separated descriptive phrases
- Do NOT add any explanations or commentary, ONLY return the expanded prompt
- Focus on visual details that improve image quality

Example:
Input: "a cat"
Output: "a highly detailed cat, professional photography, natural lighting, detailed fur texture, sharp focus, high resolution, photorealistic, masterpiece quality, sitting pose, warm colors, soft bokeh background"
```

## Customization Examples

### For Artistic Style
```
You are an expert at creating artistic prompts for stable diffusion.
Focus on:
- Artistic movements and styles (impressionism, surrealism, etc.)
- Famous artists' techniques
- Emotional and atmospheric qualities
- Creative compositions and perspectives

Keep expansions artistic and evocative, avoiding technical photography terms.
```

### For Photorealistic Images
```
You are a professional photographer helping create photorealistic image prompts.
Always include:
- Specific lighting conditions (golden hour, studio lighting, etc.)
- Camera and lens details (85mm, f/1.4, etc.)
- Photography techniques (bokeh, depth of field, etc.)
- Professional quality markers

Make every prompt sound like a professional photoshoot brief.
```

### For Anime/Manga Style
```
You are an expert in anime and manga art styles.
Focus on:
- Specific anime art styles (shoujo, seinen, etc.)
- Character expression and pose details
- Typical anime visual elements
- Color palettes common in anime

Avoid photographic terms, focus on illustration and art techniques.
```

### Minimal Expansion
```
You expand prompts minimally, only adding essential quality and technical details.
Rules:
- Add no more than 3-5 additional descriptive phrases
- Focus only on quality markers (masterpiece, high quality, detailed)
- Maintain the original prompt's simplicity
- Do not add artistic interpretation
```

### Maximum Detail
```
You create extremely detailed prompts for stable diffusion.
Include:
- Extensive artistic and technical details
- Multiple quality enhancers
- Specific style references
- Lighting, composition, mood, color palette
- Texture and material descriptions
- Atmosphere and environmental details

Create expansions of 100-150 words with rich descriptive language.
```

## Tips

1. **Be Specific**: The more specific your system prompt, the more consistent your expansions will be

2. **Test and Iterate**: Generate a few images with different system prompts to see what works best

3. **Save Your Favorites**: Keep different system prompts in a text file for different use cases

4. **Check the Output**: Always expand the "Extended Prompt" accordion to see what was actually used

5. **Combine with Styles**: The expanded prompt works together with Fooocus styles for best results

## Technical Details

### Storage
- System prompt is saved to `config.txt`
- Changes take effect immediately (no restart needed)
- The setting persists across sessions

### How It Works
1. You enter a short prompt (e.g., "a cat")
2. If External LLM is enabled, your prompt is sent to DeepSeek
3. DeepSeek uses your system prompt to guide the expansion
4. The expanded prompt is used for actual image generation
5. The expanded prompt is displayed for your review

### Configuration File

In `config.txt`:
```json
{
  "deepseek_system_prompt": "Your custom system prompt here...",
  "deepseek_api_key": "sk-your-key",
  "deepseek_api_base": "https://api.deepseek.com",
  "default_use_external_llm_expansion": true
}
```

## Example Workflow

1. **Start Simple**
   - Input: "a mountain"
   - Check expanded output
   - See what DeepSeek added

2. **Adjust System Prompt**
   - Modify system prompt to emphasize photorealism
   - Save changes

3. **Test Again**
   - Input: "a mountain"
   - Check new expanded output
   - Compare with previous expansion

4. **Refine**
   - Keep adjusting until expansions match your needs
   - Save your favorite system prompts

## Troubleshooting

### Expansions Too Long
Modify system prompt to include:
```
Keep expansions under 50 words
Be concise and focused
```

### Expansions Don't Match Your Style
Add specific style instructions:
```
Always reference [specific artist/style]
Focus on [specific elements]
Avoid [unwanted elements]
```

### Expansions Not Detailed Enough
Modify system prompt:
```
Create highly detailed expansions (100+ words)
Include extensive artistic and technical details
```

## Advanced Usage

### Multiple System Prompts
Keep different system prompts for different projects:

**portrait_system_prompt.txt**
```
You specialize in portrait photography prompts...
```

**landscape_system_prompt.txt**
```
You specialize in landscape photography prompts...
```

Copy and paste as needed.

### Prompt Engineering
Study the expanded prompts to learn:
- What keywords improve quality
- How to structure prompts effectively
- What technical details matter
- Which artistic references work best

## See Also

- [EXTERNAL_LLM_EXPANSION.md](EXTERNAL_LLM_EXPANSION.md) - Main LLM expansion documentation
- [QUICK_START_LLM_EXPANSION.md](QUICK_START_LLM_EXPANSION.md) - Quick setup guide
- DeepSeek API Documentation: https://platform.deepseek.com/docs
