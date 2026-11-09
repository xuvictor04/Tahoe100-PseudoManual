---
symbol: "GNPNAT1"
type: "gene"
col: 1978
ensembl_id: "ENSG00000100522"
name: "glucosamine-phosphate N-acetyltransferase 1"
location: "14q22.1"
module: 211
arm: "+"
pooled_cpm: 55.03
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# GNPNAT1

*glucosamine-phosphate N-acetyltransferase 1* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +13.0, q 6e-36, up in 41 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.77× (z +10.8, q 9e-25, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.449× (z -7.9, q 2e-12, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM241]] (+0.67, fdr 1e-05), [[SACS]] (+0.64, fdr 1e-05), [[PGAM5]] (+0.62, fdr 1e-05); moves opposite to [[TMEM59]] (-0.62, fdr 1e-05), [[ATOSA]] (-0.61, fdr 1e-05), [[WBP1]] (-0.60, fdr 1e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SACS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.99×** | +13.0 | 6e-36 | 41/47 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.92×** | +11.9 | 5e-30 | 38/43 (NCI-H23, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +10.8 | 9e-25 | 42/48 (NCI-H23, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +9.7 | 6e-20 | 42/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.3 | 1e-18 | 39/48 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +8.6 | 1e-15 | 38/48 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +8.1 | 5e-14 | 3/49 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.43×** | +6.7 | 2e-09 | 31/47 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.85×** | +6.1 | 8e-08 | 35/48 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.5 | 3e-06 | 25/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.36×** | +5.4 | 4e-06 | 24/44 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.31×** | +5.0 | 3e-05 | 23/47 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.30×** | +4.8 | 9e-05 | 27/48 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +4.6 | 2e-04 | 23/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 3e-04 | 23/48 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 5e-04 | 22/47 (NCI-H460, A549, …) | all doses, flat | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +4.2 | 9e-04 | 19/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.52×** | +4.1 | 1e-03 | 27/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.001 | 12/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.003 | 19/47 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.004 | 20/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.005 | 19/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.035 | 12/48 (LoVo, COLO 205, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -7.9 | 2e-12 | 43/49 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.769×** | -7.0 | 5e-10 | 26/48 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -5.9 | 7e-07 | 29/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.638×** | -4.4 | 0.001 | 28/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.806×** | -3.9 | 0.011 | 23/49 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.8 | 0.011 | 20/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.011 | 22/47 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -3.7 | 0.013 | 17/48 (A498, A549, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.707×** | -3.4 | 0.038 | 16/48 (LoVo, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.877× | -3.2 | 0.072 | 16/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.852× | -3.2 | 0.072 | 13/48 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.072 | 11/48 (LoVo, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.891× | -3.0 | 0.10 | 12/48 (AN3 CA, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.892× | -3.0 | 0.11 | 12/48 (MIA PaCa-2, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 98.4 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 53.2 | 4 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.73× (z +11.0) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 2.47× (z +9.9) | — |
| [[RKO (line)]] | wt | 116 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -15.2) |
| [[A549 (line)]] | wt | 65.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.34× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 43.6 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.44× (z +9.9) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.40× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 86.9 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.1) |
| [[LoVo (line)]] | wt | 65.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -8.8) |
| [[LS 180 (line)]] | wt | 56.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 65.7 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.83× (z +12.4) | — |
| [[A-172 (line)]] | wt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 31.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.3) |
| [[HCT15 (line)]] | alt | 68.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.0) |
| [[J82 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 80.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 75.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.125× (z -8.9) |
| [[SNU-423 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW48 (line)]] | wt | 130 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.8) |
| [[A-427 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM241]] | +0.67 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SACS]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CARNMT1]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[C12orf29]] | +0.61 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[POLR3G]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[DKC1]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[EEFSEC]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RIOX2]] | +0.59 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[RRP1B]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[BOP1]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[WBP1]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[PRPF18]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[IP6K2]] | -0.57 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[SYNRG]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[KDM6A]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[DYRK1B]] | -0.57 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CCDC115]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ZNF446]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NAPA-AS1]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[HBP1]] | -0.53 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises GNPNAT1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without SACS | 0.035 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[DHRS3]] | B | DHRS3 activity lowers GNPNAT1's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without DHRS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[CCND2]] | B | CCND2 activity raises GNPNAT1's level | lines that do not express CCND2 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without CCND2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, MTND1P23, ENSG00000237031 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, -40.8); signed map (-9.0, -55.7). **Vector** length 104, 28.4% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.2 | +9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +8.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.1 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.5 | +4.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.1 | -7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glucosamine-phosphate N-acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:52,775,193-52,791,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Gpnat1, FLJ10607 |
| Gene groups (HGNC) | GCN5 related N-acetyltransferases; Acyltransferases |
| Reactome | 4 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

UniProt [Q96EK6](https://www.uniprot.org/uniprotkb/Q96EK6) carries no function annotation.

**Summary**, from NCBI Gene [64841](https://www.ncbi.nlm.nih.gov/gene/64841):

> Enables identical protein binding activity. Predicted to be involved in UDP-N-acetylglucosamine biosynthetic process. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19980) · Entrez [64841](https://www.ncbi.nlm.nih.gov/gene/64841) · UniProt [Q96EK6](https://www.uniprot.org/uniprotkb/Q96EK6) · Ensembl [ENSG00000100522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100522)

## Data

Gene col 1978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1978); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1978]; `tensor/DDL_lfc|DDL_z.npy` [1978]; `embed/gene_vectors.npy` [1978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1978 or target_col == 1978). Every well: [[GNPNAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNPNAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
