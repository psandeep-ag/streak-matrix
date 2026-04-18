"Q 3. Assume that the two-dimensional Fourier spectrum of an image with size 640 × 480 (along x and y directions, respectively), and a spatial resolution of 72 dpi shows a dominant peak at position ±(100,100). Determine the orientation and effective frequency (in cycles per cm) of the corresponding image pattern."


# 2D Fourier Spectrum: Orientation & Frequency Analysis

## 1. Core Concept

When a 2D DFT of an image shows a **dominant peak at ±(u₀, v₀)**, it means the image contains a **dominant sinusoidal grating** (stripe pattern) with:
- A specific **orientation** (angle of stripes)
- A specific **spatial frequency** (how many cycles per unit length)

The challenge here is converting from **pixel-space frequency coordinates** → **physical frequency in cycles/cm**, using the image's resolution (dpi).

---

## 2. First Principles

### The 2D DFT Frequency Grid

For an image of size **M × N pixels**, the DFT output F(u,v) has indices:
```
u = 0, 1, 2, ..., M-1     (frequency index along x)
v = 0, 1, 2, ..., N-1     (frequency index along y)
```

A peak at index **(u₀, v₀)** corresponds to a sinusoid with:

$$f_x = \frac{u_0}{M} \text{ cycles/pixel}, \quad f_y = \frac{v_0}{N} \text{ cycles/pixel}$$

### Converting pixels → physical units

Given resolution **R dpi** (dots per inch):

$$\text{pixels per cm} = \frac{R}{2.54}$$

So physical frequency:

$$F_x = f_x \times \frac{R}{2.54} \text{ cycles/cm}, \quad F_y = f_y \times \frac{R}{2.54} \text{ cycles/cm}$$

### Orientation and Effective Frequency

$$\theta = \arctan\!\left(\frac{v_0/N}{u_0/M}\right) \quad \text{(angle of frequency vector from x-axis)}$$

$$F_{\text{eff}} = \sqrt{F_x^2 + F_y^2} \quad \text{cycles/cm}$$

> ⚠️ **Stripe orientation is PERPENDICULAR to the frequency vector direction**

---

## 3. How to Think Through This

```
Peak position (u₀,v₀) in pixel indices
        ↓
Convert to cycles/pixel using image dimensions
        ↓
Convert to cycles/cm using dpi → cm conversion
        ↓
Compute angle of frequency VECTOR → stripes are perpendicular
        ↓
Compute magnitude = effective frequency in cycles/cm
```

**Mental model:** The peak location is a **vector arrow** in frequency space. The stripes in the image run **across** that arrow (perpendicular to it).

---

## 4. Methodology — Full Solution

### Given:
| Parameter | Value |
|---|---|
| Image size | 640 × 480 pixels (M=640 along x, N=480 along y) |
| Resolution | 72 dpi |
| Peak position | ±(100, 100) → u₀=100, v₀=100 |

---

### Step 1: Cycles per pixel

$$f_x = \frac{u_0}{M} = \frac{100}{640} = 0.15625 \text{ cycles/pixel}$$

$$f_y = \frac{v_0}{N} = \frac{100}{480} = 0.20833 \text{ cycles/pixel}$$

---

### Step 2: Convert dpi → pixels per cm

$$\text{pixels/cm} = \frac{72}{2.54} = 28.346 \text{ px/cm}$$

---

### Step 3: Physical frequencies (cycles/cm)

$$F_x = f_x \times 28.346 = 0.15625 \times 28.346 = \boxed{4.429 \text{ cycles/cm}}$$

$$F_y = f_y \times 28.346 = 0.20833 \times 28.346 = \boxed{5.906 \text{ cycles/cm}}$$

---

### Step 4: Effective frequency (magnitude)

$$F_{\text{eff}} = \sqrt{F_x^2 + F_y^2} = \sqrt{(4.429)^2 + (5.906)^2}$$

$$= \sqrt{19.616 + 34.881} = \sqrt{54.497} = \boxed{7.382 \text{ cycles/cm}}$$

---

### Step 5: Orientation of frequency vector

$$\theta_{\text{vec}} = \arctan\!\left(\frac{F_y}{F_x}\right) = \arctan\!\left(\frac{5.906}{4.429}\right) = \arctan(1.3333) = \boxed{53.13°}$$

---

### Step 6: Stripe orientation (perpendicular to frequency vector)

