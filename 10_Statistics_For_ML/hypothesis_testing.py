"""
Topic:
Statistical Hypothesis Testing & P-Values (T-Tests & Chi-Square)

Importance:
Hypothesis testing allows data scientists to prove mathematically if differences in model metrics
(e.g., A/B testing user conversions) or feature means are statistically significant or just random noise.

This file covers:
- Concepts: Null Hypothesis (H0), Alternative Hypothesis (Ha), Significance Level (alpha), P-Value
- Problem 1: One-Sample T-test (Compare sample mean to population mean)
- Problem 2: Independent Two-Sample T-test (Compare two independent sample means)
- Problem 3: Chi-Square Test of Independence (Check relationship between two categorical variables)
"""

import numpy as np
from scipy import stats

# ==========================================
# Formula Explanation in Comments
# ==========================================
# 1. Null Hypothesis (H0):
#    - The baseline assumption that there is no effect, no difference, or no relationship.
#
# 2. Alternative Hypothesis (Ha):
#    - The claim we want to prove (there is an effect, difference, or relationship).
#
# 3. Significance Level (α - alpha):
#    - The probability threshold of rejecting H0 when H0 is actually true (Type I error). Typically set to 0.05 (5%).
#
# 4. P-Value:
#    - The probability of obtaining test results at least as extreme as the observed results, assuming H0 is true.
#    - Decision Rule:
#      - If P-value <= α: Reject H0 (Results are statistically significant).
#      - If P-value > α: Fail to reject H0 (Results are not statistically significant).
#
# 5. T-Test (Student's T-Test):
#    - Used to compare means of continuous variables when standard deviations are unknown and sample size is relatively small.
#    - One-sample: t = (x̄ - μ) / (s / √N)
#    - Two-sample: t = (x̄1 - x̄2) / √((s1²/N1) + (s2²/N2))
#
# 6. Chi-Square Test of Independence (χ²):
#    - Used to check if two categorical variables are independent of each other.
#    - Formula: χ² = Σ (Observed - Expected)² / Expected

# ==========================================
# Python Implementation & Verification
# ==========================================

# 1. One-Sample T-test
def run_one_sample_t_test(sample, population_mean, alpha=0.05):
    t_stat, p_value = stats.ttest_1samp(sample, popmean=population_mean)
    decision = "Reject H0" if p_value <= alpha else "Fail to reject H0"
    return t_stat, p_value, decision

# 2. Two-Sample Independent T-test
def run_two_sample_t_test(sample_1, sample_2, alpha=0.05):
    # equal_var=False performs Welch's T-test (does not assume equal variance)
    t_stat, p_value = stats.ttest_ind(sample_1, sample_2, equal_var=False)
    decision = "Reject H0" if p_value <= alpha else "Fail to reject H0"
    return t_stat, p_value, decision

# 3. Chi-Square Test of Independence
def run_chi_square_test(contingency_table, alpha=0.05):
    # stats.chi2_contingency returns chi2, p, dof, expected_table
    chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    decision = "Reject H0" if p_value <= alpha else "Fail to reject H0"
    return chi2_stat, p_value, decision


# ==========================================
# Example Data & Execution
# ==========================================
if __name__ == "__main__":
    print("=======================================")
    print("Topic: Statistical Hypothesis Testing")
    print("=======================================")
    alpha_threshold = 0.05
    
    # ------------------------------------------
    # Test 1: One-Sample T-test
    # ------------------------------------------
    # Scenario: The historical baseline exam score is 70. A prep class of 10 students scored:
    student_scores = [72, 75, 68, 74, 78, 80, 71, 73, 76, 75]
    pop_mean = 70
    
    t_stat_1, p_val_1, dec_1 = run_one_sample_t_test(student_scores, pop_mean, alpha_threshold)
    
    print("\n--- 1. One-Sample T-test ---")
    print(f"Sample scores: {student_scores} | Population Mean: {pop_mean}")
    print(f"T-statistic: {t_stat_1:.4f} | P-value: {p_val_1:.6f}")
    print(f"Decision (alpha={alpha_threshold}): {dec_1}")
    if dec_1 == "Reject H0":
        print("Interpretation: The prep class students scored significantly higher than the baseline average of 70.")
    else:
        print("Interpretation: The difference in scores is not statistically significant from baseline 70.")

    # ------------------------------------------
    # Test 2: Two-Sample Independent T-test (A/B testing)
    # ------------------------------------------
    # Scenario: Website layouts conversion rates. We check time spent on website (in seconds):
    layout_A_time = [45, 50, 48, 52, 47, 55, 49, 51, 46, 53]
    layout_B_time = [60, 58, 62, 65, 59, 61, 63, 64, 57, 62]  # looks significantly higher
    
    t_stat_2, p_val_2, dec_2 = run_two_sample_t_test(layout_A_time, layout_B_time, alpha_threshold)
    
    print("\n--- 2. Two-Sample Independent T-test (A/B Test) ---")
    print(f"Layout A Mean: {np.mean(layout_A_time):.1f}s | Layout B Mean: {np.mean(layout_B_time):.1f}s")
    print(f"T-statistic: {t_stat_2:.4f} | P-value: {p_val_2:.8f}")
    print(f"Decision (alpha={alpha_threshold}): {dec_2}")
    if dec_2 == "Reject H0":
        print("Interpretation: Layout B leads to a statistically significant increase in website user engagement time.")
    else:
        print("Interpretation: There is no significant difference in engagement times between layout A and B.")

    # ------------------------------------------
    # Test 3: Chi-Square Test of Independence
    # ------------------------------------------
    # Scenario: Check if clicking an ad (Yes/No) depends on gender (Male/Female).
    # Contingency Table:
    #          Clicked  No-Clicked
    # Male     [ 40,       60 ]
    # Female   [ 80,       20 ]
    contingency = [
        [40, 60],
        [80, 20]
    ]
    
    chi2_stat_3, p_val_3, dec_3 = run_chi_square_test(contingency, alpha_threshold)
    
    print("\n--- 3. Chi-Square Test of Independence ---")
    print("Contingency Table (Gender vs Clicked):\n", np.array(contingency))
    print(f"Chi-square Statistic: {chi2_stat_3:.4f} | P-value: {p_val_3:.8f}")
    print(f"Decision (alpha={alpha_threshold}): {dec_3}")
    if dec_3 == "Reject H0":
        print("Interpretation: Ad click rate has a statistically significant relationship with user gender.")
    else:
        print("Interpretation: Gender and Ad clicking behavior are independent of each other.")
    print("=======================================")

"""
Key Takeaways:
- Hypothesis tests yield a test statistic and a P-value representing probability of H0 occurrence.
- If P-value <= 0.05, we reject the null hypothesis (proving significance).
- Two-sample independent t-tests evaluate two distinct groups; chi-square tests check dependencies between categorical groups.

Interview Relevance:
- What is a P-value? (The probability of observing the data, or something more extreme, assuming the null hypothesis is true. A low P-value rejects the null hypothesis).
- Explain Type I and Type II errors. (Type I error is a False Positive: rejecting H0 when it is true. Type II error is a False Negative: failing to reject H0 when it is false).
- When would you use a Chi-Square test over a T-test? (Use Chi-Square when analyzing relationship dependency between two *categorical* variables; use T-test when comparing *numerical* means of continuous variables).

AI/ML Relevance:
- A/B Testing: Deploying model version B to a subset of users and testing if conversions increase significantly uses independent two-sample t-tests.
- Feature Selection: Checking if a categorical input feature relates to a categorical target label utilizes Chi-Square test values to drop unassociated features.
"""
