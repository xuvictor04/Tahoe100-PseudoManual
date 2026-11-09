---
symbol: "FDFT1"
type: "gene"
col: 1258
ensembl_id: "ENSG00000079459"
name: "farnesyl-diphosphate farnesyltransferase 1"
location: "8p23.1"
module: 86
arm: "+"
pooled_cpm: 67.18
n_lines_expressing: 49
n_dd_up: 39
n_dd_down: 19
n_dd_up_clean: 31
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# FDFT1

*farnesyl-diphosphate farnesyltransferase 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 2.34× (z +16.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.639× (z -6.2, q 4e-07, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCR]] (+0.91, fdr 7e-06), [[MSMO1]] (+0.90, fdr 7e-06), [[SREBF2]] (+0.84, fdr 7e-06); moves opposite to [[TRMT5]] (-0.53, fdr 2e-05), [[RPL7L1]] (-0.52, fdr 2e-05), [[ANKRD18A]] (-0.50, fdr 7e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **2.34×** | +16.4 | 0e+00 | 45/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **2.22×** | +15.4 | 0e+00 | 46/47 (HOP62, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +14.1 | 1e-42 | 43/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.60×** | +13.1 | 4e-37 | 44/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +12.4 | 3e-33 | 43/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +11.6 | 3e-29 | 44/46 (C-33 A, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +7.6 | 2e-12 | 38/47 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +6.5 | 6e-09 | 38/47 (HS-578T, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +6.0 | 1e-07 | 32/47 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.34×** | +5.7 | 6e-07 | 38/47 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +5.7 | 6e-07 | 32/47 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +5.6 | 9e-07 | 29/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +5.5 | 1e-06 | 33/48 (HS-578T, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +5.4 | 3e-06 | 35/47 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 4e-06 | 37/46 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ritonavir (drug)]] 5 µM |  | **1.31×** | +5.2 | 8e-06 | 36/47 (LS 180, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.639×** | -6.2 | 4e-07 | 32/47 (A-427, RPMI-7951, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -5.8 | 2e-06 | 29/47 (RKO, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.653×** | -5.7 | 3e-06 | 31/47 (KATO III, BT-474, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.679×** | -5.4 | 1e-05 | 30/46 (KATO III, RKO, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -4.9 | 1e-04 | 28/47 (KATO III, LoVo, …) | inconsistent across doses | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | **0.788×** | -4.7 | 3e-04 | 28/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -4.2 | 0.002 | 23/47 (BT-474, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.810×** | -4.1 | 0.002 | 27/47 (LS 180, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.811×** | -4.1 | 0.002 | 25/47 (SK-MEL-2, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.726×** | -4.1 | 0.002 | 25/46 (A-427, RKO, …) | all doses, flat | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -3.8 | 0.007 | 23/46 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.772×** | -3.6 | 0.016 | 24/46 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.788×** | -3.3 | 0.041 | 19/48 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.789×** | -3.3 | 0.042 | 17/47 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.053 | 15/47 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.800×** | -3.0 | 0.094 | 16/48 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[Sapanisertib (drug)]] 5 µM |  | **0.665×** | -2.9 | 0.097 | 10/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 44.7 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 60.5 | 7 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.88× (z +11.9) | — |
| [[A498 (line)]] | wt | 54.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.94× (z +17.4) | — |
| [[A549 (line)]] | wt | 36.6 | 6 | 0 | [[Berbamine (drug)]] 5 µM 4.05× (z +14.3) | — |
| [[C-33 A (line)]] | alt | 80.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.91× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 62.7 | 6 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.06× (z +17.5) | — |
| [[HT-29 (line)]] | alt | 81.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.35× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 27.6 | 5 | 0 | [[Cepharanthine (drug)]] 5 µM 3.41× (z +10.1) | — |
| [[SW480 (line)]] | alt | 49.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.70× (z +16.2) | — |
| [[A-427 (line)]] | wt | 88.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.379× (z -9.2) |
| [[BT-474 (line)]] | alt | 166 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 69.7 | 3 | 0 | [[Berbamine (drug)]] 5 µM 2.49× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 140 | 3 | 0 | [[Berbamine (drug)]] 5 µM 3.77× (z +16.1) | — |
| [[NCI-H23 (line)]] | alt | 34.4 | 2 | 1 | [[Berbamine (drug)]] 5 µM 4.59× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 50.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +11.2) | — |
| [[RKO (line)]] | wt | 95.2 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0693× (z -21.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -16.0) |
| [[SNU-1 (line)]] | wt | 72.3 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.74× (z +11.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 61.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.93× (z +9.9) | — |
| [[C32 (line)]] | wt | 53.0 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 40.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.23× (z +8.8) | — |
| [[H4 (line)]] | wt | 29.1 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.02× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 108 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.72× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 69.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.14× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.5) |
| [[HOP62 (line)]] | alt | 33.1 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.70× (z +17.1) | — |
| [[Hs 766T (line)]] | wt | 52.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 96.6 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.26× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.11× (z +10.0) | — |
| [[J82 (line)]] | alt | 35.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Berbamine (drug)]] 5 µM 2.28× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 69.2 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.91× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 48.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 97.9 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +8.8) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.7) |
| [[SW1417 (line)]] | alt | 58.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0943× (z -11.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[COLO 205 (line)]] | alt | 91.4 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.57× (z +9.0) | — |
| [[KATO III (line)]] | alt | 240 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -9.4) |
| [[SW 900 (line)]] | alt | 50.6 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.74× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 75.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCR]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 954 |
| [[MSMO1]] | +0.90 | +0.90 / +0.86 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 991 |
| [[SREBF2]] | +0.84 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 888 |
| [[FDPS]] | +0.83 | +0.86 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 995 |
| [[MVD]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 873 |
| [[DHCR7]] | +0.83 | +0.83 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 938 |
| [[ERG28]] | +0.82 | +0.83 / +0.72 | both halves | 7e-06 | STRING 984 |
| [[ACSS2]] | +0.81 | +0.82 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 569 |
| [[SCD]] | +0.81 | +0.87 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 609 |
| [[SQLE]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 999 |
| [[INSIG1]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 774 |
| [[IDI1]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 940 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RPL7L1]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD18A]] | -0.50 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[CLHC1]] | -0.49 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ST7L]] | -0.49 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[TRMT13]] | -0.48 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[GPATCH4]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZC3HC1]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[METTL6]] | -0.48 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ITPA]] | -0.48 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ZNF518A]] | -0.47 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[TAF2]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.915). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -49.0); signed map (-52.9, 32.3). **Vector** length 153, 56.4% of its response variance represented; |z| ≥ 3 in 1,569 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.68 to 19); *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.72 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.72 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +11.9 | +15.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +10.7 | +16.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.8 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.9 | +12.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +6.8 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.8 | +4.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +5.5 | +5.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.2 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.5 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | farnesyl-diphosphate farnesyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:11,795,573-11,839,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SQS |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 10 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [P37268](https://www.uniprot.org/uniprotkb/P37268) (Squalene synthase):

> Catalyzes the condensation of 2 farnesyl pyrophosphate (FPP) moieties to form squalene. Proceeds in two distinct steps. In the first half-reaction, two molecules of FPP react to form the stable presqualene diphosphate intermediate (PSQPP), with concomitant release of a proton and a molecule of inorganic diphosphate. In the second half-reaction, PSQPP undergoes heterolysis, isomerization, and reduction with NADPH or NADH to form squalene. It is the first committed enzyme of the sterol …

**Summary**, from NCBI Gene [2222](https://www.ncbi.nlm.nih.gov/gene/2222):

> This gene encodes a membrane-associated enzyme located at a branch point in the mevalonate pathway. The encoded protein is the first specific enzyme in cholesterol biosynthesis, catalyzing the dimerization of two molecules of farnesyl diphosphate in a two-step reaction to form squalene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3629) · Entrez [2222](https://www.ncbi.nlm.nih.gov/gene/2222) · UniProt [P37268](https://www.uniprot.org/uniprotkb/P37268) · Ensembl [ENSG00000079459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079459)

## Data

Gene col 1258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1258); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1258]; `tensor/DDL_lfc|DDL_z.npy` [1258]; `embed/gene_vectors.npy` [1258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1258 or target_col == 1258). Every well: [[FDFT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FDFT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
