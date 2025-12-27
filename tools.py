from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
import json
import ast
import operator
import statistics
from typing import Dict, Any, List
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to avoid threading issues
import matplotlib.pyplot as plt
import numpy as np
import os

# Helper function to get output folder
def get_output_folder():
    """Get the current output folder from environment variable"""
    return os.environ.get('AGENT_OUTPUT_FOLDER', '.')

# ---------------------------
# Save Tool
# ---------------------------
@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves structured research data to a text file in the output folder.
    
    Args:
        data: The content to save
        filename: Name of the file (default: research_output.txt)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
        f"{'=' * 50}\n\n"
    )
    
    try:
        # Use output folder
        output_folder = get_output_folder()
        filepath = os.path.join(output_folder, filename)
        
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(formatted_text)
        return f"✅ Data successfully saved to {filepath}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"

# ---------------------------
# Search Tool
# ---------------------------
_ddg = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """
    Search the web for information using DuckDuckGo.
    
    Args:
        query: The search query
    """
    try:
        result = _ddg.run(query)
        return result
    except Exception as e:
        return f"Search error: {str(e)}"

# ---------------------------
# Wikipedia Tool
# ---------------------------
_api_wrapper = WikipediaAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=500,
)
_wiki = WikipediaQueryRun(api_wrapper=_api_wrapper)

@tool
def wiki_tool(query: str) -> str:
    """
    Query Wikipedia for summary information.
    
    Args:
        query: The topic to search on Wikipedia
    """
    try:
        return _wiki.run(query)
    except Exception as e:
        return f"Wikipedia error: {str(e)}"

# ---------------------------
# Calculator Tool
# ---------------------------
@tool
def calculator_tool(expression: str) -> str:
    """
    Perform mathematical calculations. Supports basic arithmetic, powers, and common math functions.
    
    Args:
        expression: Math expression like "2 + 2", "sqrt(16)", "3**4", "log(100)"
    
    Examples:
        - "5 * 8 + 12"
        - "sqrt(144)"
        - "2**10"
        - "sin(pi/2)"
    """
    safe_functions = {
        'sqrt': np.sqrt,
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'log': np.log,
        'log10': np.log10,
        'abs': abs,
        'round': round,
        'pi': np.pi,
        'e': np.e,
    }
    
    try:
        # Replace function calls with numpy equivalents
        expr = expression.lower()
        for func_name in safe_functions:
            expr = expr.replace(func_name, f'safe_functions["{func_name}"]')
        
        # Evaluate safely
        result = eval(expr, {"__builtins__": {}}, safe_functions)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}. Please check your expression."

# ---------------------------
# Plot Tool
# ---------------------------
@tool
def plot_tool(data_dict: str, plot_type: str = "line", title: str = "Data Visualization", filename: str = "plot.png") -> str:
    """
    Create data visualizations and save them as PNG files in the output folder.
    
    Args:
        data_dict: JSON string with data, e.g., '{"x": [1,2,3], "y": [4,5,6]}'
        plot_type: Type of plot - "line", "bar", "scatter", "pie", "histogram"
        title: Title of the plot
        filename: Output filename (default: plot.png)
    
    Examples:
        - data_dict='{"labels": ["A","B","C"], "values": [10,20,30]}', plot_type="bar"
        - data_dict='{"x": [1,2,3,4], "y": [1,4,9,16]}', plot_type="scatter"
    """
    try:
        # Parse data
        data = json.loads(data_dict)
        
        # Create figure with non-interactive backend
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if plot_type == "line":
            x_data = data.get("x", list(range(len(data["y"]))))
            ax.plot(x_data, data["y"], marker='o', linewidth=2, markersize=8)
            ax.set_xlabel(data.get("xlabel", "X"), fontsize=12)
            ax.set_ylabel(data.get("ylabel", "Y"), fontsize=12)
            ax.grid(True, alpha=0.3)
            
        elif plot_type == "bar":
            labels = data.get("labels", data.get("x", []))
            values = data.get("values", data.get("y", []))
            ax.bar(labels, values, color='skyblue', edgecolor='navy', alpha=0.7)
            ax.set_xlabel(data.get("xlabel", "Categories"), fontsize=12)
            ax.set_ylabel(data.get("ylabel", "Values"), fontsize=12)
            plt.xticks(rotation=45, ha='right')
            ax.grid(True, alpha=0.3, axis='y')
            
        elif plot_type == "scatter":
            ax.scatter(data["x"], data["y"], alpha=0.6, s=100, c='coral', edgecolors='darkred')
            ax.set_xlabel(data.get("xlabel", "X"), fontsize=12)
            ax.set_ylabel(data.get("ylabel", "Y"), fontsize=12)
            ax.grid(True, alpha=0.3)
            
        elif plot_type == "pie":
            labels = data.get("labels", [])
            values = data.get("values", [])
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            
        elif plot_type == "histogram":
            ax.hist(data["values"], bins=data.get("bins", 10), 
                   color='lightgreen', edgecolor='darkgreen', alpha=0.7)
            ax.set_xlabel(data.get("xlabel", "Values"), fontsize=12)
            ax.set_ylabel(data.get("ylabel", "Frequency"), fontsize=12)
            ax.grid(True, alpha=0.3, axis='y')
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        # Save to output folder
        output_folder = get_output_folder()
        filepath = os.path.join(output_folder, filename)
        
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close(fig)
        
        return f"✅ Plot saved successfully as {filepath}"
    except Exception as e:
        plt.close('all')
        return f"❌ Plotting error: {str(e)}"

