---
title: "Parameter control in the presence of uncertainties"
collection: publications
permalink: /publication/2021-06-11-parameter-control-in-the-presence-of-uncertainties.md
excerpt: 'My PhD dissertation, which focuses on the calibration of numerical models in the presence of uncertainties'
date: 2021-11-06
paperurl: 'https://tel.archives-ouvertes.fr/tel-03275015'
citation: 'Victor Trappler. Parameter control in the presence of uncertainties. 2021'
---

## Abstract
 To understand and to be able to forecast natural
phenomena is increasingly important nowadays, as those predictions are
often the basis of many decisions, whether economical or
ecological. In order todo so, mathematical models are introduced to
represent the reality at a specific scale, and are then implemented
numerically.

However in this process of modelling, many complex
phenomena occurring at a smaller scale than the one studied have to be
simplified and quantified. This often leads to the introduction of
additional parameters, which then need to be properly
estimated. Classical methods of estimation usually involve an
objective function, that measures the distance between the simulations
and some observations, which is then optimised. Such an optimisation
require many runs of the numerical model and possibly the computation
of its gradient, thus can be expensive to evaluate
computational-wise.However, some other uncertainties can also be
present, which represent some uncontrollable and external factors that
affect the modelling. Those variables will be qualified as
environmental. By modelling them with a random variable, the objective
function is then a random variable as well, that we wish to minimise
in some sense. Omitting the random nature of the environmental
variable can lead to localised optimisation, and thus a value of the
parameters that is optimal only for the fixed nominal value.

To overcome this, the minimisation of the expected value of the
objective function is often considered in the field of optimisation
under uncertainty for instance.In this thesis, we focus instead on the
notion of regret, that measures the deviation of the objective
function from its optimal value given a realisation of the
environmental variable. This regret (either additive or relative)
translates a notion of robustness through its probability of exceeding
a specified threshold. So, by either controlling the threshold or the
probability, we can define a family of estimators based on this
regret.

The regret can quickly become expensive to evaluate since it requires
an optimisation of the objective for every realisation of the
environmental variable. We then propose to use Gaussian Processes (GP)
in order to reduce the computational burden of this evaluation. In
addition to that, we propose a few adaptive methods in order to
improve the estimation: the next points to evaluate are
chosensequentially according to a specific criterion, in a Stepwise
Uncertainty Reduction (SUR) strategy. 

Finally, we will apply some of the methods introduced in this thesis
on an academic problem of parameter estimation. We will study the
calibration of the bottom friction of a model of the Atlantic ocean
near the French coasts, while introducing some uncertainties in the
forcing of the tide, and get a robust estimation of this friction
parameter in a twin experiment setting.



## Keywords
+ Calibration
+ Robust optimisation
+ Relative-regret
+ Shallow-water equations
+ Ocean Modelling
