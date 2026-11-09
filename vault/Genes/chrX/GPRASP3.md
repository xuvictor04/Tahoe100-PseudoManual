---
symbol: "GPRASP3"
type: "gene"
col: 12729
ensembl_id: "ENSG00000198908"
name: "G protein-coupled receptor associated sorting protein family member 3"
location: "Xq22.1"
module: 23
arm: "+"
pooled_cpm: 9.44
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GPRASP3

*G protein-coupled receptor associated sorting protein family member 3* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.84× (z +12.2, q 3e-31, up in 29 of 43 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +9.3, q 6e-18, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.620× (z -6.7, q 1e-08, down in 19 of 43 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.575× (z -4.1, q 0.006, down in 12 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SW480 0.125×, A549 0.136×, PANC-1 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 0.106×, NCI-H460 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0941×); [[Harringtonine (drug)]] 0.05 µM in 1 line (C32 0.0959×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX5-GPRASP2]] (+0.75, fdr 7e-06, ⚠ same locus), [[GPRASP1]] (+0.68, fdr 1e-05), [[RRAGB]] (+0.67, fdr 7e-06), [[HPS1]] (+0.67, fdr 1e-05); moves opposite to [[LSM4]] (-0.62, fdr 2e-05), [[MYCBP]] (-0.61, fdr 1e-05), [[SLC25A39]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THBS4]] → it (grade B ⚠); 2 go from it, the strongest it → [[RRAGB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.84×** | +12.2 | 3e-31 | 29/43 (LoVo, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +9.3 | 6e-18 | 22/40 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +9.2 | 9e-18 | 25/42 (HOP62, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +8.1 | 8e-14 | 26/43 (LoVo, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.51×** | +5.8 | 6e-07 | 16/43 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 1e-04 | 11/40 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.40×** | +4.7 | 2e-04 | 13/44 (LS 180, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 5e-04 | 12/42 (KATO III, J82, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.004 | 8/36 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.9 | 0.005 | 13/33 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.005 | 9/43 (SW480, NCI-H23, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +3.5 | 0.019 | 6/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.025 | 7/36 (SNU-423, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.033 | 9/43 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.042 | 5/43 (SK-MEL-2, SNU-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.060 | 8/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SW480 0.125×, A549 0.136×, PANC-1 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 0.106×, NCI-H460 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0941×); [[Harringtonine (drug)]] 0.05 µM in 1 line (C32 0.0959×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.620×** | -6.7 | 1e-08 | 19/43 (HepG2/C3A, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.653×** | -5.7 | 4e-06 | 21/43 (SW480, HOP62, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.716×** | -4.5 | 0.001 | 18/35 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.739×** | -4.2 | 0.003 | 9/43 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.575×** | -4.1 | 0.006 | 12/39 (HCT15, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.753×** | -4.0 | 0.007 | 15/43 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.759×** | -3.9 | 0.009 | 17/39 (SW480, A549, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.757×** | -3.7 | 0.017 | 17/42 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -3.4 | 0.050 | 8/40 (SNU-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.636×** | -3.3 | 0.051 | 13/43 (KATO III, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.801×** | -3.1 | 0.099 | 10/43 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 0.803× | -3.1 | 0.10 | 15/43 (A-172, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 16.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 9.92 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A-172 (line)]] | wt | 2.99 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0635× (z -8.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A549 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[C32 (line)]] | wt | 9.04 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0959× (z -8.5) |
| [[HOP62 (line)]] | alt | 11.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0941× (z -8.6) |
| [[J82 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +17.5) | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 18.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +9.0) | — |
| [[A-427 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5-GPRASP2]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 | ⚠ same locus (6.0 kb, same strand: neighbours can correlate without regulation) |
| [[GPRASP1]] | +0.68 | +0.69 / +0.57 | both halves | 1e-05 | same gene group |
| [[RRAGB]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[HPS1]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[UFC1]] | +0.66 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[TSC1]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[HSBP1L1]] | +0.64 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ARMCX1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 | same gene group |
| [[NKAPD1]] | +0.63 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[N4BP2L1]] | +0.62 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[CELF6]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TCEAL1]] | +0.61 | +0.65 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[MYCBP]] | -0.61 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A39]] | -0.59 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SETD3]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ADARB1]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[FAM234A]] | -0.56 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[TUBG1]] | -0.56 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[NUP93]] | -0.54 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ADAM15]] | -0.54 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[NOMO1]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[TGM2]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.54 | -0.61 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity raises GPRASP3's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without THBS4 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers GPRASP3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00649]] | B | LINC00649 activity raises GPRASP3's level | lines that do not express LINC00649 (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without LINC00649 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGB]] | C | GPRASP3 activity raises RRAGB's level | lines that do not express GPRASP3 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without GPRASP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DCP1B, ST8SIA5, DISC1; maybe low, not absent; its own permutation p |
| [[THBS4]] | C | GPRASP3 activity raises THBS4's level | lines that do not express GPRASP3 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without GPRASP3 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DCP1B, ST8SIA5, DISC1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-2.7, 17.1); signed map (16.4, -14.0). **Vector** length 71.2, 12.2% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.8 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.1 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.5 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -2.7 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor associated sorting protein family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:102,720,688-102,753,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p60TRP, KIAA1701, GASP3; previously BHLHB9 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PI77](https://www.uniprot.org/uniprotkb/Q6PI77) (G protein-coupled receptor associated sorting protein 3):

> Survival and differentiation promoting protein that plays a role in the regulation of neurosynaptogenesis. Induces phosphatase PP2A activity which results in APP dephosphorylation and inhibits BACE1-mediated processing of APP.

**Summary**, from NCBI Gene [80823](https://www.ncbi.nlm.nih.gov/gene/80823):

> This gene is a member of a gene family which encodes proteins with a basic helix-loop-helix domain. Other members of this gene family encode proteins which function as transcription factors, either enhancing or inhibiting transcription depending on the activity of other DNA binding proteins. The coding region of this gene is located entirely within the terminal exon. The encoded protein may be involved in the survival of neurons (PMID: 15034937). Multiple alternatively spliced variants, …

**Accessions** — [HGNC:29353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29353) · Entrez [80823](https://www.ncbi.nlm.nih.gov/gene/80823) · UniProt [Q6PI77](https://www.uniprot.org/uniprotkb/Q6PI77) · Ensembl [ENSG00000198908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198908)

## Data

Gene col 12729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12729); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12729]; `tensor/DDL_lfc|DDL_z.npy` [12729]; `embed/gene_vectors.npy` [12729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12729 or target_col == 12729). Every well: [[GPRASP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRASP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
