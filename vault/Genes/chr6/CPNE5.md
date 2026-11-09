---
symbol: "CPNE5"
type: "gene"
col: 4566
ensembl_id: "ENSG00000124772"
name: "copine 5"
location: "6p21.2"
module: 84
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# CPNE5

*copine 5* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +9.6, q 5e-19, up in 21 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.457× (z -7.9, q 2e-12, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL13A1]] (+0.64, fdr 7e-06), [[SHC4]] (+0.62, fdr 1e-05), [[KCNN4]] (+0.61, fdr 1e-05); moves opposite to [[HNF4G]] (-0.50, fdr 6e-05), [[ARFGEF2]] (-0.47, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GBX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +9.6 | 5e-19 | 21/41 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +9.2 | 8e-18 | 1/6 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.2 | 1e-10 | 7/28 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +6.7 | 4e-09 | 16/30 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.0 | 2e-07 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.0 | 0.006 | 1/16 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.36× | +3.1 | 0.12 | 4/37 (HOP62, C-33 A, …) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.12 | 5/21 (A-172, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 1.37× | +3.1 | 0.12 | 1/16 (A-427) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.12 | 3/22 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.52× | +3.0 | 0.14 | 1/10 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.457×** | -7.9 | 2e-12 | 25/41 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -7.2 | 2e-10 | 22/33 (C-33 A, HOP62, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -7.0 | 3e-10 | 17/29 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.584×** | -5.2 | 3e-05 | 17/35 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -4.9 | 1e-04 | 16/27 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.599×** | -4.8 | 2e-04 | 9/39 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.662×** | -4.1 | 0.003 | 15/20 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -4.1 | 0.003 | 17/35 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.689×** | -3.7 | 0.012 | 15/41 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -3.4 | 0.034 | 14/32 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.703×** | -3.4 | 0.034 | 10/41 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.034 | 10/28 (C32, C-33 A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.537×** | -3.3 | 0.047 | 3/35 (SW 900, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.794×** | -3.2 | 0.059 | 6/40 (C32, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.6 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0233× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -12.0) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -18.0) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0291× (z -17.4) |
| [[C32 (line)]] | wt | 14.3 | 0 | 3 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0424× (z -9.6) |
| [[A-427 (line)]] | wt | 5.19 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0938× (z -9.6) |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 2 | — | [[Altretamine (drug)]] 5 µM 0.0575× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 7.17 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0344× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 5.62 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0341× (z -10.8) |
| [[H4 (line)]] | wt | 10.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0505× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 5.18 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0517× (z -10.2) |
| [[PANC-1 (line)]] | alt | 2.39 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0629× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0852× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 2.22 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0550× (z -10.6) |
| [[A498 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL13A1]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SHC4]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[KCNN4]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EFEMP2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TMEM255B]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[GALNT18]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TLE6]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[STAG3]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[EFR3B]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PYGL]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.57 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ARFGEF2]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX1]] | B | GBX1 activity raises CPNE5's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without GBX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises CPNE5's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without LINC02813 | 0.043 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[LINC02813]] | B | LINC02813 activity strengthens CPNE5's drug response | lines that do not express LINC02813 (21) vs lines expressing it (21) | the lines without LINC02813 respond 0.70× as strongly (z diff +0.61); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.33x (z diff +2.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; target measured in part of the lines; artifact flags |
| [[SDK1]] | B | SDK1 activity strengthens CPNE5's drug response | lines that do not express SDK1 (19) vs lines expressing it (23) | the lines without SDK1 respond 0.54× as strongly (z diff +0.98); strongest at Ouabain (Octahydrate) 0.5 µM: 0.71x vs 0.28x (z diff +3.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; target measured in part of the lines; artifact flags |
| [[PYGL]] | B | PYGL activity raises CPNE5's level | lines that do not express PYGL (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without PYGL | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |
| [[APOBEC3G]] | B | APOBEC3G activity raises CPNE5's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without APOBEC3G | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.1, 4.9); signed map (2.3, 51.7). **Vector** length 67.7, 12.5% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +7.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -7.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | copine 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:36,740,775-36,839,444 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPN5, COPN5, KIAA1599 |
| Gene groups (HGNC) | Copines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCH3](https://www.uniprot.org/uniprotkb/Q9HCH3) (Copine-5):

> Probable calcium-dependent phospholipid-binding protein that may play a role in calcium-mediated intracellular processes (By similarity). Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [57699](https://www.ncbi.nlm.nih.gov/gene/57699):

> Calcium-dependent membrane-binding proteins may regulate molecular events at the interface of the cell membrane and cytoplasm. This gene is one of several genes that encode a calcium-dependent protein containing two N-terminal type II C2 domains and an integrin A domain-like sequence in the C-terminus. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene. More variants may exist, but their full-length natures could not be determined. …

**Accessions** — [HGNC:2318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2318) · Entrez [57699](https://www.ncbi.nlm.nih.gov/gene/57699) · UniProt [Q9HCH3](https://www.uniprot.org/uniprotkb/Q9HCH3) · Ensembl [ENSG00000124772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124772)

## Data

Gene col 4566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4566); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4566]; `tensor/DDL_lfc|DDL_z.npy` [4566]; `embed/gene_vectors.npy` [4566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4566 or target_col == 4566). Every well: [[CPNE5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
