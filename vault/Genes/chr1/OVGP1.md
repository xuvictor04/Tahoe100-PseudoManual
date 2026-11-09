---
symbol: "OVGP1"
type: "gene"
col: 1428
ensembl_id: "ENSG00000085465"
name: "oviductal glycoprotein 1"
location: "1p13.2"
module: 37
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 49
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# OVGP1

*oviductal glycoprotein 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.47× (z +17.0, q 0e+00, up in 33 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (PANC-1 0.0576×; ⚠ transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (RKO 0.0602×; ⚠ transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC13]] (+0.70, fdr 7e-06), [[DCAF4L1]] (+0.65, fdr 1e-05), [[SLC26A7]] (+0.61, fdr 3e-05); moves opposite to [[LANCL1]] (-0.47, fdr 1e-04), [[TRAPPC2]] (-0.46, fdr 3e-04), [[STARD3NL]] (-0.45, fdr 4e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.47×** | +17.0 | 0e+00 | 33/33 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +12.8 | 4e-35 | 21/28 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.77×** | +12.5 | 9e-34 | 30/31 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.54×** | +12.2 | 8e-32 | 38/44 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.30×** | +11.7 | 1e-29 | 16/21 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **4.04×** | +11.2 | 4e-27 | 40/43 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.76×** | +10.6 | 2e-24 | 37/40 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.96×** | +10.6 | 2e-24 | 31/38 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.76×** | +10.2 | 1e-22 | 12/14 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **3.57×** | +10.2 | 1e-22 | 35/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.49×** | +10.0 | 5e-22 | 32/41 (A498, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.41×** | +9.8 | 3e-21 | 30/39 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.54×** | +9.8 | 8e-21 | 10/12 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.22×** | +9.0 | 7e-18 | 14/21 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +8.0 | 3e-14 | 21/32 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.41×** | +7.8 | 2e-13 | 27/34 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.33×** | +7.8 | 3e-13 | 19/24 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.17×** | +6.2 | 2e-08 | 20/42 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.03×** | +5.3 | 2e-06 | 12/39 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.3 | 3e-06 | 12/42 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.88×** | +5.1 | 1e-05 | 13/39 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1428.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (PANC-1 0.0576×; ⚠ transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (RKO 0.0602×; ⚠ transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Flutamide (drug)]] 5 µM |  | 0.637× | -3.7 | 0.14 | 14/41 (HEC-1-A, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 3.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 8.34 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.76× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 2.11 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0576× (z -10.2) ⚠ transcription drop |
| [[RKO (line)]] | wt | 6.36 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0602× (z -9.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +9.4) | — |
| [[A-172 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.856 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC13]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.65 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[SLC26A7]] | +0.61 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[AOC2]] | +0.60 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[IMPA1P1]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[EFCAB12]] | +0.56 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PIWIL2]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[GRK7]] | +0.55 | +0.66 / +0.37 | both halves | 8e-05 |  |
| [[CORIN]] | +0.54 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[MYH3]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DRC1]] | +0.53 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[ADAM32]] | +0.53 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | -0.47 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[TRAPPC2]] | -0.46 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[STARD3NL]] | -0.45 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[OTULIN]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OVGP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DDR2]] | B | DDR2 activity raises OVGP1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.39× lower at baseline in the lines without DDR2 | 0.081 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[SESN3]] | B | SESN3 activity lowers OVGP1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 1.13× higher at baseline in the lines without SESN3 | 0.087 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.8, -15.2); signed map (13.9, 4.2). **Vector** length 47.7, 5.89% of its response variance represented; |z| ≥ 3 in 1,308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +5.2 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.1 | +5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.1 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +7.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | oviductal glycoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,414,319-111,427,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHIT5, OGP; previously MUC9 |
| Gene groups (HGNC) | Mucins; Chitinases |
| Reactome | 3 pathways, smallest: Interaction With Cumulus Cells And The Zona Pellucida; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12889](https://www.uniprot.org/uniprotkb/Q12889) (Oviduct-specific glycoprotein):

> Binds to oocyte zona pellucida in vivo. May play a role in the fertilization process and/or early embryonic development.

**Summary**, from NCBI Gene [5016](https://www.ncbi.nlm.nih.gov/gene/5016):

> This gene encodes a large, carbohydrate-rich, epithelial glycoprotein with numerous O-glycosylation sites located within threonine, serine, and proline-rich tandem repeats. The gene is similar to members of the mucin and the glycosyl hydrolase 18 gene families. Regulation of expression may be estrogen-dependent. Gene expression and protein secretion occur during late follicular development through early cleavage-stage embryonic development. The protein is secreted from non-ciliated oviductal …

**Accessions** — [HGNC:8524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8524) · Entrez [5016](https://www.ncbi.nlm.nih.gov/gene/5016) · UniProt [Q12889](https://www.uniprot.org/uniprotkb/Q12889) · Ensembl [ENSG00000085465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085465)

## Data

Gene col 1428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1428); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1428]; `tensor/DDL_lfc|DDL_z.npy` [1428]; `embed/gene_vectors.npy` [1428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1428 or target_col == 1428). Every well: [[OVGP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OVGP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
