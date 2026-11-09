---
symbol: "SNHG30"
type: "gene"
col: 15544
ensembl_id: "ENSG00000267321"
name: "small nucleolar RNA host gene 30"
location: "17q12"
module: 168
arm: "+"
pooled_cpm: 18.97
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 11
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# SNHG30

*small nucleolar RNA host gene 30* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.17× (z +24.8, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.542× (z -13.3, q 2e-37, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF4]] (+0.78, fdr 7e-06), [[POM121]] (+0.73, fdr 7e-06), [[TNPO3]] (+0.71, fdr 7e-06); moves opposite to [[RTL6]] (-0.68, fdr 7e-06), [[THAP5]] (-0.67, fdr 7e-06), [[ZNF776]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +24.8 | 0e+00 | 45/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.56×** | +14.3 | 4e-44 | 42/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.58×** | +13.9 | 2e-41 | 46/47 (SW480, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **2.44×** | +13.0 | 9e-37 | 38/40 (KATO III, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.35×** | +13.0 | 9e-37 | 45/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.33×** | +12.8 | 8e-36 | 43/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.23×** | +11.8 | 5e-30 | 39/46 (SW480, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +9.3 | 1e-18 | 35/47 (NCI-H460, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +7.5 | 4e-12 | 33/48 (NCI-H2030, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.58×** | +6.9 | 3e-10 | 26/47 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.57×** | +6.9 | 3e-10 | 33/46 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +6.4 | 7e-09 | 24/43 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.52×** | +6.4 | 7e-09 | 30/45 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +5.7 | 4e-07 | 23/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.4 | 2e-06 | 22/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +4.9 | 2e-05 | 22/47 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 8e-04 | 15/47 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 14/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.002 | 15/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.002 | 14/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.003 | 10/48 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.004 | 11/48 (NCI-H460, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.005 | 12/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.017 | 12/44 (NCI-H460, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.017 | 8/48 (NCI-H2030, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.542×** | -13.3 | 2e-37 | 38/46 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -9.8 | 4e-20 | 39/46 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.622×** | -7.3 | 6e-11 | 28/46 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.625×** | -7.2 | 8e-11 | 30/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.756×** | -4.1 | 0.005 | 18/48 (HOP62, HCT15, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -4.0 | 0.007 | 18/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.836× | -3.9 | 0.007 | 13/48 (RKO, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.731×** | -3.4 | 0.040 | 13/44 (C32, RPMI-7951, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.042 | 11/47 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.808×** | -3.3 | 0.055 | 5/48 (SW 1271, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.809×** | -3.3 | 0.056 | 5/47 (COLO 205, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.073 | 8/47 (AN3 CA, HOP62, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.823× | -3.0 | 0.11 | 15/46 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.85 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.8 | 5 (4 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +16.1) | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.8) |
| [[HOP62 (line)]] | alt | 32.5 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -17.5) |
| [[A498 (line)]] | wt | 17.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.257× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 12.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +10.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 22.8 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.3) |
| [[PANC-1 (line)]] | alt | 24.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +17.3) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.0) |
| [[C32 (line)]] | wt | 19.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 16.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 16.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +11.4) | — |
| [[KATO III (line)]] | alt | 20.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0687× (z -15.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.198× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 35.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.4) |
| [[SHP-77 (line)]] | alt | 25.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.2) |
| [[A-172 (line)]] | wt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +11.4) | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -10.3) |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 7.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 9.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +13.1) | — |
| [[J82 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +17.2) | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +13.4) | — |
| [[RKO (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +9.3) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.0) |
| [[SNU-423 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +13.2) | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0938× (z -9.6) |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[POM121]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TNPO3]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[NDC1]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[IFI27L1]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SAP130]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ADPGK]] | +0.65 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[ASB7]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[MBOAT7]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTL6]] | -0.68 | -0.74 / -0.60 | both halves | 7e-06 |  |
| [[THAP5]] | -0.67 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ZNF776]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TFE3]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[SYNPO]] | -0.65 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[TIAM2]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[REPIN1]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.64 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.63 | -0.72 / -0.61 | both halves | 7e-06 |  |
| [[LZIC]] | -0.63 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[ZFHX2]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNHG30's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[L3MBTL4]] | B | L3MBTL4 activity raises SNHG30's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without L3MBTL4 | 0.069 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1 |
| [[ZFHX2]] | C | ZFHX2 activity raises SNHG30's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without ZFHX2 | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-5.2, -14.8); signed map (-43.2, 2.8). **Vector** length 104, 26.1% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.2 | +11.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.5 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +24.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.1 | +13.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -14.8 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -12.5 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 30 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q12 — chr17:35,568,050-35,574,900 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-1094M14.11; previously LINC02001 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [105371743](https://www.ncbi.nlm.nih.gov/gene/105371743):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:52836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52836) · Entrez [105371743](https://www.ncbi.nlm.nih.gov/gene/105371743) · Ensembl [ENSG00000267321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267321)

## Data

Gene col 15544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15544); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15544]; `tensor/DDL_lfc|DDL_z.npy` [15544]; `embed/gene_vectors.npy` [15544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15544 or target_col == 15544). Every well: [[SNHG30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
