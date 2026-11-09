---
symbol: "FAM91A1"
type: "gene"
col: 10757
ensembl_id: "ENSG00000176853"
name: "family with sequence similarity 91 member A1"
location: "8q24.13"
module: 20
arm: "+"
pooled_cpm: 122.84
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# FAM91A1

*family with sequence similarity 91 member A1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.13× (z +13.9, q 7e-41, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.172×, SNU-1 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.461×; ⚠ cell-cycle shift, explains ~66% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.436×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED7]] (+0.71, fdr 1e-05), [[MMGT1]] (+0.70, fdr 1e-05), [[TMEM30A]] (+0.69, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.67, fdr 7e-06), [[FOXA2]] (-0.66, fdr 2e-05), [[SUMO4]] (-0.64, fdr 7e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM171A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +13.9 | 7e-41 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +11.4 | 2e-27 | 46/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.80×** | +10.8 | 8e-25 | 44/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +9.4 | 9e-19 | 41/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +9.3 | 1e-18 | 44/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.2 | 4e-18 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 4e-15 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +7.5 | 4e-12 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +7.3 | 2e-11 | 40/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.9 | 2e-07 | 32/48 (HT-29, HCT15, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.6 | 1e-06 | 33/47 (C-33 A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.5 | 1e-06 | 37/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.4 | 2e-06 | 34/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 2e-06 | 30/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +4.7 | 9e-05 | 34/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 5e-04 | 31/48 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.006 | 29/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.016 | 24/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.13× | +3.1 | 0.040 | 4/48 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.057 | 16/48 (SW1417, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.18× | +2.8 | 0.096 | 11/48 (HT-29, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10757.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.172×, SNU-1 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.461×; ⚠ cell-cycle shift, explains ~66% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.436×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | 0.818× | -3.7 | 0.13 | 23/48 (NCI-H1573, SNU-1, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.40 | 20/48 (SW 1271, SW48, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.781× | -3.0 | 0.40 | 23/48 (NCI-H1792, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 94.7 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 69.7 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 87.1 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 107 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +12.2) | — |
| [[LoVo (line)]] | wt | 104 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 143 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 117 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +16.6) | — |
| [[SNU-1 (line)]] | wt | 276 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 158 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 73.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.61× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 126 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 148 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.18× (z +8.7) | — |
| [[A-172 (line)]] | wt | 60.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 120 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +9.2) | — |
| [[C32 (line)]] | wt | 158 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 349 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 86.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 155 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +10.9) | — |
| [[A498 (line)]] | wt | 175 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 78.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 193 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.3) | — |
| [[KATO III (line)]] | alt | 121 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 80.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 124 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.8) | — |
| [[RKO (line)]] | wt | 315 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 111 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 172 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[SW48 (line)]] | wt | 95.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +9.0) | — |
| [[A-427 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED7]] | +0.71 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.70 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[TMEM30A]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[SPTLC1]] | +0.66 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[PABIR2]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.63 | +0.38 / +0.73 | both halves | 7e-05 |  |
| [[ARF3]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TMX1]] | +0.62 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[AGO1]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FKBP1A]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[EDEM1]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.67 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[FOXA2]] | -0.66 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[SUMO4]] | -0.64 | -0.37 / -0.60 | both halves | 7e-05 |  |
| [[MPHOSPH8]] | -0.63 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[TOPORS]] | -0.62 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[THAP3]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[EID2]] | -0.62 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[PPIG]] | -0.62 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[COIL]] | -0.62 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[IRX5]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[TMEM70]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.61 | -0.49 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM171A1]] | B | FAM171A1 activity lowers FAM91A1's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 1.60× higher at baseline in the lines without FAM171A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.9, -22.5); signed map (-24.7, -39.1). **Vector** length 70.5, 18.2% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +5.2 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.1 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 91 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,768,439-123,815,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23790 |
| Reactome | 4 pathways, smallest: RHOH GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q658Y4](https://www.uniprot.org/uniprotkb/Q658Y4) (Protein FAM91A1):

> As component of the WDR11 complex acts together with TBC1D23 to facilitate the golgin-mediated capture of vesicles generated using AP-1.

**Summary**, from NCBI Gene [157769](https://www.ncbi.nlm.nih.gov/gene/157769):

> Involved in intracellular protein transport and vesicle tethering to Golgi. Located in cytoplasmic vesicle and trans-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26306) · Entrez [157769](https://www.ncbi.nlm.nih.gov/gene/157769) · UniProt [Q658Y4](https://www.uniprot.org/uniprotkb/Q658Y4) · Ensembl [ENSG00000176853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176853)

## Data

Gene col 10757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10757); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10757]; `tensor/DDL_lfc|DDL_z.npy` [10757]; `embed/gene_vectors.npy` [10757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10757 or target_col == 10757). Every well: [[FAM91A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM91A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
