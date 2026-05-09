micro architecture of physical layer processing for 5G NR SUB6 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/c155e32d-6bc2-4434-9370-eadbc16ebeb0" />


Explain each block here to a layman 

Think of the 5G NR physical layer as a **high-speed digital factory** that converts:

* your app data → into radio waves (Transmit path)
* radio waves → back into app data (Receive path)

The diagram shows the “assembly line” inside a 5G modem/baseband chip for **Sub-6 GHz (FR1)** systems.

---

# 1. Big Picture

There are two halves:

| Side              | Meaning        |
| ----------------- | -------------- |
| **Transmit (TX)** | Sending data   |
| **Receive (RX)**  | Receiving data |

Both exist in:

* the **gNB** (5G base station)
* the **UE** (phone/modem)

---

# 2. TRANSMIT CHAIN (Sending Data)

This is the path when your phone uploads a photo or the tower sends you a video.

---

# A. MAC / Higher Layer

These are networking layers above the physical radio.

| Block | Layman Explanation                             |
| ----- | ---------------------------------------------- |
| SDAP  | Decides traffic priority (video call vs email) |
| PDCP  | Security + packet handling                     |
| RLC   | Breaks large data into chunks                  |
| MAC   | Schedules when/how data is sent                |

Think of this as:

> “Traffic management before radio transmission.”

---

# B. CRC Attach

## What it does

Adds a small “error-detection signature.”

Like adding:

> “If this message changes accidentally, detect it.”

---

# C. LDPC Encoder

## Most important reliability block

5G uses:

* LDPC coding for data channels
* Polar coding for control channels

This adds carefully designed redundancy.

Example:

Instead of sending:

```text
101101
```

It sends:

```text
101101 + extra check bits
```

So receiver can recover corrupted bits.

---

# D. Code Block Segmentation

If data is too large:

* split into smaller pieces.

Like splitting a large parcel into smaller boxes.

---

# E. Rate Matching

Adjusts coding amount depending on:

* channel quality
* bandwidth
* modulation

Good channel:
→ less redundancy

Bad channel:
→ more protection

---

# F. Bit Interleaving

Shuffles bits before transmission.

Why?

Because wireless errors often happen in bursts.

Shuffling spreads errors out so decoding becomes easier.

Like:

> spreading eggs into many baskets.

---

# G. QAM Modulation

Converts bits into symbols.

Example:

| Modulation | Bits per Symbol |
| ---------- | --------------- |
| QPSK       | 2               |
| 16-QAM     | 4               |
| 64-QAM     | 6               |
| 256-QAM    | 8               |

Higher QAM:

* faster
* but needs cleaner signal

---

# H. Layer Mapping

Used for MIMO.

Instead of one stream:

```text
Stream 1
```

5G can send:

```text
Stream 1
Stream 2
Stream 3
Stream 4
```

simultaneously.

Like opening multiple lanes on a highway.

---

# I. Precoding

Smart antenna processing.

Changes signals so antennas cooperate constructively.

Goal:

* beamforming
* interference reduction
* higher SNR

Like:

> several speakers synchronizing sound toward one listener.

---

# J. Resource Element Mapping

Places symbols onto the OFDM time-frequency grid.

5G radio is like a huge spreadsheet:

| Time | Frequency |
| ---- | --------- |
| cell | cell      |

Each small box = Resource Element (RE)

Data gets inserted into these boxes.

---

# K. DMRS / PTRS / CSI-RS Insertion

These are reference signals.

---

## DMRS (Demodulation Reference Signal)

Known pilot signals.

Receiver uses them to estimate channel distortion.

Like sending:

> “Here is a known test pattern.”

---

## PTRS (Phase Tracking Reference Signal)

Corrects phase noise.

Important at high frequencies.

---

## CSI-RS (Channel State Information RS)

Measures channel quality.

Helps beamforming and scheduling.

---

# L. IFFT (OFDM Generation)

This is the heart of OFDM.

Transforms frequency-domain symbols into time-domain waveform.

Mathematically:

x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}

Layman meaning:

> combine many tiny subcarriers into one signal.

---

# M. Cyclic Prefix (CP)

