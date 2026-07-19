"""
Topic:
Probability Distributions: Uniform, Normal, Binomial, and Poisson

Importance:
Many ML algorithms (such as Linear Regression and Gaussian Naive Bayes) assume
features are normally distributed. Understanding distribution shapes and densities is essential
for simulating processes and transforming real-world variables.

This file covers:
- Uniform Distribution (Continuous)
- Normal/Gaussian Distribution (Continuous, Central Limit Theorem)
- Binomial Distribution (Discrete trials)
- Poisson Distribution (Discrete events rate)
"""

import numpy as np
from scipy import stats

# ==========================================
# Formula Explanation in Comments
# ==========================================
# 1. Uniform Distribution (Continuous):
#    - All outcomes in range [a, b] are equally likely.
#    - Probability Density Function (PDF): f(x) = 1 / (b - a) for a <= x <= b.
#
# 2. Normal (Gaussian) Distribution (Continuous):
#    - Bell-shaped symmetric curve centered at mean μ with spread standard deviation σ.
#    - Probability Density Function (PDF): f(x) = [1 / (σ * √2π)] * e^(-0.5 * ((x - μ) / σ)²)
#    - Empirical Rule:
#      - ~68% of data falls within 1σ of the mean.
#      - ~95% of data falls within 2σ of the mean.
#      - ~99.7% of data falls within 3σ of the mean.
#
# 3. Binomial Distribution (Discrete):
#    - Number of successes 'k' in 'n' independent Bernoulli trials, each with success probability 'p'.
#    - Probability Mass Function (PMF): P(X = k) = nCr * p^k * (1-p)^(n-k), where nCr = n! / (k! * (n-k)!)
#
# 4. Poisson Distribution (Discrete):
#    - Probability of a given number of events 'k' occurring in a fixed interval of time/space,
#      given a constant average event rate 'λ' (lambda).
#    - Probability Mass Function (PMF): P(X = k) = (λ^k * e^-λ) / k!

# ==========================================
# Python Implementation & Verification
# ==========================================

if __name__ == "__main__":
    print("=======================================")
    print("Topic: Probability Distributions")
    print("=======================================")
    
    # ------------------------------------------
    # 1. Continuous Uniform Distribution
    # ------------------------------------------
    print("\n--- 1. Continuous Uniform Distribution ---")
    low_bound, high_bound = 10, 20
    # Expected mean = (a + b) / 2 = 15
    # PDF height = 1 / (20 - 10) = 0.1
    uniform_pdf_val = stats.uniform.pdf(x=15, loc=low_bound, scale=high_bound-low_bound)
    print(f"Parameters: Range [{low_bound}, {high_bound}]")
    print(f"PDF height at midpoint x=15: {uniform_pdf_val:.4f} (Expected: 1/(20-10) = 0.10)")

    # ------------------------------------------
    # 2. Normal (Gaussian) Distribution
    # ------------------------------------------
    print("\n--- 2. Normal (Gaussian) Distribution ---")
    mean_val, std_dev = 170, 10  # e.g., adult height in cm
    normal_dist = stats.norm(loc=mean_val, scale=std_dev)
    
    # PDF heights at center and sides
    pdf_at_mean = normal_dist.pdf(mean_val)
    pdf_at_1std = normal_dist.pdf(mean_val + std_dev)
    
    # Cumulative Distribution Function (CDF) represents probability of X <= x
    # Probability height <= 180 (within +1 standard deviation)
    prob_less_180 = normal_dist.cdf(180)
    # Probability between 160 and 180 (within +/- 1 standard deviation)
    prob_within_1std = normal_dist.cdf(180) - normal_dist.cdf(160)
    
    print(f"Parameters: Mean mu = {mean_val}cm | Std Dev sigma = {std_dev}cm")
    print(f"Probability Density (PDF) at Mean:                   {pdf_at_mean:.4f}")
    print(f"Probability Density (PDF) at 1 Std Dev (180cm):      {pdf_at_1std:.4f}")
    print(f"Probability of Height <= 180cm (CDF):                {prob_less_180*100:.2f}%")
    print(f"Probability of Height within 160-180cm (Empirical):  {prob_within_1std*100:.2f}% (Expected: ~68%)")

    # ------------------------------------------
    # 3. Binomial Distribution
    # ------------------------------------------
    print("\n--- 3. Binomial Distribution ---")
    # Scenario: flipping a coin (p=0.5) 10 times. Probability of getting exactly 5 heads (k=5).
    num_trials = 10
    prob_success = 0.5
    k_successes = 5
    binom_pmf_val = stats.binom.pmf(k=k_successes, n=num_trials, p=prob_success)
    print(f"Parameters: Trials n = {num_trials} | Success Prob p = {prob_success}")
    print(f"Probability of exactly {k_successes} successes (PMF): {binom_pmf_val*100:.2f}%")

    # ------------------------------------------
    # 4. Poisson Distribution
    # ------------------------------------------
    print("\n--- 4. Poisson Distribution ---")
    # Scenario: a customer service center gets an average of 4 calls per hour (lambda = 4).
    # Probability of getting exactly 6 calls in an hour (k = 6).
    avg_rate = 4
    actual_events = 6
    poisson_pmf_val = stats.poisson.pmf(k=actual_events, mu=avg_rate)
    print(f"Parameters: Average Event Rate lambda = {avg_rate}")
    print(f"Probability of getting exactly {actual_events} calls (PMF): {poisson_pmf_val*100:.2f}%")
    print("=======================================")

"""
Key Takeaways:
- Continuous distributions use Probability Density Functions (PDF) where area under the curve equals 1.
- Discrete distributions use Probability Mass Functions (PMF) calculating probabilities of exact integers.
- The Cumulative Distribution Function (CDF) measures the accumulated probability area up to value X.

Interview Relevance:
- State the Empirical Rule (68-95-99.7) for normal distributions.
- Explain the difference between PDF (Probability Density Function) and PMF (Probability Mass Function). (PDF applies to continuous variables where the probability at a single point is zero; PMF applies to discrete variables representing exact probabilities).
- When would you use Poisson vs Binomial? (Binomial represents events with a fixed number of trials; Poisson represents events occurring randomly in a continuous interval where trials are infinite/untracked).

AI/ML Relevance:
- Algorithms Assumptions: Linear Regressions assume residual errors follow a Gaussian Normal distribution.
- Classifiers: Gaussian Naive Bayes calculates likelihood using normal distribution PDF equations.
- Generative Models: VAEs (Variational Autoencoders) map latent dimensions to standard normal distributions (mean=0, std=1).
"""
