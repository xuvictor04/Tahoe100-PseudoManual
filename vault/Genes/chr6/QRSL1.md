---
symbol: "QRSL1"
type: "gene"
col: 5057
ensembl_id: "ENSG00000130348"
name: "glutaminyl-tRNA amidotransferase subunit QRSL1"
location: "6q21"
module: 1
arm: "+"
pooled_cpm: 21.08
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# QRSL1

*glutaminyl-tRNA amidotransferase subunit QRSL1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.97× (z +13.5, q 1e-38, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.898× (z -7.8, q 4e-12, down in 4 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.779× (z -7.5, q 2e-11, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.209×, SW48 0.140×, SNU-1 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.192×, HepG2/C3A 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0816×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.225×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 900 0.0793×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF346]] (+0.71, fdr 1e-05), [[RCC1L]] (+0.70, fdr 1e-05), [[DHX35]] (+0.68, fdr 1e-05); moves opposite to [[BAIAP3]] (-0.65, fdr 1e-05), [[FSCN1]] (-0.61, fdr 1e-05), [[AHDC1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.97×** | +13.5 | 1e-38 | 41/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +11.7 | 2e-29 | 35/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +11.3 | 2e-27 | 36/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +9.2 | 3e-18 | 30/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.7 | 1e-12 | 32/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +7.7 | 2e-12 | 27/44 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +7.5 | 7e-12 | 25/47 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.3 | 2e-11 | 28/47 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.9 | 5e-10 | 21/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.7 | 1e-09 | 21/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.6 | 2e-09 | 27/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +6.2 | 2e-08 | 21/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +6.2 | 3e-08 | 19/47 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +5.5 | 1e-06 | 20/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +5.5 | 1e-06 | 22/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 3e-05 | 16/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 4e-04 | 13/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.5 | 0.011 | 8/48 (LS 180, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.011 | 9/48 (NCI-H1573, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.012 | 12/46 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.209×, SW48 0.140×, SNU-1 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.192×, HepG2/C3A 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0816×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.225×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 900 0.0793×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -7.8 | 4e-12 | 4/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -7.5 | 2e-11 | 32/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.805×** | -4.2 | 0.006 | 14/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.702×** | -3.9 | 0.013 | 19/46 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.836× | -3.8 | 0.017 | 11/47 (SW480, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.254× (z -9.4) |
| [[SNU-1 (line)]] | wt | 35.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[DT-061 (drug)]] 5 µM 0.0595× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 33.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0816× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 13.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.73× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.5) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.225× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SNU-423 (line)]] | alt | 25.6 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.12× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 9.05 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0793× (z -10.2) |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[A-172 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF346]] | +0.71 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[RCC1L]] | +0.70 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[DHX35]] | +0.68 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DHX30]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LARS2]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TRAPPC13]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[MRPS15]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.64 | +0.67 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP3]] | -0.65 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FSCN1]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SPAG9]] | -0.61 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PLEKHO2]] | -0.60 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ASMTL]] | -0.60 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[DNAAF3]] | -0.59 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[GNAI2]] | -0.59 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[PLXNA3]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SLC17A7]] | -0.58 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FCHO1]] | -0.58 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[GDPD5]] | -0.57 | -0.51 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers QRSL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SEMA3F]] | B | SEMA3F activity raises QRSL1's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without SEMA3F | 0.074 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[TP53]] | C | TP53 activity weakens QRSL1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.29× as strongly (z diff -0.71); strongest at Idarubicin (hydrochloride) 5 µM: 1.42x vs 1.01x (z diff -3.5) | 0.834 over the table, 0.063 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.8, 15.7); signed map (23.6, -23.9). **Vector** length 90.8, 18.6% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +13.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.7 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +6.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.0 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glutaminyl-tRNA amidotransferase subunit QRSL1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:106,629,578-106,668,417 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GatA, FLJ10989, FLJ12189, DKFZP564C1278, FLJ13447, GATA |
| Gene groups (HGNC) | Glutamyl-tRNA amidotransferase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0R6](https://www.uniprot.org/uniprotkb/Q9H0R6) (Glutamyl-tRNA(Gln) amidotransferase subunit A, mitochondrial):

> Catalytic subunit of the mitochondrial Glu-tRNA(Gln) amidotransferase complex GatCAB (Probable). GatCAB allows the formation of correctly charged Gln-tRNA(Gln) through the transamidation of misacylated Glu-tRNA(Gln) in the mitochondria. The reaction takes place in the presence of glutamine and ATP through an activated gamma-phospho-Glu-tRNA(Gln) (By similarity). This subunit probably catalyzes the hydrolysis of the amido donor Gln, releasing ammonia that is sequestered within a channel in the …

**Summary**, from NCBI Gene [55278](https://www.ncbi.nlm.nih.gov/gene/55278):

> Contributes to glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity. Involved in glutaminyl-tRNAGln biosynthesis via transamidation and mitochondrial translation. Located in mitochondrion. Part of glutamyl-tRNA(Gln) amidotransferase complex. Implicated in combined oxidative phosphorylation deficiency 40. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21020) · Entrez [55278](https://www.ncbi.nlm.nih.gov/gene/55278) · UniProt [Q9H0R6](https://www.uniprot.org/uniprotkb/Q9H0R6) · Ensembl [ENSG00000130348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130348)

## Data

Gene col 5057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5057); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5057]; `tensor/DDL_lfc|DDL_z.npy` [5057]; `embed/gene_vectors.npy` [5057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5057 or target_col == 5057). Every well: [[QRSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QRSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
