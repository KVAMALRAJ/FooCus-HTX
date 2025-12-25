# Quick Start: External LLM Prompt Expansion

## Installation Steps

### 1. Install Required Package

```bash
# If using pip directly
pip install requests==2.31.0

# OR if using the launch script, it should auto-install from requirements_versions.txt
python launch.py
```

### 2. Create .env File

Create a file named `.env` in the Fooocus root directory:

```bash
# Copy the example
cp .env.example .env

# Edit the file
nano .env  # or use your favorite text editor
```

Add your DeepSeek API key:

```env
DEEPSEEK_API_KEY=sk-your-actual-api-key-here
DEEPSEEK_API_BASE=https://api.deepseek.com
```

### 3. Get DeepSeek API Key

1. Visit https://platform.deepseek.com/
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

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
- Make sure `.env` file is in the root directory (same folder as launch.py)
- Check that the file is named exactly `.env` (not `.env.txt`)
- Verify the API key format: `DEEPSEEK_API_KEY=sk-...`

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
