See the details in my thesis. To have better understanding, here is the main messages.
# Quantum-nonlocality

One of the most striking manifestations of quantum entanglement lies in its ability to produce correlations that violate a Bell inequality [Bel64] even when measurements are carried out space-like separated. A precursor to this discovery was first discussed in the famous paper of Einstein-Podolsky-Rosen in 1935. Later, in 1964, Bell showed that some correlations allowed in quantum mechanics are impossible in local hidden variable theories.

These nonlocal quantum correlations, represented by joint probability distribution of each parties’ outcomes conditioned on their choice of measurement, are known to serve as an the indispensable resource for device-independent (DI) quantum information processing
[Sca15]. An important goal here is to distinguish them from classical resources. Operationally, such correlations between measurement outcomes cannot be explained by a local common cause [Bel04], or equivalently, by shared randomness alone.

In recent years, the development of quantum technology has progressed rapidly. One of the significant breakthroughs is quantum supremacy [AAB+19]. In 2019, Google proudly announced the first demonstration of a quantum computational advantage compared to classical computations. In some sense, the development of quantum information theory can be traced back to Bell’s discovery in 1964. As mentioned previously, a Bell experiment can be used to demonstrate that some quantum correlations cannot be reproduced by any local causal model. This leads to new questions concerning the essential features of quantum theory. In particular, people have been trying to understand the ways in which quantum theory is different from classical theory.

#  Bell experiment
In a Bell experiment, if a nonlocal correlation is found, we can make statements about the
devices Alice and Bob use that depend only on the measurement statistics involved. This
means that we can use them in quantum technologies in a device-independent way [Sca15].
In a device-independent framework, we are not concerned with the precise details of how the
devices function. Rather, we only assume that the devices obey the laws of quantum theory
and that the devices do not secretly communicate with each other.
<div align=center><img src="https://github.com/fluttering13/Quantum-nonlocality/blob/master/Figure/Bell_sceanrio.png" width="300px"/></div>


In a typical Bell experiment, two parties, Alice and Bob, share two particles from the
same source and stay in space-like separation to ensure that they obey the principle of locality (with respect to causality in special relativity). We assume that Alice and Bob can
freely choose to perform the respective measurements $x$ and $y$ and obtain the outcomes a,
b, respectively. Locally, Alice and Bob produce their outcomes, and the resulting joint conditional probability distribution $P(a, b|x, y)$ is called the correlation. Here, Alice and Bob
are permitted to use some shared randomness, represented by the parameter $λ$ with possible
values from a set $Λ$. Note that $λ$ is independent of parties’ inputs alphabets $x$, $y$, $z$, etc. From
this perspective, several applications of sharing a correlated random string can be discussed,
such as secret key generation, privacy amplification, communication complexity, and the
classical simulation of quantum nonlocal statistics.

# The correlation space
<div align=center><img src="https://github.com/fluttering13/Quantum-nonlocality/blob/master/Figure/NQL.png" width="200px"/></div>

