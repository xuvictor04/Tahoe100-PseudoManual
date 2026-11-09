---
symbol: "ERICH2-DT"
type: "gene"
col: 13951
ensembl_id: "ENSG00000234350"
name: "ERICH2 divergent transcript"
location: "2q31.1"
module: 15
arm: "+"
pooled_cpm: 6.89
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 16
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ERICH2-DT

*ERICH2 divergent transcript* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.41× (z +24.5, q 0e+00, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.446× (z -9.5, q 1e-18, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG1L9P]] (+0.75, fdr 1e-05), [[ITFG2-AS1]] (+0.75, fdr 1e-05), [[LINC00869-1]] (+0.72, fdr 1e-05); moves opposite to [[WRAP73]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[C21orf62-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.41×** | +24.5 | 0e+00 | 31/33 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +11.8 | 1e-29 | 25/30 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +10.8 | 5e-25 | 3/10 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.4 | 6e-19 | 3/8 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +9.0 | 3e-17 | 20/32 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +7.3 | 3e-11 | 13/29 (HCT15, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +5.5 | 4e-06 | 8/19 (NCI-H2347, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 10/39 (A-172, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.32×** | +4.6 | 3e-04 | 8/38 (A498, A-427, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.005 | 9/38 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.005 | 11/36 (COLO 205, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.015 | 7/36 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.028 | 6/36 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.039 | 6/36 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.039 | 6/36 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.039 | 3/36 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.041 | 0/36 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.054 | 4/39 (SW1417, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.057 | 5/38 (SW480, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -9.5 | 1e-18 | 25/36 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.448×** | -9.4 | 1e-18 | 29/39 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -8.5 | 3e-15 | 27/37 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.526×** | -7.6 | 6e-12 | 21/37 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.652×** | -5.0 | 6e-05 | 21/32 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.649×** | -4.9 | 1e-04 | 10/36 (HT-29, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -4.8 | 1e-04 | 19/36 (HT-29, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.660×** | -4.6 | 3e-04 | 16/35 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.693×** | -4.3 | 1e-03 | 9/38 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -3.7 | 0.014 | 14/34 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -3.6 | 0.014 | 12/34 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.746×** | -3.4 | 0.027 | 9/36 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.750×** | -3.4 | 0.030 | 12/39 (KATO III, COLO 205, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.751×** | -3.4 | 0.031 | 5/37 (LoVo, SW 1271, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.755×** | -3.3 | 0.035 | 8/37 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.038 | 10/37 (HT-29, SW480, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.038 | 8/37 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **0.773×** | -3.0 | 0.071 | 3/36 (SK-MEL-2, BT-474, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.2 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -14.3) |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0339× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 11.3 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0617× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0959× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 5.87 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +8.7) | [[Ixazomib citrate (drug)]] 0.5 µM 0.125× (z -9.4) |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0651× (z -13.6) |
| [[LoVo (line)]] | wt | 2.44 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.18× (z +9.1) | [[Captopril (drug)]] 0.05 µM 0.0534× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 10.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.126× (z -10.2) |
| [[PANC-1 (line)]] | alt | 4.38 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -8.6) |
| [[A-172 (line)]] | wt | 5.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +11.0) | — |
| [[A-427 (line)]] | wt | 8.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0891× (z -11.0) |
| [[A498 (line)]] | wt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.82× (z +16.4) | — |
| [[C32 (line)]] | wt | 5.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 6.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 6.86 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0631× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0759× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 3.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0623× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 1.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 6.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +9.7) | — |
| [[SW48 (line)]] | wt | 8.03 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0399× (z -8.6) |
| [[A549 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG1L9P]] | +0.75 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[ITFG2-AS1]] | +0.75 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[LINC00869-1]] | +0.72 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[OARD1]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.71 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.70 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[CCDC170]] | +0.70 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[HLA-DMA]] | +0.69 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.69 | +0.65 / +0.47 | both halves | 2e-05 | same gene group |
| [[STEAP2-AS1]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[PSMD7-DT]] | +0.67 | +0.68 / +0.41 | both halves | 4e-05 | same gene group |
| [[LRIG2-DT]] | +0.66 | +0.67 / +0.39 | both halves | 6e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.59 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERICH2-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[THNSL2]] | B | THNSL2 activity raises ERICH2-DT's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without THNSL2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[B3GAT1-DT]] | B | B3GAT1-DT activity raises ERICH2-DT's level | lines that do not express B3GAT1-DT (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without B3GAT1-DT | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000213981, HEPHL1, ENSG00000287069 |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises ERICH2-DT's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.66× lower at baseline in the lines without ANKRD20A21P | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[THBS4-AS1]] | B | THBS4-AS1 activity raises ERICH2-DT's level | lines that do not express THBS4-AS1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without THBS4-AS1 | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf62-AS1]] | B | ERICH2-DT activity raises C21orf62-AS1's level | lines that do not express ERICH2-DT (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without ERICH2-DT | 0.071 | ⚠ within organs, on part of the lines; also absent: ERICH2, GAD1, ENSG00000256673; maybe low, not absent |
| [[THNSL2]] | B | ERICH2-DT activity raises THNSL2's level | lines that do not express ERICH2-DT (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without ERICH2-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: ERICH2, GAD1, ENSG00000256673; maybe low, not absent |
| [[LINC02482]] | B | ERICH2-DT activity raises LINC02482's level | lines that do not express ERICH2-DT (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without ERICH2-DT | 0.084 | ⚠ within organs, on part of the lines; also absent: ERICH2, GAD1, ENSG00000256673; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.5, 20.1); signed map (29.0, -6.6). **Vector** length 66.3, 11.9% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +24.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | ERICH2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.1 — chr2:170,700,368-170,813,670 (-) |
| Ensembl biotype | lncRNA |
| Also known as | uc.95 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55686) · Entrez [101926913](https://www.ncbi.nlm.nih.gov/gene/101926913) · Ensembl [ENSG00000234350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234350)

## Data

Gene col 13951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13951); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13951]; `tensor/DDL_lfc|DDL_z.npy` [13951]; `embed/gene_vectors.npy` [13951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13951 or target_col == 13951). Every well: [[ERICH2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERICH2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
