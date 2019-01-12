---
layout: index
---

Course DAEs - OvGU - 2018
-----

> :rocket: Here is the paperhive lecture. Looks like you have to join this [channel](https://paperhive.org/channels/invitationLink?token=Rnz0EW4CHT70) to see the document.


Here you find basic and current information and materials for the lecture 
*DAEs* at the OvGU in the winter term 2018.

| Day | Time | Place |
| ------- | ------ | ------- |
| Thursday | 09:00-11:00 | G12-129 |
| Friday | 11:00-13:00 | G05-308 |

Consultation hours: Thursday 11:00-12:00 -- please make an appointment by email. Contact data is on my [webpage](www.janheiland.de).

:memo: Here is my [write-up](http://janheiland.de/script-daes/) of some selected topics.

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
   * Basic algebraic concepts 
   * Normal forms [[week 2]](#week-2)
   * Solvability and representations of solutions <!--- [[week 3]](#week-3)[[week 4]](#week-4) -->
 0. Linear time-varying and nonlinear DAEs (4+1)
   * Fundamental differences with the linear time-invariant case 
   * Time-dependent equivalence transformations and canonical forms <!--- [[week 5]](#week-5) -->
   * *Derivative Arrays* <!--- [[week 6]](#week-6) -->
   * *Differentiation-index and Strangeness-index*
 0. Numerical integration of DAEs (6+2)
   * Digression: Numerical integration of ODEs
   * Runge-Kutta methods (RKM) for DAEs with constant coefficients <!--- [[week 7]](#week-7)[[week 8]](#week-8) -->
   * RKM methods for semi-explicit "index-1" DAEs <!--- [[week 9]](#week-9) -->
   * RKM methods for implicit "index-1" DAEs
   * *Backward Differencing* for DAEs <!--- [[week 10]](#week-10) -->
 0. Numerical Methods for index reduction (1)
   * Derivative Arrays
   * Minimal Extension
 0. DAEs with controls (1) <!--- [[week 11]](#week-11) -->
   * Representation as *Behavior*
   * Index reduction through *Feedback*

### Exercises

| Date | Topic | Sheet |
| ------- | ------ | ------- |
| [October 25th](#exercisei) | I - Introductory Considerations and Basic Notions | [ueb1.pdf](exercises/01/ueb01.pdf) |
| [November 2nd](#exerciseii) | II - Linear DAEs with constant coefficients | [ueb2.pdf](exercises/02/ueb2.pdf) |
| [November 16th](#exerciseiii) | III - linear daes with time-varying coefficients | [ueb3.pdf](exercises/03/ueb3.pdf) |
| [December 6th](#exerciseiv) | IV - one step methods | [ueb4.pdf](exercises/04/ueb04.pdf) |
| [January 17th](#exercisev) | V - higher index and nonlinear equations | [ueb5.pdf](exercises/05/ueb05.pdf) | 

### Week 1

#### Introductory considerations (1)

+++ DAEs are coupled differential and nondifferential (algebraic) equations +++ cf. the pendulum +++ which is naturally modelled as a DAE +++ as are electrical circuits, chemical reactions, and flows +++ in numerical schemes, equations are solved approximately  +++  [back to overview](#overview)

#### General notions from DAE calculus (1)
+++ we consider *C1*-solutions although there are many ways to define less regular solutions +++ existence of solutions depends on several factors +++ smoothness of *right hand sides* +++ consistency of initial values +++ *hidden constraints* and *underlying ODE* +++ many ways to classify DAEs <-> many *indices* +++ [back to overview](#overview)

### Week 2

#### Linear DAEs with constant coefficients (1)
+++ variable transforms and scalings do not affect solvability +++ DAEs <-> (E, A) matrix pairs +++ canonical forms +++ Weierstrass canonical form +++ canonical form of a linear DAE with constant coefficients +++ [back to overview](#overview)

#### Linear DAEs with constant coefficients (2)
+++ splitting of DAEs into an ODE and a nilpotent DAE +++ explicit solution of the nilpotent DAE +++ index of a matrix pair (E,A) and its well-definedness +++ [back to overview](#overview)

### Week 3 

<h4 id="exercisei"> Course Exercise sheet I - Oct 25th </h4>
+++ multibody systems +++ separation of algebraic and differential parts +++ remodelling of the simple pendulum as ODE +++ Navier-Stokes equations +++ links to [ode modelling of the pendulum](http://www.engr.iupui.edu/~skoskie/ECE680/ECE680_l3notes.pdf) and the overhead crane +++ [back to overview](#overview)

#### Linear DAEs with constant coefficients (3)
+++ solvability solved +++ way to arrive at a explicit solution formula +++ definition of the Drazin inverse +++ properties of the Drazin inverse +++ [back to overview](#overview)

### Week 4 

#### Linear DAEs with constant coefficients (4) 

+++ DAE as superposition of a nilpotent DAE and an *index-1* DAE +++ explicit formula for all solutions of the homogeneous equations +++ explicit form of a solution of the inhomogeneous equations +++ [back to overview](#overview)

<h4 id="exerciseii"> Course Exercise sheet II - Nov 2nd </h4>
+++ regularity and Kronecker form of 3x3 examples +++ index-1 condition +++ regularity and commutativity +++ Drazin inverse as group inverse +++ [back to overview](#overview)

### Week 5 

#### Linear DAEs with time-varying coefficients (1)

+++ regularity of matrix pairs does not say much about solvability of LTV DAEs +++ time-dependent state transformations +++ global and local equivalence of matrix function pairs +++ [back to overview](#overview)


#### Linear DAEs with time-varying coefficients (2)

+++ characteristic values +++ canonical form for local equivalence transformations +++ time-varying SVD +++ canonical form for global equivalence transformations +++ [back to overview](#overview)

### Week 6 

#### Linear DAEs with time-varying coefficients (3)
+++ global equivalence ctd. +++ strangeness index +++ derivative arrays +++ [back to overview](#overview)


<h4 id="exerciseiii"> Course Exercise sheet III - Nov 16th </h4>
+++ global/local equivalence of matrix pairs +++ time-varying Drazin inverse +++ [back to overview](#overview)

### Week 7

#### Linear DAEs with time-varying coefficients (4)
strangeness free condensed form of linearized Navier-Stokes equations +++ derivative arrays for nonlinear DAEs +++ [back to overview](#overview)

#### Index-Reduction
general ideas and notions +++ local computation of the strangeness-free reformulation +++ minimal extension for NSE +++ see Kunkel/Mehrmann book 6.4 or this [original paper](http://www.mathematik.uni-leipzig.de/MI/kunkel/papers/km15.ps.gz) on *minimal extension* +++ [back to overview](#overview)

### Week 8

#### Homework -- Numerical Methods for ODEs

How does Euler's method work. +++ What is the consistency error? +++ What is stability? +++ What is meant by convergence? +++ What are Runge-Kutta methods +++ Here is a [scan](files/intro-num-odes.pdf) of the lecture I had on this by Hans-G&ouml;rg Roos back then. +++ [back to overview](#overview)

#### Numerical Solutions of DAEs (1)
+++ basic notions and definitions +++ Kronecker product and perfect shuffle +++ Runge-Kutta methods +++ [back to overview](#overview)

### Week 9

<h4 id="exerciseiv">Course Exercise sheet IV</h4>
+++ effect of rounding errors +++ consistency errors +++ two-stage Gauss method for ODEs and DAEs +++ Runge-Kutta method for linear DAEs +++ CODING: C1:*Explicit Euler and rounding errors* +++  C2:*Implicit Euler* for linear DAEs with time-varying coefficients +++ Resources: Matlab implementation by Jens Bremer -- [[zip file](exercises/04/code/Ex4_JensBremer.zip)], Python implementation -- [[webview](exercises/04/code/4c2.html)], [[ipython notebook](exercises/04/code/4c2.ipynb)], [[python file](exercises/04/code/4c2.py)] -- [[py-script to compute κs]](exercises/04/code/dae-butcher.py) +++ [back to overview](#overview)

#### Numerical Solutions of DAEs (3)
+++ Numerical analysis of Runge-Kutta schemes for DAEs with constant coefficients +++ the local consistency error +++ [back to overview](#overview)

### Week 10

#### Numerical Solutions of DAEs (4)
+++ Numerical analysis of Runge-Kutta schemes for DAEs with constant coefficients +++ the global consistency error +++ stiffly accurate RKM +++ [back to overview](#overview)

#### Numerical Solutions of DAEs (5)
+++ Numerical analysis of Runge-Kutta schemes for DAEs with constant coefficients +++ BDF schemes +++ formulation and warnings concerning RKM for DAEs with time-varying coefficients +++ [back to overview](#overview)


### Week 11
#### Numerical Solutions of DAEs (6-7)
+++ online lecture +++ RKM for nonlinear DAEs +++ semi-explicit strangeness-free +++ collocation and RKM +++ [back to overview](#overview)

### Week 12
#### Numerical Solutions of DAEs (8)
RKM for nonlinear DAEs +++ semi-explicit index-2 +++ the *Hairer-Wanner* analysis approach +++ recap: collocation and RKM +++ [back to overview](#overview)

#### Overview on Results and Software
+++ see the [script](http://janheiland.de/script-daes/numerical-analysis-and-software-overview.html) +++ [back to overview](#overview)

### Week 13
<h4 id="exercisev">Course Exercise sheet V - July 5th </h4>
+++ mass-spring chain +++ minimal extension +++ 2-stage Radau IIa +++ CODING: *Implicit Euler* for the nonlinear pendulum equations --- *Radau IIa* for the mass-spring manoeuvre --- simulation of index reduced systems +++ Resources: Use the code from the previous [exercise iv](#exerciseiv) --- check out the [*Oberwolfach snapshot*](http://www.mfo.de/math-in-public/snapshots/files/wie-steuert-man-einen-kran) on the mass-spring chain (in German) or the more verbose [preprint](http://www.mfo.de/scientific-programme/publications/owp/2015/OWP2015_18.pdf) (in English) +++ [back to overview](#overview)

### Literature

| Author | Title | comments |
| ------- | ------ | ------- |
| Kunkel, Mehrmann | Differential-Algebraic Equations | Main reference, very concise, sometimes hard to read |
| Hairer, Wanner | Solving ODEs. (Stiff and DAEs) | standard reference for solving ODEs (the first volume), intuitive and practical approach to numerical analysis of certain DAEs |

<!-- 

#### Digression: Numerical Solutions of ODEs - May 25th
+++ basic definitions +++ implicit/explicit Euler +++ consistency and stability +++ Runge-Kutta schemes +++ BDF schemes +++ [back to overview](#overview)



#### Numerical Solutions of DAEs (2) - June 1st
+++ Numerical analysis of Runge-Kutta schemes for DAEs with constant coefficients +++  [back to overview](#overview)


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
-->
