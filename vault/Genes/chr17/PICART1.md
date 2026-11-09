---
symbol: "PICART1"
type: "gene"
col: 14468
ensembl_id: "ENSG00000246640"
name: "p53 inducible cancer associated RNA transcript 1"
location: "17q21.33"
module: 92
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 14
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# PICART1

*p53 inducible cancer associated RNA transcript 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.22× (z +14.3, q 1e-43, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +8.1, q 1e-13, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.539× (z -4.3, q 0.008, down in 17 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA7B-DT]] (+0.63, fdr 1e-05), [[LINC02454]] (+0.58, fdr 1e-05), [[LINC00941]] (+0.58, fdr 1e-05); moves opposite to [[CEP162]] (-0.46, fdr 1e-04).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGA3]] → it (grade B ⚠); 14 go from it, the strongest it → cells under [[Bendamustine (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.22×** | +14.3 | 1e-43 | 5/6 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.26×** | +11.7 | 3e-29 | 10/13 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.87×** | +10.3 | 8e-23 | 4/6 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +8.1 | 1e-13 | 20/29 (A498, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.004 | 11/38 (A-172, SW480, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.0 | 0.005 | 3/27 (A549, Panc 03.27, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.006 | 9/30 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.44×** | +3.7 | 0.016 | 7/39 (PANC-1, HOP62, …) | rises with dose | low cells (technical?); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.032 | 5/40 (HOP62, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.5 | 0.032 | 2/8 (Hs 766T, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.094 | 8/33 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.539×** | -4.3 | 0.008 | 17/40 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.654×** | -3.7 | 0.059 | 12/40 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -3.6 | 0.070 | 13/40 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.608×** | -3.5 | 0.071 | 10/39 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.625×** | -3.3 | 0.097 | 14/37 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.666×** | -3.2 | 0.097 | 10/40 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -3.2 | 0.097 | 7/30 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.699×** | -3.2 | 0.097 | 11/39 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.727×** | -3.1 | 0.097 | 14/37 (Hs 766T, SW1417, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.627×** | -3.1 | 0.097 | 14/31 (SW 900, SK-MEL-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.44 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.9× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.592 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.557 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.841 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.722 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.672 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.553 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.552 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.908 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA7B-DT]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LINC00941]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[DNMBP-AS1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[FZD4-DT]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CNIH3]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MAP4K4]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TMLHE-AS1]] | +0.56 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MEI1]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[DPY19L3-DT]] | +0.55 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PECAM1]] | +0.55 | +0.40 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP162]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA3]] | B | ITGA3 activity raises PICART1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without ITGA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[CCDC190]] | B | CCDC190 activity weakens PICART1's drug response | lines that do not express CCDC190 (31) vs lines expressing it (9) | the lines without CCDC190 respond 0.90× as strongly (z diff +0.04); strongest at Dinaciclib 5 µM: 9.46x vs 2.01x (z diff -4.8) | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; target measured in part of the lines; both ways; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises PICART1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 5 µM | C | PICART1 activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.74× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| [[ITGA3]] | C | PICART1 activity raises ITGA3's level | lines that do not express PICART1 (4) vs lines expressing it (46) | 5.48× lower at baseline in the lines without PICART1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Econazole (drug)]] 0.5 µM | C | PICART1 activity lowers the cells' numbers under Econazole 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.35× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | C | PICART1 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.34× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Vortioxetine (drug)]] 0.5 µM | C | PICART1 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.34× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | C | PICART1 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.73× the cells of the other lines | 0.046 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | PICART1 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.52× the cells of the other lines | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | C | PICART1 activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.25× the cells of the other lines | 0.070 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Tranilast (drug)]] 0.5 µM | C | PICART1 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.78× the cells of the other lines | 0.079 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Nimesulide (drug)]] 5 µM | C | PICART1 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.75× the cells of the other lines | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent; cell counts less trustworthy |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | C | PICART1 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.78× the cells of the other lines | 0.086 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| cells under [[Sulfatinib (drug)]] 0.5 µM | C | PICART1 activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.28× the cells of the other lines | 0.087 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 8.2); signed map (11.5, 48.8). **Vector** length 54.9, 8.75% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | p53 inducible cancer associated RNA transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.33 — chr17:50,050,349-50,055,746 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27576) · Entrez [284080](https://www.ncbi.nlm.nih.gov/gene/284080) · Ensembl [ENSG00000246640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246640)

## Data

Gene col 14468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14468); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14468]; `tensor/DDL_lfc|DDL_z.npy` [14468]; `embed/gene_vectors.npy` [14468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14468 or target_col == 14468). Every well: [[PICART1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PICART1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
