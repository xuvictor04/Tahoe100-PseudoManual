---
symbol: "SLC26A6"
type: "gene"
col: 13477
ensembl_id: "ENSG00000225697"
name: "solute carrier family 26 member 6"
location: "3p21.31"
module: 180
arm: "+"
pooled_cpm: 14.15
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# SLC26A6

*solute carrier family 26 member 6* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.75× (z +12.6, q 7e-34, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.571× (z -6.5, q 5e-08, down in 21 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.633× (z -5.5, q 1e-05, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHDC1]] (+0.73, fdr 7e-06), [[TCIRG1]] (+0.72, fdr 1e-05), [[EFNA4]] (+0.71, fdr 1e-05); moves opposite to [[TASOR]] (-0.63, fdr 1e-05), [[YARS2]] (-0.62, fdr 1e-04), [[DPH5-DT]] (-0.61, fdr 1e-04).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +12.6 | 7e-34 | 43/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.38×** | +10.8 | 6e-25 | 39/47 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +9.1 | 2e-17 | 36/46 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +6.3 | 6e-08 | 30/47 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.003 | 18/45 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.007 | 18/45 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.008 | 12/46 (SNU-423, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.072 | 11/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | 1.29× | +3.1 | 0.13 | 2/46 (NCI-H2030, SK-MEL-2) | top dose only | plate-row cell shift; position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.0 | 0.15 | 6/47 (SHP-77, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.571×** | -6.5 | 5e-08 | 21/29 (SNU-423, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.633×** | -5.5 | 1e-05 | 24/45 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -5.4 | 1e-05 | 27/47 (Hs 766T, SNU-423, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -4.8 | 2e-04 | 19/26 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.509×** | -4.4 | 0.001 | 18/42 (NCI-H2347, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.2 | 0.003 | 23/43 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.718×** | -4.1 | 0.003 | 19/36 (SNU-423, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.714×** | -4.0 | 0.004 | 19/46 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.019 | 16/47 (SW 1088, CHP-212, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -3.5 | 0.029 | 15/47 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -3.1 | 0.091 | 19/40 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 11.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.46× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0495× (z -17.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -9.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | +0.73 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TCIRG1]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 | same gene group |
| [[EFNA4]] | +0.71 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NCKIPSD]] | +0.71 | +0.69 / +0.52 | both halves | 1e-05 | ⚠ same locus (38.4 kb, same strand: neighbours can correlate without regulation) |
| [[STK32C]] | +0.69 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.68 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[PLEKHH3]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MKNK2]] | +0.67 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PKD1]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 | same gene group |
| [[RAB3A]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MPND]] | +0.66 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DNAAF3]] | +0.66 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[PEDS1]] | +0.66 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[YARS2]] | -0.62 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.61 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[UTP20]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[GABPB1]] | -0.59 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ST7L]] | -0.59 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MED1]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[AP5M1]] | -0.58 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[DPP8]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ALG8]] | -0.57 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[GABPB2]] | -0.57 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SLC26A6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.9, -4.4); signed map (-31.0, 19.0). **Vector** length 90.6, 18.4% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +9.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 26 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,625,723-48,635,493 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586E1422 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 26 |
| Reactome | 4 pathways, smallest: Inorganic anion exchange by SLC26 transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXS9](https://www.uniprot.org/uniprotkb/Q9BXS9) (Solute carrier family 26 member 6):

> Apical membrane anion-exchanger with wide epithelial distribution that plays a role as a component of the pH buffering system for maintaining acid-base homeostasis. Acts as a versatile DIDS-sensitive inorganic and organic anion transporter that mediates the uptake of monovalent anions like chloride, bicarbonate, formate and hydroxyl ion and divalent anions like sulfate and oxalate. Functions in multiple exchange modes involving pairs of these anions, which include chloride-bicarbonate, …

**Summary**, from NCBI Gene [65010](https://www.ncbi.nlm.nih.gov/gene/65010):

> This gene belongs to the solute carrier 26 family, whose members encode anion transporter proteins. This particular family member encodes a protein involved in transporting chloride, oxalate, sulfate and bicarbonate. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:14472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14472) · Entrez [65010](https://www.ncbi.nlm.nih.gov/gene/65010) · UniProt [Q9BXS9](https://www.uniprot.org/uniprotkb/Q9BXS9) · Ensembl [ENSG00000225697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225697)

## Data

Gene col 13477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13477); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13477]; `tensor/DDL_lfc|DDL_z.npy` [13477]; `embed/gene_vectors.npy` [13477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13477 or target_col == 13477). Every well: [[SLC26A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC26A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
