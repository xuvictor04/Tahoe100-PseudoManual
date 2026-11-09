---
symbol: "FANCI"
type: "gene"
col: 6424
ensembl_id: "ENSG00000140525"
name: "FA complementation group I"
location: "15q26.1"
module: 6
arm: "+"
pooled_cpm: 89.65
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 14
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FANCI

*FA complementation group I* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.69× (z +8.7, q 2e-15, up in 33 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Irinotecan (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.3, q 8e-04, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.624× (z -11.1, q 6e-26, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPK]] (+0.95, fdr 7e-06), [[MELK]] (+0.92, fdr 7e-06), [[POLQ]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCHCR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.69×** | +8.7 | 2e-15 | 33/49 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.68×** | +8.3 | 3e-14 | 35/44 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +5.7 | 2e-06 | 33/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.43×** | +5.7 | 2e-06 | 29/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +5.5 | 4e-06 | 30/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.3 | 1e-05 | 29/50 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.36×** | +5.1 | 3e-05 | 27/47 (NCI-H23, SHP-77, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +5.0 | 5e-05 | 26/48 (J82, A549, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.36×** | +4.9 | 7e-05 | 26/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.22×** | +4.6 | 2e-04 | 26/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +4.6 | 2e-04 | 29/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.21×** | +4.5 | 4e-04 | 23/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.5 | 4e-04 | 23/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.21×** | +4.4 | 5e-04 | 21/49 (SW480, HT-29, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.3 | 8e-04 | 27/48 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 21/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.006 | 21/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.010 | 19/48 (SW480, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.018 | 18/48 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.039 | 20/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.063 | 11/48 (SW480, J82, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.624×** | -11.1 | 6e-26 | 38/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.518×** | -10.9 | 2e-25 | 45/48 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.648×** | -10.2 | 3e-22 | 37/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.696×** | -6.0 | 2e-07 | 32/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.709×** | -5.5 | 4e-06 | 32/48 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.804×** | -5.2 | 2e-05 | 29/48 (RKO, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 3e-05 | 32/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.740×** | -5.0 | 4e-05 | 29/48 (HCT15, LoVo, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.667×** | -4.8 | 9e-05 | 27/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.780×** | -4.8 | 1e-04 | 27/48 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -4.7 | 1e-04 | 27/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.758×** | -4.6 | 2e-04 | 25/49 (A498, CHP-212, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.589×** | -4.4 | 4e-04 | 28/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.765×** | -4.2 | 1e-03 | 23/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.776×** | -4.1 | 0.002 | 23/48 (HOP62, A-427, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.617×** | -4.1 | 0.002 | 23/47 (HCT15, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.796×** | -3.8 | 0.005 | 20/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.853× | -3.8 | 0.005 | 17/48 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.016 | 21/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -3.4 | 0.018 | 20/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.031 | 20/49 (A-427, HOP62, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.94 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 105 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -21.1) |
| [[A498 (line)]] | wt | 87.3 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -18.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -11.4) |
| [[H4 (line)]] | wt | 82.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -14.2) |
| [[LS 180 (line)]] | wt | 81.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.9) |
| [[KATO III (line)]] | alt | 138 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 62.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -21.5) |
| [[A-172 (line)]] | wt | 68.8 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.269× (z -13.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -8.7) |
| [[HCT15 (line)]] | alt | 178 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.7) |
| [[HT-29 (line)]] | alt | 120 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 31.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.8) |
| [[SNU-1 (line)]] | wt | 82.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -15.3) |
| [[HOP62 (line)]] | alt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.7) |
| [[NCI-H596 (line)]] | alt | 59.0 | 2 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 2.83× (z +15.1) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Methylthiouracil (drug)]] 0.05 µM 2.01× (z +10.2) | — |
| [[SW48 (line)]] | wt | 90.1 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.267× (z -9.1) |
| [[SW480 (line)]] | alt | 162 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -17.5) |
| [[AN3 CA (line)]] | alt | 140 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -9.8) |
| [[C32 (line)]] | wt | 60.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.415× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CHP-212 (line)]] | wt | 62.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.227× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 91.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -10.0) |
| [[Hs 766T (line)]] | wt | 60.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.0) |
| [[LoVo (line)]] | wt | 90.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.437× (z -11.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.444× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1792 (line)]] | alt | 49.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 74.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.397× (z -11.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0994× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.443× (z -10.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[RKO (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.506× (z -9.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW 1271 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.3) |
| [[SW1417 (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.0) |
| [[A549 (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPK]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | STRING 407 |
| [[MELK]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | STRING 615 |
| [[POLQ]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | STRING 583 |
| [[RAD51AP1]] | +0.91 | +0.92 / +0.93 | both halves | 7e-06 | STRING 625 |
| [[WDHD1]] | +0.90 | +0.87 / +0.88 | both halves | 7e-06 | STRING 519 |
| [[EXO1]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | STRING 834 |
| [[DTL]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 | STRING 689 |
| [[RAD54L]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | STRING 784 |
| [[BLM]] | +0.89 | +0.92 / +0.85 | both halves | 7e-06 | STRING 773 |
| [[ATAD5]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | STRING 605 |
| [[GINS1]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[SPC25]] | +0.88 | +0.89 / +0.86 | both halves | 7e-06 | STRING 424 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises FANCI's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without E2F8 | 0.013 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises FANCI's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.37× lower at baseline in the lines without TCF19 | 0.014 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises FANCI's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.18× lower at baseline in the lines without CDC25A | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers FANCI's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MTOR]] | B | MTOR activity raises FANCI's level | compounds that target MTOR: 4 of 8 lower it (Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 4.8% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises FANCI's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without DSCC1 | 0.013 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises FANCI's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without MCM10 | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises FANCI's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without PBK | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises FANCI's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises FANCI's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.42× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises FANCI's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.27× lower at baseline in the lines without CLSPN | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises FANCI's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCHCR1]] | C | FANCI's natural level strengthens CCHCR1's drug response | FANCI's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.36; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.924). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.9, -46.4); signed map (-39.3, -44.0). **Vector** length 166, 60.9% of its response variance represented; |z| ≥ 3 in 1,585 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.73 to 28); *DNA Replication* (reactome, mean cos +0.73 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.7 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | +5.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.5 | +5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | +5.4 | +5.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.4 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +4.1 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +3.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.5 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -12.0 | -10.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -9.8 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.3 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -7.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.7 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,243,945-89,317,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10719; previously KIAA1794 |
| Gene groups (HGNC) | FA complementation groups |
| Reactome | 4 pathways, smallest: Fanconi Anemia Pathway; TP53 Regulates Transcription of DNA Repair Genes; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVI1](https://www.uniprot.org/uniprotkb/Q9NVI1) (Fanconi anemia group I protein):

> Plays an essential role in the repair of DNA double-strand breaks by homologous recombination and in the repair of interstrand DNA cross-links (ICLs) by promoting FANCD2 monoubiquitination by FANCL and participating in recruitment to DNA repair sites. The FANCI-FANCD2 complex binds and scans double-stranded DNA (dsDNA) for DNA damage; this complex stalls at DNA junctions between double-stranded DNA and single-stranded DNA. Participates in S phase and G2 phase checkpoint activation upon DNA …

**Summary**, from NCBI Gene [55215](https://www.ncbi.nlm.nih.gov/gene/55215):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:25568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25568) · Entrez [55215](https://www.ncbi.nlm.nih.gov/gene/55215) · UniProt [Q9NVI1](https://www.uniprot.org/uniprotkb/Q9NVI1) · Ensembl [ENSG00000140525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140525)

## Data

Gene col 6424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6424); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6424]; `tensor/DDL_lfc|DDL_z.npy` [6424]; `embed/gene_vectors.npy` [6424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6424 or target_col == 6424). Every well: [[FANCI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
