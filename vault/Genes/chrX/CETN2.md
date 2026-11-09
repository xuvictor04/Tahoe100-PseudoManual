---
symbol: "CETN2"
type: "gene"
col: 7177
ensembl_id: "ENSG00000147400"
name: "centrin 2"
location: "Xq28"
module: 3
arm: "+"
pooled_cpm: 19.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CETN2

*centrin 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.90× (z +13.9, q 5e-41, up in 28 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.65× (z +4.5, q 5e-04, up in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (PANC-1 5.57×, SW480 6.79×, A498 5.61×, LOX-IMVI 10.7×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HOP62 6.97×, PANC-1 5.46×, A549 8.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 6.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.680× (z -4.4, q 0.006, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC1]] (+0.62, fdr 2e-04), [[PDZD11]] (+0.60, fdr 6e-05), [[NOMO1]] (+0.59, fdr 6e-04); moves opposite to [[SHROOM1]] (-0.61, fdr 2e-04), [[PM20D2]] (-0.61, fdr 1e-04), [[ZNF286B]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7177.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (PANC-1 5.57×, SW480 6.79×, A498 5.61×, LOX-IMVI 10.7×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HOP62 6.97×, PANC-1 5.46×, A549 8.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 6.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.90×** | +13.9 | 5e-41 | 28/29 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **5.01×** | +12.1 | 3e-31 | 37/37 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.19×** | +10.5 | 1e-23 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.13×** | +10.4 | 6e-23 | 48/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.89×** | +9.6 | 6e-20 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.08×** | +9.4 | 3e-19 | 30/33 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 5e-04 | 32/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +4.1 | 0.003 | 24/46 (A-427, NCI-H2347, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.55×** | +4.0 | 0.005 | 22/44 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.48×** | +3.4 | 0.033 | 21/40 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.32×** | +3.3 | 0.048 | 13/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.41× | +3.0 | 0.11 | 21/48 (A-172, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.680×** | -4.4 | 0.006 | 27/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.631×** | -4.2 | 0.009 | 29/48 (MIA PaCa-2, A498, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.713×** | -3.8 | 0.023 | 24/47 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.659×** | -3.8 | 0.024 | 24/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.485×** | -3.4 | 0.070 | 23/46 (A-427, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.506× | -3.2 | 0.12 | 12/48 (Panc 03.27, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | 0.700× | -3.1 | 0.15 | 20/47 (CHP-212, AN3 CA, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.712× | -3.1 | 0.15 | 17/46 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.5 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 13.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 27.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.11× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 35.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.61× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.51× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.96× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.89× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.44× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.7× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 11 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC1]] | +0.62 | +0.65 / +0.29 | both halves | 2e-04 |  |
| [[PDZD11]] | +0.60 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[NOMO1]] | +0.59 | +0.50 / +0.22 | both halves | 6e-04 |  |
| [[YIF1B]] | +0.59 | +0.56 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[SLC25A1]] | +0.59 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ARL3]] | +0.59 | +0.43 / +0.35 | both halves | 1e-04 | pathway: Assembly of the 9+0 primary cilium |
| [[ERP44]] | +0.59 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[GLG1]] | +0.58 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ALDH6A1]] | +0.58 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[MOSPD3]] | +0.58 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[GNAI2]] | +0.58 | +0.39 / +0.26 | both halves | 4e-04 |  |
| [[DCTN3]] | +0.58 | +0.27 / +0.57 | both halves | 3e-04 | pathway: AURKA Activation by TPX2 |
| [[AP2S1]] | +0.57 | +0.46 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHROOM1]] | -0.61 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[PM20D2]] | -0.61 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ZNF286B]] | -0.59 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ANKRD18A]] | -0.59 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[SNHG26]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[KCNMB3]] | -0.54 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[GCFC2]] | -0.53 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[TG]] | -0.53 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[FAXC]] | -0.53 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[NCR3LG1]] | -0.53 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[KICS2]] | -0.53 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[WNT3]] | -0.52 | -0.38 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[RCC1]] | -0.52 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CETN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BTG3]] | C | BTG3 activity raises CETN2's level | lines that do not express BTG3 (4) vs lines expressing it (46) | 1.17× lower at baseline in the lines without BTG3 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WTIP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.371). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.1, -22.8); signed map (-38.1, 12.8). **Vector** length 69.3, 16.6% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.7 | +10.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.6 | +10.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.6 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | centrin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:152,826,994-152,830,757 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEN2; previously CALT |
| Gene groups (HGNC) | EF-hand domain containing; Nucleotide excision repair; Transcription and export complex 2; Centriolar satellite proteins |
| Hallmark sets | DNA_REPAIR |
| Reactome | 25 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of Incision Complex in GG-NER; Loss of Nlp from mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [P41208](https://www.uniprot.org/uniprotkb/P41208) (Centrin-2):

> Plays a fundamental role in microtubule organizing center structure and function. Required for centriole duplication and correct spindle formation. Has a role in regulating cytokinesis and genome stability via cooperation with CALM1 and CCP110.; Involved in global genome nucleotide excision repair (GG-NER) by acting as component of the XPC complex. Cooperatively with RAD23B appears to stabilize XPC. In vitro, stimulates DNA binding of the XPC:RAD23B dimer.; The XPC complex is proposed to …

**Summary**, from NCBI Gene [1069](https://www.ncbi.nlm.nih.gov/gene/1069):

> Caltractin belongs to a family of calcium-binding proteins and is a structural component of the centrosome. The high level of conservation from algae to humans and its association with the centrosome suggested that caltractin plays a fundamental role in the structure and function of the microtubule-organizing center, possibly required for the proper duplication and segregation of the centrosome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1867) · Entrez [1069](https://www.ncbi.nlm.nih.gov/gene/1069) · UniProt [P41208](https://www.uniprot.org/uniprotkb/P41208) · Ensembl [ENSG00000147400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147400)

## Data

Gene col 7177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7177); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7177]; `tensor/DDL_lfc|DDL_z.npy` [7177]; `embed/gene_vectors.npy` [7177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7177 or target_col == 7177). Every well: [[CETN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CETN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
