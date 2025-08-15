#!/usr/bin/env python3

def hello_world():
    """Return a friendly greeting."""
    return "Hello, World from Jenkins K8s CI/CD!"

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

def main():
    """Main function to run the application."""
    print(hello_world())
    print(f"4 + 3 = {add_numbers(4, 3)}")

if __name__ == "__main__":
    main()