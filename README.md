# rsa-wiener-attack

This repository is a simple implementation of the wiener attack on a textbook implementation of RSA encryption. 

## Getting Started

#### Navigate Project

- `utils/`: This folder consist of the necessary python scripts for implementing RSA and wiener's attack.
  - `utils/common_utils.py`: This script consist of helper functions.
  - `utils/rsa.py`: This script consist of the rsa and wiener's attack implementation.
  - `primes.csv`: Consist the first million primes for testing rabin miller implementation.
- `notebook`: Consist of python notebooks for demo

#### Installations 

- See `requirements.txt`
- Tested on `python=3.8`

#### Run

- Clone this repo and navigate to the `notebook/presentation.ipynb` to run the demo

## Acknowledgements

* D. Boneh and G. Durfee. “Cryptanalysis of RSA with Private Key d Less than N^0.292”. In: Advances in Cryptology — EUROCRYPT ’99. Ed. by J. Stern. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 1999, pp. 1–11. [DOI: 10.1007/3-540-48910-X_1](https://doi.org/10.1007/3-540-48910-X_1).
* W. Susilo, J. Tonien, and G. Yang. “The Wiener Attack on RSA Revisited: A Quest for the Exact Bound”. In: Information Security and Privacy. Ed. by J. Jang-Jaccard and F. Guo. Lecture Notes in Computer Science. Cham: Springer International Publishing, 2019, pp. 381–398. [DOI: 10.1007/978-3-030-21548-4_21](https://doi.org/10.1007/978-3-030-21548-4_21).
* M. J. Wiener. “Cryptanalysis of Short RSA Secret Exponents”. In: Advances in Cryptology — EUROCRYPT ’89. Ed. by J.-J. Quisquater and J. Vandewalle. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 1990, pp. 372–372. [DOI: 10.1007/3-540-46885-4_36](https://doi.org/10.1007/3-540-46885-4_36).



