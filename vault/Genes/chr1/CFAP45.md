---
symbol: "CFAP45"
type: "gene"
col: 13081
ensembl_id: "ENSG00000213085"
name: "cilia and flagella associated protein 45"
location: "1q23.2"
module: 53
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 13
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CFAP45

*cilia and flagella associated protein 45* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +8.8, q 9e-16, up in 20 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.583× (z -5.8, q 4e-06, down in 21 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 0.0384×, NCI-H1792 0.0719×, HOP62 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.144×, C32 0.0897×, NCI-H1792 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 0.127×, C32 0.0861×, HOP62 0.189×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0959×); [[Lenalidomide (hemihydrate) (drug)]] 5 µM in 1 line (LS 180 0.179×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMZ1]] (+0.63, fdr 1e-05), [[SAMD14]] (+0.60, fdr 4e-05), [[LINC02036]] (+0.57, fdr 4e-05); moves opposite to [[VPS50]] (-0.52, fdr 8e-05), [[APOOL]] (-0.50, fdr 5e-05), [[TXNRD2]] (-0.46, fdr 9e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RCN3]] → it (grade B ⚠); 13 go from it, the strongest it → [[NDRG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +8.8 | 9e-16 | 20/37 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.78×** | +8.2 | 6e-14 | 18/38 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.55×** | +7.1 | 2e-10 | 24/36 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.0 | 4e-10 | 24/42 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +7.0 | 4e-10 | 19/37 (A-172, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +6.9 | 6e-10 | 18/31 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.55×** | +4.7 | 2e-04 | 12/32 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.001 | 16/40 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.001 | 12/41 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.48×** | +4.2 | 0.001 | 16/42 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.001 | 16/40 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.001 | 9/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.036 | 6/41 (NCI-H2030, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.057 | 6/41 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +3.1 | 0.064 | 14/41 (NCI-H1792, LoVo, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13081.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 0.0384×, NCI-H1792 0.0719×, HOP62 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.144×, C32 0.0897×, NCI-H1792 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 0.127×, C32 0.0861×, HOP62 0.189×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0959×); [[Lenalidomide (hemihydrate) (drug)]] 5 µM in 1 line (LS 180 0.179×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.583×** | -5.8 | 4e-06 | 21/41 (H4, LS 180, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.689×** | -4.0 | 0.017 | 17/24 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.704×** | -3.6 | 0.053 | 9/40 (C32, A498, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.741× | -3.2 | 0.17 | 11/42 (CHP-212, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 12.4 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +13.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0719× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 23.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.0897× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +11.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0926× (z -9.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A-172 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 3.89 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0384× (z -13.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 6.41 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 5 µM 0.179× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 3.43 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0959× (z -9.2) |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMZ1]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.60 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[LINC02036]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[CAPN12]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CELF5]] | +0.56 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[RASA4B]] | +0.55 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[SEMA3F]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[GNA15]] | +0.54 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PRKCG]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RARA]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[KCNN3]] | +0.52 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[SEMA4A]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS50]] | -0.52 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[APOOL]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[TXNRD2]] | -0.46 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[IPP]] | -0.46 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[MTX3]] | -0.46 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[QRSL1]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[POLR3F]] | -0.45 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[YTHDC2]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ARMCX5]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RCN3]] | B | RCN3 activity lowers CFAP45's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.70× higher at baseline in the lines without RCN3 | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | CFAP45 activity raises NDRG1's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 4.16× lower at baseline in the lines without CFAP45 | 0.007 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[RNF24]] | B | CFAP45 activity raises RNF24's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without CFAP45 | 0.035 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[PDE4A]] | B | CFAP45 activity lowers PDE4A's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 2.10× higher at baseline in the lines without CFAP45 | 0.044 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[ADCY10]] | B | CFAP45 activity raises ADCY10's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without CFAP45 | 0.050 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[SEMA4A]] | B | CFAP45 activity raises SEMA4A's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without CFAP45 | 0.051 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[SNAI1]] | B | CFAP45 activity lowers SNAI1's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without CFAP45 | 0.069 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | CFAP45 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express CFAP45 (6) vs lines expressing it (42) | the lines without CFAP45: 0.70× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[LINC02036]] | B | CFAP45 activity raises LINC02036's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without CFAP45 | 0.085 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[APC2]] | B | CFAP45 activity lowers APC2's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.78× higher at baseline in the lines without CFAP45 | 0.086 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[RARA]] | B | CFAP45 activity raises RARA's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without CFAP45 | 0.088 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | CFAP45 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CFAP45 (6) vs lines expressing it (42) | the lines without CFAP45: 1.32× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[MAPK8IP1]] | B | CFAP45 activity lowers MAPK8IP1's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.90× higher at baseline in the lines without CFAP45 | 0.092 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.5, -17.7); signed map (16.9, 17.6). **Vector** length 64.0, 10.8% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.9 | -0.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.9 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +7.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:159,872,364-159,900,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NESG1; previously CCDC19 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL16](https://www.uniprot.org/uniprotkb/Q9UL16) (Cilia- and flagella-associated protein 45):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. It is an AMP-binding protein that may facilitate dynein ATPase-dependent ciliary and flagellar beating via adenine nucleotide homeostasis. May function as a donor of AMP to AK8 and hence promote ADP production.

**Summary**, from NCBI Gene [25790](https://www.ncbi.nlm.nih.gov/gene/25790):

> Enables AMP binding activity. Involved in establishment of left/right asymmetry and flagellated sperm motility. Located in axonemal microtubule and sperm flagellum. Implicated in visceral heterotaxy 11. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17229) · Entrez [25790](https://www.ncbi.nlm.nih.gov/gene/25790) · UniProt [Q9UL16](https://www.uniprot.org/uniprotkb/Q9UL16) · Ensembl [ENSG00000213085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213085)

## Data

Gene col 13081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13081); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13081]; `tensor/DDL_lfc|DDL_z.npy` [13081]; `embed/gene_vectors.npy` [13081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13081 or target_col == 13081). Every well: [[CFAP45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
