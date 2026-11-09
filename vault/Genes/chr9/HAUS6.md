---
symbol: "HAUS6"
type: "gene"
col: 7229
ensembl_id: "ENSG00000147874"
name: "HAUS augmin like complex subunit 6"
location: "9p22.1"
module: 6
arm: "+"
pooled_cpm: 51.64
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# HAUS6

*HAUS augmin like complex subunit 6* — 9p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +13.8, q 1e-40, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.31× (z +9.3, q 1e-18, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.675× (z -11.9, q 8e-30, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFC4]] (+0.70, fdr 7e-06), [[DSCC1]] (+0.69, fdr 7e-06), [[NCAPD3]] (+0.69, fdr 8e-06); moves opposite to [[CDK3]] (-0.63, fdr 1e-05), [[TP53INP2]] (-0.57, fdr 1e-05), [[MMP25-AS1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.91×** | +13.8 | 1e-40 | 42/48 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.90×** | +13.7 | 2e-40 | 43/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.75×** | +12.0 | 1e-30 | 40/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +9.3 | 1e-18 | 39/48 (SW480, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +8.6 | 9e-16 | 32/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.2 | 5e-08 | 27/48 (SNU-423, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +6.2 | 5e-08 | 31/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +5.5 | 3e-06 | 25/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +5.4 | 4e-06 | 24/48 (SNU-1, A549, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.26×** | +4.9 | 5e-05 | 20/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.26×** | +4.8 | 1e-04 | 21/48 (HOP62, SW480, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 22/48 (HS-578T, A-172, …) | all doses, flat |  |
| [[Mifepristone (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 19/48 (HS-578T, A-172, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 15/48 (A549, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.14× | +3.9 | 0.004 | 8/48 (SK-MEL-2, COLO 205, …) | top dose only | position effect removed |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.004 | 11/47 (HS-578T, SW48, …) | all doses, flat |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.017 | 14/48 (HS-578T, HT-29, …) | top dose only |  |
| [[Pioglitazone (drug)]] 5 µM |  | 1.16× | +3.2 | 0.048 | 12/48 (Hs 766T, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.049 | 7/48 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.15× | +3.0 | 0.073 | 8/48 (HS-578T, A-172, …) | top dose only |  |
| [[Econazole (drug)]] 5 µM |  | 1.15× | +3.0 | 0.081 | 10/48 (A-172, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.675×** | -11.9 | 8e-30 | 36/48 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.745×** | -6.0 | 4e-07 | 25/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.778×** | -5.4 | 2e-05 | 24/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -5.1 | 5e-05 | 2/48 (MIA PaCa-2, CHP-212) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.795×** | -3.5 | 0.053 | 9/47 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.842× | -3.4 | 0.065 | 16/45 (A498, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.864× | -3.1 | 0.15 | 14/47 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.15 | 17/46 (NCI-H661, C-33 A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.869× | -3.0 | 0.15 | 11/48 (SW 1088, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 132 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 52.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -14.8) |
| [[HS-578T (line)]] | alt | 60.2 | 2 | 1 | [[Mifepristone (drug)]] 0.5 µM 2.80× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -8.9) |
| [[A-172 (line)]] | wt | 58.2 | 1 | 1 | [[Mifepristone (drug)]] 0.5 µM 2.30× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.8) |
| [[A-427 (line)]] | wt | 49.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -13.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 2 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0761× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 50.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.4) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 49.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.0) |
| [[PANC-1 (line)]] | alt | 34.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -15.3) |
| [[SW480 (line)]] | alt | 68.2 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.09× (z +9.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.64× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 69.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -14.0) |
| [[COLO 205 (line)]] | alt | 44.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 48.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.8) |
| [[J82 (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -9.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 67.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 69.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 77.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.5) |
| [[SNU-1 (line)]] | wt | 51.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.2) |
| [[SW48 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0858× (z -8.5) ⚠ toxic |
| [[A549 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFC4]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.69 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[TTI1]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[TICRR]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 | pathway: G2/M Transition |
| [[ERI1]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[POLQ]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ORC1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[BLM]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[PRKDC]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PRIM1]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[POLA1]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK3]] | -0.63 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MMP25-AS1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[MYL5]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NUTM2E]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CDIP1]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises HAUS6's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without TCF19 | 0.028 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MELK]] | C | MELK activity raises HAUS6's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity raises HAUS6's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without PBK | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.1, -45.5); signed map (-37.5, -41.1). **Vector** length 115, 29.5% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of the pre-replicative complex* (reactome, mean cos +0.50 to 22); *Telomere C-strand (Lagging Strand) Synthesis* (reactome, mean cos +0.51 to 19); *Lagging Strand Synthesis* (reactome, mean cos +0.50 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.4 | +13.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.1 | +12.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.6 | +13.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.5 | -11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -6.6 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.0 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:19,053,141-19,102,904 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20060, KIAA1574, dgt6; previously FAM29A |
| Gene groups (HGNC) | HAUS augmin like complex ; Small nucleolar RNA protein coding host genes; Centriolar satellite proteins |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4H7](https://www.uniprot.org/uniprotkb/Q7Z4H7) (HAUS augmin-like complex subunit 6):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex. Promotes the nucleation of microtubules from the spindle through recruitment of NEDD1 and gamma-tubulin.

**Summary**, from NCBI Gene [54801](https://www.ncbi.nlm.nih.gov/gene/54801):

> The protein encoded by this gene is a subunit of the augmin complex. The augmin complex plays a role in microtubule attachment to the kinetochore and central spindle formation. This protein may have a role in efficient chromosome congression and segregation by promoting microtubule-dependent microtubule amplification. Pseudogenes of this gene are located on chromosomes 7 and 20. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by …

**Accessions** — [HGNC:25948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25948) · Entrez [54801](https://www.ncbi.nlm.nih.gov/gene/54801) · UniProt [Q7Z4H7](https://www.uniprot.org/uniprotkb/Q7Z4H7) · Ensembl [ENSG00000147874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147874)

## Data

Gene col 7229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7229); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7229]; `tensor/DDL_lfc|DDL_z.npy` [7229]; `embed/gene_vectors.npy` [7229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7229 or target_col == 7229). Every well: [[HAUS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
