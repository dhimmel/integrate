# Creating a heterogeneous network for drug repurposing

This repository creates our heterogeneous network for [repurposing drugs](https://dx.doi.org/10.15363/thinklab.4). The underlying databases are processed elsewhere but integrated here. Below the network is visualized:

![](viz/network-5k.png?raw=true)

### Components:

+ [`integrate.ipynb`](integrate.ipynb): the python notebook for creating and populating the network. The network is built using the [hetio](https://github.com/dhimmel/hetio) package for heterogeneous networks.

+ [`data`](data): the directory containing saved versions of the network. [`graph.json.gz`](data/graph.json.gz) is the preferred complete-network file.

+ [`data/summary`](data/summary): the directory with tables of network statistics. See the summaries of [metanodes](data/summary/metanodes.tsv) and [metaedges](data/summary/metaedges.tsv).

+ [`viz`](viz): the directory containing network visualizations. Includes a wholistic network [view](viz/network-5k.png) as well as node [degree distributions](viz/degrees.pdf).
