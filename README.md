This project is forked from [Neural Implicit Flow (NIF)](https://github.com/pswpswpsw/nif#neural-implicit-flow-nif-mesh-agnostic-dimensionality-reduction) by [Shaowu Pan](http://www.shaowupan.com/). NIF is a mesh-agnostic, dimensionality reduction paradigm for modeling complex spatio-temporal fields. NIF has a hypernet structure that isolates the spatial complexity from the parameter (time, Reynold's number, etc.) complexity. For more details on NIF, please see this [paper](https://arxiv.org/pdf/2204.03216.pdf).

# Pruned Neural Implicit Flow (pNIF)

## NIF Background

NIF has a hypernetwork structure made up of two MLP networks called ShapeNet and ParameterNet. The weights and biases of ShapeNet are determined entirely by the output of ParameterNet. In other words, ParameterNet learns the parameters needed for spatial reconstruction of the flow field. 

| ![nif_structure](figs/nif.jpg) | 
|:--:| 
| *Hypernetwork structure of NIF [[1]](#1)* |

NIF is built using **Keras** subclassing methods and **TensorFlow 2.x**. This allows the user to use built-in Keras compiling, training, and evaluation functions on a NIF model. A NIF model with pruning functionality, called pNIF, is also compatible with the above Keras functions. 

## Pruning NIF 

## References
<a id="1">[1]</a> 
Pan, Shaowu, Steven L Brunton, and J. Nathan Kutz. “Neural Implicit Flow: a mesh-agnostic dimensionality reduction paradigm of spatio-temporal data.” arXiv preprint arXiv:2204.03216 (2022).
