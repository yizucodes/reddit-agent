#!/usr/bin/env python3
"""
Minimal Reddit Agent - Post & Comment Generation Only
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()

class RedditAgent:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # System prompt for Reddit posts
        self.post_system_prompt = """
        You are a Reddit content creation expert with 20 years of experience in viral content.
        
        Your expertise:
        - Creating viral Reddit posts that get thousands of upvotes
        - Understanding subreddit cultures and rules
        - Crafting engaging titles and content
        - Using Reddit formatting effectively
        
        Always create:
        - Compelling titles that hook readers
        - Well-structured content with clear value
        - Platform-appropriate formatting
        - Engaging conclusions that encourage comments

        Create a post also based on the analysis:
        Analysis of the last 24 hours of Reddit RoastMe data reveals that the most successful roasts are concise, creatively sarcastic, and lean heavily on dry, deadpan humor. Comments that anthropomorphize boredom or mediocrity, or use clever analogies, consistently receive the highest upvotes. Posts with self-deprecating or relatable titles and body text that invite brutal honesty tend to generate more comments. For maximum engagement, both posters and commenters should focus on relatability, originality, and a balance of wit and subtlety.

        """
        
        # NEW: Comment-specific system prompt
        self.comment_system_prompt = """
        You are a legendary Reddit commenter known for witty, concise responses that consistently get hundreds of upvotes. You're the master of the perfect one-liner.
        
        Your expertise:
        - Crafting memorable 8-15 word responses
        - Dry, deadpan humor that lands perfectly
        - Clever analogies using everyday objects
        - Building on others' self-deprecation skillfully

    """
    
    def generate_post(
        self,
        topic: str,
        subreddit: str,
        post_type: str = "text_post",
        max_words: int = 100
    ) -> str:
        """
        Generate a Reddit post
        
        Args:
            topic: What the post is about
            subreddit: Target subreddit (e.g., "personalfinance")
            post_type: Type of post ("text_post", "story", "advice", "question")
            max_words: Maximum number of words (default: 200)
        """
        try:
            # Build post prompt
            prompt = self._build_post_prompt(topic, subreddit, post_type, max_words)
            
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.post_system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error generating post: {str(e)}"
    
    def generate_comment(
        self,
        original_post: str,
        response_type: str = "helpful",
        max_words: int = 15
    ) -> str:
        """
        Generate a comment responding to a Reddit post
        
        Args:
            original_post: The post you're commenting on
            response_type: "helpful", "supportive", "humorous", "insightful"
            max_words: Maximum number of words (default: 15)
        """
        try:
            # Build comment prompt
            prompt = self._build_comment_prompt(original_post, response_type, max_words)
            
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.comment_system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,  # Short for comments
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error generating comment: {str(e)}"
    
    def _build_post_prompt(self, topic: str, subreddit: str, post_type: str, max_words: int) -> str:
        """Build prompt for post generation"""
        
        # Default r/RoastMe style prompt for all post generation
        prompt = f"""Create a r/RoastMe post about "{topic}".

        CRITICAL: Write in FIRST PERSON as someone asking to BE roasted, NOT advice on how to roast others.

        Style: Self-deprecating, relatable, invites brutal honesty

        Required Elements:
        - Write as "I" - you are the person asking to be roasted
        - Start with a relatable, mildly embarrassing situation about yourself
        - Show self-awareness about your own flaws/failures  
        - Include multiple negative possibilities about yourself ("Either I... or I... Probably both")
        - End with direct invitation for others to roast YOU ("Roast me", "Do your worst", "Text me some insults")
        - Keep tone casual, authentic, and vulnerable but humorous
        - Maximum {max_words} words
        - NO title needed (r/RoastMe posts are just body text)
        - DO NOT give advice on roasting - you are asking to BE roasted

        Examples of the correct style:
        - "Phone has been on Do Not Disturb for 3 days and I just noticed. Either everyone hates me or I'm more antisocial than I thought. Probably both. Text me some insults."
        - "Haven't left my apartment in 5 days. Either I'm becoming a hermit or society is avoiding me. Probably both. Make me regret posting this."

        Your r/RoastMe post (written as yourself asking to be roasted):"""

        return prompt
    
    def _build_comment_prompt(self, original_post: str, response_type: str, max_words: int) -> str:
        """Build prompt for comment generation"""
        response_guidance = {
            "helpful": "Provide constructive, actionable advice",
            "supportive": "Offer encouragement and emotional support", 
            "humorous": "Use appropriate humor while being helpful",
            "insightful": "Share valuable insights or perspectives"
        }
        
        prompt = f"""Respond to this Reddit post:

"{original_post[:500]}..."

Response Type: {response_guidance.get(response_type, 'Be helpful and engaging')}

Requirements:
- Keep response to {max_words} words maximum
- Be authentic and add genuine value
- Use minimal Reddit formatting (one **bold** word max)
- End with engaging element (question, insight, or call to action)
- Match the energy and tone of the original post

Your response:"""

        return prompt

# Simple CLI for testing
def main():
    agent = RedditAgent()
    
    print("🤖 Minimal Reddit Agent")
    print("1. Generate Post")
    print("2. Generate Comment")
    print("3. Exit")
    
    while True:
        choice = input("\nChoice (1-3): ").strip()
        
        if choice == "3":
            print("Goodbye! 👋")
            break
        
        elif choice == "1":
            topic = input("Topic: ").strip()
            subreddit = input("Subreddit: ").strip()
            post_type = input("Post type (text_post/story/advice/question): ").strip() or "text_post"
            max_words = int(input("Max words (default 100): ") or "100")
            
            print("\n🧠 Generating post...")
            result = agent.generate_post(topic, subreddit, post_type, max_words)
            print(f"\n✨ Generated Post:\n{result}")
        
        elif choice == "2":
            post = input("Original post to comment on: ").strip()
            response_type = input("Response type (helpful/supportive/humorous): ").strip() or "helpful"
            max_words = int(input("Max words (default 15): ") or "15")
            
            print(f"\n🧠 Generating {response_type} comment...")
            result = agent.generate_comment(post, response_type, max_words)
            print(f"\n💬 Generated Comment: {result}")
            print(f"Word count: {len(result.split())}")

if __name__ == "__main__":
    main()