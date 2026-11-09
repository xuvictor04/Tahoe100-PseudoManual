---
symbol: "APC"
type: "gene"
col: 5631
ensembl_id: "ENSG00000134982"
name: "APC regulator of Wnt signaling pathway"
location: "5q22.2"
module: 17
arm: "+"
pooled_cpm: 97.21
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 12
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# APC

*APC regulator of Wnt signaling pathway* — 5q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.20× (z +7.9, q 1e-12, up in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-172 2.78×, J82 2.20×, RKO 1.95×, NCI-H2347 1.70×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 2.54×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (J82 1.91×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.629× (z -20.2, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESD]] (+0.61, fdr 2e-05), [[HPF1]] (+0.61, fdr 1e-05), [[KBTBD6]] (+0.60, fdr 3e-05); moves opposite to [[KCNC3]] (-0.56, fdr 1e-05), [[RELT]] (-0.48, fdr 9e-05), [[CCDC200]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[CD109]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-172 2.78×, J82 2.20×, RKO 1.95×, NCI-H2347 1.70×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 2.54×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (J82 1.91×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.20×** | +7.9 | 1e-12 | 27/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +5.3 | 3e-05 | 17/48 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +5.0 | 1e-04 | 20/48 (A-172, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +4.4 | 0.001 | 15/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +4.0 | 0.007 | 6/48 (J82, H4, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.008 | 8/47 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.3 | 0.086 | 20/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.08× | +3.2 | 0.11 | 3/49 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -20.2 | 0e+00 | 40/49 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -18.1 | 0e+00 | 41/44 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.558×** | -18.0 | 0e+00 | 43/49 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.503×** | -17.3 | 0e+00 | 42/45 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -12.4 | 2e-33 | 38/48 (SW48, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.790×** | -7.0 | 3e-10 | 25/48 (SNU-423, RKO, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.817×** | -6.0 | 2e-07 | 24/50 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.829×** | -5.5 | 2e-06 | 24/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | 0.841× | -5.3 | 7e-06 | 23/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.848× | -5.1 | 2e-05 | 20/48 (RPMI-7951, HCT15, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.006 | 16/48 (SW480, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.847× | -3.6 | 0.013 | 13/48 (SW 1271, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.891× | -3.6 | 0.016 | 14/48 (C32, HT-29, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.072 | 8/48 (PANC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.932× | -3.1 | 0.085 | 2/48 (A-172, Hs 766T) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 89.2 | 0 | 18 (15 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.196× (z -28.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.5) |
| [[HOP62 (line)]] | alt | 74.1 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 162 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -14.2) |
| [[PANC-1 (line)]] | alt | 97.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -14.0) |
| [[SNU-423 (line)]] | alt | 76.6 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -14.8) |
| [[A-427 (line)]] | wt | 135 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -13.9) |
| [[SW48 (line)]] | wt | 160 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.243× (z -13.2) |
| [[A498 (line)]] | wt | 76.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.9) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 137 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -17.6) |
| [[SNU-1 (line)]] | wt | 85.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -9.2) |
| [[SW480 (line)]] | alt | 114 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.524× (z -12.4) |
| [[A-172 (line)]] | wt | 102 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 99.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -17.1) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0784× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.332× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 72.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.3) |
| [[CFPAC-1 (line)]] | alt | 84.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -12.9) |
| [[H4 (line)]] | wt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 99.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -27.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.8 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.332× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -14.4) |
| [[RKO (line)]] | wt | 114 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -15.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.1) |
| [[HT-29 (line)]] | alt | 83.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.480× (z -9.0) |
| [[J82 (line)]] | alt | 75.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 95.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.506× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 99.5 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.4) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H2347 (line)]] | alt | 96.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 123 | 0 | 2 | — | [[Decitabine (drug)]] 5 µM 0.101× (z -10.0) |
| [[C-33 A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 96.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0817× (z -24.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.444× (z -11.2) |
| [[HS-578T (line)]] | alt | 123 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 67.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 147 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.195× (z -9.8) |
| [[BT-474 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESD]] | +0.61 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[HPF1]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.60 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[CCDC43]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[METTL14]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NDUFS4]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[IRAK1BP1]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ALKBH8]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[COMMD2]] | +0.57 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[PHAX]] | +0.56 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[CDC40]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNC3]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RELT]] | -0.48 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[CCDC200]] | -0.47 | -0.29 / -0.50 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises APC's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD109]] | C | the direction of APC's effect on CD109's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 7 lines vs 26 not recorded | the APC-altered lines respond 0.52× as strongly (z diff +3.85); strongest at Harringtonine 5 µM: 0.84x vs 0.32x (z diff +5.3) | 0.011 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[PALD1]] | C | the direction of APC's effect on PALD1's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 8 lines vs 24 not recorded | the APC-altered lines respond 3.06× as strongly (z diff -3.91); strongest at Trametinib 5 µM: 0.22x vs 0.58x (z diff -6.0) | 0.014 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[SERINC5]] | C | APC activity strengthens SERINC5's drug response | recorded loss-of-function mutation of APC in 7 lines vs 39 not recorded | the APC-altered lines respond 0.66× as strongly (z diff +2.08); strongest at Idarubicin (hydrochloride) 5 µM: 1.32x vs 3.71x (z diff +7.2) | 0.017 | ⚠ tissue-confounded; across organs; target measured in part of the lines; artifact flags |
| [[RGS17]] | C | the direction of APC's effect on RGS17's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 6 lines vs 28 not recorded | the APC-altered lines respond 0.42× as strongly (z diff +3.23); strongest at Homoharringtonine 5 µM: 0.88x vs 0.29x (z diff +8.1) | 0.040 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[ORMDL2]] | C | APC activity weakens ORMDL2's drug response | recorded loss-of-function mutation of APC in 7 lines vs 38 not recorded | the APC-altered lines respond 1.71× as strongly (z diff -1.27); strongest at Panobinostat 5 µM: 2.26x vs 1.44x (z diff -2.7) | 0.047 | ⚠ tissue-confounded; across organs; target measured in part of the lines; artifact flags |
| [[SERINC5]] | C | the direction of APC's effect on SERINC5's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 10 lines vs 39 not recorded | the APC-altered lines respond 0.70× as strongly (z diff +1.94); strongest at Idarubicin (hydrochloride) 5 µM: 1.48x vs 3.71x (z diff +6.3) | 0.057 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[RGS17]] | C | APC activity strengthens RGS17's drug response | recorded loss-of-function mutation of APC in 5 lines vs 28 not recorded | the APC-altered lines respond 0.38× as strongly (z diff +3.47); strongest at Homoharringtonine 5 µM: 0.99x vs 0.29x (z diff +9.1) | 0.072 | ⚠ tissue-confounded; across organs; target measured in part of the lines; artifact flags |
| [[DNM2]] | C | APC activity strengthens DNM2's drug response | recorded loss-of-function mutation of APC in 7 lines vs 38 not recorded | the APC-altered lines respond 0.91× as strongly (z diff +0.83); strongest at Panobinostat 0.5 µM: 1.07x vs 2.04x (z diff +7.2) | 0.072 | ⚠ tissue-confounded; across organs; target measured in part of the lines; both ways; artifact flags |
| [[HADHB]] | C | the direction of APC's effect on HADHB's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 10 lines vs 40 not recorded | the APC-altered lines respond 1.91× as strongly (z diff -2.15); strongest at Panobinostat 5 µM: 2.16x vs 1.40x (z diff -4.3) | 0.091 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; artifact flags |
| [[ENSG00000270087]] | C | the direction of APC's effect on ENSG00000270087's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 10 lines vs 36 not recorded | the APC-altered lines respond 1.35× as strongly (z diff -0.59); strongest at Tucidinostat 5 µM: 2.37x vs 1.58x (z diff -2.1) | 0.269 over the table, 0.054 within its group | ⚠ within its group only (a lead); tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; both ways; artifact flags |
| [[ELL2]] | C | APC activity strengthens ELL2's drug response | recorded loss-of-function mutation of APC in 5 lines vs 32 not recorded | the APC-altered lines respond 0.08× as strongly (z diff +6.41); strongest at Idarubicin (hydrochloride) 5 µM: 1.06x vs 0.36x (z diff +9.9) | 0.300 over the table, 0.079 within its group | ⚠ within its group only (a lead); tissue-confounded; across organs; target measured in part of the lines; lower baseline (lost expression?); artifact flags |
| [[SLC12A2]] | C | the direction of APC's effect on SLC12A2's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 10 lines vs 37 not recorded | the APC-altered lines respond 0.10× as strongly (z diff +4.90); strongest at Idarubicin (hydrochloride) 5 µM: 0.99x vs 2.24x (z diff +8.5) | 0.320 over the table, 0.068 within its group | ⚠ within its group only (a lead); tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.6, 15.7); signed map (-21.2, -11.4). **Vector** length 98.8, 25.1% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +7.9 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.6 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -20.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -17.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.5 | -7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -18.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | APC regulator of Wnt signaling pathway |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.2 — chr5:112,707,518-112,846,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DP2, DP3, DP2.5, PPP1R46 |
| Gene groups (HGNC) | Armadillo repeat containing; Protein phosphatase 1 regulatory subunits |
| Hallmark sets | TGF_BETA_SIGNALING, MITOTIC_SPINDLE |
| Reactome | 26 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P25054](https://www.uniprot.org/uniprotkb/P25054) (Adenomatous polyposis coli protein):

> Tumor suppressor. Promotes rapid degradation of CTNNB1 and participates in Wnt signaling as a negative regulator. APC activity is correlated with its phosphorylation state. Activates the GEF activity of SPATA13 and ARHGEF4. Plays a role in hepatocyte growth factor (HGF)-induced cell migration. Required for MMP9 up-regulation via the JNK signaling pathway in colorectal tumor cells. Associates with both microtubules and actin filaments, components of the cytoskeleton. Plays a role in mediating …

**Summary**, from NCBI Gene [324](https://www.ncbi.nlm.nih.gov/gene/324):

> This gene encodes a tumor suppressor protein that acts as an antagonist of the Wnt signaling pathway. It is also involved in other processes including cell migration and adhesion, transcriptional activation, and apoptosis. Defects in this gene cause familial adenomatous polyposis (FAP), an autosomal dominant pre-malignant disease that usually progresses to malignancy. Mutations in the APC gene have been found to occur in most colorectal cancers, where disease-associated mutations tend to be …

**Accessions** — [HGNC:583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:583) · Entrez [324](https://www.ncbi.nlm.nih.gov/gene/324) · UniProt [P25054](https://www.uniprot.org/uniprotkb/P25054) · Ensembl [ENSG00000134982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134982)

## Data

Gene col 5631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5631); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5631]; `tensor/DDL_lfc|DDL_z.npy` [5631]; `embed/gene_vectors.npy` [5631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5631 or target_col == 5631). Every well: [[APC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
