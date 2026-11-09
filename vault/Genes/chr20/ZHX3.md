---
symbol: "ZHX3"
type: "gene"
col: 10482
ensembl_id: "ENSG00000174306"
name: "zinc fingers and homeoboxes 3"
location: "20q12"
module: 97
arm: "+"
pooled_cpm: 56.04
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 31
n_dd_up_clean: 12
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ZHX3

*zinc fingers and homeoboxes 3* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.86× (z +12.4, q 2e-32, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.508× (z -19.1, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERGIC1]] (+0.66, fdr 2e-05), [[LDLRAD3]] (+0.61, fdr 7e-06), [[LRRC20]] (+0.59, fdr 3e-05); moves opposite to [[SQSTM1]] (-0.62, fdr 7e-06), [[STX17-DT]] (-0.62, fdr 6e-05), [[LSMEM1]] (-0.60, fdr 5e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SH3RF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +12.4 | 2e-32 | 42/48 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.77×** | +11.4 | 1e-27 | 38/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.71×** | +10.8 | 9e-25 | 38/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +9.9 | 4e-21 | 39/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +9.7 | 2e-20 | 36/48 (SW1417, HepG2/C3A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +8.8 | 2e-16 | 42/48 (KATO III, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +8.1 | 6e-14 | 36/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 5e-05 | 24/48 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +4.8 | 1e-04 | 23/48 (NCI-H1792, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.003 | 21/48 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.004 | 17/48 (NCI-H1792, Hs 766T, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.005 | 13/48 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.008 | 19/48 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.023 | 13/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.030 | 19/48 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.18× | +3.2 | 0.042 | 15/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.069 | 20/48 (NCI-H1792, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.508×** | -19.1 | 0e+00 | 40/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -13.9 | 3e-41 | 35/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -13.7 | 2e-40 | 41/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.532×** | -12.5 | 6e-34 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.650×** | -12.1 | 1e-31 | 39/48 (J82, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -11.4 | 3e-28 | 39/48 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -10.9 | 1e-25 | 41/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.602×** | -10.1 | 5e-22 | 37/48 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -9.7 | 1e-20 | 36/48 (J82, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -9.2 | 2e-18 | 34/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -8.8 | 6e-17 | 31/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -8.3 | 4e-15 | 31/47 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -8.1 | 3e-14 | 32/48 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.692×** | -7.3 | 1e-11 | 29/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.693×** | -7.3 | 1e-11 | 28/48 (RKO, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.693×** | -7.3 | 1e-11 | 33/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -6.1 | 2e-08 | 29/49 (KATO III, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.744×** | -5.9 | 1e-07 | 26/48 (NCI-H23, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 66.6 | 21 | 3 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 4.96× (z +14.4) | [[Harringtonine (drug)]] 5 µM 0.191× (z -14.3) |
| [[Hs 766T (line)]] | wt | 55.6 | 17 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 5.91× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.304× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 93.6 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -19.1) |
| [[PANC-1 (line)]] | alt | 50.4 | 2 (1 ⚠) | 8 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.29× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -20.1) |
| [[HT-29 (line)]] | alt | 44.4 | 2 (1 ⚠) | 7 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.00× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.228× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 41.0 | 1 | 8 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.33× (z +8.6) | [[Harringtonine (drug)]] 0.5 µM 0.176× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 61.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -16.0) |
| [[SW480 (line)]] | alt | 74.4 | 1 | 6 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.83× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.386× (z -14.2) |
| [[A498 (line)]] | wt | 82.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -23.0) |
| [[C32 (line)]] | wt | 87.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.4) |
| [[COLO 205 (line)]] | alt | 44.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 20.2 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.16× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 5.84× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 68.9 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -10.5) |
| [[RKO (line)]] | wt | 125 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.7) |
| [[HS-578T (line)]] | alt | 61.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.266× (z -11.3) |
| [[SNU-1 (line)]] | wt | 54.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.1) |
| [[SW1417 (line)]] | alt | 83.3 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.511× (z -11.2) |
| [[HOP62 (line)]] | alt | 49.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.236× (z -13.2) |
| [[SW 900 (line)]] | alt | 43.6 | 1 | 3 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.26× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.3) |
| [[A-427 (line)]] | wt | 40.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -8.6) |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -11.3) |
| [[C-33 A (line)]] | alt | 58.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.332× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 21.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.36× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.9) |
| [[A-172 (line)]] | wt | 71.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -14.3) |
| [[H4 (line)]] | wt | 48.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0921× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.3) |
| [[KATO III (line)]] | alt | 59.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.4) |
| [[SNU-423 (line)]] | alt | 81.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.1) |
| [[LoVo (line)]] | wt | 25.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.336× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.9 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.69× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -10.5) |
| [[SHP-77 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 37.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0567× (z -15.6) |
| [[A549 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | +0.66 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[LDLRAD3]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LRRC20]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MT1X]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[P3H4]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PXYLP1]] | +0.57 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[USP31]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RHOBTB2]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[TANC2]] | +0.56 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[ANGPTL4]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[NUP93]] | +0.55 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[MT2A]] | +0.55 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SQSTM1]] | -0.62 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[STX17-DT]] | -0.62 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[LSMEM1]] | -0.60 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LRP1B]] | -0.60 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ZHX2]] | -0.60 | -0.46 / -0.50 | both halves | 3e-05 | same gene group; STRING 619 |
| [[N4BP2L1]] | -0.59 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[TTC6]] | -0.59 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ATP6V1G1]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[KLRK1-AS1]] | -0.58 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[IGSF11]] | -0.58 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.57 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ZFHX2-AS1]] | -0.57 | -0.47 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3RF3]] | B | SH3RF3 activity raises ZHX3's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without SH3RF3 | 0.014 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[SERPINE1]] | B | SERPINE1 activity raises ZHX3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without SERPINE1 | 0.020 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[DSC2]] | B | DSC2 activity lowers ZHX3's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.65× higher at baseline in the lines without DSC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 9.9); signed map (-11.5, 51.6). **Vector** length 123, 40.2% of its response variance represented; |z| ≥ 3 in 1,727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.7 | +12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +9.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.5 | +8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.0 | +10.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.9 | +3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.9 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.6 | +3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.4 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.8 | -12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.4 | -11.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.3 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -6.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc fingers and homeoboxes 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12 — chr20:41,178,448-41,317,731 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0395; previously TIX1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4I2](https://www.uniprot.org/uniprotkb/Q9H4I2) (Zinc fingers and homeoboxes protein 3):

> Acts as a transcriptional repressor. Involved in the early stages of mesenchymal stem cell (MSC) osteogenic differentiation. Is a regulator of podocyte gene expression during primary glomerula disease. Binds to promoter DNA.

**Summary**, from NCBI Gene [23051](https://www.ncbi.nlm.nih.gov/gene/23051):

> This gene encodes a member of the zinc fingers and homeoboxes (ZHX) gene family. The encoded protein contains two C2H2-type zinc fingers and five homeodomains and forms a dimer with itself or with zinc fingers and homeoboxes family member 1. In the nucleus, the dimerized protein interacts with the A subunit of the ubiquitous transcription factor nuclear factor-Y and may function as a transcriptional repressor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15935) · Entrez [23051](https://www.ncbi.nlm.nih.gov/gene/23051) · UniProt [Q9H4I2](https://www.uniprot.org/uniprotkb/Q9H4I2) · Ensembl [ENSG00000174306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174306)

## Data

Gene col 10482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10482); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10482]; `tensor/DDL_lfc|DDL_z.npy` [10482]; `embed/gene_vectors.npy` [10482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10482 or target_col == 10482). Every well: [[ZHX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZHX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
