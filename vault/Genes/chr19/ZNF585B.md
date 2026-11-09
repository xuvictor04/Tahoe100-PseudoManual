---
symbol: "ZNF585B"
type: "gene"
col: 14439
ensembl_id: "ENSG00000245680"
name: "zinc finger protein 585B"
location: "19q13.12"
module: 16
arm: "+"
pooled_cpm: 15.39
n_lines_expressing: 38
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF585B

*zinc finger protein 585B* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.38× (z +6.4, q 9e-08, up in 16 of 36 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.374× (z -13.7, q 1e-39, down in 30 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.609× (z -6.9, q 6e-10, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF594]] (+0.64, fdr 1e-05), [[ZNF155]] (+0.64, fdr 7e-06), [[ZNF829]] (+0.62, fdr 1e-05); moves opposite to [[RALGPS1]] (-0.54, fdr 3e-05), [[SETD3]] (-0.54, fdr 4e-05), [[DAG1]] (-0.51, fdr 9e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF528-AS1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF585A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.38×** | +6.4 | 9e-08 | 16/36 (AsPC-1, A-172, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.0 | 0.021 | 9/35 (A549, HCT15, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.18 | 12/36 (RKO, J82, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.30× | +3.2 | 0.21 | 4/36 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.25× | +3.0 | 0.22 | 8/35 (H4, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.374×** | -13.7 | 1e-39 | 30/36 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.425×** | -11.9 | 4e-30 | 26/35 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.488×** | -10.0 | 5e-21 | 29/35 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.538×** | -8.6 | 1e-15 | 23/35 (PANC-1, CHP-212, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.600×** | -7.1 | 1e-10 | 18/30 (SW 900, NCI-H460, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -6.9 | 6e-10 | 20/35 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.612×** | -6.6 | 5e-09 | 12/16 (NCI-H460, NCI-H1792, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.668×** | -5.4 | 5e-06 | 18/29 (J82, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.707×** | -4.8 | 1e-04 | 17/32 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.709×** | -4.8 | 1e-04 | 18/36 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -4.6 | 2e-04 | 18/35 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.745×** | -4.1 | 0.002 | 17/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.745×** | -4.1 | 0.002 | 16/35 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.815×** | -4.0 | 0.002 | 15/35 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.764×** | -3.7 | 0.007 | 14/36 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.095 | 7/36 (SW 1088, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 44.7 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H460 (line)]] | wt | 67.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0487× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[AsPC-1 (line)]] | alt | 7.27 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 35.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0947× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0965× (z -9.7) |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0483× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0686× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 18.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.195× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF594]] | +0.64 | +0.50 / +0.71 | both halves | 1e-05 | same gene group |
| [[ZNF155]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF829]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | same gene group |
| [[FAM200A]] | +0.62 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[ZNF226]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[SLC35G2]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZNF429]] | +0.61 | +0.57 / +0.45 | both halves | 3e-05 | same gene group |
| [[ZNF780B]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | same gene group |
| [[ZNF585A]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 | same gene group; ⚠ same locus (8.8 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF234]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZNF407-AS1]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF793]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF189]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGPS1]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SETD3]] | -0.54 | -0.40 / -0.59 | both halves | 4e-05 |  |
| [[DAG1]] | -0.51 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[TBC1D24]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF528-AS1]] | B | ZNF528-AS1 activity raises ZNF585B's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without ZNF528-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880 |
| [[ZNF528]] | B | ZNF528 activity raises ZNF585B's level | lines that do not express ZNF528 (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without ZNF528 | 0.020 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, ZNF625, ZNF880 |
| [[ZNF585A]] | B | ZNF585A activity raises ZNF585B's level | lines that do not express ZNF585A (6) vs lines expressing it (44) | 3.77× lower at baseline in the lines without ZNF585A | 0.076 | ⚠ within organs, on part of the lines; also absent: ZFP14, WWTR1, ZNF540 |
| [[ZNF234]] | C | ZNF234 activity raises ZNF585B's level | lines that do not express ZNF234 (4) vs lines expressing it (46) | 3.65× lower at baseline in the lines without ZNF234 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF222, ZNF551, ZNF264 |
| [[TP53]] | C | TP53 activity weakens ZNF585B's drug response | recorded loss-of-function mutation of TP53 in 23 lines vs 13 not recorded | the TP53-altered lines respond 1.76× as strongly (z diff -1.88); strongest at Dinaciclib 5 µM: 0.38x vs 0.92x (z diff -3.9) | 0.847 over the table, 0.066 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF585A]] | B | ZNF585B activity raises ZNF585A's level | lines that do not express ZNF585B (12) vs lines expressing it (38) | 2.62× lower at baseline in the lines without ZNF585B | 0.025 | ⚠ within organs, on part of the lines; also absent: CYBRD1 |
| [[ZNF415]] | B | ZNF585B activity raises ZNF415's level | lines that do not express ZNF585B (12) vs lines expressing it (38) | 2.77× lower at baseline in the lines without ZNF585B | 0.081 | ⚠ within organs, on part of the lines; also absent: CYBRD1 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.9, 13.9); signed map (1.5, -24.1). **Vector** length 59.3, 10.4% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.0 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.0 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -3.0 | -7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -2.9 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -2.6 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | -2.4 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 585B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:37,181,579-37,218,153 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14928, SZFP41, Zfp27 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q52M93](https://www.uniprot.org/uniprotkb/Q52M93) (Zinc finger protein 585B):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [92285](https://www.ncbi.nlm.nih.gov/gene/92285):

> Predicted to enable transcription cis-regulatory region binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30948) · Entrez [92285](https://www.ncbi.nlm.nih.gov/gene/92285) · UniProt [Q52M93](https://www.uniprot.org/uniprotkb/Q52M93) · Ensembl [ENSG00000245680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245680)

## Data

Gene col 14439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14439); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14439]; `tensor/DDL_lfc|DDL_z.npy` [14439]; `embed/gene_vectors.npy` [14439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14439 or target_col == 14439). Every well: [[ZNF585B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF585B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