$$\theta_{\text{stripe}} = \theta_{\text{vec}} - 90° = 53.13° - 90° = \boxed{-36.87° \approx -37°}$$

(i.e., stripes run at **~37° below horizontal**, or equivalently **~143° from horizontal**)

---

### ✅ Final Answer

| Quantity | Value |
|---|---|
| Physical frequency along x | 4.43 cycles/cm |
| Physical frequency along y | 5.91 cycles/cm |
| **Effective frequency** | **7.38 cycles/cm** |
| Frequency vector angle | 53.13° from x-axis |
| **Stripe orientation** | **−36.87° (≈ 143°) from x-axis** |

---

## 5. Key Ideas

1. **Index ≠ Frequency** — Raw DFT index must be normalized by image dimension
2. **dpi bridges pixels and physical space** — Always divide dpi by 2.54 for cm
3. **Non-square images** — u₀/M ≠ v₀/N even when u₀=v₀, because M≠N
4. **Perpendicularity** — Stripes always ⊥ to the frequency vector
5. **Effective frequency = vector magnitude** — Pythagorean theorem in frequency space
6. **The ± symmetry** — Conjugate pair; both represent the same real sinusoid

---

## 6. Framework

```
┌─────────────────────────────────────────────┐
│           INPUT: Peak at (u₀, v₀)           │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────▼──────────┐
        │  Normalize by dims  │
        │  fx = u₀/M          │
        │  fy = v₀/N          │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │  Scale by px/cm     │
        │  px/cm = dpi/2.54   │
        │  Fx = fx × px/cm    │
        │  Fy = fy × px/cm    │
        └──────────┬──────────┘
                   │
          ┌────────┴────────┐
          │                 │
   ┌──────▼──────┐   ┌──────▼──────┐
   │  MAGNITUDE  │   │    ANGLE    │
   │√(Fx²+ Fy²) │   │arctan(Fy/Fx)│
   │= Effective  │   │= freq vector│
   │  frequency  │   │  direction  │
   └─────────────┘   └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │  Subtract   │
                     │    90°      │
                     │ = Stripe    │
                     │ orientation │
                     └─────────────┘
```

---

## 7. Why This Problem Is Important

- **Calibration** — Ensures frequency measurements are in physical units, not arbitrary pixels
- **Reproducibility** — Same pattern scanned at different resolutions must give same physical frequency
- **Real-world design** — Printers, displays, medical scanners all operate in physical units
- **Aliasing detection** — Knowing physical frequency tells you if sampling was adequate
- **Cross-device comparison** — Different cameras/scanners have different dpi; normalization is essential

---

## 8. Applications

| Domain | Application |
|---|---|
| **Printing** | Detecting halftone screen frequency (LPI = lines per inch) |
| **Textile inspection** | Measuring thread count and weave orientation automatically |
| **Medical imaging** | MRI gradient calibration in physical space |
| **Remote sensing** | Measuring periodic terrain features (row crops, urban grids) |
| **Microscopy** | Measuring lattice spacing in crystallographic images |
| **Display tech** | Detecting Moiré patterns between screen pixel grids |

---

## 9. Other Examples

**Example A:** 512×512 image, 96 dpi, peak at ±(64, 0)
```
fx = 64/512 = 0.125 cyc/px
px/cm = 96/2.54 = 37.795
Fx = 4.724 cyc/cm, Fy = 0
→ Vertical stripes at 4.724 cycles/cm
```

**Example B:** 1024×768 image, 300 dpi, peak at ±(50, 50)
```
fx = 50/1024 = 0.04883, fy = 50/768 = 0.06510
px/cm = 300/2.54 = 118.11
Fx = 5.769, Fy = 7.690 cyc/cm
Feff = √(5.769²+7.690²) = 9.612 cyc/cm
θ = arctan(7.690/5.769) = 53.1°, stripes at −36.9°
```

---

## 10. Toughest Question Possible

> **An image of size 1024 × 768 pixels is captured at 150 dpi. Its 2D DFT magnitude spectrum (after shifting DC to center) shows THREE dominant peaks at:**
>
> - **Peak 1: ±(80, 60)**
> - **Peak 2: ±(−40, 120)**
> - **Peak 3: ±(200, 0)**
>
> **(i)** Compute the physical frequency (cycles/cm) and stripe orientation for each peak.
>
> **(ii)** Two of these peaks arise from a halftone printing screen applied at two different angles. The third is a Moiré artifact. Given that Moiré frequency = |F₁ − F₂| (vector subtraction), identify which peak is the Moiré and verify mathematically.
>
> **(iii)** If the image is resampled to 300 dpi (upsampled by 2×), how do the DFT peak positions (u₀, v₀) change? Do the physical frequencies change? Explain the paradox.
>
> **(iv)** Design a frequency-domain filter to suppress only the Moiré component without affecting the other two. Specify its shape, center, and bandwidth in cycles/cm.
>
> **(v)** After filtering, the inverse DFT image is printed at 600 dpi. At what pixel coordinates does the dominant stripe pattern complete exactly one full cycle?

