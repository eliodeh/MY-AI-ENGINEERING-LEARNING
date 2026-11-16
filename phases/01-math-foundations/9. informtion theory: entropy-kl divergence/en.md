# Information Theory
the lesson talks about information theory and it help with machine learning models to make good predictions.

# defination
Information theory shows how information is measured, how uncertainty works and be represented efficiently
# Examples:
a two side coin tossed, you dont know which side will appear that is called uncertainty
like: head 50% chance and tail 2% chance.
# Other theories includes:
1. Information content = it shows how surprising an event is. 
the formula is:
I(x) = -log2(P(x))
where:
. I(x)= information content or surprise
. P(x) = probability of the event
. log2 = logarithm with base 2
2. Entropy(average surprise) = this measures the average uncertainty in a probability distribution
3. cross-entropy(classification loss function) = it measures how well a model predicted probabilities match the actual answers.
4. cross-Entropy(the classification loss ffunction) = this concept measures how good predicted probabilities match the actual answers.

KL Divergence measures the extra information wasted when you use the models distribution instead of the true distribution
the formula is:

D_{KL}(P\|Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}

where:
. P = actual probability distribution
Q = predicted probability distribution
  CrossEntropy = entropy + KL Divergence
  6. Mutual Information= this measures how much knowing one variable helps to understand another variable
