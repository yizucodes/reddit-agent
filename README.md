# Reddit Content Agent

An AI-powered content creation tool optimized for Reddit virality and engagement. Create viral Reddit posts with advanced parameters for maximum impressions and upvotes.

## 🚀 Features

- **Reddit-Optimized Content**: Built specifically for Reddit's algorithm and community culture
- **Viral Hook Detection**: Automatically identifies transformation, secret, mistake, victory patterns
- **Persona Management**: Expert, everyman, helper, and storyteller personas
- **Subreddit-Specific Optimization**: Adapts to different community cultures and rules
- **Engagement Optimization**: Built-in strategies for comments and upvotes
- **Interactive CLI**: Easy-to-use command-line interface

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd reddit-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment**
   ```bash
   python setup.py
   ```

4. **Add your OpenAI API key**
   - Edit the `.env` file
   - Add your OpenAI API key: `OPENAI_API_KEY=your_key_here`

## 🧪 Testing

### Quick Test
```bash
python quick_test.py
```

### Comprehensive Test
```bash
python test_reddit_agent.py
```

### Interactive Mode
```bash
python content_agent.py
```

## 🎯 Usage

### Basic Usage
```python
from content_agent import SimpleContentAgent

agent = SimpleContentAgent()

# Generate a basic Reddit post
result = agent.generate_reddit_content(
    topic="budgeting tips for beginners",
    subreddit="personalfinance",
    post_type="first_post"
)
```

### Advanced Usage
```python
# Generate viral content with full optimization
result = agent.generate_reddit_content(
    topic="weight loss transformation",
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
```

## 📊 Parameters

### Core Parameters
- `topic`: Main content focus
- `subreddit`: Target subreddit (e.g., "personalfinance")
- `post_type`: "first_post", "comment", "reply"

### Persona Options
- `type`: "expert", "everyman", "helper", "storyteller"
- `credentials`: Professional credentials
- `tone`: "professional_but_relatable", "casual", "humorous"
- `expertise_area`: Area of expertise

### Content Strategy
- `content_type`: "personal_story", "advice", "question", "resource"
- `viral_hook`: "transformation", "secret", "mistake", "victory"
- `emotional_trigger`: "inspiration", "curiosity", "empathy"
- `story_arc`: "struggle_to_success", "problem_solution"

### Optimization
- `title_strategy`: Hook type and credibility inclusion
- `content_structure`: TL;DR, bullet points, formatting

## 🔥 Viral Content Examples

### Personal Finance Transformation
```python
agent.generate_reddit_content(
    topic="student loan forgiveness success",
    subreddit="personalfinance",
    persona={"type": "everyman", "tone": "relatable"},
    content_strategy={
        "content_type": "personal_story",
        "viral_hook": "transformation",
        "emotional_trigger": "inspiration"
    }
)
```

### Fitness Expert Advice
```python
agent.generate_reddit_content(
    topic="weight loss plateau breakthrough",
    subreddit="fitness",
    persona={
        "type": "expert",
        "credentials": "certified_personal_trainer"
    },
    content_strategy={
        "content_type": "advice",
        "viral_hook": "secret",
        "emotional_trigger": "curiosity"
    }
)
```

## 🛠️ Development

### Project Structure
```
reddit-agent/
├── content_agent.py          # Main agent with Reddit optimization
├── test_reddit_agent.py     # Comprehensive Reddit tests
├── quick_test.py            # Quick test script
├── setup.py                 # Environment setup
├── requirements.txt         # Dependencies
├── .env                    # API keys (not committed)
├── env_template.txt        # Environment template
└── README.md              # This file
```

### Adding New Features
1. Extend the `SimpleContentAgent` class
2. Add new parameters to `generate_reddit_content()`
3. Update the prompt building methods
4. Add tests in `test_reddit_agent.py`

## 🔒 Security

- API keys are stored in `.env` (not committed to Git)
- `.gitignore` prevents sensitive files from being committed
- Template approach keeps credentials secure

## 📈 Performance

- Optimized for Reddit's algorithm
- Built-in viral content patterns
- Subreddit-specific optimization
- Engagement-focused formatting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- Check the test files for usage examples
- Run `python test_reddit_agent.py` for diagnostics
- Ensure your API key is properly configured in `.env`