This demands mastery of: physical unit conversion, vector arithmetic in frequency space, Moiré theory, resampling invariance, filter design, and spatial period calculation — simultaneously.



why are we Normalizing by image dimensions ? 

explain the complete solution intuitively



# Why Normalize by Image Dimensions? — Complete Intuitive Explanation

## The Core Problem: What Does "Position 100" Mean?

When someone says **"peak at u₀ = 100"**, your first question should be:

> *"100 out of what?"*

Imagine two scenarios:

```
Image A:  200 pixels wide,  peak at u₀ = 100  →  halfway across frequency space
Image B: 1000 pixels wide,  peak at u₀ = 100  →  only 1/10th across frequency space
```

**Same number. Completely different meaning.** This is exactly why we normalize.

---

## The Fundamental Intuition

### Think of DFT as "How many complete waves fit across the image?"

The DFT index **u₀** literally means:

> **"There are u₀ complete sinusoidal cycles fitting across the entire image width"**

```
Image width = 640 pixels

Peak at u₀ = 100 means:
┌────────────────────────────────────────────────┐
│╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲...100 complete waves...  │
└────────────────────────────────────────────────┘
←──────────────── 640 pixels ───────────────────→
```

So the frequency in cycles per pixel =

$$f_x = \frac{\text{number of cycles}}{\text{total pixels}} = \frac{100}{640}$$

**This is normalization.** You're asking: *"per pixel, how many cycles occur?"*

---

## Why M and N Are Different — The Non-Square Problem

This is where it gets critical for our problem.

```
Our image: 640 × 480 pixels
Peak at: (u₀, v₀) = (100, 100)
```

Even though **u₀ = v₀ = 100** (same number!), they mean different things:

```
X-direction:  100 waves across 640 pixels  →  100/640 = 0.1563 cycles/pixel
Y-direction:  100 waves across 480 pixels  →  100/480 = 0.2083 cycles/pixel
```

**The image is shorter in Y, so the same index "100" represents a HIGHER frequency in Y.**

Visually:
```
X: ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲  ← 640px, 100 waves, less dense
Y: ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲  ← 480px, 100 waves, MORE dense
```

---

## The Bridge: Pixels → Physical Units (the dpi step)

Now you know cycles **per pixel**. But the question asks for cycles **per cm**.

### What is 72 dpi?

> **72 dots (pixels) occupy 1 inch of physical space**

```
1 inch = 2.54 cm
72 pixels = 1 inch = 2.54 cm

Therefore: 1 cm = 72/2.54 = 28.35 pixels
```

### The conversion is just unit cancellation:

$$F_x = \underbrace{\frac{100}{640}}_{\text{cycles/pixel}} \times \underbrace{\frac{72}{2.54}}_{\text{pixels/cm}} = \frac{100 \times 72}{640 \times 2.54}$$

```
cycles     pixels       cycles
──────  ×  ──────  =   ──────
pixel       cm           cm
```

The **pixels cancel out**, leaving you with **cycles per cm** — a real, physical measurement.

---

## Complete Intuitive Walkthrough of the Solution

### Stage 1: The Raw Peak — What (100,100) tells us

```
DFT space looks like this (640×480 grid):

v=0  ┌─────────────────────────────┐
     │                             │
     │         • (100,100)         │  ← our peak
     │                             │
     │           [DC at 0,0]       │
     │                             │
     │         • (−100,−100)       │  ← mirror peak (always exists)
     │                             │
v=480└─────────────────────────────┘
    u=0                          u=640
```

The peak says: *"There's a dominant wave pattern — 100 oscillations horizontally, 100 oscillations vertically"*

---

### Stage 2: Normalize — Convert to cycles/pixel

```
fx = 100/640 = 0.15625 cyc/px   (one cycle every 6.4 pixels in x)
fy = 100/480 = 0.20833 cyc/px   (one cycle every 4.8 pixels in y)
```

