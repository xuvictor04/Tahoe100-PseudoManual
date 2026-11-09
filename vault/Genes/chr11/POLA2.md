---
symbol: "POLA2"
type: "gene"
col: 284
ensembl_id: "ENSG00000014138"
name: "DNA polymerase alpha 2, accessory subunit"
location: "11q13.1"
module: 6
arm: "+"
pooled_cpm: 22.52
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 27
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLA2

*DNA polymerase alpha 2, accessory subunit* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (21 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.01× (z +11.9, q 5e-30, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.699× (z -9.0, q 1e-16, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GINS1]] (+0.85, fdr 7e-06), [[RFWD3]] (+0.84, fdr 7e-06), [[DTL]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 25 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +11.9 | 5e-30 | 33/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.40×** | +8.4 | 1e-14 | 22/46 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +8.3 | 1e-14 | 27/47 (A549, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.63×** | +8.3 | 1e-14 | 27/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.59×** | +8.3 | 2e-14 | 32/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.8 | 4e-13 | 24/47 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +6.5 | 5e-09 | 24/47 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +6.4 | 1e-08 | 23/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.42×** | +6.0 | 1e-07 | 25/47 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.38×** | +5.7 | 7e-07 | 19/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +5.5 | 2e-06 | 22/48 (SW480, SW1417, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.25×** | +5.5 | 2e-06 | 17/48 (SW480, HT-29, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.37×** | +5.4 | 3e-06 | 19/46 (SW480, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 18/47 (HOP62, SW 900, …) | two highest doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.31×** | +4.8 | 7e-05 | 11/48 (RKO, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 6e-04 | 14/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 13/47 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.001 | 17/47 (BT-474, A549, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.003 | 13/47 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Gemcitabine (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.010 | 0/46 | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.010 | 12/45 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.012 | 9/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.013 | 8/47 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.018 | 4/48 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.2 | 0.022 | 13/48 (SW480, A-427, …) | rises with dose |  |
| [[Oxaliplatin (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.034 | 3/48 (HOP62, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Olanzapine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.034 | 6/48 (HS-578T, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.699×** | -9.0 | 1e-16 | 28/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.685×** | -6.7 | 5e-09 | 26/47 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.724×** | -5.8 | 2e-06 | 24/47 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.802×** | -5.6 | 4e-06 | 24/48 (A-172, SNU-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.773×** | -5.4 | 7e-06 | 19/48 (A-427, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.757×** | -5.0 | 6e-05 | 13/48 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.757×** | -5.0 | 6e-05 | 17/47 (SW480, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.770×** | -4.7 | 2e-04 | 17/46 (HCT15, HT-29, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.837× | -4.5 | 4e-04 | 17/48 (NCI-H2030, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.719×** | -4.2 | 0.002 | 9/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.797×** | -3.9 | 0.005 | 17/47 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.801×** | -3.8 | 0.007 | 12/48 (A-427, H4, …) | two highest doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.862× | -3.7 | 0.008 | 12/48 (A-427, CFPAC-1, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.629×** | -3.7 | 0.008 | 7/46 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.008 | 10/48 (SW480, CHP-212, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.748×** | -3.7 | 0.008 | 10/46 (SW480, HT-29, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.6 | 0.009 | 14/48 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.010 | 10/47 (A-427, RPMI-7951, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.012 | 5/48 (HOP62, A498, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.824×** | -3.4 | 0.016 | 9/47 (AN3 CA, A-427, …) | two highest doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.017 | 10/48 (SW48, SNU-1, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.017 | 7/48 (SW480, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.03 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 60.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 34.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +23.7) | — |
| [[SW480 (line)]] | alt | 34.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.66× (z +8.9) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 45.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -10.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.377× (z -10.5) |
| [[A498 (line)]] | wt | 25.1 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.353× (z -11.5) |
| [[A549 (line)]] | wt | 12.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 12.7 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.57× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 22.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.375× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 12.2 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0559× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.171× (z -8.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 8.87 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +10.2) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H2347 (line)]] | alt | 7.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.123× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GINS1]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 671 |
| [[RFWD3]] | +0.84 | +0.78 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.82 | +0.77 / +0.84 | both halves | 7e-06 | STRING 412 |
| [[WDHD1]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 | STRING 764 |
| [[ATAD5]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 | STRING 609 |
| [[BRIP1]] | +0.81 | +0.78 / +0.83 | both halves | 7e-06 |  |
| [[MCM10]] | +0.81 | +0.78 / +0.83 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 833 |
| [[CDC45]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 909 |
| [[CHAF1A]] | +0.79 | +0.77 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 535 |
| [[DNA2]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 730 |
| [[POLQ]] | +0.79 | +0.77 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIF24]] | +0.79 | +0.70 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers POLA2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TLCD3B]] | B | TLCD3B activity raises POLA2's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without TLCD3B | 0.078 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.6, -47.9); signed map (-41.3, -44.8). **Vector** length 124, 34.3% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.63 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.66 to 45); *Activation of ATR in response to replication stress* (reactome, mean cos +0.68 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.7 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +11.9 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +4.3 | +5.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.3 | +5.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +4.0 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +4.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +3.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.6 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +3.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.9 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.9 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.6 | -4.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.9 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase alpha 2, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,261,913-65,305,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21662 |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 26 pathways, smallest: DNA replication initiation; Inhibition of replication initiation of damaged DNA by RB1/E2F1; Telomere C-strand synthesis initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14181](https://www.uniprot.org/uniprotkb/Q14181) (DNA polymerase alpha subunit B):

> Accessory subunit of the DNA polymerase alpha complex (also known as the alpha DNA polymerase-primase complex) which plays an essential role in the initiation of DNA synthesis. During the S phase of the cell cycle, the DNA polymerase alpha complex (composed of a catalytic subunit POLA1, an accessory subunit POLA2 and two primase subunits, the catalytic subunit PRIM1 and the regulatory subunit PRIM2) is recruited to DNA at the replicative forks via direct interactions with MCM10 and WDHD1 (By …

**Summary**, from NCBI Gene [23649](https://www.ncbi.nlm.nih.gov/gene/23649):

> Predicted to enable DNA binding activity. Involved in DNA replication initiation and DNA replication, synthesis of primer. Located in nucleoplasm. Part of alpha DNA polymerase:primase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30073) · Entrez [23649](https://www.ncbi.nlm.nih.gov/gene/23649) · UniProt [Q14181](https://www.uniprot.org/uniprotkb/Q14181) · Ensembl [ENSG00000014138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014138)

## Data

Gene col 284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 284); `tables/drug_effects.parquet` (89 rows, flagged included); `relations/gene_relations.parquet` (col_a == 284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 284]; `tensor/DDL_lfc|DDL_z.npy` [284]; `embed/gene_vectors.npy` [284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 284 or target_col == 284). Every well: [[POLA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
