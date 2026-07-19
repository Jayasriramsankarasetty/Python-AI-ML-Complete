"""
Topic:
Generative AI - Large Language Model (LLM) Basics & API Configurations

Importance:
LLM APIs form the primary interface for Generative AI applications.
Understanding how tokens are generated and how parameters like Temperature, Top-P,
and Max Tokens impact output distributions is crucial for designing predictable AI applications.

This file covers:
- Concept: Next-token prediction, tokenization, and generation parameters
- Simulating LLM text generation with probabilistic temperature models
- Real-world usage & API parameters simulation (OpenAI style)
- Industry relevance of temperature choices
"""

import numpy as np

# ==========================================
# 1. Concept Explanation & Parameter Glossary
# ==========================================
# LLMs are auto-regressive next-token prediction models.
# Given an input prompt, they compute a probability distribution over their entire vocabulary
# to select the next token, append it to the prompt, and repeat.
# Core Parameters:
#   - Temperature (0.0 to 2.0): Scales token probability distribution.
#     - Low Temp (e.g. 0.0 - 0.2): Makes model highly deterministic, choosing the top-ranked token.
#     - High Temp (e.g. 0.8 - 1.5): flattens probability curves, adding randomness and creativity.
#   - Top-P (Nucleus Sampling): Limits selection to cumulative probability sum threshold (e.g., top 90%).
#   - Max Tokens: Limit cap on tokens generated per query response.

# ==========================================
# 2. Simple LLM Probabilistic Text Generation Simulator
# ==========================================
class SimulatedLLM:
    def __init__(self):
        # A simple mock vocabulary with transition associations to mimic generation paths
        self.vocabulary = ["AI", "is", "transforming", "software", "development", "industries", "everywhere", "rapidly"]
        
        # Mock logits (raw outputs from model before softmax) for the next token given "AI is transforming..."
        self.mock_logits = {
            "software": 8.0,      # High likelihood
            "development": 2.0,
            "industries": 7.0,     # High likelihood
            "everywhere": 3.0,
            "rapidly": 1.0
        }
        
    def generate_next_token(self, temperature=1.0):
        # Convert logits dict to arrays
        tokens = list(self.mock_logits.keys())
        logits = np.array([self.mock_logits[t] for t in tokens])
        
        # Apply Temperature scaling
        # Avoid dividing by exactly 0 to prevent division by zero errors
        temp = max(1e-6, temperature)
        scaled_logits = logits / temp
        
        # Softmax conversion: e^x / sum(e^x) to get probabilities
        exp_logits = np.exp(scaled_logits - np.max(scaled_logits)) # subtract max for numerical stability
        probabilities = exp_logits / np.sum(exp_logits)
        
        # Choose next token based on probabilities
        chosen_token = np.random.choice(tokens, p=probabilities)
        
        return chosen_token, dict(zip(tokens, probabilities))

# ==========================================
# 3. Running Simulations
# ==========================================
if __name__ == "__main__":
    llm = SimulatedLLM()
    prompt = "AI is transforming"
    
    print("=======================================")
    print(f"Prompt: '{prompt} ...'")
    print("=======================================")
    
    # Simulation 1: Low Temperature (Deterministic, Analytical)
    print("\nSimulation 1: Low Temperature (0.2)")
    token_02, probs_02 = llm.generate_next_token(temperature=0.2)
    print(f"Generated Next Token: '{token_02}'")
    print("Token Probabilities:")
    for tok, p in probs_02.items():
        print(f"  - {tok:12}: {p*100:.2f}%")
        
    # Simulation 2: High Temperature (Creative, Random)
    print("\nSimulation 2: High Temperature (1.5)")
    token_15, probs_15 = llm.generate_next_token(temperature=1.5)
    print(f"Generated Next Token: '{token_15}'")
    print("Token Probabilities:")
    for tok, p in probs_15.items():
        print(f"  - {tok:12}: {p*100:.2f}%")
    print("=======================================")

# ==========================================
# 4. Real-world API Structure (OpenAI chat mock explanation)
# ==========================================
# In a production environment, you interface with APIs (OpenAI, Anthropic, local LLaMA engines) like so:
#
# client.chat.completions.create(
#     model="gpt-4o",
#     messages=[{"role": "user", "content": "Explain next-token prediction."}],
#     temperature=0.3,
#     max_tokens=100
# )

# ==========================================
# 5. Industry Relevance of Temperature settings
# ==========================================
# - Use Temp = 0.0 - 0.2: For tasks requiring high accuracy, deterministic answers, or structured code/JSON extraction.
# - Use Temp = 0.7 - 1.0: For tasks requiring brainstorming, creative copy writing, or open-ended chat interactions.

"""
Key Takeaways:
- LLMs generate outputs auto-regressively, predicting one token at a time based on probability distributions.
- Temperature scales vocabulary logits: low temperature focuses on top-ranked tokens, while high temperature flattens distributions for randomness.
- Top-P (nucleus sampling) limits token candidates to a cumulative probability percentile window.

Interview Relevance:
- What is the difference between Temperature and Top-P? (Temperature scales the logits directly to stretch or flatten the probabilities; Top-P truncates the vocabulary candidates to only the top cumulative percentile, e.g. the top 90% most likely tokens, before sampling).
- Why do LLMs sometimes hallucinate? (Because they are probabilistic next-token prediction machines, selecting tokens based on mathematical weights rather than factual lookup databases).
- What temperature would you set for a SQL query generation model? (Set temperature near 0.0 to ensure deterministic, accurate syntax replication and prevent creative syntax deviations).

AI/ML Relevance:
- Production control: Fine-tuning temperature and prompt guidelines reduces generation variance in customer-facing support agents.
"""
