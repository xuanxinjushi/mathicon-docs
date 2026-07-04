# Icons reference gallery

Welcome to the complete Mathicon gallery. This reference page is automatically compiled, showcasing all built-in static and animated icons.

## Mathematical Primitives & Core Topics
These icons represent specific mathematical topics and are matched to the chapters of the *Mathematics for AI* textbook.

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
| **activation_deriv**<br>*Activation Derivative* | ![activation_deriv](images/icons/activation_deriv.png) | Static Only | Shows the local slope of a nonlinear activation, used when explaining backpropagation and chain-rule gradients. |
| **bayes**<br>*Bayes' Rule* | ![bayes](images/icons/bayes.png) | Static Only | Represents updating a prior belief into a posterior after observing evidence. |
| **bellman**<br>*Bellman Equation* | ![bellman](images/icons/bellman.png) | Static Only | Summarizes recursive value decomposition in dynamic programming and reinforcement learning. |
| **brownian_motion**<br>*Brownian Motion* | ![brownian_motion](images/icons/brownian_motion.png) | ![brownian_motion gif](images/icons/brownian_motion.gif) | Represents continuous random motion, the noise source behind many SDE and diffusion models. |
| **cauchy_schwarz**<br>*Cauchy-Schwarz* | ![cauchy_schwarz](images/icons/cauchy_schwarz.png) | Static Only | Represents the inner-product inequality bounding $|u^T v|$ by the product of vector norms. |
| **chain_rule**<br>*Chain Rule* | ![chain_rule](images/icons/chain_rule.png) | Static Only | Shows how derivatives compose through nested functions and computational graphs. |
| **cholesky**<br>*Cholesky Decomposition* | ![cholesky](images/icons/cholesky.png) | Static Only | Represents factoring a positive-definite matrix into triangular factors. |
| **column_row_space**<br>*Column And Row Spaces* | ![column_row_space](images/icons/column_row_space.png) | Static Only | Highlights the fundamental subspaces associated with a matrix. |
| **convex_set**<br>*Convex Set* | ![convex_set](images/icons/convex_set.png) | Static Only | Shows a set where every segment between two points remains inside the set. |
| **covariance**<br>*Covariance* | ![covariance](images/icons/covariance.png) | Static Only | Represents how variables vary together and how probability mass stretches along correlated directions. |
| **cross_entropy**<br>*Cross Entropy* | ![cross_entropy](images/icons/cross_entropy.png) | Static Only | Represents the loss comparing a target distribution against predicted probabilities. |
| **denoising**<br>*Denoising Score Matching* | ![denoising](images/icons/denoising.png) | ![denoising gif](images/icons/denoising.gif) | Shows a noisy sample $\tilde{\mathbf{x}}$ converging toward clean data $\mathbf{x}_0$ along the learned score direction $s_\theta$. |
| **density_evolution**<br>*Density Evolution* | ![density_evolution](images/icons/density_evolution.png) | ![density_evolution gif](images/icons/density_evolution.gif) | Shows a probability density $p(x,t)$ spreading and flattening under Fokker–Planck diffusion from $t_0$ to $t_1$. |
| **det_area**<br>*Determinant As Area* | ![det_area](images/icons/det_area.png) | Static Only | Shows determinant magnitude as the area or volume scaling induced by a linear map. |
| **diffusion_model**<br>*Diffusion Model* | ![diffusion_model](images/icons/diffusion_model.png) | Static Only | Represents the noise-to-data generative process used in modern diffusion models. |
| **diffusion_scores**<br>*Diffusion Scores* | ![diffusion_scores](images/icons/diffusion_scores.png) | ![diffusion_scores gif](images/icons/diffusion_scores.gif) | Shows score fields $s_t(\mathbf{x})$ at increasing noise levels $t{=}0, t{=}1, \ldots, T$ in a diffusion process. |
| **eigendecomp**<br>*Eigendecomposition* | ![eigendecomp](images/icons/eigendecomp.png) | Static Only | Shows a matrix decomposed into eigenvectors and eigenvalues. |
| **elbo**<br>*ELBO* | ![elbo](images/icons/elbo.png) | Static Only | Represents the evidence lower bound used in variational inference and latent-variable models. |
| **entropy**<br>*Entropy* | ![entropy](images/icons/entropy.png) | Static Only | Represents uncertainty, spread, or information content in a probability distribution. |
| **flow_attractors**<br>*Flow Attractors* | ![flow_attractors](images/icons/flow_attractors.png) | ![flow_attractors gif](images/icons/flow_attractors.gif) | Shows score-induced flows converging toward density modes (attractors) of a multimodal distribution. |
| **fokker_planck**<br>*Fokker-Planck Equation* | ![fokker_planck](images/icons/fokker_planck.png) | Static Only | Shows the time evolution of a probability density under stochastic dynamics. |
| **forward_diffusion**<br>*Forward Diffusion* | ![forward_diffusion](images/icons/forward_diffusion.png) | ![forward_diffusion gif](images/icons/forward_diffusion.gif) | Forward diffusion corrupts a structured data density (bimodal $p_{\mathrm{data}}$) into a wide Gaussian noise distribution as $t \uparrow$; animation shows peaks merging and flattening. |
| **frechet**<br>*Fréchet Derivative* | ![frechet](images/icons/frechet.png) | Static Only | Represents the derivative of a map between normed spaces, generalizing the Jacobian to infinite dimensions. |
| **gaussian**<br>*Gaussian Distribution* | ![gaussian](images/icons/gaussian.png) | Static Only | Represents the normal distribution and its mean/covariance geometry. |
| **gradient**<br>*Gradient* | ![gradient](images/icons/gradient.png) | Static Only | Shows the direction of steepest local increase for a scalar function. |
| **gram_schmidt**<br>*Gram-Schmidt* | ![gram_schmidt](images/icons/gram_schmidt.png) | Static Only | Represents turning a list of vectors into an orthonormal basis by subtracting projections. |
| **hessian**<br>*Hessian* | ![hessian](images/icons/hessian.png) | Static Only | Represents second-order curvature information for scalar functions. |
| **householder**<br>*Householder Reflection* | ![householder](images/icons/householder.png) | Static Only | Shows reflection-based orthogonal transformations used in QR factorization. |
| **jacobian**<br>*Jacobian* | ![jacobian](images/icons/jacobian.png) | Static Only | Represents the matrix of first derivatives for a vector-valued map. |
| **kl**<br>*KL Divergence* | ![kl](images/icons/kl.png) | Static Only | Represents the directed mismatch between two probability distributions. |
| **kronecker**<br>*Kronecker Product* | ![kronecker](images/icons/kronecker.png) | Static Only | Shows block-structured multiplication between matrices. |
| **langevin_sampling**<br>*Langevin Sampling* | ![langevin_sampling](images/icons/langevin_sampling.png) | ![langevin_sampling gif](images/icons/langevin_sampling.gif) | Langevin MCMC chain: each step follows score-driven drift (blue) plus injected noise (red), gradually exploring toward a density mode. |
| **langevin_step**<br>*Langevin Step* | ![langevin_step](images/icons/langevin_step.png) | ![langevin_step gif](images/icons/langevin_step.gif) | Single Langevin update from $x_k$: dashed blue drift along $\nabla\log p$ versus red step that adds a noise kick beyond the drift target. |
| **level_set_normal**<br>*Gradient Normal to a Level Set* | ![level_set_normal](images/icons/level_set_normal.png) | Static Only | Shows the gradient as a vector normal to level sets of a scalar field. |
| **lu**<br>*LU Factorization* | ![lu](images/icons/lu.png) | Static Only | Represents decomposing a matrix into lower and upper triangular factors. |
| **markov**<br>*Markov Chain* | ![markov](images/icons/markov.png) | Static Only | Shows state transitions where the next state depends only on the current state. |
| **matrix_exponential**<br>*Matrix Exponential* | ![matrix_exponential](images/icons/matrix_exponential.png) | Static Only | Represents exp(A), the operator used to solve linear differential equations. |
| **mutual_info**<br>*Mutual Information* | ![mutual_info](images/icons/mutual_info.png) | Static Only | Represents shared information between random variables. |
| **newton**<br>*Newton Method* | ![newton](images/icons/newton.png) | Static Only | Shows curvature-aware optimization using gradient and Hessian information. |
| **noise_exploration**<br>*Noise Exploration* | ![noise_exploration](images/icons/noise_exploration.png) | ![noise_exploration gif](images/icons/noise_exploration.gif) | Contrasts noise-driven exploration: a purple sample cloud spreads inside the dashed region while a red mode point stays sharp. |
| **norms**<br>*Vector Norms* | ![norms](images/icons/norms.png) | Static Only | Compares different notions of vector length and their unit-ball geometry. |
| **orthonormal_matrix**<br>*Orthonormal Matrix* | ![orthonormal_matrix](images/icons/orthonormal_matrix.png) | Static Only | Represents matrices whose columns or rows preserve lengths and angles. |
| **polar**<br>*Polar Decomposition* | ![polar](images/icons/polar.png) | Static Only | Shows a matrix split into a rotation/reflection part and a symmetric stretch. |
| **policy_gradient**<br>*Policy Gradient* | ![policy_gradient](images/icons/policy_gradient.png) | Static Only | Represents optimizing a reinforcement-learning policy by following reward gradients. |
| **probability_current**<br>*Probability Current* | ![probability_current](images/icons/probability_current.png) | ![probability_current gif](images/icons/probability_current.gif) | Continuity equation in a control volume: blue $J_{\mathrm{in}}$ exceeds red $J_{\mathrm{out}}$ early so $p$ builds, then flux balances at $\partial_t p + \nabla\cdot J = 0$. |
| **projection**<br>*Projection* | ![projection](images/icons/projection.png) | Static Only | Shows dropping a vector onto a subspace and separating residual error. |
| **pseudoinverse**<br>*Pseudoinverse* | ![pseudoinverse](images/icons/pseudoinverse.png) | Static Only | Represents the generalized inverse used for least-squares and rank-deficient systems. |
| **qr**<br>*QR Factorization* | ![qr](images/icons/qr.png) | Static Only | Represents decomposing a matrix into an orthonormal factor Q and triangular factor R. |
| **rayleigh**<br>*Rayleigh Quotient* | ![rayleigh](images/icons/rayleigh.png) | Static Only | Shows how a vector probes eigenvalue-like curvature of a symmetric matrix. |
| **reverse_sde**<br>*Reverse SDE* | ![reverse_sde](images/icons/reverse_sde.png) | ![reverse_sde gif](images/icons/reverse_sde.gif) | Time-reversed SDE denoises a sample from noise (gray, right) back to data (blue, left); animation traces the state along the red reverse arrow opposite the black forward corruption path. |
| **rotation**<br>*Rotation* | ![rotation](images/icons/rotation.png) | ![rotation gif](images/icons/rotation.gif) | Represents a length-preserving turn in the plane. |
| **scalar_vector**<br>*Scalar vs Vector Fields* | ![scalar_vector](images/icons/scalar_vector.png) | Static Only | Contrasts a scalar field (one value per point) with a vector field (direction and magnitude at each point). |
| **scaling**<br>*Scaling* | ![scaling](images/icons/scaling.png) | ![scaling gif](images/icons/scaling.gif) | Represents axis-aligned stretching or compression of space by a diagonal linear map. |
| **schur**<br>*Schur Decomposition* | ![schur](images/icons/schur.png) | Static Only | Represents triangularization by a unitary or orthogonal change of basis. |
| **score_field**<br>*Score Field* | ![score_field](images/icons/score_field.png) | ![score_field gif](images/icons/score_field.gif) | Visualizes ∇_x log p(x) as arrows over a density landscape. |
| **score_function**<br>*Score Function* | ![score_function](images/icons/score_function.png) | Static Only | Represents the gradient of log-density, pointing toward higher probability. |
| **score_matching**<br>*Score Matching* | ![score_matching](images/icons/score_matching.png) | Static Only | Represents learning a score field directly from samples or noisy samples. |
| **sde_path**<br>*SDE Sample Path* | ![sde_path](images/icons/sde_path.png) | ![sde_path gif](images/icons/sde_path.gif) | Continuous-time SDE sample path $x_t$ driven by Brownian noise; animation grows the noisy trajectory from $t{=}0$ to $T$ along the time axis. |
| **sgld**<br>*SGLD* | ![sgld](images/icons/sgld.png) | Static Only | Represents stochastic-gradient Langevin dynamics for noisy optimization and sampling. |
| **shear**<br>*Shear* | ![shear](images/icons/shear.png) | ![shear gif](images/icons/shear.gif) | Represents a shear transformation that slants one axis relative to the other while preserving area. |
| **spectral**<br>*Spectral View* | ![spectral](images/icons/spectral.png) | Static Only | Represents reasoning through eigenvalues, singular values, or frequency-like modes. |
| **ste_subgradient**<br>*Straight-Through Estimator & Subgradient* | ![ste_subgradient](images/icons/ste_subgradient.png) | Static Only | Shows subgradients at nondifferentiable points and the straight-through estimator used in discrete layers. |
| **svd**<br>*Singular Value Decomposition* | ![svd](images/icons/svd.png) | Static Only | Shows a matrix as rotations/reflections plus axis-aligned stretching. |
| **taylor**<br>*Taylor Approximation* | ![taylor](images/icons/taylor.png) | Static Only | Represents local polynomial approximation of a function. |
| **tensor_block**<br>*Volumetric 3D Tensor Block* | ![tensor_block](images/icons/tensor_block.png) | Static Only | Represents a 3D volumetric tensor (Channels, Height, Width) projected onto a 2D isometric grid, useful for neural network layout blocks. |
| **three_levels**<br>*Paths vs Densities: Three Levels* | ![three_levels](images/icons/three_levels.png) | ![three_levels gif](images/icons/three_levels.gif) | Path-level SDEs (top), probability-flow ODE (middle), and Fokker--Planck density (bottom); animation advances time so sample paths extend, flow grows, and $p(x,t)$ spreads. |
| **trust_region**<br>*Trust Region* | ![trust_region](images/icons/trust_region.png) | Static Only | Shows constrained local optimization inside a region where the model is trusted. |
| **value_iteration**<br>*Value Iteration* | ![value_iteration](images/icons/value_iteration.png) | Static Only | Represents repeatedly applying Bellman updates to compute values. |

