---
symbol: "JUP"
type: "gene"
col: 10427
ensembl_id: "ENSG00000173801"
name: "junction plakoglobin"
location: "17q21.2"
module: 31
arm: "+"
pooled_cpm: 109.25
n_lines_expressing: 34
n_dd_up: 2
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 77
direction_downstream: 113
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# JUP

*junction plakoglobin* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +5.3, q 6e-05, up in 13 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 2.66×, A498 2.26×, A-172 1.96×; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.64×, NCI-H2030 2.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.55×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (PANC-1 3.03×); [[Tucidinostat (drug)]] 5 µM in 1 line (A498 2.05×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.424× (z -14.8, q 0e+00, down in 31 of 32 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.479× (z -12.7, q 2e-34, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FA2H]] (+0.75, fdr 7e-06), [[SEMA3B]] (+0.73, fdr 7e-06), [[HS3ST1]] (+0.70, fdr 7e-06); moves opposite to [[TAS2R14]] (-0.58, fdr 1e-05), [[ST3GAL3]] (-0.54, fdr 1e-05), [[ANAPC1]] (-0.53, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 77 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); 113 go from it, the strongest it → [[KLF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 2.66×, A498 2.26×, A-172 1.96×; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.64×, NCI-H2030 2.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.55×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (PANC-1 3.03×); [[Tucidinostat (drug)]] 5 µM in 1 line (A498 2.05×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.3 | 6e-05 | 13/32 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +4.2 | 0.007 | 13/33 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.21× | +3.4 | 0.11 | 9/31 (A-172, SW480, …) | rises with dose | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.21× | +3.3 | 0.11 | 6/31 (PANC-1, KATO III, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.21× | +3.3 | 0.11 | 9/32 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 1.20× | +3.2 | 0.14 | 10/32 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.20× | +3.1 | 0.14 | 9/31 (A-172, HCT15, …) | rises with dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 1.21× | +3.1 | 0.14 | 13/32 (NCI-H460, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.424×** | -14.8 | 0e+00 | 31/32 (A498, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.479×** | -12.7 | 2e-34 | 25/31 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -12.5 | 1e-33 | 23/31 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.526×** | -11.1 | 2e-26 | 23/32 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -9.0 | 3e-17 | 23/32 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -8.4 | 3e-15 | 25/32 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -8.0 | 1e-13 | 24/32 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -7.4 | 8e-12 | 18/31 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.452×** | -7.2 | 5e-11 | 26/32 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.483×** | -6.6 | 3e-09 | 26/32 (NCI-H2030, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -6.1 | 7e-08 | 15/32 (CFPAC-1, A498, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.704×** | -5.8 | 3e-07 | 18/31 (CFPAC-1, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.532×** | -5.7 | 6e-07 | 19/33 (CFPAC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.792×** | -5.7 | 6e-07 | 18/33 (CFPAC-1, HT-29, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.554×** | -5.3 | 4e-06 | 21/31 (NCI-H2030, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.554×** | -5.3 | 4e-06 | 23/31 (A498, A549, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -5.1 | 1e-05 | 16/32 (LoVo, A498, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -4.9 | 3e-05 | 17/31 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[EX229 (drug)]] 5 µM |  | **0.589×** | -4.8 | 5e-05 | 21/32 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 495 | 0 | 18 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -19.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -14.5) |
| [[LoVo (line)]] | wt | 154 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 307 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -11.5) |
| [[PANC-1 (line)]] | alt | 27.8 | 5 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.03× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -9.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 42.1 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.05× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.204× (z -14.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 239 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 149 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -15.6) |
| [[SW 900 (line)]] | alt | 66.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.5) |
| [[A-172 (line)]] | wt | 67.6 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 0.5 µM 0.362× (z -9.4) |
| [[BT-474 (line)]] | alt | 160 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.599× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 123 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -11.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 278 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.4) |
| [[SW480 (line)]] | alt | 95.1 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.387× (z -10.5) |
| [[Hs 766T (line)]] | wt | 57.4 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -9.3) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 335 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.3) |
| [[A549 (line)]] | wt | 43.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.0) ⚠ cell-cycle shift, explains ~27% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -8.9) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 141 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.405× (z -11.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -8.5) |
| [[LS 180 (line)]] | wt | 203 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 34.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.2) |
| [[SW1417 (line)]] | alt | 266 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 131 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.9) |
| [[A-427 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0775× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[COLO 205 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 319 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 76.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -13.9) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0699× (z -9.4) |
| [[SHP-77 (line)]] | alt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.9) |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.81 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FA2H]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SEMA3B]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[HS3ST1]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CDH1]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 999 |
| [[CRYBG2]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.69 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[PCDH1]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[RDH13]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[LIPH]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[RNF39]] | +0.66 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[CLDN4]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R14]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ST3GAL3]] | -0.54 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ANAPC1]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[AFG1L]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 48, C 29. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises JUP's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 7.31× lower at baseline in the lines without TMPRSS4 | 5e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ADGRF1]] | B | ADGRF1 activity raises JUP's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.51× lower at baseline in the lines without ADGRF1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[MAL2]] | B | MAL2 activity raises JUP's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 5.50× lower at baseline in the lines without MAL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[NECTIN4]] | B | NECTIN4 activity raises JUP's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 4.75× lower at baseline in the lines without NECTIN4 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[B3GNT3]] | B | B3GNT3 activity raises JUP's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.98× lower at baseline in the lines without B3GNT3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[BICDL2]] | B | BICDL2 activity raises JUP's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.25× lower at baseline in the lines without BICDL2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[KLK10]] | B | KLK10 activity raises JUP's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 6.12× lower at baseline in the lines without KLK10 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[KIAA0040]] | B | KIAA0040 activity raises JUP's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 4.44× lower at baseline in the lines without KIAA0040 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[CLIC5]] | B | CLIC5 activity raises JUP's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.89× lower at baseline in the lines without CLIC5 | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[GALNT3]] | B | GALNT3 activity raises JUP's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 5.31× lower at baseline in the lines without GALNT3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[CRYBG2]] | B | CRYBG2 activity raises JUP's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 4.33× lower at baseline in the lines without CRYBG2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[TINAGL1]] | B | TINAGL1 activity raises JUP's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 4.10× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |

