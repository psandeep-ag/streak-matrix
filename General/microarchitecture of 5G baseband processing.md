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






how fast is the data coming over the air 
20MHz or 100MHz or 500MHz how the bandwidth is scanned and data colelcted
in 1 second ow much daa is collected and number of RBs / resource mapping diagram how it translates / maps into this diagram's processing blocks and sequence ? 
protocol says certain things 
we have transport, logical , physical channels etc.
how all of this falls into place or maps into these microarchitecture block processing sequence



Now you are asking the *real systems question*:

> How does the abstract 5G protocol/resource grid become an actual real-time hardware dataflow pipeline?

This is exactly how modem architects think.

The confusion usually comes because 3GPP describes things in:

* logical abstractions
* channels
* RBs
* slots
* symbols

while hardware sees:

* DMA streams
* SRAM buffers
* FFT windows
* vector engines
* LDPC accelerators

The PHY microarchitecture is the bridge between these worlds.

---

# 1. First: What Is Actually Coming Over the Air?

The antenna receives a **continuous analog electromagnetic waveform**.

Not packets.
Not RBs.
Not bits.

Just:

```text id="4o02u5"
Voltage vs time
```

The receiver samples this waveform.

---

# 2. Example: 100 MHz NR Carrier

Suppose:

| Parameter         | Value     |
| ----------------- | --------- |
| Carrier bandwidth | 100 MHz   |
| SCS               | 30 kHz    |
| FR1               | Sub-6 GHz |
| MIMO              | 4x4       |

---

# 3. ADC Sampling Rate

Nyquist says:

Need sampling rate ≥ bandwidth.

Practical NR implementations for 100 MHz often use:

```text id="8qfsyf"
122.88 MSPS
```

(Million samples/sec)

per antenna chain.

---

# If 4 receive antennas:

```text id="k2lgm1"
4 × 122.88M samples/sec
```

Each sample has:

* I (real)
* Q (imaginary)

Often:

* 12 bits I
* 12 bits Q

So raw incoming digital data rate:

Approximately:

```text id="q2wzk2"
4 × 122.88M × 24 bits
≈ 11.8 Gbps
```

just entering baseband.

Before decoding anything.

---

# 4. What Is “Bandwidth Scanning”?

The receiver does NOT scan frequency like old radios.

Instead:

the RF frontend + ADC digitize the *entire channel bandwidth simultaneously.*

Example:

```text id="e41brq"
Entire 100 MHz captured at once
```

Then FFT separates frequencies digitally.

This is the revolutionary OFDM idea.

---

# Old Radio (pre-OFDM)

Old receivers:

* tuned narrowband channels individually

Like:

* rotating radio dial.

---

# OFDM Receiver

Modern OFDM receiver:

```text id="rfk4zr"
capture huge bandwidth
→ FFT splits into subcarriers
```

like a prism splitting white light into colors.

---

# 5. Where Do RBs Come From?

After FFT.

Before FFT:

receiver has:

```text id="m2j7k8"
time-domain samples
```

After FFT:

receiver gets:

```text id="11b7q7"
frequency bins (subcarriers)
```

---

# Resource Block (RB)

An RB is:

| Dimension | Size            |
| --------- | --------------- |
| Frequency | 12 subcarriers  |
| Time      | 1 slot duration |

At 30 kHz SCS:

```text id="ex6h1r"
12 × 30 kHz = 360 kHz
```

per RB.

---

# Example: 100 MHz NR @ 30 kHz

Maximum usable RBs:

~273 RBs.

---

# Frequency Domain Visualization

```text id="fjh1ya"
|RB1|RB2|RB3|...|RB273|
```

Each RB contains 12 subcarriers.

---

# 6. What FFT Actually Produces

Suppose FFT size = 4096.

FFT output:

```text id="2pd2ei"
Bin0
Bin1
Bin2
...
Bin4095
```

Each bin corresponds to one subcarrier frequency.

Now scheduler says:

```text id="d54tt8"
User A → RBs 0-50
User B → RBs 51-120
User C → RBs 121-200
```

PHY extracts only allocated RBs.

This is resource extraction block.

---

# 7. Time Structure

5G organizes time hierarchically.

---

# Frame Structure

At 30 kHz SCS:

| Unit              | Duration |
| ----------------- | -------- |
| Frame             | 10 ms    |
| Subframe          | 1 ms     |
| Slot              | 0.5 ms   |
| OFDM symbols/slot | 14       |

---

# Data Flow Timing

Every:

```text id="x1nd7f"
0.5 ms
```

receiver must:

* process all symbols
* estimate channel
* decode LDPC
* send HARQ ACK/NACK

This is extremely hard.

---

# 8. How Much Data Per Second?

Let's estimate.

---

# Raw OFDM Resources

For 100 MHz, 30 kHz:

Approximately:

| Quantity     | Value |
| ------------ | ----- |
| RBs          | 273   |
| Subcarriers  | 3276  |
| Symbols/slot | 14    |
| Slots/sec    | 2000  |

Total REs/sec:

```text id="c7gyy6"
3276 × 14 × 2000
≈ 91.7 million REs/sec
```

---

# If using 256-QAM

Each RE carries:

```text id="5lo22f"
8 bits
```

Ignoring overhead:

```text id="e6u4xg"
91.7M × 8
≈ 733 Mbps
```

single layer.

With:

* 4 layers MIMO

≈ several Gbps.

