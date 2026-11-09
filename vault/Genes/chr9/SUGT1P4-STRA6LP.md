---
symbol: "SUGT1P4-STRA6LP"
type: "gene"
col: 14899
ensembl_id: "ENSG00000254876"
name: "SUGT1P4-STRA6LP readthrough"
location: "9q22.33"
module: 17
arm: "+"
pooled_cpm: 4.81
n_lines_expressing: 41
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SUGT1P4-STRA6LP

*SUGT1P4-STRA6LP readthrough* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +5.3, q 6e-05, up in 16 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.279× (z -13.1, q 3e-36, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRA6LP]] (+0.95, fdr 7e-06, ⚠ same locus), [[SUGT1P4-STRA6LP-CCDC180]] (+0.84, fdr 7e-06, ⚠ same locus), [[MRPS31P4]] (+0.80, fdr 7e-06), [[LINC00888]] (+0.74, fdr 7e-06), [[CNEP1R1]] (+0.68, fdr 7e-06); moves opposite to [[MIATNB]] (-0.65, fdr 1e-05), [[FBXL19-AS1]] (-0.65, fdr 1e-05), [[ZNF407]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[PAPSS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +5.3 | 6e-05 | 16/38 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.9 | 3e-04 | 13/37 (HEC-1-A, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.005 | 5/37 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.005 | 12/37 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.009 | 12/37 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +3.4 | 0.054 | 4/37 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.054 | 5/38 (A-172, C32, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.12 | 6/38 (NCI-H1792, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.279×** | -13.1 | 3e-36 | 31/37 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.301×** | -12.3 | 3e-32 | 31/38 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.315×** | -11.8 | 5e-30 | 27/37 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.447×** | -11.6 | 3e-29 | 26/34 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.342×** | -11.0 | 5e-26 | 21/32 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.398×** | -9.1 | 1e-17 | 20/31 (NCI-H2347, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.428×** | -8.7 | 3e-16 | 26/36 (HEC-1-A, NCI-H23, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.571×** | -8.1 | 3e-14 | 24/38 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.454×** | -8.1 | 4e-14 | 17/20 (HS-578T, HEC-1-A, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.460×** | -7.6 | 1e-12 | 22/33 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.594×** | -5.3 | 5e-06 | 17/38 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -5.0 | 2e-05 | 13/36 (A498, C32, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.648×** | -4.1 | 0.002 | 11/12 (HEC-1-A, NCI-H2347, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -4.1 | 0.002 | 14/37 (H4, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.688×** | -3.7 | 0.009 | 9/9 (NCI-H2347, HS-578T, …) | all doses, flat | composition shift |
| [[Vilanterol (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.011 | 13/37 (SW1417, SW 1271, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.618×** | -3.5 | 0.015 | 11/36 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **0.656×** | -3.1 | 0.062 | 6/35 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.730×** | -3.0 | 0.081 | 4/37 (C-33 A, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 10.6 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0426× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -11.9) |
| [[A498 (line)]] | wt | 6.77 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0156× (z -19.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.8) |
| [[HOP62 (line)]] | alt | 7.31 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0427× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0509× (z -14.0) |
| [[A-172 (line)]] | wt | 9.03 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0599× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.177× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 6.55 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -12.1) |
| [[PANC-1 (line)]] | alt | 9.27 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 9.67 | 0 | 3 (1 ⚠) | — | [[Cepharanthine (drug)]] 0.5 µM 0.101× (z -9.4) |
| [[SNU-423 (line)]] | alt | 7.15 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -13.7) |
| [[A549 (line)]] | wt | 5.21 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0631× (z -10.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 5.12 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0603× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0723× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 5.81 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.106× (z -8.7) |
| [[SHP-77 (line)]] | alt | 5.97 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0866× (z -8.5) |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0565× (z -10.9) |
| [[A-427 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRA6LP]] | +0.95 | +0.92 / +0.91 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SUGT1P4-STRA6LP-CCDC180]] | +0.84 | +0.77 / +0.83 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MRPS31P4]] | +0.80 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[LINC00888]] | +0.74 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CNEP1R1]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ELP1]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[BBS5]] | +0.66 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[POT1]] | +0.66 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.65 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[PRPF39]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TADA1]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF18]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIATNB]] | -0.65 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | -0.65 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ZNF407]] | -0.64 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RFX3]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.43 / -0.56 | both halves | 4e-05 |  |
| [[MCF2]] | -0.61 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[BANP]] | -0.61 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SLC25A53]] | -0.60 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ASXL2]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | -0.58 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[PRDM10]] | -0.58 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[LINC02955]] | -0.58 | -0.38 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SUGT1P4-STRA6LP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZSCAN23]] | B | ZSCAN23 activity raises SUGT1P4-STRA6LP's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without ZSCAN23 | 0.051 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SUGT1P4-STRA6LP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SUGT1P4-STRA6LP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCDC180]] | C | CCDC180 activity raises SUGT1P4-STRA6LP's level | lines that do not express CCDC180 (8) vs lines expressing it (42) | 4.27× lower at baseline in the lines without CCDC180 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: STRA6LP; co-absent with the target |
| [[STRA6LP]] | C | STRA6LP's natural level strengthens SUGT1P4-STRA6LP's drug response | STRA6LP's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.26; direction not clear | 0.087 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS1]] | B | [[STRA6LP]], SUGT1P4-STRA6LP activity lowers PAPSS1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP (9) vs lines expressing them (41) | 1.32× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP | 0.027 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[CNEP1R1]] | B | [[STRA6LP]], SUGT1P4-STRA6LP, [[SUGT1P4-STRA6LP-CCDC180]] activity lowers CNEP1R1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.19× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[LYPLA2]] | B | [[STRA6LP]], SUGT1P4-STRA6LP, [[SUGT1P4-STRA6LP-CCDC180]] activity lowers LYPLA2's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.15× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[CCDC180]] | C | [[STRA6LP]], SUGT1P4-STRA6LP, [[SUGT1P4-STRA6LP-CCDC180]] activity raises CCDC180's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 5.07× lower at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.4, -4.3); signed map (-25.7, -14.5). **Vector** length 69.0, 12.5% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +5.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | -12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SUGT1P4-STRA6LP readthrough |
| Locus type | readthrough (other) |
| Location | 9q22.33 — chr9:97,238,449-97,297,314 (+) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100499484](https://www.ncbi.nlm.nih.gov/gene/100499484):

> This locus is a fusion of a partial duplication of SUGT1 at the 5' end and the ortholog of mouse 1300002K09Rik (GeneID:74152) at the 3' end. A frameshift disrupts the potential open reading frame, so this locus is considered to be a transcribed pseudogene in humans. In addition, read-through transcripts extending into the downstream locus (GeneID:100499483) are observed. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:53834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53834) · Entrez [100499484](https://www.ncbi.nlm.nih.gov/gene/100499484) · Ensembl [ENSG00000254876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254876)

## Data

Gene col 14899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14899); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14899]; `tensor/DDL_lfc|DDL_z.npy` [14899]; `embed/gene_vectors.npy` [14899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14899 or target_col == 14899). Every well: [[SUGT1P4-STRA6LP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGT1P4-STRA6LP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
