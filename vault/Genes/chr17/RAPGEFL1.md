---
symbol: "RAPGEFL1"
type: "gene"
col: 2936
ensembl_id: "ENSG00000108352"
name: "Rap guanine nucleotide exchange factor like 1"
location: "17q21.1"
module: 47
arm: "+"
pooled_cpm: 8.17
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# RAPGEFL1

*Rap guanine nucleotide exchange factor like 1* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.63× (z +6.9, q 2e-09, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.630× (z -6.7, q 2e-08, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFAP2E]] (+0.63, fdr 7e-06), [[FAM131A]] (+0.62, fdr 2e-05), [[ST6GALNAC6-1]] (+0.61, fdr 3e-05); moves opposite to [[LNPEP]] (-0.51, fdr 4e-05), [[TMEM69]] (-0.50, fdr 1e-04), [[MAP3K1]] (-0.49, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +6.9 | 2e-09 | 24/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.1 | 4e-07 | 17/48 (KATO III, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +5.6 | 4e-06 | 21/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 5e-05 | 20/47 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.047 | 15/45 (NCI-H2030, CFPAC-1, …) | top dose only | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.047 | 10/45 (C-33 A, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 1.50× | +3.0 | 0.21 | 2/41 (KATO III, LOX-IMVI) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -6.7 | 2e-08 | 22/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.3 | 5e-08 | 23/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.635×** | -6.3 | 5e-08 | 20/46 (A498, H4, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.436×** | -6.3 | 5e-08 | 20/39 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -5.9 | 5e-07 | 21/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.681×** | -5.3 | 8e-06 | 14/45 (NCI-H23, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.512×** | -5.0 | 4e-05 | 15/46 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -4.8 | 9e-05 | 16/37 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.744×** | -4.3 | 0.001 | 19/46 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 0.002 | 15/46 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.762×** | -3.9 | 0.004 | 17/37 (C32, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.783×** | -3.4 | 0.030 | 11/44 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.662×** | -3.1 | 0.074 | 10/43 (SW1417, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.793×** | -3.1 | 0.074 | 8/43 (H4, SW48, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.55 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0478× (z -14.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 14.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.131× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.43 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.118× (z -8.8) ⚠ toxic; unreliable plate only |
| [[A-427 (line)]] | wt | 15.6 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.175× (z -10.1) |
| [[BT-474 (line)]] | alt | 8.53 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0861× (z -9.0) |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.107× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 5.74 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0381× (z -19.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[KATO III (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[NCI-H460 (line)]] | wt | 7.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0863× (z -13.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 7.28 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAP2E]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FAM131A]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ST6GALNAC6-1]] | +0.61 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[BMP8A]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SLC22A13]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EPHX3]] | +0.58 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[TINCR]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FAM53A]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[EP400P1]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PRKAG1]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNPEP]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[TMEM69]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[MAP3K1]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ZHX1]] | -0.47 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[STPG2]] | -0.46 | -0.20 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[STAG2]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[CYP39A1]] | -0.45 | -0.41 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RAPGEFL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RAPGEFL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SSC5D]] | B | SSC5D activity raises RAPGEFL1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without SSC5D | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.0, -21.4); signed map (14.7, 16.2). **Vector** length 65.6, 9.60% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -4.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[NG25 (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,177,010-40,195,656 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Link-GEFII |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHV5](https://www.uniprot.org/uniprotkb/Q9UHV5) (Rap guanine nucleotide exchange factor-like 1):

> Probable guanine nucleotide exchange factor (GEF).

**Summary**, from NCBI Gene [51195](https://www.ncbi.nlm.nih.gov/gene/51195):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in Rap protein signal transduction. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17428) · Entrez [51195](https://www.ncbi.nlm.nih.gov/gene/51195) · UniProt [Q9UHV5](https://www.uniprot.org/uniprotkb/Q9UHV5) · Ensembl [ENSG00000108352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108352)

## Data

Gene col 2936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2936); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2936]; `tensor/DDL_lfc|DDL_z.npy` [2936]; `embed/gene_vectors.npy` [2936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2936 or target_col == 2936). Every well: [[RAPGEFL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEFL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
