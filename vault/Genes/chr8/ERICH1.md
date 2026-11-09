---
symbol: "ERICH1"
type: "gene"
col: 2486
ensembl_id: "ENSG00000104714"
name: "glutamate rich 1"
location: "8p23.3"
module: 172
arm: "+"
pooled_cpm: 69.04
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# ERICH1

*glutamate rich 1* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.77× (z +11.0, q 1e-25, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.507× (z -13.2, q 8e-37, down in 38 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.748× (z -7.9, q 3e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA15P]] (+0.63, fdr 1e-05), [[DHX34]] (+0.63, fdr 7e-06), [[NKAPD1]] (+0.63, fdr 7e-06); moves opposite to [[FSBP]] (-0.58, fdr 3e-05), [[TMEM106C]] (-0.54, fdr 3e-05), [[PCCB]] (-0.53, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +11.0 | 1e-25 | 40/47 (SHP-77, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.4 | 1e-18 | 28/47 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.4 | 2e-11 | 28/48 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.3 | 2e-05 | 27/47 (Hs 766T, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 23/47 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +4.4 | 9e-04 | 18/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 1.17× | +4.2 | 0.002 | 18/47 (AsPC-1, Hs 766T, …) | all doses, flat | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.002 | 22/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.003 | 19/48 (SW480, C-33 A, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.25×** | +4.1 | 0.003 | 20/47 (SW480, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.23×** | +4.0 | 0.004 | 24/48 (LS 180, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.22×** | +3.9 | 0.004 | 22/47 (SW480, A-172, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.009 | 19/49 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.014 | 20/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +3.5 | 0.014 | 21/46 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.014 | 14/48 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.035 | 7/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.038 | 17/47 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.038 | 16/46 (HOP62, SW480, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.038 | 17/46 (NCI-H23, C-33 A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.507×** | -13.2 | 8e-37 | 38/47 (AsPC-1, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.534×** | -12.1 | 2e-31 | 42/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.660×** | -8.0 | 2e-13 | 39/47 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -7.9 | 3e-13 | 32/47 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.684×** | -7.3 | 2e-11 | 35/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -7.0 | 3e-10 | 27/47 (MIA PaCa-2, A549, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -6.4 | 1e-08 | 29/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.742×** | -5.8 | 6e-07 | 30/48 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.766×** | -5.0 | 4e-05 | 26/46 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.774×** | -4.8 | 1e-04 | 25/47 (RKO, NCI-H23, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.823×** | -3.8 | 0.008 | 22/47 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.832×** | -3.6 | 0.017 | 21/46 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.5 | 0.017 | 0/49 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.827×** | -3.4 | 0.027 | 19/45 (A-172, A549, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.850× | -3.1 | 0.063 | 21/48 (A-172, KATO III, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 89.2 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.357× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 92.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -23.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -18.8) |
| [[RKO (line)]] | wt | 93.4 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -11.6) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.354× (z -11.2) |
| [[H4 (line)]] | wt | 85.1 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 96.0 | 4 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 4.09× (z +21.9) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.532× (z -9.0) |
| [[A-172 (line)]] | wt | 107 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 91.3 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 55.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +25.6) | — |
| [[PANC-1 (line)]] | alt | 34.3 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 79.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.544× (z -8.7) |
| [[BT-474 (line)]] | alt | 72.9 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +25.5) | [[TAK-901 (drug)]] 0.05 µM 0.354× (z -9.2) |
| [[HCT15 (line)]] | alt | 100 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.83× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.310× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.381× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 113 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.66× (z +16.9) | [[Tucidinostat (drug)]] 5 µM 0.589× (z -9.9) |
| [[HOP62 (line)]] | alt | 41.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 29.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +25.5) | — |
| [[NCI-H23 (line)]] | alt | 82.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 89.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 110 | 2 | 1 | [[Auranofin (drug)]] 5 µM 6.78× (z +16.1) | [[Harringtonine (drug)]] 0.5 µM 0.361× (z -8.6) |
| [[A549 (line)]] | wt | 81.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.317× (z -12.0) |
| [[AN3 CA (line)]] | alt | 69.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 76.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.319× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 66.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 77.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.73× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 93.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 40.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +23.8) | — |
| [[NCI-H2347 (line)]] | alt | 54.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.82× (z +15.7) | — |
| [[SHP-77 (line)]] | alt | 93.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +23.9) | — |
| [[SW 900 (line)]] | alt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +20.2) | — |
| [[A-427 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 62.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 22.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 44.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.9) | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0469× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 60.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 61.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA15P]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[DHX34]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[WDR81]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SLC38A7]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CUL4A]] | +0.58 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[AP5Z1]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TRMT1]] | +0.55 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ZNF621]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CELF6]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CAVIN4]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSBP]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TMEM106C]] | -0.54 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[PCCB]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[LSM4]] | -0.52 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TM7SF3]] | -0.51 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[MGAT4A]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SCML2]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[GGH]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SSX2IP]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[ALDH3A2]] | -0.48 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[FRRS1]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.8, 11.2); signed map (-7.5, -19.7). **Vector** length 115, 33.0% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.7 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.2 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.4 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.9 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Pimitespib (drug)]] 0.05 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | glutamate rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:614,746-738,106 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q86X53](https://www.uniprot.org/uniprotkb/Q86X53) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27234) · Entrez [157697](https://www.ncbi.nlm.nih.gov/gene/157697) · UniProt [Q86X53](https://www.uniprot.org/uniprotkb/Q86X53) · Ensembl [ENSG00000104714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104714)

## Data

Gene col 2486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2486); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2486]; `tensor/DDL_lfc|DDL_z.npy` [2486]; `embed/gene_vectors.npy` [2486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2486 or target_col == 2486). Every well: [[ERICH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERICH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
