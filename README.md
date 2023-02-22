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

![image](https://github.com/fluttering13/Quantum-nonlocality/blob/master/Figure/Bell_sceanrio.png)

In a typical Bell experiment, two parties, Alice and Bob, share two particles from the
same source and stay in space-like separation to ensure that they obey the principle of locality (with respect to causality in special relativity). We assume that Alice and Bob can
freely choose to perform the respective measurements x and y and obtain the outcomes a,
b, respectively. Locally, Alice and Bob produce their outcomes, and the resulting joint conditional probability distribution P(a, b|x, y) is called the correlation. Here, Alice and Bob
are permitted to use some shared randomness, represented by the parameter λ with possible
values from a set Λ. Note that λ is independent of parties’ inputs alphabets x, y, z, etc. From
this perspective, several applications of sharing a correlated random string can be discussed,
such as secret key generation, privacy amplification, communication complexity, and the
classical simulation of quantum nonlocal statistics.
