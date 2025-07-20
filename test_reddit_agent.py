#!/usr/bin/env python3
"""
Test script for Reddit Content Agent
"""

import os
from dotenv import load_dotenv
from content_agent import SimpleContentAgent

# Load environment variables
load_dotenv()

def test_reddit_basic():
    """Test basic Reddit content generation"""
    print("🧪 Testing Reddit Content Agent...")
    
    # Check if API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with: OPENAI_API_KEY=your_key_here")
        return False
    
    print("✅ API key found")
    
    # Test the agent
    agent = SimpleContentAgent()
    
    # Simple Reddit test
    print("\n📝 Testing Reddit content generation...")
    
    try:
        result = agent.generate_reddit_content(
            topic="budgeting tips for beginners",
            subreddit="personalfinance",
            post_type="first_post"
        )
        print(f"✅ Success! Generated Reddit content:\n{result}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_reddit_advanced():
    """Test advanced Reddit content generation with all parameters"""
    print("\n🧪 Testing Advanced Reddit Content Generation...")
    
    agent = SimpleContentAgent()
    
    try:
        result = agent.generate_reddit_content(
            topic="weight loss transformation",
            subreddit="fitness",
            post_type="first_post",
            persona={
                "type": "expert",
                "credentials": "certified_personal_trainer",
                "tone": "professional_but_relatable",
                "expertise_area": "fitness"
            },
            content_strategy={
                "content_type": "personal_story",
                "viral_hook": "transformation",
                "emotional_trigger": "inspiration",
                "story_arc": "struggle_to_success"
            },
            optimization={
                "title_strategy": {
                    "hook_type": "specific_number",
                    "include_credibility": True
                },
                "content_structure": {
                    "include_tl_dr": True,
                    "use_bullet_points": True
                }
            }
        )
        print(f"✅ Success with advanced parameters! Generated content:\n{result}")
        return True
    except Exception as e:
        print(f"❌ Error with advanced parameters: {e}")
        return False

def test_reddit_comment():
    """Test Reddit comment generation"""
    print("\n🧪 Testing Reddit Comment Generation...")
    
    agent = SimpleContentAgent()
    
    try:
        result = agent.generate_reddit_content(
            topic="advice for new investors",
            subreddit="investing",
            post_type="comment",
            persona={
                "type": "expert",
                "tone": "helpful",
                "expertise_area": "investing"
            }
        )
        print(f"✅ Success! Generated Reddit comment:\n{result}")
        return True
    except Exception as e:
        print(f"❌ Error with comment generation: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Reddit Content Agent Test Suite")
    print("=" * 40)
    
    # Test basic Reddit functionality
    basic_success = test_reddit_basic()
    
    if basic_success:
        # Test advanced functionality
        advanced_success = test_reddit_advanced()
        
        if advanced_success:
            # Test comment generation
            comment_success = test_reddit_comment()
            
            if comment_success:
                print("\n🎉 All Reddit tests passed! Your Reddit content agent is working correctly.")
                print("\nYou can now:")
                print("1. Run 'python content_agent.py' for interactive Reddit mode")
                print("2. Use generate_reddit_content() in your own code")
                print("3. Create viral Reddit posts with optimized parameters")
            else:
                print("\n⚠️ Basic and advanced functionality works, but comment generation has issues.")
        else:
            print("\n⚠️ Basic functionality works, but advanced features have issues.")
    else:
        print("\n❌ Basic Reddit functionality failed. Please check your API key and internet connection.") 