---
symbol: "NTN1"
type: "gene"
col: 780
ensembl_id: "ENSG00000065320"
name: "netrin 1"
location: "17p13.1"
module: 62
arm: "+"
pooled_cpm: 17.23
n_lines_expressing: 33
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 17
direction_downstream: 11
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# NTN1

*netrin 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.08× (z +28.2, q 0e+00, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.471× (z -7.0, q 1e-09, down in 15 of 28 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.768× (z -4.7, q 5e-04, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF423]] (+0.65, fdr 1e-05), [[CDKN1A]] (+0.62, fdr 1e-05), [[GLIPR2]] (+0.62, fdr 7e-06); moves opposite to [[TOMM70]] (-0.47, fdr 6e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[DNAI3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.08×** | +28.2 | 0e+00 | 25/31 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.49×** | +22.8 | 0e+00 | 26/31 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +19.4 | 0e+00 | 20/31 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.82×** | +18.4 | 0e+00 | 24/30 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.56×** | +16.6 | 0e+00 | 20/30 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +13.9 | 4e-42 | 23/30 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +13.9 | 1e-41 | 21/29 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +13.5 | 2e-39 | 20/30 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.96×** | +11.9 | 5e-31 | 17/30 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +11.2 | 2e-27 | 18/30 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.82×** | +10.6 | 2e-24 | 26/30 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +9.2 | 2e-18 | 17/30 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +8.5 | 6e-16 | 18/31 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.53×** | +7.2 | 2e-11 | 14/29 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.9 | 2e-10 | 17/31 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.31×** | +6.7 | 8e-10 | 13/31 (A549, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +6.7 | 9e-10 | 17/29 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +6.5 | 2e-09 | 9/31 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 2e-05 | 13/30 (NCI-H460, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.471×** | -7.0 | 1e-09 | 15/28 (LoVo, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -5.2 | 7e-05 | 13/28 (NCI-H2030, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -4.7 | 5e-04 | 15/30 (A-172, SW 900, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.787×** | -4.3 | 0.003 | 8/30 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.004 | 13/30 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.008 | 5/30 (SW 900, NCI-H2030, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.820×** | -3.5 | 0.028 | 6/30 (SW 900, A498, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.684×** | -3.5 | 0.028 | 10/29 (NCI-H2030, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.834× | -3.3 | 0.070 | 8/30 (SW 900, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.835× | -3.2 | 0.070 | 3/30 (SW 900, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.11 | 9/30 (SW 900, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.5 | 17 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.4× (z +27.6) | — |
| [[A549 (line)]] | wt | 21.5 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +18.9) | — |
| [[A-427 (line)]] | wt | 89.6 | 2 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.50× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.442× (z -9.2) |
| [[PANC-1 (line)]] | alt | 13.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +19.6) | — |
| [[A-172 (line)]] | wt | 46.4 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.46× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 15.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +13.5) | — |
| [[C32 (line)]] | wt | 7.00 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +12.7) | [[Sunitinib (drug)]] 0.05 µM 0.0710× (z -8.8) |
| [[LoVo (line)]] | wt | 25.0 | 4 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +14.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +14.5) | — |
| [[SW480 (line)]] | alt | 10.2 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 5.27× (z +16.3) | — |
| [[H4 (line)]] | wt | 10.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +11.6) | [[Bortezomib (drug)]] 0.05 µM 0.0637× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 33.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +17.2) | — |
| [[A498 (line)]] | wt | 6.36 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 64.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.1) | [[Verteporfin (drug)]] 5 µM 0.0561× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 50.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.5) | [[Lonafarnib (drug)]] 5 µM 0.0895× (z -13.5) ⚠ toxic |
| [[J82 (line)]] | alt | 7.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.36× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -11.7) |
| [[BT-474 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 5.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.101× (z -9.1) |
| [[SNU-1 (line)]] | wt | 49.5 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF423]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[CDKN1A]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[GLIPR2]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CDIP1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[WIPF3]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DNAI3]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ACHE]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ELOVL7]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RHBDL3]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PLD5]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM70]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 14, C 3. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NTN1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ADRA2C]] | B | ADRA2C activity raises NTN1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without ADRA2C | 0.009 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[CHRNA7]] | B | CHRNA7 activity raises NTN1's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without CHRNA7 | 0.024 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[HES6]] | B | HES6 activity raises NTN1's level | lines that do not express HES6 (8) vs lines expressing it (42) | 3.16× lower at baseline in the lines without HES6 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ACHE]] | B | ACHE activity raises NTN1's level | lines that do not express ACHE (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without ACHE | 0.037 | ⚠ within organs, on part of the lines; also absent: DKK1, KREMEN2; maybe low, not absent |
| [[KCNG3]] | B | KCNG3 activity raises NTN1's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.42× lower at baseline in the lines without KCNG3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[RHBDL3]] | B | RHBDL3 activity raises NTN1's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 3.13× lower at baseline in the lines without RHBDL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[GABBR1]] | B | GABBR1 activity raises NTN1's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without GABBR1 | 0.061 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[DRAM1]] | B | DRAM1 activity raises NTN1's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without DRAM1 | 0.065 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[NFATC1]] | B | NFATC1 activity raises NTN1's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 2.77× lower at baseline in the lines without NFATC1 | 0.068 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |
| [[TOP1]] | B | TOP1 activity lowers NTN1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC16A10]] | B | SLC16A10 activity raises NTN1's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without SLC16A10 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAI3]] | B | NTN1 activity raises DNAI3's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.52× lower at baseline in the lines without NTN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[NFATC1]] | B | NTN1 activity raises NFATC1's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without NTN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[BTG3]] | B | NTN1 activity raises BTG3's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.58× lower at baseline in the lines without NTN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[RHBDL3]] | B | NTN1 activity raises RHBDL3's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.29× lower at baseline in the lines without NTN1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[CHRNA7]] | B | NTN1 activity raises CHRNA7's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.15× lower at baseline in the lines without NTN1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[OLFM2]] | B | NTN1 activity raises OLFM2's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.62× lower at baseline in the lines without NTN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[RASGRP1]] | B | NTN1 activity raises RASGRP1's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without NTN1 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[HHAT]] | B | NTN1 activity raises HHAT's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without NTN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[BTG2]] | B | NTN1 activity strengthens BTG2's drug response | lines that do not express NTN1 (14) vs lines expressing it (27) | the lines without NTN1 respond 0.54× as strongly (z diff +1.51); strongest at Idarubicin (hydrochloride) 5 µM: 1.07x vs 2.21x (z diff +4.3) | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC01828]] | B | NTN1 activity lowers LINC01828's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.65× higher at baseline in the lines without NTN1 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[SH3GL2]] | C | NTN1 activity raises SH3GL2's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without NTN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, 38.5); signed map (44.2, -21.9). **Vector** length 94.1, 23.3% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +22.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +6.0 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | +5.9 | +3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.0 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -7.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | netrin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:9,021,510-9,244,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTN1L, NET1 |
| Gene groups (HGNC) | Netrins |
| Reactome | 9 pathways, smallest: DSCAM interactions; Role of second messengers in netrin-1 signaling; Netrin mediated repulsion signals |
| Matched by | ensembl_id |

