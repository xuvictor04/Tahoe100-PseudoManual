---
symbol: "RFWD3"
type: "gene"
col: 9647
ensembl_id: "ENSG00000168411"
name: "ring finger and WD repeat domain 3"
location: "16q23.1"
module: 71
arm: "+"
pooled_cpm: 80.1
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# RFWD3

*ring finger and WD repeat domain 3* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.89× (z +12.6, q 2e-33, up in 45 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.78× (z +10.6, q 8e-24, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.797× (z -6.4, q 8e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLA2]] (+0.84, fdr 7e-06), [[DDIAS]] (+0.84, fdr 7e-06), [[CENPO]] (+0.83, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 23 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.89×** | +12.6 | 2e-33 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.82×** | +11.8 | 9e-30 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +10.6 | 8e-24 | 39/49 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.70×** | +10.5 | 1e-23 | 44/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.59×** | +9.2 | 4e-18 | 40/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.56×** | +8.4 | 3e-15 | 35/50 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.51×** | +7.9 | 3e-13 | 37/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +7.8 | 4e-13 | 31/48 (HEC-1-A, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.48×** | +7.4 | 1e-11 | 36/48 (NCI-H1792, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +6.5 | 5e-09 | 32/48 (SW480, LoVo, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.24×** | +6.0 | 9e-08 | 25/48 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +6.0 | 1e-07 | 33/48 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.9 | 1e-07 | 27/48 (LoVo, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.34×** | +5.8 | 3e-07 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.32×** | +5.5 | 2e-06 | 29/47 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.4 | 4e-04 | 20/48 (SW480, SW1417, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.061 | 9/48 (HT-29, HOP62, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -6.4 | 8e-08 | 29/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.735×** | -6.1 | 2e-07 | 26/49 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.740×** | -6.0 | 4e-07 | 28/48 (A498, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.761×** | -5.2 | 2e-05 | 28/47 (HOP62, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -5.1 | 3e-05 | 23/43 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.771×** | -5.0 | 6e-05 | 28/48 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.782×** | -4.9 | 7e-05 | 25/49 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.786×** | -4.8 | 1e-04 | 27/47 (A-427, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -4.6 | 3e-04 | 22/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.806×** | -4.3 | 9e-04 | 21/49 (A498, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.838× | -4.3 | 0.001 | 22/50 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.812×** | -4.2 | 0.002 | 20/48 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.813×** | -4.1 | 0.002 | 20/48 (SW 900, C-33 A, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.874× | -3.8 | 0.005 | 18/48 (A-427, A498, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 0.867× | -3.7 | 0.008 | 17/49 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.832×** | -3.7 | 0.008 | 18/47 (NCI-H2030, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.5 | 0.016 | 17/48 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.846× | -3.3 | 0.024 | 15/48 (LS 180, A498, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.889× | -3.3 | 0.026 | 6/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.048 | 15/48 (SK-MEL-2, A-427, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.861× | -3.0 | 0.063 | 13/48 (KATO III, SW480, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.868× | -2.8 | 0.096 | 7/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.904× | -2.8 | 0.096 | 7/48 (HOP62, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 74.2 | 8 (6 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +15.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.16× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 124 | 4 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.28× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 109 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.438× (z -8.8) |
| [[KATO III (line)]] | alt | 71.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.05× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.29× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 40.3 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[HEC-1-A (line)]] | alt | 87.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.37× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.488× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 123 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +10.2) ⚠ cell-cycle shift, explains ~42% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 185 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.429× (z -11.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 54.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.05× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.4) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[C-33 A (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.05× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +10.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SHP-77 (line)]] | alt | 154 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.36× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.141× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLA2]] | +0.84 | +0.78 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[DDIAS]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CENPO]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[POLQ]] | +0.83 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 |  |
| [[DTL]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | same gene group |
| [[ATAD5]] | +0.83 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[GINS1]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[MELK]] | +0.82 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[BLM]] | +0.81 | +0.82 / +0.87 | both halves | 7e-06 | STRING 409 |
| [[WDHD1]] | +0.81 | +0.81 / +0.83 | both halves | 7e-06 | same gene group |
| [[RAD51]] | +0.81 | +0.78 / +0.84 | both halves | 7e-06 | same gene group; STRING 749 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises RFWD3's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without E2F2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises RFWD3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without CDC25A | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[ANXA1]] | B | ANXA1 activity lowers RFWD3's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.39× higher at baseline in the lines without ANXA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[ZNF66]] | B | ZNF66 activity raises RFWD3's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without ZNF66 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[MIR924HG]] | B | MIR924HG activity lowers RFWD3's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without MIR924HG | 0.094 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[CENPP]] | C | CENPP activity raises RFWD3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CENPP | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.897). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -48.2); signed map (-41.5, -44.2). **Vector** length 124, 40.6% of its response variance represented; |z| ≥ 3 in 1,360 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metabolism of non-coding RNA* (reactome, mean cos +0.54 to 5); *snRNP Assembly* (reactome, mean cos +0.54 to 5); *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +6.1 | +7.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.7 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.9 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | +3.4 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -5.2 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | ring finger and WD repeat domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,621,399-74,666,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10520, RNF201, FANCW |
| Gene groups (HGNC) | Ring finger proteins; WD repeat domain containing; FA complementation groups; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCD5](https://www.uniprot.org/uniprotkb/Q6PCD5) (E3 ubiquitin-protein ligase RFWD3):

> E3 ubiquitin-protein ligase required for the repair of DNA interstrand cross-links (ICL) in response to DNA damage. Plays a key role in RPA-mediated DNA damage signaling and repair. Acts by mediating ubiquitination of the RPA complex (RPA1, RPA2 and RPA3 subunits) and RAD51 at stalled replication forks, leading to remove them from DNA damage sites and promote homologous recombination. Also mediates the ubiquitination of p53/TP53 in the late response to DNA damage, and acts as a positive …

**Summary**, from NCBI Gene [55159](https://www.ncbi.nlm.nih.gov/gene/55159):

> Enables MDM2/MDM4 family protein binding activity; p53 binding activity; and ubiquitin protein ligase activity. Involved in several processes, including DNA metabolic process; regulation of cell cycle phase transition; and response to ionizing radiation. Located in cytosol; nucleoplasm; and site of double-strand break. Implicated in Fanconi anemia complementation group W. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25539) · Entrez [55159](https://www.ncbi.nlm.nih.gov/gene/55159) · UniProt [Q6PCD5](https://www.uniprot.org/uniprotkb/Q6PCD5) · Ensembl [ENSG00000168411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168411)

## Data

Gene col 9647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9647); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9647]; `tensor/DDL_lfc|DDL_z.npy` [9647]; `embed/gene_vectors.npy` [9647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9647 or target_col == 9647). Every well: [[RFWD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFWD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
