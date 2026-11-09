---
symbol: "TRAF3IP2-AS1"
type: "gene"
col: 13820
ensembl_id: "ENSG00000231889"
name: "TRAF3IP2 antisense RNA 1"
location: "6q21"
module: 46
arm: "+"
pooled_cpm: 49.67
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# TRAF3IP2-AS1

*TRAF3IP2 antisense RNA 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.15× (z +16.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.336× (z -22.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (68 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 33 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNK]] (+0.71, fdr 1e-05), [[REV3L]] (+0.70, fdr 1e-05, ⚠ same locus), [[DNAI4]] (+0.69, fdr 2e-04), [[EFCAB2]] (+0.68, fdr 4e-05); moves opposite to [[ST6GALNAC4]] (-0.62, fdr 1e-04), [[MFSD9]] (-0.61, fdr 6e-05), [[NAPG]] (-0.59, fdr 6e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KCNK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +16.0 | 0e+00 | 44/48 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +13.9 | 3e-41 | 33/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +13.3 | 4e-38 | 38/48 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.1 | 9e-32 | 38/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +12.0 | 3e-31 | 39/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +12.0 | 5e-31 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +9.5 | 2e-19 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +7.4 | 1e-11 | 30/48 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.0 | 4e-05 | 20/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +4.7 | 2e-04 | 20/49 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 6e-04 | 22/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 21/48 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.021 | 17/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.030 | 16/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +3.3 | 0.036 | 12/49 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.093 | 8/47 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.097 | 12/48 (HEC-1-A, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.336×** | -22.8 | 0e+00 | 47/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.359×** | -21.5 | 0e+00 | 46/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.377×** | -20.4 | 0e+00 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.536×** | -13.1 | 8e-37 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.550×** | -12.5 | 6e-34 | 40/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.683×** | -7.7 | 1e-12 | 23/40 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.708×** | -7.3 | 3e-11 | 29/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.711×** | -7.1 | 7e-11 | 25/47 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.624×** | -4.8 | 1e-04 | 23/48 (SHP-77, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.7 | 1e-04 | 19/48 (PANC-1, A498, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.689×** | -3.8 | 0.008 | 14/46 (HEC-1-A, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.695×** | -3.7 | 0.011 | 15/43 (AN3 CA, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.830×** | -3.6 | 0.013 | 21/45 (NCI-H23, H4, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.845× | -3.5 | 0.017 | 19/48 (HepG2/C3A, A-172, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.712×** | -3.4 | 0.022 | 14/47 (C32, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.048 | 9/48 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.747×** | -3.0 | 0.098 | 13/48 (J82, SW 1271, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.5 | 12 (4 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.39× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.190× (z -18.7) |
| [[PANC-1 (line)]] | alt | 105 | 6 (1 ⚠) | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.87× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.266× (z -17.9) |
| [[A549 (line)]] | wt | 55.4 | 5 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.4) | [[Belinostat (drug)]] 5 µM 0.251× (z -14.9) |
| [[SHP-77 (line)]] | alt | 105 | 4 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.230× (z -16.9) |
| [[A-172 (line)]] | wt | 65.7 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -16.9) |
| [[A498 (line)]] | wt | 39.7 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.7) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 43.2 | 2 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -11.3) |
| [[A-427 (line)]] | wt | 58.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -13.3) |
| [[C-33 A (line)]] | alt | 100 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.50× (z +8.5) | [[Belinostat (drug)]] 5 µM 0.357× (z -9.7) |
| [[HOP62 (line)]] | alt | 39.7 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.335× (z -11.0) |
| [[J82 (line)]] | alt | 68.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.279× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 86.1 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 43.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.216× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 87.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.271× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.217× (z -13.7) |
| [[RKO (line)]] | wt | 79.6 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 4.28× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.239× (z -11.7) |
| [[SNU-423 (line)]] | alt | 71.8 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -11.2) |
| [[SW480 (line)]] | alt | 47.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.322× (z -12.7) |
| [[C32 (line)]] | wt | 73.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -13.1) |
| [[HS-578T (line)]] | alt | 49.8 | 1 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.38× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 67.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 57.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -11.5) |
| [[HT-29 (line)]] | alt | 30.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -8.5) |
| [[LoVo (line)]] | wt | 35.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 49.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -8.8) |
| [[SNU-1 (line)]] | wt | 51.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -10.9) |
| [[SW 900 (line)]] | alt | 37.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.40× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -8.7) |
| [[H4 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0848× (z -8.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 32 of them with an alert (⚠; 31 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | +0.71 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[REV3L]] | +0.70 | +0.54 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DNAI4]] | +0.69 | +0.52 / +0.29 | both halves | 2e-04 |  |
| [[EFCAB2]] | +0.68 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[AHI1-DT]] | +0.67 | +0.48 / +0.22 | both halves | 6e-04 |  |
| [[ACTA2]] | +0.66 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CASD1]] | +0.66 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[OXA1L-DT]] | +0.66 | +0.52 / +0.23 | both halves | 5e-04 |  |
| [[RNF146]] | +0.65 | +0.48 / +0.28 | both halves | 3e-04 |  |
| [[DRAM1]] | +0.65 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[EFCAB5]] | +0.65 | +0.44 / +0.12 | ⚠ not reproduced | 0.002 |  |
| [[GALNT7-DT]] | +0.65 | +0.41 / +0.24 | both halves | 5e-04 |  |
| [[TSTD3]] | +0.64 | +0.49 / +0.26 | both halves | 4e-04 |  |
| [[PBLD]] | +0.64 | +0.36 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.62 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[MFSD9]] | -0.61 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[NAPG]] | -0.59 | -0.57 / -0.21 | both halves | 6e-04 |  |
| [[SPTLC2]] | -0.59 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[LRFN3]] | -0.58 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[NDFIP2]] | -0.58 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[FLNB]] | -0.58 | -0.44 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[WASF3]] | -0.58 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[GDPGP1]] | -0.57 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.57 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[BCR]] | -0.57 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[LRBA]] | -0.57 | -0.40 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK1]] | B | KCNK1 activity lowers TRAF3IP2-AS1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.82× higher at baseline in the lines without KCNK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[MCTP2]] | B | MCTP2 activity lowers TRAF3IP2-AS1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.70× higher at baseline in the lines without MCTP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[PTCHD4]] | B | PTCHD4 activity raises TRAF3IP2-AS1's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.56× lower at baseline in the lines without PTCHD4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[TNIK]] | B | TNIK activity weakens TRAF3IP2-AS1's drug response | lines that do not express TNIK (11) vs lines expressing it (37) | the lines without TNIK respond 1.37× as strongly (z diff -1.65); rises at some drug-doses, falls at others (25% from rises): Belinostat 5 µM: 0.28x vs 0.44x (z diff -2.8); Panobinostat 0.5 µM: 0.28x vs 0.40x (z diff -2.3); Ouabain (Octahydrate) 5 µM: 2.46x vs 1.94x (z diff -1.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[KCNK1]] | B | KCNK1 activity weakens TRAF3IP2-AS1's drug response | lines that do not express KCNK1 (23) vs lines expressing it (25) | the lines without KCNK1 respond 1.11× as strongly (z diff -1.15); strongest at Belinostat 0.5 µM: 0.50x vs 0.60x (z diff -2.6) | 0.0998 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132; target measured in part of the lines; artifact flags |
| [[TYMSOS]] | C | TYMSOS activity raises TRAF3IP2-AS1's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without TYMSOS | 0.099 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.5, 12.4); signed map (24.7, -18.1). **Vector** length 112, 31.5% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +13.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.3 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.5 | -20.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.0 | -21.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -22.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -13.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | TRAF3IP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q21 — chr6:111,483,459-111,598,783 (+) |
| Ensembl biotype | lncRNA |
| Also known as | C6UAS, BetaFAAR; previously TRAF3IP2-AS2, C6orf3, NCRNA00248 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40005) · Entrez [643749](https://www.ncbi.nlm.nih.gov/gene/643749) · Ensembl [ENSG00000231889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231889)

## Data

Gene col 13820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13820); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13820]; `tensor/DDL_lfc|DDL_z.npy` [13820]; `embed/gene_vectors.npy` [13820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13820 or target_col == 13820). Every well: [[TRAF3IP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF3IP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
