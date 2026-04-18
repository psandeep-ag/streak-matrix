<img width="1239" height="316" alt="image" src="https://github.com/user-attachments/assets/0fa215ad-f5ce-4c47-a955-c82cdca74b04" />



# Solving Ax = b: Least Squares, Rank, and Residuals

## 1. Core Concept

This problem is about an **overdetermined system** — more equations than unknowns.

```
A is 3×2,  x is 2×1,  b is 3×1

3 equations:   x₁ + 2x₂ = −1
              2x₁ − x₂  =  3
              3x₁ + x₂  =  2

2 unknowns: x₁, x₂
```

> **3 equations, 2 unknowns — generically NO exact solution exists.**
> The best we can do is find x̂ that makes Ax as CLOSE to b as possible.
> This is the **Least Squares** problem.

---

## 2. First Principles

### Why no exact solution?

b must lie in the **column space** of A for Ax = b to have an exact solution.

```
Column space of A = all vectors of the form:

     x₁[1]  +  x₂[ 2]     for any x₁, x₂ ∈ ℝ
       [2]       [-1]
       [3]       [ 1]
```

This spans a **2D plane** inside **3D space**. The vector b is a random point in 3D — it almost certainly does NOT lie on that 2D plane.

### The Least Squares Idea

Since we can't hit b exactly, we find the **point on the column space plane closest to b**:

```
        b  ●  ← actual b (off the plane)
           │
           │ ← residual e = b − Ax̂
           │   (perpendicular to column space)
           ▼
    ───────●─────────  ← Column space of A (2D plane)
          Ax̂  ← closest point to b ON the plane
```

The closest point is found by dropping a **perpendicular** from b onto the column space. This perpendicular condition is:

$$A^T(b - A\hat{x}) = 0$$

Which gives the **Normal Equations:**

$$A^T A \hat{x} = A^T b$$

---

## 3. How to Think Through This

```
Step 1: Is the system overdetermined? → rows > cols? → YES (3>2)
             ↓
Step 2: Does exact solution exist? → is b in col(A)?
             ↓
Step 3: If not → use Least Squares → solve Normal Equations
             ↓
Step 4: Compute residual e = b − Ax̂
             ↓
Step 5: Is Ax̂ − b = 0? → Only if b was in col(A) to begin with
```

---

## 4. Methodology — Complete Solution

### Step 1: Find Rank of A

$$A = \begin{bmatrix} 1 & 2 \\ 2 & -1 \\ 3 & 1 \end{bmatrix}$$

Row reduce:
```
R2 → R2 − 2R1:    [0, −5]
R3 → R3 − 3R1:    [0, −5]
R3 → R3 − R2:     [0,  0]

Result:
[1   2]
[0  −5]
[0   0]
```

**2 pivot columns → Rank(A) = 2**

This means:
- Columns are linearly independent ✓
- AᵀA is invertible ✓
- Unique least squares solution exists ✓

---

### Step 2: Compute AᵀA

$$A^T = \begin{bmatrix} 1 & 2 & 3 \\ 2 & -1 & 1 \end{bmatrix}$$

$$A^TA = \begin{bmatrix} 1&2&3\\2&-1&1 \end{bmatrix} \begin{bmatrix}1&2\\2&-1\\3&1\end{bmatrix}$$

$$= \begin{bmatrix} 1+4+9 & 2-2+3 \\ 2-2+3 & 4+1+1 \end{bmatrix} = \begin{bmatrix} 14 & 3 \\ 3 & 6 \end{bmatrix}$$

---

### Step 3: Compute Aᵀb

$$A^Tb = \begin{bmatrix}1&2&3\\2&-1&1\end{bmatrix}\begin{bmatrix}-1\\3\\2\end{bmatrix} = \begin{bmatrix}-1+6+6\\-2-3+2\end{bmatrix} = \begin{bmatrix}11\\-3\end{bmatrix}$$

---

### Step 4: Solve Normal Equations AᵀAx̂ = Aᵀb

$$\begin{bmatrix}14&3\\3&6\end{bmatrix}\hat{x} = \begin{bmatrix}11\\-3\end{bmatrix}$$

Find inverse of AᵀA:

$$\det(A^TA) = 14\times6 - 3\times3 = 84 - 9 = 75$$

$$(A^TA)^{-1} = \frac{1}{75}\begin{bmatrix}6&-3\\-3&14\end{bmatrix}$$

