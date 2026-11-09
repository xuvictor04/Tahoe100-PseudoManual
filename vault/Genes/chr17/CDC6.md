---
symbol: "CDC6"
type: "gene"
col: 1726
ensembl_id: "ENSG00000094804"
name: "cell division cycle 6"
location: "17q21.2"
module: 6
arm: "+"
pooled_cpm: 27.09
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDC6

*cell division cycle 6* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (31 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.18× (z +19.5, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +5.6, q 1e-06, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.666× (z -5.6, q 1e-05, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.783× (z -4.8, q 4e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.87, fdr 7e-06), [[MYBL2]] (+0.86, fdr 7e-06), [[MCM10]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 31 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 31 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **4.18×** | +19.5 | 0e+00 | 48/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **3.59×** | +17.5 | 0e+00 | 47/47 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **3.55×** | +17.3 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **1.76×** | +7.4 | 2e-11 | 31/44 (PANC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.66×** | +6.9 | 5e-10 | 28/47 (J82, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.40×** | +6.4 | 1e-08 | 25/46 (A549, J82, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.63×** | +6.4 | 2e-08 | 30/48 (J82, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.57×** | +6.2 | 5e-08 | 29/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.58×** | +6.0 | 1e-07 | 27/46 (HOP62, PANC-1, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.35×** | +5.8 | 4e-07 | 27/48 (SW480, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +5.8 | 5e-07 | 29/48 (NCI-H23, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +5.6 | 1e-06 | 25/47 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~86% of this change | **1.50×** | +5.3 | 4e-06 | 26/45 (SNU-423, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.47×** | +5.2 | 8e-06 | 21/47 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.41×** | +4.7 | 1e-04 | 23/43 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.7 | 1e-04 | 22/48 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 6e-04 | 15/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 1e-03 | 13/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.001 | 16/48 (J82, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +3.8 | 0.003 | 15/45 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.011 | 20/47 (LoVo, HOP62, …) | top dose only |  |
| [[Isocorydine (drug)]] 5 µM |  | 1.16× | +2.9 | 0.058 | 1/48 (NCI-H1573) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.065 | 7/45 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.23×** | +2.8 | 0.077 | 12/47 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +2.7 | 0.085 | 9/48 (A549, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.22×** | +2.7 | 0.090 | 9/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.666×** | -5.6 | 1e-05 | 24/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.783×** | -4.8 | 4e-04 | 22/48 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.796×** | -4.5 | 0.001 | 22/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.746×** | -4.1 | 0.007 | 20/46 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.742×** | -3.9 | 0.009 | 18/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.009 | 16/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.765×** | -3.7 | 0.014 | 19/46 (SK-MEL-2, KATO III, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.757×** | -3.7 | 0.014 | 18/47 (HEC-1-A, NCI-H23, …) | top dose only | position effect removed |
| [[palbociclib (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.015 | 14/46 (NCI-H1792, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.789×** | -3.6 | 0.015 | 17/48 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.840× | -3.4 | 0.030 | 14/48 (Hs 766T, NCI-H2030, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.719×** | -3.3 | 0.051 | 6/48 (NCI-H23, A498, …) | rises with dose | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.599×** | -3.2 | 0.051 | 16/45 (LoVo, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.799×** | -3.1 | 0.073 | 13/48 (RPMI-7951, A498, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.085 | 11/47 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.740×** | -3.0 | 0.098 | 12/48 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.098 | 14/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.37 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 51.7 | 2 (2 ⚠) | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.2) ⚠ cell-cycle shift, explains ~59% of this change | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.3) |
| [[A498 (line)]] | wt | 32.5 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.93× (z +10.6) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.255× (z -15.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 19.0 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +11.3) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[SW480 (line)]] | alt | 34.9 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +13.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A549 (line)]] | wt | 12.5 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 14.6× (z +13.1) ⚠ cell-cycle shift, explains ~62% of this change | [[Cobimetinib (drug)]] 5 µM 0.118× (z -10.1) |
| [[LoVo (line)]] | wt | 19.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.62× (z +10.0) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.397× (z -8.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HOP62 (line)]] | alt | 17.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.02× (z +10.4) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[J82 (line)]] | alt | 52.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.53× (z +11.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.99× (z +8.6) | — |
| [[KATO III (line)]] | alt | 67.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.46× (z +9.8) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.84× (z +12.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 20.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +9.9) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0867× (z -8.8) |
| [[SW1417 (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[AsPC-1 (line)]] | alt | 7.29 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.97× (z +8.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +9.0) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.186× (z -11.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[H4 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.224× (z -8.7) ⚠ cell-cycle shift, explains ~69% of this change |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -13.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +8.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.167× (z -12.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H2347 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +9.4) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A-172 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 966 |
| [[MYBL2]] | +0.86 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 691 |
| [[MCM10]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 998 |
| [[CDC45]] | +0.85 | +0.79 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 994 |
| [[E2F1]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 977 |
| [[WDR76]] | +0.84 | +0.80 / +0.87 | both halves | 7e-06 |  |
| [[MCM4]] | +0.83 | +0.85 / +0.83 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 999 |
| [[DTL]] | +0.83 | +0.79 / +0.85 | both halves | 7e-06 | STRING 963 |
| [[CLSPN]] | +0.83 | +0.79 / +0.87 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 867 |
| [[GINS2]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 705 |
| [[PCLAF]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 | STRING 524 |
| [[DSCC1]] | +0.81 | +0.72 / +0.84 | both halves | 7e-06 | STRING 654 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDC6's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises CDC6's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.29× lower at baseline in the lines without TCF19 | 0.029 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises CDC6's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 2.8% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises CDC6's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without FAM111B | 0.040 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CDC6's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without E2F8 | 0.054 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TP73]] | B | TP73 activity raises CDC6's level | lines that do not express TP73 (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without TP73 | 0.059 | ⚠ within organs, on part of the lines; also absent: SPTB, PRR36, EMID1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises CDC6's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without E2F2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises CDC6's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without TLCD3B | 0.079 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CDC6's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without CDC25A | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CLSPN]] | C | CLSPN activity raises CDC6's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without CLSPN | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CDC6's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.44× lower at baseline in the lines without E2F1, MCM3 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent genes |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises CDC6's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.88× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.865). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -44.8); signed map (-37.9, -45.2). **Vector** length 119, 36.6% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.71 to 28); *Homology Directed Repair* (reactome, mean cos +0.69 to 32).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.6 | +6.9 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.5 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.0 | +19.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +4.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -7.2 | -4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -5.8 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,287,879-40,304,657 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CDC18L |
| Hallmark sets | IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_LATE, G2M_CHECKPOINT |
| Reactome | 20 pathways, smallest: CDC6 association with the ORC:origin complex; Transcription of E2F targets under negative control by DREAM complex; G0 and Early G1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99741](https://www.uniprot.org/uniprotkb/Q99741) (DNA replication factor CDC6):

> Involved in the initiation of DNA replication. Also participates in checkpoint controls that ensure DNA replication is completed before mitosis is initiated.

**Summary**, from NCBI Gene [990](https://www.ncbi.nlm.nih.gov/gene/990):

> The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Cdc6, a protein essential for the initiation of DNA replication. This protein functions as a regulator at the early steps of DNA replication. It localizes in cell nucleus during cell cyle G1, but translocates to the cytoplasm at the start of S phase. The subcellular translocation of this protein during cell cyle is regulated through its phosphorylation by Cdks. Transcription of this protein was reported to be …

**Accessions** — [HGNC:1744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1744) · Entrez [990](https://www.ncbi.nlm.nih.gov/gene/990) · UniProt [Q99741](https://www.uniprot.org/uniprotkb/Q99741) · Ensembl [ENSG00000094804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094804)

## Data

Gene col 1726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1726); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1726]; `tensor/DDL_lfc|DDL_z.npy` [1726]; `embed/gene_vectors.npy` [1726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1726 or target_col == 1726). Every well: [[CDC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
