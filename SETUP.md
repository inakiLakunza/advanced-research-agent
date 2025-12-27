# 🚀 Complete Setup Guide

Step-by-step instructions to get the Advanced Research Agent running on your system.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- 500MB free disk space (for dependencies and outputs)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/inakiLakunza/advanced-research-agent.git
cd advanced-research-agent
```

### 2. Create Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected installation time:** 2-5 minutes

**Packages installed:**
- LangChain & LangGraph (agent framework)
- OpenAI integration
- Matplotlib & NumPy (visualization)
- PyPDF2 (PDF processing)
- DuckDuckGo search
- Wikipedia API
- And more...

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env  # Linux/Mac
# OR
type nul > .env  # Windows
```

Add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Important:**
- Never commit your `.env` file to Git
- Keep your API key secret
- The `.gitignore` file already excludes `.env`

### 5. Verify Installation

Test that everything is installed correctly:

```bash
python -c "import langchain; import matplotlib; import PyPDF2; print('✅ All dependencies installed!')"
```

If you see the success message, you're ready!

### 6. Run Your First Test

```bash
python main.py
```

When prompted, try this simple query:
```
Calculate 2 + 2
```

You should see:
- ✅ Agent processes the query
- ✅ Output folder created in `outputs/`
- ✅ Result: 4
- ✅ Session summary saved

## Troubleshooting

### Issue: ImportError for PyPDF2

**Solution:**
```bash
pip install --upgrade PyPDF2
```

### Issue: Matplotlib backend warnings

**Solution:**
Already handled in `tools.py` with `matplotlib.use('Agg')`

### Issue: OpenAI API key not found

**Solution:**
1. Check `.env` file exists
2. Verify key format: `OPENAI_API_KEY=sk-...`
3. Ensure no spaces around the `=`
4. Try restarting your terminal

### Issue: DuckDuckGo search fails

**Solution:**
```bash
pip install --upgrade duckduckgo-search
```

### Issue: Permission denied when creating folders

**Solution:**
```bash
mkdir outputs  # Create manually
chmod 755 outputs  # Set permissions (Linux/Mac)
```

## Directory Structure

After setup, your directory should look like:

```
advanced-research-agent/
├── main.py                 # Entry point
├── tools.py                # Tool definitions
├── requirements.txt        # Dependencies
├── .env                    # Your API key (create this)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── SETUP.md               # This file
├── TEST_EXAMPLES.md       # Test cases
├── venv/                  # Virtual environment
└── outputs/               # Generated outputs (auto-created)
    └── 20241227_120000_test/
        ├── session_summary.txt
        └── ...
```

## Verification Checklist

Before using the agent, verify:

- [ ] Virtual environment activated (`(venv)` in prompt)
- [ ] All packages installed without errors
- [ ] `.env` file created with valid API key
- [ ] `python main.py` runs without import errors
- [ ] `outputs/` folder created automatically
- [ ] Test query produces expected results

## Next Steps

1. **Read the README**: `README.md` for feature overview and working examples
2. **Try Examples** Check `README.md` , [outputs](outputs/) folder or `TEST_EXAMPLES.md` for tested queries
3. **Customize**: Modify `tools.py` to add your own tools
4. **Experiment**: Try complex multi-tool workflows

## Updating

To update dependencies:

```bash
pip install --upgrade -r requirements.txt
```

To pull latest changes:

```bash
git pull origin main
pip install -r requirements.txt  # Install any new dependencies
```

## Uninstallation

To remove everything:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv  # Linux/Mac
# OR
rmdir /s venv  # Windows

# Remove outputs (optional)
rm -rf outputs

# Remove the directory
cd ..
rm -rf advanced-research-agent
```

## Getting Help

If you encounter issues:

1. Check real examples in [README.md](README.md) or in [outputs](outputs/), otherwise there are nice ideas in [TEST_EXAMPLES.md](TEST_EXAMPLES.md)
2. Review error messages carefully
3. Ensure API key is valid and has credits
4. Check internet connection (for web searches)
5. Open an issue on GitHub

## Common Configuration Changes

### Change Model

Edit `main.py`:
```python
llm = ChatOpenAI(
    model="gpt-4",  # Change from gpt-4o-mini
    temperature=0.7,
    max_tokens=2000
)
```

### Increase Recursion Limit

Edit `main.py`:
```python
config={"recursion_limit": 100}  # Increase from 50
```

### Change Output Folder Location

Edit `main.py`, modify `create_output_folder()`:
```python
if not os.path.exists("my_outputs"):  # Change folder name
    os.makedirs("my_outputs")
```

## Performance Tips

1. **API Usage**: GPT-4o-mini is cost-effective for most tasks
2. **Recursion Limit**: Higher limits = more tool calls = higher costs
3. **Output Management**: Regularly clean `outputs/` folder
4. **Batch Operations**: Combine related queries in one session

## Security Notes

- ✅ `.env` file is git-ignored
- ✅ Code execution is sandboxed
- ✅ No external file system access in code executor
- ⚠️ Don't share your API key
- ⚠️ Review costs on OpenAI dashboard

---

**Setup complete!** 🎉 You're ready to use the Advanced Research Agent.

For usage examples, see real examples in [README.md](README.md) or in [outputs](outputs/), otherwise there are nice ideas in [TEST_EXAMPLES.md](TEST_EXAMPLES.md).
