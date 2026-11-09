---
symbol: "MATN1-AS1"
type: "gene"
col: 11771
ensembl_id: "ENSG00000186056"
name: "MATN1 antisense RNA 1"
location: "1p35.2"
module: 181
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# MATN1-AS1

*MATN1 antisense RNA 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +8.7, q 2e-15, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.380× (z -10.5, q 3e-23, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYSM1]] (+0.62, fdr 7e-05), [[GOSR1]] (+0.61, fdr 3e-05), [[C3orf20]] (+0.61, fdr 3e-05); moves opposite to [[HACD3]] (-0.58, fdr 4e-05), [[CBX1]] (-0.57, fdr 3e-05), [[STRN]] (-0.56, fdr 3e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[EPHX3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +8.7 | 2e-15 | 20/33 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 0.002 | 8/33 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.9 | 0.012 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.012 | 6/40 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.094 | 14/38 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.37× | +3.2 | 0.12 | 5/28 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.32× | +3.0 | 0.19 | 2/40 (MIA PaCa-2, HOP62) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.380×** | -10.5 | 3e-23 | 30/41 (NCI-H1573, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.464×** | -8.4 | 2e-14 | 21/29 (PANC-1, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.492×** | -7.7 | 2e-12 | 23/40 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.535×** | -6.8 | 1e-09 | 25/41 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.321×** | -6.5 | 1e-08 | 20/38 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.561×** | -6.3 | 3e-08 | 21/43 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.581×** | -5.9 | 3e-07 | 15/39 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -5.1 | 2e-05 | 17/41 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.617×** | -5.1 | 3e-05 | 14/27 (HOP62, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.631×** | -5.0 | 3e-05 | 15/39 (HOP62, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.644×** | -4.8 | 9e-05 | 13/32 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -4.4 | 4e-04 | 14/31 (HEC-1-A, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.670×** | -4.1 | 0.002 | 6/40 (SW 900, HEC-1-A, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.006 | 11/40 (BT-474, SW480, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.522×** | -3.7 | 0.008 | 10/26 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.730×** | -3.4 | 0.023 | 8/40 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Cysteamine (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.1 | 0.055 | 4/42 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.756×** | -3.0 | 0.075 | 2/40 (AsPC-1, C32) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.30 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 8.18 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.27 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0740× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.09 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0864× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 4.30 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0443× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0981× (z -9.3) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW480 (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYSM1]] | +0.62 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[GOSR1]] | +0.61 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[C3orf20]] | +0.61 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[MIRLET7IHG]] | +0.60 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[METTL1]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[HELQ]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CYP27B1]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[NEPRO-AS1]] | +0.58 | +0.67 / +0.34 | both halves | 1e-04 | same gene group |
| [[MEPCE]] | +0.58 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[CYP20A1]] | +0.58 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[CHRNA10]] | +0.57 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[ENO3]] | +0.57 | +0.63 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | -0.58 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[CBX1]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[STRN]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[KDM1A]] | -0.55 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[HDAC1]] | -0.55 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[CUL2]] | -0.55 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[FAM210B]] | -0.55 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SLC9A6]] | -0.54 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[IARS2]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[PEBP1]] | -0.54 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[UBAC1]] | -0.54 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[RPA1]] | -0.53 | -0.58 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHX3]] | C | MATN1-AS1 activity lowers EPHX3's level | lines that do not express MATN1-AS1 (4) vs lines expressing it (46) | 1.41× higher at baseline in the lines without MATN1-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CYB561, LINC01569, E2F8; its own permutation p |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.5, -24.7); signed map (16.5, 0.6). **Vector** length 66.5, 11.2% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.2 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -10.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -2.8 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.6 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MATN1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p35.2 — chr1:30,718,504-30,726,827 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40364) · Entrez [100129196](https://www.ncbi.nlm.nih.gov/gene/100129196) · Ensembl [ENSG00000186056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186056)

## Data

Gene col 11771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11771); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11771]; `tensor/DDL_lfc|DDL_z.npy` [11771]; `embed/gene_vectors.npy` [11771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11771 or target_col == 11771). Every well: [[MATN1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MATN1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