**Function**, from UniProt [O95631](https://www.uniprot.org/uniprotkb/O95631) (Netrin-1):

> Netrins control guidance of CNS commissural axons and peripheral motor axons. Its association with either DCC or some UNC5 receptors will lead to axon attraction or repulsion, respectively. Binding to UNC5C might cause dissociation of UNC5C from polymerized TUBB3 in microtubules and thereby lead to increased microtubule dynamics and axon repulsion. Involved in dorsal root ganglion axon projection towards the spinal cord. It also serves as a survival factor via its association with its receptors …

**Summary**, from NCBI Gene [9423](https://www.ncbi.nlm.nih.gov/gene/9423):

> Netrin is included in a family of laminin-related secreted proteins. The function of this gene has not yet been defined; however, netrin is thought to be involved in axon guidance and cell migration during development. Mutations and loss of expression of netrin suggest that variation in netrin may be involved in cancer development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8029) · Entrez [9423](https://www.ncbi.nlm.nih.gov/gene/9423) · UniProt [O95631](https://www.uniprot.org/uniprotkb/O95631) · Ensembl [ENSG00000065320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065320)

## Data

Gene col 780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 780); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 780]; `tensor/DDL_lfc|DDL_z.npy` [780]; `embed/gene_vectors.npy` [780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 780 or target_col == 780). Every well: [[NTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
