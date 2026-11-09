---
symbol: "STK32C"
type: "gene"
col: 9180
ensembl_id: "ENSG00000165752"
name: "serine/threonine kinase 32C"
location: "10q26.3"
module: 3
arm: "+"
pooled_cpm: 22.32
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# STK32C

*serine/threonine kinase 32C* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.26× (z +9.9, q 3e-20, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.447× (z -9.7, q 1e-19, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXP]] (+0.76, fdr 7e-06), [[RAB40C]] (+0.73, fdr 7e-06), [[VKORC1]] (+0.72, fdr 7e-06); moves opposite to [[TASOR]] (-0.71, fdr 7e-06), [[ZNF655]] (-0.71, fdr 7e-06), [[DNAJC8]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +9.9 | 3e-20 | 42/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +7.1 | 4e-10 | 30/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +5.7 | 2e-06 | 33/46 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +4.8 | 2e-04 | 25/43 (A498, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.7 | 3e-04 | 28/46 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.3 | 0.002 | 21/44 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.62×** | +4.2 | 0.002 | 18/45 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.014 | 18/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +3.7 | 0.015 | 21/46 (HOP62, A498, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.040 | 18/43 (COLO 205, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.056 | 10/34 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.30×** | +3.2 | 0.071 | 13/45 (HS-578T, PANC-1, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.071 | 12/46 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.094 | 11/44 (SW 900, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.447×** | -9.7 | 1e-19 | 35/46 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -4.9 | 3e-04 | 25/46 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.771×** | -4.4 | 0.002 | 23/46 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -3.9 | 0.016 | 22/45 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.551×** | -3.8 | 0.019 | 19/47 (NCI-H460, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -3.3 | 0.078 | 20/46 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.837× | -3.0 | 0.19 | 10/47 (SW 1088, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 53.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.7) |
| [[A-172 (line)]] | wt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.6) |
| [[A-427 (line)]] | wt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.6) |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 16.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0799× (z -10.2) |
| [[HOP62 (line)]] | alt | 9.81 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +8.6) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.2) |
| [[LoVo (line)]] | wt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 9.62 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.7) |
| [[SNU-423 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.6) |
| [[SW480 (line)]] | alt | 21.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[A498 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXP]] | +0.76 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.73 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[PKD1]] | +0.71 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CARD19]] | +0.71 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[GUK1]] | +0.71 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[XYLT2]] | +0.70 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CD81]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SLC26A6]] | +0.69 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.69 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.69 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.71 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.71 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[DNAJC8]] | -0.70 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.67 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.66 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[DPP8]] | -0.66 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[TRIP12]] | -0.66 | -0.43 / -0.65 | both halves | 4e-05 |  |
| [[GDAP1]] | -0.65 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[SMIM15]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.65 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[TAF2]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity strengthens STK32C's drug response | lines that do not express SLC17A7 (8) vs lines expressing it (39) | the lines without SLC17A7 respond 0.81× as strongly (z diff +0.74); strongest at Homoharringtonine 5 µM: 1.31x vs 0.68x (z diff +5.1) | 0.048 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[NXPH4]] | B | NXPH4 activity raises STK32C's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without NXPH4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[STARD9]] | B | STARD9 activity weakens STK32C's drug response | lines that do not express STARD9 (7) vs lines expressing it (40) | the lines without STARD9 respond 0.96× as strongly (z diff +0.25); strongest at Panobinostat 5 µM: 4.03x vs 2.25x (z diff -3.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CAMKK1]] | C | CAMKK1 activity raises STK32C's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without CAMKK1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.1, -3.0); signed map (-31.7, 17.8). **Vector** length 86.3, 19.4% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +9.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 32C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,207,492-132,331,847 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKE, MGC23665, YANK3 |
| Gene groups (HGNC) | Serine/threonine kinase 32 family |
| Matched by | ensembl_id |

UniProt [Q86UX6](https://www.uniprot.org/uniprotkb/Q86UX6) carries no function annotation.

**Summary**, from NCBI Gene [282974](https://www.ncbi.nlm.nih.gov/gene/282974):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. It is thought that this family member is functional in brain due to its high expression levels there. DNA methylation differences have been found in this gene in monozygotic twins that are discordant for adolescent depression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:21332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21332) · Entrez [282974](https://www.ncbi.nlm.nih.gov/gene/282974) · UniProt [Q86UX6](https://www.uniprot.org/uniprotkb/Q86UX6) · Ensembl [ENSG00000165752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165752)

## Data

Gene col 9180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9180); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9180]; `tensor/DDL_lfc|DDL_z.npy` [9180]; `embed/gene_vectors.npy` [9180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9180 or target_col == 9180). Every well: [[STK32C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK32C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
