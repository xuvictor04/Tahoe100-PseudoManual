---
symbol: "HSPA4L"
type: "gene"
col: 8854
ensembl_id: "ENSG00000164070"
name: "heat shock protein family A (Hsp70) member 4 like"
location: "4q28.1"
module: 94
arm: "+"
pooled_cpm: 46.19
n_lines_expressing: 48
n_dd_up: 48
n_dd_down: 12
n_dd_up_clean: 33
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# HSPA4L

*heat shock protein family A (Hsp70) member 4 like* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.25× (z +34.1, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.738× (z -5.1, q 2e-04, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPDR1]] (+0.66, fdr 1e-05), [[XPO1]] (+0.63, fdr 7e-06), [[NUDT9]] (+0.60, fdr 7e-06); moves opposite to [[ZMYND19]] (-0.56, fdr 2e-05), [[AXIN1]] (-0.52, fdr 1e-05), [[ANKMY1]] (-0.51, fdr 5e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 20 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.25×** | +34.1 | 0e+00 | 46/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.05×** | +27.0 | 0e+00 | 46/46 (HT-29, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **3.01×** | +26.0 | 0e+00 | 46/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.51×** | +24.2 | 0e+00 | 46/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **3.17×** | +19.3 | 0e+00 | 45/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.30×** | +18.8 | 0e+00 | 45/46 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.86×** | +17.5 | 0e+00 | 46/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.65×** | +16.3 | 0e+00 | 40/45 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +15.7 | 0e+00 | 38/46 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.53×** | +15.4 | 0e+00 | 41/46 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.42×** | +14.7 | 0e+00 | 39/46 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +14.1 | 2e-43 | 42/46 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.75×** | +13.6 | 2e-40 | 40/41 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.06×** | +12.1 | 5e-32 | 44/45 (C-33 A, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.60×** | +11.4 | 2e-28 | 40/46 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +10.5 | 4e-24 | 37/47 (A498, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.738×** | -5.1 | 2e-04 | 24/45 (RKO, SW48, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.771×** | -4.2 | 0.006 | 18/45 (H4, RKO, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.779×** | -4.2 | 0.006 | 22/46 (Panc 03.27, C32, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.782×** | -3.9 | 0.015 | 16/46 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.803×** | -3.7 | 0.028 | 19/45 (SW 1271, PANC-1, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.683×** | -3.3 | 0.073 | 10/46 (LS 180, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.3 | 0.073 | 1/47 (SW 1088) | inconsistent across doses |  |
| [[Erythromycin (drug)]] 5 µM |  | **0.824×** | -3.2 | 0.085 | 7/46 (SW 1088, RPMI-7951, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.768×** | -3.2 | 0.087 | 6/46 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.697×** | -3.1 | 0.087 | 15/45 (NCI-H23, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.829×** | -3.1 | 0.087 | 16/46 (SW48, A549, …) | two highest doses |  |
| [[DTP3 (drug)]] 5 µM |  | **0.702×** | -3.1 | 0.093 | 8/44 (C-33 A, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.093 | 11/45 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.7 | 18 (4 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.72× (z +18.9) | — |
| [[A498 (line)]] | wt | 63.2 | 15 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +16.1) | — |
| [[RKO (line)]] | wt | 113 | 13 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 9.16× (z +23.1) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 51.4 | 13 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 16.8× (z +24.9) | — |
| [[SW480 (line)]] | alt | 52.8 | 12 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.92× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 36.3 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +25.3) | — |
| [[NCI-H2347 (line)]] | alt | 55.1 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +25.2) | — |
| [[LS 180 (line)]] | wt | 123 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +17.2) | — |
| [[PANC-1 (line)]] | alt | 68.9 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +27.3) | — |
| [[SW1417 (line)]] | alt | 18.0 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +20.4) | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +20.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +17.1) | — |
| [[HS-578T (line)]] | alt | 28.8 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +15.8) | — |
| [[LoVo (line)]] | wt | 60.0 | 9 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 8.62× (z +18.8) | — |
| [[A-427 (line)]] | wt | 62.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +18.2) | — |
| [[A549 (line)]] | wt | 38.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 12.3 | 8 | 0 | [[Auranofin (drug)]] 5 µM 29.7× (z +17.8) | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +15.1) | — |
| [[SW48 (line)]] | wt | 102 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +19.5) | — |
| [[A-172 (line)]] | wt | 37.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 86.2 | 6 | 0 | [[Auranofin (drug)]] 5 µM 6.84× (z +16.5) | — |
| [[J82 (line)]] | alt | 53.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +16.9) | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 6 | 0 | [[Selinexor (drug)]] 5 µM 7.58× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 6 | 0 | [[Selinexor (drug)]] 5 µM 5.17× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 5 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.72× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[C32 (line)]] | wt | 46.0 | 5 | 0 | [[Auranofin (drug)]] 5 µM 9.64× (z +17.2) | — |
| [[COLO 205 (line)]] | alt | 28.0 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.20× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 50.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 40.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +23.8) | — |
| [[H4 (line)]] | wt | 22.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 34.6 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.66× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 162 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.43× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 27.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +16.0) | — |
| [[SW 900 (line)]] | alt | 42.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +17.3) | — |
| [[HCT15 (line)]] | alt | 69.1 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 3.75× (z +9.6) | [[Sonidegib (drug)]] 5 µM 0.0766× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 38.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 54.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.29× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 29.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.49× (z +14.2) | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPDR1]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[XPO1]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NUDT9]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RNF150]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ANKEF1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DUSP15]] | +0.59 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TYW3]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.57 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PHYH]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[BLOC1S2]] | +0.56 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[CCDC43]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[RBM41]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[AXIN1]] | -0.52 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ANKMY1]] | -0.51 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[MAPKAPK2]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 | pathway: Cellular response to heat stress |
| [[CRYGS]] | -0.51 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[IL9RP3]] | -0.50 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[GRK6]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MXD3]] | -0.48 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[VKORC1L1]] | -0.48 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.47 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[USP20]] | -0.47 | -0.19 / -0.42 | ⚠ not reproduced | 8e-04 |  |
| [[CMC2]] | -0.47 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TMEM104]] | -0.46 | -0.48 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAP2]] | B | CAP2 activity strengthens HSPA4L's drug response | lines that do not express CAP2 (6) vs lines expressing it (40) | the lines without CAP2 respond 0.93× as strongly (z diff +0.08); strongest at Homoharringtonine 0.5 µM: 1.26x vs 2.72x (z diff +4.4) | 0.090 | ⚠ within organs, on part of the lines; also absent: SCML2, ADORA1, ASAP3; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.0, 23.8); signed map (8.0, -33.4). **Vector** length 125, 42.6% of its response variance represented; |z| ≥ 3 in 1,743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +17.8 | +26.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +12.8 | +19.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.9 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.3 | +27.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +15.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.7 | +12.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.9 | +9.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.2 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.1 | +9.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 4 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:127,781,821-127,840,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APG-1, Osp94, HSPH3 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | SPERMATOGENESIS, ESTROGEN_RESPONSE_LATE, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O95757](https://www.uniprot.org/uniprotkb/O95757) (Heat shock 70 kDa protein 4L):

> Possesses chaperone activity in vitro where it inhibits aggregation of citrate synthase.

**Summary**, from NCBI Gene [22824](https://www.ncbi.nlm.nih.gov/gene/22824):

> The protein encoded by this gene is heat shock inducible and may act as a chaperone. The encoded protein can protect the heat-shocked cell against the harmful effects of aggregated proteins. This gene is highly expressed in leukemia cells and may be a good target for therapeutic intervention. Several transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:17041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17041) · Entrez [22824](https://www.ncbi.nlm.nih.gov/gene/22824) · UniProt [O95757](https://www.uniprot.org/uniprotkb/O95757) · Ensembl [ENSG00000164070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164070)

## Data

Gene col 8854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8854); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8854]; `tensor/DDL_lfc|DDL_z.npy` [8854]; `embed/gene_vectors.npy` [8854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8854 or target_col == 8854). Every well: [[HSPA4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
