---
symbol: "NALF1"
type: "gene"
col: 12875
ensembl_id: "ENSG00000204442"
name: "NALCN channel auxiliary factor 1"
location: "13q33.3"
module: 13
arm: "+"
pooled_cpm: 361.29
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NALF1

*NALCN channel auxiliary factor 1* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +10.3, q 4e-22, up in 9 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.590× (z -7.1, q 7e-10, down in 18 of 19 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.648× (z -6.1, q 3e-07, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH13]] (+0.73, fdr 7e-06), [[SAMD3]] (+0.70, fdr 7e-06), [[TCF4]] (+0.70, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[PDE3A]] → it (grade C ⚠); 11 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +10.3 | 4e-22 | 9/20 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.3 | 7e-08 | 1/19 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.5 | 9e-06 | 1/21 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.5 | 0.001 | 4/20 (A-427, SNU-423, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.011 | 12/21 (CFPAC-1, C-33 A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.042 | 1/22 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.043 | 14/20 (A-172, NCI-H2347, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.060 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.060 | 8/20 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +3.3 | 0.060 | 9/20 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.087 | 0/20 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -7.1 | 7e-10 | 18/19 (SHP-77, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.648×** | -6.1 | 3e-07 | 15/20 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -5.0 | 1e-04 | 13/20 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.689×** | -4.8 | 2e-04 | 7/20 (HOP62, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.728×** | -4.5 | 9e-04 | 13/20 (LS 180, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.688×** | -4.3 | 0.001 | 11/19 (CHP-212, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -4.2 | 0.002 | 12/20 (C-33 A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.602×** | -3.7 | 0.014 | 11/20 (HS-578T, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.762×** | -3.6 | 0.021 | 0/20 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.5 | 0.028 | 1/22 (HOP62) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.784×** | -3.4 | 0.033 | 9/19 (LS 180, H4, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.629×** | -3.4 | 0.033 | 12/20 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.635×** | -3.3 | 0.039 | 4/20 (H4, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.795×** | -3.2 | 0.054 | 13/20 (SHP-77, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 1,013 | 0 | 18 (13 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -18.7) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.213× (z -13.2) |
| [[A-427 (line)]] | wt | 94.7 | 10 (8 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -8.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 1,221 | 0 | 8 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1,473 | 0 | 8 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.187× (z -12.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 300 | 3 (1 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.68× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.324× (z -10.8) ⚠ cell-cycle shift, explains ~91% of this change |
| [[SHP-77 (line)]] | alt | 2,928 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -17.1) ⚠ toxic |
| [[H4 (line)]] | wt | 1,269 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.226× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 1,146 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -15.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 617 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -11.2) ⚠ toxic |
| [[J82 (line)]] | alt | 1,927 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 2,132 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 138 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +17.2) | — |
| [[SW 900 (line)]] | alt | 171 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +11.2) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 242 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.20× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 669 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -9.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 435 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 180 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.9) | — |
| [[A-172 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 88.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 73.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 60.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 32.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 30.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 27.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 41.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 39.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 40.7 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 532 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 70.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 46.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 33.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 28.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 41.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 28.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH13]] | +0.73 | +0.61 / +0.79 | both halves | 7e-06 | same gene group |
| [[SAMD3]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TCF4]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PDE3A]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ADAMTS6]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NETO1]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[HS3ST3A1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[LRFN5]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SPOCK1]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ADAMTS12]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[BAALC]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE3A]] | C | PDE3A activity raises NALF1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 5.72× lower at baseline in the lines without PDE3A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises NALF1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.38× lower at baseline in the lines without TRPC4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[LRFN5]] | C | LRFN5 activity raises NALF1's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 5.58× lower at baseline in the lines without LRFN5 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises NALF1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 8.68× lower at baseline in the lines without NETO1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[LINC01060]] | C | LINC01060 activity raises NALF1's level | lines that do not express LINC01060 (29) vs lines expressing it (21) | 3.31× lower at baseline in the lines without LINC01060 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, ENSG00000287598, NTM; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises NALF1's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 4.01× lower at baseline in the lines without KCNE4 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises NALF1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 6.21× lower at baseline in the lines without PDGFRB | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[FBN2]] | C | FBN2 activity raises NALF1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 5.29× lower at baseline in the lines without FBN2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises NALF1's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 4.00× lower at baseline in the lines without TMEM200A | 0.037 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[HGF]] | C | HGF activity raises NALF1's level | lines that do not express HGF (38) vs lines expressing it (12) | 4.75× lower at baseline in the lines without HGF | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises NALF1's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 3.43× lower at baseline in the lines without SAMD3 | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[ADGRB3]] | C | ADGRB3 activity raises NALF1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.92× lower at baseline in the lines without ADGRB3 | 0.069 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | NALF1 activity raises LSAMP's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without NALF1 | 0.065 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837 |
| [[EVA1A]] | B | NALF1 activity raises EVA1A's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without NALF1 | 0.066 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837 |
| [[NTNG1]] | C | NALF1 activity raises NTNG1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 3.16× lower at baseline in the lines without NALF1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[RIMS1]] | C | NALF1 activity raises RIMS1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.50× lower at baseline in the lines without NALF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[NETO1]] | C | NALF1 activity raises NETO1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without NALF1 | 0.025 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[ADGRB3]] | C | NALF1 activity raises ADGRB3's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 4.48× lower at baseline in the lines without NALF1 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[TMEM200A]] | C | NALF1 activity raises TMEM200A's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.86× lower at baseline in the lines without NALF1 | 0.043 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[FBN2]] | C | NALF1 activity raises FBN2's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 3.17× lower at baseline in the lines without NALF1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[HS3ST3A1]] | C | NALF1 activity raises HS3ST3A1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 3.93× lower at baseline in the lines without NALF1 | 0.058 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[SAMD3]] | C | NALF1 activity raises SAMD3's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.87× lower at baseline in the lines without NALF1 | 0.069 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[MME]] | C | NALF1 activity raises MME's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 4.42× lower at baseline in the lines without NALF1 | 0.072 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, 21.5); signed map (20.1, 47.4). **Vector** length 102, 36.3% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.7 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NALCN channel auxiliary factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:107,163,510-107,867,496 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NLF-1; previously FAM155A |
| Gene groups (HGNC) | MicroRNA protein coding host genes; NALCN channel complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [B1AL88](https://www.uniprot.org/uniprotkb/B1AL88) (NALCN channel auxiliary factor 1):

> Auxilary subunit component of the NALCN channelosome complex, which regulates the resting membrane potential by depolarizing sodium leak currents. The NALCN channelosome complex is a voltage-gated ion channel responsible for the resting Na(+) permeability that controls neuronal excitability. The NALCN channelosome is constitutively active and conducts monovalent cations but is blocked by physiological concentrations of extracellular divalent cations.

**Summary**, from NCBI Gene [728215](https://www.ncbi.nlm.nih.gov/gene/728215):

> Predicted to contribute to stretch-activated, monoatomic cation-selective, calcium channel activity. Involved in regulation of neuronal action potential and sodium ion transmembrane transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33877) · Entrez [728215](https://www.ncbi.nlm.nih.gov/gene/728215) · UniProt [B1AL88](https://www.uniprot.org/uniprotkb/B1AL88) · Ensembl [ENSG00000204442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204442)

## Data

Gene col 12875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12875); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12875]; `tensor/DDL_lfc|DDL_z.npy` [12875]; `embed/gene_vectors.npy` [12875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12875 or target_col == 12875). Every well: [[NALF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NALF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
