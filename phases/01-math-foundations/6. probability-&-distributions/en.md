A probability distribution is a rule that says how likely each possible outcome of a random process is. It assigns a probability to every outcome (or range of outcomes), and all of those probabilities add up to 1.

Model prediction is a probability distribution, and training means making the predicted distribution match the true one.

## The Concepts

# PMF vs PDF: 
The PMF gives exact probabilities for discrete outcomes. A PDF gives a density for continuous variables, so you integrate over an interval to get a probability (and density can exceed 1).
Conditional probability and independence: P(A|B) = P(A and B) / P(B). Events are independent when P(A and B) = P(A)·P(B).
# Common distributions: 
Bernoulli (binary), categorical (multi-class), uniform (initialization), normal (the bell curve), Poisson (rare event counts).
# Expected value and variance: 
the weighted average, and the spread around it. Expected value shows up as the loss, and high gradient variance means noisy training.
# Joint and marginal distributions: 
A joint describes two variables together, and summing out one gives the marginal of the other.
# Central Limit Theorem: 
The averages of many independent samples become Gaussian regardless of the source distribution, which is why normals are everywhere.
# Log probabilities: 
adding logs replaces multiplying tiny probabilities, which avoids underflow. Cross-entropy is −log P(correct class).
# Softmax: 
turns logits into probabilities. Subtract the max logit first to prevent overflow without changing the result. Log-softmax combines both steps stably.
# Sampling: 
drawing values from a distribution (Bernoulli, categorical, Box-Muller for normals), used in dropout, language models, and diffusion.

## What you build: 
The PMFs and PDFs from scratch, expected value and variance, samplers, softmax, log-softmax, cross-entropy, and a CLT demo. Then you compare against NumPy and SciPy.

## Exercises: 
The exponential inverse-transform sampling is a loaded-dice joint table with an independence check, cross-entropy for a 5-class example (≈ 0.4209), and best-sequence log probability.