Solve:

$$\hat{x} = \frac{1}{75}\begin{bmatrix}6&-3\\-3&14\end{bmatrix}\begin{bmatrix}11\\-3\end{bmatrix} = \frac{1}{75}\begin{bmatrix}66+9\\-33-42\end{bmatrix} = \frac{1}{75}\begin{bmatrix}75\\-75\end{bmatrix}$$

$$\boxed{\hat{x} = \begin{bmatrix}1\\-1\end{bmatrix}}$$

---

### Step 5: Compute Ax̂ and check residual

$$A\hat{x} = \begin{bmatrix}1&2\\2&-1\\3&1\end{bmatrix}\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}1-2\\2+1\\3-1\end{bmatrix} = \begin{bmatrix}-1\\3\\2\end{bmatrix}$$

$$e = b - A\hat{x} = \begin{bmatrix}-1\\3\\2\end{bmatrix} - \begin{bmatrix}-1\\3\\2\end{bmatrix} = \begin{bmatrix}0\\0\\0\end{bmatrix}$$

$$\boxed{A\hat{x} - b = 0}$$

---

## 5. Key Ideas

| Idea | Meaning |
|---|---|
| **Overdetermined system** | More equations than unknowns — usually inconsistent |
| **Rank = 2** | Both columns independent → unique least squares solution |
| **Normal equations** | AᵀAx̂ = Aᵀb — the fundamental least squares formula |
| **Residual = 0** | Means b accidentally WAS in the column space — exact solution existed! |
| **Projection** | Ax̂ is the orthogonal projection of b onto col(A) |

---

## 6. Framework

```
         Given: Ax = b
                │
    ┌───────────▼────────────┐
    │  Is system square?     │
    │  rows = cols?          │
    └───────┬────────────────┘
            │NO (overdetermined)
            ▼
    ┌───────────────────────┐
    │  Find Rank(A)         │
    │  via row reduction    │
    └───────┬───────────────┘
            │
    ┌───────▼───────────────┐
    │  Rank = num cols?     │──NO──→ Infinitely many solutions
    └───────┬───────────────┘
            │YES
            ▼
    ┌───────────────────────┐
    │  Solve Normal Eqs:    │
    │  AᵀAx̂ = Aᵀb          │
    │  x̂ = (AᵀA)⁻¹Aᵀb     │
    └───────┬───────────────┘
            │
    ┌───────▼───────────────┐
    │  Compute residual:    │
    │  e = b − Ax̂          │
    └───────┬───────────────┘
            │
    ┌───────▼───────────────┐
    │  e = 0?               │
    │  YES → b in col(A)    │
    │  NO  → true LS approx │
    └───────────────────────┘
```

---

## 7. Why This Problem Is Important

> **Most real-world problems are overdetermined. Reality gives you more data than unknowns.**

- You never have a perfectly consistent system in practice
- Measurement noise, experimental error, model mismatch — all create overdetermined systems
- Least squares is the **backbone of data fitting, regression, and estimation**

---

## 8. Applications

| Domain | Application |
|---|---|
| **Machine Learning** | Linear regression — fitting a line to thousands of data points |
| **Computer Vision** | Camera calibration, homography estimation |
| **GPS/Navigation** | Combining signals from multiple satellites to find position |
| **Signal Processing** | Filter design, system identification |
| **Robotics** | Sensor fusion — combining noisy sensors |
| **Economics** | Fitting economic models to historical data |
| **Structural Engineering** | Stress analysis with more constraints than variables |

---

## 9. Other Examples

**Example A — True Least Squares (residual ≠ 0):**
```
A = [1  0]    b = [1]
    [1  1]        [2]
    [1  2]        [4]   ← this b is NOT in col(A)

x̂ = best fit line → residual ≠ 0
```

**Example B — Underdetermined (rank < cols):**
```
A = [1  2  3]    b = [6]
    [2  4  6]        [12]

Rank = 1, infinite solutions — need regularization
```

---

## 10. Toughest Question Possible

