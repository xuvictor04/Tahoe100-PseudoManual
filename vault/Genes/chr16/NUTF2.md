---
symbol: "NUTF2"
type: "gene"
col: 2286
ensembl_id: "ENSG00000102898"
name: "nuclear transport factor 2"
location: "16q22.1"
module: 11
arm: "-"
pooled_cpm: 37.42
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NUTF2

*nuclear transport factor 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.42× (z +18.7, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.58× (z +4.1, q 0.003, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.542× (z -10.9, q 9e-25, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHID1]] (+0.71, fdr 7e-06), [[COLGALT1]] (+0.69, fdr 7e-06), [[FAM20B]] (+0.68, fdr 7e-06); moves opposite to [[PPIG]] (-0.72, fdr 7e-06), [[CCDC174]] (-0.69, fdr 7e-06), [[LARP7]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.42×** | +18.7 | 0e+00 | 45/45 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.79×** | +16.1 | 0e+00 | 38/39 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +12.6 | 4e-34 | 42/44 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.5 | 5e-06 | 32/46 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.53×** | +5.2 | 3e-05 | 31/47 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.41×** | +4.4 | 0.001 | 28/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.2 | 0.002 | 16/33 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.003 | 25/48 (Panc 03.27, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.011 | 25/47 (SNU-1, CFPAC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.34×** | +3.7 | 0.012 | 27/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.32×** | +3.5 | 0.020 | 24/46 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +3.5 | 0.023 | 21/48 (SNU-423, A-172, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.030 | 23/48 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.079 | 18/48 (NCI-H1792, HOP62, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.079 | 15/48 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.086 | 19/48 (SK-MEL-2, NCI-H460, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.542×** | -10.9 | 9e-25 | 41/48 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.641×** | -5.4 | 2e-05 | 34/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.6 | 7e-04 | 29/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.7) |
| [[J82 (line)]] | alt | 48.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 38.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.5) |
| [[PANC-1 (line)]] | alt | 26.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.6) |
| [[A-172 (line)]] | wt | 27.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 49.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +14.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 39.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +13.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 33.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.25× (z +16.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 61.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 33.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +14.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 72.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 25.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 66.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.6) |
| [[SNU-423 (line)]] | alt | 27.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.49× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 58.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -13.1) |
| [[A-427 (line)]] | wt | 51.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.34× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.3) |
| [[C-33 A (line)]] | alt | 45.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.0) |
| [[C32 (line)]] | wt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +11.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 39.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 26.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +11.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 32.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +13.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.5) |
| [[SW 900 (line)]] | alt | 24.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.6) |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.0) |
| [[HCT15 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.69× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +13.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.7) |
| [[AN3 CA (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHID1]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PPT1]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[MDH2]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[HACD3]] | +0.64 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[RPSA]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SELENON]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[AHCY]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIG]] | -0.72 | -0.74 / -0.63 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[LARP7]] | -0.68 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[ZNF585A]] | -0.68 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.66 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[CLK4]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[MED18]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[RSF1]] | -0.65 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[GORAB]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[SCAF11]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.64 | -0.76 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.1, -26.1); signed map (-26.7, -41.6). **Vector** length 74.1, 17.6% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +18.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.5 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | +0.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.4 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.4 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transport factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,846,882-67,872,567 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTF2, PP15 |
| Matched by | ensembl_id |

**Function**, from UniProt [P61970](https://www.uniprot.org/uniprotkb/P61970) (Nuclear transport factor 2):

> Mediates the import of GDP-bound RAN from the cytoplasm into the nucleus which is essential for the function of RAN in cargo receptor-mediated nucleocytoplasmic transport. Thereby, plays indirectly a more general role in cargo receptor-mediated nucleocytoplasmic transport. Interacts with GDP-bound RAN in the cytosol, recruits it to the nuclear pore complex via its interaction with nucleoporins and promotes its nuclear import.

**Summary**, from NCBI Gene [10204](https://www.ncbi.nlm.nih.gov/gene/10204):

> This gene encodes a cytosolic factor that facilitates protein transport into the nucleus. The encoded protein is required for nuclear import of the small Ras-like GTPase, Ran which is involved in numerous cellular processes. This protein also interacts with the nuclear pore complex glycoprotein p62. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:13722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13722) · Entrez [10204](https://www.ncbi.nlm.nih.gov/gene/10204) · UniProt [P61970](https://www.uniprot.org/uniprotkb/P61970) · Ensembl [ENSG00000102898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102898)

## Data

Gene col 2286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2286); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2286]; `tensor/DDL_lfc|DDL_z.npy` [2286]; `embed/gene_vectors.npy` [2286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2286 or target_col == 2286). Every well: [[NUTF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUTF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
