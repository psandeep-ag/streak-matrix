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