> **Given:**
> $$A = \begin{bmatrix}1&1&0\\1&0&1\\0&1&1\\1&1&1\end{bmatrix}, \quad b = \begin{bmatrix}2\\3\\1\\4\end{bmatrix}$$
>
> **(i)** Find Rank(A). Does a unique least squares solution exist?
>
> **(ii)** Compute x̂ using normal equations. What is the geometric meaning of Ax̂?
>
> **(iii)** Decompose b = p + e where p = Ax̂ is the projection and e is the residual. Verify p ⊥ e.
>
> **(iv)** What is the projection matrix P = A(AᵀA)⁻¹Aᵀ? Verify P² = P and Pᵀ = P (idempotent + symmetric).
>
> **(v)** If b is replaced by b' = b + n where n is in the null space of Aᵀ, how does x̂ change? Why?
>
> **(vi)** Compute the SVD of A and express x̂ using the pseudoinverse A⁺. Connect this to the normal equation solution.

---

## 11. Intuitive Explanation of This Specific Solution

### Why did we get residual = 0?

This is the beautiful surprise of this problem. Even though we have 3 equations and 2 unknowns (which usually means NO exact solution), here:

```
x̂ = [1, −1] satisfies ALL THREE equations perfectly:

Eq 1:  1(1) + 2(−1) = −1  ✓  matches b₁ = −1
Eq 2:  2(1) + (−1)(−1) = 3  ✓  matches b₂ = 3
Eq 3:  3(1) + 1(−1) = 2  ✓  matches b₃ = 2
```

**b happened to lie exactly on the column space plane of A.** The "3D point" b was already sitting on the "2D plane" — so the perpendicular drop had zero length.

### The Geometric Picture

```
                b●  ← b is right here on the plane!
               /│\
              / │ \
             /  │  \      ← Column space of A
            /   │   \        (2D plane in 3D)
           /    ↓    \
          /    Ax̂     \
         /      ●      \
        /________________\

Since b is ON the plane: Ax̂ = b exactly, residual = 0
```

### Why did we still use Least Squares?

Because we didn't KNOW in advance that b was in the column space. The least squares machinery is **general** — it automatically gives the exact solution when one exists (residual = 0) and the best approximation when one doesn't (residual ≠ 0).

> **Least squares is not just for approximate solutions — it's a universal solver that degrades gracefully from exact to approximate as needed.**




# Rank, Pivots, and Why Everything Connects

## Start Here: What is a Pivot?

When you row-reduce a matrix, a **pivot** is the first non-zero entry in each row after elimination.

```
A = [1   2]          R2 → R2 - 2R1      [1   2]
    [2  -1]    →                    →   [0  -5]
    [3   1]          R3 → R3 - 3R1      [0  -5]

                     R3 → R3 - R2       [1   2]
                                        [0  -5]
                                        [0   0]
```

The pivots are the **bold entries**:
```
[1   2]   ← pivot: 1
[0  -5]   ← pivot: -5
[0   0]   ← NO pivot (zero row)
```

**2 pivots → Rank = 2**

---

## Condition 1: Columns are Linearly Independent

### Mathematical Statement

Columns c₁, c₂ of A are linearly independent if:

$$\alpha_1 c_1 + \alpha_2 c_2 = 0 \implies \alpha_1 = 0 \text{ AND } \alpha_2 = 0$$

In other words: **the only way to combine columns to get zero is the trivial way.**

### The Pivot Connection — Mathematically

After row reduction:
```
[1   2]
[0  -5]
[0   0]
```

Suppose α₁c₁ + α₂c₂ = 0. This means Ax = 0 where x = [α₁, α₂]ᵀ

Row reduction gives:
```
From row 2:   -5α₂ = 0   →   α₂ = 0
From row 1:    α₁ + 2(0) = 0   →   α₁ = 0
```

**Every pivot row forces one variable to be zero — back-substitution kills all freedom.**

If there were NO pivot in column 2 (i.e., the column was a multiple of column 1), you'd have:
```
[1   2]       c₂ = 2c₁
[0   0]   →   so 2c₁ - c₂ = 0
[0   0]       non-trivial solution exists → DEPENDENT
```

### Intuitive Picture

```
INDEPENDENT columns:              DEPENDENT columns:
                                  
c₂  ↗                            c₂ = 2c₁ ↗
   /  ← angle between            ↗  (same direction!)
  /     them ≠ 0°               ↗
 / θ                            ↗
└──────→ c₁                    └──────→ c₁

They span a 2D PLANE            They only span a 1D LINE
= full rank                     = rank deficient
```

**Each pivot = one new independent direction being added.**
- 1st pivot → column 1 points somewhere new ✓
- 2nd pivot → column 2 points somewhere NEW (not along column 1) ✓
- No 3rd pivot → row 3 is redundant, adds no new direction

