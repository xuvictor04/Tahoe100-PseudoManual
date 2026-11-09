---
symbol: "SEPTIN1"
type: "gene"
col: 11079
ensembl_id: "ENSG00000180096"
name: "septin 1"
location: "16p11.2"
module: 21
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SEPTIN1

*septin 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.16× (z +19.8, q 0e+00, up in 30 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.588× (z -4.4, q 0.006, down in 20 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Arbutin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0589×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.134×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFATC2IP-AS1]] (+0.74, fdr 9e-06), [[UBOX5-AS1]] (+0.73, fdr 1e-05), [[LANCL1-AS1]] (+0.71, fdr 3e-05); moves opposite to [[OCRL]] (-0.61, fdr 4e-05), [[FARSB]] (-0.60, fdr 2e-05), [[PRMT5]] (-0.60, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MIR3659HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.16×** | +19.8 | 0e+00 | 30/30 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +11.4 | 1e-27 | 10/13 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.38×** | +11.3 | 2e-27 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +8.8 | 2e-16 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +6.4 | 2e-08 | 11/25 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +6.3 | 2e-08 | 19/41 (SW480, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +4.8 | 1e-04 | 6/20 (A498, A549, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.6 | 3e-04 | 9/31 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.4 | 6e-04 | 3/10 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.5 | 0.026 | 3/13 (A-172, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.3 | 0.044 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.052 | 2/28 (NCI-H460, RKO) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.052 | 2/24 (A-427, PANC-1) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.052 | 5/24 (HEC-1-A, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.45×** | +3.2 | 0.056 | 6/45 (C32, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.070 | 5/44 (PANC-1, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.070 | 10/44 (SNU-423, SW480, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.070 | 3/22 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.095 | 4/25 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11079.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Arbutin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0589×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.588×** | -4.4 | 0.006 | 20/37 (A498, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -3.8 | 0.044 | 12/44 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.64 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +12.2) | [[Harringtonine (drug)]] 5 µM 0.134× (z -8.6) |
| [[A-172 (line)]] | wt | 5.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +10.1) | — |
| [[A549 (line)]] | wt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.05× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.35 | 0 | 1 | — | [[Arbutin (drug)]] 0.5 µM 0.0589× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.18× (z +10.7) | — |
| [[SW480 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +9.1) | — |
| [[A-427 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.841 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC2IP-AS1]] | +0.74 | +0.57 / +0.77 | both halves | 9e-06 |  |
| [[UBOX5-AS1]] | +0.73 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[LANCL1-AS1]] | +0.71 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[CAPN10-DT]] | +0.71 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[EOGT-DT]] | +0.70 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[HRG-AS1]] | +0.69 | +0.37 / +0.74 | both halves | 7e-05 |  |
| [[A2ML1-AS1]] | +0.69 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.69 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.68 | +0.42 / +0.76 | both halves | 4e-05 |  |
| [[SPDYE5]] | +0.68 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[HIGD2A]] | +0.68 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.68 | +0.49 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | -0.61 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[FARSB]] | -0.60 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[PRMT5]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[FKTN]] | -0.59 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PIGO]] | -0.58 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[RUVBL1]] | -0.58 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[WDR7]] | -0.58 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[AGK]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[YTHDC2]] | -0.57 | -0.35 / -0.63 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3659HG]] | B | MIR3659HG activity raises SEPTIN1's level | lines that do not express MIR3659HG (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without MIR3659HG | 0.033 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SEPTIN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 28.3); signed map (34.9, 4.1). **Vector** length 42.6, 4.82% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +19.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -0.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | septin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,378,135-30,395,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PNUTL3, Septin-1; previously DIFF6, SEPT1 |
| Gene groups (HGNC) | Septins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYJ6](https://www.uniprot.org/uniprotkb/Q8WYJ6) (Septin-1):

> Filament-forming cytoskeletal GTPase (By similarity). May play a role in cytokinesis (Potential).

**Summary**, from NCBI Gene [1731](https://www.ncbi.nlm.nih.gov/gene/1731):

> This gene is a member of the septin family of GTPases. Members of this family are required for cytokinesis and the maintenance of cellular morphology. This gene encodes a protein that can form homo- and heterooligomeric filaments, and may contribute to the formation of neurofibrillary tangles in Alzheimer's disease. Alternatively spliced transcript variants have been found but the full-length nature of these variants has not been determined. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:2879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2879) · Entrez [1731](https://www.ncbi.nlm.nih.gov/gene/1731) · UniProt [Q8WYJ6](https://www.uniprot.org/uniprotkb/Q8WYJ6) · Ensembl [ENSG00000180096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180096)

## Data

Gene col 11079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11079); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11079]; `tensor/DDL_lfc|DDL_z.npy` [11079]; `embed/gene_vectors.npy` [11079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11079 or target_col == 11079). Every well: [[SEPTIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
