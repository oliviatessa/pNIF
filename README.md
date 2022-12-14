This project is forked from [Neural Implicit Flow (NIF)](https://github.com/pswpswpsw/nif#neural-implicit-flow-nif-mesh-agnostic-dimensionality-reduction) by [Shaowu Pan](http://www.shaowupan.com/). NIF is a mesh-agnostic, dimensionality reduction paradigm for modeling complex spatio-temporal fields. NIF has a hypernet structure that isolates the spatial complexity from the parameter (time, Reynold's number, etc.) complexity. For more details on NIF, please see this [paper](https://arxiv.org/pdf/2204.03216.pdf).

# Pruned Neural Implicit Flow (pNIF)

NIF has a hypernet structure made up of two MLP networks called ShapeNet and ParameterNet. 


![This is an image!](figs/nif.jpg)
*caption [[1]](#1)*

| ![nif_structure](figs/nif.jpg) | 
|:--:| 
| *caption [[1]](#1)* |

## References
<a id="1">[1]</a> 
Pan, Shaowu, Steven L Brunton, and J. Nathan Kutz. “Neural Implicit Flow: a mesh-agnostic dimensionality reduction paradigm of spatio-temporal data.” arXiv preprint arXiv:2204.03216 (2022).