Intuition check:
```
X stripe period = 1/fx = 6.4 pixels between repeats  (wider spacing)
Y stripe period = 1/fy = 4.8 pixels between repeats  (tighter spacing)
```

---

### Stage 3: Scale to physical — Convert to cycles/cm

```
72 dpi → 28.35 pixels per cm

Fx = 0.15625 × 28.35 = 4.43 cycles/cm
Fy = 0.20833 × 28.35 = 5.91 cycles/cm
```

Physical intuition:
```
In 1 cm of the printed image:
  → Horizontally: 4.43 complete stripe oscillations
  → Vertically:   5.91 complete stripe oscillations
```

---

### Stage 4: The Frequency Vector — Visualizing in 2D

Think of (Fx, Fy) as an **arrow** pointing in frequency space:

```
          Fy ↑
          6  │         ★ (4.43, 5.91)
             │        /|
          5  │       / |
             │      /  | Fy = 5.91
          4  │     /   |
             │    /    |
          3  │   /     |
             │  / θ=53°|
          2  │ /       |
             │/________|
          1  └──────────────→ Fx
             0  1  2  3  4  5  6

The arrow length = Feff = √(4.43² + 5.91²) = 7.38 cyc/cm
The arrow angle  = arctan(5.91/4.43) = 53.13° from horizontal
```

---

### Stage 5: The Perpendicularity Rule — Finding Stripe Orientation

This is the most misunderstood step. Here's the intuition:

> **The frequency vector points in the direction the wave "travels". The stripes are the wave fronts — always perpendicular to travel direction.**

Think of ocean waves:
```
Wave travels →→→→→→→     Stripe/crest orientation:
                              │   │   │   │   │
→→→→→→→→→→→→→→→→             │   │   │   │   │
                              │   │   │   │   │
→→→→→→→→→→→→→→→→             │   │   │   │   │

Direction of travel: horizontal (0°)
Crest/stripe orientation: VERTICAL (90°) ← perpendicular!
```

In our problem:
```
Frequency vector points at:  53.13° from horizontal
Stripe orientation:          53.13° − 90° = −36.87°

So stripes are tilted at ~37° BELOW horizontal
```

Visually the image looks like:
```
╲╲╲╲╲╲╲╲╲╲╲╲╲
 ╲╲╲╲╲╲╲╲╲╲╲╲╲   ← stripes tilted ~37° below horizontal
  ╲╲╲╲╲╲╲╲╲╲╲╲╲
   ╲╲╲╲╲╲╲╲╲╲╲╲╲
```

---

## The Complete Picture in One Diagram

```
GIVEN: 640×480 image, 72dpi, peak at ±(100,100)
         │
         ▼
┌─────────────────────────────────────┐
│  STEP 1: Normalize by dimensions    │
│  fx = 100/640 = 0.1563 cyc/px      │
│  fy = 100/480 = 0.2083 cyc/px      │
│                                     │
│  WHY? Because index alone is        │
│  meaningless without knowing        │
│  the total image size               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  STEP 2: Convert px → cm           │
│  72dpi ÷ 2.54 = 28.35 px/cm       │
│  Fx = 0.1563 × 28.35 = 4.43 c/cm  │
│  Fy = 0.2083 × 28.35 = 5.91 c/cm  │
│                                     │
│  WHY? Physical frequency doesn't   │
│  depend on how many pixels you use  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  STEP 3: Magnitude = Feff          │
│  √(4.43²+5.91²) = 7.38 cyc/cm     │
│                                     │
│  WHY? The wave travels diagonally  │
│  — its true speed is the vector    │
│  magnitude, not just one component  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  STEP 4: Orientation               │
│  Vector angle = arctan(5.91/4.43)  │
│               = 53.13°             │
│  Stripe angle = 53.13° − 90°       │
│               = −36.87°            │
│                                     │
│  WHY? Stripes ⊥ wave travel dir.   │
└─────────────────────────────────────┘

ANSWER: 7.38 cycles/cm at −36.87° stripe orientation
```

---

## One-Line Summary of Each Key Step

| Step | What you do | Why |
|---|---|---|
| **÷ M, ÷ N** | Normalize index by image size | Index "100" is relative, not absolute |
| **× dpi/2.54** | Convert pixels to cm | Need physical, not pixel, frequency |
| **√(Fx²+Fy²)** | Compute vector magnitude | Diagonal wave has one true frequency |
| **arctan(Fy/Fx)** | Find vector angle | Locates direction of wave propagation |
| **− 90°** | Rotate to get stripe angle | Stripes always ⊥ to propagation direction |



