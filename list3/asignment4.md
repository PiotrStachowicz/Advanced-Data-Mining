# Assignment 4 – GNN
**Advanced Data Mining**
**Deadline:** 23.03.2026 7:00 (SKOS), 16–24.03.2026 (presentation)

#### Piotr Stachowicz 337942
## Task 1: Action of the Graph Laplacian [2 points]

Let $G = (V, E)$ be an undirected graph with $|V| = n$.

**Definitions:**
- Adjacency matrix $A \in \mathbb{R}^{n \times n}$: $A_{ij} = 1$ if $i \sim j$, otherwise $0$
- Degree matrix $D \in \mathbb{R}^{n \times n}$ (diagonal): $D_{ii} = \deg(i)$
- Graph Laplacian: $L = D - A$
- Action on a vector: $(Lx)_i = \sum_{j \sim i}(x_i - x_j)$

Consider the graph (path): $1 - 2 - 3$

and the vector:
$$x = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

### 1.1 Compute the matrices $A$, $D$, $L = D - A$

**Adjacency matrix $A$:**

$$A = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$

**Degree matrix $D$:**

$$D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

**Laplacian $L = D - A$:**

$$L = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$$

### 1.2 Compute the vector $Lx$

$$Lx = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$$


**Questions:**

- **Which vertices have non-zero values?**

  Non-zero values appear on vertices 1 and 2.

- **On which values does $(Lx)_i$ depend?**

  $(Lx)_i$ depends on $x_i$ and value of their 1-step neighbours.

- **Describe in words what operation $Lx$ performs:**

  It transforms input vector x to a representation, where it's dependent on it's neighbours.

### 1.3 Compute $L^2 x = L(Lx)$

$$L^2x = L(Lx) = L\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}$$


**Questions:**

- **Does a non-zero value appear at vertex 3?**

  Yes.

- **Does $L^2 x$ depend only on neighbors, or also on more distant vertices?**

  It is dependent on vertices of distance 2.

### 1.4 General rule for $L^k x$

Each i-th value of vector x is dependent on the original input value and vertices which are at maximum distance of k.  

## Task 2: Weighted Graph Laplacian [2 points]

Let $G = (V, E)$ be an undirected weighted graph with $|V| = n$.

**Definitions:**
- Weighted adjacency matrix: $W_{ij} = w_{ij}$ if $(i,j) \in E$, otherwise $0$
- Degree matrix: $D_{ii} = \sum_j w_{ij}$
- Weighted Laplacian: $L = D - W$
- Action on a vector: $(Lx)_i = \sum_{j \sim i} w_{ij}(x_i - x_j)$

Consider the weighted graph:
$$1 \overset{1}{-} 2 \overset{2}{-} 3$$

with weights $w_{12} = 1$, $w_{23} = 2$ and the vector:
$$x = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

### 2.1 Construct the matrices $W$, $D$, $L = D - W$

**Matrix $W$:**

$$W = \begin{pmatrix} \cdot & 1 & \cdot \\ 1 & \cdot & 2 \\ \cdot & 2 & \cdot \end{pmatrix}$$

**Matrix $D$:**

$$D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

**Laplacian $L$:**

$$L = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 3 & -2 \\ 0 & -2 & 2 \end{pmatrix}$$

### 2.2 Compute $Lx$

$$Lx = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$$

**Compare with the unweighted case. Which influence is stronger: from vertex 1 to 2, or from vertex 2 to 3?**

Now each vertex has different weights. In this particular step, weight from vertex 1 to 2 has more influence, because we have not reached vertex 3 yet.

### 2.3 Compute $L^2 x$

$$L^2x = L(Lx) = L\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ -4 \\ 2 \end{pmatrix}$$

**Does the value at vertex 3 depend on the weight $w_{23}$? Explain.**

Yes, we multiply by $w_{23}$.

### 2.4 Show that $x^T L x = \sum_{(i,j) \in E} w_{ij}(x_i - x_j)^2$

$$x^T L x = x^T (D - W) x = x^T D x - x^T W x$$

$$x^T D x = \sum_{i=1}^n D_{ii} x_i^2 = \sum_{i=1}^n \left( \sum_{j=1}^n w_{ij} \right) x_i^2 = \sum_{i,j} w_{ij} x_i^2$$

$$x^T W x = \sum_{i=1}^n \sum_{j=1}^n w_{ij} x_i x_j$$

$$x^T L x = \sum_{i,j} w_{ij} x_i^2 - \sum_{i,j} w_{ij} x_i x_j$$

$$\sum_{i,j} w_{ij} x_i^2 - \sum_{i,j} w_{ij} x_i x_j = \frac{1}{2} \sum_{i,j} w_{ij}(x^2_i - 2x_ix_j + x^2_j) = \sum_{i,j} w_{ij}(x_i - x_j)^2\$$

### 2.5 Interpret the role of weights

**What happens when a weight $w_{ij}$ is very large?**

Weight $w_{ij}$ is the penalty that we impose on the difference between the two verticies.

## Task 3: Kernel of the Laplacian [1 point]

Let $G = (V, E)$ be an undirected graph with Laplacian matrix $L$.

### 3.1 Show that $L\mathbf{1} = 0$

Since $(Lx)_i​=\sum_{j∼i​}(x_i​−x_j​)$ where j is neighbour, then since each is equal to 1 => L1=0.

### 3.2 Intuitive explanation

**Give an intuitive explanation why $L\mathbf{1} = 0$, based on the formula $(Lx)_i = \sum_{j \sim i}(x_i - x_j)$:**

Since, we can think of x_i as of how much it differs from it's neighbours, if all verticies are of value 1, then x_i at each i is not standing out from it's neighbours => 0.