---

## Condition 2: AᵀA is Invertible

### Why This Is NOT Obvious

AᵀA is always:
- **Square** (2×2 here, since A is 3×2)
- **Symmetric** (since (AᵀA)ᵀ = AᵀA)
- **Positive semi-definite** (since xᵀAᵀAx = ||Ax||² ≥ 0)

But being invertible requires the stronger condition: **positive DEFINITE**, meaning:

$$x^TA^TAx > 0 \quad \text{for all } x \neq 0$$

### Mathematical Proof of the Connection

$$x^T A^T A x = (Ax)^T(Ax) = \|Ax\|^2$$

AᵀA is invertible
⟺ AᵀA has no zero eigenvalue
⟺ ||Ax||² > 0 for all x ≠ 0
⟺ Ax = 0 has only the trivial solution x = 0
⟺ **A has trivial null space**
⟺ **columns of A are linearly independent**
⟺ **Rank(A) = number of columns**

So the chain is:

```
2 pivots
    ↕
Rank(A) = 2 = number of columns
    ↕
Null space of A = {0} only
    ↕  [because Ax=0 → x=0]
||Ax||² > 0 for all x ≠ 0
    ↕
AᵀA is positive definite
    ↕
AᵀA is invertible
```

### Verify Directly for Our Problem

$$A^TA = \begin{bmatrix}14&3\\3&6\end{bmatrix}$$

Check invertibility:
```
det(AᵀA) = 14×6 − 3×3 = 84 − 9 = 75 ≠ 0  ✓
```

Check positive definiteness — eigenvalues must be > 0:
```
Trace    = 14 + 6 = 20  > 0  ✓
Det      = 75           > 0  ✓
→ Both eigenvalues positive → positive definite ✓
```

### Intuitive Picture

```
CASE 1: Rank = 2 (full column rank)        CASE 2: Rank = 1 (deficient)

AᵀA maps 2D → 2D, STRETCHES space         AᵀA collapses 2D → 1D

   ·  ·  ·              ·  ·  ·              ·  ·  ·
   ·  ·  ·   AᵀA→       ·  ·  ·              ·  ·  ·   AᵀA→  · · · · · ·
   ·  ·  ·              ·  ·  ·              ·  ·  ·
   
 No direction is        Invertible ✓       One direction
 squashed to 0                             squashed to 0
                                           NOT invertible ✗
```

When a direction gets **squashed to zero**, you lose information — you can't recover what went in, so no inverse exists.

---

## Condition 3: Unique Least Squares Solution Exists

### The Normal Equations

The least squares solution satisfies:

$$A^TA\hat{x} = A^Tb$$

For a unique solution to exist, we need to solve this for x̂ — which requires **(AᵀA)⁻¹ to exist**.

### Mathematical Chain

$$A^TA \text{ invertible} \implies \hat{x} = (A^TA)^{-1}A^Tb \text{ is unique}$$

If AᵀA were NOT invertible (singular):
```
AᵀAx̂ = Aᵀb

If AᵀA is singular → it has a null space vector n ≠ 0
If x̂ is one solution → x̂ + αn is ALSO a solution for any α

→ Infinitely many least squares solutions
```

### Why Uniqueness Requires Full Column Rank — Geometrically

```
FULL RANK (rank=2):              RANK DEFICIENT (rank=1):

Column space = 2D plane          Column space = 1D line

        b●                               b●
        │                               /│\
        │⊥                             / │ \
        ▼                             /  │  \
   ─────●─────  (plane)         ─────●──●──●─  (line)
       Ax̂                            ↑  ↑  ↑
   ONE closest point                 Many equally
   on the plane                      close points!
   → unique x̂ ✓                     → infinitely many x̂ ✗
```

When the column space is a full 2D plane, there's **exactly one closest point** to b — like dropping a perpendicular to a flat floor. Unique.

When columns are dependent, the column space collapses to a line — there might be **infinitely many** points on the line equidistant from b in a degenerate case, or the projection isn't even well-defined through a single x.

---

## The Master Chain — Everything Connected

