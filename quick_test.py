#!/usr/bin/env python3
"""
Quick test for Reddit Content Agent
"""

from content_agent import SimpleContentAgent

def quick_test():
    print("🚀 Quick Reddit Agent Test")
    print("=" * 30)
    
    agent = SimpleContentAgent()
    
    # Test 1: Basic Reddit post
    print("\n📝 Test 1: Basic Reddit Post")
    result1 = agent.generate_reddit_content(
        topic="budgeting tips for beginners",
        subreddit="personalfinance",
        post_type="first_post"
    )
    print(f"Result: {result1[:300]}..." if len(result1) > 300 else f"Result: {result1}")
    
    # Test 2: Advanced viral post
    print("\n📝 Test 2: Advanced Viral Post")
    result2 = agent.generate_reddit_content(
        topic="weight loss transformation story",
        subreddit="fitness",
        post_type="first_post",
        persona={
            "type": "expert",
            "credentials": "certified_personal_trainer",
            "tone": "professional_but_relatable"
        },
        content_strategy={
            "content_type": "personal_story",
            "viral_hook": "transformation",
            "emotional_trigger": "inspiration"
        }
    )
    print(f"Result: {result2[:300]}..." if len(result2) > 300 else f"Result: {result2}")
    
    print("\n✅ Quick test completed!")

if __name__ == "__main__":
    quick_test() 