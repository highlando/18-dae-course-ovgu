---
layout: index
---

Course DAEs - OvGU - 2016
-----

> :rocket: The 5th exercise is up. We will discuss it in the last week of the course. That is Tuesday, July 5th.

> :rocket: :rocket: There was a little mistake in the 5th exercise sheet (wrong initial conditions for the cars in the spring mass system) -- it's fixed now.

Here you find basic and current information and materials for the lecture 
*DAEs* at the OvGU in the summer term 2016.

| Day | Time | Place |
| ------- | ------ | ------- |
| Tuesday | 17:00-18:30 | G05-313 |
| Wednesday | 09:30-11:00 | G05-313 |

:memo: Jump to the [exercises](#exercises) section.

<h3 id="overview">Course of the lecture (22+6=28)</h3>
 0. Introductory considerations (1) [[week 1]](#week-1)
   * DAEs in mathematical modelling
   * Applications areas and examples
   * Challenges in the numerical and analytical treatment of DAEs
   * [Literature](#literature)
 0. General notions from DAE calculus (1+1)
   * Solutions and solvability
   * Consistency and regularity
   * Indices
 0. Linear DAEs with constant coefficients (4+1)
   * Basic algebraic concepts [[week 2]](#week-2)
   * Normal forms
   * Solvability and representations of solutions [[week 3]](#week-3)[[week 4]](#week-4)
 0. Linear time-varying and nonlinear DAEs (4+1)
   * Fundamental differences with the linear time-invariant case 
   * Time-dependent equivalence transformations and canonical forms [[week 5]](#week-5)
   * *Derivative Arrays* [[week 6]](#week-6)
   * *Differentiation-index and Strangeness-index*
 0. Numerical integration of DAEs (6+2)
   * Digression: Numerical integration of ODEs
   * Runge-Kutta methods (RKM) for DAEs with constant coefficients [[week 7]](#week-7)[[week 8]](#week-8)
   * RKM methods for semi-explicit "index-1" DAEs [[week 9]](#week-9)
   * RKM methods for implicit "index-1" DAEs
   * *Backward Differencing* for DAEs [[week 10]](#week-10)
 0. Numerical Methods for index reduction (1)
   * Derivative Arrays
   * Minimal Extension
 0. DAEs with controls (1) [[week 11]](#week-11)
   * Representation as *Behavior*
   * Index reduction through *Feedback*

### Exercises

| Date | Topic | Sheet |
| ------- | ------ | ------- |
| [April 20th](#exercisei) | I - Introductory Considerations and Basic Notions | [ueb1.pdf](exercises/01/ueb01.pdf) |
| [May 11th](#exerciseii) | II - Linear DAEs with constant coefficients | [ueb2.pdf](exercises/02/ueb2.pdf) |
| [May 18th](#exerciseiii) | III - linear daes with time-varying coefficients | [ueb3.pdf](exercises/03/ueb3.pdf) |
| [June 8th](#exerciseiv) | IV - one step methods | [ueb4.pdf](exercises/04/ueb04.pdf) |
| [July 5th](#exercisev) | V - higher index and nonlinear equations | [ueb5.pdf](exercises/05/ueb05.pdf) |

### Week 1

#### Introductory considerations (1)

+++ DAEs are coupled differential and nondifferential (algebraic) equations +++ cf. the pendulum +++ which is naturally modelled as a DAE +++ as are electrical circuits, chemical reactions, and flows +++ in numerical schemes, equations are solved approximately - what does this mean for the pendulum? +++  [back to overview](#overview)

#### General notions from DAE calculus (1)
+++ we consider *C1*-solutions although there are many ways to define less regular solutions +++ existence of solutions depends on several factors +++ smoothness of *right hand sides* +++ consistency of initial values +++ *hidden constraints* and *underlying ODE* +++ many ways to classify DAEs <-> many *indices* +++ [back to overview](#overview)

#### Literature

| Author | Title | comments |
| ------- | ------ | ------- |
| Kunkel, Mehrmann | Differential-Algebraic Equations | Main reference, very concise, sometimes hard to read |
| Hairer, Wanner | Solving ODEs. (Stiff and DAEs) | standard reference for solving ODEs (the first volume), intuitive and practical approach to numerical analysis of certain DAEs |

### Week 2

#### Linear DAEs with constant coefficients (1)
+++ variable transforms and scalings do not affect solvability +++ DAEs <-> (E, A) matrix pairs +++ canonical forms +++ Weierstrass canonical form +++ canonical form of a linear DAE with constant coefficients +++ [back to overview](#overview)

#### Linear DAEs with constant coefficients (2)
+++ splitting of DAEs into an ODE and a nilpotent DAE +++ explicit solution of the nilpotent DAE +++ index of a matrix pair (E,A) and its well-definedness +++ [back to overview](#overview)

### Week 3 

#### Linear DAEs with constant coefficients (3) - April 19th
+++ solvability solved +++ way to arrive at a explicit solution formula +++ definition of the Drazin inverse +++ properties of the Drazin inverse +++ [back to overview](#overview)

<h4 id="exercisei"> Course Exercise sheet I - April 20th </h4>
+++ multibody systems +++ separation of algebraic and differential parts +++ remodelling of the simple pendulum as ODE +++ Navier-Stokes equations +++ links to [ode modelling of the pendulum](http://www.engr.iupui.edu/~skoskie/ECE680/ECE680_l3notes.pdf) and the overhead crane +++ [back to overview](#overview)

### Week 4 

#### Linear DAEs with constant coefficients (4) - April 26th

+++ DAE as superposition of a nilpotent DAE and an *index-1* DAE +++ explicit formula for all solutions of the homogeneous equations +++ explicit form of a solution of the inhomogeneous equations +++ [back to overview](#overview)

#### Linear DAEs with time-varying coefficients (1) - April 27th

+++ regularity of matrix pairs does not say much about solvability of LTV DAEs +++ time-dependent state transformations +++ global and local equivalence of matrix function pairs +++ [back to overview](#overview)

### Week 5 

#### Linear DAEs with time-varying coefficients (2) - May 10th

+++ characteristic values +++ canonical form for local equivalence transformations +++ time-varying SVD +++ canonical form for global equivalence transformations +++ [back to overview](#overview)

<h4 id="exerciseii"> Course Exercise sheet II - May 11th </h4>
+++ regularity and Kronecker form of 3x3 examples +++ index-1 condition +++ regularity and commutativity +++ Drazin inverse as group inverse +++ [back to overview](#overview)

### Week 5 

#### Linear DAEs with time-varying coefficients (3) - May 17th

<h4 id="exerciseiii"> Course Exercise sheet III - May 18th </h4>

### Week 6

#### Linear DAEs with time-varying coefficients (4) - May 24th
+++ derivative arrays +++ strangeness free condensed form of linearized Navier-Stokes equations +++ derivative arrays for nonlinear DAEs +++ [back to overview](#overview)

#### Digression: Numerical Solutions of ODEs - May 25th
+++ basic definitions +++ implicit/explicit Euler +++ consistency and stability +++ Runge-Kutta schemes +++ BDF schemes +++ [back to overview](#overview)


### Week 7

#### Numerical Solutions of DAEs (1) - May 31th
+++ basic notions and definitions +++ Kronecker product and perfect shuffle +++ Runge-Kutta methods +++ [back to overview](#overview)

#### Numerical Solutions of DAEs (2) - June 1st
+++ Numerical analysis of Runge-Kutta schemes for DAEs with constant coefficients +++ the local consistency error +++ [back to overview](#overview)

### Week 8

#### Numerical Solutions of DAEs (3) - June 7th
+++ Numerical analysis of Runge-Kutta schemes for DAEs with constant coefficients +++ the global convergence error +++ [back to overview](#overview)

<h4 id="exerciseiv">Course Exercise sheet IV - June 8th </h4>
+++ effect of rounding errors +++ consistency errors +++ two-stage Gauss method for ODEs and DAEs +++ Runge-Kutta method for linear DAEs +++ CODING: C1:*Explicit Euler and rounding errors* +++  C2:*Implicit Euler* for linear DAEs with time-varying coefficients +++ Resources: Matlab implementation by Jens Bremer -- [[zip file](exercises/04/code/Ex4_JensBremer.zip)], Python implementation -- [[webview](exercises/04/code/4c2-ipynb.html)], [[ipython notebook](exercises/04/code/4c2.ipynb)], [[python file](exercises/04/code/4c2.py)] +++ [back to overview](#overview)

### Week 9

#### Numerical Solutions of DAEs (4) - June 20th
+++ Note on Runge-Kutta methods for linear time-varying DAEs +++ definition and analysis of Runge-Kutta schemes for semi-explicit "index-1" DAEs +++ [back to overview](#overview)

#### Numerical Solutions of DAEs (5) - June 21st
+++ stiffly accurate Runge-Kutta methods +++ definition and analysis of Runge-Kutta schemes for implicit "index-1" DAEs +++ [back to overview](#overview)

### Week 10 

#### Numerical Solutions of DAEs (6) - June 27th
+++ general remarks on collocation Runge-Kutta methods +++ Backward differencing schemes for DAEs +++ [back to overview](#overview)

#### Numerical Methods for Index Reduction - June 28th
+++ general concepts of index reduction +++ numerical approach to index reduction via derivative arrays +++ minimal extension +++ [back to overview](#overview)

### Week 11
<h4 id="exercisev">Course Exercise sheet V - July 5th </h4>
+++ mass-spring chain +++ minimal extension +++ 2-stage Radau IIa +++ CODING: *Implicit Euler* for the nonlinear pendulum equations --- *Radau IIa* for the mass-spring manoeuvre --- simulation of index reduced systems +++ Resources: Use the code from the previous [exercise iv](#exerciseiv) --- check out the [*Oberwolfach snapshot*](http://www.mfo.de/math-in-public/snapshots/files/wie-steuert-man-einen-kran) on the mass-spring chain (in German) or the more verbose [preprint](http://www.mfo.de/scientific-programme/publications/owp/2015/OWP2015_18.pdf) (in English) +++ [back to overview](#overview)