### Downstream of this gene

*113 arrows, 113 of them with an alert ⚠; grade A 0, B 84, C 29. Shown: the 12 strongest; 101 more arrows (101 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | B | JUP activity raises KLF5's level | lines that do not express JUP (16) vs lines expressing it (34) | 4.07× lower at baseline in the lines without JUP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[GAREM1]] | B | JUP activity raises GAREM1's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.09× lower at baseline in the lines without JUP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[TUFT1]] | B | JUP activity raises TUFT1's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without JUP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ST3GAL3]] | B | JUP activity lowers ST3GAL3's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.20× higher at baseline in the lines without JUP | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[GPRC5A]] | B | JUP activity strengthens GPRC5A's drug response | lines that do not express JUP (9) vs lines expressing it (28) | the lines without JUP respond 0.54× as strongly (z diff +3.68); strongest at Panobinostat 5 µM: 0.88x vs 0.35x (z diff +5.7) | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671; target measured in part of the lines; artifact flags |
| [[KIAA1522]] | B | JUP activity raises KIAA1522's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.03× lower at baseline in the lines without JUP | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[CCDC120]] | B | JUP activity raises CCDC120's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without JUP | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[PTK2B]] | B | JUP activity raises PTK2B's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.94× lower at baseline in the lines without JUP | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[EPS8L1]] | B | JUP activity raises EPS8L1's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without JUP | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[KIAA0040]] | B | JUP activity raises KIAA0040's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.83× lower at baseline in the lines without JUP | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[PARD6B]] | B | JUP activity raises PARD6B's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without JUP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[DLG3]] | B | JUP activity raises DLG3's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.95× lower at baseline in the lines without JUP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, 56.2); signed map (-1.3, 37.3). **Vector** length 123, 38.8% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.2 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.1 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.6 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -14.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -7.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -4.2 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | junction plakoglobin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,754,604-41,786,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DP3, PDGB, PKGB, DPIII, PG; previously CTNNG |
| Gene groups (HGNC) | Armadillo repeat containing; Beta catenins |
| Hallmark sets | XENOBIOTIC_METABOLISM, KRAS_SIGNALING_UP, APICAL_JUNCTION |
| Reactome | 35 pathways, smallest: CDH11 homotypic and heterotypic interactions; Regulation of CDH19 Expression and Function; Regulation of CDH11 function |
| Matched by | ensembl_id |

**Function**, from UniProt [P14923](https://www.uniprot.org/uniprotkb/P14923) (Junction plakoglobin):

> Common junctional plaque protein. The membrane-associated plaques are architectural elements in an important strategic position to influence the arrangement and function of both the cytoskeleton and the cells within the tissue. The presence of plakoglobin in both the desmosomes and in the intermediate junctions suggests that it plays a central role in the structure and function of submembranous plaques. Acts as a substrate for VE-PTP and is required by it to stimulate VE-cadherin function in …

**Summary**, from NCBI Gene [3728](https://www.ncbi.nlm.nih.gov/gene/3728):

> This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associated with Naxos disease. Alternative splicing occurs in this gene; however, not all transcripts have …

**Accessions** — [HGNC:6207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6207) · Entrez [3728](https://www.ncbi.nlm.nih.gov/gene/3728) · UniProt [P14923](https://www.uniprot.org/uniprotkb/P14923) · Ensembl [ENSG00000173801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173801)

## Data

Gene col 10427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10427); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10427]; `tensor/DDL_lfc|DDL_z.npy` [10427]; `embed/gene_vectors.npy` [10427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10427 or target_col == 10427). Every well: [[JUP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JUP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