```
┌─────────────────────────────────────────────────────────┐
│                    2 PIVOTS FOUND                       │
└─────────────────────────────┬───────────────────────────┘
                              │ means
                              ▼
┌─────────────────────────────────────────────────────────┐
│              RANK(A) = 2 = num columns                  │
│         (maximum possible rank for 3×2 matrix)          │
└──────────────┬──────────────────────────┬───────────────┘
               │ means                    │ means
               ▼                          ▼
┌──────────────────────┐    ┌─────────────────────────────┐
│  Columns are         │    │  Null space of A            │
│  LINEARLY            │    │  contains ONLY zero         │
│  INDEPENDENT         │    │  Ax = 0 ⟹ x = 0            │
│                      │    │                             │
│  No column is a      │    │  No "hidden" direction      │
│  combo of others     │    │  that A destroys            │
└──────────────────────┘    └──────────────┬──────────────┘
               │                           │
               └─────────────┬─────────────┘
                             │ together imply
                             ▼
┌─────────────────────────────────────────────────────────┐
│              AᵀA IS INVERTIBLE                          │
│         ||Ax||² > 0 for all x ≠ 0                      │
│         det(AᵀA) = 75 ≠ 0                              │
└─────────────────────────────┬───────────────────────────┘
                              │ therefore
                              ▼
┌─────────────────────────────────────────────────────────┐
│         UNIQUE LEAST SQUARES SOLUTION EXISTS            │
│                                                         │
│         x̂ = (AᵀA)⁻¹Aᵀb                               │
│                                                         │
│         ONE closest point in column space to b          │
│         Perpendicular drop from b is unique             │
└─────────────────────────────────────────────────────────┘
```

---

## One-Line Intuition for Each Condition

| Condition | One-Line Intuition |
|---|---|
| **2 pivots = rank 2** | Row reduction found 2 truly independent directions — nothing was redundant |
| **Columns independent** | No column can be "built" from the others — each adds genuinely new information |
| **AᵀA invertible** | A doesn't crush any direction to zero — all information is recoverable |
| **Unique x̂ exists** | There's exactly one point in the column space closest to b — the perpendicular foot is unique |




# Where Does x̂ = (AᵀA)⁻¹Aᵀb Come From?

## Start With the Real Problem

You have:
```
Ax = b

A is 3×2,  b is 3×1,  x is 2×1

3 equations, 2 unknowns → NO exact solution (generically)
```

So what do you actually want?

> **Find x̂ such that Ax̂ is as close to b as possible.**

"Close" means minimize the distance:

$$\min_x \|Ax - b\|^2$$

This is the **least squares problem.** Everything else flows from this one sentence.

---

## Step 1: Why Does No Exact Solution Exist?

Think about what Ax actually does.

```
A is 3×2. It takes a 2D input vector x and produces a 3D output vector.

All possible outputs Ax form a 2D PLANE inside 3D space.
This plane is the COLUMN SPACE of A.

        3D space
        ────────
             b ●  ← b is a random point in 3D
              /│
             / │
            /  │ ← b is OFF the plane
           /   │
──────────●────┘─────────── ← Column space of A
                              (2D plane in 3D)

b is almost certainly NOT on the plane.
So Ax = b has no solution.
```

---

## Step 2: What is the Best We Can Do?

Since we can't reach b exactly, we want to get as **close as possible.**

The closest point on the plane to b is found by dropping a **perpendicular** from b onto the plane.

```
        b ●
          │
          │  ← this is the ERROR vector e = b - Ax̂
          │     it is PERPENDICULAR to the plane
          │
──────────●──────────  ← Column space of A
         Ax̂
         
Ax̂ = closest point to b that lies on the column space plane
```

This perpendicular point **Ax̂** is called the **projection of b onto the column space of A.**

---

## Step 3: The Perpendicularity Condition — Where Aᵀ Comes From

Here is the KEY geometric insight:

> **The error vector e = b − Ax̂ must be perpendicular to EVERY vector in the column space of A.**

Why? Because if e had ANY component along the plane, you could move Ax̂ slightly in that direction and get even closer to b. The minimum distance point is exactly where e is purely perpendicular.

### What does "perpendicular to the column space" mean mathematically?

The column space of A contains all vectors of the form Av. So e must be perpendicular to every such vector:

$$\text{For ALL vectors } v: \quad (Av) \cdot e = 0$$

Write this using dot product as transpose multiplication:

$$(Av)^T e = 0$$

$$v^T A^T e = 0$$

This must hold for ALL v. The only way this is true for every v is:

$$\boxed{A^T e = 0}$$

**THIS is where Aᵀ comes from.** It's not arbitrary. It's the mathematical way of saying "e is perpendicular to the entire column space."

---

