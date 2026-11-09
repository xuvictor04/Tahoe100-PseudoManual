---
symbol: "LMNTD1"
type: "gene"
col: 7669
ensembl_id: "ENSG00000152936"
name: "lamin tail domain containing 1"
location: "12p12.1"
module: 19
arm: "+"
pooled_cpm: 6.97
n_lines_expressing: 27
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LMNTD1

*lamin tail domain containing 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.23× (z +16.2, q 0e+00, up in 16 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.627× (z -4.6, q 0.002, down in 6 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0776×, NCI-H460 0.283×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.172×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0880×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.116×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAVIN2-AS1]] (+0.69, fdr 7e-06), [[PDE1A]] (+0.60, fdr 1e-05), [[NTRK3]] (+0.59, fdr 3e-05); moves opposite to [[LDLRAP1]] (-0.48, fdr 1e-04), [[TPST2]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CHL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.23×** | +16.2 | 0e+00 | 16/22 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +14.4 | 1e-44 | 12/19 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.32×** | +13.8 | 7e-41 | 0/5 | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.27×** | +13.1 | 3e-37 | 1/5 (HS-578T) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +12.2 | 5e-32 | 2/7 (HOP62, HS-578T) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +9.0 | 2e-17 | 13/22 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +8.8 | 1e-16 | 13/23 (SW480, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.36×** | +8.4 | 4e-15 | 11/21 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +6.7 | 1e-09 | 10/21 (MIA PaCa-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +6.3 | 2e-08 | 7/20 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 7e-04 | 5/17 (CFPAC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.3 | 9e-04 | 2/17 (A-172, LoVo) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.7 | 0.010 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.3 | 0.037 | 1/12 (A-172) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.056 | 5/24 (HS-578T, HOP62, …) | top dose only |  |
| [[Orlistat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.056 | 1/24 (NCI-H2030) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.058 | 2/16 (SK-MEL-2, J82) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.38×** | +2.9 | 0.096 | 3/18 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.096 | 4/24 (CFPAC-1, HS-578T, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7669.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0776×, NCI-H460 0.283×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.172×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0880×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.627×** | -4.6 | 0.002 | 6/21 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.889× | -4.2 | 0.007 | 7/25 (RPMI-7951, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 86.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0776× (z -16.0) |
| [[A-172 (line)]] | wt | 2.58 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 137× (z +18.8) | — |
| [[NCI-H460 (line)]] | wt | 32.0 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.122× (z -10.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.157× (z -8.9) |
| [[HOP62 (line)]] | alt | 1.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 4.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.7) | — |
| [[J82 (line)]] | alt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +12.8) | — |
| [[LoVo (line)]] | wt | 2.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +9.9) | — |
| [[A-427 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN2-AS1]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NTRK3]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[NRG1]] | +0.58 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[WAKMAR2]] | +0.58 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CPED1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[CLDN16]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[TRPM3]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LINC01010]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CSF3]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDLRAP1]] | -0.48 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[TPST2]] | -0.47 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHL1]] | B | CHL1 activity raises LMNTD1's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 1.71× lower at baseline in the lines without CHL1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[ADGRL3]] | B | ADGRL3 activity raises LMNTD1's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 1.69× lower at baseline in the lines without ADGRL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[LINC03000]] | B | LINC03000 activity raises LMNTD1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 1.96× lower at baseline in the lines without LINC03000 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[MIR99AHG]] | B | MIR99AHG activity raises LMNTD1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 1.34× lower at baseline in the lines without MIR99AHG | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[LINC02945]] | B | LINC02945 activity raises LMNTD1's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 1.91× lower at baseline in the lines without LINC02945 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016 |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises LMNTD1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 1.92× lower at baseline in the lines without MARCOL, SPINK13 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC01035]] | C | LINC01035 activity raises LMNTD1's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 1.95× lower at baseline in the lines without LINC01035 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises LMNTD1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 3.13× lower at baseline in the lines without TBXT | 0.089 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.6, 27.4); signed map (41.9, 29.1). **Vector** length 46.3, 9.25% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +16.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +0.9 | +0.6 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -0.8 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | lamin tail domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:25,409,307-25,648,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36004, Pas1c1; previously IFLTD1 |
| Matched by | ensembl_id |

UniProt [Q8N9Z9](https://www.uniprot.org/uniprotkb/Q8N9Z9) carries no function annotation.

**Summary**, from NCBI Gene [160492](https://www.ncbi.nlm.nih.gov/gene/160492):

> Predicted to act upstream of or within cell population proliferation. Predicted to be located in intermediate filament and nucleus. Predicted to be active in cytoplasm and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26683) · Entrez [160492](https://www.ncbi.nlm.nih.gov/gene/160492) · UniProt [Q8N9Z9](https://www.uniprot.org/uniprotkb/Q8N9Z9) · Ensembl [ENSG00000152936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152936)

## Data

Gene col 7669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7669); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7669]; `tensor/DDL_lfc|DDL_z.npy` [7669]; `embed/gene_vectors.npy` [7669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7669 or target_col == 7669). Every well: [[LMNTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMNTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
