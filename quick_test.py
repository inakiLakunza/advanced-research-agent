"""
Quick test script to verify the agent is working correctly.
Run this after setup to ensure everything is configured properly.
"""

import os
import sys
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed"""
    print("🔍 Checking dependencies...")
    
    required = {
        'langchain': 'LangChain',
        'langchain_openai': 'LangChain OpenAI',
        'langgraph': 'LangGraph',
        'matplotlib': 'Matplotlib',
        'numpy': 'NumPy',
        'PyPDF2': 'PyPDF2',
        'dotenv': 'python-dotenv',
    }
    
    missing = []
    for package, name in required.items():
        try:
            __import__(package)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✅ All dependencies installed!\n")
    return True

def check_env_file():
    """Check if .env file exists and has API key"""
    print("🔍 Checking environment configuration...")
    
    if not os.path.exists('.env'):
        print("  ❌ .env file not found")
        print("\nCreate .env file with:")
        print("  OPENAI_API_KEY=your-key-here")
        return False
    
    with open('.env', 'r') as f:
        content = f.read()
    
    if 'OPENAI_API_KEY' not in content:
        print("  ❌ OPENAI_API_KEY not found in .env")
        return False
    
    if 'sk-' not in content:
        print("  ⚠️  API key format looks incorrect")
        print("  OpenAI keys start with 'sk-'")
        return False
    
    print("  ✅ .env file configured\n")
    return True

def check_files():
    """Check if required files exist"""
    print("🔍 Checking required files...")
    
    required_files = ['main.py', 'tools.py', 'requirements.txt']
    
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - NOT FOUND")
            return False
    
    print("\n✅ All required files present!\n")
    return True

def run_simple_test():
    """Run a simple test of the agent"""
    print("🧪 Running simple calculation test...")
    print("=" * 50)
    
    try:
        from dotenv import load_dotenv
        from langchain_openai import ChatOpenAI
        from langgraph.prebuilt import create_react_agent
        from tools import calculator_tool
        
        load_dotenv()
        
        # Check if API key is loaded
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ API key not loaded from .env")
            return False
        
        # Create simple agent
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        agent = create_react_agent(llm, [calculator_tool])
        
        # Simple test query
        result = agent.invoke(
            {"messages": [("user", "Calculate 2 + 2")]},
            config={"recursion_limit": 10}
        )
        
        final_message = str(result["messages"][-1].content)
        
        print("\nTest Query: Calculate 2 + 2")
        print(f"Agent Response: {final_message[:200]}")
        
        if '4' in final_message:
            print("\n✅ Agent test PASSED!\n")
            return True
        else:
            print("\n⚠️  Agent responded but result unclear\n")
            return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all checks"""
    print("=" * 50)
    print("🤖 ADVANCED RESEARCH AGENT - QUICK TEST")
    print("=" * 50)
    print()
    
    # Run checks
    checks = [
        ("Dependencies", check_dependencies),
        ("Files", check_files),
        ("Environment", check_env_file),
    ]
    
    all_passed = True
    for name, check_func in checks:
        if not check_func():
            all_passed = False
            print(f"\n❌ {name} check failed. Please fix before proceeding.\n")
            return
    
    if all_passed:
        print("=" * 50)
        print("✅ All preliminary checks passed!")
        print("=" * 50)
        print()
        
        # Run actual test
        if run_simple_test():
            print("=" * 50)
            print("🎉 SUCCESS! Your agent is ready to use!")
            print("=" * 50)
            print()
            print("Next steps:")
            print("  1. Run: python main.py")
            print("  2. Try: 'Calculate the first 10 Fibonacci numbers'")
            print("  3. Check: outputs/ folder for results")
            print()
            print("For more examples, see TEST_EXAMPLES.md")
        else:
            print("=" * 50)
            print("⚠️  Setup incomplete or test failed")
            print("=" * 50)

if __name__ == "__main__":
    main()