## Step 4: Expand Aᵀe = 0 to Get the Normal Equations

Substitute e = b − Ax̂:

$$A^T(b - A\hat{x}) = 0$$

Expand:

$$A^Tb - A^TA\hat{x} = 0$$

Rearrange:

$$\boxed{A^TA\hat{x} = A^Tb}$$

These are called the **Normal Equations.**

"Normal" comes from the Latin word for **perpendicular** — because we're enforcing that the error is perpendicular (normal) to the column space.

---

## Step 5: Solve for x̂

Since Rank(A) = 2 = number of columns, AᵀA is invertible. So multiply both sides by (AᵀA)⁻¹:

$$\hat{x} = (A^TA)^{-1}A^Tb$$

---

## The Complete Derivation in One Flow

```
GOAL: minimize ||Ax - b||²
           │
           │ geometric insight
           ▼
Error e = b - Ax̂ must be ⊥ to column space of A
           │
           │ math translation
           ▼
(Av)ᵀe = 0   for ALL vectors v
           │
           │ simplify
           ▼
vᵀ Aᵀ e = 0   for ALL v
           │
           │ only way this works for ALL v
           ▼
Aᵀe = 0
           │
           │ substitute e = b - Ax̂
           ▼
Aᵀ(b - Ax̂) = 0
           │
           │ expand
           ▼
AᵀAx̂ = Aᵀb        ← Normal Equations
           │
           │ AᵀA is invertible (rank = 2)
           ▼
x̂ = (AᵀA)⁻¹Aᵀb    ← THE FORMULA
```

---

## Why Does Aᵀ Appear Twice?

This confuses everyone. Let's be very explicit.

### First Aᵀ — from the perpendicularity condition

```
Aᵀe = 0

This says: "Test e against every row of Aᵀ"
         = "Test e against every COLUMN of A"
         = "e is perpendicular to every column of A"
         = "e is perpendicular to the column space"
```

### Second Aᵀ — from expanding e

```
Aᵀ(b - Ax̂) = 0
Aᵀb - AᵀAx̂ = 0

The AᵀA comes from Aᵀ acting on Ax̂.
It converts a rectangular system (3×2) into a SQUARE system (2×2).

A    is 3×2    ← rectangular, can't invert
AᵀA  is 2×2    ← square, CAN invert (if full rank)
```

### The dimension story

```
b    is 3×1   (lives in 3D output space)
Aᵀb  is 2×1   (Aᵀ pulls it back to 2D input space)

AᵀA  is 2×2   (maps 2D input space to itself)
x̂    is 2×1   (lives in 2D input space)

AᵀAx̂ = Aᵀb
 2×2    2×1    2×1   ← dimensions all consistent ✓
```

**Aᵀ is a "dimension reducer" — it brings everything from 3D back to 2D where we can solve.**

---

## Intuitive Analogy — Shadow on the Floor

Imagine b is a point floating in the air (3D). The column space of A is the floor (2D plane).

```
         b ● (floating in air)
           │
           │ ← shadow ray (perpendicular)
           │
═══════════●══════════  ← floor (column space)
          Ax̂ (shadow of b on floor)
```

- You can't stand exactly at b (off the floor)
- Best you can do: stand at the shadow Ax̂
- The shadow ray (error e) is **perpendicular to the floor**
- Aᵀe = 0 is just the mathematical statement that "the ray is perpendicular to the floor"
- x̂ = (AᵀA)⁻¹Aᵀb tells you **the coordinates of the shadow**

---

## Why Not Just Use A⁻¹?

```
If A were square (n×n) and invertible:
    Ax = b  →  x = A⁻¹b   (direct solve)

But A is 3×2 — RECTANGULAR.
Rectangular matrices have NO inverse.

Why? Because:
    A  maps ℝ² → ℝ³   (2D to 3D)
    A⁻¹ would need to map ℝ³ → ℝ²  (3D to 2D)
    
    You can't perfectly "undo" a dimension increase.
    Information was added (went from 2D to 3D).
    You can't perfectly reverse that.
    
So instead we use Aᵀ to come back:
    Aᵀ maps ℝ³ → ℝ²   (3D back to 2D)
    AᵀA maps ℝ² → ℝ²  (2D to 2D — square! invertible!)
    
    x̂ = (AᵀA)⁻¹ Aᵀ b
          ↑         ↑
       inverts    brings b
       the 2D     from 3D
       system     to 2D
```

