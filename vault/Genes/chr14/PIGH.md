---
symbol: "PIGH"
type: "gene"
col: 1985
ensembl_id: "ENSG00000100564"
name: "phosphatidylinositol glycan anchor biosynthesis class H"
location: "14q24.1"
module: 24
arm: "+"
pooled_cpm: 11.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PIGH

*phosphatidylinositol glycan anchor biosynthesis class H* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.95× (z +14.6, q 1e-45, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HOP62 0.174×, NCI-H2347 0.284×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.262×; ⚠ cell-cycle shift, explains ~0% of this change); [[Alpelisib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0819×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIF1B]] (+0.72, fdr 1e-05), [[NDUFA12]] (+0.68, fdr 4e-05), [[RNF114]] (+0.68, fdr 1e-05); moves opposite to [[RCC2]] (-0.69, fdr 1e-05), [[PBLD]] (-0.68, fdr 4e-05), [[EPM2A]] (-0.68, fdr 3e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PEAR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +14.6 | 1e-45 | 45/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.67×** | +13.3 | 6e-38 | 45/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +13.2 | 1e-37 | 43/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +6.8 | 1e-09 | 34/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +6.4 | 2e-08 | 26/45 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.3 | 1e-05 | 23/48 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.9 | 1e-04 | 16/42 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.38×** | +4.4 | 8e-04 | 13/35 (HEC-1-A, SW480, …) | all doses, flat | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.009 | 8/44 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.019 | 5/45 (NCI-H2030, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.031 | 9/47 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.036 | 8/48 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.056 | 8/41 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.060 | 9/44 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.27×** | +3.2 | 0.060 | 8/22 (PANC-1, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HOP62 0.174×, NCI-H2347 0.284×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.262×; ⚠ cell-cycle shift, explains ~0% of this change); [[Alpelisib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0819×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 0.839× | -3.3 | 0.23 | 14/48 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -3.3 | 0.23 | 15/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.634× | -3.2 | 0.24 | 13/43 (LOX-IMVI, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.793× | -3.1 | 0.25 | 3/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.45× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[Hs 766T (line)]] | wt | 7.10 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0819× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 16.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | +0.72 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.68 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RNF114]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.68 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[NECAP1]] | +0.68 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[PLPPR2]] | +0.68 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[EDF1]] | +0.68 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[RBIS]] | +0.67 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CIAO2B]] | +0.66 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PLD3]] | +0.66 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CYB561D1]] | +0.65 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.65 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC2]] | -0.69 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[PBLD]] | -0.68 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[EPM2A]] | -0.68 | -0.63 / -0.28 | both halves | 3e-04 |  |
| [[SLC39A10]] | -0.68 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[CRPPA]] | -0.67 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.67 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TASOR]] | -0.66 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SNX5]] | -0.66 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[PSME3IP1]] | -0.66 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PRRC2B]] | -0.65 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[FGD5-AS1]] | -0.65 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.65 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEAR1]] | B | PEAR1 activity lowers PIGH's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 1.09× higher at baseline in the lines without PEAR1 | 0.090 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[LINC01518]] | B | LINC01518 activity weakens PIGH's drug response | lines that do not express LINC01518 (36) vs lines expressing it (12) | the lines without LINC01518 respond 1.36× as strongly (z diff -0.30); strongest at Panobinostat 0.5 µM: 3.04x vs 2.31x (z diff -1.8) | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.5, -5.6); signed map (-30.2, 1.3). **Vector** length 73.1, 13.1% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.1 | +13.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +13.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +14.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -0.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,581,955-67,600,286 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPI-H |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol-N-acetylglucosaminyltransferase complex |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14442](https://www.uniprot.org/uniprotkb/Q14442) (Phosphatidylinositol N-acetylglucosaminyltransferase subunit H):

> Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis.

**Summary**, from NCBI Gene [5283](https://www.ncbi.nlm.nih.gov/gene/5283):

> This gene encodes an endoplasmic reticulum associated protein that is involved in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI anchor is a glycolipid found on many blood cells and which serves to anchor proteins to the cell surface. The protein encoded by this gene is a subunit of the GPI N-acetylglucosaminyl (GlcNAc) transferase that transfers GlcNAc to phosphatidylinositol (PI) on the cytoplasmic side of the endoplasmic reticulum. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8964) · Entrez [5283](https://www.ncbi.nlm.nih.gov/gene/5283) · UniProt [Q14442](https://www.uniprot.org/uniprotkb/Q14442) · Ensembl [ENSG00000100564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100564)

## Data

Gene col 1985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1985); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1985]; `tensor/DDL_lfc|DDL_z.npy` [1985]; `embed/gene_vectors.npy` [1985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1985 or target_col == 1985). Every well: [[PIGH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
