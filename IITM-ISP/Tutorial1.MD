Great — this is exactly the kind of assignment where *first-principles thinking* makes everything much easier (and also prepares you strongly for exams).

I’ll act like a **teaching assistant sitting next to you**, and we’ll build a **systematic problem-solving framework** that you can apply to *all questions (Q1–Q12)*.

---

# 🔴 BIG PICTURE: What this tutorial is really testing

Before solving anything, understand this:

This assignment is about **3 fundamental pillars of Image Processing / Computer Vision**:

### 1. 📷 Image Formation (Camera Model)

* How 3D → 2D projection works
* Camera matrix (K), focal length, pixels

### 2. 🔁 Geometric Transformations

* Affine, Homography, Rotation
* Warping shapes (circle → ellipse etc.)

### 3. 🌫️ Blur, Focus, and Depth

* Motion blur vs defocus blur
* Shape-from-focus
* Camera optics

---

# 🧠 MASTER STRATEGY (Use for EVERY question)

Whenever you see a problem:

### Step 1: Identify the domain

Ask:

* Is this **projection?**
* **Transformation?**
* **Blur / optics?**
* **Probability / RANSAC?**

---

### Step 2: Write the core equation (FIRST PRINCIPLE)

Every question reduces to 1–2 equations:

* Projection → ( x = \frac{fX}{Z} )
* Affine → ( x' = Ax + t )
* Homography → ( x' = Hx )
* RANSAC → probability formula
* Blur → physical intuition

---

### Step 3: Map given values → variables

Convert words → symbols

---

### Step 4: Solve step-by-step (no shortcuts)

---

### Step 5: Interpret physically

This is what examiners LOVE.

---

Now let’s go question by question.

---

# ✅ Q1: Camera Calibration Matrix (K)

## 🔹 First principle

Camera matrix:

[
K =
\begin{bmatrix}
f_x & 0 & c_x \
0 & f_y & c_y \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔹 Step-by-step

### Step 1: Convert focal length into pixels

Given:

* ( f = 5 ) mm
* Pixel size = (0.02) mm

So:

[
f_x = f_y = \frac{5}{0.02} = 250
]

---

### Step 2: Principal point

[
(c_x, c_y) = (500, 500)
]

---

### Step 3: Final matrix

[
K =
\begin{bmatrix}
250 & 0 & 500 \
0 & 250 & 500 \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔥 Exam insight

* If pixel size differs → (f_x \neq f_y)
* If skew present → non-zero off-diagonal

---

# ✅ Q2: Find focal length

## 🔹 First principle (Perspective projection)

[
x = \frac{fX}{Z}, \quad y = \frac{fY}{Z}
]

---

## 🔹 Given

3D point:
[
(400, 600, 1200)
]

Image:
[
(24, 36)
]

---

## 🔹 Solve

From x:

[
24 = \frac{f \cdot 400}{1200}
\Rightarrow f = 72 \text{ mm}
]

---

## 🔥 Key intuition

* Larger depth → smaller projection
* This is pure pinhole geometry

---

# ✅ Q3: Warping a circle

## 🔹 First principle

Affine transform:

[
x' = Ax + t
]

A circle under affine transform → **ellipse**

---

## 🔹 Given

Circle:
[
x^2 + y^2 = 4
]

Matrix includes:

* scaling
* shear (0.2)
* translation

---

## 🔹 Result

👉 Shape = **Ellipse**

---

## 🔥 Exam insight

* Affine preserves:

  * parallel lines
* Does NOT preserve:

  * angles
  * circles

---

# ✅ Q4: Homography derivation

## 🔹 First principle

[
H = R + \frac{t n^T}{d}
]

---

## 🔹 Strategy

1. Apply **translation first**
2. Then apply **rotation**
3. Multiply matrices

---

## 🔥 Key insight

Order matters:

* Translation → Rotation ≠ Rotation → Translation

---

# ✅ Q5: True/False

### 1. ❌ False

Rotation is **NOT commutative**

---

### 2. ❌ False

Homography can make parallel lines meet (vanishing point)

---

### 3. ✅ True

All transforms → linear in homogeneous coordinates

---

# ✅ Q6: RANSAC iterations

## 🔹 Formula

[
N = \frac{\log(1 - p)}{\log(1 - (1 - \epsilon)^s)}
]

Where:

* ( p = 0.99 )
* outliers = 40% → inliers = 0.6
* ( s = 4 )

---

## 🔹 Solve

[
N \approx 35
]

---

## 🔥 Insight

* More outliers → more iterations

---

# ✅ Q7: Motion vs Defocus blur

## 🔹 First principle

* Motion blur → directional
* Defocus → uniform circular blur

---

## 🔹 Answer

* (I1) → Motion blur
* (I2) → Defocus blur

Direction:
👉 Along rows (horizontal)

---

# ✅ Q8: SFF step size

✔️ Answer: **(a) Depth of Field / 2**

---

# ✅ Q9: Image stitching

False statements:

👉 (c) Pure translation does NOT work for 3D scenes
👉 (d) 6D motion not allowed for planar stitching

---

# ✅ Q10: Focus

Closest to working distance (110 mm) is:

👉 125 mm → most focused

---

# ✅ Q11: Globe blur

✔️ Correct:

* Space-variant blur
* Depth variation across globe

---

# ✅ Q12: DFT diagonalization

## 🔹 First principle

DFT diagonalizes **circulant matrices**

Steps:

1. Compute DFT matrix
2. Multiply:
   [
   F A F^{-1}
   ]

---

## 🔥 Insight

* Eigenvectors = Fourier basis

---

# 📚 HOW TO PREPARE FOR MID-TERM (VERY IMPORTANT)

### Easy Questions

* Direct formulas (Q1, Q2)

### Medium

* Transformations (Q3, Q4, Q5)

### Tough

* RANSAC (Q6)
* Conceptual blur (Q7, Q11)
* DFT (Q12)

---

# 🧠 FINAL ADVICE (CRITICAL)

When stuck:

1. Draw diagram ✏️
2. Write base equation
3. Plug values slowly
4. Interpret physically

---

If you want next level understanding, I can:

* Solve **Q3, Q4, Q12 in full derivation (step-by-step math)**
* Or convert this into **exam-ready notes + cheat sheet**

Just tell me 👍
---

Perfect — now we go into **deep, exam-grade derivations** for Q3, Q4, Q12. I’ll walk exactly like a TA at the board, building everything from first principles, no jumps.

---

# 🔴 Q3: Warping a Circle using an Affine Transform

## 🧠 Step 0: What is happening?

We are given:

* A **circle** in ((x, y))
* An **affine transform** (A)
* Asked: *What is the new equation and shape?*

---

## 🔹 Step 1: Write everything in homogeneous coordinates

Circle:
[
x^2 + y^2 = 4
]

Affine transform:
[
A =
\begin{bmatrix}
1 & 0.2 & 1 \
0 & 1 & 1 \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔹 Step 2: Understand forward mapping

[
\begin{bmatrix}
x' \
y' \
1
\end{bmatrix}
=============

A
\begin{bmatrix}
x \
y \
1
\end{bmatrix}
]

So:

[
x' = x + 0.2y + 1
]
[
y' = y + 1
]

---

## 🔹 Step 3: IMPORTANT IDEA (Core Trick)

We **do NOT substitute forward**.

👉 We must express **old coordinates in terms of new**
(i.e., inverse transform)

---

## 🔹 Step 4: Solve inverse mapping

From:
[
y' = y + 1 \Rightarrow y = y' - 1
]

Substitute into (x'):

[
x' = x + 0.2(y' - 1) + 1
]

[
x' = x + 0.2y' - 0.2 + 1
]

[
x' = x + 0.2y' + 0.8
]

[
x = x' - 0.2y' - 0.8
]

---

## 🔹 Step 5: Substitute into circle equation

[
(x' - 0.2y' - 0.8)^2 + (y' - 1)^2 = 4
]

---

## 🔹 Step 6: Expand fully (exam important)

First term:
[
(x' - 0.2y' - 0.8)^2
]

[
= x'^2 + 0.04y'^2 + 0.64 - 0.4x'y' - 1.6x' + 0.32y'
]

Second term:
[
(y' - 1)^2 = y'^2 - 2y' + 1
]

---

## 🔹 Step 7: Combine all terms

[
x'^2 + (0.04 + 1)y'^2 - 0.4x'y' + (-1.6)x' + (0.32 - 2)y' + (0.64 + 1) = 4
]

[
x'^2 + 1.04y'^2 - 0.4x'y' - 1.6x' - 1.68y' + 1.64 = 4
]

---

## 🔹 Step 8: Final equation

[
x'^2 + 1.04y'^2 - 0.4x'y' - 1.6x' - 1.68y' - 2.36 = 0
]

---

## 🎯 Final Answer

### Shape:

👉 **Ellipse**

### Why?

* Quadratic with (x'^2, y'^2, xy)
* Affine transform → ellipse

---

## 🔥 Exam Insight

* Circle → ellipse under affine
* Cross term (x'y') indicates **rotation/shear**

---

# 🔴 Q4: Deriving Homography (Translation → Rotation)

---

## 🧠 Step 0: What is happening?

We are deriving:

[
H =
\begin{bmatrix}
c & -s & cp - sq \
s & c & sp + cq \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔹 Step 1: Camera model (given)

* (K = I)
* Planar scene
* Homography:

[
H = R + \frac{t n^T}{d}
]

---

## 🔹 Step 2: Assume plane

Plane:
[
Z = d
]

Normal:
[
n = \begin{bmatrix}0 \ 0 \ 1\end{bmatrix}
]

---

## 🔹 Step 3: Translation first

Let translation:

[
t = \begin{bmatrix}p \ q \ 0\end{bmatrix}
]

---

## 🔹 Step 4: Rotation matrix (Z-axis)

[
R =
\begin{bmatrix}
c & -s & 0 \
s & c & 0 \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔹 Step 5: Compute (tn^T)

[
n^T = [0 ; 0 ; 1]
]

[
t n^T =
\begin{bmatrix}
p \
q \
0
\end{bmatrix}
[0 ; 0 ; 1]
===========

\begin{bmatrix}
0 & 0 & p \
0 & 0 & q \
0 & 0 & 0
\end{bmatrix}
]

---

## 🔹 Step 6: Divide by (d = 1)

Same matrix.

---

## 🔹 Step 7: Add with rotation

[
H = R + tn^T
]

[
H =
\begin{bmatrix}
c & -s & p \
s & c & q \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔹 Step 8: Apply rotation AFTER translation

Now rotation affects translation:

[
\begin{bmatrix}
p' \
q'
\end{bmatrix}
=============

\begin{bmatrix}
c & -s \
s & c
\end{bmatrix}
\begin{bmatrix}
p \
q
\end{bmatrix}
]

[
p' = cp - sq
]
[
q' = sp + cq
]

---

## 🎯 Final Homography

[
H =
\begin{bmatrix}
c & -s & cp - sq \
s & c & sp + cq \
0 & 0 & 1
\end{bmatrix}
]

---

## 🔥 Key Insight

👉 Order matters:

* Translate → Rotate ⇒ rotated translation

---

# 🔴 Q12: Diagonalization using DFT

---

## 🧠 Step 0: Concept

DFT diagonalizes **circulant matrices**

Given:

[
A =
\begin{bmatrix}
3 & -1 & 2 \
2 & 3 & -1 \
-1 & 2 & 3
\end{bmatrix}
]

---

## 🔹 Step 1: Check structure

Each row is a **cyclic shift** → circulant

---

## 🔹 Step 2: First row defines matrix

[
[3, -1, 2]
]

---

## 🔹 Step 3: Eigenvalues using DFT

For (N=3):

[
\omega = e^{-j2\pi/3}
]

Eigenvalues:

[
\lambda_k = a_0 + a_1 \omega^k + a_2 \omega^{2k}
]

---

## 🔹 Step 4: Compute eigenvalues

### (k=0)

[
\lambda_0 = 3 - 1 + 2 = 4
]

---

### (k=1)

[
\omega = -\frac{1}{2} - j\frac{\sqrt{3}}{2}
]

[
\lambda_1 = 3 - \omega + 2\omega^2
]

Compute:

[
= 3 + \frac{1}{2} + j\frac{\sqrt{3}}{2} + 2\left(-\frac{1}{2} + j\frac{\sqrt{3}}{2}\right)
]

[
= 3 + 0.5 -1 + j\left(\frac{\sqrt{3}}{2} + \sqrt{3}\right)
]

[
= 2.5 + j\frac{3\sqrt{3}}{2}
]

---

### (k=2)

[
\lambda_2 = \text{conjugate}
]

[
= 2.5 - j\frac{3\sqrt{3}}{2}
]

---

## 🔹 Step 5: Final diagonal matrix

[
D =
\begin{bmatrix}
4 & 0 & 0 \
0 & 2.5 + j\frac{3\sqrt{3}}{2} & 0 \
0 & 0 & 2.5 - j\frac{3\sqrt{3}}{2}
\end{bmatrix}
]

---

## 🔹 Step 6: Final relation

[
A = F^{-1} D F
]

---

## 🔥 Key Insight

* DFT basis = eigenvectors
* Circulant matrices → diagonal in Fourier domain

---

# 🧠 FINAL TAKEAWAYS (VERY IMPORTANT)

### Q3

* Always use **inverse mapping**
* Circle → ellipse

### Q4

* Homography = rotation + translated plane effect
* Order matters

### Q12

* Recognize circulant matrix instantly
* Use DFT shortcut (don’t brute force eigenvalues)

---

If you want next level mastery, I can:

* Give **exam-type tricky variations** of these 3 questions
* Or convert these into a **1-page revision sheet + memory tricks**

Just tell me 👍
