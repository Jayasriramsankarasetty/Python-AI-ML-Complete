"""
Topic:
Probability Basics & Bayes' Theorem

Importance:
Probability is the bedrock of machine learning optimization.
It models dataset uncertainty, defines optimization objectives (like maximum likelihood),
and serves as the foundation for algorithms like Naive Bayes.

This file covers:
- Conditional, Joint, and Marginal Probability
- Bayes' Theorem implementation
- Practical case study: Naive Bayes spam filter classification
"""

# ==========================================
# Formula Explanation in Comments
# ==========================================
# 1. Marginal Probability: P(A)
#    - The probability of an event A occurring, regardless of other variables.
#
# 2. Joint Probability: P(A ∩ B) or P(A, B)
#    - The probability of events A and B both occurring.
#    - Formula: P(A ∩ B) = P(A|B) * P(B)
#
# 3. Conditional Probability: P(A|B)
#    - The probability of event A occurring given that event B has already occurred.
#    - Formula: P(A|B) = P(A ∩ B) / P(B)
#
# 4. Bayes' Theorem: P(A|B) = [P(B|A) * P(A)] / P(B)
#    - Allows us to update the probability of a hypothesis (A) in light of new evidence (B).
#    - Terms:
#      - P(A|B) is the Posterior probability (what we want to calculate).
#      - P(B|A) is the Likelihood of observing evidence B given hypothesis A is true.
#      - P(A) is the Prior probability of hypothesis A being true before seeing B.
#      - P(B) is the Marginal likelihood of observing evidence B under all possible hypotheses.
#        - B can occur when A is true or when A is false: P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)

# ==========================================
# Python Implementation & Examples
# ==========================================

def calculate_bayes_theorem(prior_a, likelihood_b_given_a, likelihood_b_given_not_a):
    """
    Computes P(A|B) using Bayes' Theorem:
    P(A|B) = [P(B|A) * P(A)] / [P(B|A)*P(A) + P(B|not A)*P(not A)]
    """
    prior_not_a = 1.0 - prior_a
    
    # Calculate Marginal Likelihood P(B)
    marginal_b = (likelihood_b_given_a * prior_a) + (likelihood_b_given_not_a * prior_not_a)
    
    # Calculate Posterior Probability P(A|B)
    posterior_a_given_b = (likelihood_b_given_a * prior_a) / marginal_b
    
    return posterior_a_given_b, marginal_b


# ==========================================
# Example Data & Execution
# ==========================================
if __name__ == "__main__":
    print("=======================================")
    print("Topic: Bayes' Theorem in Action")
    print("=======================================")
    
    # Scenario: Spam Filtering
    # Let A = Email is Spam.
    # Let B = Email contains the word "Offer".
    #
    # Given dataset statistics:
    # 1. 20% of all emails received are Spam -> P(Spam) = 0.20
    # 2. 80% of spam emails contain the word "Offer" -> P("Offer" | Spam) = 0.80
    # 3. 10% of legitimate (non-spam) emails contain "Offer" -> P("Offer" | Non-Spam) = 0.10
    
    prior_spam = 0.20
    p_offer_given_spam = 0.80
    p_offer_given_non_spam = 0.10
    
    p_spam_given_offer, p_offer = calculate_bayes_theorem(
        prior_a=prior_spam,
        likelihood_b_given_a=p_offer_given_spam,
        likelihood_b_given_not_a=p_offer_given_non_spam
    )
    
    # ==========================================
    # Interpretation of Results
    # ==========================================
    print("--- Inputs (Priors & Likelihoods) ---")
    print(f"Prior Probability of Spam P(Spam):                    {prior_spam:.2f}")
    print(f"Likelihood P('Offer' | Spam):                         {p_offer_given_spam:.2f}")
    print(f"Likelihood P('Offer' | Non-Spam):                     {p_offer_given_non_spam:.2f}")
    
    print("\n--- Calculations & Outputs ---")
    print(f"Marginal probability of seeing word 'Offer' P('Offer'): {p_offer:.4f}")
    print(f"Posterior probability P(Spam | 'Offer'):               {p_spam_given_offer:.4f}")
    
    print("\n--- Interpretation ---")
    print(f"Initially, any incoming email has only a {prior_spam*100:.1f}% chance of being spam (Prior probability).")
    print(f"However, once we observe that the email contains the word 'Offer' (Evidence),")
    print(f"the probability that this email is spam rises to {p_spam_given_offer*100:.1f}% (Posterior probability).")
    print("This demonstrates how Bayes' Theorem updates our belief system upon receiving new evidence.")
    print("=======================================")

"""
Key Takeaways:
- Prior Probability represents original beliefs before checking evidence.
- Posterior Probability represents the updated belief after checking evidence.
- Bayes' Theorem updates predictions by accounting for base rate parameters (marginal likelihoods).

Interview Relevance:
- State Bayes' Theorem and explain its components.
- Given some false-positive rates of a medical test, calculate the probability of a patient having the disease given a positive test (a classic conditional probability interview question).
- What is Naive Bayes classification and why is it called 'Naive'? (It assumes all features are conditionally independent given the class label).

AI/ML Relevance:
- Classifier Models: Naive Bayes uses conditional probability products to classify text (spam vs ham, sentiment classification).
- Maximum A Posteriori (MAP): Weight optimization models in Bayesian Deep Learning look to maximize parameter posteriors under regularized priors.
"""
