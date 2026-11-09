---
symbol: "EAPP"
type: "gene"
col: 4983
ensembl_id: "ENSG00000129518"
name: "E2F associated phosphoprotein"
location: "14q13.1"
module: 187
arm: "+"
pooled_cpm: 47.68
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# EAPP

*E2F associated phosphoprotein* — 14q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +10.1, q 2e-21, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.323× (z -14.2, q 3e-43, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.411× (z -5.9, q 7e-07, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIR1]] (+0.83, fdr 7e-06), [[SYF2]] (+0.81, fdr 7e-06), [[BSDC1]] (+0.76, fdr 7e-06); moves opposite to [[TFDP1]] (-0.68, fdr 7e-06), [[VARS1]] (-0.66, fdr 1e-05), [[ARHGAP4]] (-0.64, fdr 8e-06).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +10.1 | 2e-21 | 44/48 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.20×** | +7.7 | 4e-12 | 44/49 (LoVo, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.52×** | +7.6 | 8e-12 | 37/48 (C32, LoVo, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +7.0 | 3e-10 | 43/48 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +6.8 | 1e-09 | 41/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +6.5 | 1e-08 | 39/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.67×** | +6.3 | 3e-08 | 41/48 (LoVo, NCI-H2347, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.0 | 4e-05 | 38/47 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +4.2 | 0.002 | 27/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.31×** | +3.5 | 0.030 | 22/47 (C32, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.323×** | -14.2 | 3e-43 | 48/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -7.8 | 1e-12 | 32/42 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.411×** | -5.9 | 7e-07 | 44/48 (CHP-212, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.412×** | -5.8 | 7e-07 | 42/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.433×** | -5.5 | 4e-06 | 41/48 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.435×** | -5.5 | 4e-06 | 41/48 (CHP-212, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.445×** | -5.3 | 8e-06 | 40/48 (NCI-H661, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.720×** | -3.6 | 0.022 | 28/48 (RKO, SW48, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -3.6 | 0.022 | 25/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.698×** | -3.5 | 0.024 | 26/48 (RPMI-7951, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.040 | 23/48 (Hs 766T, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 39.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.7× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -10.3) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 63.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.3) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.126× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 37.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -9.7) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 43.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +20.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 66.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -8.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 43.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.317× (z -9.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 62.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 61.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.344× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 51.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -10.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 65.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -10.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -16.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 60.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.343× (z -9.2) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -9.9) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.293× (z -10.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -9.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -11.9) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -9.1) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -9.1) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -8.9) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.234× (z -12.4) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -11.0) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.271× (z -12.6) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 215 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0662× (z -9.4) |
| [[RKO (line)]] | wt | 37.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.263× (z -9.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -11.6) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.378× (z -8.8) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | +0.83 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[SYF2]] | +0.81 | +0.72 / +0.86 | both halves | 7e-06 |  |
| [[BSDC1]] | +0.76 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.75 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[CDC37L1]] | +0.74 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[SLU7]] | +0.72 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.72 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[BRAP]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | +0.71 | +0.57 / +0.75 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CWC15]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[FRG1]] | +0.70 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[TTI2]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP1]] | -0.68 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[VARS1]] | -0.66 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[NUP188]] | -0.64 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[VMA21]] | -0.64 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[UBE2G2]] | -0.64 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[CS]] | -0.64 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[BOP1]] | -0.62 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.62 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ICMT]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.61 | -0.53 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA9]] | B | HOXA9 activity lowers EAPP's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.22× higher at baseline in the lines without HOXA9 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[HEIH]] | B | HEIH activity raises EAPP's level | lines that do not express HEIH (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without HEIH | 0.071 | ⚠ within organs, on part of the lines; also absent: HYI, LINC00847; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.900). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.6, -46.1); signed map (-13.6, 6.4). **Vector** length 130, 42.6% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.5 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.2 | -14.2 |
|  | [[EX229 (drug)]] 5 µM |  | -7.7 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.5 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.3 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.1 | -5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.2 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | E2F associated phosphoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1 — chr14:34,515,938-34,539,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BM036, FLJ20578; previously C14orf11 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q56P03](https://www.uniprot.org/uniprotkb/Q56P03) (E2F-associated phosphoprotein):

> May play an important role in the fine-tuning of both major E2F1 activities, the regulation of the cell-cycle and the induction of apoptosis. Promotes S-phase entry, and inhibits p14(ARP) expression.

**Summary**, from NCBI Gene [55837](https://www.ncbi.nlm.nih.gov/gene/55837):

> This gene encodes a phosphoprotein that interacts with several members of the E2F family of proteins. The protein localizes to the nucleus, and is present throughout the cell cycle except during mitosis. It functions to modulate E2F-regulated transcription and stimulate proliferation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:19312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19312) · Entrez [55837](https://www.ncbi.nlm.nih.gov/gene/55837) · UniProt [Q56P03](https://www.uniprot.org/uniprotkb/Q56P03) · Ensembl [ENSG00000129518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129518)

## Data

Gene col 4983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4983); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4983]; `tensor/DDL_lfc|DDL_z.npy` [4983]; `embed/gene_vectors.npy` [4983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4983 or target_col == 4983). Every well: [[EAPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EAPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
