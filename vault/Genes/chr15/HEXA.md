---
symbol: "HEXA"
type: "gene"
col: 13117
ensembl_id: "ENSG00000213614"
name: "hexosaminidase subunit alpha"
location: "15q23"
module: 122
arm: "+"
pooled_cpm: 47.36
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# HEXA

*hexosaminidase subunit alpha* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.02× (z +24.6, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.757× (z -8.8, q 6e-16, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPNS1]] (+0.78, fdr 7e-06), [[WASHC2C]] (+0.71, fdr 7e-06), [[ATP6V1H]] (+0.71, fdr 7e-06); moves opposite to [[ADARB1]] (-0.55, fdr 2e-05), [[ARHGAP29]] (-0.54, fdr 4e-05), [[UACA]] (-0.53, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.02×** | +24.6 | 0e+00 | 44/46 (HT-29, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +15.2 | 0e+00 | 38/46 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +11.2 | 4e-27 | 37/46 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +11.2 | 5e-27 | 33/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +9.4 | 4e-19 | 36/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +8.6 | 7e-16 | 31/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.5 | 2e-15 | 34/45 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.44×** | +8.1 | 4e-14 | 39/46 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +7.6 | 2e-12 | 30/46 (PANC-1, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +7.0 | 1e-10 | 32/46 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +6.9 | 2e-10 | 36/47 (RPMI-7951, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +5.6 | 1e-06 | 21/43 (RKO, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.5 | 2e-06 | 24/47 (A549, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.4 | 4e-04 | 19/46 (RPMI-7951, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.22×** | +4.4 | 5e-04 | 18/47 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +4.3 | 6e-04 | 18/46 (RKO, CFPAC-1, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +4.2 | 9e-04 | 7/46 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.008 | 10/47 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.009 | 12/47 (BT-474, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.033 | 4/45 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.034 | 11/46 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.040 | 15/46 (HepG2/C3A, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.757×** | -8.8 | 6e-16 | 34/46 (SW480, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -7.3 | 1e-10 | 30/46 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.726×** | -7.2 | 2e-10 | 26/46 (SW1417, KATO III, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.739×** | -6.5 | 1e-08 | 25/46 (HOP62, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.758×** | -6.2 | 7e-08 | 25/46 (SW480, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.765×** | -6.0 | 2e-07 | 27/46 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.782×** | -5.5 | 3e-06 | 21/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -4.9 | 7e-05 | 23/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.820×** | -4.5 | 5e-04 | 18/46 (C32, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **0.814×** | -4.4 | 5e-04 | 22/45 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.844× | -3.8 | 0.008 | 18/46 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.038 | 17/45 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.039 | 9/46 (MIA PaCa-2, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.861× | -3.2 | 0.052 | 15/46 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.868× | -3.2 | 0.055 | 11/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.7 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.40× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 45.8 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +15.9) | — |
| [[J82 (line)]] | alt | 49.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +12.7) | — |
| [[KATO III (line)]] | alt | 61.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.84× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.76× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 48.8 | 2 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.60× (z +15.8) | [[Tucidinostat (drug)]] 5 µM 0.566× (z -10.0) |
| [[Hs 766T (line)]] | wt | 45.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 65.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.07× (z +16.6) | — |
| [[SNU-423 (line)]] | alt | 73.4 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.63× (z +17.5) | — |
| [[SW1417 (line)]] | alt | 49.3 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.78× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -11.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 40.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.17× (z +15.6) | — |
| [[C32 (line)]] | wt | 78.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.50× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 58.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.36× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 55.1 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.57× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 62.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.12× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 94.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.46× (z +17.4) | — |
| [[SHP-77 (line)]] | alt | 47.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.20× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 54.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.54× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 79.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.78× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 47.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.39× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 35.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.07× (z +10.2) | — |
| [[A498 (line)]] | wt | 18.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 104 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.71× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 73.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +13.0) | — |
| [[H4 (line)]] | wt | 50.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 39.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 45.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.412× (z -8.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HT-29 (line)]] | alt | 54.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +22.2) | — |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.327× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~55% of this change |
| [[Panc 03.27 (line)]] | alt | 42.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.65× (z +11.4) | — |
| [[RKO (line)]] | wt | 49.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.00× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 51.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +10.3) | — |
| [[A549 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPNS1]] | +0.78 | +0.73 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[WASHC2C]] | +0.71 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[ATP6V1H]] | +0.71 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[CLN3]] | +0.70 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[ATP6V1C1]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZBTB26]] | +0.69 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[MED28]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[VPS11]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MYL6B]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[RRAGB]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HPS1]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADARB1]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ARHGAP29]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[UACA]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[SMC6]] | -0.50 | -0.29 / -0.66 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HEXA's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HEXA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.3, 14.1); signed map (-9.8, -19.3). **Vector** length 122, 33.8% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.5 | +24.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +11.5 | +11.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +7.7 | +8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.3 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.8 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +7.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Afatinib (drug)]] 5 µM |  | +4.0 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.6 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | hexosaminidase subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:72,340,924-72,376,420 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Hexosaminidases |
| Hallmark sets | HYPOXIA |
| Reactome | 15 pathways, smallest: Keratan sulfate degradation; Hyaluronan degradation; CS/DS degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P06865](https://www.uniprot.org/uniprotkb/P06865) (Beta-hexosaminidase subunit alpha):

> Hydrolyzes the non-reducing end N-acetyl-D-hexosamine and/or sulfated N-acetyl-D-hexosamine of glycoconjugates, such as the oligosaccharide moieties from proteins and neutral glycolipids, or from certain mucopolysaccharides. The isozyme S is as active as the isozyme A on the anionic bis-sulfated glycans, the chondroitin-6-sulfate trisaccharide (C6S-3), and the dermatan sulfate pentasaccharide, and the sulfated glycosphingolipid SM2. The isozyme B does not hydrolyze each of these substrates, …

**Summary**, from NCBI Gene [3073](https://www.ncbi.nlm.nih.gov/gene/3073):

> This gene encodes a member of the glycosyl hydrolase 20 family of proteins. The encoded preproprotein is proteolytically processed to generate the alpha subunit of the lysosomal enzyme beta-hexosaminidase. This enzyme, together with the cofactor GM2 activator protein, catalyzes the degradation of the ganglioside GM2, and other molecules containing terminal N-acetyl hexosamines. Mutations in this gene lead to an accumulation of GM2 ganglioside in neurons, the underlying cause of …

**Accessions** — [HGNC:4878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4878) · Entrez [3073](https://www.ncbi.nlm.nih.gov/gene/3073) · UniProt [P06865](https://www.uniprot.org/uniprotkb/P06865) · Ensembl [ENSG00000213614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213614)

## Data

Gene col 13117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13117); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13117]; `tensor/DDL_lfc|DDL_z.npy` [13117]; `embed/gene_vectors.npy` [13117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13117 or target_col == 13117). Every well: [[HEXA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEXA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
