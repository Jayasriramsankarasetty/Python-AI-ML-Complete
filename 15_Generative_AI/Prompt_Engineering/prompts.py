"""
Topic:
Generative AI - Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought)

Importance:
Programming LLMs is done via natural language instructions.
Structuring prompts systematically using few-shot exemplars or logical reasoning chains
significantly improves performance on reasoning, parsing, and classification tasks.

This file covers:
- Concept: Context window, instruction tuning, in-context learning
- Formatting Zero-Shot classification prompts
- Formatting Few-Shot parsing prompts
- Formatting Chain-of-Thought (CoT) mathematical reasoning templates
- Executing python string templates to preview output configurations
"""

# ==========================================
# 1. Concept Explanation & Glossary
# ==========================================
# Prompt Engineering is the practice of optimizing natural language inputs to elicit desired outputs.
#   - Zero-Shot: Prompting the model to perform a task *without* any examples. Relying on pretrained knowledge.
#   - Few-Shot (In-Context Learning): Providing a few input-output examples inside the prompt context.
#     Helps the model learn structured patterns, formatting, and task details dynamically.
#   - Chain-of-Thought (CoT): Directing the model to output its step-by-step reasoning process
#     before outputting the final answer. Essential for math, logic, and multi-step tasks.

# ==========================================
# 2. String Prompt Templates Implementations
# ==========================================

# Example A: Zero-Shot Classification Template
def format_zero_shot_prompt(text):
    prompt_template = f"""
Instruction: Classify the sentiment of the text below as POSITIVE, NEGATIVE, or NEUTRAL.
Do not output any introductory or concluding text, only the classification label.

Text: "{text}"
Sentiment:"""
    return prompt_template.strip()

# Example B: Few-Shot Parsing Template (Parsing names & phone numbers to JSON)
def format_few_shot_prompt(raw_text):
    prompt_template = f"""
Instruction: Parse customer contact information from raw text records into clean JSON objects.

Example 1:
Input: "Hey, this is John Doe. Hit me up at 555-0199."
Output: {{"name": "John Doe", "phone": "555-0199"}}

Example 2:
Input: "Send the invoice to Jane Smith. Her number is 555-0231."
Output: {{"name": "Jane Smith", "phone": "555-0231"}}

Example 3:
Input: "{raw_text}"
Output:"""
    return prompt_template.strip()

# Example C: Chain-of-Thought (CoT) Mathematical Reasoning Template
def format_chain_of_thought_prompt(question):
    prompt_template = f"""
Instruction: Solve the math question below. First, explain your step-by-step reasoning logic.
Then, write the final numerical answer inside double asterisks (e.g. **Answer: 42**).

Question: {question}
Reasoning:"""
    return prompt_template.strip()

# ==========================================
# 3. Execution & Preview
# ==========================================
if __name__ == "__main__":
    print("=======================================")
    print("Zero-Shot Classification Prompt Preview:")
    print("=======================================")
    zero_shot = format_zero_shot_prompt("I love this product! It saved me hours of coding.")
    print(zero_shot)
    
    print("\n=======================================")
    print("Few-Shot Parsing Prompt Preview:")
    print("=======================================")
    few_shot = format_few_shot_prompt("Call Alice Johnson at 555-8910 when ready.")
    print(few_shot)
    
    print("\n=======================================")
    print("Chain-of-Thought (CoT) Reasoning Prompt Preview:")
    print("=======================================")
    cot = format_chain_of_thought_prompt("A store sells apples in boxes of 6. If Bob buys 4 boxes and eats 5 apples, how many apples does he have left?")
    print(cot)
    print("=======================================")

# ==========================================
# 4. Industry Relevance of Prompt Types
# ==========================================
# - Zero-Shot: Ideal for simple classifications, translations, and summarization tasks.
# - Few-Shot: Best when outputs must conform to a strict custom formatting structure (like custom JSON schemas).
# - Chain-of-Thought: Crucial for financial math, code debugging, and algorithmic reasoning workflows.

"""
Key Takeaways:
- Zero-Shot relies entirely on LLM base instruction training; Few-Shot provides exemplars to map structural expectations.
- Chain-of-Thought prompts force step-by-step reasoning prior to final outputs, increasing logical accuracy.
- Delimiters (like triple quotes or XML tags) help LLMs separate instructions from dynamic variable values.

Interview Relevance:
- Explain Chain-of-Thought (CoT) prompting and why it works. (It directs the LLM to write out its reasoning steps first. Because LLMs generate text token-by-token, writing the reasoning path provides additional context tokens in its memory, helping it calculate a more accurate final token).
- How does Few-Shot prompting differ from Fine-Tuning? (Few-Shot prompting changes model behavior at inference time by providing examples inside the input context window, without updating weights. Fine-tuning actually updates the model's weights using a training dataset).
- How do you prevent Prompt Injection? (By separating system instructions from user variables using clean delimiter boundaries, escaping characters, or employing dedicated LLM guardrail checkers).

AI/ML Relevance:
- In-Context learning: Few-shot context learning is highly effective for prototyping tasks without launching expensive parameter update jobs.
"""
