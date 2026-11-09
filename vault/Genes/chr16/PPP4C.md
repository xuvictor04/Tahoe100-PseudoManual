---
symbol: "PPP4C"
type: "gene"
col: 7414
ensembl_id: "ENSG00000149923"
name: "protein phosphatase 4 catalytic subunit"
location: "16p11.2"
module: 2
arm: "+"
pooled_cpm: 31.09
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PPP4C

*protein phosphatase 4 catalytic subunit* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.92× (z +13.0, q 8e-36, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.801× (z -4.4, q 0.005, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (HCT15 0.222×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPN1]] (+0.67, fdr 7e-06), [[ARHGEF1]] (+0.65, fdr 7e-06), [[SLC25A44]] (+0.64, fdr 3e-05); moves opposite to [[SETDB2]] (-0.50, fdr 2e-05), [[ZC3H6]] (-0.49, fdr 2e-05), [[ANAPC16]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SDC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +13.0 | 8e-36 | 41/48 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +11.9 | 2e-30 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +9.9 | 7e-21 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +7.2 | 6e-11 | 26/42 (Panc 03.27, J82, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +7.1 | 1e-10 | 30/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.0 | 3e-10 | 23/32 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.41×** | +6.9 | 5e-10 | 31/43 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.2 | 5e-08 | 27/48 (A498, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +5.9 | 2e-07 | 29/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.36×** | +5.8 | 3e-07 | 18/38 (A549, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.8 | 3e-07 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.3 | 4e-06 | 23/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.30×** | +5.1 | 2e-05 | 22/47 (LoVo, PANC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.0 | 2e-05 | 20/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.58×** | +4.8 | 6e-05 | 20/46 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 14/47 (NCI-H2030, SW1417, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.007 | 16/48 (A498, BT-474, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.020 | 9/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.021 | 12/44 (HT-29, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.047 | 6/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BI-78D3 (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.055 | 5/48 (BT-474, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.058 | 3/48 (Panc 03.27, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.078 | 10/47 (SW1417, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7414.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (HCT15 0.222×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.801×** | -4.4 | 0.005 | 20/48 (KATO III, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -3.7 | 0.063 | 12/48 (J82, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.820×** | -3.5 | 0.090 | 14/48 (A-427, HCT15, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.885× | -3.4 | 0.090 | 12/48 (NCI-H23, Hs 766T, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.840× | -3.3 | 0.090 | 13/47 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.889× | -3.3 | 0.090 | 10/48 (KATO III, SHP-77, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 5 µM |  | 0.895× | -3.1 | 0.14 | 4/48 (NCI-H460, SK-MEL-2, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.876× | -3.0 | 0.17 | 7/48 (NCI-H23, A498, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +10.8) | — |
| [[LoVo (line)]] | wt | 25.9 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.13× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 33.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 34.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.0) | — |
| [[A549 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[AsPC-1 (line)]] | alt | 53.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.222× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.06× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPN1]] | +0.67 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ARHGEF1]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SLC25A44]] | +0.64 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[AKT1]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PMPCA]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[NT5DC2]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SH3BP1]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[WDR55]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[RAB5C]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PPP6R1]] | +0.56 | +0.66 / +0.51 | both halves | 1e-05 | STRING 725 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETDB2]] | -0.50 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ZC3H6]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ANAPC16]] | -0.49 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SEPSECS]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NUDCD2]] | -0.49 | -0.32 / -0.57 | both halves | 1e-04 |  |
| [[TMEM42]] | -0.48 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TCEAL4]] | -0.48 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[EBAG9]] | -0.48 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ASNSD1]] | -0.47 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDC1]] | B | SDC1 activity raises PPP4C's level | lines that do not express SDC1 (8) vs lines expressing it (42) | 1.20× lower at baseline in the lines without SDC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CARD10, MFNG, BMAL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (8.3, -26.6); signed map (-50.0, 1.1). **Vector** length 61.2, 9.74% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.0 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +2.6 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | +0.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,075,978-30,085,376 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP4, PPX |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits |
| Hallmark sets | COMPLEMENT |
| Reactome | 5 pathways, smallest: Processing of DNA double-strand break ends; HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA); Homology Directed Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [P60510](https://www.uniprot.org/uniprotkb/P60510) (Serine/threonine-protein phosphatase 4 catalytic subunit):

> Protein phosphatase that is involved in many processes such as microtubule organization at centrosomes, maturation of spliceosomal snRNPs, apoptosis, DNA repair, tumor necrosis factor (TNF)-alpha signaling, activation of c-Jun N-terminal kinase MAPK8, regulation of histone acetylation, DNA damage checkpoint signaling, NF-kappa-B activation and cell migration. The PPP4C-PPP4R1 PP4 complex may play a role in dephosphorylation and regulation of HDAC3. The PPP4C-PPP4R2-PPP4R3A PP4 complex …

**Summary**, from NCBI Gene [5531](https://www.ncbi.nlm.nih.gov/gene/5531):

> Enables protein serine/threonine phosphatase activity. Involved in regulation of double-strand break repair via homologous recombination. Located in chromatin; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9319) · Entrez [5531](https://www.ncbi.nlm.nih.gov/gene/5531) · UniProt [P60510](https://www.uniprot.org/uniprotkb/P60510) · Ensembl [ENSG00000149923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149923)

## Data

Gene col 7414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7414); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7414]; `tensor/DDL_lfc|DDL_z.npy` [7414]; `embed/gene_vectors.npy` [7414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7414 or target_col == 7414). Every well: [[PPP4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
