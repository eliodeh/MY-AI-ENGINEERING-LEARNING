# Optimization
Training a neural net = finding weights that minimize loss. You're blindfolded on a landscape, feeling the gradient (slope), trying to reach the lowest valley efficiently.

The 3 Optimizers to Build
Optimizer	Rule	Analogy
Vanilla GD	w = w - lr * gradient	Cautious walker
SGD + Momentum	v = β*v + gradient; w = w - lr*v	Ball rolling downhill
Adam	Track m (grad avg) & v (grad² avg); w = w - lr * m̂/(√v̂ + ε)	Smart walker, per-weight stride
Key Concepts
Learning rate: step size. Too small = crawl; too big = diverge. No formula — experiment. Start 0.001 (Adam), 0.01 (SGD+m).

Momentum (β≈0.9): accumulates past gradients → dampens zigzag, builds speed in consistent directions.

Adam: divides by √v̂ → each weight gets its own effective lr. Bias correction (1-β^t) fixes the cold start (m, v start at 0). Defaults: lr=0.001, β1=0.9, β2=0.999, ε=1e-8.

Convex vs non-convex: neural nets are non-convex (many local minima, saddle points). Saddle points are the real obstacle; noise + momentum escape them.

Schedules: step decay, cosine annealing, warmup. Large steps early, small steps late.

Build Steps
Rosenbrock function f(x,y)=(1-x)²+100(y-x²)² — min at (1,1), narrow curved valley.

GradientDescent — one-line update.

SGDMomentum — persistent velocity attribute.

Adam — persistent m, v, t; bias correction; divide by √v̂.

optimize() loop + compare final loss: Adam fastest, SGD+m smoothest, GD slowest.


# summary
GD = fixed-step downhill; Momentum = remember past steps for speed; Adam = per-weight adaptive stride. Build all three, race them on Rosenbrock, then sweep lr/momentum and test saddle escapessssss