## Matrix Icons
Matrix shapes and layouts using the book legend color scheme (`chapterx/img/legend.py`). Use these ids in mindmaps for consistent matrix taxonomy.

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
| **antidiagonal_matrix**<br>*Antidiagonal Matrix* | ![antidiagonal_matrix](images/icons/antidiagonal_matrix.png) | Static Only | Mindmap icon for Antidiagonal Matrix. Used to represent the antidiagonal matrix concept in Math4AI diagrams. |
| **column_vector**<br>*Column Vector* | ![column_vector](images/icons/column_vector.png) | Static Only | Mindmap icon for Column Vector. Used to represent the column vector concept in Math4AI diagrams. |
| **diagonal_matrix**<br>*Diagonal Matrix* | ![diagonal_matrix](images/icons/diagonal_matrix.png) | Static Only | Mindmap icon for Diagonal Matrix. Used to represent the diagonal matrix concept in Math4AI diagrams. |
| **eigenvector_matrix**<br>*Eigenvector Matrix* | ![eigenvector_matrix](images/icons/eigenvector_matrix.png) | Static Only | Mindmap icon for Eigenvector Matrix. Used to represent the eigenvector matrix concept in Math4AI diagrams. |
| **generalized_upper_triangular_matrix**<br>*Generalized Upper Triangular Matrix* | ![generalized_upper_triangular_matrix](images/icons/generalized_upper_triangular_matrix.png) | Static Only | Mindmap icon for Generalized Upper Triangular Matrix. Used to represent the generalized upper triangular matrix concept in Math4AI diagrams. |
| **lower_triangular_matrix**<br>*Lower Triangular Matrix* | ![lower_triangular_matrix](images/icons/lower_triangular_matrix.png) | Static Only | Mindmap icon for Lower Triangular Matrix. Used to represent the lower triangular matrix concept in Math4AI diagrams. |
| **lower_unit_triangular_matrix**<br>*Lower Unit Triangular Matrix* | ![lower_unit_triangular_matrix](images/icons/lower_unit_triangular_matrix.png) | Static Only | Mindmap icon for Lower Unit Triangular Matrix. Used to represent the lower unit triangular matrix concept in Math4AI diagrams. |
| **nonnegative_matrix**<br>*Nonnegative Matrix* | ![nonnegative_matrix](images/icons/nonnegative_matrix.png) | Static Only | Mindmap icon for Nonnegative Matrix. Used to represent the nonnegative matrix concept in Math4AI diagrams. |
| **orthogonal_matrix**<br>*Orthogonal Matrix* | ![orthogonal_matrix](images/icons/orthogonal_matrix.png) | Static Only | Mindmap icon for Orthogonal Matrix. Used to represent the orthogonal matrix concept in Math4AI diagrams. |
| **permutation_matrix**<br>*Permutation Matrix* | ![permutation_matrix](images/icons/permutation_matrix.png) | Static Only | Mindmap icon for Permutation Matrix. Used to represent the permutation matrix concept in Math4AI diagrams. |
| **rect_matrix**<br>*Rect Matrix* | ![rect_matrix](images/icons/rect_matrix.png) | Static Only | Mindmap icon for Rect Matrix. Used to represent the rect matrix concept in Math4AI diagrams. |
| **rectangular_matrix**<br>*Rectangular Matrix* | ![rectangular_matrix](images/icons/rectangular_matrix.png) | Static Only | Mindmap icon for Rectangular Matrix. Used to represent the rectangular matrix concept in Math4AI diagrams. |
| **row_vector**<br>*Row Vector* | ![row_vector](images/icons/row_vector.png) | Static Only | Mindmap icon for Row Vector. Used to represent the row vector concept in Math4AI diagrams. |
| **square_matrix**<br>*Square Matrix* | ![square_matrix](images/icons/square_matrix.png) | Static Only | Mindmap icon for Square Matrix. Used to represent the square matrix concept in Math4AI diagrams. |
| **symmetric_matrix**<br>*Symmetric Matrix* | ![symmetric_matrix](images/icons/symmetric_matrix.png) | Static Only | Mindmap icon for Symmetric Matrix. Used to represent the symmetric matrix concept in Math4AI diagrams. |
| **tall_matrix**<br>*Tall Matrix* | ![tall_matrix](images/icons/tall_matrix.png) | Static Only | Mindmap icon for Tall Matrix. Used to represent the tall matrix concept in Math4AI diagrams. |
| **triangular_matrix**<br>*Triangular Matrix* | ![triangular_matrix](images/icons/triangular_matrix.png) | Static Only | Mindmap icon for Triangular Matrix. Used to represent the triangular matrix concept in Math4AI diagrams. |
| **upper_triangular_matrix**<br>*Upper Triangular Matrix* | ![upper_triangular_matrix](images/icons/upper_triangular_matrix.png) | Static Only | Mindmap icon for Upper Triangular Matrix. Used to represent the upper triangular matrix concept in Math4AI diagrams. |
| **wide_matrix**<br>*Wide Matrix* | ![wide_matrix](images/icons/wide_matrix.png) | Static Only | Mindmap icon for Wide Matrix. Used to represent the wide matrix concept in Math4AI diagrams. |

