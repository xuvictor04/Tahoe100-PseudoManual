---
symbol: "FES"
type: "gene"
col: 11293
ensembl_id: "ENSG00000182511"
name: "FES proto-oncogene, tyrosine kinase"
location: "15q26.1"
module: 38
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 39
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# FES

*FES proto-oncogene, tyrosine kinase* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.02× (z +11.0, q 2e-25, up in 21 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.381× (z -6.8, q 5e-09, down in 22 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1C]] (+0.68, fdr 7e-06), [[SMIM41]] (+0.67, fdr 7e-06), [[A3GALT2]] (+0.67, fdr 7e-06); moves opposite to [[VPS41]] (-0.51, fdr 6e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K2]] → it (grade B ⚠); 7 go from it, the strongest it → [[FURIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +11.0 | 2e-25 | 21/24 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.23×** | +8.0 | 5e-13 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.32×** | +5.9 | 6e-07 | 1/8 (HEC-1-A) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +5.8 | 8e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +5.6 | 2e-06 | 2/9 (NCI-H460, LoVo) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +4.0 | 0.005 | 9/34 (HCT15, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.0 | 0.005 | 4/16 (HCT15, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.030 | 2/33 (HT-29, NCI-H2030) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.050 | 4/27 (C32, NCI-H1792, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.58× | +3.1 | 0.12 | 2/27 (SW480, LOX-IMVI) | top dose only | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.381×** | -6.8 | 5e-09 | 22/32 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -5.3 | 3e-05 | 12/29 (SHP-77, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.569×** | -4.0 | 0.012 | 9/34 (A-172, NCI-H1573, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.563×** | -3.8 | 0.023 | 11/34 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.625×** | -3.7 | 0.027 | 7/35 (SK-MEL-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -3.6 | 0.033 | 15/34 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.640×** | -3.3 | 0.086 | 10/34 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -3.2 | 0.097 | 11/35 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.700× | -3.1 | 0.11 | 7/31 (hTERT-HPNE, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.433× | -3.1 | 0.11 | 8/27 (NCI-H1573, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0403× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0450× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0227× (z -14.5) |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0369× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0406× (z -10.9) |
| [[A-172 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.728 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.628 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.635 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.860 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1C]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[XG]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[F2]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PYGM]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[AVIL]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[FNDC7]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CHADL]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SH2D4B]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 | same gene group |
| [[RFPL3S]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TTLL13]] | +0.61 | +0.53 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS41]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises FES's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FURIN]] | B | FES activity raises FURIN's level | lines that do not express FES (11) vs lines expressing it (39) | 2.24× lower at baseline in the lines without FES | 0.014 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[POU2F2]] | B | FES activity raises POU2F2's level | lines that do not express FES (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without FES | 0.063 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[SCAT1]] | B | FES activity raises SCAT1's level | lines that do not express FES (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without FES | 0.076 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[A3GALT2]] | B | FES activity raises A3GALT2's level | lines that do not express FES (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without FES | 0.078 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[ADCY10P1]] | B | FES activity raises ADCY10P1's level | lines that do not express FES (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without FES | 0.090 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | FES activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express FES (11) vs lines expressing it (37) | the lines without FES: 1.23× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[AZU1]] | B | FES activity lowers AZU1's level | lines that do not express FES (11) vs lines expressing it (39) | 1.64× higher at baseline in the lines without FES | 0.096 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.5, -17.8); signed map (15.7, 13.9). **Vector** length 48.9, 7.82% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | FES proto-oncogene, tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,883,695-90,895,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FPS |
| Gene groups (HGNC) | SH2 domain containing; F-BAR domain containing; Fes family tyrosine kinases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 8 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; CRMPs in Sema3A signaling; Sema3A PAK dependent Axon repulsion |
| Matched by | ensembl_id |

**Function**, from UniProt [P07332](https://www.uniprot.org/uniprotkb/P07332) (Tyrosine-protein kinase Fes/Fps):

> Tyrosine-protein kinase that acts downstream of cell surface receptors and plays a role in the regulation of the actin cytoskeleton, microtubule assembly, cell attachment and cell spreading. Plays a role in FCER1 (high affinity immunoglobulin epsilon receptor)-mediated signaling in mast cells. Acts down-stream of the activated FCER1 receptor and the mast/stem cell growth factor receptor KIT. Plays a role in the regulation of mast cell degranulation. Plays a role in the regulation of cell …

**Summary**, from NCBI Gene [2242](https://www.ncbi.nlm.nih.gov/gene/2242):

> This gene encodes the human cellular counterpart of a feline sarcoma retrovirus protein with transforming capabilities. The gene product has tyrosine-specific protein kinase activity and that activity is required for maintenance of cellular transformation. Its chromosomal location has linked it to a specific translocation event identified in patients with acute promyelocytic leukemia but it is also involved in normal hematopoiesis as well as growth factor and cytokine receptor signaling. …

**Accessions** — [HGNC:3657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3657) · Entrez [2242](https://www.ncbi.nlm.nih.gov/gene/2242) · UniProt [P07332](https://www.uniprot.org/uniprotkb/P07332) · Ensembl [ENSG00000182511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182511)

## Data

Gene col 11293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11293); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11293]; `tensor/DDL_lfc|DDL_z.npy` [11293]; `embed/gene_vectors.npy` [11293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11293 or target_col == 11293). Every well: [[FES — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FES.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
