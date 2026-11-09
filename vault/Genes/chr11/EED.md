---
symbol: "EED"
type: "gene"
col: 1074
ensembl_id: "ENSG00000074266"
name: "embryonic ectoderm development"
location: "11q14.2"
module: 186
arm: "+"
pooled_cpm: 53.73
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# EED

*embryonic ectoderm development* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +7.4, q 7e-11, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +6.7, q 5e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.365× (z -16.5, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.707× (z -5.5, q 8e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE7A]] (+0.68, fdr 7e-06), [[FAM168A]] (+0.66, fdr 7e-06), [[APAF1]] (+0.63, fdr 7e-06); moves opposite to [[CCDC91]] (-0.59, fdr 1e-05), [[ATP9B]] (-0.59, fdr 1e-05), [[RNF123]] (-0.57, fdr 1e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +7.4 | 7e-11 | 31/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +6.7 | 5e-09 | 33/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +6.7 | 5e-09 | 34/49 (SW48, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.49×** | +6.2 | 7e-08 | 34/48 (SW48, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +6.1 | 1e-07 | 38/49 (PANC-1, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.9 | 1e-04 | 24/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.29×** | +4.1 | 0.003 | 22/48 (A549, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.30×** | +4.0 | 0.004 | 22/47 (A-172, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.9 | 0.006 | 19/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.006 | 23/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.019 | 23/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.027 | 0/49 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.24×** | +3.4 | 0.028 | 20/48 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.073 | 15/48 (A-427, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +3.1 | 0.078 | 11/48 (J82, KATO III, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.086 | 15/48 (A-427, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.365×** | -16.5 | 0e+00 | 46/49 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.369×** | -15.7 | 0e+00 | 38/42 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.707×** | -5.5 | 8e-06 | 31/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.707×** | -5.3 | 2e-05 | 24/45 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -4.5 | 8e-04 | 30/48 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.815×** | -3.4 | 0.070 | 14/48 (SW1417, SW 1271, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.818×** | -3.3 | 0.072 | 15/48 (A498, BT-474, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | **0.821×** | -3.3 | 0.077 | 21/48 (SNU-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.819×** | -3.2 | 0.098 | 19/47 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 47.0 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 44.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 58.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.354× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 63.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -18.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.153× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 89.8 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -14.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 65.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 34.9 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +14.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 73.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 66.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.160× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 61.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -13.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LOX-IMVI (line)]] | wt | 81.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 52.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 99.4 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0976× (z -10.8) |
| [[A498 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.7 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.358× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 58.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 93.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -15.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE7A]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[FAM168A]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[APAF1]] | +0.63 | +0.67 / +0.64 | both halves | 7e-06 | same gene group; pathway: Transcriptional Regulation by E2F6 |
| [[MED26]] | +0.63 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NDC1]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 | pathway: HCMV Early Events |
| [[NUP54]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 | pathway: HCMV Early Events |
| [[ALG9]] | +0.60 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[TIAL1]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[POLH]] | +0.57 | +0.35 / +0.67 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC91]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ATP9B]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RNF123]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression |
| [[JPX]] | -0.53 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SETX]] | -0.53 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TAF1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CHMP6]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 | pathway: HCMV Infection |
| [[ZNF354A]] | -0.53 | -0.56 / -0.40 | both halves | 5e-05 | pathway: Epigenetic regulation of gene expression |
| [[COMMD10]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZNF554]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 1, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens EED's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.68× as strongly (z diff +1.33); strongest at Idarubicin (hydrochloride) 5 µM: 1.23x vs 2.01x (z diff +4.8) | 0.018 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers EED's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[POLH]] | C | POLH's natural level strengthens EED's drug response | POLH's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.10; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.2, -18.0); signed map (-41.8, 15.8). **Vector** length 107, 28.3% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.7 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.5 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.3 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | +4.7 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -7.2 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -5.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | embryonic ectoderm development |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:86,201,212-86,278,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WAIT-1, HEED |
| Gene groups (HGNC) | WD repeat domain containing; Polycomb repressive complex 2; MicroRNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 35 pathways, smallest: Defective pyroptosis; PRC2 methylates histones and DNA; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75530](https://www.uniprot.org/uniprotkb/O75530) (Polycomb protein EED):

> Polycomb group (PcG) protein. Component of the PRC2/EED-EZH2 complex, which methylates 'Lys-9' and 'Lys-27' of histone H3, leading to transcriptional repression of the affected target gene. Also recognizes 'Lys-26' trimethylated histone H1 with the effect of inhibiting PRC2 complex methyltransferase activity on nucleosomal histone H3 'Lys-27', whereas H3 'Lys-27' recognition has the opposite effect, enabling the propagation of this repressive mark. The PRC2/EED-EZH2 complex may also serve as a …

**Summary**, from NCBI Gene [8726](https://www.ncbi.nlm.nih.gov/gene/8726):

> This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein interacts with enhancer of zeste 2, the cytoplasmic tail of integrin beta7, immunodeficiency virus type 1 (HIV-1) MA protein, and histone deacetylase proteins. This protein mediates repression of gene activity through histone deacetylation, and may act as …

**Accessions** — [HGNC:3188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3188) · Entrez [8726](https://www.ncbi.nlm.nih.gov/gene/8726) · UniProt [O75530](https://www.uniprot.org/uniprotkb/O75530) · Ensembl [ENSG00000074266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074266)

## Data

Gene col 1074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1074); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1074]; `tensor/DDL_lfc|DDL_z.npy` [1074]; `embed/gene_vectors.npy` [1074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1074 or target_col == 1074). Every well: [[EED — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EED.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
