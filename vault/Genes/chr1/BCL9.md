---
symbol: "BCL9"
type: "gene"
col: 3763
ensembl_id: "ENSG00000116128"
name: "BCL9 transcription coactivator"
location: "1q21.2"
module: 183
arm: "+"
pooled_cpm: 26.54
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# BCL9

*BCL9 transcription coactivator* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.35× (z +4.9, q 6e-04, up in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.30× (z +4.3, q 0.004, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -14.2, q 1e-42, down in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.477× (z -11.8, q 8e-30, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JKAMP]] (+0.67, fdr 7e-06), [[TMEM9]] (+0.66, fdr 1e-05), [[KCTD6]] (+0.64, fdr 1e-05); moves opposite to [[LARP1B]] (-0.59, fdr 2e-05), [[DGKH]] (-0.58, fdr 1e-05), [[KDSR]] (-0.58, fdr 2e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MGLL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.35×** | +4.9 | 6e-04 | 24/47 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.004 | 20/47 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.004 | 16/48 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.018 | 19/46 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.018 | 19/47 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.27×** | +3.7 | 0.019 | 17/47 (HepG2/C3A, CHP-212, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.030 | 17/48 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.042 | 16/47 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.4 | 0.042 | 18/48 (HOP62, NCI-H2347, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.3 | 0.061 | 15/47 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.061 | 11/48 (AsPC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.097 | 7/48 (RPMI-7951, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.533×** | -14.2 | 1e-42 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -12.2 | 1e-31 | 31/37 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.477×** | -11.8 | 8e-30 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -9.7 | 7e-20 | 34/44 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -9.1 | 1e-17 | 38/47 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -7.5 | 6e-12 | 30/48 (NCI-H2347, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.658×** | -6.4 | 1e-08 | 26/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -6.3 | 2e-08 | 31/46 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -5.7 | 9e-07 | 26/40 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -4.9 | 5e-05 | 22/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.9 | 5e-05 | 24/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.751×** | -4.1 | 0.002 | 17/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -4.0 | 0.002 | 23/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.770×** | -4.0 | 0.003 | 18/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.778×** | -4.0 | 0.003 | 15/48 (NCI-H460, SNU-1, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -3.7 | 0.009 | 19/48 (SNU-1, SW1417, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.725×** | -3.6 | 0.009 | 17/46 (SW 900, NCI-H23, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.058 | 12/44 (SNU-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.811×** | -3.0 | 0.063 | 9/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.822×** | -3.0 | 0.080 | 13/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.0 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -27.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -19.9) |
| [[C32 (line)]] | wt | 52.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 27.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 48.4 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -14.2) |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -12.4) |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.4) |
| [[A-427 (line)]] | wt | 31.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -13.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 76.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 48.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -8.6) |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 19.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -18.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.215× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.141× (z -11.3) |
| [[SW480 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -15.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0527× (z -14.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -16.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.108× (z -8.6) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JKAMP]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TMEM9]] | +0.66 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[KCTD6]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ARL6]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TRAPPC2]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[GSTA4]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FAM104A]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[USP30]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[HSF2]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PGAP1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP1B]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[DGKH]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[KDSR]] | -0.58 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[GNG12-AS1]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.57 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[GRK4]] | -0.57 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[MIRLET7IHG]] | -0.57 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[LINC02936]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[ITPRIPL2]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CFLAR]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[WNK4]] | -0.55 | -0.60 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGLL]] | B | MGLL activity lowers BCL9's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.80× higher at baseline in the lines without MGLL | 0.015 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises BCL9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.1, -8.4); signed map (-31.6, -7.3). **Vector** length 99.5, 23.0% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.9 | +4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.0 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.9 | -14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | BCL9 transcription coactivator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:147,541,501-147,626,216 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Reactome | 4 pathways, smallest: Deactivation of the beta-catenin transactivating complex; Formation of the beta-catenin:TCF transactivating complex; TCF dependent signaling in response to WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [O00512](https://www.uniprot.org/uniprotkb/O00512) (B-cell CLL/lymphoma 9 protein):

> Involved in signal transduction through the Wnt pathway. Promotes beta-catenin's transcriptional activity (By similarity).

**Summary**, from NCBI Gene [607](https://www.ncbi.nlm.nih.gov/gene/607):

> BCL9 is associated with B-cell acute lymphoblastic leukemia. It may be a target of translocation in B-cell malignancies with abnormalities of 1q21. Its function is unknown. The overexpression of BCL9 may be of pathogenic significance in B-cell malignancies. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1008) · Entrez [607](https://www.ncbi.nlm.nih.gov/gene/607) · UniProt [O00512](https://www.uniprot.org/uniprotkb/O00512) · Ensembl [ENSG00000116128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116128)

## Data

Gene col 3763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3763); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3763]; `tensor/DDL_lfc|DDL_z.npy` [3763]; `embed/gene_vectors.npy` [3763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3763 or target_col == 3763). Every well: [[BCL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
