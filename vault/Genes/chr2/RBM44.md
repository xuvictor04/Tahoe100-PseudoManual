---
symbol: "RBM44"
type: "gene"
col: 10827
ensembl_id: "ENSG00000177483"
name: "RNA binding motif protein 44"
location: "2q37.3"
module: 37
arm: "+"
pooled_cpm: 7.72
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# RBM44

*RNA binding motif protein 44* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +5.7, q 5e-06, up in 22 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.382× (z -14.9, q 0e+00, down in 34 of 40 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.274× (z -13.6, q 7e-40, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GET1-SH3BGR]] (+0.68, fdr 7e-06), [[SLC22A13]] (+0.61, fdr 7e-06), [[CCDC168]] (+0.61, fdr 1e-05); moves opposite to [[ZNF214]] (-0.59, fdr 1e-05), [[NFYC]] (-0.56, fdr 1e-05), [[ZNF282]] (-0.55, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ANKFN1]] → it (grade B ⚠); 8 go from it, the strongest it → [[LYG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.7 | 5e-06 | 22/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 1e-04 | 17/41 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.31×** | +4.5 | 0.001 | 11/36 (LS 180, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +4.5 | 0.001 | 13/40 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.23×** | +4.4 | 0.002 | 12/41 (LS 180, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.2 | 0.002 | 5/45 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.2 | 0.002 | 1/14 (NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.6 | 0.023 | 10/45 (PANC-1, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.88×** | +3.4 | 0.039 | 6/44 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.088 | 11/43 (A-172, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 5 µM |  | 1.22× | +3.0 | 0.12 | 4/45 (RPMI-7951, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.382×** | -14.9 | 0e+00 | 34/40 (HS-578T, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.274×** | -13.6 | 7e-40 | 35/42 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.447×** | -8.8 | 2e-16 | 27/45 (RPMI-7951, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.464×** | -8.4 | 5e-15 | 29/44 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.467×** | -8.3 | 8e-15 | 26/42 (H4, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.538×** | -6.8 | 1e-09 | 18/42 (A549, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.549×** | -6.6 | 4e-09 | 19/42 (AsPC-1, BT-474, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.316×** | -6.2 | 3e-08 | 24/41 (RPMI-7951, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.573×** | -6.1 | 7e-08 | 20/40 (HS-578T, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.578×** | -6.0 | 1e-07 | 20/37 (A549, HEC-1-A, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.339×** | -5.8 | 3e-07 | 21/34 (LOX-IMVI, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -5.3 | 7e-06 | 19/30 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.722×** | -5.0 | 2e-05 | 12/43 (LS 180, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.643×** | -4.8 | 5e-05 | 17/36 (HS-578T, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.626×** | -4.7 | 8e-05 | 16/38 (hTERT-HPNE, LS 180, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -4.5 | 3e-04 | 18/40 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.028 | 16/38 (J82, H4, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.028 | 13/43 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.640×** | -3.3 | 0.030 | 12/35 (KATO III, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.648×** | -3.2 | 0.039 | 7/31 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.059 | 12/45 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Berberine (chloride hydrate) (drug)]] 0.05 µM |  | **0.759×** | -3.0 | 0.062 | 6/44 (CFPAC-1, C-33 A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.758×** | -2.9 | 0.083 | 10/41 (COLO 205, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0230× (z -15.1) |
| [[A549 (line)]] | wt | 9.80 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.133× (z -9.1) |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0714× (z -16.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.120× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 5.32 | 0 | 4 (2 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.0841× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 6.36 | 0 | 4 (2 ⚠) | — | [[Budesonide (drug)]] 0.5 µM 0.0714× (z -10.3) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 6.20 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Penfluridol (drug)]] 5 µM 0.0667× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0349× (z -15.6) |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0310× (z -15.4) |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0737× (z -11.2) |
| [[SW480 (line)]] | alt | 3.70 | 0 | 2 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0812× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 4.11 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0697× (z -9.0) |
| [[KATO III (line)]] | alt | 6.64 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0902× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -8.5) |
| [[LS 180 (line)]] | wt | 9.50 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0589× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 7.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.173× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GET1-SH3BGR]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SLC22A13]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CCDC168]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[BMP8A]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[WDR49]] | +0.59 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[LSP1P5-1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[GPRC5D-AS1]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PLAC1]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[IL20RB]] | +0.58 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TMED3]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LINC02036]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LINC02935]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF214]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[NFYC]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ZNF282]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SCAF8]] | -0.55 | -0.28 / -0.54 | both halves | 3e-04 | same gene group |
| [[RNF115]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LIPT1]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[REPIN1]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SIAH1]] | -0.53 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TGIF2]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SMAD1]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZFX]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MARK2]] | -0.52 | -0.36 / -0.52 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKFN1]] | B | ANKFN1 activity raises RBM44's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 1.97× lower at baseline in the lines without ANKFN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[LYG1]] | C | LYG1 activity raises RBM44's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without LYG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent; co-absent with the target |
| [[CYP2E1]], [[SCART1]] | C | CYP2E1, SCART1 activity raises RBM44's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 2.93× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[LINC02133]] | C | LINC02133 activity raises RBM44's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without LINC02133 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYG1]] | C | RBM44 activity raises LYG1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.79× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SCART1]] | C | RBM44 activity raises SCART1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[C9orf153]] | C | RBM44 activity raises C9orf153's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |
| [[PPP1R32]] | C | RBM44 activity raises PPP1R32's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |
| [[CYP2E1]] | C | RBM44 activity raises CYP2E1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without RBM44 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; co-absent with the target |
| [[DRC1]] | C | RBM44 activity raises DRC1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without RBM44 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent |
| [[CDRT4]] | C | RBM44 activity raises CDRT4's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 3.62× lower at baseline in the lines without RBM44 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |
| [[TPCN2]] | C | RBM44 activity raises TPCN2's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without RBM44 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -21.4); signed map (8.9, 7.3). **Vector** length 86.6, 17.3% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +4.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.7 | -14.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,798,389-237,842,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40411 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZP01](https://www.uniprot.org/uniprotkb/Q6ZP01) (RNA-binding protein 44):

> Component of intercellular bridges during meiosis. Intercellular bridges are evolutionarily conserved structures that connect differentiating germ cells. Not required for fertility (By similarity).

**Summary**, from NCBI Gene [375316](https://www.ncbi.nlm.nih.gov/gene/375316):

> Predicted to enable mRNA 3'-UTR binding activity and protein homodimerization activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be located in cytoplasm and intercellular bridge. Predicted to be part of catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24756) · Entrez [375316](https://www.ncbi.nlm.nih.gov/gene/375316) · UniProt [Q6ZP01](https://www.uniprot.org/uniprotkb/Q6ZP01) · Ensembl [ENSG00000177483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177483)

## Data

Gene col 10827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10827); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10827]; `tensor/DDL_lfc|DDL_z.npy` [10827]; `embed/gene_vectors.npy` [10827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10827 or target_col == 10827). Every well: [[RBM44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
