---
symbol: "CDKL1"
type: "gene"
col: 1973
ensembl_id: "ENSG00000100490"
name: "cyclin dependent kinase like 1"
location: "14q21.3"
module: 38
arm: "+"
pooled_cpm: 44.55
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CDKL1

*cyclin dependent kinase like 1* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +13.9, q 2e-41, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.417× (z -18.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO10]] (+0.76, fdr 7e-06), [[EEF1AKMT1]] (+0.71, fdr 7e-06), [[IDI2-AS1]] (+0.71, fdr 7e-06); moves opposite to [[SNX1]] (-0.60, fdr 5e-05), [[FUCA1]] (-0.58, fdr 1e-05), [[PLEKHH3]] (-0.58, fdr 5e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +13.9 | 2e-41 | 33/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +13.7 | 3e-40 | 40/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +11.5 | 3e-28 | 36/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.7 | 4e-09 | 31/48 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.6 | 6e-09 | 26/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.5 | 4e-06 | 21/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +5.1 | 2e-05 | 20/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.1 | 2e-05 | 21/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.8 | 9e-05 | 20/48 (hTERT-HPNE, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.8 | 1e-04 | 19/48 (LoVo, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.4 | 5e-04 | 23/46 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.001 | 22/47 (RKO, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +4.2 | 0.001 | 17/48 (NCI-H2347, SK-MEL-2, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 14/48 (A-172, A549, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.0 | 0.002 | 12/34 (NCI-H1792, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.003 | 17/47 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.008 | 11/48 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.5 | 0.012 | 9/47 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.022 | 9/48 (SW480, SW 900, …) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.086 | 9/47 (A-172, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.417×** | -18.0 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -17.5 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.488×** | -14.8 | 0e+00 | 43/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -6.9 | 5e-10 | 26/47 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.759×** | -5.7 | 1e-06 | 23/45 (HOP62, CHP-212, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.775×** | -5.3 | 1e-05 | 22/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.769×** | -5.2 | 2e-05 | 22/40 (SW480, SHP-77, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.621×** | -5.1 | 2e-05 | 21/47 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.791×** | -4.8 | 8e-05 | 25/47 (SK-MEL-2, LoVo, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.791×** | -4.7 | 2e-04 | 21/48 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.800×** | -4.6 | 2e-04 | 20/48 (C-33 A, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.794×** | -4.6 | 2e-04 | 20/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.859× | -4.4 | 4e-04 | 22/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.871× | -4.0 | 0.002 | 13/48 (A-172, H4, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.796×** | -4.0 | 0.003 | 15/48 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.695×** | -3.9 | 0.003 | 18/47 (SK-MEL-2, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.827×** | -3.8 | 0.005 | 11/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift |
| [[Brivudine (drug)]] 5 µM |  | **0.708×** | -3.7 | 0.006 | 13/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.810×** | -3.7 | 0.008 | 14/47 (RKO, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.889× | -3.4 | 0.017 | 11/48 (HEC-1-A, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 74.7 | 4 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +23.6) | [[Panobinostat (drug)]] 5 µM 0.236× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 67.8 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -15.7) |
| [[SW480 (line)]] | alt | 56.0 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.190× (z -21.3) |
| [[COLO 205 (line)]] | alt | 40.0 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[RKO (line)]] | wt | 77.8 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.84× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[NCI-H460 (line)]] | wt | 42.6 | 4 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 5.90× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -8.7) |
| [[A-427 (line)]] | wt | 37.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -9.4) |
| [[A549 (line)]] | wt | 46.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +8.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.232× (z -14.2) |
| [[PANC-1 (line)]] | alt | 28.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -12.8) |
| [[A498 (line)]] | wt | 36.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -11.0) |
| [[C-33 A (line)]] | alt | 78.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 51.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -11.7) |
| [[HOP62 (line)]] | alt | 105 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 70.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 75.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.74× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 35.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 45.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.330× (z -9.1) |
| [[SW48 (line)]] | wt | 66.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 45.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0956× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.232× (z -9.1) |
| [[Hs 766T (line)]] | wt | 27.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.5) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.264× (z -9.8) |
| [[KATO III (line)]] | alt | 22.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.83× (z +11.1) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.315× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.98× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.35× (z +10.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[LOX-IMVI (line)]] | wt | 42.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H23 (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.8) | — |
| [[A-172 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO10]] | +0.76 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[EEF1AKMT1]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.71 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.71 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[MSH4]] | +0.70 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ARL9]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SNHG26]] | +0.69 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.68 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[LINC01355]] | +0.68 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CDKL4]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 | same gene group; STRING 791 |
| [[SCUBE2]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX1]] | -0.60 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[FUCA1]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.58 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[ALAD]] | -0.56 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[BAG4]] | -0.56 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[FAM234A]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.2, -12.7); signed map (16.9, 4.7). **Vector** length 122, 32.6% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.3 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.7 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -17.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -14.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -18.0 |
|  | [[NG25 (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -3.2 | -4.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.2 | -3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:50,326,265-50,416,461 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KKIALRE |
| Gene groups (HGNC) | Cyclin dependent kinase like family |
| Matched by | ensembl_id |

UniProt [Q00532](https://www.uniprot.org/uniprotkb/Q00532) carries no function annotation.

**Summary**, from NCBI Gene [8814](https://www.ncbi.nlm.nih.gov/gene/8814):

> This gene product is a member of a large family of CDC2-related serine/threonine protein kinases that accumulates primarily in the nucleus. [provided by RefSeq, Nov 2018]

**Accessions** — [HGNC:1781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1781) · Entrez [8814](https://www.ncbi.nlm.nih.gov/gene/8814) · UniProt [Q00532](https://www.uniprot.org/uniprotkb/Q00532) · Ensembl [ENSG00000100490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100490)

## Data

Gene col 1973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1973); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1973]; `tensor/DDL_lfc|DDL_z.npy` [1973]; `embed/gene_vectors.npy` [1973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1973 or target_col == 1973). Every well: [[CDKL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
