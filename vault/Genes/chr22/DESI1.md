---
symbol: "DESI1"
type: "gene"
col: 1957
ensembl_id: "ENSG00000100418"
name: "desumoylating isopeptidase 1"
location: "22q13.2"
module: 45
arm: "-"
pooled_cpm: 20.71
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# DESI1

*desumoylating isopeptidase 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +20.9, q 0e+00, up in 40 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +16.9, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.489× (z -7.1, q 6e-10, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASEH1]] (+0.68, fdr 7e-06), [[LTO1]] (+0.64, fdr 1e-05), [[FBXO30]] (+0.63, fdr 1e-05); moves opposite to [[SUFU]] (-0.70, fdr 1e-05), [[KIAA2013]] (-0.66, fdr 7e-06), [[PLEKHH3]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +20.9 | 0e+00 | 40/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +20.8 | 0e+00 | 32/32 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +16.9 | 0e+00 | 37/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +16.3 | 0e+00 | 34/36 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +14.0 | 2e-42 | 37/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +12.6 | 1e-34 | 42/46 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +11.6 | 3e-29 | 37/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +9.2 | 2e-18 | 29/47 (A498, COLO 205, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.2 | 3e-18 | 35/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +8.5 | 8e-16 | 27/46 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +8.3 | 4e-15 | 26/47 (COLO 205, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.7 | 7e-13 | 29/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.49×** | +7.2 | 2e-11 | 25/43 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +7.1 | 4e-11 | 23/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.42×** | +6.6 | 2e-09 | 24/47 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.6 | 2e-09 | 26/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.6 | 8e-07 | 20/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 18/47 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 2e-05 | 16/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.002 | 12/45 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.002 | 10/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -7.1 | 6e-10 | 28/48 (RKO, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -6.9 | 1e-09 | 28/45 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.828×** | -5.1 | 6e-05 | 21/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -4.6 | 7e-04 | 19/48 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.655×** | -4.2 | 0.003 | 12/45 (A498, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.803×** | -4.2 | 0.003 | 12/48 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.815×** | -3.9 | 0.008 | 18/48 (A498, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.0 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 19.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.0) | — |
| [[A498 (line)]] | wt | 29.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +12.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 19.2 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.81× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 5.60× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 21.1 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +11.4) | — |
| [[LoVo (line)]] | wt | 27.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.40× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 17.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.05× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 1 | — | [[Methotrexate (drug)]] 0.5 µM 0.0730× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0978× (z -9.7) |
| [[Hs 766T (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0974× (z -10.2) |
| [[SW1417 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEH1]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[LTO1]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[FBXO30]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PSME3]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ELK4]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ABCF2]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SELENOI]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[TSTD2]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CCDC200]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[AVEN]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUFU]] | -0.70 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[KIAA2013]] | -0.66 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[PLEKHH3]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CFD]] | -0.64 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ORC4]] | -0.64 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MTF2]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.63 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[GUSBP18]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[THRA]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.60 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[MALSU1]] | -0.60 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[TNNI3]] | -0.60 | -0.40 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DESI1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.9, -8.5); signed map (19.9, -26.5). **Vector** length 97.0, 22.3% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +20.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +20.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +9.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +9.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.5 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.5 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | desumoylating isopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,598,028-41,621,043 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D15Wsu75e, DESI-1, POST; previously FAM152B, PPPDE2 |
| Gene groups (HGNC) | Desumoylating isopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ICB0](https://www.uniprot.org/uniprotkb/Q6ICB0) (Desumoylating isopeptidase 1):

> Protease which deconjugates SUMO1, SUMO2 and SUMO3 from some substrate proteins. Has isopeptidase but not SUMO-processing activity (By similarity). Desumoylates ZBTB46 (By similarity). Collaborates with UBQLN4 in the export of ubiquitinated proteins from the nucleus to the cytoplasm. Exhibits palmitoyl protein thioesterase (S-depalmitoylation) activity towards synthetic substrates 4-methylumbelliferyl-6-S-palmitoyl-beta-D-glucopyranoside and S-depalmitoylation probe 5 (DPP-5).

**Summary**, from NCBI Gene [27351](https://www.ncbi.nlm.nih.gov/gene/27351):

> Enables importin-alpha family protein binding activity and long-chain fatty acyl-CoA hydrolase activity. Involved in protein export from nucleus and regulation of proteasomal ubiquitin-dependent protein catabolic process. Located in cytosol. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24577) · Entrez [27351](https://www.ncbi.nlm.nih.gov/gene/27351) · UniProt [Q6ICB0](https://www.uniprot.org/uniprotkb/Q6ICB0) · Ensembl [ENSG00000100418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100418)

## Data

Gene col 1957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1957); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1957]; `tensor/DDL_lfc|DDL_z.npy` [1957]; `embed/gene_vectors.npy` [1957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1957 or target_col == 1957). Every well: [[DESI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DESI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
