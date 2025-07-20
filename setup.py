#!/usr/bin/env python3
"""
Setup script for Content Agent
"""

import os
import shutil

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    if not os.path.exists('.env'):
        if os.path.exists('env_template.txt'):
            shutil.copy('env_template.txt', '.env')
            print("✅ Created .env file from template")
            print("📝 Please edit .env file and add your OpenAI API key")
        else:
            print("❌ env_template.txt not found")
            return False
    else:
        print("✅ .env file already exists")
    
    return True

def check_env_file():
    """Check if .env file has a valid API key"""
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        return False
    
    with open('.env', 'r') as f:
        content = f.read()
    
    if 'your_openai_api_key_here' in content:
        print("⚠️  Please update your .env file with your actual OpenAI API key")
        print("   Get your API key from: https://platform.openai.com/api-keys")
        return False
    
    if 'OPENAI_API_KEY=' in content:
        print("✅ .env file appears to be configured")
        return True
    
    print("❌ OPENAI_API_KEY not found in .env file")
    return False

def main():
    print("🚀 Content Agent Setup")
    print("=" * 30)
    
    # Create .env file if needed
    if create_env_file():
        # Check if it's properly configured
        if check_env_file():
            print("\n🎉 Setup complete! You can now run:")
            print("   python test_content_agent.py")
            print("   python content_agent.py")
        else:
            print("\n📝 Next steps:")
            print("1. Edit .env file and add your OpenAI API key")
            print("2. Run: python test_content_agent.py")
    else:
        print("\n❌ Setup failed. Please check the files.")

if __name__ == "__main__":
    main() 