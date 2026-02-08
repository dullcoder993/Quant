# Mithril Instability Engine (v1.0)
### Log-Periodic Power Law (LPPL) Analysis for Market Singularity Detection

---

 Project Overview

**Mithril Instability Engine** is a quantitative research tool designed to detect **super-exponential price behavior** and **speculative bubbles** in financial markets.

Rather than tracking price direction, the engine measures **instability in the price formation process itself**, identifying mathematical signatures of **herding behavior** that typically precede **regime shifts, peaks, or crashes**.

The core methodology is based on the **Log-Periodic Power Law (LPPL)** framework developed by Didier Sornette and collaborators.

---

Core Idea

Markets approaching a crash often exhibit:
- Accelerating (super-exponential) growth  
- Increasingly frequent oscillations  
- Collective synchronization of trader behavior  

LPPL captures these dynamics by modeling the **log of price** as it approaches a critical time \( t_c \), interpreted as a **singularity point**.

---

 Features

 7-Parameter LPPL Optimization
- Implements the full LPPL equation using **SciPy’s `least_squares` optimizer**
- Levenberg–Marquardt algorithm for non-linear convergence
- Enforces theoretical constraints on parameters to avoid spurious fits

 Multi-Scale Windowing
- Evaluates **15 distinct rolling look-back windows**
- Ensures robustness across time scales
- Filters out false positives caused by local noise

 Criticality & Hazard Metrics
- **Criticality Score**
  - Measures degree of crowd synchronization
  - Values **> 55** indicate extreme instability
- **Hazard Score**
  - Estimates instantaneous probability of a crash occurring at `t_today`
  - Derived from convergence and proximity to predicted \( t_c \)

 Automated Regime Classification
Assets are classified into:
- **NORMAL** – Stable, non-bubble behavior
- **WARNING** – Developing instability
- **CRITICAL** – Imminent regime shift risk

---

 Mathematical Foundation

The engine fits the natural logarithm of price \( \ln P(t) \) to the LPPL formulation:

$$ln P(t) = A + B(t_c - t)^m [1 + C \cos(\omega \ln(t_c - t) + \phi)]$$

 Parameter Interpretation
-  t_c : Predicted singularity (crash / peak time)
-  m: Power-law exponent  
  - Valid bubble range: \( 0.1 < m < 0.9 \)
- **\( \omega \)**: Frequency of log-periodic oscillations
- **\( C \)**: Oscillation amplitude (herding strength)
- **\( A, B, \phi \)**: Calibration parameters

---

## 📊 Performance Case Study

### Asset: Silver Futures (SI=F)

**Simulation Period:** February 2026  

| Metric | Value |
|------|------|
| Signal Date | Feb 2, 2026 |
| Hazard Score | **0.249** |
| Criticality | **58.53** |
| Predicted \( t_c \) | 13 days from signal |

### Outcome
- Engine identified a **high-risk singularity window**
- Captured the **peak of a 5× parabolic price run**
- Signal occurred **before** the actual market reversal

This validates the engine’s ability to detect **structural instability**, not just trend exhaustion.

---

## 📦 Tech Stack

- Python
- NumPy
- SciPy
- Pandas
- Custom statistical validation modules

---

## ⚠️ Disclaimer

This project is for **research and educational purposes only**.  
It does **not** constitute financial advice or a trading system.

LPPL models identify **probabilistic instability**, not guaranteed crashes.

---

 Future Work (v1.1+)
- Bayesian parameter stability scoring
- Cross-asset contagion analysis
- Real-time streaming inference
- Integration with volatility & options-implied stress metrics

---

## 🧙‍♂️ Why “Mithril”?
Mithril doesn’t predict direction — it reveals **hidden structural weakness** before collapse.