why is the image size M x N treated as DFT space ? 

why is u=0 v=0 not at same point and why is v increasing in downward direction unlike cartesian coordinates ? 

DFT space looks like this (640×480 grid):
v=0  ┌─────────────────────────────┐
     │                             │
     │         • (100,100)         │  ← our peak
     │                             │
     │           [DC at 0,0]       │
     │                             │
     │         • (−100,−100)       │  ← mirror peak (always exists)
     │                             │
v=480└─────────────────────────────┘
    u=0                          u=640




# Why DFT Space = Image Size, and Why the Axes Behave Differently

## The Most Important Realization First

> **The DFT does NOT produce a "frequency space" that is separate from the image grid. It produces exactly M×N output values for M×N input values. One-to-one.**

This shocks most people. Let me build this from scratch.

---

## Part 1: Why DFT Space is M×N

### Start with 1D — the simplest case

Say you have **8 pixel values** (a 1D signal):

```
Input:  [x₀, x₁, x₂, x₃, x₄, x₅, x₆, x₇]   ← 8 values
Output: [F₀, F₁, F₂, F₃, F₄, F₅, F₆, F₇]   ← exactly 8 values
```

The DFT formula is:

$$F_u = \sum_{n=0}^{N-1} x_n \cdot e^{-j2\pi un/N}$$

For each output index **u = 0, 1, 2, ..., N−1**, you get one complex number.

**N inputs → N outputs. Always.**

### The physical meaning of each output index

```
F₀ → asks: "how much of a wave with 0 cycles fits in 8 pixels?"   = DC (flat)
F₁ → asks: "how much of a wave with 1 cycle  fits in 8 pixels?"
F₂ → asks: "how much of a wave with 2 cycles fits in 8 pixels?"
F₃ → asks: "how much of a wave with 3 cycles fits in 8 pixels?"
...
F₇ → asks: "how much of a wave with 7 cycles fits in 8 pixels?"
```

**The index u literally = number of complete cycles across the entire signal.**

So the DFT grid is not a separate abstract space — it's just **a reorganization of the same N slots**, each slot now representing one frequency bin.

### Extend to 2D — images

Image is M×N pixels:
```
Input:  M×N pixel values   f(x,y)
Output: M×N complex values F(u,v)
```

$$F(u,v) = \sum_{x=0}^{M-1}\sum_{y=0}^{N-1} f(x,y)\cdot e^{-j2\pi(ux/M + vy/N)}$$

- **u** runs from 0 to M−1 → exactly M values → same as image width
- **v** runs from 0 to N−1 → exactly N values → same as image height

```
Image pixel grid:          DFT output grid:
┌─────────────────┐        ┌─────────────────┐
│ f(0,0) f(1,0).. │        │ F(0,0) F(1,0).. │
│ f(0,1) f(1,1).. │  DFT→  │ F(0,1) F(1,1).. │
│ ...             │        │ ...             │
│ f(M-1,N-1)      │        │ F(M-1,N-1)      │
└─────────────────┘        └─────────────────┘
   M×N pixels                 M×N frequencies
```

**They are the same size by mathematical construction — not by coincidence.**

---

## Part 2: Why u=0,v=0 is at Top-Left, Not Center

### The raw DFT puts DC at the corner

The formula gives u=0, v=0 at **array index [0,0]** — the top-left corner.

Why? Because the formula starts counting from 0:

```
u = 0, 1, 2, ..., M−1
v = 0, 1, 2, ..., N−1
```

The raw DFT output looks like:

```
(0,0)          (M/2,0)
  ┌──────────┬──────────┐
  │          │          │
  │  Low     │  High    │
  │  freq    │  freq    │
  │  (left)  │ (right)  │
  ├──────────┼──────────┤
  │          │          │
  │  High    │  High    │
  │  freq    │  freq    │
  │ (bottom) │          │
  └──────────┴──────────┘
(0,N/2)              (M-1,N-1)
```

DC (zero frequency) sits at the **top-left corner**. This is mathematically correct but visually ugly.

### The fftshift operation moves DC to center

Most software (MATLAB, Python, NumPy) applies **fftshift** which rearranges the quadrants:

