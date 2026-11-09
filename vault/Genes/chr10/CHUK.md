---
symbol: "CHUK"
type: "gene"
col: 13097
ensembl_id: "ENSG00000213341"
name: "component of inhibitor of nuclear factor kappa B kinase complex"
location: "10q24.31"
module: 36
arm: "+"
pooled_cpm: 37.68
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# CHUK

*component of inhibitor of nuclear factor kappa B kinase complex* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.17× (z +17.8, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[4EGI-1 (drug)]] 5 µM: 0.666× (z -4.0, q 0.034, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC10]] (+0.68, fdr 7e-06), [[ZNF410]] (+0.65, fdr 7e-06), [[AREL1]] (+0.65, fdr 7e-06); moves opposite to [[FNIP1]] (-0.59, fdr 1e-05), [[ZNF638]] (-0.58, fdr 3e-05), [[RSF1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IRAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.17×** | +17.8 | 0e+00 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.38×** | +16.2 | 0e+00 | 46/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.30×** | +15.6 | 0e+00 | 46/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.22×** | +14.9 | 0e+00 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +14.1 | 6e-43 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.96×** | +12.6 | 3e-34 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +12.3 | 7e-33 | 40/48 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +11.7 | 1e-29 | 43/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.04×** | +10.9 | 1e-25 | 38/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +10.3 | 6e-23 | 42/48 (SW480, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.71×** | +9.7 | 2e-20 | 40/47 (SW480, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.63×** | +9.1 | 3e-18 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +9.0 | 1e-17 | 40/48 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +8.7 | 1e-16 | 36/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.38×** | +8.5 | 6e-16 | 34/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +8.4 | 1e-15 | 38/47 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +8.0 | 5e-14 | 37/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +6.3 | 1e-08 | 30/48 (HCT15, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 6e-06 | 28/48 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 1e-05 | 24/48 (HOP62, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.1 | 8e-04 | 17/48 (A-172, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.004 | 11/48 (SNU-423, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13097.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[4EGI-1 (drug)]] 5 µM |  | **0.666×** | -4.0 | 0.034 | 15/47 (SHP-77, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.753×** | -3.8 | 0.036 | 19/48 (HCT15, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.825×** | -3.7 | 0.047 | 16/48 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.087 | 15/47 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 0.850× | -3.1 | 0.20 | 16/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.853× | -3.0 | 0.20 | 11/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.854× | -3.0 | 0.20 | 6/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 40.6 | 15 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +17.3) | — |
| [[LoVo (line)]] | wt | 34.6 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 25.4 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.05× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 51.1 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +13.0) | — |
| [[KATO III (line)]] | alt | 24.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 43.3 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.08× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.71× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 30.5 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.17× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 30.0 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.74× (z +10.0) | — |
| [[RKO (line)]] | wt | 43.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 39.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 34.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 65.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +8.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 28.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 37.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.29× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.30× (z +8.7) | — |
| [[A-172 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC10]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ZNF410]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[AREL1]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[STIMATE]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[NUP93]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[PLAA]] | +0.60 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[STRAP]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PSMD1]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Activation of NF-kappaB in B cells |
| [[NUDT5]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TIMM23]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DGCR8]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNIP1]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZNF638]] | -0.58 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[RSF1]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SNAPC1]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.55 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[MITD1]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[WASHC4]] | -0.53 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[NBPF19]] | -0.53 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[BTG1]] | -0.52 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[BET1]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | B | IRAG2 activity lowers CHUK's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.24× higher at baseline in the lines without IRAG2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-11.1, -16.3); signed map (-44.5, -23.0). **Vector** length 65.9, 15.0% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +17.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.7 | +9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +2.7 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +10.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.1 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -3.1 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.5 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | component of inhibitor of nuclear factor kappa B kinase complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,188,300-100,229,596 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IKK1, IKK-alpha, IkBKA, NFKBIKA, IKKA; previously TCF16 |
| Gene groups (HGNC) | I kappa B kinase family; IKK complex |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 83 pathways, smallest: IKBKB deficiency causes SCID; IKBKG deficiency causes anhidrotic ectodermal dysplasia with immunodeficiency (EDA-ID) (via TLR); SLC15A4:TASL-dependent IRF5 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15111](https://www.uniprot.org/uniprotkb/O15111) (Inhibitor of nuclear factor kappa-B kinase subunit alpha):

> Serine kinase that plays an essential role in the NF-kappa-B signaling pathway which is activated by multiple stimuli such as inflammatory cytokines, bacterial or viral products, DNA damages or other cellular stresses. Acts as a part of the canonical IKK complex in the conventional pathway of NF-kappa-B activation and phosphorylates inhibitors of NF-kappa-B on serine residues. These modifications allow polyubiquitination of the inhibitors and subsequent degradation by the proteasome. In turn, …

**Summary**, from NCBI Gene [1147](https://www.ncbi.nlm.nih.gov/gene/1147):

> This gene encodes a member of the serine/threonine protein kinase family. The encoded protein, a component of a cytokine-activated protein complex that is an inhibitor of the essential transcription factor NF-kappa-B complex, phosphorylates sites that trigger the degradation of the inhibitor via the ubiquination pathway, thereby activating the transcription factor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1974) · Entrez [1147](https://www.ncbi.nlm.nih.gov/gene/1147) · UniProt [O15111](https://www.uniprot.org/uniprotkb/O15111) · Ensembl [ENSG00000213341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213341)

## Data

Gene col 13097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13097); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13097]; `tensor/DDL_lfc|DDL_z.npy` [13097]; `embed/gene_vectors.npy` [13097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13097 or target_col == 13097). Every well: [[CHUK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHUK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
