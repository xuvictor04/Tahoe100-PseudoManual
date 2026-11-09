---
symbol: "ABCA7"
type: "gene"
col: 756
ensembl_id: "ENSG00000064687"
name: "ATP binding cassette subfamily A member 7"
location: "19p13.3"
module: 135
arm: "-"
pooled_cpm: 22.8
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# ABCA7

*ATP binding cassette subfamily A member 7* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.85× (z +16.7, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.374× (z -12.2, q 2e-31, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB9]] (+0.64, fdr 2e-05), [[CARHSP1]] (+0.64, fdr 3e-05), [[SLC66A2]] (+0.61, fdr 3e-05); moves opposite to [[ZNF507]] (-0.61, fdr 4e-05), [[DPH5-DT]] (-0.59, fdr 1e-04), [[DUS4L]] (-0.58, fdr 7e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.85×** | +16.7 | 0e+00 | 43/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.25×** | +14.6 | 0e+00 | 40/45 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +11.4 | 6e-28 | 41/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +8.6 | 9e-16 | 38/45 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.7 | 3e-09 | 30/46 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +5.2 | 2e-05 | 24/44 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +4.5 | 4e-04 | 19/46 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +3.5 | 0.037 | 18/45 (LS 180, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.056 | 10/44 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.061 | 13/46 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.28× | +3.0 | 0.12 | 15/45 (C-33 A, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.374×** | -12.2 | 2e-31 | 39/45 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.444×** | -10.1 | 2e-21 | 38/45 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.624×** | -8.3 | 3e-14 | 31/46 (NCI-H1573, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.532×** | -7.8 | 7e-13 | 32/45 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -7.8 | 7e-13 | 30/45 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.543×** | -7.6 | 4e-12 | 31/45 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.330×** | -7.2 | 5e-11 | 32/44 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.339×** | -7.0 | 2e-10 | 28/45 (HT-29, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -6.6 | 3e-09 | 26/44 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.584×** | -6.4 | 8e-09 | 29/44 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -5.6 | 9e-07 | 24/44 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.456×** | -5.1 | 2e-05 | 25/37 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -4.9 | 3e-05 | 24/43 (NCI-H1792, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -4.5 | 2e-04 | 23/45 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.686×** | -4.3 | 5e-04 | 21/45 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -4.2 | 7e-04 | 21/45 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.718×** | -4.1 | 0.001 | 18/45 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.719×** | -4.1 | 0.001 | 22/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.6 | 0.008 | 19/46 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0775× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 30.5 | 0 | 10 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -15.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -15.2) |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -15.8) |
| [[LS 180 (line)]] | wt | 27.1 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.10× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 32.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 75.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -15.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 19.0 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 3.15× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.406× (z -9.7) |
| [[SW480 (line)]] | alt | 20.7 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.49× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 3 | 1 | [[Belinostat (drug)]] 5 µM 4.57× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 65.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -11.0) |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 14.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.22× (z +11.6) | — |
| [[LoVo (line)]] | wt | 12.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.18× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.209× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 40.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.64× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 9.55 | 0 | 3 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0706× (z -9.4) |
| [[A549 (line)]] | wt | 20.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -8.5) |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0387× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 21.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +10.4) | — |
| [[J82 (line)]] | alt | 15.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.23× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.6) |
| [[SW1417 (line)]] | alt | 18.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +10.1) | — |
| [[A-172 (line)]] | wt | 10.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.51× (z +9.6) | — |
| [[A-427 (line)]] | wt | 18.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +8.8) | — |
| [[A498 (line)]] | wt | 9.94 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.85× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 20.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.208× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.1) |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0923× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -10.6) |
| [[SNU-423 (line)]] | alt | 7.40 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.75× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0434× (z -8.8) |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.3) |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB9]] | +0.64 | +0.48 / +0.59 | both halves | 2e-05 | pathway: ABC-family protein mediated transport |
| [[CARHSP1]] | +0.64 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SLC66A2]] | +0.61 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[KDM4B]] | +0.61 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.60 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GNAI2]] | +0.60 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[DNAAF3]] | +0.60 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[RASSF7]] | +0.59 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[SH3GL1]] | +0.59 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[PEDS1]] | +0.59 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SLC26A6]] | +0.58 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[ARID3A]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | -0.61 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[DPH5-DT]] | -0.59 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[DUS4L]] | -0.58 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[KICS2]] | -0.58 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TRMT5]] | -0.57 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[UTP20]] | -0.56 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ATXN10]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MTHFSD]] | -0.54 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[FAIM]] | -0.54 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[U2SURP]] | -0.54 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[MBTPS2]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[QSER1]] | -0.54 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ABCA7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ABCA7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (5.4, -3.1); signed map (-29.4, 18.8). **Vector** length 94.3, 23.9% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.2 | +11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +16.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +14.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | +1.9 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -8.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,039,997-1,065,572 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ABCX |
| Gene groups (HGNC) | ATP binding cassette subfamily A; ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: ABC transporters in lipid homeostasis; ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZY2](https://www.uniprot.org/uniprotkb/Q8IZY2) (Phospholipid-transporting ATPase ABCA7):

> Catalyzes the translocation of specific phospholipids from the cytoplasmic to the extracellular/lumenal leaflet of membrane coupled to the hydrolysis of ATP. Transports preferentially phosphatidylserine over phosphatidylcholine. Plays a role in lipid homeostasis and macrophage-mediated phagocytosis. Binds APOA1 and may function in apolipoprotein-mediated phospholipid efflux from cells. May also mediate cholesterol efflux. May regulate cellular ceramide homeostasis during keratinocyte …

**Summary**, from NCBI Gene [10347](https://www.ncbi.nlm.nih.gov/gene/10347):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. This full transporter has been detected …

**Accessions** — [HGNC:37](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37) · Entrez [10347](https://www.ncbi.nlm.nih.gov/gene/10347) · UniProt [Q8IZY2](https://www.uniprot.org/uniprotkb/Q8IZY2) · Ensembl [ENSG00000064687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064687)

## Data

Gene col 756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 756); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 756]; `tensor/DDL_lfc|DDL_z.npy` [756]; `embed/gene_vectors.npy` [756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 756 or target_col == 756). Every well: [[ABCA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
