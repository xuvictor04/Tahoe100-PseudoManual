---
symbol: "SCARA3"
type: "gene"
col: 9594
ensembl_id: "ENSG00000168077"
name: "scavenger receptor class A member 3"
location: "8p21.1"
module: 6
arm: "+"
pooled_cpm: 8.04
n_lines_expressing: 31
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SCARA3

*scavenger receptor class A member 3* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.67× (z +13.7, q 1e-39, up in 10 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bentamapimod (drug)]] 0.05 µM: 1.59× (z +4.4, q 0.001, up in 8 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.386× (z -14.7, q 1e-45, down in 22 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBLN1]] (+0.66, fdr 1e-05), [[CEP78]] (+0.59, fdr 1e-05), [[DDX12P]] (+0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DKK3]] → it (grade B ⚠); 8 go from it, the strongest it → [[F2R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +13.7 | 1e-39 | 10/11 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +12.2 | 1e-31 | 18/20 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +7.1 | 3e-10 | 10/15 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.59×** | +4.4 | 0.001 | 8/26 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.6 | 0.026 | 3/16 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.026 | 8/27 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.6 | 0.026 | 3/9 (A-172, HS-578T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.094 | 5/26 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.094 | 6/28 (A-172, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.386×** | -14.7 | 1e-45 | 22/24 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.404×** | -9.9 | 2e-20 | 19/26 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.406×** | -9.8 | 2e-20 | 22/27 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.446×** | -8.8 | 2e-16 | 21/24 (Hs 766T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.477×** | -8.1 | 9e-14 | 21/28 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.496×** | -7.3 | 2e-11 | 15/27 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.599×** | -5.6 | 2e-06 | 16/26 (A-172, H4, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.600×** | -5.6 | 2e-06 | 17/27 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.607×** | -5.4 | 4e-06 | 16/27 (SW48, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -4.8 | 7e-05 | 16/24 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.641×** | -4.6 | 2e-04 | 14/25 (SW48, HS-578T, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -4.5 | 3e-04 | 12/28 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -4.2 | 1e-03 | 8/28 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -4.2 | 0.001 | 4/29 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -4.0 | 0.003 | 10/25 (C-33 A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.778×** | -3.8 | 0.004 | 7/29 (KATO III, A549, …) | top dose only |  |
| [[Captopril (drug)]] 5 µM |  | **0.706×** | -3.8 | 0.005 | 1/27 (SW480) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.4) |
| [[A-172 (line)]] | wt | 37.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.2) |
| [[SW480 (line)]] | alt | 5.61 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -14.3) |
| [[H4 (line)]] | wt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0841× (z -9.5) |
| [[HOP62 (line)]] | alt | 9.49 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -8.6) |
| [[Hs 766T (line)]] | wt | 60.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -18.7) |
| [[HS-578T (line)]] | alt | 61.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.3) |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -8.7) |
| [[KATO III (line)]] | alt | 5.01 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0642× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0820× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 4.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.3) |
| [[RKO (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0750× (z -11.3) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-427 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBLN1]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CEP78]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DDX12P]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PARP1]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[POGLUT3]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CASP2]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[FOXM1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[GUSB]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[MMS22L]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TUBGCP3]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[WDR76]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[HELLS]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DKK3]] | B | DKK3 activity raises SCARA3's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without DKK3 | 0.054 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[DZIP1L]] | B | DZIP1L activity raises SCARA3's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.52× lower at baseline in the lines without DZIP1L | 0.060 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[FHL1]] | B | FHL1 activity raises SCARA3's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without FHL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2R]] | B | SCARA3 activity raises F2R's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without SCARA3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[CRTAP]] | B | SCARA3 activity raises CRTAP's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.62× lower at baseline in the lines without SCARA3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[RBBP7]] | B | SCARA3 activity raises RBBP7's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without SCARA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[PRPS2]] | B | SCARA3 activity raises PRPS2's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without SCARA3 | 0.061 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[P3H3]] | B | SCARA3 activity raises P3H3's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.78× lower at baseline in the lines without SCARA3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[ANXA6]] | B | SCARA3 activity raises ANXA6's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without SCARA3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[POGLUT3]] | B | SCARA3 activity raises POGLUT3's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without SCARA3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[DKK3]] | B | SCARA3 activity raises DKK3's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 2.48× lower at baseline in the lines without SCARA3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.7, -43.1); signed map (-34.7, -43.0). **Vector** length 53.3, 10.8% of its response variance represented; |z| ≥ 3 in 647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.6 | +4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -7.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor class A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:27,633,868-27,676,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSR1, CSR, MSLR1, APC7, MSRL1 |
| Gene groups (HGNC) | Scavenger receptors; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6AZY7](https://www.uniprot.org/uniprotkb/Q6AZY7) (Scavenger receptor class A member 3):

> Seems to protect cells by scavenging oxidative molecules or harmful products of oxidation.

**Summary**, from NCBI Gene [51435](https://www.ncbi.nlm.nih.gov/gene/51435):

> This gene encodes a macrophage scavenger receptor-like protein. This protein has been shown to deplete reactive oxygen species, and thus play an important role in protecting cells from oxidative stress. The expression of this gene is induced by oxidative stress. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19000) · Entrez [51435](https://www.ncbi.nlm.nih.gov/gene/51435) · UniProt [Q6AZY7](https://www.uniprot.org/uniprotkb/Q6AZY7) · Ensembl [ENSG00000168077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168077)

## Data

Gene col 9594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9594); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9594]; `tensor/DDL_lfc|DDL_z.npy` [9594]; `embed/gene_vectors.npy` [9594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9594 or target_col == 9594). Every well: [[SCARA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCARA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
