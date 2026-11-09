---
symbol: "USP39"
type: "gene"
col: 9714
ensembl_id: "ENSG00000168883"
name: "ubiquitin specific peptidase 39"
location: "2p11.2"
module: 25
arm: "+"
pooled_cpm: 28.13
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# USP39

*ubiquitin specific peptidase 39* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +21.9, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cyclosporin A (drug)]] 0.5 µM in 1 line (NCI-H661 0.0704×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX16]] (+0.69, fdr 1e-05), [[GOT2]] (+0.67, fdr 7e-06), [[USP5]] (+0.66, fdr 1e-05); moves opposite to [[SLC25A4]] (-0.68, fdr 3e-05), [[RPL36AL]] (-0.65, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[BTG1]] (-0.65, fdr 1e-05), [[LAMTOR5]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +21.9 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.55×** | +21.2 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.46×** | +20.3 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.40×** | +19.8 | 0e+00 | 40/43 (SW480, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.34×** | +19.2 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.15×** | +17.3 | 0e+00 | 42/47 (HOP62, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +17.3 | 0e+00 | 37/47 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.10×** | +16.1 | 0e+00 | 28/38 (SW480, LoVo, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.11×** | +15.6 | 0e+00 | 37/42 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +15.1 | 0e+00 | 43/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +15.0 | 0e+00 | 44/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +15.0 | 0e+00 | 44/48 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.93×** | +14.9 | 0e+00 | 43/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +12.9 | 2e-36 | 42/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +11.6 | 1e-29 | 37/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +10.8 | 1e-25 | 38/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +9.3 | 5e-19 | 33/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +8.6 | 1e-16 | 33/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 2e-05 | 17/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.6 | 6e-05 | 11/48 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 1e-04 | 14/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cyclosporin A (drug)]] 0.5 µM in 1 line (NCI-H661 0.0704×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -6.7 | 1e-08 | 3/48 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.839× | -4.0 | 0.019 | 16/47 (SW 1271, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.812× | -3.4 | 0.11 | 13/48 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.863× | -3.3 | 0.11 | 8/48 (HCT15, NCI-H23, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 0.867× | -3.3 | 0.11 | 5/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | 0.761× | -3.2 | 0.11 | 6/48 (HCT15, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.15 | 9/47 (SW 1271, HS-578T, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.1 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.8) | — |
| [[LoVo (line)]] | wt | 22.5 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 20.4 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.88× (z +13.4) | — |
| [[SW480 (line)]] | alt | 38.6 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.19× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.59× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 26.4 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.2) | — |
| [[A549 (line)]] | wt | 24.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 22.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.4) | — |
| [[A-172 (line)]] | wt | 29.8 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.38× (z +11.1) | — |
| [[KATO III (line)]] | alt | 29.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A498 (line)]] | wt | 35.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.79× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 18.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.9) | — |
| [[C32 (line)]] | wt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 23.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.96× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 45.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 40.7 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0704× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.81× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW48 (line)]] | wt | 36.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.41× (z +9.1) | — |
| [[A-427 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX16]] | +0.69 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[GOT2]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[USP5]] | +0.66 | +0.49 / +0.63 | both halves | 1e-05 | same gene group; STRING 772 |
| [[API5]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[MFN2]] | +0.65 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.62 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[ATL3]] | +0.62 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.61 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[NUP155]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MCM3AP]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[EMC1]] | +0.60 | +0.30 / +0.65 | both halves | 2e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A4]] | -0.68 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.65 | -0.52 / -0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BTG1]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.62 | -0.46 / -0.70 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.61 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.60 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[IFI27L2]] | -0.58 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[TMEM258]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | -0.58 | -0.47 / -0.61 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IMP3]] | -0.58 | -0.28 / -0.68 | both halves | 3e-04 |  |
| [[CNNM4]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PIM2]] | -0.57 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[KRTCAP2]] | -0.57 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[C19orf81]] | -0.56 | -0.37 / -0.60 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises USP39's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without HES6 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FRMD3]] | B | FRMD3 activity lowers USP39's level | lines that do not express FRMD3 (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without FRMD3 | 0.047 | ⚠ within organs, on part of the lines; also absent: SSUH2, CACNG2, ZMIZ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-36.0, -27.1); signed map (-15.3, -43.4). **Vector** length 59.6, 12.0% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.3 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +5.2 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.0 | +15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +17.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +15.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +12.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +2.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -2.1 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.4 | +11.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.1 | +3.3 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.0 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,602,856-85,649,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAD1, CGI-21, SNRNP65 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; tri-snRP complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GS9](https://www.uniprot.org/uniprotkb/Q53GS9) (Ubiquitin carboxyl-terminal hydrolase 39):

> Deubiquitinating enzyme that plays a role in many cellular processes including cellular antiviral response, epithelial morphogenesis, DNA repair or B-cell development. Plays a role in pre-mRNA splicing as a component of the U4/U6-U5 tri-snRNP, one of the building blocks of the precatalytic spliceosome. Specifically regulates immunoglobulin gene rearrangement in a spliceosome-dependent manner, which involves modulating chromatin interactions at the Igh locus and therefore plays an essential role …

**Summary**, from NCBI Gene [10713](https://www.ncbi.nlm.nih.gov/gene/10713):

> Predicted to enable cysteine-type deubiquitinase activity and zinc ion binding activity. Involved in spliceosomal complex assembly. Located in nucleoplasm. Part of U4/U6 x U5 tri-snRNP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20071) · Entrez [10713](https://www.ncbi.nlm.nih.gov/gene/10713) · UniProt [Q53GS9](https://www.uniprot.org/uniprotkb/Q53GS9) · Ensembl [ENSG00000168883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168883)

## Data

Gene col 9714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9714); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9714]; `tensor/DDL_lfc|DDL_z.npy` [9714]; `embed/gene_vectors.npy` [9714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9714 or target_col == 9714). Every well: [[USP39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
