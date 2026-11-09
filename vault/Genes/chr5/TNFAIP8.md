---
symbol: "TNFAIP8"
type: "gene"
col: 7024
ensembl_id: "ENSG00000145779"
name: "TNF alpha induced protein 8"
location: "5q23.1"
module: 141
arm: "+"
pooled_cpm: 129.2
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 19
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# TNFAIP8

*TNF alpha induced protein 8* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.38× (z +6.2, q 2e-07, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.366× (z -21.3, q 0e+00, down in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.439× (z -17.4, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD1]] (+0.59, fdr 1e-05), [[SHB]] (+0.58, fdr 2e-05), [[GPRC5A]] (+0.56, fdr 1e-05); moves opposite to [[CSDE1]] (-0.47, fdr 1e-04), [[NNT]] (-0.47, fdr 5e-05), [[GPX8]] (-0.47, fdr 4e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +6.2 | 2e-07 | 28/47 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +5.8 | 1e-06 | 26/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 2e-06 | 24/47 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +5.2 | 3e-05 | 20/47 (RKO, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.26×** | +4.8 | 2e-04 | 23/46 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.002 | 20/46 (NCI-H2030, LS 180, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.003 | 22/48 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.20×** | +3.9 | 0.007 | 18/47 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.9 | 0.007 | 19/47 (KATO III, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.012 | 17/47 (A-427, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.092 | 14/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.16× | +3.1 | 0.092 | 11/47 (RKO, A498, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.095 | 6/47 (HEC-1-A, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.366×** | -21.3 | 0e+00 | 39/48 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -19.9 | 0e+00 | 37/43 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.439×** | -17.4 | 0e+00 | 41/47 (C-33 A, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.449×** | -15.7 | 0e+00 | 34/43 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -15.3 | 0e+00 | 30/47 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -14.5 | 1e-45 | 38/46 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -14.2 | 1e-43 | 39/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -13.9 | 7e-42 | 37/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -13.6 | 2e-40 | 37/47 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -9.9 | 2e-21 | 34/47 (C32, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.433×** | -9.3 | 9e-19 | 39/46 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.686×** | -8.0 | 8e-14 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -7.8 | 3e-13 | 29/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -7.4 | 7e-12 | 29/47 (A549, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -7.3 | 9e-12 | 24/48 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.779×** | -5.1 | 1e-05 | 19/47 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.792×** | -4.9 | 2e-05 | 23/47 (BT-474, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.802×** | -4.7 | 8e-05 | 25/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.666×** | -4.5 | 2e-04 | 22/47 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -4.4 | 2e-04 | 20/47 (NCI-H1573, HCT15, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 245 | 0 | 15 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -18.6) |
| [[PANC-1 (line)]] | alt | 86.9 | 0 | 14 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 134 | 0 | 13 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -24.5) |
| [[LoVo (line)]] | wt | 373 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -17.7) |
| [[C32 (line)]] | wt | 117 | 0 | 10 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -15.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.252× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 174 | 4 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +24.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.377× (z -12.2) |
| [[HCT15 (line)]] | alt | 189 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -21.6) |
| [[NCI-H2030 (line)]] | alt | 233 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.7) |
| [[C-33 A (line)]] | alt | 99.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -23.6) |
| [[HS-578T (line)]] | alt | 172 | 6 (2 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 9.91× (z +23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.89× (z +20.3) | [[Auranofin (drug)]] 5 µM 0.326× (z -11.9) |
| [[J82 (line)]] | alt | 78.7 | 3 (1 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 5.41× (z +19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.4) | [[Auranofin (drug)]] 5 µM 0.382× (z -11.4) |
| [[A-427 (line)]] | wt | 68.8 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0669× (z -28.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.192× (z -26.8) |
| [[SW480 (line)]] | alt | 55.6 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.299× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -13.8) |
| [[A549 (line)]] | wt | 272 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -12.2) |
| [[HOP62 (line)]] | alt | 96.0 | 2 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 6.73× (z +22.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 78.2 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 244 | 1 (1 ⚠) | 6 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.53× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.9) |
| [[A498 (line)]] | wt | 103 | 2 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -8.9) |
| [[HT-29 (line)]] | alt | 114 | 2 | 4 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.50× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.9) |
| [[LS 180 (line)]] | wt | 182 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 420 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.2) |
| [[NCI-H2347 (line)]] | alt | 99.8 | 2 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.93× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.47× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.379× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 143 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.85× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0413× (z -31.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.425× (z -8.8) |
| [[A-172 (line)]] | wt | 87.6 | 2 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.22× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -8.8) |
| [[Hs 766T (line)]] | wt | 98.6 | 2 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.51× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 114 | 1 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.51× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -12.5) |
| [[SW 900 (line)]] | alt | 87.9 | 4 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 5.84× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.29× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.386× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.296× (z -10.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -17.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 88.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.439× (z -11.7) |
| [[KATO III (line)]] | alt | 55.9 | 1 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.88× (z +9.3) ⚠ cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 49.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.70× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.4× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 47.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.0) |
| [[RKO (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 60.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SHB]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[GPRC5A]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[FGD6]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SFR1]] | +0.54 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SAV1]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[IFNAR2]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SERPINB7]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PPP4R4]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NNT]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[GPX8]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NAXD]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ARFGEF1]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ALDH2]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[TMEM268]] | -0.45 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[CMPK1]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises TNFAIP8's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.82× lower at baseline in the lines without GPRC5A | 0.003 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[LAMA3]] | B | LAMA3 activity raises TNFAIP8's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without LAMA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[PTK6]] | B | PTK6 activity raises TNFAIP8's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without PTK6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[PHLDA2]] | B | PHLDA2 activity raises TNFAIP8's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without PHLDA2 | 0.008 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[PI3]] | B | PI3 activity raises TNFAIP8's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without PI3 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[ABTB2]] | B | ABTB2 activity raises TNFAIP8's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without ABTB2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[SH2D3A]] | B | SH2D3A activity raises TNFAIP8's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without SH2D3A | 0.026 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[IL1RN]] | B | IL1RN activity raises TNFAIP8's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without IL1RN | 0.028 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[ITGA2]] | B | ITGA2 activity raises TNFAIP8's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without ITGA2 | 0.030 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[LINC01589]] | B | LINC01589 activity raises TNFAIP8's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without LINC01589 | 0.034 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[CDCP1]] | B | CDCP1 activity raises TNFAIP8's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without CDCP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[LAMC2]] | B | LAMC2 activity raises TNFAIP8's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without LAMC2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.3, 1.9); signed map (2.0, 44.0). **Vector** length 139, 46.8% of its response variance represented; |z| ≥ 3 in 1,837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.8 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.0 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.5 | -17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.9 | -19.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.1 | -21.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.7 | -14.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.6 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.8 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | TNF alpha induced protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:119,268,692-119,399,688 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GG2-1, MDC-3.13, SCC-S2 |
| Gene groups (HGNC) | TIPE family |
| Hallmark sets | ANDROGEN_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: PI Metabolism; Phospholipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O95379](https://www.uniprot.org/uniprotkb/O95379) (Tumor necrosis factor alpha-induced protein 8):

> Acts as a negative mediator of apoptosis and may play a role in tumor progression. Suppresses the TNF-mediated apoptosis by inhibiting caspase-8 activity but not the processing of procaspase-8, subsequently resulting in inhibition of BID cleavage and caspase-3 activation.

**Summary**, from NCBI Gene [25816](https://www.ncbi.nlm.nih.gov/gene/25816):

> Enables cysteine-type endopeptidase inhibitor activity involved in apoptotic process. Involved in positive regulation of apoptotic process. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17260) · Entrez [25816](https://www.ncbi.nlm.nih.gov/gene/25816) · UniProt [O95379](https://www.uniprot.org/uniprotkb/O95379) · Ensembl [ENSG00000145779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145779)

## Data

Gene col 7024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7024); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7024]; `tensor/DDL_lfc|DDL_z.npy` [7024]; `embed/gene_vectors.npy` [7024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7024 or target_col == 7024). Every well: [[TNFAIP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFAIP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
