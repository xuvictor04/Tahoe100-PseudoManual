---
symbol: "RAD51AP1"
type: "gene"
col: 3207
ensembl_id: "ENSG00000111247"
name: "RAD51 associated protein 1"
location: "12p13.32"
module: 6
arm: "+"
pooled_cpm: 30.71
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RAD51AP1

*RAD51 associated protein 1* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +14.3, q 1e-43, up in 38 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.23× (z +3.9, q 0.003, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.573× (z -7.4, q 1e-10, down in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.690× (z -7.1, q 3e-10, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPC25]] (+0.92, fdr 7e-06), [[FANCI]] (+0.91, fdr 7e-06), [[ATAD5]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 23 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **2.88×** | +14.3 | 1e-43 | 38/41 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **2.88×** | +13.7 | 2e-40 | 30/37 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.51×** | +11.5 | 4e-28 | 36/41 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.24×** | +10.5 | 2e-23 | 37/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.65×** | +9.6 | 9e-20 | 33/45 (J82, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.94×** | +8.6 | 7e-16 | 35/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.84×** | +8.2 | 2e-14 | 37/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.67×** | +6.9 | 3e-10 | 32/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.38×** | +6.1 | 7e-08 | 29/46 (RKO, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.49×** | +5.4 | 4e-06 | 27/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.47×** | +5.2 | 1e-05 | 27/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.43×** | +4.7 | 1e-04 | 22/46 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.40×** | +4.4 | 6e-04 | 18/45 (A549, HS-578T, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +4.1 | 0.002 | 19/46 (LoVo, HS-578T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 22/46 (J82, SW480, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.018 | 14/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.069 | 8/46 (MIA PaCa-2, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.573×** | -7.4 | 1e-10 | 33/46 (LS 180, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -7.1 | 3e-10 | 36/46 (SHP-77, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.719×** | -6.3 | 5e-08 | 23/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.527×** | -6.2 | 9e-08 | 30/46 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.736×** | -5.9 | 5e-07 | 23/46 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -5.7 | 1e-06 | 23/45 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.668×** | -5.4 | 7e-06 | 26/45 (H4, LoVo, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.694×** | -4.8 | 9e-05 | 23/44 (NCI-H661, MIA PaCa-2, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.784×** | -4.7 | 2e-04 | 24/46 (A-172, A-427, …) | all doses, flat | low cells (technical?) |
| [[palbociclib (drug)]] 5 µM |  | **0.519×** | -4.6 | 2e-04 | 24/45 (SW480, HCT15, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.707×** | -4.6 | 2e-04 | 23/46 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -4.4 | 4e-04 | 23/45 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.800×** | -4.3 | 8e-04 | 27/46 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.658×** | -4.0 | 0.002 | 18/46 (SW480, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.747×** | -4.0 | 0.003 | 23/46 (SNU-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.826×** | -3.7 | 0.008 | 16/46 (LoVo, SW480, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.597×** | -3.6 | 0.008 | 16/45 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.688×** | -3.6 | 0.009 | 20/46 (Hs 766T, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.612×** | -3.5 | 0.014 | 16/45 (A-427, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.783×** | -3.3 | 0.022 | 16/46 (AN3 CA, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.025 | 16/45 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 0.847× | -3.2 | 0.031 | 16/46 (MIA PaCa-2, RPMI-7951, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.11 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 103 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.256× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -12.3) |
| [[PANC-1 (line)]] | alt | 24.3 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +12.1) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[H4 (line)]] | wt | 35.9 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.179× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.274× (z -8.7) |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.123× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 2 (2 ⚠) | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +10.5) ⚠ cell-cycle shift, explains ~55% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.167× (z -11.2) |
| [[SW480 (line)]] | alt | 71.6 | 2 (2 ⚠) | 2 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.6) ⚠ cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 26.6 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.149× (z -11.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 15.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | [[Selinexor (drug)]] 5 µM 0.107× (z -17.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 12.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.315× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 62.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LoVo (line)]] | wt | 22.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.237× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 11.1 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.5) ⚠ cell-cycle shift, explains ~50% of this change | [[Radotinib (drug)]] 0.5 µM 0.0936× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 48.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[A549 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[AN3 CA (line)]] | alt | 42.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0922× (z -10.6) |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -8.5) |
| [[HCT15 (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.5) |
| [[KATO III (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0880× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 83.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.6) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.4) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.226× (z -9.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[RKO (line)]] | wt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[SHP-77 (line)]] | alt | 33.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.370× (z -9.1) |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -9.4) |
| [[SW 900 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[AsPC-1 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPC25]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 582 |
| [[FANCI]] | +0.91 | +0.92 / +0.93 | both halves | 7e-06 | STRING 625 |
| [[ATAD5]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | STRING 442 |
| [[CENPK]] | +0.88 | +0.90 / +0.90 | both halves | 7e-06 | STRING 598 |
| [[MELK]] | +0.88 | +0.91 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 887 |
| [[ZGRF1]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[PCLAF]] | +0.88 | +0.85 / +0.89 | both halves | 7e-06 | STRING 516 |
| [[CHAF1A]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[GINS1]] | +0.87 | +0.86 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 559 |
| [[KNTC1]] | +0.86 | +0.85 / +0.87 | both halves | 7e-06 | STRING 644 |
| [[RAD54L]] | +0.86 | +0.87 / +0.87 | both halves | 7e-06 | STRING 798 |
| [[POLQ]] | +0.86 | +0.89 / +0.86 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 409 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises RAD51AP1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without E2F8 | 0.020 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RAD51AP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises RAD51AP1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without TCF19 | 0.027 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises RAD51AP1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without FAM111B | 0.029 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises RAD51AP1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without CDC25A | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises RAD51AP1's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without ZNF66 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[MYBL1]] | B | MYBL1 activity raises RAD51AP1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without MYBL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises RAD51AP1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.78× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises RAD51AP1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.95× lower at baseline in the lines without AURKB | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises RAD51AP1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises RAD51AP1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.41× lower at baseline in the lines without MCM10 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.880). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.8, -46.5); signed map (-40.2, -45.7). **Vector** length 143, 48.5% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.69 to 40); *E2F G1/S* (control, mean cos +0.67 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +7.5 | +10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +6.8 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.0 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +5.0 | +6.9 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.6 | +6.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.5 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.6 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -7.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -5.7 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | -5.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAD51 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:4,538,798-4,560,047 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIR51 |
| Hallmark sets | E2F_TARGETS |
| Reactome | 17 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B01](https://www.uniprot.org/uniprotkb/Q96B01) (RAD51-associated protein 1):

> Structure-specific DNA-binding protein involved in DNA repair by promoting RAD51-mediated homologous recombination. Acts by stimulating D-Loop formation by RAD51: specifically enhances joint molecule formation through its structure-specific DNA interaction and its interaction with RAD51. Binds single-stranded DNA (ssDNA), double-stranded DNA (dsDNA) and secondary DNA structures, such as D-loop structures: has a strong preference for branched-DNA structures that are obligatory intermediates …

**Summary**, from NCBI Gene [10635](https://www.ncbi.nlm.nih.gov/gene/10635):

> Enables DNA binding activity and RNA binding activity. Involved in DNA repair; cellular response to ionizing radiation; and positive regulation of DNA recombination. Located in chromatin and nucleus. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16956) · Entrez [10635](https://www.ncbi.nlm.nih.gov/gene/10635) · UniProt [Q96B01](https://www.uniprot.org/uniprotkb/Q96B01) · Ensembl [ENSG00000111247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111247)

## Data

Gene col 3207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3207); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3207]; `tensor/DDL_lfc|DDL_z.npy` [3207]; `embed/gene_vectors.npy` [3207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3207 or target_col == 3207). Every well: [[RAD51AP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD51AP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
