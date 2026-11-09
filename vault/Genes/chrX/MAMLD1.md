---
symbol: "MAMLD1"
type: "gene"
col: 281
ensembl_id: "ENSG00000013619"
name: "mastermind like domain containing 1"
location: "Xq28"
module: 193
arm: "+"
pooled_cpm: 32.35
n_lines_expressing: 39
n_dd_up: 30
n_dd_down: 28
n_dd_up_clean: 20
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 24
direction_downstream: 15
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# MAMLD1

*mastermind like domain containing 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 2.00× (z +9.6, q 4e-19, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.672× (z -7.9, q 2e-12, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCHIP1]] (+0.65, fdr 7e-06), [[CORO2B]] (+0.64, fdr 7e-06), [[ASAP2]] (+0.62, fdr 1e-05); moves opposite to [[DYNC2LI1]] (-0.61, fdr 1e-05), [[FPGT]] (-0.57, fdr 1e-05), [[NDUFS2]] (-0.55, fdr 1e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CD59]] → it (grade B ⚠); 15 go from it, the strongest it → [[CD59]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +9.6 | 4e-19 | 31/37 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +8.2 | 7e-14 | 26/37 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.9 | 6e-13 | 27/37 (SW 900, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.8 | 1e-12 | 21/37 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.7 | 2e-12 | 21/37 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.3 | 2e-11 | 24/37 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +7.2 | 4e-11 | 29/36 (A-172, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.2 | 4e-11 | 27/37 (SW480, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +6.0 | 1e-07 | 21/37 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +5.4 | 3e-06 | 21/37 (PANC-1, CFPAC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.49×** | +5.3 | 7e-06 | 21/36 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +4.8 | 8e-05 | 21/37 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.40×** | +4.6 | 2e-04 | 18/37 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.37×** | +4.4 | 5e-04 | 16/36 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +4.2 | 0.001 | 17/36 (A-172, C32, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.005 | 14/35 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.013 | 12/37 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.017 | 9/37 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.039 | 14/37 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.672×** | -7.9 | 2e-12 | 25/37 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.595×** | -7.3 | 1e-10 | 23/34 (SK-MEL-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -5.4 | 2e-05 | 17/31 (HOP62, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.701×** | -5.0 | 9e-05 | 17/37 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.740×** | -4.9 | 1e-04 | 22/37 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.745×** | -4.8 | 1e-04 | 21/37 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -4.5 | 7e-04 | 17/36 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.547×** | -4.4 | 7e-04 | 17/36 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -4.4 | 7e-04 | 18/36 (SW1417, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.004 | 14/37 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.004 | 16/37 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.607×** | -3.6 | 0.012 | 17/36 (H4, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.776×** | -3.6 | 0.016 | 16/37 (RPMI-7951, SNU-423, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.763×** | -3.5 | 0.016 | 15/37 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.795×** | -3.5 | 0.016 | 14/37 (HOP62, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.834× | -3.5 | 0.016 | 12/37 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.019 | 13/38 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -3.3 | 0.030 | 14/37 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.798×** | -3.1 | 0.058 | 12/37 (HOP62, J82, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.859× | -3.0 | 0.060 | 8/38 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 96.3 | 0 | 9 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.468× (z -18.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.267× (z -10.8) |
| [[A-172 (line)]] | wt | 35.4 | 7 (5 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.4 | 7 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 8.42× (z +13.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.79× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 8.35 | 5 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 8.61× (z +12.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 5.96× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 41.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +22.1) | — |
| [[A-427 (line)]] | wt | 20.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -9.0) ⚠ toxic |
| [[A498 (line)]] | wt | 31.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 97.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -16.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 66.5 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.659× (z -10.1) ⚠ position not correctable |
| [[SK-MEL-2 (line)]] | alt | 57.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0974× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.2) |
| [[SW1417 (line)]] | alt | 12.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.16× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -10.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 18.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 47.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.170× (z -14.8) |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0904× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[C32 (line)]] | wt | 34.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 45.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.338× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 14.2× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.483× (z -11.2) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCHIP1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SHANK2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[BMAL2]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[AGO2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Pre-NOTCH Expression and Processing; STRING 537 |
| [[SLC35F3]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CDH4]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ANTXR2]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CDYL2]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NAV3]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2LI1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[FPGT]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NDUFS2]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TENT2]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[EFCAB7]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DNASE2]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PIGB]] | -0.53 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[HMBOX1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ANAPC10]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[EXD2]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[APOOL]] | -0.50 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[CRYZL1]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 16, C 8. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises MAMLD1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 3.79× lower at baseline in the lines without CD59 | 0.011 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[CCND1]] | B | CCND1 activity raises MAMLD1's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without CCND1 | 0.017 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[CLCF1]] | B | CLCF1 activity raises MAMLD1's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without CLCF1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[ST3GAL6]] | B | ST3GAL6 activity raises MAMLD1's level | lines that do not express ST3GAL6 (8) vs lines expressing it (42) | 4.30× lower at baseline in the lines without ST3GAL6 | 0.024 | ⚠ within organs, on part of the lines; also absent: DCBLD2; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises MAMLD1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without ITGA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[NAV3]] | B | NAV3 activity raises MAMLD1's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without NAV3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[GLI2]] | B | GLI2 activity raises MAMLD1's level | lines that do not express GLI2 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without GLI2 | 0.047 | ⚠ within organs, on part of the lines; also absent: HAPLN3 |
| [[TOP2A]] | B | TOP2A activity lowers MAMLD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MGLL]] | B | MGLL activity raises MAMLD1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without MGLL | 0.047 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[DPF3]] | B | DPF3 activity raises MAMLD1's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without DPF3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[GPR39]] | B | GPR39 activity raises MAMLD1's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without GPR39 | 0.057 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[BCAR3]] | B | BCAR3 activity raises MAMLD1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 3.57× lower at baseline in the lines without BCAR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | MAMLD1 activity raises CD59's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without MAMLD1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[KLF12]] | B | MAMLD1 activity raises KLF12's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without MAMLD1 | 0.014 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[EGFR]] | B | MAMLD1 activity raises EGFR's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without MAMLD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[ARHGAP10]] | B | MAMLD1 activity raises ARHGAP10's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without MAMLD1 | 0.016 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[TEAD1]] | B | MAMLD1 activity raises TEAD1's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without MAMLD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[ITGA2]] | B | MAMLD1 activity raises ITGA2's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without MAMLD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[GLI2]] | B | MAMLD1 activity raises GLI2's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without MAMLD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[FOSL1]] | B | MAMLD1 activity raises FOSL1's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without MAMLD1 | 0.061 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[GPR39]] | B | MAMLD1 activity raises GPR39's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without MAMLD1 | 0.063 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[CCND1]] | B | MAMLD1 activity raises CCND1's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without MAMLD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[ARHGAP31]] | B | MAMLD1 activity raises ARHGAP31's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 3.65× lower at baseline in the lines without MAMLD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[SYNJ2]] | B | MAMLD1 activity raises SYNJ2's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without MAMLD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.3, 8.5); signed map (8.9, 43.7). **Vector** length 115, 29.6% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.2 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +5.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.0 | -7.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.1 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.2 | -3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | mastermind like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:150,361,422-150,514,178 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CG1, F18; previously CXorf6 |
| Reactome | 28 pathways, smallest: NOTCH2 intracellular domain regulates transcription; RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13495](https://www.uniprot.org/uniprotkb/Q13495) (Mastermind-like domain-containing protein 1):

> Transactivates the HES3 promoter independently of NOTCH proteins. HES3 is a non-canonical NOTCH target gene which lacks binding sites for RBPJ.

**Summary**, from NCBI Gene [10046](https://www.ncbi.nlm.nih.gov/gene/10046):

> This gene encodes a mastermind-like domain containing protein. This protein may function as a transcriptional co-activator. Mutations in this gene are the cause of X-linked hypospadias type 2. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:2568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2568) · Entrez [10046](https://www.ncbi.nlm.nih.gov/gene/10046) · UniProt [Q13495](https://www.uniprot.org/uniprotkb/Q13495) · Ensembl [ENSG00000013619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013619)

## Data

Gene col 281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 281); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 281]; `tensor/DDL_lfc|DDL_z.npy` [281]; `embed/gene_vectors.npy` [281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 281 or target_col == 281). Every well: [[MAMLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAMLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
