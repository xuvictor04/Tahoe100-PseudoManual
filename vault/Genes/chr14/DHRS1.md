---
symbol: "DHRS1"
type: "gene"
col: 8065
ensembl_id: "ENSG00000157379"
name: "dehydrogenase/reductase 1"
location: "14q12"
module: 30
arm: "+"
pooled_cpm: 6.82
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# DHRS1

*dehydrogenase/reductase 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +8.5, q 1e-14, up in 27 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -10.6, q 1e-23, down in 34 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC11A]] (+0.78, fdr 7e-06), [[IFI27L1]] (+0.74, fdr 7e-06), [[NDUFAF7]] (+0.72, fdr 7e-06); moves opposite to [[ZMYM4]] (-0.66, fdr 7e-06), [[R3HDM2]] (-0.63, fdr 2e-05), [[PBRM1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF474]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SDHAP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.5 | 1e-14 | 27/40 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.9 | 1e-06 | 18/46 (HOP62, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.2 | 3e-05 | 17/47 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.1 | 4e-05 | 10/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +5.0 | 8e-05 | 16/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.9 | 1e-04 | 17/41 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 6e-04 | 14/41 (NCI-H2030, SW48, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +4.3 | 0.001 | 18/46 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.2 | 0.002 | 7/19 (NCI-H2030, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +4.2 | 0.002 | 15/37 (SW480, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.0 | 0.003 | 12/35 (NCI-H2030, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.005 | 13/45 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.8 | 0.005 | 13/43 (LS 180, HCT15, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.015 | 5/43 (PANC-1, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.015 | 5/35 (LS 180, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.018 | 7/36 (SW 900, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.033 | 9/42 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.053 | 8/47 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -10.6 | 1e-23 | 34/39 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -10.3 | 2e-22 | 36/44 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -8.5 | 3e-15 | 28/38 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -5.5 | 4e-06 | 23/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -4.0 | 0.008 | 12/39 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.583× | -3.3 | 0.11 | 10/44 (COLO 205, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.758× | -3.2 | 0.11 | 16/44 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.766× | -3.1 | 0.15 | 11/46 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 8.28 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.2) |
| [[Hs 766T (line)]] | wt | 8.58 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 5.17 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.3) |
| [[A-172 (line)]] | wt | 7.10 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0629× (z -12.2) |
| [[HS-578T (line)]] | alt | 7.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 5.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.170× (z -8.5) |
| [[RKO (line)]] | wt | 3.19 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.106× (z -8.9) |
| [[SNU-423 (line)]] | alt | 6.36 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0806× (z -9.9) |
| [[A-427 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC11A]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[IFI27L1]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ATPAF2]] | +0.70 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.67 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CDS2]] | +0.67 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PIP4K2C]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MAX]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[R3HDM2]] | -0.63 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[PBRM1]] | -0.63 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.63 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[EPC2]] | -0.63 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MIS12]] | -0.63 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.63 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[BPTF]] | -0.62 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[ZC3H11A]] | -0.62 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[PPP1R10]] | -0.61 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[RBM23]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF474]] | B | ZNF474 activity lowers DHRS1's level | lines that do not express ZNF474 (6) vs lines expressing it (44) | 1.41× higher at baseline in the lines without ZNF474 | 0.085 | ⚠ within organs, on part of the lines; also absent: RBFOX1, NEK10, LINC01524; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP2]] | C | DHRS1's natural level strengthens SDHAP2's drug response | DHRS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69, reverse -0.09; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.3, -14.5); signed map (-36.6, -8.6). **Vector** length 73.8, 13.2% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,290,598-24,299,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25430, MGC20204, SDR19C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LJ7](https://www.uniprot.org/uniprotkb/Q96LJ7) (Dehydrogenase/reductase SDR family member 1):

> NADPH-dependent oxidoreductase which catalyzes the reduction of steroids (estrone, androstene-3,17-dione and cortisone) as well as prostaglandin E1, isatin and xenobiotics in vitro. May have a role in steroid and/or xenobiotic metabolism.

**Summary**, from NCBI Gene [115817](https://www.ncbi.nlm.nih.gov/gene/115817):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family. The encoded enzyme contains a conserved catalytic domain and likely functions as an oxidoreductase. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:16445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16445) · Entrez [115817](https://www.ncbi.nlm.nih.gov/gene/115817) · UniProt [Q96LJ7](https://www.uniprot.org/uniprotkb/Q96LJ7) · Ensembl [ENSG00000157379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157379)

## Data

Gene col 8065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8065); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8065]; `tensor/DDL_lfc|DDL_z.npy` [8065]; `embed/gene_vectors.npy` [8065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8065 or target_col == 8065). Every well: [[DHRS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
