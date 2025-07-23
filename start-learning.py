#!/usr/bin/env python3
"""
Amazon Q CLI Self-Paced Learning Navigator
Interactive guide to help choose and start the right learning path
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

class LearningNavigator:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.courses = {
            '90min': {
                'name': '90-Minute Live Demo',
                'path': '90min-live-demo',
                'description': 'Executive briefings and technical demonstrations',
                'time': '90 minutes',
                'level': 'Executive/Principal',
                'prerequisites': 'Basic AWS knowledge, familiar with Cursor'
            },
            '5day': {
                'name': '5-Day Comprehensive Workshop',
                'path': '5day-comprehensive',
                'description': 'Production-ready expertise and team enablement',
                'time': '40 hours (5 days)',
                'level': 'Principal+',
                'prerequisites': '90-min demo completion + advanced experience'
            }
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        print(\"\"\"
╔══════════════════════════════════════════════════════════════════════════════╗
║                    Amazon Q CLI Self-Paced Learning Hub                      ║
║                                                                              ║
║        Master Amazon Q CLI with MCP Integration & Advanced Prompting        ║
║                     for Principal Software Engineers                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
        \"\"\")
    
    def print_course_overview(self):
        print(\"\\n🎯 Available Learning Paths:\\n\")
        
        for key, course in self.courses.items():
            print(f\"📚 {course['name']}\")
            print(f\"   Time: {course['time']}\")
            print(f\"   Level: {course['level']}\")
            print(f\"   Focus: {course['description']}\")
            print(f\"   Prerequisites: {course['prerequisites']}\")
            print()
    
    def get_user_choice(self):
        print(\"\\n🚀 What would you like to do?\\n\")
        print(\"1. Start 90-Minute Live Demo Course\")
        print(\"2. Start 5-Day Comprehensive Workshop\")
        print(\"3. Compare courses in detail\")
        print(\"4. Check technical requirements\")
        print(\"5. Get help choosing the right path\")
        print(\"6. Exit\")
        
        while True:
            try:
                choice = input(\"\\nEnter your choice (1-6): \").strip()
                if choice in ['1', '2', '3', '4', '5', '6']:
                    return choice
                else:
                    print(\"❌ Please enter a number between 1 and 6\")
            except KeyboardInterrupt:
                print(\"\\n\\n👋 Goodbye! Happy learning!\")
                sys.exit(0)
    
    def start_course(self, course_key):
        course = self.courses[course_key]
        course_path = self.base_path / course['path']
        readme_path = course_path / 'README.md'
        
        if not readme_path.exists():
            print(f\"❌ Course materials not found at {course_path}\")
            input(\"\\nPress Enter to continue...\")
            return
        
        print(f\"\\n🎓 Starting {course['name']}\\n\")
        print(f\"📁 Course Location: {course_path}\")
        print(f\"📖 Opening: {readme_path}\\n\")
        
        # Try to open the README file
        try:
            if sys.platform == 'darwin':  # macOS
                subprocess.run(['open', str(readme_path)])
            elif sys.platform == 'win32':  # Windows
                os.startfile(str(readme_path))
            else:  # Linux
                subprocess.run(['xdg-open', str(readme_path)])
            
            print(\"✅ Course README opened in your default application\")
        except Exception as e:
            print(f\"⚠️  Could not auto-open file. Please manually open: {readme_path}\")
        
        print(f\"\\n📋 Next Steps:\")
        print(f\"1. Follow the setup instructions in the README\")
        print(f\"2. Complete the prerequisites if needed\")
        print(f\"3. Start with the first module\")
        print(f\"4. Join our community for support\")
        
        input(\"\\nPress Enter to continue...\")
    
    def compare_courses(self):
        comparison_path = self.base_path / 'course-comparison.md'
        
        print(\"\\n📊 Opening detailed course comparison...\\n\")
        
        try:
            if sys.platform == 'darwin':  # macOS
                subprocess.run(['open', str(comparison_path)])
            elif sys.platform == 'win32':  # Windows
                os.startfile(str(comparison_path))
            else:  # Linux
                subprocess.run(['xdg-open', str(comparison_path)])
            
            print(\"✅ Course comparison opened in your default application\")
        except Exception as e:
            print(f\"⚠️  Could not auto-open file. Please manually open: {comparison_path}\")
        
        print(\"\\n🤔 Still need help deciding?\")
        print(\"- Email: guidance@amazon-q-cli.dev\")
        print(\"- Office Hours: Tuesdays 2-4 PM PST\")
        print(\"- Discord: #course-selection channel\")
        
        input(\"\\nPress Enter to continue...\")
    
    def check_requirements(self):
        print(\"\\n🛠️  Technical Requirements Check\\n\")
        
        requirements = {
            'Amazon Q CLI': 'q --version',
            'Node.js': 'node --version',
            'AWS CLI': 'aws --version',
            'Git': 'git --version',
            'Python': 'python --version'
        }
        
        print(\"Checking installed tools...\\n\")
        
        for tool, command in requirements.items():
            try:
                result = subprocess.run(command.split(), 
                                      capture_output=True, 
                                      text=True, 
                                      timeout=5)
                if result.returncode == 0:
                    version = result.stdout.strip().split('\\n')[0]
                    print(f\"✅ {tool}: {version}\")
                else:
                    print(f\"❌ {tool}: Not found or error\")
            except (subprocess.TimeoutExpired, FileNotFoundError):
                print(f\"❌ {tool}: Not installed\")
        
        print(\"\\n📋 Additional Requirements:\")
        print(\"- AWS account with appropriate permissions\")
        print(\"- GitHub account and repository access\")
        print(\"- Stable internet connection\")
        print(\"- 4GB+ RAM available\")
        
        print(\"\\n🔧 Installation Help:\")
        print(\"- Amazon Q CLI: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/\")
        print(\"- Node.js: https://nodejs.org/\")
        print(\"- AWS CLI: https://aws.amazon.com/cli/\")
        
        input(\"\\nPress Enter to continue...\")
    
    def get_help_choosing(self):
        print(\"\\n🤝 Help Choosing Your Learning Path\\n\")
        
        questions = [
            {
                'question': 'What is your primary goal?',
                'options': {
                    'a': 'Evaluate Amazon Q CLI for my team',
                    'b': 'Learn for personal development',
                    'c': 'Implement in production environment',
                    'd': 'Train and enable my entire team'
                }
            },
            {
                'question': 'How much time can you dedicate?',
                'options': {
                    'a': '1-2 hours maximum',
                    'b': 'A few hours over several days',
                    'c': 'Full day intensive learning',
                    'd': 'Full week dedicated learning'
                }
            },
            {
                'question': 'What is your current experience level?',
                'options': {
                    'a': 'New to Amazon Q CLI and AWS',
                    'b': 'Familiar with AWS, new to Q CLI',
                    'c': 'Some Q CLI experience, want to go deeper',
                    'd': 'Want to become expert and train others'
                }
            }
        ]
        
        answers = []
        
        for i, q in enumerate(questions, 1):
            print(f\"{i}. {q['question']}\")
            for key, option in q['options'].items():
                print(f\"   {key}) {option}\")
            
            while True:
                answer = input(\"\\nYour choice (a-d): \").strip().lower()
                if answer in ['a', 'b', 'c', 'd']:
                    answers.append(answer)
                    break
                print(\"❌ Please enter a, b, c, or d\")
            print()
        
        # Simple recommendation logic
        recommendation = self.get_recommendation(answers)
        
        print(f\"\\n🎯 Recommendation: {recommendation['course']}\\n\")
        print(f\"📝 Reasoning: {recommendation['reason']}\\n\")
        print(f\"📋 Next Steps: {recommendation['next_steps']}\\n\")
        
        start_now = input(\"Would you like to start this course now? (y/n): \").strip().lower()
        if start_now == 'y':
            if '90-Minute' in recommendation['course']:
                self.start_course('90min')
            else:
                self.start_course('5day')
        
        input(\"\\nPress Enter to continue...\")
    
    def get_recommendation(self, answers):
        # Simple scoring system
        demo_score = 0
        comprehensive_score = 0
        
        # Question 1: Primary goal
        if answers[0] == 'a':  # Evaluate
            demo_score += 3
        elif answers[0] == 'b':  # Personal
            demo_score += 1
            comprehensive_score += 1
        elif answers[0] == 'c':  # Production
            comprehensive_score += 3
        elif answers[0] == 'd':  # Train team
            comprehensive_score += 3
        
        # Question 2: Time available
        if answers[1] == 'a':  # 1-2 hours
            demo_score += 3
        elif answers[1] == 'b':  # Few hours
            demo_score += 2
        elif answers[1] == 'c':  # Full day
            comprehensive_score += 2
        elif answers[1] == 'd':  # Full week
            comprehensive_score += 3
        
        # Question 3: Experience level
        if answers[2] == 'a':  # New
            demo_score += 2
        elif answers[2] == 'b':  # Familiar AWS
            demo_score += 2
        elif answers[2] == 'c':  # Some experience
            comprehensive_score += 2
        elif answers[2] == 'd':  # Want expertise
            comprehensive_score += 3
        
        if demo_score > comprehensive_score:
            return {
                'course': '90-Minute Live Demo',
                'reason': 'Based on your responses, you would benefit most from a quick, comprehensive overview to evaluate Amazon Q CLI capabilities.',
                'next_steps': 'Start with the 90-minute demo, then consider the comprehensive course if you decide to implement.'
            }
        else:
            return {
                'course': '5-Day Comprehensive Workshop',
                'reason': 'Based on your responses, you are ready for deep, production-focused learning with hands-on implementation.',
                'next_steps': 'Ensure you meet the prerequisites, then dive into the comprehensive workshop for expert-level skills.'
            }
    
    def run(self):
        while True:
            self.clear_screen()
            self.print_header()
            self.print_course_overview()
            
            choice = self.get_user_choice()
            
            if choice == '1':
                self.start_course('90min')
            elif choice == '2':
                self.start_course('5day')
            elif choice == '3':
                self.compare_courses()
            elif choice == '4':
                self.check_requirements()
            elif choice == '5':
                self.get_help_choosing()
            elif choice == '6':
                print(\"\\n👋 Thank you for using Amazon Q CLI Learning Hub!\")
                print(\"🚀 Happy learning and building amazing things with Amazon Q CLI!\")
                break

def main():
    try:
        navigator = LearningNavigator()
        navigator.run()
    except KeyboardInterrupt:
        print(\"\\n\\n👋 Goodbye! Happy learning!\")
    except Exception as e:
        print(f\"\\n❌ An error occurred: {e}\")
        print(\"Please report this issue to: support@amazon-q-cli.dev\")

if __name__ == \"__main__\":
    main()