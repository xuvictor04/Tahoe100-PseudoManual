---
symbol: "TNFRSF10C"
type: "gene"
col: 10398
ensembl_id: "ENSG00000173535"
name: "TNF receptor superfamily member 10c"
location: "8p21.3"
module: 20
arm: "-"
pooled_cpm: 3.95
n_lines_expressing: 33
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TNFRSF10C

*TNF receptor superfamily member 10c* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +8.3, q 8e-14, up in 9 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.527× (z -6.1, q 5e-07, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM98C]] (+0.53, fdr 1e-04), [[TERF2IP]] (+0.53, fdr 2e-05), [[DDB2]] (+0.53, fdr 3e-05); moves opposite to [[ELMOD2]] (-0.47, fdr 1e-04), [[DROSHA]] (-0.46, fdr 1e-04), [[HERC2]] (-0.45, fdr 1e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXB-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[CHCHD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.3 | 8e-14 | 9/23 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.0 | 5e-07 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.4 | 2e-05 | 4/14 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.6 | 5e-04 | 6/24 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.5 | 7e-04 | 1/7 (LS 180) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.012 | 3/29 (A-172, HS-578T, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.094 | 0/23 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.39× | +3.2 | 0.11 | 2/30 (CFPAC-1, A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -6.1 | 5e-07 | 19/30 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -5.3 | 3e-05 | 11/30 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -5.1 | 6e-05 | 12/20 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.584×** | -4.7 | 3e-04 | 12/29 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.622×** | -4.5 | 7e-04 | 10/30 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.648×** | -4.1 | 0.003 | 15/30 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -4.1 | 0.003 | 15/28 (SW 900, HEC-1-A, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -3.5 | 0.033 | 13/30 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.511×** | -3.3 | 0.051 | 5/28 (HEC-1-A, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.786×** | -3.2 | 0.063 | 7/30 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.712×** | -3.2 | 0.063 | 7/28 (COLO 205, H4, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.696×** | -3.2 | 0.069 | 8/28 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -3.1 | 0.094 | 10/27 (COLO 205, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.07 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0723× (z -19.5) |
| [[NCI-H460 (line)]] | wt | 2.05 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.48× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0745× (z -9.5) |
| [[LS 180 (line)]] | wt | 16.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +15.2) | — |
| [[NCI-H2030 (line)]] | alt | 7.57 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 7.23 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -9.5) |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.103× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 2.75 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0358× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 7.01 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0513× (z -10.7) |
| [[A-172 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.642 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM98C]] | +0.53 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[TERF2IP]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[DDB2]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[IRX2]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[MRPL27]] | +0.52 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[POLR1H]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[HOXA11]] | +0.51 | +0.24 / +0.59 | both halves | 5e-04 |  |
| [[ZNF440]] | +0.51 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[FLT3LG]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[CCNP]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[NR1H3]] | +0.50 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[TRIM5]] | +0.50 | +0.45 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD2]] | -0.47 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[DROSHA]] | -0.46 | -0.42 / -0.32 | both halves | 1e-04 |  |
| [[HERC2]] | -0.45 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[MMGT1]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[TALDO1]] | -0.45 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[PRKDC]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[CHCHD3]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[PABIR2]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CCNY]] | -0.44 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[VTI1B]] | -0.43 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[PRELID3B]] | -0.43 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.43 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB-AS1]] | B | HOXB-AS1 activity lowers TNFRSF10C's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.81× higher at baseline in the lines without HOXB-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHCHD3]] | B | TNFRSF10C activity lowers CHCHD3's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.40× higher at baseline in the lines without TNFRSF10C | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[HOXB-AS1]] | B | TNFRSF10C activity lowers HOXB-AS1's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.75× higher at baseline in the lines without TNFRSF10C | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[PI4KB]] | B | TNFRSF10C activity raises PI4KB's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.18× lower at baseline in the lines without TNFRSF10C | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[TRIM5]] | B | TNFRSF10C activity raises TRIM5's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.52× lower at baseline in the lines without TNFRSF10C | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[PDLIM2]] | B | TNFRSF10C activity raises PDLIM2's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.87× lower at baseline in the lines without TNFRSF10C | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[HERC2]] | B | TNFRSF10C activity lowers HERC2's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.40× higher at baseline in the lines without TNFRSF10C | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.1, 33.5); signed map (-4.6, 5.4). **Vector** length 43.8, 6.82% of its response variance represented; |z| ≥ 3 in 695 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.7 | +3.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.7 | +0.4 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +0.6 | +1.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -1.6 | -2.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.4 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 10c |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,102,921-23,117,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DcR1, TRAILR3, LIT, TRID, CD263 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Death Receptors and Ligands; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [O14798](https://www.uniprot.org/uniprotkb/O14798) (Tumor necrosis factor receptor superfamily member 10C):

> Acts as a receptor for the cytotoxic ligand TRAIL but does not contain the intracellular death domain required to initiate apoptosis. By competing with the functional TRAIL receptors TNFRSF10A and TNFRSF10B for ligand binding, it functions as a decoy receptor that protects cells from TRAIL-induced apoptosis.

**Summary**, from NCBI Gene [8794](https://www.ncbi.nlm.nih.gov/gene/8794):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor contains an extracellular TRAIL-binding domain and a transmembrane domain, but no cytoplasmic death domain. This receptor is not capable of inducing apoptosis, and is thought to function as an antagonistic receptor that protects cells from TRAIL-induced apoptosis. This gene was found to be a p53-regulated DNA damage-inducible gene. The expression of this gene was detected in many normal tissues but not …

**Accessions** — [HGNC:11906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11906) · Entrez [8794](https://www.ncbi.nlm.nih.gov/gene/8794) · UniProt [O14798](https://www.uniprot.org/uniprotkb/O14798) · Ensembl [ENSG00000173535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173535)

## Data

Gene col 10398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10398); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10398]; `tensor/DDL_lfc|DDL_z.npy` [10398]; `embed/gene_vectors.npy` [10398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10398 or target_col == 10398). Every well: [[TNFRSF10C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF10C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
