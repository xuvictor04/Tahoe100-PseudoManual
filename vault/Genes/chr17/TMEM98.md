---
symbol: "TMEM98"
type: "gene"
col: 100
ensembl_id: "ENSG00000006042"
name: "transmembrane protein 98"
location: "17q11.2"
module: 115
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 32
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# TMEM98

*transmembrane protein 98* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.45× (z +12.4, q 2e-32, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.95× (z +7.8, q 9e-13, up in 15 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -7.3, q 1e-10, down in 20 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.183×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMID1]] (+0.61, fdr 1e-05), [[HPSE]] (+0.59, fdr 7e-06), [[PRKCQ]] (+0.59, fdr 2e-05); moves opposite to [[DYNC2I1]] (-0.50, fdr 1e-04), [[AP3D1]] (-0.47, fdr 9e-05), [[BBOF1]] (-0.45, fdr 2e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATP6V0E2]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC27A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.45×** | +12.4 | 2e-32 | 5/6 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.50×** | +12.0 | 1e-30 | 1/1 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +8.7 | 7e-16 | 1/1 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +7.8 | 9e-13 | 15/30 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.88×** | +7.4 | 2e-11 | 13/28 (LoVo, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.36×** | +7.1 | 1e-10 | 12/24 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.0 | 2e-07 | 7/10 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.8 | 5e-07 | 7/18 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.4 | 6e-04 | 2/13 (HCT15, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.3 | 9e-04 | 3/12 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.002 | 8/29 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.70×** | +4.1 | 0.002 | 3/17 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.88×** | +3.7 | 0.008 | 4/18 (HOP62, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.88×** | +3.7 | 0.008 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.7 | 0.010 | 1/9 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.014 | 6/24 (HOP62, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.034 | 2/27 (NCI-H460, SHP-77) | all doses, stronger at high dose |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.037 | 4/23 (SHP-77, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.040 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.67×** | +3.0 | 0.071 | 2/20 (LoVo, HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.65×** | +3.0 | 0.083 | 1/18 (NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 100.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.183×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -7.3 | 1e-10 | 20/25 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -4.7 | 9e-04 | 16/25 (HCT15, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.686× | -3.1 | 0.33 | 6/30 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -8.7) |
| [[A-172 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.566 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.619 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.654 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.698 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.614 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMID1]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[HPSE]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PRKCQ]] | +0.59 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[RAB15]] | +0.56 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[ABHD14A]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TTPA]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[XK]] | +0.53 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[LYSMD2]] | +0.53 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[CCDC69]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[HAGLR]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[MTMR8]] | +0.51 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[ZNF385B]] | +0.51 | +0.24 / +0.62 | both halves | 4e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2I1]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[AP3D1]] | -0.47 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[BBOF1]] | -0.45 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[TAF1]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CEP104]] | -0.44 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[MAPK8IP3]] | -0.42 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[UACA]] | -0.42 | -0.34 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0E2]] | B | ATP6V0E2 activity lowers TMEM98's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 1.78× higher at baseline in the lines without ATP6V0E2 | 0.057 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC27A2]] | B | TMEM98 activity raises SLC27A2's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without TMEM98 | 0.072 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[PRKCQ]] | B | TMEM98 activity raises PRKCQ's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without TMEM98 | 0.083 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[DNAJC22]] | B | TMEM98 activity raises DNAJC22's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.11× lower at baseline in the lines without TMEM98 | 0.087 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[HAGLR]] | B | TMEM98 activity raises HAGLR's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without TMEM98 | 0.098 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.0, 37.0); signed map (53.2, 30.3). **Vector** length 31.9, 4.16% of its response variance represented; |z| ≥ 3 in 547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -1.2 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -4.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 98 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,927,910-32,945,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564K1964 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Y6](https://www.uniprot.org/uniprotkb/Q9Y2Y6) (Transmembrane protein 98):

> Functions as a negative regulator of MYRF in oligodendrocyte differentiation and myelination. Interacts with the C-terminal of MYRF inhibiting MYRF self-cleavage and N-fragment nuclear translocation. The secreted form promotes differentiation of T helper 1 cells (Th1).

**Summary**, from NCBI Gene [26022](https://www.ncbi.nlm.nih.gov/gene/26022):

> This gene encodes a transmembrane protein. A missense mutation in this gene result in Nanophthalmos 4 (NNO4). Alternatively spliced transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:24529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24529) · Entrez [26022](https://www.ncbi.nlm.nih.gov/gene/26022) · UniProt [Q9Y2Y6](https://www.uniprot.org/uniprotkb/Q9Y2Y6) · Ensembl [ENSG00000006042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006042)

## Data

Gene col 100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 100); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 100]; `tensor/DDL_lfc|DDL_z.npy` [100]; `embed/gene_vectors.npy` [100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 100 or target_col == 100). Every well: [[TMEM98 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM98.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
