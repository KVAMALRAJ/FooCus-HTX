# Quick Start: External LLM Prompt Expansion

## Installation Steps

### 1. Install Required Package

```bash
# If using pip directly
pip install requests==2.31.0

# OR if using the launch script, it should auto-install from requirements_versions.txt
python launch.py
```

### 2. Add API Key to config.txt

Edit your `config.txt` file (it will be created after first launch if it doesn't exist):

```json
{
  "deepseek_api_key": "sk-your-actual-api-key-here",
  "deepseek_api_base": "https://api.deepseek.com"
}
```

**Note:** The `deepseek_api_base` is optional and defaults to `https://api.deepseek.com`

### 3. Get DeepSeek API Key

1. Visit https://platform.deepseek.com/
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy the key to your `config.txt` file

### 4. Launch Fooocus

```bash
python launch.py
```

### 5. Enable in UI

1. Open the web interface
2. Click on **Advanced** tab
3. Check ☑ **"Use External LLM for Prompt Expansion"**
4. Make sure you have "Fooocus V2" or another expansion style selected

## Test It Out

Try these prompts to see the difference:

**Simple prompt:** `a cat sitting on a chair`

**With External LLM:** You'll get much more detailed expansions with professional photography terms, lighting descriptions, quality enhancers, and artistic details.

**Check Console:** You should see:
```
[External LLM Expansion] DeepSeek API initialized successfully.
[External LLM Expansion] Original: a cat sitting on a chair
[External LLM Expansion] Expanded: [detailed expanded prompt]
```

## Troubleshooting

**No API key warning?**
- Make sure `config.txt` has the `deepseek_api_key` field
- Check that the API key format is correct: `"deepseek_api_key": "sk-..."`
- Verify the JSON syntax in config.txt is valid (no missing commas or quotes)

**Import error for requests?**
```bash
pip install requests
```

**Still using standard expansion?**
- Check the console for error messages
- Verify your API key is valid
- Check internet connection
- Make sure the checkbox is enabled

## Success Indicators

✓ Console shows: `[External LLM Expansion] DeepSeek API initialized successfully`
✓ During generation: `[External LLM Expansion] Using external LLM expansion`
✓ Expanded prompts are longer and more detailed than standard Fooocus expansion

## Need Help?

See full documentation in `EXTERNAL_LLM_EXPANSION.md`
