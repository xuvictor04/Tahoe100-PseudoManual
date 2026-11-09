---
symbol: "ZNF280B"
type: "gene"
col: 15835
ensembl_id: "ENSG00000275004"
name: "zinc finger protein 280B"
location: "22q11.22"
module: 16
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 38
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF280B

*zinc finger protein 280B* — 22q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.55× (z +13.0, q 4e-36, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.666× (z -5.7, q 6e-06, down in 15 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.185×, SHP-77 0.215×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.115×); [[Sinomenine (drug)]] 0.5 µM in 1 line (HCT15 0.0613×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0912×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF2]] (+0.53, fdr 9e-05), [[RDH14]] (+0.53, fdr 5e-05), [[LRP12]] (+0.50, fdr 3e-04); moves opposite to [[AKT2]] (-0.51, fdr 4e-05), [[COPB2-DT]] (-0.45, fdr 6e-04), [[CCNL2]] (-0.44, fdr 5e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HHEX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +13.0 | 4e-36 | 28/36 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.25×** | +11.3 | 4e-27 | 26/36 (A498, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.08×** | +10.2 | 3e-22 | 26/36 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +9.6 | 7e-20 | 17/33 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +8.7 | 3e-16 | 17/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.3 | 2e-11 | 20/36 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.4 | 2e-08 | 14/33 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +5.9 | 2e-07 | 14/35 (A-172, A549, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.8 | 3e-07 | 10/35 (NCI-H1573, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.8 | 4e-07 | 17/36 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 3e-06 | 16/36 (SK-MEL-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 3e-06 | 12/32 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 1e-05 | 11/33 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +4.9 | 3e-05 | 7/34 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.9 | 4e-05 | 10/36 (A-427, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.9 | 4e-05 | 6/36 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.2 | 7e-04 | 9/35 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.002 | 13/35 (SK-MEL-2, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.034 | 3/31 (LoVo, A549, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.185×, SHP-77 0.215×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.115×); [[Sinomenine (drug)]] 0.5 µM in 1 line (HCT15 0.0613×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0912×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -5.7 | 6e-06 | 15/36 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.801× | -3.1 | 0.37 | 11/29 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ML264 (drug)]] 0.05 µM |  | 0.792× | -3.1 | 0.37 | 2/36 (SW 1271, SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.2 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 6.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 7.57 | 0 | 1 | — | [[Sinomenine (drug)]] 0.5 µM 0.0613× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.34 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0912× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 6.19 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -9.5) |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF2]] | +0.53 | +0.37 / +0.50 | both halves | 9e-05 |  |
| [[RDH14]] | +0.53 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[LRP12]] | +0.50 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[FSD1L]] | +0.50 | +0.39 / +0.38 | both halves | 6e-05 |  |
| [[ZFP1]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 | same gene group |
| [[MSANTD4]] | +0.49 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[DGAT2]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[LSM10]] | +0.48 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MSL3P1]] | +0.48 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[FAM169A]] | +0.47 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ZNF625]] | +0.46 | +0.50 / +0.35 | both halves | 1e-04 | same gene group |
| [[FAM241B]] | +0.46 | +0.37 / +0.47 | both halves | 8e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT2]] | -0.51 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[COPB2-DT]] | -0.45 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[CCNL2]] | -0.44 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[GET4]] | -0.43 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[LTB4R]] | -0.41 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[TPCN1]] | -0.41 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[CDK5RAP3]] | -0.41 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[CA5BP1]] | -0.40 | -0.48 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHEX]] | B | HHEX activity raises ZNF280B's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without HHEX | 0.067 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.292). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.6, 3.2); signed map (-0.1, -19.0). **Vector** length 42.1, 5.37% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +4.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +2.6 |
|  | [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -2.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 280B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.22 — chr22:22,484,421-22,508,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 5'OY11.1, ZNF632; previously ZNF279, SUHW2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YH2](https://www.uniprot.org/uniprotkb/Q86YH2) (Zinc finger protein 280B):

> May function as a transcription factor.

**Summary**, from NCBI Gene [140883](https://www.ncbi.nlm.nih.gov/gene/140883):

> The protein encoded by this gene is a transcription factor that upregulates expression of MDM2, which negatively regulates p53 expression. This gene is highly expressed in prostate cancer cells, which leads to a reduction in p53 levels and an increase in growth of the cancer cells. Several transcript variants have been found for this gene, but only one of them is protein-coding. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:23022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23022) · Entrez [140883](https://www.ncbi.nlm.nih.gov/gene/140883) · UniProt [Q86YH2](https://www.uniprot.org/uniprotkb/Q86YH2) · Ensembl [ENSG00000275004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275004)

## Data

Gene col 15835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15835); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15835]; `tensor/DDL_lfc|DDL_z.npy` [15835]; `embed/gene_vectors.npy` [15835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15835 or target_col == 15835). Every well: [[ZNF280B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF280B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
