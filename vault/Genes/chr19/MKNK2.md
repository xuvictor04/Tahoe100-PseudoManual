---
symbol: "MKNK2"
type: "gene"
col: 1823
ensembl_id: "ENSG00000099875"
name: "MAPK interacting serine/threonine kinase 2"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 90.39
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MKNK2

*MAPK interacting serine/threonine kinase 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.88× (z +5.3, q 6e-05, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.283× (z -5.6, q 1e-05, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERPUD1]] (+0.73, fdr 7e-06), [[DDIT4]] (+0.70, fdr 8e-06), [[CARD19]] (+0.68, fdr 7e-06); moves opposite to [[PSME3IP1]] (-0.64, fdr 4e-05), [[TASOR]] (-0.63, fdr 1e-05), [[ZNF507]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SYTL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +5.3 | 6e-05 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +5.0 | 2e-04 | 32/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +4.8 | 3e-04 | 33/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.011 | 31/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.5 | 0.058 | 6/50 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.32× | +3.3 | 0.10 | 26/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.44× | +3.1 | 0.17 | 25/48 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.283×** | -5.6 | 1e-05 | 40/49 (CFPAC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.286×** | -5.5 | 1e-05 | 40/48 (COLO 205, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.535×** | -5.3 | 3e-05 | 35/48 (H4, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -5.0 | 8e-05 | 29/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -4.7 | 3e-04 | 31/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.676×** | -4.7 | 3e-04 | 26/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -4.4 | 0.001 | 27/49 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.623×** | -3.7 | 0.017 | 25/42 (SW 900, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.6 | 0.017 | 31/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -3.6 | 0.020 | 29/48 (LS 180, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.699× | -3.0 | 0.13 | 28/48 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 269 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0796× (z -16.8) |
| [[LS 180 (line)]] | wt | 200 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -13.1) |
| [[HT-29 (line)]] | alt | 205 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0871× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 74.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -9.7) |
| [[SW 900 (line)]] | alt | 120 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.196× (z -9.8) |
| [[SW480 (line)]] | alt | 76.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +10.9) | — |
| [[A-427 (line)]] | wt | 46.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -17.1) |
| [[COLO 205 (line)]] | alt | 85.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -9.0) |
| [[HCT15 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.6) |
| [[HOP62 (line)]] | alt | 114 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.336× (z -10.6) |
| [[PANC-1 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -11.5) |
| [[SW 1271 (line)]] | alt | 71.4 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.101× (z -8.6) |
| [[SW48 (line)]] | wt | 83.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +9.7) | — |
| [[A-172 (line)]] | wt | 88.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.6) |
| [[A498 (line)]] | wt | 222 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 89.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -9.2) |
| [[H4 (line)]] | wt | 93.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.142× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 54.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 87.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -9.1) |
| [[LoVo (line)]] | wt | 38.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +10.0) | — |
| [[RKO (line)]] | wt | 25.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.99× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 67.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.8) |
| [[SNU-423 (line)]] | alt | 54.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.5) |
| [[SW 1088 (line)]] | alt | 170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.4) |
| [[A549 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERPUD1]] | +0.73 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DDIT4]] | +0.70 | +0.57 / +0.67 | both halves | 8e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[CARD19]] | +0.68 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[RASSF7]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC26A6]] | +0.67 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PLEKHH3]] | +0.67 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PKD1]] | +0.66 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[MPST]] | +0.66 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PMM1]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | -0.64 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TASOR]] | -0.63 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SLC39A10]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.61 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CDK6]] | -0.61 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[CRPPA]] | -0.60 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ZMPSTE24]] | -0.60 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[OTUD4]] | -0.60 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[UTP20]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL1]] | B | SYTL1 activity raises MKNK2's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.54× lower at baseline in the lines without SYTL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[PRSS8]] | B | PRSS8 activity raises MKNK2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without PRSS8 | 0.010 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[S100A14]] | B | S100A14 activity raises MKNK2's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.62× lower at baseline in the lines without S100A14 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[HDAC6]] | B | HDAC6 activity lowers MKNK2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MCTP2]] | B | MCTP2 activity raises MKNK2's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without MCTP2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.6, -3.9); signed map (-30.5, 18.6). **Vector** length 146, 50.0% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.2 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.3 | +4.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.2 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.5 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -0.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | MAPK interacting serine/threonine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,037,465-2,051,244 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MNK2; previously GPRK7 |
| Gene groups (HGNC) | MAPK activated protein kinases; MAPK interacting serine/threonine kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBH9](https://www.uniprot.org/uniprotkb/Q9HBH9) (MAP kinase-interacting serine/threonine-protein kinase 2):

> Serine/threonine-protein kinase that phosphorylates SFPQ/PSF, HNRNPA1 and EIF4E. May play a role in the response to environmental stress and cytokines. Appears to regulate translation by phosphorylating EIF4E, thus increasing the affinity of this protein for the 7-methylguanosine-containing mRNA cap. Required for mediating PP2A-inhibition-induced EIF4E phosphorylation. Triggers EIF4E shuttling from cytoplasm to nucleus. Isoform 1 displays a high basal kinase activity, but isoform 2 exhibits a …

**Summary**, from NCBI Gene [2872](https://www.ncbi.nlm.nih.gov/gene/2872):

> This gene encodes a member of the calcium/calmodulin-dependent protein kinases (CAMK) Ser/Thr protein kinase family, which belongs to the protein kinase superfamily. This protein contains conserved DLG (asp-leu-gly) and ENIL (glu-asn-ile-leu) motifs, and an N-terminal polybasic region which binds importin A and the translation factor scaffold protein eukaryotic initiation factor 4G (eIF4G). This protein is one of the downstream kinases activated by mitogen-activated protein (MAP) kinases. It …

**Accessions** — [HGNC:7111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7111) · Entrez [2872](https://www.ncbi.nlm.nih.gov/gene/2872) · UniProt [Q9HBH9](https://www.uniprot.org/uniprotkb/Q9HBH9) · Ensembl [ENSG00000099875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099875)

## Data

Gene col 1823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1823); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1823]; `tensor/DDL_lfc|DDL_z.npy` [1823]; `embed/gene_vectors.npy` [1823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1823 or target_col == 1823). Every well: [[MKNK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKNK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