## Neural Network Icons
Architecture diagrams rendered with [visualtorch](https://github.com/willyfh/visualtorch). Requires `pip install mathicon[nn]` (torch + aggdraw).

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
| **nn_mlp**<br>*Neural Network MLP* | ![nn_mlp](images/icons/nn_mlp.png) | Static Only | Minimal dense feedforward network (2→3→2) as a node-link graph (visualtorch graph style). |

## Other Miscellaneous Icons

| Key / Title | Static Image | Loopable GIF | Concept & Role |
| :--- | :---: | :---: | :--- |
| **basis_dim**<br>*Basis Dim* | ![basis_dim](images/icons/basis_dim.png) | Static Only | Mindmap icon for Basis Dim. Used to represent the basis dim concept in Math4AI diagrams. |
| **bellman_backup**<br>*Bellman Backup* | ![bellman_backup](images/icons/bellman_backup.png) | Static Only | Mindmap icon for Bellman Backup. Used to represent the bellman backup concept in Math4AI diagrams. |
| **beta_dirichlet_vmf**<br>*Beta Dirichlet Vmf* | ![beta_dirichlet_vmf](images/icons/beta_dirichlet_vmf.png) | Static Only | Mindmap icon for Beta Dirichlet Vmf. Used to represent the beta dirichlet vmf concept in Math4AI diagrams. |
| **block_lu**<br>*Block Lu* | ![block_lu](images/icons/block_lu.png) | Static Only | Mindmap icon for Block Lu. Used to represent the block lu concept in Math4AI diagrams. |
| **block_matrix**<br>*Block Matrix* | ![block_matrix](images/icons/block_matrix.png) | Static Only | Mindmap icon for Block Matrix. Used to represent the block matrix concept in Math4AI diagrams. |
| **column_span**<br>*Column Span* | ![column_span](images/icons/column_span.png) | Static Only | Mindmap icon for Column Span. Used to represent the column span concept in Math4AI diagrams. |
| **contraction**<br>*Contraction* | ![contraction](images/icons/contraction.png) | Static Only | Mindmap icon for Contraction. Used to represent the contraction concept in Math4AI diagrams. |
| **ctmc**<br>*Ctmc* | ![ctmc](images/icons/ctmc.png) | Static Only | Mindmap icon for Ctmc. Used to represent the ctmc concept in Math4AI diagrams. |
| **ddim**<br>*Ddim* | ![ddim](images/icons/ddim.png) | Static Only | Mindmap icon for Ddim. Used to represent the ddim concept in Math4AI diagrams. |
| **definiteness**<br>*Definiteness* | ![definiteness](images/icons/definiteness.png) | Static Only | Mindmap icon for Definiteness. Used to represent the definiteness concept in Math4AI diagrams. |
| **detailed_balance**<br>*Detailed Balance* | ![detailed_balance](images/icons/detailed_balance.png) | Static Only | Mindmap icon for Detailed Balance. Used to represent the detailed balance concept in Math4AI diagrams. |
| **diffusion_unify**<br>*Diffusion Unify* | ![diffusion_unify](images/icons/diffusion_unify.png) | Static Only | Mindmap icon for Diffusion Unify. Used to represent the diffusion unify concept in Math4AI diagrams. |
| **duality**<br>*Duality* | ![duality](images/icons/duality.png) | Static Only | Mindmap icon for Duality. Used to represent the duality concept in Math4AI diagrams. |
| **ebm**<br>*Ebm* | ![ebm](images/icons/ebm.png) | Static Only | Mindmap icon for Ebm. Used to represent the ebm concept in Math4AI diagrams. |
| **eigen_stability**<br>*Eigen Stability* | ![eigen_stability](images/icons/eigen_stability.png) | Static Only | Mindmap icon for Eigen Stability. Used to represent the eigen stability concept in Math4AI diagrams. |
| **eigenvector_scaling**<br>*Eigenvector Scaling* | ![eigenvector_scaling](images/icons/eigenvector_scaling.png) | Static Only | Mindmap icon for Eigenvector Scaling. Used to represent the eigenvector scaling concept in Math4AI diagrams. |
| **ellipsoid**<br>*Ellipsoid* | ![ellipsoid](images/icons/ellipsoid.png) | Static Only | Mindmap icon for Ellipsoid. Used to represent the ellipsoid concept in Math4AI diagrams. |
| **em**<br>*Em* | ![em](images/icons/em.png) | Static Only | Mindmap icon for Em. Used to represent the em concept in Math4AI diagrams. |
| **euler_bilinear**<br>*Euler Bilinear* | ![euler_bilinear](images/icons/euler_bilinear.png) | Static Only | Mindmap icon for Euler Bilinear. Used to represent the euler bilinear concept in Math4AI diagrams. |
| **euler_maruyama**<br>*Euler Maruyama* | ![euler_maruyama](images/icons/euler_maruyama.png) | Static Only | Mindmap icon for Euler Maruyama. Used to represent the euler maruyama concept in Math4AI diagrams. |
| **expectation**<br>*Expectation* | ![expectation](images/icons/expectation.png) | Static Only | Mindmap icon for Expectation. Used to represent the expectation concept in Math4AI diagrams. |
| **f_divergence**<br>*F Divergence* | ![f_divergence](images/icons/f_divergence.png) | Static Only | Mindmap icon for F Divergence. Used to represent the f divergence concept in Math4AI diagrams. |
| **fast_sampler**<br>*Fast Sampler* | ![fast_sampler](images/icons/fast_sampler.png) | Static Only | Mindmap icon for Fast Sampler. Used to represent the fast sampler concept in Math4AI diagrams. |
| **fisher_divergence**<br>*Fisher Divergence* | ![fisher_divergence](images/icons/fisher_divergence.png) | Static Only | Mindmap icon for Fisher Divergence. Used to represent the fisher divergence concept in Math4AI diagrams. |
| **fisher_info**<br>*Fisher Info* | ![fisher_info](images/icons/fisher_info.png) | Static Only | Mindmap icon for Fisher Info. Used to represent the fisher info concept in Math4AI diagrams. |
| **generative_compare**<br>*Generative Compare* | ![generative_compare](images/icons/generative_compare.png) | Static Only | Mindmap icon for Generative Compare. Used to represent the generative compare concept in Math4AI diagrams. |
| **gmm**<br>*Gmm* | ![gmm](images/icons/gmm.png) | Static Only | Mindmap icon for Gmm. Used to represent the gmm concept in Math4AI diagrams. |
| **gptq_hessian**<br>*Gptq Hessian* | ![gptq_hessian](images/icons/gptq_hessian.png) | Static Only | Mindmap icon for Gptq Hessian. Used to represent the gptq hessian concept in Math4AI diagrams. |
| **gram**<br>*Gram* | ![gram](images/icons/gram.png) | Static Only | Mindmap icon for Gram. Used to represent the gram concept in Math4AI diagrams. |
| **graph_laplacian**<br>*Graph Laplacian* | ![graph_laplacian](images/icons/graph_laplacian.png) | Static Only | Mindmap icon for Graph Laplacian. Used to represent the graph laplacian concept in Math4AI diagrams. |
| **hadamard_outer**<br>*Hadamard Outer* | ![hadamard_outer](images/icons/hadamard_outer.png) | Static Only | Mindmap icon for Hadamard Outer. Used to represent the hadamard outer concept in Math4AI diagrams. |
| **independence**<br>*Independence* | ![independence](images/icons/independence.png) | Static Only | Mindmap icon for Independence. Used to represent the independence concept in Math4AI diagrams. |
| **interpolative_decomposition**<br>*Interpolative Decomposition* | ![interpolative_decomposition](images/icons/interpolative_decomposition.png) | Static Only | Mindmap icon for Interpolative Decomposition. Used to represent the interpolative decomposition concept in Math4AI diagrams. |
| **intractable_posterior**<br>*Intractable Posterior* | ![intractable_posterior](images/icons/intractable_posterior.png) | Static Only | Mindmap icon for Intractable Posterior. Used to represent the intractable posterior concept in Math4AI diagrams. |
| **ito_lemma**<br>*Ito Lemma* | ![ito_lemma](images/icons/ito_lemma.png) | Static Only | Mindmap icon for Ito Lemma. Used to represent the ito lemma concept in Math4AI diagrams. |
| **ito_vs_strat**<br>*Ito Vs Strat* | ![ito_vs_strat](images/icons/ito_vs_strat.png) | Static Only | Mindmap icon for Ito Vs Strat. Used to represent the ito vs strat concept in Math4AI diagrams. |
| **joint_marginal**<br>*Joint Marginal* | ![joint_marginal](images/icons/joint_marginal.png) | Static Only | Mindmap icon for Joint Marginal. Used to represent the joint marginal concept in Math4AI diagrams. |
| **kkt**<br>*Kkt* | ![kkt](images/icons/kkt.png) | Static Only | Mindmap icon for Kkt. Used to represent the kkt concept in Math4AI diagrams. |
| **kron_properties**<br>*Kron Properties* | ![kron_properties](images/icons/kron_properties.png) | Static Only | Mindmap icon for Kron Properties. Used to represent the kron properties concept in Math4AI diagrams. |
| **kron_vector**<br>*Kron Vector* | ![kron_vector](images/icons/kron_vector.png) | Static Only | Mindmap icon for Kron Vector. Used to represent the kron vector concept in Math4AI diagrams. |
| **langevin_equation**<br>*Langevin Equation* | ![langevin_equation](images/icons/langevin_equation.png) | Static Only | Mindmap icon for Langevin Equation. Used to represent the langevin equation concept in Math4AI diagrams. |
| **latent_model**<br>*Latent Model* | ![latent_model](images/icons/latent_model.png) | Static Only | Mindmap icon for Latent Model. Used to represent the latent model concept in Math4AI diagrams. |
| **ldlt_decomposition**<br>*Ldlt Decomposition* | ![ldlt_decomposition](images/icons/ldlt_decomposition.png) | Static Only | Mindmap icon for Ldlt Decomposition. Used to represent the ldlt decomposition concept in Math4AI diagrams. |
| **lin_indep**<br>*Lin Indep* | ![lin_indep](images/icons/lin_indep.png) | Static Only | Mindmap icon for Lin Indep. Used to represent the lin indep concept in Math4AI diagrams. |
| **low_rank_adaptation**<br>*Low Rank Adaptation* | ![low_rank_adaptation](images/icons/low_rank_adaptation.png) | Static Only | Mindmap icon for Low Rank Adaptation. Used to represent the low rank adaptation concept in Math4AI diagrams. |
| **lower_diagonal_upper_decomposition**<br>*Lower Diagonal Upper Decomposition* | ![lower_diagonal_upper_decomposition](images/icons/lower_diagonal_upper_decomposition.png) | Static Only | Mindmap icon for Lower Diagonal Upper Decomposition. Used to represent the lower diagonal upper decomposition concept in Math4AI diagrams. |
| **lq_decomposition**<br>*Lq Decomposition* | ![lq_decomposition](images/icons/lq_decomposition.png) | Static Only | Mindmap icon for Lq Decomposition. Used to represent the lq decomposition concept in Math4AI diagrams. |
| **mala**<br>*Mala* | ![mala](images/icons/mala.png) | Static Only | Mindmap icon for Mala. Used to represent the mala concept in Math4AI diagrams. |
| **mdp**<br>*Mdp* | ![mdp](images/icons/mdp.png) | Static Only | Mindmap icon for Mdp. Used to represent the mdp concept in Math4AI diagrams. |
| **mean_field**<br>*Mean Field* | ![mean_field](images/icons/mean_field.png) | Static Only | Mindmap icon for Mean Field. Used to represent the mean field concept in Math4AI diagrams. |
| **nonlinear_activation**<br>*Nonlinear Activation* | ![nonlinear_activation](images/icons/nonlinear_activation.png) | Static Only | Mindmap icon for Nonlinear Activation. Used to represent the nonlinear activation concept in Math4AI diagrams. |
| **nonnegative_matrix_factorization**<br>*Nonnegative Matrix Factorization* | ![nonnegative_matrix_factorization](images/icons/nonnegative_matrix_factorization.png) | Static Only | Mindmap icon for Nonnegative Matrix Factorization. Used to represent the nonnegative matrix factorization concept in Math4AI diagrams. |
| **null_space**<br>*Null Space* | ![null_space](images/icons/null_space.png) | Static Only | Mindmap icon for Null Space. Used to represent the null space concept in Math4AI diagrams. |
| **ortho**<br>*Ortho* | ![ortho](images/icons/ortho.png) | Static Only | Mindmap icon for Ortho. Used to represent the ortho concept in Math4AI diagrams. |
| **orthonormal_inverse**<br>*Orthonormal Inverse* | ![orthonormal_inverse](images/icons/orthonormal_inverse.png) | Static Only | Mindmap icon for Orthonormal Inverse. Used to represent the orthonormal inverse concept in Math4AI diagrams. |
| **ou_heat**<br>*Ou Heat* | ![ou_heat](images/icons/ou_heat.png) | Static Only | Mindmap icon for Ou Heat. Used to represent the ou heat concept in Math4AI diagrams. |
| **partition_z**<br>*Partition Z* | ![partition_z](images/icons/partition_z.png) | Static Only | Mindmap icon for Partition Z. Used to represent the partition z concept in Math4AI diagrams. |
| **permuted_lu_decomposition**<br>*Permuted Lu Decomposition* | ![permuted_lu_decomposition](images/icons/permuted_lu_decomposition.png) | Static Only | Mindmap icon for Permuted Lu Decomposition. Used to represent the permuted lu decomposition concept in Math4AI diagrams. |
| **placeholder**<br>*Placeholder* | ![placeholder](images/icons/placeholder.png) | Static Only | Mindmap icon for Placeholder. Used to represent the placeholder concept in Math4AI diagrams. |
| **power_method**<br>*Power Method* | ![power_method](images/icons/power_method.png) | Static Only | Mindmap icon for Power Method. Used to represent the power method concept in Math4AI diagrams. |
| **preservation**<br>*Preservation* | ![preservation](images/icons/preservation.png) | Static Only | Mindmap icon for Preservation. Used to represent the preservation concept in Math4AI diagrams. |
| **proj**<br>*Proj* | ![proj](images/icons/proj.png) | Static Only | Mindmap icon for Proj. Used to represent the proj concept in Math4AI diagrams. |
| **quadratic_variation**<br>*Quadratic Variation* | ![quadratic_variation](images/icons/quadratic_variation.png) | Static Only | Mindmap icon for Quadratic Variation. Used to represent the quadratic variation concept in Math4AI diagrams. |
| **randomized_svd**<br>*Randomized Svd* | ![randomized_svd](images/icons/randomized_svd.png) | Static Only | Mindmap icon for Randomized Svd. Used to represent the randomized svd concept in Math4AI diagrams. |
| **rank1**<br>*Rank1* | ![rank1](images/icons/rank1.png) | Static Only | Mindmap icon for Rank1. Used to represent the rank1 concept in Math4AI diagrams. |
| **rank_revealing_qr**<br>*Rank Revealing Qr* | ![rank_revealing_qr](images/icons/rank_revealing_qr.png) | Static Only | Mindmap icon for Rank Revealing Qr. Used to represent the rank revealing qr concept in Math4AI diagrams. |
| **reflection**<br>*Reflection* | ![reflection](images/icons/reflection.png) | Static Only | Mindmap icon for Reflection. Used to represent the reflection concept in Math4AI diagrams. |
| **reparam**<br>*Reparam* | ![reparam](images/icons/reparam.png) | Static Only | Mindmap icon for Reparam. Used to represent the reparam concept in Math4AI diagrams. |
| **reverse_fp**<br>*Reverse Fp* | ![reverse_fp](images/icons/reverse_fp.png) | Static Only | Mindmap icon for Reverse Fp. Used to represent the reverse fp concept in Math4AI diagrams. |
| **rope**<br>*Rope* | ![rope](images/icons/rope.png) | Static Only | Mindmap icon for Rope. Used to represent the rope concept in Math4AI diagrams. |
| **rotation_circle**<br>*Rotation Circle* | ![rotation_circle](images/icons/rotation_circle.png) | Static Only | Mindmap icon for Rotation Circle. Used to represent the rotation circle concept in Math4AI diagrams. |
| **saddle_point**<br>*Saddle Point* | ![saddle_point](images/icons/saddle_point.png) | Static Only | Mindmap icon for Saddle Point. Used to represent the saddle point concept in Math4AI diagrams. |
| **schur_complement**<br>*Schur Complement* | ![schur_complement](images/icons/schur_complement.png) | Static Only | Mindmap icon for Schur Complement. Used to represent the schur complement concept in Math4AI diagrams. |
| **schur_gp**<br>*Schur Gp* | ![schur_gp](images/icons/schur_gp.png) | Static Only | Mindmap icon for Schur Gp. Used to represent the schur gp concept in Math4AI diagrams. |
| **sde_definition**<br>*Sde Definition* | ![sde_definition](images/icons/sde_definition.png) | Static Only | Mindmap icon for Sde Definition. Used to represent the sde definition concept in Math4AI diagrams. |
| **sde_optim_limit**<br>*Sde Optim Limit* | ![sde_optim_limit](images/icons/sde_optim_limit.png) | Static Only | Mindmap icon for Sde Optim Limit. Used to represent the sde optim limit concept in Math4AI diagrams. |
| **sphere_ellipse**<br>*Sphere Ellipse* | ![sphere_ellipse](images/icons/sphere_ellipse.png) | Static Only | Mindmap icon for Sphere Ellipse. Used to represent the sphere ellipse concept in Math4AI diagrams. |
| **ssm**<br>*Ssm* | ![ssm](images/icons/ssm.png) | Static Only | Mindmap icon for Ssm. Used to represent the ssm concept in Math4AI diagrams. |
| **stable_discretization**<br>*Stable Discretization* | ![stable_discretization](images/icons/stable_discretization.png) | Static Only | Mindmap icon for Stable Discretization. Used to represent the stable discretization concept in Math4AI diagrams. |
| **state_space_model**<br>*State Space Model* | ![state_space_model](images/icons/state_space_model.png) | Static Only | Mindmap icon for State Space Model. Used to represent the state space model concept in Math4AI diagrams. |
| **stochastic_variational_inference**<br>*Stochastic Variational Inference* | ![stochastic_variational_inference](images/icons/stochastic_variational_inference.png) | Static Only | Mindmap icon for Stochastic Variational Inference. Used to represent the stochastic variational inference concept in Math4AI diagrams. |
| **subspaces**<br>*Subspaces* | ![subspaces](images/icons/subspaces.png) | Static Only | Mindmap icon for Subspaces. Used to represent the subspaces concept in Math4AI diagrams. |
| **svd_mapping**<br>*Svd Mapping* | ![svd_mapping](images/icons/svd_mapping.png) | Static Only | Mindmap icon for Svd Mapping. Used to represent the svd mapping concept in Math4AI diagrams. |
| **tensor_parallel**<br>*Tensor Parallel* | ![tensor_parallel](images/icons/tensor_parallel.png) | Static Only | Mindmap icon for Tensor Parallel. Used to represent the tensor parallel concept in Math4AI diagrams. |
| **tensor_train**<br>*Tensor Train* | ![tensor_train](images/icons/tensor_train.png) | Static Only | Mindmap icon for Tensor Train. Used to represent the tensor train concept in Math4AI diagrams. |
| **truncated_svd**<br>*Truncated Svd* | ![truncated_svd](images/icons/truncated_svd.png) | Static Only | Mindmap icon for Truncated Svd. Used to represent the truncated svd concept in Math4AI diagrams. |
| **var_family**<br>*Var Family* | ![var_family](images/icons/var_family.png) | Static Only | Mindmap icon for Var Family. Used to represent the var family concept in Math4AI diagrams. |
| **weyl_bounds**<br>*Weyl Bounds* | ![weyl_bounds](images/icons/weyl_bounds.png) | Static Only | Mindmap icon for Weyl Bounds. Used to represent the weyl bounds concept in Math4AI diagrams. |
| **zoh**<br>*Zoh* | ![zoh](images/icons/zoh.png) | Static Only | Mindmap icon for Zoh. Used to represent the zoh concept in Math4AI diagrams. |

