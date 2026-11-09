---
symbol: "NEPRO-AS1"
type: "gene"
col: 14223
ensembl_id: "ENSG00000240057"
name: "NEPRO antisense RNA 1"
location: "3q13.2"
module: 88
arm: "+"
pooled_cpm: 8.49
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# NEPRO-AS1

*NEPRO antisense RNA 1* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.21× (z +28.2, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.304× (z -14.3, q 8e-44, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST7L]] (+0.77, fdr 7e-06), [[KRCC1]] (+0.77, fdr 7e-06), [[LINC00486]] (+0.77, fdr 2e-05); moves opposite to [[SLC9A6]] (-0.75, fdr 1e-05), [[RPA1]] (-0.71, fdr 7e-06), [[GNB2]] (-0.70, fdr 3e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FJX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.21×** | +28.2 | 0e+00 | 40/41 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.95×** | +16.5 | 0e+00 | 39/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.79×** | +15.4 | 0e+00 | 36/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +8.1 | 1e-13 | 27/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +6.9 | 5e-10 | 24/45 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.3 | 1e-05 | 19/44 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +5.1 | 3e-05 | 14/44 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.9 | 0.008 | 3/14 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.16 | 5/45 (SW480, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.304×** | -14.3 | 8e-44 | 39/45 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.459×** | -9.4 | 2e-18 | 34/45 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.484×** | -8.7 | 5e-16 | 30/45 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -8.0 | 2e-13 | 27/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.519×** | -7.9 | 4e-13 | 24/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.496×** | -7.4 | 9e-12 | 26/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.543×** | -7.3 | 2e-11 | 25/44 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.563×** | -6.9 | 4e-10 | 25/40 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.606×** | -6.0 | 1e-07 | 21/41 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.413×** | -5.6 | 2e-06 | 21/45 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -5.5 | 2e-06 | 21/45 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.637×** | -5.2 | 9e-06 | 17/34 (J82, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -5.0 | 3e-05 | 19/39 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.630×** | -4.9 | 4e-05 | 15/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[NG25 (drug)]] 5 µM |  | **0.470×** | -4.7 | 8e-05 | 16/36 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -4.4 | 3e-04 | 15/43 (LOX-IMVI, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.743×** | -3.6 | 0.012 | 10/45 (NCI-H1792, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.2 | 2 | 11 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.165× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 7.38 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.0943× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.109× (z -13.1) |
| [[J82 (line)]] | alt | 19.8 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +12.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -11.1) |
| [[PANC-1 (line)]] | alt | 6.57 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.0263× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -12.1) |
| [[A-172 (line)]] | wt | 11.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +13.2) | [[Belinostat (drug)]] 5 µM 0.146× (z -10.0) |
| [[H4 (line)]] | wt | 12.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.0404× (z -11.6) |
| [[HOP62 (line)]] | alt | 15.4 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +19.4) | [[Belinostat (drug)]] 0.5 µM 0.216× (z -9.3) |
| [[A-427 (line)]] | wt | 4.23 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0647× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 19.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 3.09 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0803× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[HCT15 (line)]] | alt | 5.80 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.0278× (z -11.0) |
| [[HS-578T (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.42× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0366× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.20 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.0889× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 4.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +11.6) | — |
| [[C32 (line)]] | wt | 7.92 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0919× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 3.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +15.8) | — |
| [[HepG2_C3A (line)]] | wt | 7.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 6.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +9.6) | — |
| [[LoVo (line)]] | wt | 2.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.120× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 5.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 4.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.2) | — |
| [[SW48 (line)]] | wt | 8.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +8.7) | — |
| [[A498 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | +0.77 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.77 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.77 | +0.83 / +0.47 | both halves | 2e-05 |  |
| [[CYREN]] | +0.75 | +0.82 / +0.53 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | +0.75 | +0.76 / +0.46 | both halves | 2e-05 | same gene group |
| [[RAB30-DT]] | +0.75 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.75 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.73 | +0.74 / +0.61 | both halves | 7e-06 | same gene group |
| [[ANGPT2]] | +0.73 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[LZIC]] | +0.73 | +0.80 / +0.54 | both halves | 1e-05 |  |
| [[GABPB2]] | +0.72 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.71 | +0.78 / +0.50 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.75 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[RPA1]] | -0.71 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[GNB2]] | -0.70 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[IGSF8]] | -0.69 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.68 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.67 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.67 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.67 | -0.72 / -0.48 | both halves | 2e-05 |  |
| [[PPT2]] | -0.66 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.66 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[MYPOP]] | -0.66 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.66 | -0.75 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FJX1]] | B | FJX1 activity raises NEPRO-AS1's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without FJX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[LTBP2]] | B | LTBP2 activity raises NEPRO-AS1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without LTBP2 | 0.011 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ZC3H12C]] | B | ZC3H12C activity raises NEPRO-AS1's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without ZC3H12C | 0.012 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[CCDC102A]] | B | CCDC102A activity raises NEPRO-AS1's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without CCDC102A | 0.018 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent |
| [[ASAP3]] | B | ASAP3 activity raises NEPRO-AS1's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 2.53× lower at baseline in the lines without ASAP3 | 0.027 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[NALCN]] | B | NALCN activity raises NEPRO-AS1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without NALCN | 0.086 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[CD163L1]] | B | CD163L1 activity raises NEPRO-AS1's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without CD163L1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (5.4, 8.7); signed map (16.5, -25.3). **Vector** length 105, 24.3% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.2 | +28.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.6 | +16.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.1 | +15.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -14.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NEPRO antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q13.2 — chr3:113,019,468-113,184,377 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41049) · Entrez [102723430](https://www.ncbi.nlm.nih.gov/gene/102723430) · Ensembl [ENSG00000240057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240057)

## Data

Gene col 14223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14223); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14223]; `tensor/DDL_lfc|DDL_z.npy` [14223]; `embed/gene_vectors.npy` [14223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14223 or target_col == 14223). Every well: [[NEPRO-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEPRO-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
