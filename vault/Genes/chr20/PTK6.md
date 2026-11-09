---
symbol: "PTK6"
type: "gene"
col: 2097
ensembl_id: "ENSG00000101213"
name: "protein tyrosine kinase 6"
location: "20q13.33"
module: 31
arm: "+"
pooled_cpm: 11.87
n_lines_expressing: 33
n_dd_up: 6
n_dd_down: 40
n_dd_up_clean: 5
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 75
direction_downstream: 48
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PTK6

*protein tyrosine kinase 6* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.80× (z +4.7, q 7e-04, up in 16 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.347× (z -12.5, q 3e-33, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMC6]] (+0.72, fdr 7e-06), [[SDR16C5]] (+0.69, fdr 7e-06), [[FAM83E]] (+0.68, fdr 7e-06); moves opposite to [[ANTXR1]] (-0.55, fdr 2e-04), [[CASD1]] (-0.51, fdr 1e-04), [[GTF2I]] (-0.50, fdr 8e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 48 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +4.7 | 7e-04 | 16/29 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.28×** | +4.7 | 7e-04 | 10/29 (LS 180, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.4 | 0.002 | 3/18 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.009 | 10/29 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.025 | 9/30 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.060 | 4/31 (HT-29, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.14 | 12/31 (SW480, LS 180, …) | two highest doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.47× | +3.1 | 0.14 | 0/31 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.14 | 5/31 (NCI-H1573, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.347×** | -12.5 | 3e-33 | 27/31 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -10.6 | 9e-24 | 22/30 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.441×** | -10.0 | 3e-21 | 27/31 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.432×** | -9.9 | 5e-21 | 26/31 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -8.9 | 7e-17 | 22/31 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.473×** | -8.8 | 8e-17 | 24/31 (HT-29, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -8.7 | 2e-16 | 25/30 (SW1417, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.496×** | -8.6 | 9e-16 | 23/31 (AsPC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.495×** | -8.3 | 5e-15 | 25/31 (AsPC-1, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.495×** | -8.1 | 3e-14 | 21/31 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -7.8 | 4e-13 | 21/31 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.538×** | -7.6 | 2e-12 | 22/31 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -7.3 | 1e-11 | 23/31 (HT-29, CFPAC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -6.9 | 2e-10 | 24/29 (Hs 766T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.590×** | -6.4 | 5e-09 | 19/31 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.340×** | -6.2 | 3e-08 | 23/30 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.636×** | -5.5 | 1e-06 | 17/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.654×** | -5.2 | 6e-06 | 18/31 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -5.2 | 6e-06 | 18/31 (AsPC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.462×** | -4.4 | 3e-04 | 17/29 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 37.9 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -19.0) |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0436× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0498× (z -13.3) |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 44.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.6) |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.0) |
| [[SW480 (line)]] | alt | 16.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.7) |
| [[A-172 (line)]] | wt | 14.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0734× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.0) |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -9.3) |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0486× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -13.7) |
| [[KATO III (line)]] | alt | 28.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0782× (z -11.7) |
| [[A549 (line)]] | wt | 8.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 6.84 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0546× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~74% of this change |
| [[LoVo (line)]] | wt | 11.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.168× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 9.45 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0936× (z -9.8) |
| [[PANC-1 (line)]] | alt | 8.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -8.6) |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0772× (z -17.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC6]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SDR16C5]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[FAM83E]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RDH13]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ARHGAP27]] | +0.66 | +0.59 / +0.73 | both halves | 7e-06 | same gene group |
| [[NGEF]] | +0.64 | +0.66 / +0.48 | both halves | 2e-05 | same gene group |
| [[SEMA3B]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[UNC13D]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FA2H]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PLEKHM1]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR1]] | -0.55 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[CASD1]] | -0.51 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[GTF2I]] | -0.50 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 45, C 30. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises PTK6's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without SRMS | 0.002 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[PTAFR]] | B | PTAFR activity raises PTK6's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.09× lower at baseline in the lines without PTAFR | 0.003 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[CEACAM1]] | B | CEACAM1 activity raises PTK6's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without CEACAM1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[HSD17B2]] | B | HSD17B2 activity raises PTK6's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.53× lower at baseline in the lines without HSD17B2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[CRYBG2]] | B | CRYBG2 activity raises PTK6's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.53× lower at baseline in the lines without CRYBG2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[PCDH1]] | B | PCDH1 activity strengthens PTK6's drug response | lines that do not express PCDH1 (11) vs lines expressing it (20) | the lines without PCDH1 respond 0.45× as strongly (z diff +3.23); strongest at Homoharringtonine 5 µM: 0.73x vs 0.39x (z diff +4.9) | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29; target measured in part of the lines; artifact flags |
| [[KLF5]] | B | KLF5 activity raises PTK6's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without KLF5 | 0.012 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[ATP2C2]] | B | ATP2C2 activity raises PTK6's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.13× lower at baseline in the lines without ATP2C2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[FAM83A]] | B | FAM83A activity raises PTK6's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.50× lower at baseline in the lines without FAM83A | 0.016 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[ADAM8]] | B | ADAM8 activity raises PTK6's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without ADAM8 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[TFF2]] | B | TFF2 activity raises PTK6's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 4.23× lower at baseline in the lines without TFF2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[MOGAT3]] | B | MOGAT3 activity raises PTK6's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without MOGAT3 | 0.019 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 27, C 21. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | PTK6 activity raises EPHA2's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without PTK6 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[EHD1]] | B | PTK6 activity raises EHD1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.79× lower at baseline in the lines without PTK6 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[PTK2B]] | B | PTK6 activity raises PTK2B's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 3.01× lower at baseline in the lines without PTK6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[TNFAIP8]] | B | PTK6 activity raises TNFAIP8's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without PTK6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[GPRC5A]] | B | PTK6 activity raises GPRC5A's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 4.40× lower at baseline in the lines without PTK6 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[ARHGAP27]] | B | PTK6 activity raises ARHGAP27's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without PTK6 | 0.026 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[EZR]] | B | PTK6 activity raises EZR's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 2.34× lower at baseline in the lines without PTK6 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[UNC13D]] | B | PTK6 activity raises UNC13D's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without PTK6 | 0.032 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[SERPINB1]] | B | PTK6 activity raises SERPINB1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 3.30× lower at baseline in the lines without PTK6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[SH3BP2]] | B | PTK6 activity raises SH3BP2's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.61× lower at baseline in the lines without PTK6 | 0.041 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[LSMEM2]] | B | PTK6 activity raises LSMEM2's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without PTK6 | 0.042 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[TICAM1]] | B | PTK6 activity raises TICAM1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without PTK6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, 55.4); signed map (0.5, 37.6). **Vector** length 79.8, 21.2% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -12.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[NG25 (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,528,001-63,537,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRK |
| Gene groups (HGNC) | SH2 domain containing; PTK6 family tyrosine kinases; SH3 domain containing |
| Reactome | 27 pathways, smallest: PTK6 Down-Regulation; PTK6 Activates STAT3; PTK6 Expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13882](https://www.uniprot.org/uniprotkb/Q13882) (Protein-tyrosine kinase 6):

> Non-receptor tyrosine-protein kinase implicated in the regulation of a variety of signaling pathways that control the differentiation and maintenance of normal epithelia, as well as tumor growth. Function seems to be context dependent and differ depending on cell type, as well as its intracellular localization. A number of potential nuclear and cytoplasmic substrates have been identified. These include the RNA-binding proteins: KHDRBS1/SAM68, KHDRBS2/SLM1, KHDRBS3/SLM2 and SFPQ/PSF; …

**Summary**, from NCBI Gene [5753](https://www.ncbi.nlm.nih.gov/gene/5753):

> The protein encoded by this gene is a cytoplasmic nonreceptor protein kinase which may function as an intracellular signal transducer in epithelial tissues. Overexpression of this gene in mammary epithelial cells leads to sensitization of the cells to epidermal growth factor and results in a partially transformed phenotype. Expression of this gene has been detected at low levels in some breast tumors but not in normal breast tissue. The encoded protein has been shown to undergo …

**Accessions** — [HGNC:9617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9617) · Entrez [5753](https://www.ncbi.nlm.nih.gov/gene/5753) · UniProt [Q13882](https://www.uniprot.org/uniprotkb/Q13882) · Ensembl [ENSG00000101213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101213)

## Data

Gene col 2097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2097); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2097]; `tensor/DDL_lfc|DDL_z.npy` [2097]; `embed/gene_vectors.npy` [2097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2097 or target_col == 2097). Every well: [[PTK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
