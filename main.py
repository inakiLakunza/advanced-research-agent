from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools import (
    save_tool, 
    search_tool, 
    wiki_tool,
    calculator_tool,
    plot_tool,
    data_analysis_tool,
    file_reader_tool,
    code_executor_tool,
    weather_tool,
    summarize_tool,
    pdf_reader_tool,
    url_pdf_reader_tool
)
import os
from datetime import datetime
import re

load_dotenv()

def create_output_folder(query: str) -> str:
    """
    Create a unique output folder for this session.
    Format: outputs/{DATE}_{TOPIC_IN_TWO_WORDS}
    """
    # Create outputs directory if it doesn't exist
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    
    # Get current date
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Extract topic (first 2-3 meaningful words)
    words = re.findall(r'\b[a-zA-Z]+\b', query.lower())
    # Filter out common words
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    meaningful_words = [w for w in words if w not in stopwords][:2]
    
    if not meaningful_words:
        topic = "task"
    else:
        topic = "_".join(meaningful_words)
    
    # Create folder name
    folder_name = f"{date_str}_{topic}"
    folder_path = os.path.join("outputs", folder_name)
    
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    
    return folder_path

def main():
    # Initialize LLM with better configuration
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=2000
    )
    
    # Comprehensive tool list
    tools = [
        save_tool,
        search_tool,
        wiki_tool,
        calculator_tool,
        plot_tool,
        data_analysis_tool,
        file_reader_tool,
        code_executor_tool,
        weather_tool,
        summarize_tool,
        pdf_reader_tool,
        url_pdf_reader_tool
    ]
    
    # Create agent with tools
    agent = create_react_agent(llm, tools)
    
    system_prompt = """
You are an advanced research and analysis assistant with multiple capabilities.

AVAILABLE TOOLS:
1. wiki_tool: Query Wikipedia for information
2. search_tool: Search the web using DuckDuckGo
3. save_tool: Save content to a text file (params: data, filename)
4. calculator_tool: Perform mathematical calculations (params: expression)
5. plot_tool: Create data visualizations (params: data_dict, plot_type, title, filename)
6. data_analysis_tool: Analyze datasets and compute statistics (params: data, analysis_type)
7. file_reader_tool: Read content from existing text files (params: filename)
8. code_executor_tool: Execute Python code safely (params: code)
9. weather_tool: Get current weather information (params: location)
10. summarize_tool: Summarize long text content (params: text, max_length)
11. pdf_reader_tool: Read and extract text from PDF files (params: pdf_path)
12. url_pdf_reader_tool: Download and read PDF from URL (params: url)

INSTRUCTIONS:
- Use the appropriate tools to complete the user's request
- For calculations or code: use calculator_tool or code_executor_tool
- For data visualization: use plot_tool with proper JSON format
- For file operations: use save_tool or file_reader_tool
- For PDF files: use pdf_reader_tool (local) or url_pdf_reader_tool (URL)
- Chain tools together when needed for complex tasks
- After completing the task, provide a clear summary of what you did

IMPORTANT:
- All output files (plots, saved data) will be automatically saved to: {output_folder}
- When using save_tool or plot_tool, just provide the filename (e.g., "results.txt")
- The system will automatically place it in the correct output folder
- For plots, use descriptive filenames like "fibonacci_growth.png"

IMPORTANT FOR PLOTS:
- The data_dict parameter must be a valid JSON string
- Example: '{{"x": [1,2,3], "y": [4,5,6]}}'
- For bar charts: '{{"labels": ["A","B","C"], "values": [10,20,30]}}'

Be efficient and direct. Complete the task, then summarize your actions.
"""
    
    print("=" * 70)
    print("🤖 ADVANCED RESEARCH AGENT")
    print("=" * 70)
    print("\n✨ New Features:")
    print("  • Automatic output folder organization")
    print("  • PDF reading (local files & URLs)")
    print("  • All outputs saved in: outputs/{DATE}_{TOPIC}/")
    print("\n🔧 Capabilities:")
    print("  • Web & Wikipedia Research")
    print("  • Mathematical Calculations")
    print("  • Data Visualization & Analysis")
    print("  • File Operations (Read/Write)")
    print("  • Code Execution")
    print("  • PDF Document Processing")
    print("  • Weather Information")
    print("  • Text Summarization")
    print("\n📝 Examples:")
    print("  - 'Calculate the first 10 Fibonacci numbers'")
    print("  - 'Generate Fibonacci sequence and create a plot'")
    print("  - 'Research quantum computing and summarize'")
    print("  - 'Read PDF from path /path/to/file.pdf and summarize'")
    print("  - 'Download PDF from https://example.com/paper.pdf and analyze'")
    print("=" * 70)
    
    user_input = input("\n📝 Enter your query: ")
    
    try:
        # Create output folder for this session
        output_folder = create_output_folder(user_input)
        print(f"\n📁 Output folder created: {output_folder}")
        
        # Set output folder as environment variable for tools to use
        os.environ['AGENT_OUTPUT_FOLDER'] = output_folder
        
        # Combine system prompt with user query
        full_query = system_prompt.replace("{output_folder}", output_folder) + f"\n\nUser request: {user_input}"
        
        print("\n⚙️  Processing your request...\n")
        
        # Invoke agent with increased recursion limit
        result = agent.invoke(
            {"messages": [("user", full_query)]},
            config={"recursion_limit": 50}
        )
        
        # Display agent reasoning steps
        print("\n" + "=" * 70)
        print("🔍 AGENT EXECUTION TRACE:")
        print("=" * 70)
        
        tool_calls = 0
        for i, message in enumerate(result["messages"], 1):
            if hasattr(message, 'content') and message.content:
                content = str(message.content)
                # Show tool usage
                if any(keyword in content.lower() for keyword in ['tool', 'result', 'executed', 'saved']):
                    tool_calls += 1
                    # Truncate long content
                    display_content = content[:200] + "..." if len(content) > 200 else content
                    print(f"\n[Step {i}] {display_content}")
        
        # Get the final message
        final_message = result["messages"][-1].content
        
        print("\n" + "=" * 70)
        print("📊 FINAL RESULTS:")
        print("=" * 70)
        print(f"\n{final_message}")
        
        # Create a summary file
        summary_path = os.path.join(output_folder, "session_summary.txt")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"Agent Session Summary\n")
            f.write(f"{'=' * 50}\n\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"User Query:\n{user_input}\n\n")
            f.write(f"{'=' * 50}\n\n")
            f.write(f"Agent Response:\n{final_message}\n\n")
            f.write(f"{'=' * 50}\n\n")
            f.write(f"Tool Calls: {tool_calls}\n")
            f.write(f"Output Folder: {output_folder}\n")
        
        print("\n" + "=" * 70)
        print(f"✅ Task completed successfully!")
        print(f"📁 All outputs saved to: {output_folder}")
        print(f"📄 Session summary: {summary_path}")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()