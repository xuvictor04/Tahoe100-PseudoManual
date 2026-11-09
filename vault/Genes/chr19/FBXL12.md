---
symbol: "FBXL12"
type: "gene"
col: 4811
ensembl_id: "ENSG00000127452"
name: "F-box and leucine rich repeat protein 12"
location: "19p13.2"
module: 212
arm: "+"
pooled_cpm: 16.02
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# FBXL12

*F-box and leucine rich repeat protein 12* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +13.0, q 8e-36, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.621× (z -9.0, q 2e-16, down in 23 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.792× (z -4.2, q 0.002, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 0.166×, HS-578T 0.158×, MIA PaCa-2 0.155×, Hs 766T 0.157×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 0.164×, A498 0.360×, hTERT-HPNE 0.181×, HS-578T 0.304×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HS-578T 0.207×, Panc 03.27 0.189×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSWIM8]] (+0.67, fdr 1e-05), [[C19orf25]] (+0.66, fdr 7e-06), [[RABGEF1]] (+0.65, fdr 7e-06); moves opposite to [[G3BP1]] (-0.72, fdr 7e-06), [[IPO8]] (-0.61, fdr 2e-05), [[ZDHHC21]] (-0.60, fdr 3e-05).
> It is in [[Module 212]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF816-ZNF321P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +13.0 | 8e-36 | 34/46 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +9.2 | 1e-17 | 35/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.8 | 1e-06 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.25×** | +4.1 | 0.006 | 16/48 (SW1417, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.5 | 0.042 | 13/45 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.042 | 9/47 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +3.3 | 0.069 | 11/48 (SW480, RKO, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.069 | 13/46 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.13× | +3.2 | 0.086 | 8/48 (A549, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.096 | 8/47 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.10 | 5/47 (NCI-H1792, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 0.166×, HS-578T 0.158×, MIA PaCa-2 0.155×, Hs 766T 0.157×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 0.164×, A498 0.360×, hTERT-HPNE 0.181×, HS-578T 0.304×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HS-578T 0.207×, Panc 03.27 0.189×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -9.0 | 2e-16 | 23/39 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -7.1 | 4e-10 | 18/30 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.730×** | -5.5 | 9e-06 | 20/34 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -4.6 | 6e-04 | 21/43 (J82, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.790×** | -4.4 | 0.001 | 15/45 (NCI-H23, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.799×** | -4.2 | 0.002 | 14/47 (A-172, H4, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.792×** | -4.2 | 0.002 | 13/47 (KATO III, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -4.0 | 0.005 | 16/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.707×** | -3.4 | 0.041 | 7/43 (COLO 205, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 25.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.115× (z -9.2) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -14.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -12.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.5) | — |
| [[A-172 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM8]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SDF2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ATAT1]] | +0.64 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMEM134]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[QPCTL]] | +0.63 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[RABAC1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZNF324]] | +0.60 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[PEX16]] | +0.60 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[HIC2]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZNF200]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[G3BP1]] | -0.72 | -0.59 / -0.75 | both halves | 7e-06 |  |
| [[IPO8]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ZDHHC21]] | -0.60 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[ATIC]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[CEP41]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[DHX9]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[VPS13A]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[AGPS]] | -0.58 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[MYO5C]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[HUWE1]] | -0.56 | -0.38 / -0.62 | both halves | 7e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[EWSR1]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[CDH2]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF816-ZNF321P]] | B | ZNF816-ZNF321P activity raises FBXL12's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without ZNF816-ZNF321P | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[MYO5C]] | B | MYO5C activity lowers FBXL12's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 1.30× higher at baseline in the lines without MYO5C | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-24.5, -32.7); signed map (-18.5, 1.1). **Vector** length 78.6, 13.9% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +9.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:9,810,267-9,827,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20188, Fbl12 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXK8](https://www.uniprot.org/uniprotkb/Q9NXK8) (F-box/LRR-repeat protein 12):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Mediates the polyubiquitination and proteasomal degradation of CAMK1 leading to disruption of cyclin D1/CDK4 complex assembly which results in G1 cell cycle arrest in lung epithelia.

**Summary**, from NCBI Gene [54850](https://www.ncbi.nlm.nih.gov/gene/54850):

> Members of the F-box protein family, such as FBXL12, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13611) · Entrez [54850](https://www.ncbi.nlm.nih.gov/gene/54850) · UniProt [Q9NXK8](https://www.uniprot.org/uniprotkb/Q9NXK8) · Ensembl [ENSG00000127452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127452)

## Data

Gene col 4811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4811); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4811]; `tensor/DDL_lfc|DDL_z.npy` [4811]; `embed/gene_vectors.npy` [4811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4811 or target_col == 4811). Every well: [[FBXL12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
