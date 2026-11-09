---
symbol: "MRGBP"
type: "gene"
col: 2089
ensembl_id: "ENSG00000101189"
name: "MRG domain binding protein"
location: "20q13.33"
module: 30
arm: "+"
pooled_cpm: 17.32
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MRGBP

*MRG domain binding protein* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.45× (z +4.7, q 0.002, up in 23 of 42 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.56× (z +4.0, q 0.012, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.454× (z -13.9, q 4e-41, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP21]] (+0.72, fdr 7e-06), [[UNC45A]] (+0.71, fdr 1e-05), [[TBCB]] (+0.70, fdr 2e-05); moves opposite to [[GALNT7]] (-0.58, fdr 4e-05), [[CRPPA]] (-0.57, fdr 1e-04), [[PSMD6-AS1]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.45×** | +4.7 | 0.002 | 23/42 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.012 | 20/46 (CHP-212, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.012 | 18/45 (NCI-H2030, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.012 | 24/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.020 | 17/44 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.052 | 20/48 (KATO III, HT-29, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.080 | 17/45 (SNU-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -13.9 | 4e-41 | 43/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.550×** | -10.5 | 3e-23 | 38/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -5.6 | 5e-06 | 29/46 (HOP62, C-33 A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -4.9 | 1e-04 | 22/48 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -4.8 | 2e-04 | 24/47 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.701×** | -4.4 | 9e-04 | 23/48 (AsPC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -4.3 | 0.002 | 21/48 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -4.0 | 0.005 | 21/47 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.736×** | -3.8 | 0.008 | 19/47 (SW 1271, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.7 | 0.015 | 21/48 (C-33 A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -3.4 | 0.037 | 20/48 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.759×** | -3.3 | 0.043 | 16/47 (SW 1088, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.780×** | -3.1 | 0.085 | 11/47 (LS 180, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -10.7) |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.7) |
| [[A-172 (line)]] | wt | 24.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.2) |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -8.5) |
| [[COLO 205 (line)]] | alt | 8.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.0) |
| [[H4 (line)]] | wt | 14.8 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0565× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.103× (z -9.7) ⚠ transcription drop |
| [[J82 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.4) |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.1) |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.5) |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.1) |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.3) |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP21]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.71 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[TBCB]] | +0.70 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[PUS3]] | +0.67 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[WRAP73]] | +0.65 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.64 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[TRAPPC5]] | +0.64 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[POLR2I]] | +0.64 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[CYB5R1]] | +0.64 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SLX9]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.62 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CRPPA]] | -0.57 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[PSMD6-AS1]] | -0.57 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SNX5]] | -0.57 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PBLD]] | -0.56 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[GALNT7-DT]] | -0.56 | -0.55 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[RAP2C]] | -0.56 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ANXA2R-AS1]] | -0.55 | -0.55 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[OXCT1]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ANKRD18B]] | -0.55 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD18A]] | -0.55 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[ARAP2]] | -0.55 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.55 | -0.46 / -0.20 | both halves | 7e-04 |  |
| [[EIF4G2]] | -0.55 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MRGBP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARAP2]] | B | ARAP2 activity lowers MRGBP's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.25× higher at baseline in the lines without ARAP2 | 0.086 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.1, -4.9); signed map (-34.2, -3.0). **Vector** length 74.3, 14.6% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -13.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.1 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Dapagliflozin (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Brimonidine (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MRG domain binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,796,473-62,801,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10914, MRG15BP, Eaf7; previously C20orf20 |
| Gene groups (HGNC) | Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV56](https://www.uniprot.org/uniprotkb/Q9NV56) (MRG/MORF4L-binding protein):

> Component of the NuA4 histone acetyltransferase (HAT) complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. This modification may both alter nucleosome - DNA interactions and promote interaction of the modified histones with other proteins which positively regulate transcription. This complex may be required for the activation of transcriptional programs associated with oncogene and proto-oncogene mediated growth …

**Summary**, from NCBI Gene [55257](https://www.ncbi.nlm.nih.gov/gene/55257):

> Involved in positive regulation of double-strand break repair via homologous recombination and regulation of cell cycle. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15866) · Entrez [55257](https://www.ncbi.nlm.nih.gov/gene/55257) · UniProt [Q9NV56](https://www.uniprot.org/uniprotkb/Q9NV56) · Ensembl [ENSG00000101189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101189)

## Data

Gene col 2089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2089); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2089]; `tensor/DDL_lfc|DDL_z.npy` [2089]; `embed/gene_vectors.npy` [2089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2089 or target_col == 2089). Every well: [[MRGBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRGBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
