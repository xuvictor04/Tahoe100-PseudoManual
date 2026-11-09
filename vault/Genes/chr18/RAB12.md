---
symbol: "RAB12"
type: "gene"
col: 13043
ensembl_id: "ENSG00000206418"
name: "RAB12, member RAS oncogene family"
location: "18p11.22"
module: 190
arm: "+"
pooled_cpm: 64.39
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# RAB12

*RAB12, member RAS oncogene family* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.57× (z +11.3, q 1e-26, up in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.26× (z +6.1, q 2e-07, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.934× (z -6.3, q 2e-07, down in 0 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.804× (z -5.7, q 3e-06, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 0.331×, SK-MEL-2 0.269×, NCI-H23 0.424×, AsPC-1 0.421×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A-427 0.366×, NCI-H1573 0.357×, PANC-1 0.458×, NCI-H460 0.566×; ⚠ cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.415×); [[Voriconazole (drug)]] 0.05 µM in 1 line (SW 1088 0.0695×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAPB]] (+0.63, fdr 7e-06), [[ATP5F1C]] (+0.60, fdr 1e-05), [[RNPEP]] (+0.60, fdr 1e-05); moves opposite to [[PPP1R10]] (-0.61, fdr 1e-05), [[EPC2]] (-0.60, fdr 1e-05), [[COQ7]] (-0.59, fdr 1e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +11.3 | 1e-26 | 40/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +6.8 | 2e-09 | 29/48 (HOP62, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +6.1 | 2e-07 | 25/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +5.8 | 7e-07 | 24/48 (LoVo, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +5.5 | 4e-06 | 17/48 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +5.2 | 2e-05 | 23/48 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +5.1 | 2e-05 | 17/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.22×** | +5.1 | 3e-05 | 22/43 (NCI-H23, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.21×** | +4.9 | 6e-05 | 24/48 (HOP62, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.20×** | +4.8 | 9e-05 | 17/48 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 1.18× | +4.3 | 9e-04 | 22/48 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~2% of this change | 1.15× | +3.6 | 0.014 | 15/47 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.6 | 0.015 | 15/45 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.037 | 7/49 (HOP62, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.1 | 0.076 | 5/48 (C32, LoVo, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.076 | 10/47 (LOX-IMVI, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.093 | 3/48 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13043.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 0.331×, SK-MEL-2 0.269×, NCI-H23 0.424×, AsPC-1 0.421×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A-427 0.366×, NCI-H1573 0.357×, PANC-1 0.458×, NCI-H460 0.566×; ⚠ cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.415×); [[Voriconazole (drug)]] 0.05 µM in 1 line (SW 1088 0.0695×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -6.3 | 2e-07 | 0/49 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.804×** | -5.7 | 3e-06 | 25/48 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.807×** | -5.6 | 4e-06 | 23/48 (A-427, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -5.5 | 7e-06 | 22/48 (NCI-H1573, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.831×** | -4.9 | 1e-04 | 19/48 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 0.851× | -4.2 | 0.002 | 18/48 (NCI-H460, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 87.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.415× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 90.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 66.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.80× (z +8.5) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.566× (z -8.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[PANC-1 (line)]] | alt | 62.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -11.3) ⚠ cell-cycle shift, explains ~8% of this change |
| [[A-427 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -13.9) ⚠ cell-cycle shift, explains ~8% of this change |
| [[AsPC-1 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 45.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.38× (z +9.0) ⚠ toxic; cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.08× (z +10.6) ⚠ toxic | — |
| [[RKO (line)]] | wt | 66.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW 1088 (line)]] | alt | 70.6 | 0 | 1 | — | [[Voriconazole (drug)]] 0.05 µM 0.0695× (z -9.3) |
| [[A-172 (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPB]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RNPEP]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DRAM2]] | +0.59 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CDS1]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PIKFYVE]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.58 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[RPA1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GTF2IP4]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[EPC2]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[COQ7]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ZNF830]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZNF274]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SP2]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[IBA57]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PDCL3P4]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HELQ]] | -0.56 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[PNRC2]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB38]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RAB12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.2, -9.9); signed map (-36.5, -12.7). **Vector** length 94.6, 20.4% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +11.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.0 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -6.5 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB12, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:8,609,437-8,639,383 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 5 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ22](https://www.uniprot.org/uniprotkb/Q6IQ22) (Ras-related protein Rab-12):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB12 may play a role in protein transport from recycling endosomes to lysosomes regulating, for …

**Summary**, from NCBI Gene [201475](https://www.ncbi.nlm.nih.gov/gene/201475):

> Enables GDP binding activity. Predicted to be involved in several processes, including endocytic recycling; endosome to lysosome transport; and positive regulation of macroautophagy. Predicted to act upstream of or within cellular response to type II interferon. Predicted to be located in lysosome; phagocytic vesicle; and recycling endosome membrane. Predicted to be active in cytoplasmic vesicle and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31332) · Entrez [201475](https://www.ncbi.nlm.nih.gov/gene/201475) · UniProt [Q6IQ22](https://www.uniprot.org/uniprotkb/Q6IQ22) · Ensembl [ENSG00000206418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206418)

## Data

Gene col 13043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13043); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13043]; `tensor/DDL_lfc|DDL_z.npy` [13043]; `embed/gene_vectors.npy` [13043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13043 or target_col == 13043). Every well: [[RAB12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
