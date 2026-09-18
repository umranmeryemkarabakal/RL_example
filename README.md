# RL_example

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib" />
</p>

## 🇬🇧 Overview

Two reinforcement-learning approaches to the multi-armed bandit problem, choosing which ad to show on `Ads_CTR_Optimisation.csv`: Upper Confidence Bound and Thompson Sampling.

**Quick start:** `pip install -r requirements.txt && python ucb.py`

## 🇹🇷 Proje hakkında

Çok kollu haydut (multi-armed bandit) problemini reklam seçimi üzerinden çözen iki pekiştirmeli öğrenme yöntemi: Upper Confidence Bound (UCB) ve Thompson Sampling.

## ✨ Özellikler

- `ucb.py`: UCB ile reklam seçimi ve toplam ödül
- `thompson_sampling.py`: Beta dağılımıyla Thompson Sampling
- Seçilen reklamların histogramı

## ⚙️ Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```bash
python thompson_sampling.py
```

## 📁 Dosya yapısı

```text
RL_example/
├── Ads_CTR_Optimisation.csv
├── thompson_sampling.py
└── ucb.py
```
