---
symbol: "WHAMMP1"
type: "gene"
col: 13345
ensembl_id: "ENSG00000223509"
name: "WHAMM pseudogene 1"
location: "15q13.3"
module: 175
arm: "+"
pooled_cpm: 6.36
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# WHAMMP1

*WHAMM pseudogene 1* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.30× (z +8.2, q 1e-13, up in 28 of 46 measured lines) ⚠ position not correctable.
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.523× (z -8.5, q 1e-14, down in 26 of 39 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.595× (z -4.6, q 7e-04, down in 25 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (J82 0.121×, NCI-H460 0.233×, HOP62 0.204×, C32 0.223×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HOP62 0.0955×, A498 0.134×, NCI-H2030 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.129×, HOP62 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.0745×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (A-172 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A2]] (+0.72, fdr 7e-06), [[PMS2P3-1]] (+0.69, fdr 7e-06), [[ABCB10]] (+0.68, fdr 7e-06); moves opposite to [[BCL10]] (-0.64, fdr 1e-05), [[SLC22A1]] (-0.61, fdr 7e-06), [[DNAH17]] (-0.61, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[UNC13D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.30×** | +8.2 | 1e-13 | 28/46 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.43× | +3.3 | 0.16 | 7/44 (SW48, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.43× | +3.3 | 0.16 | 12/45 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13345.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (J82 0.121×, NCI-H460 0.233×, HOP62 0.204×, C32 0.223×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HOP62 0.0955×, A498 0.134×, NCI-H2030 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.129×, HOP62 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.0745×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (A-172 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.523×** | -8.5 | 1e-14 | 26/39 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.586×** | -4.7 | 6e-04 | 21/42 (C32, A-427, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -4.6 | 7e-04 | 25/38 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -4.4 | 0.001 | 22/44 (MIA PaCa-2, C32, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.697×** | -3.3 | 0.095 | 15/27 (A498, A-172, …) | inconsistent across doses | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 8.90 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0955× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 6.63 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.112× (z -8.5) |
| [[A498 (line)]] | wt | 13.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[C32 (line)]] | wt | 15.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 9.30 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0745× (z -8.8) |
| [[HS-578T (line)]] | alt | 4.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ABCB10]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NDC1]] | +0.67 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[RPA1]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NAPB]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LNPK]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PCCB]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ALG9]] | +0.60 | +0.70 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL10]] | -0.64 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[SLC22A1]] | -0.61 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[DNAH17]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[MTNR1A]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[PPP1R10]] | -0.59 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.58 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[ADNP2]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[BPTF]] | -0.57 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[XKR6]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ZNF829]] | -0.57 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[HDAC9]] | -0.56 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[CAVIN4]] | -0.56 | -0.66 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC13D]] | B | UNC13D activity lowers WHAMMP1's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.66× higher at baseline in the lines without UNC13D | 0.008 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[CD22]] | B | CD22 activity lowers WHAMMP1's level | lines that do not express CD22 (21) vs lines expressing it (29) | 1.26× higher at baseline in the lines without CD22 | 0.089 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.6, -14.6); signed map (-38.8, -14.2). **Vector** length 60.7, 9.07% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +0.9 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +0.9 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.0 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.4 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | WHAMM pseudogene 1 |
| Locus type | pseudogene |
| Location | 15q13.3 — chr15:32,523,026-32,536,926 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously WHDC1P1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32361) · Entrez [100288615](https://www.ncbi.nlm.nih.gov/gene/100288615) · Ensembl [ENSG00000223509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223509)

## Data

Gene col 13345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13345); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13345]; `tensor/DDL_lfc|DDL_z.npy` [13345]; `embed/gene_vectors.npy` [13345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13345 or target_col == 13345). Every well: [[WHAMMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WHAMMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
