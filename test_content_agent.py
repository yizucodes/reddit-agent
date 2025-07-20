#!/usr/bin/env python3
"""
Simple test script for the Content Agent
"""

import os
from dotenv import load_dotenv
from content_agent import SimpleContentAgent, example_usage

# Load environment variables
load_dotenv()

def test_basic_functionality():
    """Test basic content generation"""
    print("🧪 Testing Content Agent...")
    
    # Check if API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with: OPENAI_API_KEY=your_key_here")
        return False
    
    print("✅ API key found")
    
    # Test the agent
    agent = SimpleContentAgent()
    
    # Simple test prompt
    test_prompt = "Write a short Instagram caption for a sunset photo"
    print(f"\n📝 Testing with prompt: {test_prompt}")
    
    try:
        result = agent.generate_content(test_prompt)
        print(f"✅ Success! Generated content:\n{result}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_with_context():
    """Test the enhanced context functionality"""
    print("\n🧪 Testing with context...")
    
    agent = SimpleContentAgent()
    
    prompt = "Write a social media post"
    context = {
        "platform": "LinkedIn",
        "audience": "professionals",
        "tone": "professional",
        "length": "short"
    }
    
    try:
        result = agent.generate_with_context(prompt, context)
        print(f"✅ Success with context! Generated content:\n{result}")
        return True
    except Exception as e:
        print(f"❌ Error with context: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Content Agent Test Suite")
    print("=" * 40)
    
    # Test basic functionality
    basic_success = test_basic_functionality()
    
    if basic_success:
        # Test with context
        context_success = test_with_context()
        
        if context_success:
            print("\n🎉 All tests passed! Your content agent is working correctly.")
            print("\nYou can now:")
            print("1. Run 'python content_agent.py' for interactive mode")
            print("2. Use the agent in your own code")
            print("3. Uncomment example_usage() in content_agent.py to see more examples")
        else:
            print("\n⚠️ Basic functionality works, but context feature has issues.")
    else:
        print("\n❌ Basic functionality failed. Please check your API key and internet connection.") 