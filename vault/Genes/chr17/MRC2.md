---
symbol: "MRC2"
type: "gene"
col: 221
ensembl_id: "ENSG00000011028"
name: "mannose receptor C-type 2"
location: "17q23.2"
module: 53
arm: "+"
pooled_cpm: 56.43
n_lines_expressing: 33
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 20
direction_downstream: 22
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# MRC2

*mannose receptor C-type 2* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +5.5, q 2e-05, up in 14 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.383× (z -17.0, q 0e+00, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO9-AS1]] (+0.61, fdr 1e-05), [[FAM20C]] (+0.61, fdr 1e-05), [[DLG4]] (+0.60, fdr 1e-05); moves opposite to [[FYCO1]] (-0.51, fdr 3e-05), [[PTGES2]] (-0.47, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[EDNRA]] → it (grade B ⚠); 22 go from it, the strongest it → [[NPAS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.5 | 2e-05 | 14/31 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.017 | 13/31 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.019 | 13/31 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.19 | 4/31 (PANC-1, H4, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.19 | 10/31 (J82, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.19 | 6/31 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.383×** | -17.0 | 0e+00 | 27/31 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.398×** | -16.4 | 0e+00 | 31/31 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -13.3 | 8e-38 | 27/31 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -10.0 | 2e-21 | 29/30 (NCI-H1792, C-33 A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -9.3 | 2e-18 | 24/31 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.627×** | -8.0 | 1e-13 | 23/31 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.644×** | -7.8 | 5e-13 | 24/31 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -7.6 | 2e-12 | 23/31 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -7.5 | 3e-12 | 25/31 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -7.1 | 6e-11 | 25/32 (NCI-H2347, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -6.6 | 2e-09 | 24/31 (LOX-IMVI, A549, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -6.3 | 1e-08 | 24/31 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.703×** | -6.3 | 2e-08 | 19/30 (H4, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.748×** | -5.1 | 1e-05 | 20/31 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.624×** | -4.4 | 5e-04 | 17/31 (AN3 CA, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.636×** | -4.2 | 9e-04 | 15/31 (LOX-IMVI, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.004 | 16/31 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 58.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.382× (z -10.6) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.274× (z -14.3) |
| [[A-172 (line)]] | wt | 200 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.354× (z -12.7) |
| [[A-427 (line)]] | wt | 53.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -15.2) |
| [[A549 (line)]] | wt | 63.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 52.4 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.9) | [[Harringtonine (drug)]] 0.5 µM 0.315× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 102 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +16.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.253× (z -16.6) |
| [[CHP-212 (line)]] | wt | 124 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -10.3) |
| [[HOP62 (line)]] | alt | 303 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -18.5) |
| [[J82 (line)]] | alt | 66.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 43.9 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.312× (z -9.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -8.7) |
| [[SW 900 (line)]] | alt | 97.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -11.8) |
| [[H4 (line)]] | wt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -11.0) |
| [[HS-578T (line)]] | alt | 142 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -17.0) |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.349× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -11.4) |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -13.3) ⚠ cell-cycle shift, explains ~3% of this change |
| [[C-33 A (line)]] | alt | 75.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -10.4) |
| [[A498 (line)]] | wt | 73.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.342× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0933× (z -10.4) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -10.4) |
| [[SW480 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.25 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9-AS1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FAM20C]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[DLG4]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.60 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[C2orf92]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[C12orf57]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[DENND2A]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[COL23A1]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ASGR1]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 | same gene group |
| [[HMGA2-AS1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SSC5D]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MEIS3]] | +0.54 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FYCO1]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PTGES2]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDNRA]] | B | EDNRA activity raises MRC2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 4.07× lower at baseline in the lines without EDNRA | 0.021 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[NPAS1]] | B | NPAS1 activity raises MRC2's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 3.96× lower at baseline in the lines without NPAS1 | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TWIST2]] | B | TWIST2 activity raises MRC2's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.92× lower at baseline in the lines without TWIST2 | 0.050 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[LAG3]] | B | LAG3 activity raises MRC2's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 5.51× lower at baseline in the lines without LAG3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[NOTCH3]] | B | NOTCH3 activity raises MRC2's level | lines that do not express NOTCH3 (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without NOTCH3 | 0.073 | ⚠ within organs, on part of the lines; also absent: WNT5B, GPR68, RNF150; maybe low, not absent |
| [[FAM20C]] | C | FAM20C activity raises MRC2's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 4.69× lower at baseline in the lines without FAM20C | 0.007 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1; co-absent with the target |
| [[TSHZ3]], [[TSHZ3-AS1]] | C | TSHZ3, TSHZ3-AS1 activity raises MRC2's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 4.87× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[WNT5B]] | C | WNT5B activity raises MRC2's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 5.47× lower at baseline in the lines without WNT5B | 0.013 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises MRC2's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 5.16× lower at baseline in the lines without ADAMTS2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[COL6A2]] | C | COL6A2 activity raises MRC2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 4.92× lower at baseline in the lines without COL6A2 | 0.018 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises MRC2's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 4.70× lower at baseline in the lines without NTNG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[FMNL1-DT]] | C | FMNL1-DT activity raises MRC2's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 3.46× lower at baseline in the lines without FMNL1-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 12, C 10. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS1]] | B | MRC2 activity raises NPAS1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 2.44× lower at baseline in the lines without MRC2 | 0.027 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[CD27-AS1]] | B | MRC2 activity raises CD27-AS1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without MRC2 | 0.029 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[DALRD3]] | B | MRC2 activity raises DALRD3's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.34× lower at baseline in the lines without MRC2 | 0.036 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[C12orf57]] | B | MRC2 activity raises C12orf57's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.44× lower at baseline in the lines without MRC2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[SLC26A4]] | B | MRC2 activity raises SLC26A4's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without MRC2 | 0.049 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[TGFB1]] | B | MRC2 activity raises TGFB1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 2.38× lower at baseline in the lines without MRC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[LAG3]] | B | MRC2 activity raises LAG3's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without MRC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[CYS1]] | B | MRC2 activity raises CYS1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without MRC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[FYCO1]] | B | MRC2 activity raises FYCO1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without MRC2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[RYR1]] | B | MRC2 activity raises RYR1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without MRC2 | 0.077 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[CYGB]] | B | MRC2 activity raises CYGB's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without MRC2 | 0.087 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[LINC01119]] | B | MRC2 activity raises LINC01119's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.89× lower at baseline in the lines without MRC2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.4, -17.0); signed map (17.9, 17.9). **Vector** length 94.9, 26.0% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -9.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -16.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | mannose receptor C-type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:62,627,670-62,693,597 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0709, ENDO180, CLEC13E, CD280 |
| Gene groups (HGNC) | CD molecules; C-type lectin domain containing |
| Reactome | 4 pathways, smallest: Cross-presentation of soluble exogenous antigens (endosomes); Antigen processing-Cross presentation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBG0](https://www.uniprot.org/uniprotkb/Q9UBG0) (C-type mannose receptor 2):

> May play a role as endocytotic lectin receptor displaying calcium-dependent lectin activity. Internalizes glycosylated ligands from the extracellular space for release in an endosomal compartment via clathrin-mediated endocytosis. May be involved in plasminogen activation system controlling the extracellular level of PLAUR/PLAU, and thus may regulate protease activity at the cell surface. May contribute to cellular uptake, remodeling and degradation of extracellular collagen matrices. May play …

**Summary**, from NCBI Gene [9902](https://www.ncbi.nlm.nih.gov/gene/9902):

> This gene encodes a member of the mannose receptor family of proteins that contain a fibronectin type II domain and multiple C-type lectin-like domains. The encoded protein plays a role in extracellular matrix remodeling by mediating the internalization and lysosomal degradation of collagen ligands. Expression of this gene may play a role in the tumorigenesis and metastasis of several malignancies including breast cancer, gliomas and metastatic bone disease. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:16875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16875) · Entrez [9902](https://www.ncbi.nlm.nih.gov/gene/9902) · UniProt [Q9UBG0](https://www.uniprot.org/uniprotkb/Q9UBG0) · Ensembl [ENSG00000011028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011028)

## Data

Gene col 221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 221); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 221]; `tensor/DDL_lfc|DDL_z.npy` [221]; `embed/gene_vectors.npy` [221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 221 or target_col == 221). Every well: [[MRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