---

# Resource Grid Mapping

This is the key abstraction.

---

# Time-Frequency Grid

Each RE is:

| Frequency    | Time     |
| ------------ | -------- |
| Subcarrier k | Symbol n |

So PHY creates giant matrix:

```text id="f11y8r"
resource_grid[subcarrier][symbol]
```

---

# Some REs carry:

| RE Type | Purpose            |
| ------- | ------------------ |
| PDSCH   | User data          |
| DMRS    | Channel estimation |
| PTRS    | Phase tracking     |
| PDCCH   | Control            |
| PBCH    | Broadcast          |

---

# Example Grid

```text id="7i7h1n"
Freq ↑

DMRS DATA DATA DATA
DATA DATA DATA DATA
DATA PTRS DATA DATA

      → Time
```

---

# 9. How This Maps Into Hardware Blocks

NOW we connect protocol ↔ microarchitecture.

This is the important bridge.

---

# Protocol Layer View

3GPP says:

```text id="7vqk5h"
Transport Block
→ Channel Coding
→ Modulation
→ Layer Mapping
→ Resource Mapping
```

---

# Hardware View

Actual chip does:

```text id="25azhb"
DMA fetch
→ LDPC accelerator
→ Interleaver SRAM
→ QAM mapper
→ MIMO matrix engine
→ Resource grid writer
→ FFT engine
```

---

# 10. Channel Hierarchy

This confuses many people.

---

# Logical Channels

“What type of information?”

Examples:

| Logical Channel | Meaning           |
| --------------- | ----------------- |
| DTCH            | User data         |
| DCCH            | Control signaling |

Handled mostly by MAC/RLC.

---

# Transport Channels

“How is it transported?”

Examples:

| Transport Channel | Meaning                 |
| ----------------- | ----------------------- |
| DL-SCH            | Downlink shared channel |
| UL-SCH            | Uplink shared           |
| BCH               | Broadcast               |

Transport channels define:

* coding
* HARQ
* scheduling

---

# Physical Channels

“What actual REs carry it?”

Examples:

| Physical Channel | Meaning                  |
| ---------------- | ------------------------ |
| PDSCH            | Physical downlink shared |
| PUSCH            | Physical uplink shared   |
| PBCH             | Broadcast                |
| PDCCH            | Control                  |

These map onto actual OFDM resources.

---

# 11. Full Mapping Example

Suppose:
You download YouTube video.

---

# Step 1 — IP Packet

Application generates data.

---

# Step 2 — MAC

MAC scheduler decides:

```text id="t5l1qq"
User gets:
RBs 50-100
Slot #245
MCS 22
4 MIMO layers
```

---

# Step 3 — Transport Block

MAC forms:

```text id="fc0f2g"
Transport Block
```

---

# Step 4 — PHY Processing

Transport block enters:

| PHY Block        | Operation           |
| ---------------- | ------------------- |
| CRC              | Add error detection |
| LDPC             | Add redundancy      |
| Rate match       | Match RB allocation |
| QAM mapper       | Bits → symbols      |
| Layer mapping    | MIMO streams        |
| Precoding        | Beamforming         |
| Resource mapping | Fill RE grid        |

---

# 12. Resource Mapping Hardware

This is literally memory addressing.

Hardware writes symbols into:

```text id="25jlwm"
grid[subcarrier][symbol][antenna]
```

according to scheduler grants.

---

# 13. Then OFDM Generation

IFFT converts:

```text id="pw3wjm"
frequency grid
```

into:

```text id="p4fkk9"
time-domain waveform
```

Now DAC + RF transmit it.

---

# 14. Receiver Does Reverse

Receiver:

```text id="1b55wc"
ADC samples
→ FFT
→ recover subcarriers
→ extract allocated RBs
→ equalize
→ demodulate
→ LDPC decode
```

---

# 15. Important Insight:

# PHY Is Really a Streaming Matrix Processor

Modern 5G PHY is basically:

* gigantic FFT engine
* gigantic matrix algebra engine
* gigantic error-correction engine

processing:

```text id="6mjlwm"
time × frequency × antenna
```

data cube continuously.

---

# 16. Why Order Matters

Because each stage reveals structure.

---

# Before FFT

Receiver sees:

```text id="6q9f7m"
mixed waveform
```

---

# After FFT

Receiver sees:

```text id="f1xk5y"
frequency-separated subcarriers
```

---

# After Resource Extraction

Receiver sees:

```text id="wsmq3d"
only this user's RBs
```

---

# After Equalization

Receiver sees:

```text id="7cvxyo"
clean constellation points
```

---

# After LDPC

Receiver sees:

```text id="ixx7c9"
reliable bits
```

---

# 17. Real Modem Parallelism

Real chips do NOT process serially like software.

They pipeline everything.

Example:

| Engine       | Simultaneously Doing |
| ------------ | -------------------- |
| FFT engine   | Slot N               |
| Equalizer    | Slot N-1             |
| LDPC decoder | Slot N-2             |
| HARQ manager | Slot N-3             |

All concurrently.

---

# 18. Final Mental Model

The entire 5G PHY is:

## A giant real-time conveyor belt

converting:

```text id="jlwm5s"
Electromagnetic waveform
↔
Structured time-frequency resource grid
↔
Reliable bits
```

using:

* FFTs
* matrix operations
* probabilistic decoding
* beamforming
* synchronization

all within microseconds.
