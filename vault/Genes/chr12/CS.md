---
symbol: "CS"
type: "gene"
col: 711
ensembl_id: "ENSG00000062485"
name: "citrate synthase"
location: "12q13.3"
module: 50
arm: "+"
pooled_cpm: 61.49
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CS

*citrate synthase* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.35× (z +20.1, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.404×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO3]] (+0.74, fdr 1e-05), [[COLGALT1]] (+0.68, fdr 7e-06), [[TTLL12]] (+0.68, fdr 1e-05); moves opposite to [[TERF2IP]] (-0.68, fdr 1e-05), [[ARID4B]] (-0.67, fdr 1e-05), [[NDUFC1]] (-0.66, fdr 8e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.35×** | +20.1 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +19.1 | 0e+00 | 46/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +17.0 | 0e+00 | 48/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.93×** | +14.9 | 0e+00 | 34/43 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.79×** | +13.7 | 6e-41 | 42/49 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +9.1 | 6e-18 | 40/47 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +8.7 | 2e-16 | 41/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +8.6 | 4e-16 | 37/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +6.7 | 1e-09 | 23/48 (HEC-1-A, LoVo, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +6.4 | 7e-09 | 35/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +6.4 | 1e-08 | 27/48 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +6.2 | 3e-08 | 30/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.33×** | +6.1 | 4e-08 | 29/45 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.8 | 2e-07 | 25/48 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +5.6 | 6e-07 | 26/49 (SW1417, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +4.8 | 5e-05 | 23/48 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +4.6 | 1e-04 | 20/48 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 21/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.001 | 17/49 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.001 | 15/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.002 | 15/48 (LoVo, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.012 | 15/48 (LS 180, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.020 | 15/48 (KATO III, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.404×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.959× | -3.4 | 0.18 | 1/49 (H4) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.868× | -3.3 | 0.18 | 17/48 (C-33 A, COLO 205, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.3 | 0.18 | 17/48 (CHP-212, LS 180, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.18 | 9/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.876× | -3.2 | 0.18 | 6/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.19 | 9/48 (COLO 205, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 75.1 | 8 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +14.5) | — |
| [[KATO III (line)]] | alt | 35.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.33× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 68.9 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 53.1 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.27× (z +10.4) | — |
| [[A-427 (line)]] | wt | 78.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.9) | — |
| [[A549 (line)]] | wt | 58.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 35.2 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 69.7 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 37.6 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.03× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 49.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.95× (z +9.9) | — |
| [[SW480 (line)]] | alt | 106 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 42.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 57.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.35× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 54.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 64.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.67× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 80.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 63.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 45.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 74.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.99× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.52× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 40.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 79.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HEC-1-A (line)]] | alt | 61.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HepG2_C3A (line)]] | wt | 64.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 47.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +8.6) | — |
| [[J82 (line)]] | alt | 81.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 99.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO3]] | +0.74 | +0.56 / +0.70 | both halves | 1e-05 | pathway: Protein localization |
| [[COLGALT1]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[TTLL12]] | +0.68 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ICMT]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TUBB]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[MTHFD1]] | +0.66 | +0.63 / +0.72 | both halves | 7e-06 | STRING 421 |
| [[APMAP]] | +0.66 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.66 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[PDHA1]] | +0.66 | +0.43 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 832 |
| [[TRAF7]] | +0.65 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SKP2]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.68 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.67 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.66 | -0.58 / -0.61 | both halves | 8e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SPATC1]] | -0.66 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SLU7]] | -0.66 | -0.57 / -0.69 | both halves | 9e-06 |  |
| [[EIF3J-DT]] | -0.65 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[GPANK1]] | -0.64 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[TOPORS]] | -0.64 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[RSF1]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[EAPP]] | -0.64 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[BET1]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[GCC2]] | -0.62 | -0.59 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers CS's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without ZNF341-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[FBXO32]] | B | FBXO32 activity lowers CS's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.33× higher at baseline in the lines without FBXO32 | 0.078 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[TERF2IP]] | C | TERF2IP's natural level weakens CS's drug response | TERF2IP's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.03; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.3, -27.0); signed map (-27.5, -42.6). **Vector** length 96.8, 24.3% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +7.1 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +6.5 | +13.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +5.7 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +20.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.9 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | citrate synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,271,699-56,300,391 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Acyltransferases |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O75390](https://www.uniprot.org/uniprotkb/O75390) (Citrate synthase, mitochondrial):

> Key enzyme of the Krebs tricarboxylic acid cycle which catalyzes the synthesis of citrate from acetyl coenzyme A and oxaloacetate.

**Summary**, from NCBI Gene [1431](https://www.ncbi.nlm.nih.gov/gene/1431):

> The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2422) · Entrez [1431](https://www.ncbi.nlm.nih.gov/gene/1431) · UniProt [O75390](https://www.uniprot.org/uniprotkb/O75390) · Ensembl [ENSG00000062485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062485)

## Data

Gene col 711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 711); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 711]; `tensor/DDL_lfc|DDL_z.npy` [711]; `embed/gene_vectors.npy` [711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 711 or target_col == 711). Every well: [[CS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