```
BEFORE fftshift:              AFTER fftshift:
┌──────────┬──────────┐       ┌──────────┬──────────┐
│  Q1 (DC) │    Q2   │       │    Q3    │    Q4   │
│  corner  │         │  →→→  │          │         │
├──────────┼──────────┤       ├──────────┼──────────┤
│    Q3    │    Q4   │       │  Q1 (DC) │    Q2   │
│          │         │       │  CENTER  │         │
└──────────┴──────────┘       └──────────┴──────────┘
```

After fftshift, DC is at the center, and the spectrum looks like:

```
u = −M/2, ..., −1, 0, +1, ..., +M/2
v = −N/2, ..., −1, 0, +1, ..., +N/2
```

**This is why in many textbook diagrams, the origin appears at center.**

### The diagram I drew earlier was WRONG/MIXED

My earlier diagram was inconsistent — it mixed raw DFT indexing with shifted indexing. Here's the correct picture:

```
RAW DFT (no shift):              SHIFTED DFT (fftshift):

v=0  ┌────────────────┐     v=−240┌────────────────┐
     │ DC●            │           │                │
     │                │           │   ●(−100,−100) │
     │                │           │                │
     │                │           │         ●(0,0) │←DC at CENTER
     │                │           │                │
     │                │           │  ●(+100,+100)  │
v=480└────────────────┘     v=+240└────────────────┘
    u=0             u=640        u=−320           u=+320
```

**The peak at ±(100,100) only makes sense in the SHIFTED version**, where the origin is at center and coordinates run negative to positive.

---

## Part 3: Why v Increases Downward (Not Like Cartesian)

### This is an image/array convention, not a math choice

In **mathematics**: y increases upward (standard Cartesian)

In **images/arrays**: row index increases downward

```
Mathematics:              Image/Array:
y↑                        row 0 ──→ col increases
│                         row 1
│                         row 2
└────→ x                  ↓ row increases
```

**Why?** Because when you store a 2D array in memory, you store it row by row:

```
Memory layout:
[row0_col0, row0_col1, ..., row0_colM,
 row1_col0, row1_col1, ..., row1_colM,
 ...
 rowN_col0, ...]
```

The first element is top-left. Row index naturally increases as you go **down** through memory.

### The DFT inherits this convention from the image

Since DFT input is an image (array), and DFT output has the same M×N shape:

```
f(x, y) → F(u, v)

x increases rightward  →  u increases rightward
y increases DOWNWARD   →  v increases DOWNWARD
```

So the v-axis is **flipped** relative to Cartesian math convention.

### Does this affect our frequency calculation?

**For frequency magnitude — NO.** Because:
```
Feff = √(Fx² + Fy²)
```
Squaring removes the sign — direction doesn't matter for magnitude.

**For orientation angle — YES, you must be careful:**
```
In Cartesian:  θ = arctan(Fy/Fx)  counts counterclockwise from x-axis
In image:      θ = arctan(Fy/Fx)  counts CLOCKWISE from x-axis
               (because y/v axis is flipped)
```

---

## The Complete Corrected Picture

```
SHIFTED DFT space for 640×480 image:

              u = −320        u = 0        u = +320
               │               │               │
v = −240 ──────┼───────────────┼───────────────┼──────
               │               │               │
               │   (−100,−100) │               │
               │       ●       │               │
               │               │               │
v = 0    ──────┼───────────────●───────────────┼──────
               │               DC              │
               │               │               │
               │               │   ●           │
               │               │ (+100,+100)   │
               │               │               │
v = +240 ──────┼───────────────┼───────────────┼──────

REMEMBER:
• DC (zero frequency) at CENTER (0,0) after fftshift
• Conjugate peaks at (+100,+100) and (−100,−100) — symmetric about DC
• v increases DOWNWARD (image convention)
• Peak at (+100,+100) means:
      100 cycles across 640 pixels in x-direction
      100 cycles across 480 pixels in y-direction
```

---

## Summary Table

| Question | Answer |
|---|---|
| Why is DFT space M×N? | DFT gives exactly one output per input — N inputs → N frequency bins, always |
| What does index u mean? | u complete wave cycles fit across the M-pixel width |
| Why DC at corner in raw DFT? | Formula starts at u=0, v=0 which maps to array index [0,0] = top-left |
| Why DC at center in diagrams? | fftshift swaps quadrants, remapping indices to run −M/2 to +M/2 |
| Why v increases downward? | Inherited from image/array convention — rows stored top-to-bottom in memory |
| Does downward-v affect results? | Magnitude: No. Angle: Yes — measured clockwise, not counterclockwise |


