---
symbol: "FOSB"
type: "gene"
col: 4653
ensembl_id: "ENSG00000125740"
name: "FosB proto-oncogene, AP-1 transcription factor subunit"
location: "19q13.32"
module: 109
arm: "+"
pooled_cpm: 64.57
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# FOSB

*FosB proto-oncogene, AP-1 transcription factor subunit* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.54× (z +12.5, q 2e-33, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +5.9, q 9e-07, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.301× (z -5.1, q 2e-04, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOS]] (+0.89, fdr 7e-06), [[FAM222A]] (+0.78, fdr 7e-06), [[CFAP210]] (+0.70, fdr 7e-06); moves opposite to [[NDUFAF5]] (-0.61, fdr 8e-06), [[PSMF1]] (-0.60, fdr 1e-05), [[C8orf76]] (-0.57, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **7.54×** | +12.5 | 2e-33 | 44/46 (NCI-H460, SK-MEL-2, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +5.9 | 9e-07 | 40/48 (BT-474, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **3.67×** | +5.5 | 8e-06 | 42/47 (NCI-H460, SK-MEL-2, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **2.84×** | +4.6 | 6e-04 | 35/47 (NCI-H460, H4, …) | two highest doses | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.56×** | +4.1 | 0.004 | 38/47 (NCI-H460, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **2.32×** | +3.7 | 0.021 | 31/47 (NCI-H460, AsPC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.33×** | +3.6 | 0.024 | 36/47 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **2.33×** | +3.6 | 0.024 | 41/48 (NCI-H2030, SW 900, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **2.18×** | +3.3 | 0.065 | 36/47 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 2.00× | +3.0 | 0.14 | 26/46 (NCI-H460, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.301×** | -5.1 | 2e-04 | 41/47 (SW48, SHP-77, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.310×** | -5.0 | 2e-04 | 38/46 (HS-578T, SHP-77, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.366×** | -4.4 | 0.002 | 40/47 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.346×** | -4.3 | 0.002 | 42/47 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.500×** | -4.3 | 0.002 | 36/48 (NCI-H1573, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.489×** | -4.3 | 0.002 | 41/47 (NCI-H23, C32, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.420×** | -3.8 | 0.010 | 34/46 (NCI-H1792, C32, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.425×** | -3.8 | 0.010 | 38/47 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.383×** | -3.7 | 0.010 | 40/49 (NCI-H23, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.428×** | -3.7 | 0.010 | 38/48 (COLO 205, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Carbamazepine (drug)]] 0.5 µM |  | **0.429×** | -3.7 | 0.010 | 39/47 (RPMI-7951, NCI-H661, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.443×** | -3.6 | 0.016 | 41/47 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.582×** | -3.4 | 0.033 | 28/47 (KATO III, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.473×** | -3.3 | 0.040 | 34/48 (BT-474, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.482×** | -3.2 | 0.049 | 34/47 (KATO III, SW 900, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | **0.508×** | -3.0 | 0.096 | 33/48 (NCI-H2030, COLO 205, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.86 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.9 | 11 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +19.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +19.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 46.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +11.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 72.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +11.4) ⚠ cell-cycle shift, explains ~34% of this change | [[Cobimetinib (drug)]] 5 µM 0.112× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 85.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 77.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +10.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 68.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 37.5× (z +13.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +15.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 182 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +14.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 74.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +11.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 78.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[J82 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +15.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 71.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +10.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 45.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +14.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 48.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +10.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +10.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[RPMI-7951 (line)]] | alt | 96.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +11.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 32.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +15.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 84.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +9.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW48 (line)]] | wt | 58.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +12.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 8.55 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOS]] | +0.89 | +0.92 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[FAM222A]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CFAP210]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PRKCG]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KIF9]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TEX14]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SEMA4A]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[KLHL15]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[HES1]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IQCN]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[EGR1]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 987 |
| [[TENT5C]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF5]] | -0.61 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[PSMF1]] | -0.60 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.57 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[TRIP4]] | -0.57 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | -0.57 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ABHD13]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[VPS33B]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SNX4]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[MBD2]] | -0.53 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[RBM45]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[EXO5-DT]] | -0.53 | -0.57 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGR2]] | B | EGR2 activity raises FOSB's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without EGR2 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises FOSB's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.47× lower at baseline in the lines without SEMA4A | 0.098 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.7, -27.7); signed map (2.9, 17.9). **Vector** length 159, 61.7% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Methylthiouracil (drug)]] 5 µM |  | +4.5 | +2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[Artemether (drug)]] 0.05 µM |  | +4.2 | +2.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +4.1 | +3.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -8.3 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.6 | -1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -6.5 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.4 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.3 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | FosB proto-oncogene, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,467,995-45,475,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G0S3, GOSB, GOS3, AP-1, MGC42291, DKFZp686C0818 |
| Gene groups (HGNC) | Fos transcription factor family |
| Hallmark sets | UV_RESPONSE_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 16 pathways, smallest: NGF-stimulated transcription; Regulation of PD-L1(CD274) transcription; Nuclear Events (kinase and transcription factor activation) |
| Matched by | ensembl_id |

**Function**, from UniProt [P53539](https://www.uniprot.org/uniprotkb/P53539) (Protein FosB):

> Heterodimerizes with proteins of the JUN family to form an AP-1 transcription factor complex, thereby enhancing their DNA binding activity to gene promoters containing an AP-1 consensus sequence 5'-TGA[GC]TCA-3' and enhancing their transcriptional activity. As part of the AP-1 complex, facilitates enhancer selection together with cell-type-specific transcription factors by collaboratively binding to nucleosomal enhancers and recruiting the SWI/SNF (BAF) chromatin remodeling complex to establish …

**Summary**, from NCBI Gene [2354](https://www.ncbi.nlm.nih.gov/gene/2354):

> The Fos gene family consists of 4 members: FOS, FOSB, FOSL1, and FOSL2. These genes encode leucine zipper proteins that can dimerize with proteins of the JUN family, thereby forming the transcription factor complex AP-1. As such, the FOS proteins have been implicated as regulators of cell proliferation, differentiation, and transformation. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3797) · Entrez [2354](https://www.ncbi.nlm.nih.gov/gene/2354) · UniProt [P53539](https://www.uniprot.org/uniprotkb/P53539) · Ensembl [ENSG00000125740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125740)

## Data

Gene col 4653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4653); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4653]; `tensor/DDL_lfc|DDL_z.npy` [4653]; `embed/gene_vectors.npy` [4653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4653 or target_col == 4653). Every well: [[FOSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
