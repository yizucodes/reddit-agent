# simple_content_agent.py - MVP: Prompt → Text
import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()

class SimpleContentAgent:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Agent personality and expertise
        self.system_prompt = """
        You are a professional content creation assistant. You help users create high-quality content for social media, blogs, marketing, and other platforms.
        
        Your expertise includes:
        - Writing engaging headlines and titles
        - Creating compelling social media posts
        - Developing blog content and articles
        - Crafting marketing copy
        - Generating content ideas and strategies
        - Optimizing content for different platforms
        
        Always provide:
        - Clear, actionable content
        - Platform-specific formatting when relevant
        - Creative but professional tone
        - Value-focused content that serves the audience
        
        Keep responses concise but comprehensive. Provide single, focused responses unless specifically asked for multiple options.
        """
        
        # Reddit-specific system prompt
        self.reddit_system_prompt = """
        You are a Reddit content creation expert with 20 years of experience in viral content. You understand Reddit's unique ecosystem and what makes posts go viral.
        
        Your expertise includes:
        - Reddit's algorithm and what drives upvotes
        - Subreddit-specific cultures and rules
        - Viral title and content patterns
        - Engagement optimization strategies
        - Credibility building techniques
        - Timing and posting strategies
        
        Reddit Virality Principles:
        - Hook readers in the first sentence
        - Use specific numbers and emotional triggers
        - Tell personal stories with clear arcs
        - Provide actionable value
        - Encourage engagement through questions
        - Follow subreddit rules and culture
        - Use appropriate formatting (TL;DR, bullet points, bold text)
        
        Always provide:
        - Single, focused responses optimized for Reddit
        - Platform-specific formatting and structure
        - Authentic, relatable tone
        - Clear value proposition
        - Engagement hooks
        """
    
    def generate_content(self, user_prompt: str) -> str:
        """
        Main function: Takes a prompt, returns generated content
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # or "gpt-3.5-turbo" for cheaper option
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=1000,
                temperature=0.7  # Balance creativity with consistency
            )
            
            content = response.choices[0].message.content
            return content.strip()
            
        except Exception as e:
            return f"Error generating content: {str(e)}"
    
    def generate_reddit_content(
        self,
        topic: str,
        subreddit: str,
        post_type: str = "first_post",
        persona: dict = None,
        content_strategy: dict = None,
        optimization: dict = None
    ) -> str:
        """
        Generate optimized Reddit content based on virality factors
        """
        try:
            # Build context-aware prompt
            enhanced_prompt = self._build_reddit_prompt(
                topic=topic,
                subreddit=subreddit,
                post_type=post_type,
                persona=persona,
                content_strategy=content_strategy,
                optimization=optimization
            )
            
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.reddit_system_prompt},
                    {"role": "user", "content": enhanced_prompt}
                ],
                max_tokens=1500,
                temperature=0.8  # Slightly higher for creativity
            )
            
            content = response.choices[0].message.content
            return content.strip()
            
        except Exception as e:
            return f"Error generating Reddit content: {str(e)}"
    
    def _build_reddit_prompt(
        self,
        topic: str,
        subreddit: str,
        post_type: str,
        persona: dict = None,
        content_strategy: dict = None,
        optimization: dict = None
    ) -> str:
        """
        Build a comprehensive Reddit prompt based on all parameters
        """
        prompt_parts = []
        
        # Basic context
        prompt_parts.append(f"Create a Reddit {post_type} about '{topic}' for r/{subreddit}")
        
        # Persona context
        if persona:
            persona_text = self._format_persona(persona)
            prompt_parts.append(f"Persona: {persona_text}")
        
        # Content strategy
        if content_strategy:
            strategy_text = self._format_content_strategy(content_strategy)
            prompt_parts.append(f"Content Strategy: {strategy_text}")
        
        # Optimization factors
        if optimization:
            optimization_text = self._format_optimization(optimization)
            prompt_parts.append(f"Optimization: {optimization_text}")
        
        # Reddit-specific instructions
        reddit_instructions = self._get_reddit_instructions(subreddit, post_type)
        prompt_parts.append(f"Reddit Instructions: {reddit_instructions}")
        
        return "\n\n".join(prompt_parts)
    
    def _format_persona(self, persona: dict) -> str:
        """Format persona information for prompt"""
        parts = []
        
        if persona.get('type'):
            parts.append(f"Type: {persona['type']}")
        
        if persona.get('credentials'):
            parts.append(f"Credentials: {persona['credentials']}")
        
        if persona.get('tone'):
            parts.append(f"Tone: {persona['tone']}")
        
        if persona.get('expertise_area'):
            parts.append(f"Expertise: {persona['expertise_area']}")
        
        return "; ".join(parts)
    
    def _format_content_strategy(self, strategy: dict) -> str:
        """Format content strategy for prompt"""
        parts = []
        
        if strategy.get('content_type'):
            parts.append(f"Content Type: {strategy['content_type']}")
        
        if strategy.get('viral_hook'):
            parts.append(f"Viral Hook: {strategy['viral_hook']}")
        
        if strategy.get('emotional_trigger'):
            parts.append(f"Emotional Trigger: {strategy['emotional_trigger']}")
        
        if strategy.get('story_arc'):
            parts.append(f"Story Arc: {strategy['story_arc']}")
        
        if strategy.get('value_type'):
            parts.append(f"Value Type: {strategy['value_type']}")
        
        return "; ".join(parts)
    
    def _format_optimization(self, optimization: dict) -> str:
        """Format optimization factors for prompt"""
        parts = []
        
        if optimization.get('title_strategy'):
            title = optimization['title_strategy']
            title_parts = []
            if title.get('hook_type'):
                title_parts.append(f"Hook: {title['hook_type']}")
            if title.get('include_credibility'):
                title_parts.append("Include credibility")
            if title_parts:
                parts.append(f"Title: {'; '.join(title_parts)}")
        
        if optimization.get('content_structure'):
            structure = optimization['content_structure']
            structure_parts = []
            if structure.get('include_tl_dr'):
                structure_parts.append("Include TL;DR")
            if structure.get('use_bullet_points'):
                structure_parts.append("Use bullet points")
            if structure_parts:
                parts.append(f"Structure: {'; '.join(structure_parts)}")
        
        return "; ".join(parts)
    
    def _get_reddit_instructions(self, subreddit: str, post_type: str) -> str:
        """Get Reddit-specific instructions based on subreddit and post type"""
        instructions = []
        
        # General Reddit instructions
        instructions.append("Use Reddit formatting (bold, bullet points, TL;DR)")
        instructions.append("End with a question to encourage engagement")
        instructions.append("Keep paragraphs short and readable")
        
        # Post type specific
        if post_type == "first_post":
            instructions.append("Make the title compelling and specific")
            instructions.append("Hook readers in the first sentence")
        elif post_type == "comment":
            instructions.append("Be helpful and add value to the discussion")
            instructions.append("Keep it concise but informative")
        
        # Subreddit specific (basic examples)
        if "finance" in subreddit.lower():
            instructions.append("Include specific numbers and data when relevant")
            instructions.append("Focus on actionable financial advice")
        elif "fitness" in subreddit.lower():
            instructions.append("Include before/after details if applicable")
            instructions.append("Focus on practical fitness advice")
        
        return "; ".join(instructions)
    
    def generate_with_context(self, user_prompt: str, context: dict = None) -> str:
        """
        Enhanced version with additional context
        """
        # Add context to the prompt if provided
        enhanced_prompt = user_prompt
        
        if context:
            context_info = []
            if context.get('platform'):
                context_info.append(f"Platform: {context['platform']}")
            if context.get('audience'):
                context_info.append(f"Target audience: {context['audience']}")
            if context.get('tone'):
                context_info.append(f"Tone: {context['tone']}")
            if context.get('length'):
                context_info.append(f"Length: {context['length']}")
            
            if context_info:
                enhanced_prompt = f"{user_prompt}\n\nAdditional context:\n" + "\n".join(context_info)
        
        return self.generate_content(enhanced_prompt)

# Simple CLI interface for testing
def main():
    agent = SimpleContentAgent()
    
    print("🤖 Content Agent MVP Ready!")
    print("Enter your content requests (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("\n📝 Your prompt: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye! 👋")
                break
            
            if not user_input:
                continue
            
            print("\n🧠 Generating content...")
            
            # Generate content
            result = agent.generate_content(user_input)
            
            # Display result
            print("\n✨ Generated Content:")
            print("-" * 30)
            print(result)
            print("-" * 30)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")

# API-style interface (for web integration)
class ContentAgentAPI:
    def __init__(self):
        self.agent = SimpleContentAgent()
    
    def create_content(self, prompt: str, context: dict = None) -> dict:
        """
        API endpoint style - returns structured response
        """
        try:
            if context:
                content = self.agent.generate_with_context(prompt, context)
            else:
                content = self.agent.generate_content(prompt)
            
            return {
                "success": True,
                "content": content,
                "prompt": prompt,
                "context": context or {}
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "prompt": prompt
            }

# Flask web API (optional - for web interface)
try:
    from flask import Flask, request, jsonify
    
    app = Flask(__name__)
    api = ContentAgentAPI()
    
    @app.route('/generate', methods=['POST'])
    def generate_content_api():
        data = request.json
        prompt = data.get('prompt', '')
        context = data.get('context', {})
        
        if not prompt:
            return jsonify({"success": False, "error": "Prompt required"}), 400
        
        result = api.create_content(prompt, context)
        return jsonify(result)
    
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "healthy", "agent": "content-agent-mvp"})
    
    def run_web_api():
        print("🌐 Starting web API on http://localhost:5000")
        app.run(debug=True, port=5000)

except ImportError:
    print("Flask not installed - web API unavailable")
    def run_web_api():
        print("Install Flask to use web API: pip install flask")

# Example usage functions
def example_usage():
    agent = SimpleContentAgent()
    
    # Basic examples
    examples = [
        "Write a catchy Instagram caption for a coffee shop's morning special",
        "Create a LinkedIn post about the importance of work-life balance",
        "Generate 3 blog post title ideas about sustainable living",
        "Write a product description for wireless headphones",
        "Create an email subject line for a flash sale announcement"
    ]
    
    print("🔥 Example Content Generation:")
    print("=" * 50)
    
    for i, prompt in enumerate(examples, 1):
        print(f"\n{i}. Prompt: {prompt}")
        result = agent.generate_content(prompt)
        print(f"Result: {result[:100]}..." if len(result) > 100 else f"Result: {result}")
        print("-" * 30)

# Reddit-specific CLI interface
def reddit_main():
    agent = SimpleContentAgent()
    
    print("🤖 Reddit Content Agent Ready!")
    print("Create viral Reddit posts with optimized parameters")
    print("-" * 50)
    
    while True:
        try:
            print("\n📝 Reddit Post Generator")
            print("1. Quick post (basic parameters)")
            print("2. Advanced post (full optimization)")
            print("3. Exit")
            
            choice = input("\nChoose option (1-3): ").strip()
            
            if choice == "3":
                print("Goodbye! 👋")
                break
            
            if choice == "1":
                # Quick post generation
                topic = input("Topic: ").strip()
                subreddit = input("Subreddit (e.g., personalfinance): ").strip()
                post_type = input("Post type (first_post/comment): ").strip() or "first_post"
                
                print("\n🧠 Generating Reddit content...")
                result = agent.generate_reddit_content(
                    topic=topic,
                    subreddit=subreddit,
                    post_type=post_type
                )
                
                print("\n✨ Generated Reddit Content:")
                print("-" * 30)
                print(result)
                print("-" * 30)
                
            elif choice == "2":
                # Advanced post generation
                topic = input("Topic: ").strip()
                subreddit = input("Subreddit: ").strip()
                post_type = input("Post type: ").strip() or "first_post"
                
                # Persona
                print("\n👤 Persona Setup:")
                persona_type = input("Persona type (expert/everyman/helper/storyteller): ").strip()
                credentials = input("Credentials (optional): ").strip()
                tone = input("Tone (professional_but_relatable/casual/humorous): ").strip()
                
                persona = {
                    "type": persona_type,
                    "credentials": credentials if credentials else None,
                    "tone": tone if tone else "professional_but_relatable"
                }
                
                # Content strategy
                print("\n📊 Content Strategy:")
                content_type = input("Content type (personal_story/advice/question/resource): ").strip()
                viral_hook = input("Viral hook (transformation/secret/mistake/victory): ").strip()
                emotional_trigger = input("Emotional trigger (inspiration/curiosity/empathy): ").strip()
                
                content_strategy = {
                    "content_type": content_type,
                    "viral_hook": viral_hook,
                    "emotional_trigger": emotional_trigger,
                    "story_arc": "struggle_to_success"
                }
                
                # Optimization
                print("\n🎯 Optimization:")
                include_tl_dr = input("Include TL;DR? (y/n): ").strip().lower() == "y"
                use_bullet_points = input("Use bullet points? (y/n): ").strip().lower() == "y"
                include_credibility = input("Include credibility in title? (y/n): ").strip().lower() == "y"
                
                optimization = {
                    "title_strategy": {
                        "hook_type": "specific_number",
                        "include_credibility": include_credibility
                    },
                    "content_structure": {
                        "include_tl_dr": include_tl_dr,
                        "use_bullet_points": use_bullet_points
                    }
                }
                
                print("\n🧠 Generating optimized Reddit content...")
                result = agent.generate_reddit_content(
                    topic=topic,
                    subreddit=subreddit,
                    post_type=post_type,
                    persona=persona,
                    content_strategy=content_strategy,
                    optimization=optimization
                )
                
                print("\n✨ Generated Optimized Reddit Content:")
                print("-" * 30)
                print(result)
                print("-" * 30)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")

# Reddit example usage
def reddit_example_usage():
    agent = SimpleContentAgent()
    
    print("🔥 Reddit Content Generation Examples:")
    print("=" * 50)
    
    # Example 1: Personal finance story
    print("\n1. Personal Finance Transformation Story")
    result1 = agent.generate_reddit_content(
        topic="student loan forgiveness success",
        subreddit="personalfinance",
        post_type="first_post",
        persona={
            "type": "everyman",
            "tone": "relatable",
            "expertise_area": "personal_finance"
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
    print(f"Result: {result1[:200]}..." if len(result1) > 200 else f"Result: {result1}")
    
    # Example 2: Fitness advice
    print("\n2. Fitness Expert Advice")
    result2 = agent.generate_reddit_content(
        topic="weight loss plateau breakthrough",
        subreddit="fitness",
        post_type="first_post",
        persona={
            "type": "expert",
            "credentials": "certified_personal_trainer",
            "tone": "professional_but_relatable",
            "expertise_area": "fitness"
        },
        content_strategy={
            "content_type": "advice",
            "viral_hook": "secret",
            "emotional_trigger": "curiosity",
            "value_type": "actionable_advice"
        }
    )
    print(f"Result: {result2[:200]}..." if len(result2) > 200 else f"Result: {result2}")
    
    print("\n" + "-" * 30)

if __name__ == "__main__":
    # Choose your interface:
    
    # 1. Original command line interface
    # main()
    
    # 2. Reddit-specific interface
    reddit_main()
    
    # 3. Run Reddit examples
    # reddit_example_usage()
    
    # 4. Web API (requires Flask)
    # run_web_api()