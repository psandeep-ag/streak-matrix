Let me read the PDF carefully and explain the assignment thoroughly.

# EE5175W Lab-5: K-means Clustering — Full Breakdown

## 🧠 Big Picture First: What is K-means Clustering?

K-means is an algorithm that **groups similar things together**. Here, instead of grouping people or documents, we're grouping **pixel colors** in an image. The goal is to simplify an image by reducing all its colors down to just **K representative colors** (called *cluster centers* or *centroids*).

---

## 📸 The Setup

> *"Perform K-means clustering on two input images (car.png and flower.png) for K = 3 clusters."*

- You have **2 images** to work on: a car and a flower.
- **K = 3** means you want to group all pixel colors into exactly **3 color groups**.
- At the end, every pixel in the image will be replaced by one of 3 colors — giving a "posterized" look.

---

> *"Basic data units to be clustered are vectors containing pixel data, i.e., [r g b]"*

- Each pixel is not just a single number — it has **3 values**: Red, Green, Blue (each ranging 0–255).
- So one pixel = one data point = one vector like `[120, 45, 200]`.
- You're clustering these vectors in **3D color space**.

---

> *"Use only Euclidean distance as the distance measure"*

- When deciding which cluster a pixel belongs to, you measure **how far** its color `[r, g, b]` is from each cluster center using the standard distance formula:

$$d = \sqrt{(r_1 - r_2)^2 + (g_1 - g_2)^2 + (b_1 - b_2)^2}$$

- The pixel joins whichever cluster center it is **closest** to.

---

> *"Perform 5 iterations of the algorithm"*

One iteration of K-means = two steps:
1. **Assign** every pixel to the nearest cluster center
2. **Update** each cluster center = average color of all pixels assigned to it

You repeat this 5 times. The centers gradually "move" to better represent the colors in the image.

---

> *"Replace each pixel with the cluster center it belongs to and display the resulting image"*

- After 5 iterations, each pixel gets **replaced** by its cluster center's color.
- If a pixel was assigned to cluster 2 whose center is `[200, 180, 30]`, that pixel now becomes that golden-yellow color.
- This is how you **visualize** the clustering output.

---

## Part (a): Fixed Initialization

> *"Initial cluster means: c₁ = [255,0,0], c₂ = [0,0,0], c₃ = [255,255,255]"*

- You **manually set** the starting cluster centers:
  - c₁ = pure **Red**
  - c₂ = pure **Black**
  - c₃ = pure **White**
- The algorithm then runs 5 iterations from these starting points.
- **Why this matters:** K-means is sensitive to where you start. This part gives you a **controlled, reproducible** baseline — same starting point every time.

---

## Part (b): Random Initialization (N = 30 runs)

> *"Generate 3 random vectors of size 1×3 sampled from uniform distribution in [0, 255]"*

- Instead of fixed starting colors, you **randomly pick** 3 starting colors.
- Each component (R, G, B) is a random number between 0 and 255.
- Example random start: `[34, 210, 88]`, `[190, 5, 140]`, `[77, 77, 200]`

---

> *"Perform K-means clustering using N = 30 such initializations"*

- You run the **entire K-means process 30 separate times**, each with a different random start.
- This is because bad starting points can lead to bad final clustering (K-means can get stuck in local optima).

---

> *"The cost C = Σ dist(pᵢ, cₖ)"*

- After each run, you compute a **cost score C**:
  - For every pixel, find the Euclidean distance to its assigned cluster center.
  - **Sum all those distances** across all pixels.
- A **low C** = pixels are very close to their cluster centers = tight, good clusters = better image compression.
- A **high C** = pixels are far from centers = loose, bad clusters = poor representation.

---

> *"Find the output corresponding to the lowest and highest value of C. Comment on your observations."*

- Among 30 runs, pick:
  - The **best run** (lowest C) → show that image
  - The **worst run** (highest C) → show that image
- **Expected observation:** The best-C image will look more "faithful" to the original's color regions, while the worst-C image may have poor color groupings (e.g., an entire region getting the wrong color).

---

## 📝 The Notes Explained

> *"Each pixel has (R,G,B) components. The matrix is 3-dimensional (height × width × 3)"*

- An image of size 480×640 becomes a matrix of shape `480 × 640 × 3`.
- `img[m, n, 0]` = Red value at row m, column n
- `img[m, n, 1]` = Green value
- `img[m, n, 2]` = Blue value

---

> *"If any cluster turned out to be empty, use only the non-empty clusters"*

- Sometimes a cluster center is so far from all pixels that **no pixel gets assigned to it** — it becomes an empty cluster.
- You can't compute an average of nothing, so just **ignore that cluster** and work with the remaining ones.
- This is a common edge case in K-means implementations.

---

## 🔑 Summary Table

| Concept | What it means |
|---|---|
| K = 3 | Final image will have only 3 colors |
| [r, g, b] vector | Each pixel is a point in 3D color space |
| Euclidean distance | How "different" two colors are |
| 5 iterations | How many times you refine the cluster centers |
| Fixed init (part a) | Controlled, deterministic starting point |
| Random init (part b) | Explores different solutions |
| Cost C | Measures how good a clustering is (lower = better) |
| N = 30 | Run 30 times to find best & worst outcomes |

The core idea: **compress an image's color palette to K colors** using iterative optimization, and understand how starting conditions affect the result.


Now I have the full picture. Let me build a detailed, beautiful flowchart.Now I have everything I need. Let me build the flowchart.Here's the complete flowchart of your implementation. Let me walk you through the key structural choices:

**Overall structure** — `main()` runs `process_image()` once per image, then splits into two parallel tracks: Part (a) on the left and Part (b) on the right. Both eventually merge and the whole thing repeats for the second image.

**The dashed boxes** represent loops — the inner one is the 5-iteration K-means loop (shared by both parts), and the outer one in Part (b) is the 30-run random restart loop.

**Key flow inside `kmeans_basic`** (the 5-iteration loop):
1. For every pixel → compute Euclidean distance to all 3 centers → assign to nearest
2. For each cluster → collect its pixels → take mean → handle empty cluster edge case
3. Arrow on the left curves back up to repeat for the next iteration

**Part (b) extra logic** — after each of the 30 runs, there's a diamond checking whether the new cost is better or worse than the tracked best/worst, and the corresponding image gets saved. After all 30 runs, the best and worst images are displayed.


