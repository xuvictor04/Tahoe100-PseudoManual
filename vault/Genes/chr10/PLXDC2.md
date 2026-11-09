---
symbol: "PLXDC2"
type: "gene"
col: 4193
ensembl_id: "ENSG00000120594"
name: "plexin domain containing 2"
location: "10p12.31"
module: 9
arm: "+"
pooled_cpm: 13.4
n_lines_expressing: 26
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PLXDC2

*plexin domain containing 2* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +15.5, q 0e+00, up in 13 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.699× (z -4.2, q 0.012, down in 16 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.221×, BT-474 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0188×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0440×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.374×); [[TAK-901 (drug)]] 5 µM in 1 line (HepG2/C3A 0.0900×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.296×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALRD1]] (+0.61, fdr 1e-05, ⚠ same locus), [[PPARGC1A]] (+0.60, fdr 1e-05), [[PRUNE2]] (+0.60, fdr 1e-05), [[DMD]] (+0.59, fdr 2e-05); moves opposite to [[DIP2A]] (-0.53, fdr 2e-05), [[SWI5]] (-0.48, fdr 1e-04), [[SLC66A3]] (-0.48, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[ENPP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +15.5 | 0e+00 | 13/21 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +14.6 | 1e-45 | 18/24 (LoVo, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.7 | 2e-34 | 5/11 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +12.6 | 2e-34 | 10/17 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +9.4 | 6e-19 | 7/15 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +8.2 | 3e-14 | 17/23 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +7.5 | 7e-12 | 6/23 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.7 | 2e-09 | 7/24 (A-172, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.2 | 3e-08 | 6/20 (A-172, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.7 | 8e-07 | 4/21 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 7e-04 | 13/23 (A-172, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.2 | 0.001 | 14/23 (LoVo, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.2 | 0.001 | 5/17 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 8/23 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 11/23 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.027 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.030 | 6/24 (A-172, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.066 | 6/23 (A-172, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.078 | 8/24 (A-172, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4193.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.221×, BT-474 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0188×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0440×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.374×); [[TAK-901 (drug)]] 5 µM in 1 line (HepG2/C3A 0.0900×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.296×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -4.2 | 0.012 | 16/23 (HepG2/C3A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.754× | -3.3 | 0.24 | 5/23 (SNU-423, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.35 | 11/23 (A498, SW 900, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 43.5 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +20.9) | — |
| [[HepG2_C3A (line)]] | wt | 290 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0188× (z -33.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.2) |
| [[A498 (line)]] | wt | 75.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.248× (z -10.2) |
| [[LoVo (line)]] | wt | 7.83 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +10.3) | — |
| [[A-427 (line)]] | wt | 3.61 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.38× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[H4 (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.5) | — |
| [[J82 (line)]] | alt | 6.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 47.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -8.5) |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0678× (z -10.2) |
| [[A549 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALRD1]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 | ⚠ same locus (25.8 kb, same strand: neighbours can correlate without regulation) |
| [[PPARGC1A]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PRUNE2]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[DMD]] | +0.59 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[LINC01091]] | +0.58 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[KCNMB2-AS1]] | +0.57 | +0.53 / +0.43 | both halves | 4e-05 |  |
| [[GPNMB]] | +0.57 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[ZNF608]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CD36]] | +0.56 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[FIGN]] | +0.56 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[LINC01170]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SLC9A9]] | +0.54 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PPFIA2]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SWI5]] | -0.48 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[SLC66A3]] | -0.48 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[PLD2]] | -0.46 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[ATG16L2]] | -0.46 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[CEP89]] | -0.45 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[KIF21B]] | -0.45 | -0.44 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[MYO9B]] | -0.45 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[ZFYVE21]] | -0.45 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLXDC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SORBS2]] | B | SORBS2 activity raises PLXDC2's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without SORBS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[FOXP2]] | B | FOXP2 activity raises PLXDC2's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.43× lower at baseline in the lines without FOXP2 | 0.086 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLXDC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[GPNMB]] | C | GPNMB activity raises PLXDC2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without GPNMB | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP3]] | B | PLXDC2 activity raises ENPP3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.59× lower at baseline in the lines without PLXDC2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[MALRD1]] | B | PLXDC2 activity raises MALRD1's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without PLXDC2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[ARHGAP24]] | B | PLXDC2 activity raises ARHGAP24's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without PLXDC2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[DENND2B]] | B | PLXDC2 activity raises DENND2B's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without PLXDC2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[MAPK10]] | B | PLXDC2 activity raises MAPK10's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without PLXDC2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[COL12A1]] | B | PLXDC2 activity raises COL12A1's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without PLXDC2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[CNKSR3]] | B | PLXDC2 activity raises CNKSR3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without PLXDC2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[FOXP2]] | B | PLXDC2 activity raises FOXP2's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without PLXDC2 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[PEX5L]] | B | PLXDC2 activity raises PEX5L's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without PLXDC2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[PDZRN3]] | B | PLXDC2 activity raises PDZRN3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without PLXDC2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[PEG3]] | C | PLXDC2 activity raises PEG3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.15× lower at baseline in the lines without PLXDC2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | PLXDC2 activity raises ANGPT1's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.58× lower at baseline in the lines without PLXDC2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, 37.0); signed map (46.2, 30.2). **Vector** length 50.2, 9.82% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +12.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.9 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | +0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | plexin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:19,816,239-20,289,856 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEM7R, FLJ14623, PLXDC2-OT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX71](https://www.uniprot.org/uniprotkb/Q6UX71) (Plexin domain-containing protein 2):

> May play a role in tumor angiogenesis.

**Summary**, from NCBI Gene [84898](https://www.ncbi.nlm.nih.gov/gene/84898):

> Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21013) · Entrez [84898](https://www.ncbi.nlm.nih.gov/gene/84898) · UniProt [Q6UX71](https://www.uniprot.org/uniprotkb/Q6UX71) · Ensembl [ENSG00000120594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120594)

## Data

Gene col 4193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4193); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4193]; `tensor/DDL_lfc|DDL_z.npy` [4193]; `embed/gene_vectors.npy` [4193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4193 or target_col == 4193). Every well: [[PLXDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
