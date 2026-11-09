---
symbol: "ZNF512B"
type: "gene"
col: 12269
ensembl_id: "ENSG00000196700"
name: "zinc finger protein 512B"
location: "20q13.33"
module: 16
arm: "+"
pooled_cpm: 7.8
n_lines_expressing: 40
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF512B

*zinc finger protein 512B* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +7.0, q 1e-09, up in 19 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.56× (z +4.5, q 9e-04, up in 18 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 9.55×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.356× (z -15.6, q 0e+00, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGO]] (+0.72, fdr 7e-06), [[CEP41]] (+0.66, fdr 7e-06), [[CCDC113]] (+0.65, fdr 7e-06); moves opposite to [[GRK3]] (-0.60, fdr 1e-05), [[C9orf153]] (-0.60, fdr 3e-05), [[RAB6A]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[TCTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 9.55×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.0 | 1e-09 | 19/28 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.3 | 6e-08 | 12/16 (A498, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +6.0 | 5e-07 | 12/22 (NCI-H2030, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.56×** | +4.5 | 9e-04 | 18/37 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.043 | 9/38 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.043 | 5/38 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 1.35× | +3.2 | 0.11 | 4/37 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.35× | +3.2 | 0.11 | 3/38 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.33× | +3.0 | 0.16 | 13/32 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.356×** | -15.6 | 0e+00 | 30/34 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.399×** | -9.8 | 4e-20 | 29/37 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -9.4 | 1e-18 | 25/36 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.464×** | -8.2 | 4e-14 | 24/37 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -7.4 | 2e-11 | 24/36 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -6.7 | 2e-09 | 25/37 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -5.7 | 1e-06 | 20/37 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.598×** | -5.5 | 3e-06 | 22/36 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -5.2 | 1e-05 | 21/36 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -5.2 | 1e-05 | 19/33 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -4.8 | 6e-05 | 20/38 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -4.6 | 2e-04 | 19/38 (Hs 766T, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -4.3 | 9e-04 | 16/32 (NCI-H460, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.674×** | -4.2 | 0.001 | 16/37 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -4.2 | 0.001 | 17/34 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.677×** | -4.2 | 0.001 | 15/38 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.17 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0802× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -12.4) |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.194× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0774× (z -16.8) |
| [[PANC-1 (line)]] | alt | 7.63 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -8.7) |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0744× (z -8.8) |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0713× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 7.77 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.6) |
| [[J82 (line)]] | alt | 8.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 5.93 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 9.93 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0637× (z -10.8) |
| [[SW480 (line)]] | alt | 5.40 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.0) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGO]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CEP41]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CCDC113]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ZFP41]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | same gene group |
| [[PABIR1]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZNF839]] | +0.64 | +0.60 / +0.57 | both halves | 8e-06 | same gene group |
| [[ZNF252P-1]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[USP19]] | +0.62 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[N6AMT1]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FKTN]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[BACE1-AS]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK3]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[C9orf153]] | -0.60 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[TMEM165]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[HIGD2A]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CEP164P1]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PIK3C2A]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[UBA52]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SPDYE5]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[SSR4]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SLC37A3]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZNF512B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CCDC113]] | C | CCDC113 activity raises ZNF512B's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without CCDC113 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCTN1]] | B | ZNF512B activity raises TCTN1's level | lines that do not express ZNF512B (10) vs lines expressing it (40) | 2.05× lower at baseline in the lines without ZNF512B | 0.069 | ⚠ within organs, on part of the lines; also absent: HLTF, FERMT2, DNAAF9; maybe low, not absent |
| [[RRP15]] | B | ZNF512B activity raises RRP15's level | lines that do not express ZNF512B (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without ZNF512B | 0.074 | ⚠ within organs, on part of the lines; also absent: HLTF, FERMT2, DNAAF9; maybe low, not absent |
| [[CEP41]] | B | ZNF512B activity raises CEP41's level | lines that do not express ZNF512B (10) vs lines expressing it (40) | 1.91× lower at baseline in the lines without ZNF512B | 0.098 | ⚠ within organs, on part of the lines; also absent: HLTF, FERMT2, DNAAF9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.7, 15.2); signed map (0.8, -34.1). **Vector** length 70.2, 14.0% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.7 |
|  | [[Larotrectinib (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 512B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,956,704-63,969,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GM632, MGC149845, MGC149846 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 4 pathways, smallest: RHOV GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KM6](https://www.uniprot.org/uniprotkb/Q96KM6) (Zinc finger protein 512B):

> Involved in transcriptional regulation by repressing gene expression. Associates with the nucleosome remodeling and histone deacetylase (NuRD) complex, which promotes transcriptional repression by histone deacetylation and nucleosome remodeling. Sequence-specific DNA-binding protein that recognizes repetitive and non-consecutive TTC sequences in pericentric repeat and initiate heterochromatin formation through interaction with SUV39H1/2 methyltransferases which catalyze histone H3K9 methylation …

**Summary**, from NCBI Gene [57473](https://www.ncbi.nlm.nih.gov/gene/57473):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in negative regulation of miRNA transcription. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29212) · Entrez [57473](https://www.ncbi.nlm.nih.gov/gene/57473) · UniProt [Q96KM6](https://www.uniprot.org/uniprotkb/Q96KM6) · Ensembl [ENSG00000196700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196700)

## Data

Gene col 12269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12269); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12269]; `tensor/DDL_lfc|DDL_z.npy` [12269]; `embed/gene_vectors.npy` [12269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12269 or target_col == 12269). Every well: [[ZNF512B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF512B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