**(AᵀA)⁻¹Aᵀ** is called the **Moore-Penrose Pseudoinverse** — it's the closest thing to A⁻¹ when A is rectangular.

---

## Summary — Every Piece Justified

| Piece | Why It's There |
|---|---|
| **Aᵀ in Aᵀe=0** | Perpendicularity condition — e must be ⊥ to all columns of A |
| **AᵀA** | Makes the system square (2×2) so it can be inverted |
| **Aᵀb** | Brings b from 3D output space back to 2D input space |
| **(AᵀA)⁻¹** | Inverts the square system to isolate x̂ |
| **Whole formula** | Finds the 2D coordinates of the shadow of b on the column space |











# Complete Guide to Finding Matrix Inverse

## First: When Does an Inverse Exist?

Before any algorithm, always check:

```
Matrix A is invertible IF AND ONLY IF:
  • A is SQUARE (n×n)
  • det(A) ≠ 0
  • Rank(A) = n
  • No row/column is a linear combination of others

All four conditions are equivalent — if one holds, all hold.
```

---

## The Master Algorithm: Gauss-Jordan Elimination

This is the most general, reliable method. Everything else is a special case.

### Core Idea

$$[A | I] \xrightarrow{\text{row operations}} [I | A^{-1}]$$

> **If you can reduce A to identity on the left, the right side automatically becomes A⁻¹.**

### Why Does This Work?

Every row operation is a left-multiplication by an elementary matrix E:

```
E₁E₂E₃...A = I

Therefore:   E₁E₂E₃... = A⁻¹

When you apply the same operations to I:
E₁E₂E₃...I = A⁻¹  ✓
```

---

## Full Step-by-Step Algorithm

### Phase 1: Forward Elimination (make lower triangle zero)
### Phase 2: Backward Elimination (make upper triangle zero)  
### Phase 3: Scale (make diagonal all ones)

Let's do this completely for a 3×3 matrix.

---

## Complete Worked Example

$$A = \begin{bmatrix}2&1&1\\4&3&3\\8&7&9\end{bmatrix}$$

### Setup: Write Augmented Matrix [A|I]

$$\left[\begin{array}{ccc|ccc}2&1&1&1&0&0\\4&3&3&0&1&0\\8&7&9&0&0&1\end{array}\right]$$

---

### Phase 1: Forward Elimination

**Step 1:** Eliminate column 1 below pivot (row 1)

```
R2 → R2 - (4/2)R1 = R2 - 2R1
R3 → R3 - (8/2)R1 = R3 - 4R1
```

$$\left[\begin{array}{ccc|ccc}2&1&1&1&0&0\\0&1&1&-2&1&0\\0&3&5&-4&0&1\end{array}\right]$$

**Step 2:** Eliminate column 2 below pivot (row 2)

```
R3 → R3 - (3/1)R2 = R3 - 3R2
```

$$\left[\begin{array}{ccc|ccc}2&1&1&1&0&0\\0&1&1&-2&1&0\\0&0&2&2&-3&1\end{array}\right]$$

Forward elimination complete. Left side is upper triangular.

---

### Phase 2: Backward Elimination

**Step 3:** Eliminate column 3 above pivot (row 3)

```
R2 → R2 - (1/2)R3
R1 → R1 - (1/2)R3
```

$$\left[\begin{array}{ccc|ccc}2&1&0&0&3/2&-1/2\\0&1&0&-3&5/2&-1/2\\0&0&2&2&-3&1\end{array}\right]$$

**Step 4:** Eliminate column 2 above pivot (row 2)

```
R1 → R1 - (1)R2
```

$$\left[\begin{array}{ccc|ccc}2&0&0&3&-1&0\\0&1&0&-3&5/2&-1/2\\0&0&2&2&-3&1\end{array}\right]$$

---

### Phase 3: Scale to Get Identity

```
R1 → R1/2
R3 → R3/2
```

$$\left[\begin{array}{ccc|ccc}1&0&0&3/2&-1/2&0\\0&1&0&-3&5/2&-1/2\\0&0&1&1&-3/2&1/2\end{array}\right]$$

### Result:

$$A^{-1} = \begin{bmatrix}3/2&-1/2&0\\-3&5/2&-1/2\\1&-3/2&1/2\end{bmatrix}$$

### Verify: AA⁻¹ = I

```
Always verify by multiplying back.
If any entry is wrong, you'll catch it here.
```

---

