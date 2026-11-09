---
symbol: "GATA2-AS1"
type: "gene"
col: 14400
ensembl_id: "ENSG00000244300"
name: "GATA2 antisense RNA 1"
location: "3q21.3"
module: 46
arm: "+"
pooled_cpm: 13.9
n_lines_expressing: 40
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# GATA2-AS1

*GATA2 antisense RNA 1* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +15.7, q 0e+00, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.519× (z -12.9, q 2e-35, down in 29 of 36 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.463× (z -10.7, q 2e-24, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN7L3-AS1]] (+0.66, fdr 2e-04), [[POU6F1]] (+0.63, fdr 8e-05), [[SETD1B]] (+0.62, fdr 4e-05); moves opposite to [[INTS13]] (-0.56, fdr 1e-04), [[TTC26]] (-0.54, fdr 1e-04), [[POT1]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[ATG4C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +15.7 | 0e+00 | 31/37 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.7 | 4e-12 | 14/20 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +5.4 | 1e-05 | 13/25 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.8 | 3e-04 | 13/37 (HS-578T, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 5e-04 | 10/38 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.1 | 0.003 | 12/32 (H4, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.004 | 13/38 (SHP-77, PANC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.012 | 9/38 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.019 | 14/38 (NCI-H1573, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.056 | 9/38 (HS-578T, CHP-212, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.26×** | +3.3 | 0.056 | 7/38 (C-33 A, SHP-77, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.087 | 8/38 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.11 | 7/38 (LoVo, J82, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.519×** | -12.9 | 2e-35 | 29/36 (BT-474, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.463×** | -10.7 | 2e-24 | 32/38 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.483×** | -10.1 | 7e-22 | 29/38 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.528×** | -8.9 | 8e-17 | 25/38 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -8.2 | 2e-14 | 24/36 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.553×** | -7.9 | 2e-13 | 23/38 (SW480, NCI-H23, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -6.4 | 2e-08 | 19/38 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -6.0 | 2e-07 | 20/38 (HOP62, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.653×** | -5.9 | 2e-07 | 19/38 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.699×** | -5.0 | 4e-05 | 18/38 (BT-474, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.703×** | -4.9 | 5e-05 | 19/36 (A-427, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -4.2 | 0.001 | 10/38 (NCI-H1573, C-33 A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.570×** | -4.1 | 0.002 | 13/37 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.573×** | -4.1 | 0.002 | 13/33 (SHP-77, C32, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.027 | 14/38 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.779×** | -3.3 | 0.036 | 13/38 (AN3 CA, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.079 | 12/38 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 40.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.198× (z -12.0) |
| [[LoVo (line)]] | wt | 26.6 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 16.6 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.0546× (z -17.9) |
| [[SW480 (line)]] | alt | 15.3 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.226× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.265× (z -11.0) |
| [[COLO 205 (line)]] | alt | 31.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0846× (z -14.4) |
| [[A-427 (line)]] | wt | 8.80 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.114× (z -9.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0866× (z -10.2) |
| [[HT-29 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 6.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 6.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.9) | — |
| [[A-172 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L3-AS1]] | +0.66 | +0.32 / +0.56 | both halves | 2e-04 | same gene group |
| [[POU6F1]] | +0.63 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[SETD1B]] | +0.62 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SAP30L-AS1]] | +0.59 | +0.37 / +0.38 | both halves | 8e-05 | same gene group |
| [[SPESP1]] | +0.59 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[CIBAR1-DT]] | +0.58 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[FAM174B]] | +0.58 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[ZNF514]] | +0.58 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[PHF8]] | +0.57 | +0.46 / +0.23 | both halves | 5e-04 |  |
| [[GTF3C2-AS2]] | +0.57 | +0.31 / +0.38 | both halves | 2e-04 | same gene group |
| [[ANXA2R-OT1]] | +0.56 | +0.19 / +0.45 | ⚠ not reproduced | 8e-04 |  |
| [[CASTOR3P-1]] | +0.56 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[ARID1A]] | +0.56 | +0.51 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS13]] | -0.56 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TTC26]] | -0.54 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[POT1]] | -0.53 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[TLE6]] | -0.53 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[GPATCH11]] | -0.52 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[SKIC3]] | -0.52 | -0.41 / -0.26 | both halves | 3e-04 |  |
| [[RAB3A]] | -0.51 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[STN1]] | -0.50 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[C17orf58]] | -0.50 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[ZNF511]] | -0.49 | -0.39 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[PIP4P2]] | -0.49 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[ATG4C]] | -0.49 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[MRPL17]] | -0.49 | -0.35 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATG4C]] | B | GATA2-AS1 activity raises ATG4C's level | lines that do not express GATA2-AS1 (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without GATA2-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GATA2 |
| [[NBPF3]] | B | GATA2-AS1 activity raises NBPF3's level | lines that do not express GATA2-AS1 (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without GATA2-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: GATA2 |
| [[PDCD6IP-DT]] | B | GATA2-AS1 activity lowers PDCD6IP-DT's level | lines that do not express GATA2-AS1 (10) vs lines expressing it (40) | 1.36× higher at baseline in the lines without GATA2-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: GATA2 |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.8, 11.5); signed map (25.5, -24.4). **Vector** length 65.8, 12.0% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +15.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -10.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -6.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | GATA2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q21.3 — chr3:128,489,212-128,502,970 (+) |
| Ensembl biotype | lncRNA |
| Also known as | GATA2AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51108) · Entrez [101927167](https://www.ncbi.nlm.nih.gov/gene/101927167) · Ensembl [ENSG00000244300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244300)

## Data

Gene col 14400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14400); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14400]; `tensor/DDL_lfc|DDL_z.npy` [14400]; `embed/gene_vectors.npy` [14400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14400 or target_col == 14400). Every well: [[GATA2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATA2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
