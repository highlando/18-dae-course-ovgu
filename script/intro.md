---
title: DAEs
author: Jan Heiland
date: \today
institute: OVGU/MPI
output: 
  bookdown::html_book:
  bookdown::pdf_book:
  #   pdf_document:
  #     keep_tex: true
# output: html_document
---

# Introduction

DAEs are coupled differential- and algebraic equations. Throughout this lecture, the free variable will be the time $t$ and differentiation will always be considered with respect to $t$.

In other words, we consider dynamical processes -- here are the differential equations -- that are subject to constraints: the algebraic equations.

## Examples

### Free fall vs. the pendulum

![Free fall of a point mass](pics/freefall.png)

Free fall: Newton's second law applies: 

> `force = mass*acceleration`

In 2D, the $x$, $y$ coordinates of a point of mass $m$:

\begin{align}
m\ddot x &= 0 \\
m\ddot y &= -mg
\end{align}
where $g$ is the gravity. 

Now the pendulum: *The same point mass attached to a string*.

![a pendulum](pics/pendulum.png)

Again, we have `force = mass*acceleration` but also the conditions that the mass moves on a circle:

$$
 (x(t) - c_x)^2 + (y(t) - c_y)^2 = l^2,
$$
where $(c_x, c_y)$ are the coordinates of the center and $l$ is the length of the string.

We use the Langrangian function to derive the equations of motion. For the pendulum, we have the kinetic energy $T$, the potential $U$, and the constraint $g$ as

$$
  T = \frac 12 m (\dot x(t)^2 + \dot y(t)^2), \quad U = mgy, \quad \text{and} \quad g = (x(t) - c_x)^2 + (y(t) - c_y)^2 - l^2 .
$$

Thus, from the principle that 

$$
\frac{d}{dt}(\frac{\partial L}{\partial \dot q}) - \frac{\partial L}{\partial q} = 0, \quad\text{for}\quad L = U -T - \lambda g \quad\text{and}\quad q=x, y ,\lambda
$$

one obtains:

| generalized coordinate | equation |
|:-----------------------|---------:|
|$q \leftarrow x$ | $m\ddot x (t) + 2 \lambda x = 0$ |
|$q \leftarrow y$ | $m\ddot y (t) + mgy + 2 \lambda y = 0$ |
|$q \leftarrow \lambda$ | $(x(t) - c_x)^2 + (y(t) - c_y)^2 - l^2 =0$ |

After an order reduction via the new variables $u:=\dot x$ and $v=\dot y$ the overall system reads

\begin{align}\label{eqn_pendulum}
  \dot x &= u \notag \\
  \dot y &= v \notag \\
  \dot u &= - 2 \lambda x \\ 
  \dot v &= - 2 \lambda y - mgy\notag \\
        0&=(x - c_x)^2 + (y - c_y)^2 - l^2 \notag,
\end{align}

where we have omitted the time dependence. Equation is a canonical example for a DAE with combined differential and algebraic equations.

### Example -- Electrical Circuit

*charging of a conductor through a resistor*

![A simple electrical circuit](pics/circuit.png)

We formulate the problem in terms of the potentials $x_1$, $x_2$, $x_3$, that are assumed to reside in the wires between a source $U$ and a resistor $R$, the resistor $R$ and the capacitor $C$, and the capacitor and the source.

A model for the circuit is given through the following principles and considerations.

 * the source defines the difference in the neighboring potentials: $x_1 - x_3 - U = 0$
 * the current $I_R$ that is induced by the potentials neighboring the resistor is is defined through *Ohm's law*: $I_R = \frac{x_1 - x_2}{R}$
 * the current $I_C$ that is induced by the potentials neighboring the capacitor is described through: $I_C = C(\dot x_3 - \dot x_2)$
 * \emph{Kirchhoff's law} states that everywhere in the circuit the currents sum up to zero: $I_C + I_R = C(\dot x_3 - \dot x_2)+ \frac{x_1 - x_2}{R}=0$
 * finally, we can set a ground potential (note that so far all equations only consider differences in the potential) and we set $x_3 = 0$.

Summing all up, the equations that model the circuit are given as 

\begin{align}
C(\dot x_3 - \dot x_2) &= - \frac{x_1 - x_2}{R}\notag \\
0  &= x_1 - x_3 - U \\
0 &= x_3 \notag
\end{align}

### Example -- Navier-Stokes Equations

The Navier-Stokes equations (NSE) are commonly used to model all kind of flows. They describe the evolution of the velocity $v$ of the fluid and the pressure $p$ in the fluid. Note that the flow occupies a spatial domain, say in $\mathbb R^{3}$ so that $v$ and $p$ are functions both of the time variable $t$ and a space variable $\xi$:

$$
v\colon (t, \xi) \mapsto v(t,\xi)\in \mathbb R^{3} \quad\text{and}\quad  p\colon (t, \xi) \mapsto p(t,\xi)\in \mathbb R.
$$

The NSE:

\begin{align*}
  \frac{\partial v}{\partial t} + (v\otimes \nabla_\xi)v - \Delta_\xi v + \nabla_\xi p &= 0, \\
  \nabla \cdot v &= 0,
\end{align*}

with $\otimes$ denoting the outer product and $\nabla_\xi$ and $\Delta_\xi$ denoting the gradient and the *Laplace* operator. If we only count the derivatives with respect to time, as postulated in the introduction, the NSE can be seen as an (abstract) DAE. 

### Example -- Automatic Modelling or *Engineers vs. Mathematicians*

If a system, say an engine, consists of many interacting processes, it is convenient and common practice to model the dynamics of each particular process and to couple the subprocesses through interface conditions.

This coupling is done through equating quantities so that the overall model will consist of dynamical equations of the subprocesses and algebraic relations at the interfaces -- which makes it a DAE.

In fact, tools like [`modelica`](https://www.modelica.org/) for automatic modelling of complex processes do exactly this. 

The approach of *automatic modelling* is universal and convenient for engineers. However, the resulting model equations will be DAEs which, as we will see, pose particular problems in their analytical and numerical treatment.  