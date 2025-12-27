# 🧪 Test Examples & Use Cases

This document contains tested examples for the Advanced Research Agent. Use these as templates for your own queries.

## Table of Contents
1. [Mathematical Calculations](#mathematical-calculations)
2. [Fibonacci & Sequences](#fibonacci--sequences)
3. [Data Analysis](#data-analysis)
4. [Research & Web Search](#research--web-search)
5. [PDF Processing](#pdf-processing)
6. [Code Execution](#code-execution)
7. [Complex Multi-Tool Workflows](#complex-multi-tool-workflows)

---

## Mathematical Calculations

### Test 1: Basic Calculator
**Query:**
```
Calculate 2^10 + sqrt(144) * 5
```

**Expected Output:**
- Result: 1084.0
- Explanation of calculation
- Output folder: `outputs/YYYYMMDD_HHMMSS_calculate/`

**Files Created:**
- `session_summary.txt`

---

### Test 2: Scientific Calculations
**Query:**
```
Calculate sin(pi/2) + cos(0) + log10(1000)
```

**Expected Output:**
- Result showing trigonometric and logarithmic calculations
- Step-by-step breakdown

---

## Fibonacci & Sequences

### Test 3: Basic Fibonacci
**Query:**
```
Calculate the first 10 Fibonacci numbers
```

**Expected Output:**
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Files Created:**
- `session_summary.txt`
- Output folder: `outputs/YYYYMMDD_HHMMSS_calculate_first/`

---

### Test 4: Fibonacci with Visualization
**Query:**
```
Calculate the first 15 Fibonacci numbers, then create a line plot showing their growth
```

**Expected Output:**
- Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
- Line plot showing exponential growth
- Plot saved as `fibonacci_plot.png`

**Files Created:**
- `fibonacci_plot.png` - Beautiful line plot with markers
- `session_summary.txt`
- Output folder: `outputs/YYYYMMDD_HHMMSS_calculate_first/`

**Plot Features:**
- X-axis: Index (0-14)
- Y-axis: Fibonacci value
- Grid lines for readability
- Markers at each data point

---

### Test 5: Fibonacci Analysis
**Query:**
```
Generate the first 20 Fibonacci numbers, analyze their growth rate by calculating ratios between consecutive numbers, and create both a line plot of the sequence and a scatter plot of the ratios
```

**Expected Output:**
- Full Fibonacci sequence
- Golden ratio convergence analysis
- Two plots showing sequence and ratio convergence
- Statistical analysis of ratios

**Files Created:**
- `fibonacci_sequence.png`
- `ratio_analysis.png`
- `analysis_results.txt`
- `session_summary.txt`

---

## Data Analysis

### Test 6: Simple Statistical Analysis
**Query:**
```
Analyze these test scores: [85, 92, 78, 95, 88, 76, 91, 89] and provide statistics
```

**Expected Output:**
```
📊 Statistical Summary:
  • Count: 8.00
  • Mean: 86.75
  • Median: 88.50
  • Stdev: 6.52
  • Min: 76.00
  • Max: 95.00
  • Range: 19.00
```

**Files Created:**
- `session_summary.txt`
- Output folder: `outputs/YYYYMMDD_HHMMSS_analyze_these/`

---

### Test 7: Data Analysis with Visualization
**Query:**
```
Analyze the sales data [45, 52, 61, 58, 73, 68, 82, 79, 91, 88] and create a bar chart showing the trend
```

**Expected Output:**
- Statistical summary (mean, median, std dev)
- Bar chart showing sales trend
- Insights about growth pattern

**Files Created:**
- `sales_chart.png`
- `analysis_summary.txt`
- `session_summary.txt`

---

### Test 8: Distribution Analysis
**Query:**
```
Analyze the distribution of these values [12, 15, 18, 19, 22, 23, 25, 28, 30, 32, 35, 38, 40, 42, 45] and create a histogram
```

**Expected Output:**
- Distribution statistics (quartiles, IQR)
- Histogram showing data distribution
- Analysis of spread

**Files Created:**
- `distribution_histogram.png`
- `distribution_analysis.txt`
- `session_summary.txt`

---

## Research & Web Search

### Test 9: Wikipedia Research
**Query:**
```
Research quantum computing on Wikipedia and save a summary
```

**Expected Output:**
- Summary of quantum computing from Wikipedia
- Key concepts extracted
- Saved to text file

**Files Created:**
- `quantum_research.txt`
- `session_summary.txt`
- Output folder: `outputs/YYYYMMDD_HHMMSS_research_quantum/`

---

### Test 10: Web Search & Summary
**Query:**
```
Search the web for recent developments in artificial intelligence and summarize the findings
```

**Expected Output:**
- Web search results from DuckDuckGo
- Summary of recent AI developments
- Sources cited

**Files Created:**
- `ai_developments.txt`
- `session_summary.txt`

---

### Test 11: Research with Visualization
**Query:**
```
Research the top 5 programming languages in 2024 and create a pie chart showing their popularity
```

**Expected Output:**
- List of top 5 languages
- Popularity percentages
- Pie chart visualization

**Files Created:**
- `programming_languages_pie.png`
- `language_research.txt`
- `session_summary.txt`

---

## PDF Processing

### Test 12: Local PDF Reading
**Query:**
```
Read the PDF from /home/user/documents/research_paper.pdf and summarize the main findings
```

**Expected Output:**
- Full text extraction from PDF
- Summary of key findings
- Page count and metadata

**Files Created:**
- `pdf_summary.txt`
- `session_summary.txt`
- Output folder: `outputs/YYYYMMDD_HHMMSS_read_pdf/`

**Note:** Replace path with actual PDF path on your system

---

### Test 13: URL PDF Download
**Query:**
```
Download the PDF from https://arxiv.org/pdf/2301.07041.pdf and extract the abstract
```

**Expected Output:**
- Downloaded PDF saved to output folder
- Text extraction from PDF
- Abstract and key sections identified

**Files Created:**
- `2301.07041.pdf` (downloaded)
- `abstract_summary.txt`
- `session_summary.txt`

---

### Test 14: PDF Analysis
**Query:**
```
Read the PDF at /path/to/paper.pdf, analyze the methodology section, and create a summary
```

**Expected Output:**
- Full PDF text extraction
- Methodology section identified and analyzed
- Structured summary

**Files Created:**
- `methodology_analysis.txt`
- `session_summary.txt`

---

## Code Execution

### Test 15: Simple Code Execution
**Query:**
```
Execute Python code to print the squares of numbers from 1 to 10
```

**Expected Output:**
```
1 squared = 1
2 squared = 4
3 squared = 9
...
10 squared = 100
```

**Files Created:**
- `session_summary.txt`

---

### Test 16: Factorial Calculation
**Query:**
```
Write and execute code to calculate the factorial of 10
```

**Expected Output:**
- Code execution result
- Factorial value: 3628800
- Explanation

---

### Test 17: Prime Numbers
**Query:**
```
Execute code to find all prime numbers between 1 and 50 and display them
```

**Expected Output:**
- List of prime numbers
- Count of primes found
- Code execution confirmation

---

## Complex Multi-Tool Workflows

### Test 18: Complete Research Report
**Query:**
```
Research machine learning on Wikipedia, calculate how many neurons would be in a 4-layer neural network with sizes [784, 256, 128, 10], create a bar chart of layer sizes, and save everything to a report
```

**Expected Output:**
- Wikipedia research on ML
- Neural network parameter calculation
- Bar chart of layer architecture
- Complete report file

**Files Created:**
- `neural_network_architecture.png`
- `ml_research_report.txt`
- `session_summary.txt`
- Output folder: `outputs/YYYYMMDD_HHMMSS_research_machine/`

**Tools Used:**
- wiki_tool
- calculator_tool
- plot_tool
- save_tool

---

### Test 19: Data Science Pipeline
**Query:**
```
Generate a dataset of 50 random numbers between 1 and 100 using code, perform statistical analysis, create both a histogram and a box plot equivalent, and save all results
```

**Expected Output:**
- Random dataset generated
- Statistical analysis (mean, median, std dev, quartiles)
- Two visualizations
- Complete analysis report

**Files Created:**
- `histogram.png`
- `distribution_plot.png`
- `statistical_analysis.txt`
- `session_summary.txt`

**Tools Used:**
- code_executor_tool
- data_analysis_tool
- plot_tool
- save_tool

---

### Test 20: Financial Analysis
**Query:**
```
Calculate compound interest for $10,000 at 5% annual rate for 10 years, show yearly values, create a line plot of growth, perform statistical analysis on the yearly gains, and save everything
```

**Expected Output:**
- Year-by-year values
- Line plot showing investment growth
- Statistical analysis of yearly gains
- Total return calculation

**Files Created:**
- `investment_growth.png`
- `financial_analysis.txt`
- `session_summary.txt`

**Tools Used:**
- calculator_tool or code_executor_tool
- plot_tool
- data_analysis_tool
- save_tool

---

## Tips for Testing

1. **Start Simple**: Begin with Test 1-5 to verify basic functionality
2. **Check Outputs**: Always verify files are created in `outputs/` folder
3. **Test PDF Tools**: Use actual PDF files on your system for Tests 12-14
4. **Iterate**: If a test fails, try rephrasing the query
5. **Combine Tools**: The agent works best when combining multiple tools

## Success Criteria

For each test, verify:
- ✅ Agent completes without errors
- ✅ Output folder created with correct naming
- ✅ `session_summary.txt` exists
- ✅ Expected files (plots, text files) are generated
- ✅ Content is accurate and well-formatted
- ✅ No matplotlib threading warnings

## Troubleshooting

**Issue**: Agent makes too many tool calls
- **Solution**: Be more specific in your query

**Issue**: Plots not generated
- **Solution**: Check that matplotlib backend is set to 'Agg' in tools.py

**Issue**: PDF reading fails
- **Solution**: Ensure PyPDF2 is installed and PDF path is correct

**Issue**: Recursion limit reached
- **Solution**: Already set to 50 in main.py, increase if needed

---

## Template for Adding New Tests

```markdown
### Test N: [Test Name]
**Query:**
```
[Your query here]
```

**Expected Output:**
- [Expected result 1]
- [Expected result 2]

**Files Created:**
- `filename.ext`
- `session_summary.txt`

**Tools Used:**
- tool_name_1
- tool_name_2
```

Happy testing! 🎉