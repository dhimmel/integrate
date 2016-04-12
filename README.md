# Building hetionet: data integration, hetnet permutation, and Neo4j import

[![DOI](https://zenodo.org/badge/14475/dhimmel/integrate.svg)](https://zenodo.org/badge/latestdoi/14475/dhimmel/integrate)

Hetnets are networks with multiple types of nodes and edges. This repository creates `hetionet v1.0`, which is a hetnet encoding biology, disease, and pharmacology. We created `hetionet v1.0` for [Rephetio](https://doi.org/10.15363/thinklab.4), our project to systematically evaluate why drugs work and to predict new therapeutic uses for existing drugs.

**Note: this repository is for building `hetionet v1.0`. We recommend that users interested in downloading and using the completed hetnet, do so from the [`dhimmel/hetionet`](https://github.com/dhimmel/hetionet) repository.**

## Execution

The dependencies are listed in [`environment.yml`](environment.yml). All available through Anaconda or
PyPI, except for [`hetio`](https://github.com/dhimmel/hetio).

1. [`precompile.sh`](precompile.sh) executes notebooks which combine multiple resources into a single type of edge. See the contents of [`compile`](compile) for more information.

2. [`build.sh`](build.sh) builds the hetnet, creates permuted derivatives, and exports the hetnet to Neo4j.

## Notebooks

1. [`integrate.ipynb`](integrate.ipynb) creates the hetnet, by integrating data that is stored either in [`compile`](compile) or elsewhere on GitHub. All GitHub links use commit hashes to be version specific. The JSON-formatted hetnet is exported to [`data/hetnet.json.bz2`](data/hetnet.json.bz2).
2. [`permute.ipynb`](permute.ipynb) loads the created hetnet and creates permuted derivatives that preserve node degree but destroy edge specificity. The permuted hetnets are written to [`data/permuted`](data/permuted), but are not uploaded due to file size.
3. [`neo4j-import.ipynb`](neo4j-import.ipynb) imports the hetnet and its permutations into separate neo4j instances. These neo4j instances are not uploaded due to file size and [licensing issues](https://doi.org/10.15363/thinklab.d130). Currently, neo4j-community-2.3.3 is used.

## Components

+ [`data`](data): the directory containing saved versions of the network.
+ [`data/summary`](data/summary): the directory with tables of network statistics. See the summaries of [metanodes](data/summary/metanodes.tsv) and [metaedges](data/summary/metaedges.tsv).
+ [`viz`](viz): the directory containing network visualizations. Includes a holistic network [view](viz/network-5k.png) as well as node [degree distributions](viz/degrees.pdf).

## License

All original content in this repository is released as [CC0](https://creativecommons.org/publicdomain/zero/1.0/ "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"). However, the hetnet integrates data from many resources and users should consider the licensing of each source. We apply a `license` attribute on a per node and per edge basis for sources with defined licenses. However, some resources don't provide any license, so for those we've requested permission. More information is [available on Thinklab](http://thinklab.com/discussion/integrating-resources-with-disparate-licensing-into-an-open-network/107). See [`licenses/README.md`](licenses/README.md) for a table of all resources and their licensing.
