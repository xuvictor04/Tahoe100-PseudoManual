---
symbol: "GCNT4"
type: "gene"
col: 10769
ensembl_id: "ENSG00000176928"
name: "glucosaminyl (N-acetyl) transferase 4"
location: "5q13.3"
module: 80
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 40
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# GCNT4

*glucosaminyl (N-acetyl) transferase 4* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.0× (z +31.9, q 0e+00, up in 28 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.356× (z -9.8, q 1e-19, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.74, fdr 1e-05), [[PPP1R12A-AS2]] (+0.71, fdr 3e-04), [[WNT3]] (+0.71, fdr 4e-05); moves opposite to [[IFT172]] (-0.72, fdr 2e-05), [[GUSBP1]] (-0.69, fdr 2e-05), [[ELP1]] (-0.69, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[RGS20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.0×** | +31.9 | 0e+00 | 28/28 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.16×** | +12.9 | 1e-35 | 23/30 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.08×** | +12.7 | 7e-35 | 20/25 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +10.9 | 1e-25 | 21/30 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.05×** | +10.5 | 1e-23 | 23/32 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +7.0 | 2e-10 | 17/33 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +6.7 | 1e-09 | 16/28 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.3 | 1e-05 | 15/34 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 3e-04 | 8/34 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.5 | 3e-04 | 12/21 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +4.5 | 3e-04 | 2/11 (PANC-1, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.5 | 4e-04 | 1/10 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +4.3 | 8e-04 | 13/35 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.60×** | +4.2 | 0.001 | 8/32 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.001 | 10/34 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.019 | 9/34 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.077 | 7/34 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.077 | 7/32 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.356×** | -9.8 | 1e-19 | 25/36 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.429×** | -8.0 | 4e-13 | 22/35 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -6.2 | 1e-07 | 21/35 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -4.1 | 0.004 | 12/29 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.646×** | -4.1 | 0.004 | 9/32 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -3.6 | 0.029 | 13/31 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.701×** | -3.4 | 0.061 | 5/34 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -3.3 | 0.066 | 12/29 (SW 900, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.0597× (z -15.2) |
| [[J82 (line)]] | alt | 13.2 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.195× (z -8.8) |
| [[LoVo (line)]] | wt | 9.19 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.156× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 7.82 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 14.0× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 4.81 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 2.90 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 5.40 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +14.4) | — |
| [[A-172 (line)]] | wt | 4.13 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +13.3) | [[Belinostat (drug)]] 5 µM 0.0746× (z -8.7) |
| [[A498 (line)]] | wt | 2.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.4) | — |
| [[A549 (line)]] | wt | 6.99 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.0850× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 3.97 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +15.9) | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0840× (z -10.0) |
| [[KATO III (line)]] | alt | 11.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0732× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 1.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.5× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.93× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 1.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.7× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0966× (z -9.1) |
| [[SNU-423 (line)]] | alt | 3.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 4.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +11.3) | — |
| [[SW480 (line)]] | alt | 1.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +9.6) | — |
| [[A-427 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.74 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.71 | +0.66 / +0.28 | both halves | 3e-04 |  |
| [[WNT3]] | +0.71 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[LINC01829]] | +0.70 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[ZBED5]] | +0.69 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[LRRC8C-DT]] | +0.69 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[CCDC73]] | +0.69 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.69 | +0.65 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[SPHK1]] | +0.68 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PBLD]] | +0.68 | +0.62 / +0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[LINC00863]] | +0.68 | +0.62 / +0.40 | both halves | 4e-05 |  |
| [[ATE1OSP]] | +0.67 | +0.59 / +0.23 | both halves | 5e-04 |  |
| [[PATL2]] | +0.66 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[GABPB1]] | +0.66 | +0.48 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.72 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[GUSBP1]] | -0.69 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ELP1]] | -0.69 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ALAD]] | -0.68 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[GUSBP18]] | -0.68 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[POT1]] | -0.67 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[EHMT2]] | -0.65 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[HLTF]] | -0.65 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ARL6]] | -0.65 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[SPATA6]] | -0.64 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ATG4C]] | -0.64 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[RFC1]] | -0.64 | -0.46 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GCNT4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.9% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RGS20]] | B | RGS20 activity raises GCNT4's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.66× lower at baseline in the lines without RGS20 | 0.009 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[NKX3-1]] | B | NKX3-1 activity raises GCNT4's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without NKX3-1 | 0.039 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[CGAS]] | B | CGAS activity raises GCNT4's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without CGAS | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[HDAC6]] | B | HDAC6 activity raises GCNT4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CA3]] | B | CA3 activity strengthens GCNT4's drug response | lines that do not express CA3 (8) vs lines expressing it (28) | the lines without CA3 respond 0.84× as strongly (z diff +0.48); strongest at Epirubicin (hydrochloride) 5 µM: 1.77x vs 4.91x (z diff +2.8) | 0.087 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS20]] | B | GCNT4 activity raises RGS20's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without GCNT4 | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HECTD2]] | B | GCNT4 activity raises HECTD2's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without GCNT4 | 0.025 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SPHK1]] | B | GCNT4 activity raises SPHK1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without GCNT4 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NKX3-1]] | B | GCNT4 activity raises NKX3-1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 2.36× lower at baseline in the lines without GCNT4 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HLA-L-1]] | B | GCNT4 activity raises HLA-L-1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without GCNT4 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RXYLT1]] | B | GCNT4 activity raises RXYLT1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without GCNT4 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, 9.2); signed map (23.4, -6.3). **Vector** length 79.3, 17.1% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +31.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -8.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -6.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | glucosaminyl (N-acetyl) transferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,025,346-75,052,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C2GNT3; previously LINC01336 |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P109](https://www.uniprot.org/uniprotkb/Q9P109) (Beta-1,3-galactosyl-O-glycosyl-glycoprotein beta-1,6-N-acetylglucosaminyltransferase 4):

> Glycosyltransferase that mediates core 2 O-glycan branching, an important step in mucin-type biosynthesis. Does not have core 4 O-glycan or I-branching enzyme activity.

**Summary**, from NCBI Gene [51301](https://www.ncbi.nlm.nih.gov/gene/51301):

> Predicted to enable acetylglucosaminyltransferase activity. Predicted to be involved in carbohydrate metabolic process and protein O-linked glycosylation via N-acetyl-galactosamine. Predicted to act upstream of or within several processes, including inter-male aggressive behavior; kidney morphogenesis; and thyroid hormone metabolic process. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17973) · Entrez [51301](https://www.ncbi.nlm.nih.gov/gene/51301) · UniProt [Q9P109](https://www.uniprot.org/uniprotkb/Q9P109) · Ensembl [ENSG00000176928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176928)

## Data

Gene col 10769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10769); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10769]; `tensor/DDL_lfc|DDL_z.npy` [10769]; `embed/gene_vectors.npy` [10769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10769 or target_col == 10769). Every well: [[GCNT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCNT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
