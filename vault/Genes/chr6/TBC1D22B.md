---
symbol: "TBC1D22B"
type: "gene"
col: 789
ensembl_id: "ENSG00000065491"
name: "TBC1 domain family member 22B"
location: "6p21.2"
module: 68
arm: "+"
pooled_cpm: 42.69
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TBC1D22B

*TBC1 domain family member 22B* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +20.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.661× (z -6.9, q 4e-09, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.368×, PANC-1 0.420×, HepG2/C3A 0.290×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SNU-423 0.252×, MIA PaCa-2 0.326×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.104×, RKO 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (CHP-212 0.0658×); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (CHP-212 0.0784×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRAM1]] (+0.66, fdr 1e-05), [[DUSP16]] (+0.63, fdr 1e-05), [[RC3H2]] (+0.62, fdr 4e-05); moves opposite to [[ETV5]] (-0.62, fdr 2e-05), [[HPCAL1]] (-0.60, fdr 5e-05), [[GNAI3]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +20.2 | 0e+00 | 47/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.71×** | +16.4 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.41×** | +12.8 | 4e-35 | 44/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +12.7 | 1e-34 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +12.0 | 7e-31 | 46/47 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +11.3 | 1e-27 | 43/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +10.5 | 6e-24 | 42/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +8.4 | 4e-15 | 36/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +7.6 | 3e-12 | 34/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +6.7 | 9e-10 | 35/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.1 | 2e-05 | 23/47 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.0 | 2e-05 | 26/48 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 7e-04 | 23/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.3 | 7e-04 | 23/48 (HT-29, BT-474, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +4.2 | 8e-04 | 20/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 8e-04 | 23/47 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 9e-04 | 24/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.001 | 24/47 (HT-29, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.368×, PANC-1 0.420×, HepG2/C3A 0.290×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SNU-423 0.252×, MIA PaCa-2 0.326×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.104×, RKO 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (CHP-212 0.0658×); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (CHP-212 0.0784×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -6.9 | 4e-09 | 31/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.789×** | -4.0 | 0.022 | 24/48 (SW1417, A498, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.795×** | -3.7 | 0.047 | 19/39 (Panc 03.27, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.824× | -3.2 | 0.15 | 13/48 (A498, NCI-H2030, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | 0.827× | -3.2 | 0.15 | 22/46 (AN3 CA, RKO, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.828× | -3.2 | 0.15 | 17/47 (NCI-H460, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.5 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HOP62 (line)]] | alt | 34.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.85× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 32.3 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.06× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 33.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 61.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 55.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 33.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 54.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 40.9 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +13.8) | — |
| [[LoVo (line)]] | wt | 39.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 75.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 64.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.7) | [[Auranofin (drug)]] 5 µM 0.252× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 34.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.8) | — |
| [[CFPAC-1 (line)]] | alt | 43.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +18.6) | — |
| [[NCI-H23 (line)]] | alt | 52.8 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 67.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.3) | — |
| [[A-172 (line)]] | wt | 26.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +16.1) | — |
| [[A498 (line)]] | wt | 53.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.8) | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 2 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0658× (z -10.7) |
| [[H4 (line)]] | wt | 24.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Docetaxel (drug)]] 0.05 µM 0.173× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HEC-1-A (line)]] | alt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.4) | — |
| [[J82 (line)]] | alt | 38.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 41.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.326× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 80.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.8) | — |
| [[RKO (line)]] | wt | 41.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[SW 900 (line)]] | alt | 39.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) | — |
| [[A549 (line)]] | wt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.5) | — |
| [[AN3 CA (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.245× (z -9.4) |
| [[HS-578T (line)]] | alt | 39.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.2) | — |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM1]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[DUSP16]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[RC3H2]] | +0.62 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[MR1]] | +0.60 | +0.63 / +0.25 | both halves | 4e-04 |  |
| [[UNK]] | +0.58 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[ZDHHC1]] | +0.58 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[TTC32]] | +0.58 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[PATL2]] | +0.58 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[LGALSL-DT]] | +0.58 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[LINC00944]] | +0.58 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[KMO]] | +0.58 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[SLC9A8]] | +0.57 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETV5]] | -0.62 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[HPCAL1]] | -0.60 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[GNAI3]] | -0.59 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[HK1]] | -0.58 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RNF168]] | -0.57 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TNIK]] | -0.55 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[SPTLC2]] | -0.55 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[ZNF511]] | -0.54 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[EIF4EBP1]] | -0.53 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[NCKAP5L]] | -0.53 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | -0.53 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[ERRFI1]] | -0.53 | -0.58 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.3, 9.9); signed map (42.3, -3.8). **Vector** length 81.7, 20.3% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +12.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +3.9 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -6.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.1 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.0 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 22B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,257,772-37,332,970 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20337, dJ744I24.2; previously C6orf197 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NU19](https://www.uniprot.org/uniprotkb/Q9NU19) (TBC1 domain family member 22B):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [55633](https://www.ncbi.nlm.nih.gov/gene/55633):

> Enables 14-3-3 protein binding activity. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21602) · Entrez [55633](https://www.ncbi.nlm.nih.gov/gene/55633) · UniProt [Q9NU19](https://www.uniprot.org/uniprotkb/Q9NU19) · Ensembl [ENSG00000065491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065491)

## Data

Gene col 789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 789); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 789]; `tensor/DDL_lfc|DDL_z.npy` [789]; `embed/gene_vectors.npy` [789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 789 or target_col == 789). Every well: [[TBC1D22B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D22B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
