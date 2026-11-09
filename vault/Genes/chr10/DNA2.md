---
symbol: "DNA2"
type: "gene"
col: 6156
ensembl_id: "ENSG00000138346"
name: "DNA replication helicase/nuclease 2"
location: "10q21.3"
module: 6
arm: "+"
pooled_cpm: 33.23
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DNA2

*DNA replication helicase/nuclease 2* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (22 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +13.5, q 2e-38, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~87% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM: 1.31× (z +4.9, q 3e-05, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.704× (z -6.5, q 4e-08, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.555× (z -5.7, q 3e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRIP1]] (+0.87, fdr 7e-06), [[GINS1]] (+0.86, fdr 7e-06), [[ATAD5]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 27 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **2.07×** | +13.5 | 2e-38 | 39/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.83×** | +11.2 | 2e-26 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.82×** | +10.6 | 4e-24 | 36/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.67×** | +9.1 | 2e-17 | 23/38 (LoVo, C32, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.59×** | +8.2 | 3e-14 | 34/47 (PANC-1, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +8.1 | 6e-14 | 30/48 (A549, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.53×** | +7.9 | 3e-13 | 27/44 (RKO, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.55×** | +7.8 | 6e-13 | 36/48 (SW480, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +6.7 | 2e-09 | 32/47 (A549, HT-29, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +6.0 | 1e-07 | 25/48 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.40×** | +5.9 | 2e-07 | 25/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.39×** | +5.9 | 2e-07 | 22/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.9 | 2e-07 | 22/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +5.8 | 2e-07 | 22/47 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.37×** | +5.8 | 3e-07 | 25/47 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 3e-05 | 19/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 5e-05 | 18/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.6 | 1e-04 | 18/48 (SW480, KATO III, …) | top dose only | plate-row cell shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 5e-04 | 12/47 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.002 | 10/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.002 | 11/47 (LS 180, SW480, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.004 | 13/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.014 | 14/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.015 | 14/47 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Methotrexate (drug)]] 5 µM |  | 1.19× | +3.2 | 0.020 | 7/48 (HOP62, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.035 | 11/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.17× | +2.8 | 0.064 | 6/45 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +2.7 | 0.089 | 12/48 (A549, SW480, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.16× | +2.7 | 0.096 | 9/48 (HOP62, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6156.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.704×** | -6.5 | 4e-08 | 26/48 (A-427, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -5.7 | 3e-06 | 25/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.814×** | -5.4 | 1e-05 | 26/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.831×** | -4.9 | 2e-04 | 21/48 (KATO III, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.619×** | -4.7 | 3e-04 | 20/47 (HS-578T, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.780×** | -4.6 | 3e-04 | 18/47 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.843× | -4.5 | 5e-04 | 18/48 (A-172, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -4.4 | 7e-04 | 14/48 (LS 180, KATO III, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.718×** | -4.4 | 7e-04 | 15/48 (SW480, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.697×** | -3.5 | 0.022 | 15/45 (AN3 CA, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.769×** | -3.5 | 0.022 | 13/48 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.769×** | -3.5 | 0.022 | 14/48 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.048 | 16/47 (RKO, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.2 | 0.048 | 16/48 (A-427, AN3 CA, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.833× | -3.2 | 0.049 | 14/48 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 0.846× | -3.1 | 0.061 | 10/47 (hTERT-HPNE, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.061 | 13/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 0.841× | -3.0 | 0.088 | 8/47 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | 0.895× | -2.9 | 0.095 | 2/48 (COLO 205, Panc 03.27) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.01 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 66.6 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -12.4) |
| [[A-172 (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.140× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 22.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.0904× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 3.40× (z +8.9) ⚠ cell-cycle shift, explains ~58% of this change | [[AZD2858 (drug)]] 0.5 µM 0.110× (z -11.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 47.1 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.33× (z +9.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SW480 (line)]] | alt | 65.1 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.99× (z +12.6) ⚠ toxic; cell-cycle shift, explains ~59% of this change | — |
| [[A498 (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[AN3 CA (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -10.2) ⚠ cell-cycle shift, explains ~81% of this change |
| [[C-33 A (line)]] | alt | 97.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.395× (z -8.6) |
| [[COLO 205 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 31.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +9.2) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.358× (z -9.0) ⚠ cell-cycle shift, explains ~13% of this change |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIP1]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 882 |
| [[GINS1]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | pathway: DNA Replication; STRING 431 |
| [[ATAD5]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | STRING 812 |
| [[EXO1]] | +0.85 | +0.78 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 998 |
| [[WDHD1]] | +0.85 | +0.80 / +0.88 | both halves | 7e-06 | STRING 997 |
| [[CDC45]] | +0.85 | +0.76 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 791 |
| [[CENPK]] | +0.85 | +0.80 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[WDR76]] | +0.85 | +0.77 / +0.87 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.84 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[FANCI]] | +0.84 | +0.76 / +0.86 | both halves | 7e-06 | STRING 616 |
| [[FANCA]] | +0.84 | +0.75 / +0.89 | both halves | 7e-06 | STRING 657 |
| [[CLSPN]] | +0.83 | +0.79 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 639 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises DNA2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without E2F2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises DNA2's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without TLCD3B | 0.032 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers DNA2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TERT]] | B | TERT activity raises DNA2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without TERT | 0.053 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[CDC25A]] | B | CDC25A activity raises DNA2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without CDC25A | 0.0998 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.862). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.6, -46.2); signed map (-39.3, -44.9). **Vector** length 123, 35.1% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *E2F G1/S* (control, mean cos +0.69 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.72 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +7.2 | +11.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.5 | +5.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.2 | +5.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +3.9 | +5.9 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.9 | +6.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.4 | +4.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +3.3 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +4.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -7.4 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.8 | -6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.3 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA replication helicase/nuclease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,414,064-68,472,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0083; previously DNA2L |
| Gene groups (HGNC) | UPF1 like RNA helicases |
| Reactome | 42 pathways, smallest: Removal of the Flap Intermediate; Processive synthesis on the lagging strand; Removal of the Flap Intermediate from the C-strand |
| Matched by | ensembl_id |

**Function**, from UniProt [P51530](https://www.uniprot.org/uniprotkb/P51530) (DNA replication ATP-dependent helicase/nuclease DNA2):

> Key enzyme involved in DNA replication and DNA repair in nucleus and mitochondrion. Involved in Okazaki fragments processing by cleaving long flaps that escape FEN1: flaps that are longer than 27 nucleotides are coated by replication protein A complex (RPA), leading to recruit DNA2 which cleaves the flap until it is too short to bind RPA and becomes a substrate for FEN1. Also involved in 5'-end resection of DNA during double-strand break (DSB) repair: recruited by BLM and mediates the cleavage …

**Summary**, from NCBI Gene [1763](https://www.ncbi.nlm.nih.gov/gene/1763):

> This gene encodes a member of the DNA2/NAM7 helicase family. The encoded protein is a conserved helicase/nuclease involved in the maintenance of mitochondrial and nuclear DNA stability. Mutations in this gene are associated with autosomal dominant progressive external ophthalmoplegia-6 (PEOA6) and Seckel syndrome 8. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:2939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2939) · Entrez [1763](https://www.ncbi.nlm.nih.gov/gene/1763) · UniProt [P51530](https://www.uniprot.org/uniprotkb/P51530) · Ensembl [ENSG00000138346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138346)

## Data

Gene col 6156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6156); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6156]; `tensor/DDL_lfc|DDL_z.npy` [6156]; `embed/gene_vectors.npy` [6156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6156 or target_col == 6156). Every well: [[DNA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