## Algorithm 2: For 2×2 — Direct Formula

For a 2×2 matrix, there is a closed-form formula. Memorize this.

$$A = \begin{bmatrix}a&b\\c&d\end{bmatrix}$$

$$A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

### The Four Operations:

```
Step 1: Compute det = ad - bc
        If det = 0 → STOP, no inverse exists

Step 2: SWAP main diagonal      [a b]  →  [d b]
                                [c d]     [c a]

Step 3: NEGATE off-diagonal     [d  b]  →  [d  -b]
                                [c  a]     [-c  a]

Step 4: DIVIDE everything by det
```

### Example:

$$A = \begin{bmatrix}3&2\\1&4\end{bmatrix}$$

```
det = 3×4 - 2×1 = 10

Swap diagonal:    [4  2]
                  [1  3]

Negate off-diag:  [4  -2]
                  [-1   3]

Divide by 10:     [0.4   -0.2]
                  [-0.1   0.3]
```

$$A^{-1} = \begin{bmatrix}0.4&-0.2\\-0.1&0.3\end{bmatrix}$$

---

## Algorithm 3: Using Determinant + Cofactor Matrix

This is the theoretical/analytical method. Good for understanding, slow for large matrices.

$$A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)$$

where adj(A) = transpose of the cofactor matrix.

### Step-by-Step:

**Step 1: Compute det(A)**

For 3×3, expand along any row:

$$\det(A) = a_{11}(a_{22}a_{33}-a_{23}a_{32}) - a_{12}(a_{21}a_{33}-a_{23}a_{31}) + a_{13}(a_{21}a_{32}-a_{22}a_{31})$$

**Step 2: Compute Cofactor Matrix**

For each element aᵢⱼ:
- Delete row i and column j
- Compute determinant of remaining 2×2 matrix (= Minor Mᵢⱼ)
- Apply sign: Cᵢⱼ = (−1)^(i+j) × Mᵢⱼ

Sign pattern:
```
[+  -  +]
[-  +  -]
[+  -  +]
```

**Step 3: Transpose the Cofactor Matrix**

$$\text{adj}(A) = C^T$$

**Step 4: Divide by det**

$$A^{-1} = \frac{1}{\det(A)} \cdot C^T$$

---

## All Methods Compared

```
┌─────────────────┬──────────┬────────────┬─────────────────────┐
│ Method          │ Best For │ Complexity │ Notes               │
├─────────────────┼──────────┼────────────┼─────────────────────┤
│ Gauss-Jordan    │ Any size │   O(n³)    │ Most general        │
│ 2×2 Formula     │ 2×2 only │   O(1)     │ Memorize this       │
│ Cofactor/Adj    │ 3×3 max  │   O(n!)    │ Good for theory     │
│ LU Decomp       │ Large n  │   O(n³)    │ Best for computers  │
└─────────────────┴──────────┴────────────┴─────────────────────┘
```

---

## The Decision Framework

```
Given matrix A (n×n)
        │
        ▼
Is det(A) = 0?
   YES → NO INVERSE. Stop.
   NO  → Continue
        │
        ▼
What size is A?
        │
   ┌────┼────┐
  2×2  3×3  n×n
   │    │    │
   │    │    ▼
   │    │  Gauss-Jordan
   │    │  on [A|I]
   │    │
   │    ▼
   │  Cofactor method
   │  OR Gauss-Jordan
   │
   ▼
Direct formula:
(1/det)×[d -b; -c a]
```

---

## Common Mistakes to Avoid

```
MISTAKE 1: Forgetting to check det = 0 first
→ You'll get division by zero or a wrong answer

MISTAKE 2: Wrong sign pattern in cofactors
→ Remember [+ - +; - + -; + - +]

MISTAKE 3: Forgetting to TRANSPOSE the cofactor matrix
→ adj(A) = Cᵀ, not C

MISTAKE 4: Arithmetic errors in row operations
→ Always verify: compute AA⁻¹ and check = I

MISTAKE 5: Applying row operations to only one side
→ Whatever you do to A, do EXACTLY the same to I
```

---

## Quick Verification Checklist

After finding A⁻¹, always verify:

```
✓ AA⁻¹ = I  (right inverse)
✓ A⁻¹A = I  (left inverse)
✓ det(A⁻¹) = 1/det(A)
✓ (A⁻¹)⁻¹ = A
```

If any of these fail → you made an arithmetic error somewhere.


