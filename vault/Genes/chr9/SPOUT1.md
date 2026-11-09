---
symbol: "SPOUT1"
type: "gene"
col: 12736
ensembl_id: "ENSG00000198917"
name: "SPOUT domain containing methyltransferase 1"
location: "9q34.11"
module: 5
arm: "+"
pooled_cpm: 13.65
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SPOUT1

*SPOUT domain containing methyltransferase 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +9.9, q 3e-20, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.48× (z +4.9, q 8e-05, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.856× (z -6.6, q 3e-08, down in 24 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.725× (z -5.7, q 4e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H18]] (+0.69, fdr 7e-06), [[DDX51]] (+0.68, fdr 7e-06), [[TIMM50]] (+0.63, fdr 9e-06); moves opposite to [[RNF11]] (-0.57, fdr 1e-05), [[PRCP]] (-0.54, fdr 4e-05), [[PKIB]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATXN1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.20×** | +9.9 | 3e-20 | 45/47 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.00×** | +8.7 | 8e-16 | 41/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.05×** | +8.7 | 8e-16 | 12/22 (J82, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +8.1 | 8e-14 | 34/41 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.88×** | +7.9 | 3e-13 | 28/37 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.65×** | +6.2 | 4e-08 | 32/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.9 | 8e-05 | 21/47 (MIA PaCa-2, HS-578T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +4.9 | 9e-05 | 26/47 (J82, RKO, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.45×** | +4.6 | 2e-04 | 22/46 (HEC-1-A, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.27×** | +4.2 | 0.001 | 17/46 (SHP-77, H4, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +4.2 | 0.001 | 17/46 (LOX-IMVI, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.001 | 21/44 (Hs 766T, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.39×** | +4.2 | 0.001 | 19/47 (COLO 205, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.39×** | +4.1 | 0.001 | 16/40 (LOX-IMVI, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.25×** | +4.0 | 0.002 | 18/45 (COLO 205, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 15/47 (BT-474, SNU-423, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.011 | 12/44 (NCI-H1573, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.017 | 15/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.039 | 7/47 (LOX-IMVI, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.051 | 7/47 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.856× | -6.6 | 3e-08 | 24/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.725×** | -5.7 | 4e-06 | 29/48 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.640×** | -5.6 | 5e-06 | 24/46 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.592×** | -3.4 | 0.090 | 12/48 (A498, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.757×** | -3.3 | 0.098 | 12/46 (SW 900, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.642× (z -8.8) ⚠ position not correctable |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.100× (z -9.2) |
| [[A-172 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H18]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[DDX51]] | +0.68 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[TIMM50]] | +0.63 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[POLR1G]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[L3MBTL2]] | +0.60 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[AFG3L2]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NIP7]] | +0.60 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[RRP1]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CDK10]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PWP2]] | +0.60 | +0.57 / +0.59 | both halves | 8e-06 | STRING 421 |
| [[NR2C2AP]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[MECR]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF11]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PRCP]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PKIB]] | -0.54 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[DSTN]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GPM6A]] | -0.52 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[TFG]] | -0.51 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[AKR1B1]] | -0.51 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[ATP6V1A]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TMSB4X]] | -0.50 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[TLCD4]] | -0.50 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[PDE5A]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PPP1CB]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity lowers SPOUT1's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.64× higher at baseline in the lines without ATXN1-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[SLC7A6OS]] | C | SLC7A6OS's natural level strengthens SPOUT1's drug response | SLC7A6OS's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.04; direction not clear | 0.0999 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.7, -40.8); signed map (1.4, -47.7). **Vector** length 61.8, 10.7% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.9 | +9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.7 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +3.6 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SPOUT domain containing methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,819,651-128,829,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC109, CENP-32; previously C9orf114 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T280](https://www.uniprot.org/uniprotkb/Q5T280) (28S rRNA):

> S-adenosyl-L-methionine-dependent RNA methyltransferase. Specifically methylates the N3 position of a uridine in 28S rRNA. Required for association of the centrosomes with the poles of the bipolar mitotic spindle during metaphase, ensuring proper spindle organization. Also involved in chromosome alignment. May promote centrosome maturation probably by recruiting A-kinase anchor protein AKAP9 to centrosomes in early mitosis. Binds specifically to miRNA MIR145 hairpin, regulates MIR145 expression …

**Summary**, from NCBI Gene [51490](https://www.ncbi.nlm.nih.gov/gene/51490):

> Enables S-adenosyl-L-methionine binding activity; miRNA binding activity; and rRNA (uridine-N3-)-methyltransferase activity. Involved in maintenance of centrosome location; miRNA processing; and rRNA base methylation. Acts upstream of with a positive effect on post-transcriptional regulation of gene expression. Located in kinetochore; mitotic spindle; and spindle pole centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26933) · Entrez [51490](https://www.ncbi.nlm.nih.gov/gene/51490) · UniProt [Q5T280](https://www.uniprot.org/uniprotkb/Q5T280) · Ensembl [ENSG00000198917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198917)

## Data

Gene col 12736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12736); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12736]; `tensor/DDL_lfc|DDL_z.npy` [12736]; `embed/gene_vectors.npy` [12736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12736 or target_col == 12736). Every well: [[SPOUT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOUT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