Copies a small tail of OFDM symbol and pastes at front.

Why?

To combat multipath reflections.

Like adding a “safety guard region.”

---

# N. Windowing

Smooths waveform edges.

Reduces spectral leakage.

Think:

> softening sharp edges to reduce splatter.

---

# O. DAC + RF Frontend

## DAC

Digital → Analog conversion.

Computer numbers become electrical waveform.

---

## Upconversion

Moves signal from baseband to RF frequency.

Example:

```text
Baseband → 3.5 GHz
```

---

## Power Amplifier (PA)

Boosts signal power before antenna transmission.

---

# 3. ANTENNA SYSTEM

Multiple antennas enable:

* MIMO
* Beamforming
* Spatial multiplexing

Instead of broadcasting everywhere:

5G forms directed beams.

Like flashlight beams instead of light bulbs.

---

# 4. RECEIVE CHAIN (Reverse Process)

Now the receiver undoes everything.

---

# A. LNA (Low Noise Amplifier)

Very weak incoming signals are amplified carefully.

Like hearing a whisper with minimal added noise.

---

# B. ADC

Analog radio wave → digital samples.

---

# C. CP Removal

Removes cyclic prefix added earlier.

---

# D. FFT

Reverse of IFFT.

Separates OFDM signal back into subcarriers.

X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}

---

# E. Timing Synchronization

Finds exact OFDM symbol boundaries.

Without this:
everything shifts incorrectly.

Like aligning pages before reading.

---

# F. Frequency Offset Compensation

Corrects oscillator mismatch.

Even tiny frequency errors break OFDM.

---

# G. Channel Estimation

Uses DMRS pilots to estimate channel distortion.

Wireless channel causes:

* fading
* phase shifts
* reflections

Receiver learns channel behavior.

---

# H. Equalization

Attempts to reverse channel distortion.

Mathematically:

\hat{X}=\frac{Y}{H}

Meaning:

```text
Received Signal / Channel Effect
```

≈ original signal.

---

# I. MIMO Equalization

Separates multiple spatial streams.

If antennas received mixed streams:

```text
A+B+C
```

this block untangles them.

Very computation-heavy.

---

# J. QAM Demodulation

Converts constellation points back into bits.

Example:

```text
symbol → 110101
```

---

# K. LLR Generation

Creates “confidence values” for decoder.

Not just:

```text
1 or 0
```

but:

```text
probably 1 with 95% confidence
```

Critical for LDPC decoding.

---

# L. LDPC Decoder

Recovers original data using redundancy.

This is one of the largest hardware accelerators in a 5G modem.

Often consumes massive silicon area and power.

---

# M. CRC Check

Final integrity check.

If failed:
→ retransmission requested (HARQ).

---

# 5. Common Functions

---

# HARQ

Hybrid Automatic Repeat Request.

If packet corrupted:

* retransmit only necessary parts.

Like:

> asking someone to repeat only unclear words.

---

# CQI / PMI / RI Reporting

Phone reports channel quality to tower.

Tower adapts:

* modulation
* coding
* beamforming
* MIMO layers

---

# Beam Management

Tracks best beam direction dynamically.

Critical in mobility.

---

# Power Monitoring

Controls transmit power.

Avoids:

* battery waste
* interference

---

# 6. Numerology (Very Important in 5G)

5G supports different subcarrier spacing.

| μ | Subcarrier Spacing |
| - | ------------------ |
| 0 | 15 kHz             |
| 1 | 30 kHz             |
| 2 | 60 kHz             |
| 3 | 120 kHz            |

Larger spacing:

* lower latency
* better for high frequencies
* but less coverage efficiency

---

# 7. What Makes 5G PHY Hard?

The modem must simultaneously handle:

* OFDM
* LDPC
* Massive MIMO
* Beamforming
* Synchronization
* Channel estimation
* HARQ
* Scheduling
* Multi-gigabit throughput

all in real time with millisecond latency.

---

# 8. Real Hardware Microarchitecture

Inside an actual SoC:

