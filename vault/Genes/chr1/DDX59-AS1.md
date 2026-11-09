---
symbol: "DDX59-AS1"
type: "gene"
col: 15261
ensembl_id: "ENSG00000260088"
name: "DDX59 antisense RNA 1"
location: "1q32.1"
module: 15
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DDX59-AS1

*DDX59 antisense RNA 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.95× (z +13.5, q 9e-39, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.396× (z -8.1, q 2e-13, down in 25 of 38 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.476× (z -6.5, q 8e-09, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DICER1-AS1]] (+0.79, fdr 7e-06), [[UGDH-AS1]] (+0.76, fdr 7e-06), [[ITFG2-AS1]] (+0.75, fdr 1e-05); moves opposite to [[USB1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SGK2]] → it (grade B ⚠); 5 go from it, the strongest it → [[CHD1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +13.5 | 9e-39 | 23/28 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +6.7 | 6e-09 | 13/24 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +6.5 | 2e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +6.1 | 2e-07 | 6/17 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +5.6 | 2e-06 | 8/27 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.83×** | +5.4 | 8e-06 | 12/38 (A-172, A498, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.2 | 2e-05 | 14/29 (C-33 A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +5.0 | 5e-05 | 15/38 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +4.7 | 2e-04 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.012 | 5/24 (SW480, A498, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.012 | 8/33 (A-172, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.6 | 0.015 | 2/15 (SW480, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.015 | 5/32 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.017 | 7/36 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.017 | 8/37 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.091 | 3/26 (HOP62, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.396×** | -8.1 | 2e-13 | 25/38 (PANC-1, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.438×** | -7.3 | 1e-10 | 18/36 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.469×** | -6.6 | 6e-09 | 21/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.473×** | -6.6 | 7e-09 | 19/39 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -6.5 | 8e-09 | 21/37 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.531×** | -5.5 | 3e-06 | 18/35 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.555×** | -5.2 | 2e-05 | 18/38 (AsPC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.557×** | -5.1 | 2e-05 | 17/37 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -4.9 | 5e-05 | 16/39 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.573×** | -4.9 | 6e-05 | 18/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.586×** | -4.7 | 1e-04 | 15/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.602×** | -4.4 | 4e-04 | 18/28 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -4.2 | 0.001 | 18/30 (A498, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.437×** | -3.8 | 0.006 | 16/32 (PANC-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.444×** | -3.7 | 0.007 | 13/27 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.487×** | -3.3 | 0.029 | 7/29 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.487×** | -3.3 | 0.029 | 10/28 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.601×** | -3.2 | 0.040 | 5/39 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.708×** | -3.0 | 0.064 | 6/35 (SW 900, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.64 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.57 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0386× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.9) |
| [[A498 (line)]] | wt | 8.94 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 6.53 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0773× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 4.73 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[C32 (line)]] | wt | 6.45 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0666× (z -8.6) |
| [[A-172 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.924 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DICER1-AS1]] | +0.79 | +0.78 / +0.67 | both halves | 7e-06 | same gene group |
| [[UGDH-AS1]] | +0.76 | +0.80 / +0.61 | both halves | 7e-06 | same gene group |
| [[ITFG2-AS1]] | +0.75 | +0.75 / +0.54 | both halves | 1e-05 | same gene group |
| [[OXA1L-DT]] | +0.75 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[NSMCE1-DT]] | +0.75 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[EPM2A-DT]] | +0.75 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.73 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 | same gene group |
| [[HLA-DMA]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.70 | +0.69 / +0.56 | both halves | 1e-05 | same gene group |
| [[TMEM9B-AS1]] | +0.70 | +0.67 / +0.51 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USB1]] | -0.60 | -0.47 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGK2]] | B | SGK2 activity raises DDX59-AS1's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without SGK2 | 0.091 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DDX59-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD1-DT]] | B | DDX59-AS1 activity raises CHD1-DT's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without DDX59-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[AGAP5]] | B | DDX59-AS1 activity raises AGAP5's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without DDX59-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[DARS1-AS1]] | B | DDX59-AS1 activity raises DARS1-AS1's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without DDX59-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[CCDC18-AS1]] | B | DDX59-AS1 activity raises CCDC18-AS1's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without DDX59-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[EPM2A-DT]] | B | DDX59-AS1 activity raises EPM2A-DT's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without DDX59-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (5.0, 21.0); signed map (30.4, -7.0). **Vector** length 67.5, 13.0% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +0.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.6 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +5.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.9 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.8 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.9 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DDX59 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.1 — chr1:200,669,507-200,694,250 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41094) · Entrez [101929224](https://www.ncbi.nlm.nih.gov/gene/101929224) · Ensembl [ENSG00000260088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260088)

## Data

Gene col 15261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15261); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15261]; `tensor/DDL_lfc|DDL_z.npy` [15261]; `embed/gene_vectors.npy` [15261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15261 or target_col == 15261). Every well: [[DDX59-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX59-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
