
# what is Baye's theorem?
Bayes' theorem says: posterior ∝ likelihood × prior. Compute the evidence as a normalizer via total probability, then divide. Rare conditions produce mostly false positives even with accurate tests, because the prior dominates. Naive Bayes scales this to many features by assuming independence, using Laplace smoothing to kill zeros and logs to kill underflow. MAP adds a prior over parameters = regularization. Conjugate priors (Beta-Binomial) make updating pure addition, enabling sequential/online learning and clean Bayesian A/B tests via Monte Carlo on 
P(B>A).


# Why It Matters for ML
Priors = regularization

Posteriors = uncertainty quantification

Bayes updates = online learning

Model comparison (BIC, Bayes factors) = Bayesian reasoning.



# Formula

P(A∣B)= P(B)P(B∣A)⋅P(A)
        _______________
            P(B)
​  

 