| Function       | Hardware Style         |
| -------------- | ---------------------- |
| FFT/IFFT       | DSP accelerator        |
| LDPC           | Dedicated ASIC         |
| MIMO Equalizer | Matrix accelerator     |
| Beamforming    | Vector processors      |
| Scheduling     | Embedded CPU           |
| RF control     | Mixed-signal circuitry |

---

# 9. Mental Model

A useful analogy:

| 5G Block     | Analogy                        |
| ------------ | ------------------------------ |
| Coding       | Error-proof packaging          |
| Modulation   | Translating into wave patterns |
| OFDM         | Multi-lane highway             |
| MIMO         | Multiple highways              |
| Beamforming  | Steering traffic intelligently |
| Equalization | Undoing road damage            |
| HARQ         | Asking for repeats             |

---

# 10. Core Insight

The physical layer is fundamentally doing 3 things:

1. **Protect data against wireless corruption**
2. **Pack enormous data efficiently into spectrum**
3. **Exploit space/time/frequency simultaneously**

That is why modern 5G modems are among the most sophisticated digital systems ever built.


consider the recieve path
why is the order of processing this way

The receive chain order is not arbitrary.

It is dictated by:

1. **Physics of radio propagation**
2. **Mathematics of OFDM**
3. **Information dependencies**
4. **Hardware feasibility**

Each block prepares the signal so the *next* block can work correctly.

The chain is essentially a sequence of:

> progressively converting an unknown distorted analog waveform into reliable bits.

---

# Big Picture

At the antenna, the receiver gets:

```text
Desired signal
+ noise
+ interference
+ multipath reflections
+ oscillator mismatch
+ Doppler shift
```

all mixed together.

The receive chain carefully removes uncertainty layer-by-layer.

---

# 1. Antenna → LNA

## Why first?

Incoming signal is extremely weak.

Typical received power:

```text
-70 dBm to -110 dBm
```

That is tiny.

Without amplification:

* ADC cannot resolve signal properly
* thermal noise dominates

---

## Why LNA before everything else?

Because once noise is added later:

you cannot remove it.

So the first amplifier must be:

* very low noise
* very linear

This determines receiver sensitivity.

---

# 2. RF Filtering

After amplification:

remove unwanted frequencies.

Why?

Receiver may also see:

* WiFi
* neighboring carriers
* other operators
* harmonics

If these enter ADC:

* dynamic range collapses
* clipping occurs

So filtering must happen early.

---

# 3. Downconversion

Signal arrives at RF:

Example:

```text
3.5 GHz
```

Digital processing at GHz carrier directly is impractical.

So mixer shifts signal to:

```text
baseband or IF
```

Now DSP becomes feasible.

---

# 4. ADC

Now convert analog waveform into digital samples.

Why here?

Because all later operations are digital:

* FFT
* equalization
* LDPC
* MIMO

ADC bridges physical world ↔ DSP world.

---

# Important Dependency

ADC must happen AFTER:

* amplification
* filtering

Otherwise:

* quantization poor
* overload occurs

---

# 5. CP Removal

Now we enter OFDM mathematics.

Transmitter added cyclic prefix.

Receiver must remove it before FFT.

Why?

Because OFDM assumes:

x[n+N]=x[n]

CP converts linear convolution into circular convolution.

FFT-based equalization only works after removing CP properly.

---

# Why not FFT before CP removal?

Because FFT window would contain duplicated samples.

That destroys subcarrier orthogonality.

Result:

* intercarrier interference (ICI)

---

# 6. FFT

Now convert time-domain waveform into frequency-domain subcarriers.

Why now?

Because before FFT:

all subcarriers are mixed together in time-domain.

After FFT:

```text
Subcarrier 1
Subcarrier 2
Subcarrier 3
...
```

become separated.

This is essential because:

* equalization
* demodulation
* channel estimation

are done per subcarrier.

---

# Key Insight

Before FFT:

```text
one complicated waveform
```

After FFT:

```text
thousands of narrowband channels
```

This dramatically simplifies receiver design.

---

# 7. Timing Synchronization

Now determine exact OFDM symbol boundaries.

Why after FFT-related acquisition stages?

Because synchronization often uses:

* PSS/SSS
* correlation
* pilot structure

which become clearer after partial processing.

---

# Why synchronization is critical