Schematic view of correlation space: From outside to inside pattern are the no-signaling set $\mathcal{NS}$, the quantum set $\mathcal{Q}$, the local set $\mathcal{L}$, respectively.
## The set of no signaling correlation $\mathcal{NS}$
Let us continue with the introduction of the Bell scenario. Here Alice and Bob may share some common information obtained from a source but they are not allowed to exchange information. It is natural to look into the joint conditional probability distribution space $P(a,b|x,y)$, but what would be a legitimate distribution from the physical point of view? For this, we may look at the relationship between relativity and quantum theory. To be compatible with both theories, faster-than-light communication cannot be allowed. 
Thus, in addition to the positivity condition $P(a,b|x,y) \ge 0$ and normalization $\sum\limits_{a,b} {P\left( {a,b|x,y} \right) = 1}$, the no-signaling conditions are imposed; then each party's outcome distribution is independent of the others' measurement choices.
$$\sum\limits_b {P\left( {a,b|x,y} \right) = } \sum\limits_b {P\left( {a,b|x,y'} \right)= P(a|x)} \forall y$$
$$\sum\limits_a {P\left( {a,b|x,y} \right) = } \sum\limits_a {P\left( {a,b|x',y} \right)= P(b|y)} \forall x$$

So the $\mathcal{NS}$ sets can be described as the intersection of hyperplanes given above and positivity half-spaces. Hence, the $\mathcal{NS}$ set is a polytope.
Summing over from one's inputs $x,y$ and other inputs $x'$, $y'$ results in their marginal distribution $P(a|x)$ and $P(b|y)$. Consider the two-party scenario with $n_{in}$ inputs and $n_{out}$ outcomes as $(n_{in},n_{out})$. The normalization constraint and the no-signaling conditions mean that the dimension $d_{NS}$ is reduced to
$$d_{NS}=(n_{in}-1)^2 n_{out}^2+ 2(n_{in}-1)n_{out}$$

## The set of Bell-local correlation $\mathcal{L}$
A correlation corresponds to the observed statistics from the experimental data. Apart from that, physicists are familiar with the Hamiltonian formalism to describe the dynamics of systems but sometimes we do care about whether a system behaves like a quantum or classical one. From an informational point of view, all these classical correlations can be simply described by the local hidden variable model: 
$$P(a,b|x,y)=\sum_\lambda P(\lambda) P(a|x,\lambda) P(b|y,\lambda)$$
where $P(a|x,\lambda)$, $P(b|y,\lambda)$ are local response functions over all possible local hidden variables $\lambda$.
In some sense, the hidden variables $\lambda$ that Alice and Bob share correspond to certain classical properties. In classical mechanics, we can measure things such as particle number, phase, wavelength, moment,  etc., and we say that the outcome reveals a pre-existing value. In some cases, we will have some ignorance of these definite values, and this can be represented by a probability distribution $P(\lambda)$.
A Bell inequality $B_{abxy}$ says that a linear combination of elements of the conditional probability distribution $P(a,b|x,y)$, which we call the Bell value, is bounded by some threshold $B_0$ called the local bound: 
$$\sum\limits_{abxy} { {{B_{abxy}} P_{abxy} \;  \overset{\mathcal{L}}{\le} } B_0}$$
In practice, the set of local correlation is a convex set obtained from linear combinations of deterministic strategies $\delta_{a,f(x)}$, $\delta_{b,f(y)}$. So the maximum value from the above equation is obtained by maximizing over all these deterministic strategies. It is straightforward to show that the number of extremal points will grow exponentially as the setting increases.  For the bipartite scenario $(n_{in},n_{out})$, some of the full lists are known:
$(n_{in},2)$  with $n_{in} \in (2,3)$  	
****
https://arxiv.org/abs/quant-ph/0306129 
****
$n_{in} \in (4)$
****
https://arxiv.org/abs/1811.11820  
****
$(2,n_{out})$ with $n_{out} \in (2,3)$
****
https://arxiv.org/abs/quant-ph/0306129 
****
The partial list $(3,3)$ is given in
****
https://arxiv.org/abs/1511.05253
****

## Take an example of local correlation: local deterministic strategy
Consider the local hidden variable model, Alice and Bob share the hidden variables $λ$, and
the joint probabilities distribution is given by:

$$\sum_\lambda P(\lambda) P(a \mid x, \lambda) P(b \mid y, \lambda)$$
Technologically, we can sort of this model as polytope optimization problems and rewrite
them as a convex combination of local deterministic strategies, which are so-called extremal
points of the local polytope.
$$\sum_\lambda P(\lambda) \delta_{a, f(x, \lambda)} \delta_{b, f(y, \lambda)}$$
To characterize the sets of deterministic strategies and start from a simple example, we will
write some examples in the following tables. For example, consider that Alice and Bob are
in two input binary settings and they can decide on the strategies beforehand. One of the
strategy matrices $D_{ax}$ from Alice’s side is given by

$$\begin{array}{c|c|c|} 
& x=0 & x=1 \\
\hline a=0 & 1 & 0 \\
\hline a=1 & 0 & 1 \\
\hline
\end{array}$$

Similarly, the strategy matrix for Bob's side $D_{bx}$

$$
\begin{array}{c|c|c|} 
& y=0 & y=1 \\
\hline a=0 & 0 & 1 \\
\hline a=1 & 1 & 0 \\
\hline
\end{array}
$$

Vectorize $D_{ax}$ and $D_{bx}$ and compute the tensor product of them. The joint probability distribution $P(a,b|x,y)$ can be constructed by

$$D_{ax} \otimes D_{by}=\left[\begin{array}{llll}
1 & 0 & 0 & 1
\end{array}\right] \otimes\left[\begin{array}{l}
0 \\
1 \\
1 \\
0
\end{array}\right]$$

End up
<div align=center><img src="https://github.com/fluttering13/Quantum-nonlocality/blob/master/Figure/mathpix%202023-02-22%2017-46-15.png" width="200px"/></div>
## The quantum set $\mathcal{Q}$
To better understand the counterintuitive features of quantum mechanics, it pays to investigate the difference between the set of Bell-local correlations and those allowed in quantum theory. This can be done, for example, by investigating the maximal quantum violation of a Bell inequality. To begin with the characterization of quantum correlations, recall that the outcome probabilities for quantum measurements are governed by Born's rule.
$$P(a, b \mid x, y) = \operatorname{tr}\left(\rho M_{a \mid x} \otimes M_{b \mid y}\right)$$

The joint conditional probability can be defined for any bipartite density matrix $\rho$ and a set of positive operator-valued measures [NC11] $M_{a \mid x}$ and $M_{b \mid y}$ for Alice and Bob, respectively.  By that definition, it is straightforward to show that the quantum set $\mathcal{Q}$ strictly belongs to the $\mathcal{NS}$ set.
Also, if density matrix is separable, the corresponding probability distribution must be local. In general, the following relations hold for the sets considered here:
$$\mathcal{L} \subsetneq \mathcal{Q} \subsetneq \mathcal{N S}.$$
A full characterization of the set of quantum correlations is an important but difficult issue. The standard approach is to use some hierarchy of SDPs that provides a collection of outer approximations
****
https://arxiv.org/abs/quant-ph/0607119  
https://arxiv.org/abs/0803.4290  
https://arxiv.org/abs/0803.4373  
https://arxiv.org/abs/1302.1336  
****