# ---------------------------
# Data Analysis Tool
# ---------------------------
@tool
def data_analysis_tool(data: str, analysis_type: str = "summary") -> str:
    """
    Analyze datasets and compute statistics.
    
    Args:
        data: JSON string with numeric data, e.g., '[1, 2, 3, 4, 5]'
        analysis_type: Type of analysis - "summary", "correlation", "distribution"
    
    Returns statistical analysis of the data
    """
    try:
        dataset = json.loads(data)
        
        if not isinstance(dataset, list):
            return "Error: Data must be a list of numbers"
        
        if analysis_type == "summary":
            result = {
                "count": len(dataset),
                "mean": statistics.mean(dataset),
                "median": statistics.median(dataset),
                "stdev": statistics.stdev(dataset) if len(dataset) > 1 else 0,
                "min": min(dataset),
                "max": max(dataset),
                "range": max(dataset) - min(dataset)
            }
            
            output = "📊 Statistical Summary:\n"
            for key, value in result.items():
                output += f"  • {key.capitalize()}: {value:.2f}\n"
            return output
            
        elif analysis_type == "distribution":
            sorted_data = sorted(dataset)
            n = len(sorted_data)
            q1 = sorted_data[n//4]
            q2 = statistics.median(sorted_data)
            q3 = sorted_data[3*n//4]
            
            return f"""📊 Distribution Analysis:
  • Q1 (25th percentile): {q1:.2f}
  • Q2 (Median): {q2:.2f}
  • Q3 (75th percentile): {q3:.2f}
  • IQR: {q3 - q1:.2f}
"""
        
        return "Analysis complete"
        
    except Exception as e:
        return f"❌ Analysis error: {str(e)}"

# ---------------------------
# File Reader Tool
# ---------------------------
@tool
def file_reader_tool(filename: str) -> str:
    """
    Read content from existing text files.
    
    Args:
        filename: Name of the file to read (can be full path or relative)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"📄 Content of {filename}:\n\n{content}"
    except FileNotFoundError:
        return f"❌ File '{filename}' not found"
    except Exception as e:
        return f"❌ Error reading file: {str(e)}"

# ---------------------------
# Code Executor Tool
# ---------------------------
@tool
def code_executor_tool(code: str) -> str:
    """
    Execute simple Python code safely (limited operations for security).
    
    Args:
        code: Python code to execute (limited to safe operations)
    
    Example: "fib = [0, 1]\\nfor i in range(8): fib.append(fib[-1] + fib[-2])\\nprint(fib)"
    """
    try:
        safe_dict = {
            '__builtins__': {
                'print': print,
                'len': len,
                'range': range,
                'sum': sum,
                'max': max,
                'min': min,
                'abs': abs,
                'round': round,
                'sorted': sorted,
                'list': list,
                'dict': dict,
                'str': str,
                'int': int,
                'float': float,
            },
        }
        
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        exec(code, safe_dict)
        
        sys.stdout = old_stdout
        output = buffer.getvalue()
        
        if not output:
            result_vars = {k: v for k, v in safe_dict.items() 
                          if not k.startswith('_') and k != '__builtins__'}
            if result_vars:
                output = "Variables created:\n" + "\n".join(f"{k} = {v}" for k, v in result_vars.items())
        
        return f"✅ Code executed successfully:\n{output if output else 'Code executed with no output'}"
    except Exception as e:
        return f"❌ Execution error: {str(e)}"

# ---------------------------
# Weather Tool
# ---------------------------
@tool
def weather_tool(location: str) -> str:
    """
    Get current weather information for a location.
    Note: This is a simulated tool. In production, integrate with a real weather API.
    
    Args:
        location: City or location name
    """
    import random
    
    conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Clear"]
    temp = random.randint(10, 30)
    condition = random.choice(conditions)
    humidity = random.randint(40, 80)
    
    return f"""🌤️ Weather for {location}:
  • Temperature: {temp}°C
  • Condition: {condition}
  • Humidity: {humidity}%
  
Note: For real-time data, integrate with OpenWeatherMap or similar API
"""

# ---------------------------
# Summarize Tool
# ---------------------------
@tool
def summarize_tool(text: str, max_length: int = 150) -> str:
    """
    Summarize long text content.
    
    Args:
        text: The text to summarize
        max_length: Maximum words in summary (default: 150)
    """
    try:
        words = text.split()
        
        if len(words) <= max_length:
            return f"Text is already short ({len(words)} words):\n{text}"
        
        first_part = ' '.join(words[:max_length//2])
        last_part = ' '.join(words[-(max_length//2):])
        
        summary = f"{first_part} [...] {last_part}"
        
        return f"""📝 Summary ({len(summary.split())} words from {len(words)} words):

{summary}

Original length: {len(words)} words
Summary length: {len(summary.split())} words
"""
    except Exception as e:
        return f"❌ Summarization error: {str(e)}"

# ---------------------------
# PDF Reader Tool (Local Files)
# ---------------------------
@tool
def pdf_reader_tool(pdf_path: str) -> str:
    """
    Read and extract text from a local PDF file.
    
    Args:
        pdf_path: Full path to the PDF file (e.g., /home/user/document.pdf)
    
    Example: pdf_path="/home/user/research_paper.pdf"
    """
    try:
        import PyPDF2
        
        if not os.path.exists(pdf_path):
            return f"❌ PDF file not found: {pdf_path}"
        
        text_content = []
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text_content.append(page.extract_text())
        
        full_text = "\n\n".join(text_content)
        
        return f"""📄 PDF Content Extracted:
File: {pdf_path}
Pages: {num_pages}

Content:
{full_text[:2000]}{'...' if len(full_text) > 2000 else ''}

Total characters: {len(full_text)}
"""
    except ImportError:
        return "❌ PyPDF2 not installed. Install with: pip install PyPDF2"
    except Exception as e:
        return f"❌ Error reading PDF: {str(e)}"

# ---------------------------
# URL PDF Reader Tool
# ---------------------------
@tool
def url_pdf_reader_tool(url: str) -> str:
    """
    Download and read a PDF from a URL.
    
    Args:
        url: URL of the PDF file (e.g., https://example.com/paper.pdf)
    
    Example: url="https://arxiv.org/pdf/1234.5678.pdf"
    """
    try:
        import PyPDF2
        import requests
        from io import BytesIO
        
        # Download PDF
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Read PDF from bytes
        pdf_file = BytesIO(response.content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        num_pages = len(pdf_reader.pages)
        text_content = []
        
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text_content.append(page.extract_text())
        
        full_text = "\n\n".join(text_content)
        
        # Save PDF to output folder
        output_folder = get_output_folder()
        filename = url.split('/')[-1] or "downloaded.pdf"
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        
        pdf_path = os.path.join(output_folder, filename)
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        
        return f"""📄 PDF Downloaded and Extracted:
URL: {url}
Saved to: {pdf_path}
Pages: {num_pages}

Content Preview:
{full_text[:2000]}{'...' if len(full_text) > 2000 else ''}

Total characters: {len(full_text)}
"""
    except ImportError:
        return "❌ Required libraries not installed. Install with: pip install PyPDF2 requests"
    except Exception as e:
        return f"❌ Error downloading/reading PDF: {str(e)}"