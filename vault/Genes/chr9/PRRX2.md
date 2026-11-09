---
symbol: "PRRX2"
type: "gene"
col: 9426
ensembl_id: "ENSG00000167157"
name: "paired related homeobox 2"
location: "9q34.11"
module: 128
arm: "+"
pooled_cpm: 6.22
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# PRRX2

*paired related homeobox 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +17.9, q 0e+00, up in 6 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.450× (z -8.7, q 2e-15, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBX1]] (+0.60, fdr 2e-05), [[PALM]] (+0.60, fdr 1e-05), [[CERS4]] (+0.56, fdr 2e-05); moves opposite to [[MYCBP2]] (-0.42, fdr 1e-04), [[FAM120A]] (-0.41, fdr 1e-04), [[CADPS]] (-0.39, fdr 3e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CACNG6]] → it (grade C ⚠); 2 go from it, the strongest it → [[ITGA2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +17.9 | 0e+00 | 6/22 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +8.2 | 5e-14 | 0/11 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +7.2 | 8e-11 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +7.1 | 1e-10 | 4/21 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.0 | 2e-10 | 1/16 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +6.8 | 7e-10 | 10/23 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +6.3 | 2e-08 | 3/23 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.3 | 8e-06 | 7/23 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 9e-04 | 2/20 (MIA PaCa-2, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.40×** | +3.6 | 0.015 | 6/22 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.3 | 0.042 | 1/13 (HOP62) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.39×** | +3.3 | 0.047 | 2/21 (SW480, HOP62) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.048 | 1/17 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.1 | 0.075 | 2/18 (A-427, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.086 | 3/23 (NCI-H460, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.450×** | -8.7 | 2e-15 | 21/23 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.538×** | -6.7 | 5e-09 | 17/23 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.559×** | -6.3 | 5e-08 | 16/22 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.573×** | -6.1 | 2e-07 | 19/23 (AsPC-1, MIA PaCa-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.578×** | -6.0 | 3e-07 | 16/23 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.600×** | -5.3 | 9e-06 | 18/23 (MIA PaCa-2, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.623×** | -5.1 | 2e-05 | 13/23 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.438×** | -4.7 | 2e-04 | 10/21 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.666×** | -4.4 | 6e-04 | 15/23 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -4.0 | 0.003 | 10/23 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.692×** | -4.0 | 0.003 | 15/23 (MIA PaCa-2, AsPC-1, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.555×** | -3.3 | 0.039 | 6/20 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.663×** | -3.2 | 0.061 | 5/23 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 13 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0528× (z -20.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 20.9 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0575× (z -17.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 6 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.9) |
| [[A-427 (line)]] | wt | 18.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -9.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.5) |
| [[PANC-1 (line)]] | alt | 7.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.4) |
| [[A-172 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBX1]] | +0.60 | +0.49 / +0.61 | both halves | 2e-05 | **novel candidate** |
| [[PALM]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CERS4]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ADAP2]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[CBFA2T3]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SLC26A11]] | +0.49 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[SMO]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ELFN1]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[LINC02643]] | +0.49 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[CYS1]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[EDARADD]] | +0.48 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[SEC14L4]] | +0.48 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYCBP2]] | -0.42 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[FAM120A]] | -0.41 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[CADPS]] | -0.39 | -0.41 / -0.26 | both halves | 3e-04 |  |
| [[SNTB1]] | -0.39 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG6]] | C | CACNG6 activity raises PRRX2's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without CACNG6 | 0.040 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1; co-absent with the target |
| [[SLC35G2]] | C | SLC35G2 activity raises PRRX2's level | lines that do not express SLC35G2 (12) vs lines expressing it (38) | 3.05× lower at baseline in the lines without SLC35G2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SMARCA1, LARP6, ZSCAN12; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2B]] | B | PRRX2 activity raises ITGA2B's level | lines that do not express PRRX2 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without PRRX2 | 0.082 | ⚠ within organs, on part of the lines; also absent: PTCHD1, CYP27C1, STOX2 |
| [[SEC14L4]] | C | PRRX2 activity raises SEC14L4's level | lines that do not express PRRX2 (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without PRRX2 | 0.094 | ⚠ within organs, on part of the lines; also absent: PTCHD1, CYP27C1, STOX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.1, 38.7); signed map (23.9, 24.1). **Vector** length 53.1, 12.0% of its response variance represented; |z| ≥ 3 in 526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +17.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -8.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | paired related homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,665,647-129,722,674 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRX2, PMX2 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99811](https://www.uniprot.org/uniprotkb/Q99811) (Paired mesoderm homeobox protein 2):

> May play a role in the scarless healing of cutaneous wounds during the first two trimesters of development.

**Summary**, from NCBI Gene [51450](https://www.ncbi.nlm.nih.gov/gene/51450):

> The DNA-associated protein encoded by this gene is a member of the paired family of homeobox proteins. Expression is localized to proliferating fetal fibroblasts and the developing dermal layer, with downregulated expression in adult skin. Increases in expression of this gene during fetal but not adult wound healing suggest a possible role in mechanisms that control mammalian dermal regeneration and prevent formation of scar response to wounding. The expression patterns provide evidence …

**Accessions** — [HGNC:21338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21338) · Entrez [51450](https://www.ncbi.nlm.nih.gov/gene/51450) · UniProt [Q99811](https://www.uniprot.org/uniprotkb/Q99811) · Ensembl [ENSG00000167157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167157)

## Data

Gene col 9426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9426); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9426]; `tensor/DDL_lfc|DDL_z.npy` [9426]; `embed/gene_vectors.npy` [9426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9426 or target_col == 9426). Every well: [[PRRX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