OFDM subcarriers are orthogonal only if FFT window aligned correctly.

Small timing error causes:

* phase rotation
* intersymbol interference
* intercarrier interference

---

# 8. Frequency Offset Compensation

Transmitter and receiver oscillators are never identical.

Example:

```text
TX: 3.500000 GHz
RX: 3.500001 GHz
```

Tiny mismatch causes rotating phase error.

---

# Why before equalization/demodulation?

Because frequency offset destroys constellation structure.

QAM points rotate continuously:

```text
ideal constellation → spinning constellation
```

Demodulator cannot decide bits correctly.

So carrier correction must occur early.

---

# 9. Channel Estimation

Now estimate wireless channel.

Wireless channel behaves like:

Y[k]=H[k]X[k]+N[k]

Receiver knows:

* pilot symbols
* received pilots

So it estimates:

H[k]=\frac{Y[k]}{X[k]}

---

# Why only now?

Because:

* subcarriers must already be separated (FFT)
* timing must be aligned
* frequency offset corrected

Otherwise pilot measurements are wrong.

---

# 10. Equalization

Now undo channel distortion.

Example:

If channel attenuated subcarrier by:

```text
0.2
```

equalizer compensates by:

```text
×5
```

---

# Why after channel estimation?

Equalizer needs channel estimate.

Without knowing (H[k]), inversion impossible.

---

# Why before demodulation?

Because demodulator expects ideal constellation points.

Without equalization:

```text
QAM clusters become smeared/distorted
```

Bit decisions become unreliable.

---

# 11. MIMO Detection / Layer Demapping

In MIMO:

multiple streams overlap spatially.

Receiver observes:

\mathbf{y}=\mathbf{H}\mathbf{x}+\mathbf{n}

Need matrix inversion or MMSE/ZF detection.

---

# Why after equalization?

Because channel matrix estimate needed first.

---

# Why before demodulation?

Because individual streams not yet separated.

Demodulator requires isolated symbols.

---

# 12. QAM Demodulation

Now constellation points are mostly corrected.

Convert symbols → bits.

Example:

```text
received point near (1,1)
→ binary pattern
```

---

# Why only now?

Because before:

* synchronization errors
* channel fading
* MIMO mixing

made symbol interpretation impossible.

---

# 13. LLR Generation

Modern decoders do not want hard bits.

Instead:

```text
Bit = 1 with 92% confidence
```

These soft probabilities dramatically improve coding gain.

---

# Why after demodulation?

Need constellation distance information first.

LLRs are derived from:

* Euclidean distances
* noise variance

---

# 14. LDPC Decoding

Now use redundancy to recover original bits.

Iterative belief propagation uses LLRs.

---

# Why near the end?

Because decoder assumes:

* synchronized bits
* separated streams
* corrected channel effects

Otherwise decoding fails catastrophically.

---

# 15. CRC Check

Final integrity verification.

If failed:

* HARQ retransmission requested.

---

# The Deep Principle

The order follows a dependency ladder:

| Step               | Removes                    |
| ------------------ | -------------------------- |
| RF frontend        | Analog impairments         |
| Synchronization    | Time/frequency uncertainty |
| FFT                | Subcarrier mixing          |
| Channel estimation | Unknown channel            |
| Equalization       | Channel distortion         |
| MIMO detection     | Spatial mixing             |
| Demodulation       | Symbol uncertainty         |
| LDPC decoding      | Residual bit errors        |

Each stage reduces uncertainty.

---

# Another Way to View It

The receiver progressively changes the representation:

| Stage        | Representation       |
| ------------ | -------------------- |
| Antenna      | Electromagnetic wave |
| ADC          | Time samples         |
| FFT          | Frequency bins       |
| Equalizer    | Corrected symbols    |
| Demodulator  | Probabilities        |
| LDPC decoder | Reliable bits        |
| MAC          | Packets              |

---

# Most Important Insight

OFDM receiver design is fundamentally based on this trick:

Instead of solving one gigantic broadband channel problem,

FFT converts it into:

```text
many tiny narrowband problems
```

That single idea is why:

* equalization becomes simple
* MIMO becomes tractable
* 5G becomes scalable.


