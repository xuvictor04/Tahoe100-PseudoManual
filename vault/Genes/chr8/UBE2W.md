---
symbol: "UBE2W"
type: "gene"
col: 2446
ensembl_id: "ENSG00000104343"
name: "ubiquitin conjugating enzyme E2 W"
location: "8q21.11"
module: 172
arm: "+"
pooled_cpm: 97.65
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# UBE2W

*ubiquitin conjugating enzyme E2 W* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +15.0, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.590× (z -15.1, q 0e+00, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.862× (z -4.1, q 0.004, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.166×, SNU-1 0.160×, NCI-H23 0.220×, HT-29 0.291×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.270×, NCI-H2030 0.235×, RKO 0.320×, HT-29 0.303×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.424×, C32 0.353×, HEC-1-A 0.434×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP6R2]] (+0.64, fdr 7e-06), [[FAM222B]] (+0.61, fdr 1e-05), [[ZNF212]] (+0.60, fdr 1e-05); moves opposite to [[PGRMC1]] (-0.55, fdr 2e-05), [[CA5BP1-1]] (-0.52, fdr 1e-04), [[VAMP1]] (-0.51, fdr 2e-04).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +15.0 | 0e+00 | 40/48 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +12.5 | 4e-33 | 41/49 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +12.1 | 4e-31 | 40/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +10.6 | 6e-24 | 39/48 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +8.9 | 5e-17 | 39/48 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +8.9 | 7e-17 | 37/48 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +8.5 | 1e-15 | 36/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +8.2 | 1e-14 | 35/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +8.2 | 2e-14 | 33/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +7.7 | 7e-13 | 35/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +7.5 | 2e-12 | 28/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +5.8 | 3e-07 | 21/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +5.6 | 1e-06 | 23/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +5.6 | 1e-06 | 31/49 (RKO, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +5.2 | 6e-06 | 26/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.9 | 3e-05 | 10/48 (A-172, HT-29, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.166×, SNU-1 0.160×, NCI-H23 0.220×, HT-29 0.291×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.270×, NCI-H2030 0.235×, RKO 0.320×, HT-29 0.303×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.424×, C32 0.353×, HEC-1-A 0.434×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -15.1 | 0e+00 | 40/49 (NCI-H1573, C32, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -14.4 | 1e-44 | 36/45 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -11.4 | 6e-28 | 28/44 (NCI-H1573, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.831×** | -5.3 | 2e-05 | 23/48 (SW 1271, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -4.9 | 1e-04 | 22/49 (A-427, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -4.1 | 0.004 | 19/48 (NCI-H1573, A549, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.908× | -3.9 | 0.007 | 3/48 (Hs 766T, SNU-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.782×** | -3.4 | 0.055 | 10/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 82.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 142 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -26.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 87.7 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.04× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 90.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -14.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -17.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 131 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 98.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 112 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 142 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -17.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 85.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 76.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 65.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 65.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 98.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -12.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 188 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -15.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -12.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 73.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -13.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 68.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 69.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 96.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -13.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 78.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.7) | — |
| [[J82 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 134 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP6R2]] | +0.64 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[FAM222B]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZNF212]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TRAPPC5]] | +0.59 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[GTF2H5]] | +0.59 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ZNF609]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[USP4]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[GATAD2B]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[IP6K1]] | +0.55 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[MRPL36]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[MTLN]] ⚠ | +0.53 | +0.47 / +0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPIP5K1]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[NDUFC2]] | +0.53 | +0.41 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CA5BP1-1]] | -0.52 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[VAMP1]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[SMG1P6]] | -0.51 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[RPN1]] | -0.49 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PAPOLA]] | -0.47 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[EDEM1]] | -0.47 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[HSPE1-MOB4]] | -0.47 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[CANX]] | -0.46 | -0.29 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.364). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.2, -13.1); signed map (-16.0, -12.1). **Vector** length 76.2, 17.1% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | +3.3 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.6 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -14.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 W |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,780,097-73,878,910 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11011, UBC-16 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B02](https://www.uniprot.org/uniprotkb/Q96B02) (Ubiquitin-conjugating enzyme E2 W):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. Specifically monoubiquitinates the N-terminus of various substrates, including ATXN3, MAPT/TAU, POLR2H/RPB8 and STUB1/CHIP, by recognizing backbone atoms of disordered N-termini. Involved in degradation of misfolded chaperone substrates by mediating monoubiquitination of STUB1/CHIP, leading to recruitment of ATXN3 to monoubiquitinated STUB1/CHIP, and restriction of the length of ubiquitin chain …

**Summary**, from NCBI Gene [55284](https://www.ncbi.nlm.nih.gov/gene/55284):

> This gene encodes a nuclear-localized ubiquitin-conjugating enzyme (E2) that, along with ubiquitin-activating (E1) and ligating (E3) enzymes, coordinates the addition of a ubiquitin moiety to existing proteins. The encoded protein promotes the ubiquitination of Fanconi anemia complementation group proteins and may be important in the repair of DNA damage. There is a pseudogene for this gene on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug …

**Accessions** — [HGNC:25616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25616) · Entrez [55284](https://www.ncbi.nlm.nih.gov/gene/55284) · UniProt [Q96B02](https://www.uniprot.org/uniprotkb/Q96B02) · Ensembl [ENSG00000104343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104343)

## Data

Gene col 2446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2446); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2446]; `tensor/DDL_lfc|DDL_z.npy` [2446]; `embed/gene_vectors.npy` [2446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2446 or target_col == 2446). Every well: [[UBE2W — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2W.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
