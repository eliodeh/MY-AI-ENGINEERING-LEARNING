All generative AI is sampling: you can only make uniform random numbers, so every method (inverse CDF, rejection, MCMC, temperature, top-k/top-p, reparameterization) is just a trick to turn U ~ [0,1) into draws from a target distribution — and the chosen trick controls the output's diversity, quality, and controllability.

1. Inverse CDF works because P(F⁻¹(U) ≤ x) = F(x) — uniform randomness maps directly to any distribution.

2. Rejection's killer flaw: acceptance rate collapses as dimensions grow (curse of dimensionality).

3. MCMC's magic: you only need p(x) up to a constant — normalization cancels in the ratio.

4. Detailed balance is why MCMC converges: p(x)T(x→y) = p(y)T(y→x).

5. Temperature doesn't change which tokens are possible — it changes how probability mass is allocated.

6. Top-p > Top-k because it adapts: few tokens when confident, many when uncertain.

7. Reparameterization separates randomness (ε) from parameters (μ,σ), so gradients flow — this single trick made VAEs trainable.

8. Gumbel-Softmax = differentiable categorical sampling; τ→0 gives hard one-hot, τ→∞ gives uniform.

9. Diffusion models = iterative sampling: start from noise, denoise step-by-step (each step uses reparameterization).

