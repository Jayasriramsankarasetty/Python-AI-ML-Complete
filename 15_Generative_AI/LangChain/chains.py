"""
Topic:
Generative AI - LangChain Foundations (Chains & Memory)

Importance:
LangChain is the standard framework for orchestrating LLM application pipelines.
Understanding how prompts, chains, and memory states interact allows engineers to build
conversational agents and multi-step reasoning systems.

This file covers:
- Concept: LLMChain, prompt template variables, memory buffers
- Implementing a simulated LLM Chain class
- Storing conversational context memory across multiple turns
- Execution flow demonstration showing inputs being augmented by historical threads
"""

# ==========================================
# 1. Concept Explanation & Glossary
# ==========================================
# LangChain abstracts common LLM integration patterns:
#   - PromptTemplates: Manage templates with dynamic variables placeholder parameters.
#   - Chains: Connect prompts, models, and output parsers into a single sequential execution path.
#   - Memory: Holds context histories. Since LLM APIs are stateless (each API request has no memory of the past),
#     LangChain stores previous conversational turns and injects them back into subsequent prompts.

# ==========================================
# 2. Simple LLM Chain & Memory Simulation
# ==========================================
class SimpleMemoryBuffer:
    def __init__(self):
        self.history = []
        
    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
        
    def get_conversation_string(self):
        # Concatenate history as a string to inject into LLM context prompts
        history_str = ""
        for msg in self.history:
            history_str += f"{msg['role'].capitalize()}: {msg['content']}\n"
        return history_str

class SimpleChain:
    def __init__(self, prompt_template, memory=None):
        self.prompt_template = prompt_template
        self.memory = memory or SimpleMemoryBuffer()
        
    def run(self, user_input):
        # Format the context from memory
        chat_history = self.memory.get_conversation_string()
        
        # Build prompt using the template and memory
        formatted_prompt = self.prompt_template.format(
            history=chat_history,
            input=user_input
        )
        
        # Mock LLM generation logic based on simple keyword checks
        if "weather" in user_input.lower():
            response = "The weather is currently sunny and 72 degrees."
        elif "my name" in user_input.lower():
            # Try to retrieve name from memory history
            name = "stranger"
            for msg in reversed(self.memory.history):
                if msg["role"] == "user" and "name is" in msg["content"].lower():
                    words = msg["content"].split()
                    name = words[-1].strip(".")
                    break
            response = f"Your name is {name}."
        else:
            response = f"I hear you talking about: '{user_input}'."
            
        # Store turn in memory
        self.memory.add_message("user", user_input)
        self.memory.add_message("assistant", response)
        
        return response, formatted_prompt

# ==========================================
# 3. Execution & Testing
# ==========================================
if __name__ == "__main__":
    # Define a prompt template matching conversational memory patterns
    template = """
You are a helpful AI assistant. Review the history below to maintain conversation context.

Conversation History:
{history}
Current User Input: {input}
Assistant Response:"""
    
    chain = SimpleChain(prompt_template=template)
    
    print("=======================================")
    print("Conversational Chain Simulation:")
    print("=======================================")
    
    # Turn 1
    resp1, prompt1 = chain.run("Hi, my name is John.")
    print("--- Turn 1 Prompt Injected: ---")
    print(prompt1)
    print(f"Assistant Output: {resp1}\n")
    
    # Turn 2
    resp2, prompt2 = chain.run("What is my name?")
    print("--- Turn 2 Prompt Injected (Memory active): ---")
    print(prompt2)
    print(f"Assistant Output: {resp2}\n")
    
    print("=======================================")
    print("Final Memory Storage Status:")
    print("=======================================")
    print(chain.memory.get_conversation_string())
    print("=======================================")

"""
Key Takeaways:
- Memory buffers override stateless API limits by maintaining conversational logs on client nodes.
- LangChain sequences input-output templates to automate prompt pipeline compilation.
- Conversational chains inject formatting structures (System, User, History placeholders) transparently.

Interview Relevance:
- Why do LLM APIs need memory libraries like LangChain? (LLM APIs are stateless, meaning they treat every query as completely independent. To maintain context in a chatbot, the client must store the chat history and send it back with every new query).
- What is the difference between ConversationBufferMemory and ConversationSummaryMemory? (ConversationBufferMemory stores the entire conversation verbatim, which can quickly exceed LLM context window limits; ConversationSummaryMemory uses an LLM to periodically summarize the history, keeping the context token footprint small).
- What are LangChain Agents? (Agents use an LLM to dynamically determine *which* tools to use and in what order to solve a user's prompt, rather than following a hard-coded sequence of steps).

AI/ML Relevance:
- Agent Pipelines: Chains and routing memory are foundational components to construct multi-tool autonomous AI agents.
"""
