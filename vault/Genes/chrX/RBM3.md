---
symbol: "RBM3"
type: "gene"
col: 2239
ensembl_id: "ENSG00000102317"
name: "RNA binding motif protein 3"
location: "Xp11.23"
module: 23
arm: "+"
pooled_cpm: 92.4
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RBM3

*RNA binding motif protein 3* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.28× (z +18.0, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.90× (z +6.6, q 4e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.648× (z -4.4, q 0.005, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGDH-AS1]] (+0.65, fdr 1e-05), [[PCBP2]] (+0.62, fdr 1e-05), [[SOX2-OT]] (+0.60, fdr 2e-05); moves opposite to [[POLR3K]] (-0.61, fdr 9e-05), [[POP5]] (-0.60, fdr 4e-04), [[MRPL17]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DPF1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.28×** | +18.0 | 0e+00 | 49/49 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.36×** | +14.8 | 0e+00 | 43/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.93×** | +13.0 | 1e-36 | 43/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +6.6 | 4e-09 | 38/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.88×** | +6.5 | 7e-09 | 45/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +5.7 | 1e-06 | 44/47 (COLO 205, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.73×** | +5.7 | 1e-06 | 43/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.56×** | +4.6 | 3e-04 | 40/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.4 | 6e-04 | 30/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.005 | 25/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.011 | 31/48 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.6 | 0.013 | 24/38 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.95×** | +3.6 | 0.013 | 38/49 (NCI-H2030, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.40×** | +3.5 | 0.017 | 29/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.36×** | +3.2 | 0.049 | 26/48 (NCI-H1573, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.648×** | -4.4 | 0.005 | 36/48 (hTERT-HPNE, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -4.1 | 0.010 | 44/48 (RKO, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.677×** | -4.0 | 0.013 | 35/48 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.711×** | -3.5 | 0.068 | 36/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.731× | -3.2 | 0.16 | 31/48 (A-172, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 102 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.0 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.53× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 63.4 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +13.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 49.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 177 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.62× (z +17.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 66.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.55× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.52× (z +9.6) | — |
| [[C32 (line)]] | wt | 45.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.88× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 69.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.81× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 123 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +15.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 117 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 104 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +9.1) | — |
| [[A-427 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +14.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 45.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 128 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.00× (z +16.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 81.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.47× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 85.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 81.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 59.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.48× (z +13.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 95.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +14.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 68.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +14.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 114 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 64.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +13.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 92.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +14.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 86.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +14.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +16.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 59.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +14.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 66.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.77× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 74.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 143 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +16.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 53.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +13.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 43.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +15.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 52.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +13.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 79.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +13.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 79.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Glasdegib (drug)]] 5 µM 0.0815× (z -8.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 70.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +11.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGDH-AS1]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PCBP2]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 | STRING 539 |
| [[SOX2-OT]] | +0.60 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[COPB2-DT]] | +0.60 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[MGAM]] | +0.59 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CHD1-DT]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.57 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ZRANB2-DT]] | +0.57 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[HEXIM2-AS1]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MAILR]] | +0.56 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[CSDE1]] | +0.56 | +0.36 / +0.55 | both halves | 9e-05 | STRING 416 |
| [[PSMD7-DT]] | +0.56 | +0.48 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3K]] | -0.61 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[POP5]] | -0.60 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[MRPL17]] | -0.57 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[AARS2]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[DPF1]] | -0.54 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[PWP2]] | -0.54 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MAP1S]] | -0.52 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[BAK1]] | -0.52 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[EXOSC4]] | -0.51 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[RGS19]] | -0.51 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[WRAP73]] | -0.51 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[LBHD1]] | -0.51 | -0.06 / -0.59 | ⚠ one half (not replicated) | 0.004 |  |
| [[CBR1]] | -0.50 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPF1]] | C | DPF1 activity raises RBM3's level | lines that do not express DPF1 (4) vs lines expressing it (46) | 1.19× lower at baseline in the lines without DPF1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (7.6, 18.5); signed map (29.4, -8.1). **Vector** length 82.7, 27.8% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | -0.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.9 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | -0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.3 | +0.9 |
|  | [[vincristine (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,574,449-48,581,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IS1-RNPL |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P98179](https://www.uniprot.org/uniprotkb/P98179) (RNA-binding protein 3):

> Cold-inducible mRNA binding protein that enhances global protein synthesis at both physiological and mild hypothermic temperatures. Reduces the relative abundance of microRNAs, when overexpressed. Enhances phosphorylation of translation initiation factors and active polysome formation (By similarity).

**Summary**, from NCBI Gene [5935](https://www.ncbi.nlm.nih.gov/gene/5935):

> This gene is a member of the glycine-rich RNA-binding protein family and encodes a protein with one RNA recognition motif (RRM) domain. Expression of this gene is induced by cold shock and low oxygen tension. A pseudogene exists on chromosome 1. Multiple alternatively spliced transcript variants that are predicted to encode different isoforms have been characterized although some of these variants fit nonsense-mediated decay (NMD) criteria. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9900) · Entrez [5935](https://www.ncbi.nlm.nih.gov/gene/5935) · UniProt [P98179](https://www.uniprot.org/uniprotkb/P98179) · Ensembl [ENSG00000102317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102317)

## Data

Gene col 2239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2239); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2239]; `tensor/DDL_lfc|DDL_z.npy` [2239]; `embed/gene_vectors.npy` [2239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2239 or target_col == 2239). Every well: [[RBM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
