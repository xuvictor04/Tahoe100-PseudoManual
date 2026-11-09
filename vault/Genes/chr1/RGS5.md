---
symbol: "RGS5"
type: "gene"
col: 6703
ensembl_id: "ENSG00000143248"
name: "regulator of G protein signaling 5"
location: "1q23.3"
module: 88
arm: "+"
pooled_cpm: 40.68
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# RGS5

*regulator of G protein signaling 5* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +7.1, q 8e-10, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.548× (z -7.4, q 7e-11, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA6A-AS1]] (+0.76, fdr 7e-06), [[ST7L]] (+0.76, fdr 1e-05), [[RAB30-DT]] (+0.74, fdr 7e-06); moves opposite to [[GMCL1]] (-0.68, fdr 2e-05), [[ZNF823]] (-0.68, fdr 1e-05), [[POGLUT2]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FBXO38-DT]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.1 | 8e-10 | 30/46 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 2e-06 | 26/46 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +4.8 | 2e-04 | 29/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +4.4 | 0.002 | 20/47 (SK-MEL-2, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.002 | 27/47 (A-172, A498, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.002 | 30/47 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.016 | 22/47 (J82, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.019 | 20/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.6 | 0.023 | 16/40 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.5 | 0.027 | 20/43 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.028 | 18/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.028 | 20/46 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.060 | 15/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.100 | 17/46 (SW480, LoVo, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.548×** | -7.4 | 7e-11 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.543×** | -7.2 | 1e-10 | 29/46 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -6.9 | 1e-09 | 32/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.606×** | -6.2 | 9e-08 | 30/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.410×** | -5.7 | 1e-06 | 29/47 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -4.9 | 9e-05 | 27/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -4.9 | 9e-05 | 26/47 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.675×** | -4.8 | 1e-04 | 29/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.684×** | -4.4 | 6e-04 | 26/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.694×** | -4.3 | 0.001 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -4.2 | 0.002 | 25/47 (HT-29, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.034 | 21/47 (CHP-212, A-427, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.613×** | -3.2 | 0.071 | 19/47 (SHP-77, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.700×** | -3.1 | 0.073 | 16/47 (BT-474, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +35.8) | — |
| [[PANC-1 (line)]] | alt | 35.5 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -14.2) |
| [[SW480 (line)]] | alt | 37.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 56.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.284× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -18.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +23.8) | — |
| [[HCT15 (line)]] | alt | 50.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.223× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 38.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.3) | — |
| [[RKO (line)]] | wt | 59.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -12.0) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -9.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.3) | — |
| [[J82 (line)]] | alt | 42.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 32.1 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0453× (z -9.1) |
| [[SNU-423 (line)]] | alt | 42.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.2) | — |
| [[A-427 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA6A-AS1]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[ST7L]] | +0.76 | +0.84 / +0.55 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.74 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.72 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.72 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.71 | +0.81 / +0.47 | both halves | 2e-05 |  |
| [[UFL1-AS1]] | +0.70 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | +0.69 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[CLHC1]] | +0.68 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[DPH5-DT]] | +0.67 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.67 | +0.80 / +0.42 | both halves | 4e-05 |  |
| [[JPX]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.68 | -0.75 / -0.47 | both halves | 2e-05 |  |
| [[ZNF823]] | -0.68 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.66 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[PDZD7]] | -0.66 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PI4KAP2]] | -0.66 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.65 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[MGST3]] | -0.65 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[CARD19]] | -0.65 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.64 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[RRAS]] | -0.63 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[SS18L1]] | -0.61 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[EFNA4]] | -0.61 | -0.57 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO38-DT]] | C | FBXO38-DT activity raises RGS5's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without FBXO38-DT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (5.2, 7.6); signed map (18.3, -25.4). **Vector** length 98.6, 26.5% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +4.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -4.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:163,111,121-163,321,791 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Reactome | 4 pathways, smallest: G alpha (q) signalling events; G alpha (i) signalling events; GPCR downstream signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [O15539](https://www.uniprot.org/uniprotkb/O15539) (Regulator of G protein signaling 5):

> Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits thereby driving them into their inactive GDP-bound form. Binds to G(i)-alpha and G(o)-alpha, but not to G(s)-alpha (By similarity).

**Summary**, from NCBI Gene [8490](https://www.ncbi.nlm.nih.gov/gene/8490):

> This locus represents naturally occurring readthrough transcription between the neighboring LOC127814295 (uncharacterized LOC127814295) and RGS5 (regulator of G-protein signaling 5) genes on chromosome 1. Some variants of the readthrough transcript encode novel proteins with unique N-termini. [provided by RefSeq, Nov 2022]

**Accessions** — [HGNC:10001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10001) · Entrez [8490](https://www.ncbi.nlm.nih.gov/gene/8490) · UniProt [O15539](https://www.uniprot.org/uniprotkb/O15539) · Ensembl [ENSG00000143248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143248)

## Data

Gene col 6703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6703); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6703]; `tensor/DDL_lfc|DDL_z.npy` [6703]; `embed/gene_vectors.npy` [6703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6703 or target_col == 6703). Every well: [[RGS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
