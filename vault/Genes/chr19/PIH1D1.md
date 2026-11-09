---
symbol: "PIH1D1"
type: "gene"
col: 2512
ensembl_id: "ENSG00000104872"
name: "PIH1 domain containing 1"
location: "19q13.33"
module: 76
arm: "+"
pooled_cpm: 22.61
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# PIH1D1

*PIH1 domain containing 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.96× (z +9.8, q 9e-20, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.80× (z +4.6, q 6e-04, up in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 4.88×, SW480 2.75×, A549 3.49×, SW1417 3.20×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 3.77×, SHP-77 3.66×, Panc 03.27 4.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 3.16×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.471× (z -11.3, q 7e-27, down in 43 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.649× (z -9.2, q 1e-17, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARF1]] (+0.61, fdr 1e-05), [[KLHDC3]] (+0.59, fdr 7e-06), [[PAIP2]] (+0.58, fdr 3e-05); moves opposite to [[CDV3]] (-0.60, fdr 1e-05), [[KIF21A]] (-0.55, fdr 1e-05), [[CLIP1]] (-0.54, fdr 4e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 4.88×, SW480 2.75×, A549 3.49×, SW1417 3.20×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 3.77×, SHP-77 3.66×, Panc 03.27 4.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 3.16×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.8 | 9e-20 | 28/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.62×** | +7.3 | 9e-11 | 32/43 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +6.3 | 6e-08 | 29/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +4.6 | 6e-04 | 21/45 (RPMI-7951, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.27×** | +3.6 | 0.032 | 18/46 (KATO III, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.6 | 0.036 | 20/43 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.24×** | +3.3 | 0.093 | 17/45 (HT-29, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.49× | +3.2 | 0.11 | 12/45 (CFPAC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.49× | +3.1 | 0.11 | 16/48 (LoVo, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.471×** | -11.3 | 7e-27 | 43/47 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -9.2 | 1e-17 | 35/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.469×** | -6.0 | 4e-07 | 30/45 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -5.9 | 4e-07 | 28/47 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.505×** | -5.4 | 9e-06 | 24/46 (C-33 A, AN3 CA, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.548×** | -4.7 | 2e-04 | 22/45 (NCI-H2030, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.554×** | -4.6 | 3e-04 | 19/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.808×** | -4.1 | 0.003 | 19/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.0 | 0.003 | 2/48 (MIA PaCa-2, AN3 CA) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.768×** | -3.8 | 0.007 | 14/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.775×** | -3.8 | 0.007 | 18/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.712×** | -3.6 | 0.013 | 15/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.787×** | -3.6 | 0.014 | 16/48 (A-427, NCI-H23, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.644×** | -3.5 | 0.023 | 17/46 (H4, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.836× | -3.4 | 0.024 | 16/48 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.028 | 15/47 (NCI-H2030, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.064 | 10/48 (RKO, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.800×** | -3.0 | 0.072 | 13/47 (A-427, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 34.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -19.5) |
| [[HCT15 (line)]] | alt | 53.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -8.8) |
| [[LoVo (line)]] | wt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.8) |
| [[SW480 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.16× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.140× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -8.8) |
| [[SHP-77 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARF1]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PAIP2]] | +0.58 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[FAM117B]] | +0.56 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[BNIP3L]] | +0.55 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[BCKDHA]] | +0.54 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.53 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[FBXO25]] | +0.53 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[WIPI2]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ELK1]] | +0.53 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[UHRF2]] | +0.53 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDV3]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[KIF21A]] | -0.55 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[CLIP1]] | -0.54 | -0.66 / -0.43 | both halves | 4e-05 |  |
| [[DENND1B]] | -0.50 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[NUTM2B-AS1]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CPLANE1]] | -0.47 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[EML5]] | -0.46 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[CUEDC1]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SLC9A8]] | -0.44 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[HPS1]] | -0.44 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[MRPS16]] | -0.44 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[ANXA3]] | -0.44 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PIH1D1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, -23.2); signed map (-19.3, 9.9). **Vector** length 85.4, 18.5% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.5 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -11.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.2 | -6.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | PIH1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,446,298-49,453,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20643, Pih1, MOT48, DNAAF14; previously NOP17 |
| Gene groups (HGNC) | R2TP complex; Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWS0](https://www.uniprot.org/uniprotkb/Q9NWS0) (PIH1 domain-containing protein 1):

> Involved in the assembly of C/D box small nucleolar ribonucleoprotein (snoRNP) particles. Recruits the SWI/SNF complex to the core promoter of rRNA genes and enhances pre-rRNA transcription. Mediates interaction of TELO2 with the R2TP complex which is necessary for the stability of MTOR and SMG1. Positively regulates the assembly and activity of the mTORC1 complex.

**Summary**, from NCBI Gene [55011](https://www.ncbi.nlm.nih.gov/gene/55011):

> Enables several functions, including enzyme binding activity; histone binding activity; and phosphoprotein binding activity. Involved in several processes, including positive regulation of signal transduction; positive regulation of transcription of nucleolar large rRNA by RNA polymerase I; and protein-containing complex assembly. Located in cytoplasm and nucleolus. Part of R2TP complex and pre-snoRNP complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26075) · Entrez [55011](https://www.ncbi.nlm.nih.gov/gene/55011) · UniProt [Q9NWS0](https://www.uniprot.org/uniprotkb/Q9NWS0) · Ensembl [ENSG00000104872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104872)

## Data

Gene col 2512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2512); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2512]; `tensor/DDL_lfc|DDL_z.npy` [2512]; `embed/gene_vectors.npy` [2512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2512 or target_col == 2512). Every well: [[PIH1D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIH1D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
