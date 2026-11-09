---
symbol: "MSANTD4"
type: "gene"
col: 10022
ensembl_id: "ENSG00000170903"
name: "Myb/SANT DNA binding domain containing 4 with coiled-coils"
location: "11q22.3"
module: 16
arm: "+"
pooled_cpm: 19.88
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MSANTD4

*Myb/SANT DNA binding domain containing 4 with coiled-coils* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.23× (z +18.1, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.700× (z -8.0, q 5e-13, down in 26 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.705× (z -7.9, q 8e-13, down in 25 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.233×, NCI-H460 0.301×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.366×, NCI-H2030 0.165×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.298×, PANC-1 0.458×; ⚠ cell-cycle shift, explains ~4% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0932×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (COLO 205 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBLL1]] (+0.70, fdr 8e-06), [[KLHL9]] (+0.68, fdr 7e-06), [[ZBTB6]] (+0.68, fdr 7e-06); moves opposite to [[DNM2]] (-0.56, fdr 1e-05), [[PPP1R13B]] (-0.55, fdr 1e-04), [[CD81]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZSCAN12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +18.1 | 0e+00 | 39/45 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +13.9 | 2e-41 | 39/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +12.3 | 3e-32 | 37/46 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +11.2 | 3e-27 | 34/46 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +11.0 | 5e-26 | 30/46 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +10.2 | 1e-22 | 29/46 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +9.8 | 7e-21 | 31/46 (PANC-1, A-427, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +9.7 | 2e-20 | 31/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +9.6 | 6e-20 | 28/46 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +9.0 | 2e-17 | 31/46 (SNU-423, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +8.9 | 2e-17 | 26/45 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +8.4 | 3e-15 | 24/45 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +8.2 | 8e-15 | 29/46 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +7.7 | 8e-13 | 27/45 (NCI-H23, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +7.2 | 3e-11 | 18/46 (A549, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10022.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.233×, NCI-H460 0.301×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.366×, NCI-H2030 0.165×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.298×, PANC-1 0.458×; ⚠ cell-cycle shift, explains ~4% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0932×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (COLO 205 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -8.0 | 5e-13 | 26/45 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -7.9 | 8e-13 | 25/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.694×** | -4.3 | 0.003 | 15/45 (HepG2/C3A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.853× | -3.5 | 0.075 | 3/46 (NCI-H2030, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.860× | -3.4 | 0.075 | 14/45 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.867× | -3.2 | 0.12 | 16/45 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.17 | 11/45 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.3 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.18× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.298× (z -10.9) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -10.9) |
| [[SW480 (line)]] | alt | 41.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.61× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.110× (z -9.3) |
| [[H4 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0938× (z -9.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0932× (z -10.9) |
| [[SW48 (line)]] | wt | 13.9 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0761× (z -8.7) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLL1]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[KLHL9]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ZSCAN12]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ZSCAN20]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | same gene group |
| [[FANCF]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ZNF613]] | +0.65 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[ZNF284]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ZNF317]] | +0.64 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[REXO4]] | +0.64 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[MSL3P1]] | +0.63 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[RPF1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNM2]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PPP1R13B]] | -0.55 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[CD81]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN12 activity raises MSANTD4's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without ZSCAN12 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[SOGA3]] | B | SOGA3 activity raises MSANTD4's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without SOGA3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.4, 10.2); signed map (0.5, -27.3). **Vector** length 78.1, 14.2% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +13.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +18.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +12.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +9.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -3.0 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Myb/SANT DNA binding domain containing 4 with coiled-coils |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:105,995,623-106,022,403 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1826 |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

UniProt [Q8NCY6](https://www.uniprot.org/uniprotkb/Q8NCY6) carries no function annotation.

**Summary**, from NCBI Gene [84437](https://www.ncbi.nlm.nih.gov/gene/84437):

> Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29383) · Entrez [84437](https://www.ncbi.nlm.nih.gov/gene/84437) · UniProt [Q8NCY6](https://www.uniprot.org/uniprotkb/Q8NCY6) · Ensembl [ENSG00000170903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170903)

## Data

Gene col 10022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10022); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10022]; `tensor/DDL_lfc|DDL_z.npy` [10022]; `embed/gene_vectors.npy` [10022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10022 or target_col == 10022). Every well: [[MSANTD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSANTD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
