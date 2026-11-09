---
symbol: "EGLN2"
type: "gene"
col: 15640
ensembl_id: "ENSG00000269858"
name: "egl-9 family hypoxia inducible factor 2"
location: "19q13.2"
module: 11
arm: "+"
pooled_cpm: 12.53
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# EGLN2

*egl-9 family hypoxia inducible factor 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.38× (z +5.9, q 2e-06, up in 23 of 46 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.48× (z +4.9, q 2e-04, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.521× (z -4.5, q 0.004, down in 20 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HS-578T 0.0765×, LoVo 0.146×, KATO III 0.164×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.218×, A-172 0.226×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0553×; ⚠ toxic; transcription drop); [[Silodosin (drug)]] 5 µM in 1 line (HCT15 0.0851×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC66A1]] (+0.72, fdr 7e-06), [[PIAS4]] (+0.64, fdr 1e-05), [[TOPORS]] (+0.63, fdr 1e-05); moves opposite to [[OPA1]] (-0.62, fdr 1e-05), [[RPL6]] (-0.60, fdr 1e-05), [[BPNT2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MSX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.38×** | +5.9 | 2e-06 | 23/46 (BT-474, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.2 | 7e-05 | 3/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.9 | 2e-04 | 23/43 (NCI-H23, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.9 | 2e-04 | 21/45 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.6 | 5e-04 | 22/46 (KATO III, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.2 | 0.002 | 17/41 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +4.2 | 0.003 | 17/43 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.003 | 20/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.9 | 0.007 | 21/46 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.025 | 14/44 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.29×** | +3.3 | 0.050 | 14/46 (KATO III, A-172, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.079 | 7/45 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.090 | 3/46 (H4, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.091 | 9/41 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.0 | 0.091 | 6/29 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15640.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HS-578T 0.0765×, LoVo 0.146×, KATO III 0.164×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.218×, A-172 0.226×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0553×; ⚠ toxic; transcription drop); [[Silodosin (drug)]] 5 µM in 1 line (HCT15 0.0851×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -4.5 | 0.004 | 20/44 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.531×** | -4.4 | 0.004 | 18/47 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.761×** | -3.5 | 0.098 | 15/25 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.718× | -3.3 | 0.11 | 10/31 (HS-578T, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.780× | -3.3 | 0.11 | 12/35 (MIA PaCa-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.777× | -3.2 | 0.12 | 14/46 (SNU-423, J82, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -3.2 | 0.12 | 15/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0851× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -10.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0765× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0553× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -10.8) ⚠ toxic |
| [[RKO (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A1]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[PIAS4]] | +0.64 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CD2BP2]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[DAXX]] | +0.62 | +0.36 / +0.69 | both halves | 1e-04 |  |
| [[RCE1]] | +0.62 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[RRAGC]] | +0.62 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SEMA4C]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[TRIM47]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CDK3]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[RPL6]] | -0.60 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[BPNT2]] | -0.60 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.59 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[TMED7]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PAICS]] | -0.57 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[LYRM7]] | -0.57 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[SKP2]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.56 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[BTAF1]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[MRPL19]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PRPF8]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | MSX1 activity lowers EGLN2's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without MSX1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.1, -2.5); signed map (1.2, -10.1). **Vector** length 74.2, 14.0% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.8 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | egl-9 family hypoxia inducible factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,798,996-40,808,434 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHD1, HIFPH1 |
| Gene groups (HGNC) | Egl-9 family hypoxia inducible factors |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 4 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KS0](https://www.uniprot.org/uniprotkb/Q96KS0) (Prolyl hydroxylase EGLN2):

> Prolyl hydroxylase that mediates hydroxylation of proline residues in target proteins, such as ATF4, IKBKB, CEP192 and HIF1A. Target proteins are preferentially recognized via a LXXLAP motif. Cellular oxygen sensor that catalyzes, under normoxic conditions, the post-translational formation of 4-hydroxyproline in hypoxia-inducible factor (HIF) alpha proteins. Hydroxylates a specific proline found in each of the oxygen-dependent degradation (ODD) domains (N-terminal, NODD, and C-terminal, CODD) …

**Summary**, from NCBI Gene [112398](https://www.ncbi.nlm.nih.gov/gene/112398):

> The hypoxia inducible factor (HIF) is a transcriptional complex that is involved in oxygen homeostasis. At normal oxygen levels, the alpha subunit of HIF is targeted for degration by prolyl hydroxylation. This gene encodes an enzyme responsible for this post-translational modification. Alternative splicing results in multiple transcript variants. Read-through transcription also exists between this gene and the upstream RAB4B (RAB4B, member RAS oncogene family) gene. [provided by RefSeq, Feb …

**Accessions** — [HGNC:14660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14660) · Entrez [112398](https://www.ncbi.nlm.nih.gov/gene/112398) · UniProt [Q96KS0](https://www.uniprot.org/uniprotkb/Q96KS0) · Ensembl [ENSG00000269858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269858)

## Data

Gene col 15640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15640); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15640]; `tensor/DDL_lfc|DDL_z.npy` [15640]; `embed/gene_vectors.npy` [15640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15640 or target_col == 15640). Every well: [[EGLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
