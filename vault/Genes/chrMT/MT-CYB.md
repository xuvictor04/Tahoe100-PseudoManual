---
symbol: "MT-CYB"
type: "gene"
col: 12655
ensembl_id: "ENSG00000198727"
name: "mitochondrially encoded cytochrome b"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 328.16
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-CYB

*mitochondrially encoded cytochrome b* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.60× (z +15.0, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.40× (z +3.3, q 0.074, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HCT15 7.38×, LoVo 6.87×, NCI-H460 5.30×, LS 180 6.45×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 5.45×, HT-29 5.45×, NCI-H460 4.83×, A498 6.02×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 5 µM in 2 lines (SW1417 2.13×, SNU-423 2.18×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.346× (z -14.8, q 0e+00, down in 44 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HCT15 7.38×, LoVo 6.87×, NCI-H460 5.30×, LS 180 6.45×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 5.45×, HT-29 5.45×, NCI-H460 4.83×, A498 6.02×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 5 µM in 2 lines (SW1417 2.13×, SNU-423 2.18×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.60×** | +15.0 | 0e+00 | 49/49 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +13.2 | 4e-37 | 44/44 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +10.5 | 1e-23 | 44/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.2 | 0.004 | 31/47 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.8 | 0.017 | 35/47 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.44×** | +3.5 | 0.037 | 43/49 (NCI-H2347, RKO, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.41×** | +3.4 | 0.060 | 41/47 (SW480, BT-474, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.074 | 41/48 (SW48, LS 180, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +3.2 | 0.078 | 37/48 (HS-578T, KATO III, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.2 | 0.087 | 24/38 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.13 | 33/48 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12655.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.346×** | -14.8 | 0e+00 | 44/48 (A549, Hs 766T, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.271×** | -12.9 | 1e-35 | 48/48 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.505×** | -9.6 | 2e-19 | 42/49 (NCI-H460, Hs 766T, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -7.4 | 3e-11 | 36/48 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.621×** | -4.7 | 3e-04 | 33/48 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.641×** | -4.4 | 9e-04 | 31/48 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -4.2 | 0.002 | 28/48 (RKO, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -3.9 | 0.007 | 31/48 (C32, SW 900, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.729× | -3.1 | 0.10 | 34/48 (BT-474, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | 0.733× | -3.1 | 0.11 | 35/47 (AsPC-1, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 469 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -13.4) |
| [[SW1417 (line)]] | alt | 330 | 4 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.13× (z +9.7) | [[Docetaxel (drug)]] 0.05 µM 0.270× (z -12.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.446× (z -10.6) |
| [[A-172 (line)]] | wt | 348 | 4 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +12.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.220× (z -16.8) |
| [[A498 (line)]] | wt | 287 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +14.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.257× (z -14.5) |
| [[A549 (line)]] | wt | 359 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +13.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.132× (z -24.1) |
| [[H4 (line)]] | wt | 193 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +10.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.236× (z -14.1) |
| [[Hs 766T (line)]] | wt | 396 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.155× (z -23.3) |
| [[LS 180 (line)]] | wt | 297 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +14.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 324 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +13.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.258× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 242 | 5 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.259× (z -11.8) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 344 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +14.7) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.187× (z -21.0) |
| [[PANC-1 (line)]] | alt | 414 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.149× (z -21.6) |
| [[SNU-423 (line)]] | alt | 299 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.18× (z +8.9) | [[Docetaxel (drug)]] 0.05 µM 0.282× (z -10.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.424× (z -9.7) |
| [[SW480 (line)]] | alt | 316 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.45× (z +14.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.290× (z -15.0) |
| [[C-33 A (line)]] | alt | 214 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +10.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.273× (z -12.1) |
| [[C32 (line)]] | wt | 182 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.45× (z +10.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.403× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 388 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +11.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.285× (z -9.5) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.438× (z -8.8) |
| [[HOP62 (line)]] | alt | 190 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +12.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.288× (z -13.3) |
| [[HS-578T (line)]] | alt | 194 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.36× (z +11.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.283× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 231 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +10.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.385× (z -10.2) |
| [[J82 (line)]] | alt | 350 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +10.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.175× (z -15.2) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.328× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 202 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +12.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.228× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 390 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.194× (z -19.3) |
| [[SW 900 (line)]] | alt | 352 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +11.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.217× (z -17.0) |
| [[A-427 (line)]] | wt | 399 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.215× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 213 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +11.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.308× (z -8.9) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 186 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +11.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.338× (z -8.5) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 369 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.172× (z -14.3) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.350× (z -12.0) |
| [[HT-29 (line)]] | alt | 353 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +13.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.271× (z -10.8) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 450 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.277× (z -10.3) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 257 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +14.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.304× (z -9.1) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 299 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.94× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.293× (z -8.8) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 217 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +12.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.267× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 817 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +10.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.198× (z -19.8) |
| [[SK-MEL-2 (line)]] | alt | 560 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -20.2) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 342 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.201× (z -16.1) |
| [[AN3 CA (line)]] | alt | 259 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.206× (z -9.2) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 286 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.232× (z -9.3) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 212 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 417 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +11.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.232× (z -12.3) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.388× (z -11.3) |
| [[SW48 (line)]] | wt | 332 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +11.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.307× (z -9.3) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 250 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +15.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 180 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 729 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.187× (z -14.2) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 203 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.316× (z -10.9) |
| [[NCI-H661 (line)]] | alt | 359 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.131× (z -15.0) |
| [[SW 1271 (line)]] | alt | 246 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.156× (z -14.1) |
| [[NCI-H2122 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 233 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded cytochrome b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:14,747-15,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COB, CYTB, UQCR3; previously MTCYB |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits; Mitochondrially encoded protein coding genes |
| Reactome | 16 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P00156](https://www.uniprot.org/uniprotkb/P00156) (Cytochrome b):

> Component of the ubiquinol-cytochrome c reductase complex (complex III or cytochrome b-c1 complex) that is part of the mitochondrial respiratory chain. The b-c1 complex mediates electron transfer from ubiquinol to cytochrome c. Contributes to the generation of a proton gradient across the mitochondrial membrane that is then used for ATP synthesis.

**Summary**, from NCBI Gene [4519](https://www.ncbi.nlm.nih.gov/gene/4519):

> Predicted to enable electron transfer activity; metal ion binding activity; and oxidoreductase activity. Predicted to contribute to quinol-cytochrome-c reductase activity. Predicted to be involved in mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrial inner membrane. Implicated in ovarian carcinoma and urinary bladder cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7427) · Entrez [4519](https://www.ncbi.nlm.nih.gov/gene/4519) · UniProt [P00156](https://www.uniprot.org/uniprotkb/P00156) · Ensembl [ENSG00000198727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198727)

## Data

Gene col 12655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12655); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12655, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12655]; `tensor/DDL_lfc|DDL_z.npy` [12655]; `embed/gene_vectors.npy` [12655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12655 or target_col == 12655). Every well: [[MT-CYB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-CYB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
