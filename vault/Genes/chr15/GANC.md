---
symbol: "GANC"
type: "gene"
col: 13161
ensembl_id: "ENSG00000214013"
name: "glucosidase alpha, neutral C"
location: "15q15.1"
module: 10
arm: "+"
pooled_cpm: 26.07
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GANC

*glucosidase alpha, neutral C* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +6.5, q 5e-08, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.317× (z -16.3, q 0e+00, down in 44 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.366× (z -14.2, q 2e-43, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK4]] (+0.63, fdr 2e-05), [[CAPN3]] (+0.61, fdr 5e-05, ⚠ same locus), [[EFCAB6]] (+0.60, fdr 4e-05), [[LINC00663]] (+0.58, fdr 3e-05); moves opposite to [[DNMT3B]] (-0.55, fdr 9e-05), [[FCHO1]] (-0.54, fdr 1e-04), [[SYP]] (-0.54, fdr 0.002, ⚠ one half only (not replicated)), [[OTUD7A]] (-0.53, fdr 6e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.5 | 5e-08 | 29/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +5.2 | 6e-05 | 28/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.9 | 1e-04 | 18/33 (Panc 03.27, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.9 | 2e-04 | 24/47 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.5 | 6e-04 | 19/48 (A-427, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.003 | 18/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.1 | 0.003 | 17/44 (SHP-77, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.003 | 19/48 (KATO III, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.006 | 17/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.009 | 17/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.022 | 17/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.5 | 0.022 | 15/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.030 | 15/47 (HepG2/C3A, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.030 | 12/47 (NCI-H460, C32, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.043 | 16/48 (HS-578T, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.044 | 12/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.053 | 12/48 (SW480, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.317×** | -16.3 | 0e+00 | 44/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.366×** | -14.2 | 2e-43 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.418×** | -12.4 | 7e-33 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.435×** | -11.8 | 6e-30 | 41/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.637×** | -6.1 | 9e-08 | 28/47 (HOP62, A498, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -5.8 | 6e-07 | 23/48 (RKO, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.668×** | -5.7 | 9e-07 | 28/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -5.5 | 3e-06 | 28/48 (C32, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.761×** | -5.5 | 3e-06 | 25/47 (A549, C32, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -5.2 | 1e-05 | 24/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.686×** | -5.1 | 1e-05 | 25/46 (A-172, H4, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.699×** | -5.1 | 2e-05 | 26/48 (PANC-1, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -4.9 | 4e-05 | 23/47 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.717×** | -4.7 | 9e-05 | 26/47 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.725×** | -4.6 | 2e-04 | 24/48 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -4.1 | 0.002 | 20/48 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.587×** | -4.0 | 0.003 | 23/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.010 | 15/48 (NCI-H2030, C32, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.032 | 15/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.659×** | -3.1 | 0.049 | 13/47 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.1 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.186× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -13.3) |
| [[LoVo (line)]] | wt | 47.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.332× (z -10.7) |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.215× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 27.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -12.2) |
| [[SW480 (line)]] | alt | 27.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -13.6) |
| [[RKO (line)]] | wt | 63.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -10.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.360× (z -9.5) |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0693× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -10.3) |
| [[A-172 (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.280× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 21.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -8.6) |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0845× (z -16.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -14.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.7× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.236× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK4]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CAPN3]] | +0.61 | +0.67 / +0.39 | both halves | 5e-05 | ⚠ same locus (5.8 kb, same strand: neighbours can correlate without regulation) |
| [[EFCAB6]] | +0.60 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[LINC00663]] | +0.58 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[CTBP1-DT]] | +0.56 | +0.54 / +0.26 | both halves | 4e-04 |  |
| [[RABL2A]] | +0.55 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[DECR1]] | +0.55 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[CTPS2]] | +0.54 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[MAMDC2-AS1]] | +0.54 | +0.60 / +0.22 | both halves | 6e-04 |  |
| [[FAM120AOS]] | +0.54 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[CFLAR]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[BRCC3]] | +0.53 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[HIPK3]] | +0.53 | +0.28 / +0.48 | both halves | 3e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT3B]] | -0.55 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[FCHO1]] | -0.54 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[SYP]] | -0.54 | -0.14 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[OTUD7A]] | -0.53 | -0.21 / -0.57 | both halves | 6e-04 |  |
| [[ANKDD1A]] | -0.53 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[EPN2]] | -0.53 | -0.55 / -0.21 | both halves | 6e-04 |  |
| [[SGSM1]] | -0.52 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[AMN1]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CDC14B]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[EXOC6]] | -0.52 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[EDA]] | -0.52 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ARHGEF4]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SPATA2L]] | -0.51 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers GANC's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers GANC's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EDA]] | B | EDA activity lowers GANC's level | lines that do not express EDA (12) vs lines expressing it (38) | 1.45× higher at baseline in the lines without EDA | 0.097 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.5, 20.3); signed map (29.6, -12.1). **Vector** length 74.1, 15.5% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.7 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.9 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | glucosidase alpha, neutral C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:42,273,201-42,353,666 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycoside hydrolase family 31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TET4](https://www.uniprot.org/uniprotkb/Q8TET4) (Neutral alpha-glucosidase C):

> Has alpha-glucosidase activity.

**Summary**, from NCBI Gene [2595](https://www.ncbi.nlm.nih.gov/gene/2595):

> Glycosyl hydrolase enzymes hydrolyse the glycosidic bond between two or more carbohydrates, or between a carbohydrate and a non-carbohydrate moiety. This gene encodes a member of glycosyl hydrolases family 31. This enzyme hydrolyses terminal, non-reducing 1,4-linked alpha-D-glucose residues and releases alpha-D-glucose. This is a key enzyme in glycogen metabolism and its gene localizes to a chromosomal region (15q15) that is associated with susceptibility to diabetes. Alternative splicing …

**Accessions** — [HGNC:4139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4139) · Entrez [2595](https://www.ncbi.nlm.nih.gov/gene/2595) · UniProt [Q8TET4](https://www.uniprot.org/uniprotkb/Q8TET4) · Ensembl [ENSG00000214013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214013)

## Data

Gene col 13161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13161); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13161]; `tensor/DDL_lfc|DDL_z.npy` [13161]; `embed/gene_vectors.npy` [13161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13161 or target_col == 13161). Every well: [[GANC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GANC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
