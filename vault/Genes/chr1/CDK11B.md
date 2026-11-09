---
symbol: "CDK11B"
type: "gene"
col: 14532
ensembl_id: "ENSG00000248333"
name: "cyclin dependent kinase 11B"
location: "1p36.33"
module: 11
arm: "+"
pooled_cpm: 45.97
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CDK11B

*cyclin dependent kinase 11B* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (18 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.11× (z +17.4, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.843× (z -10.8, q 2e-24, down in 16 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.702× (z -8.8, q 3e-16, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK11A]] (+0.90, fdr 7e-06, ⚠ same locus), [[ZC3H18]] (+0.76, fdr 7e-06), [[L3MBTL2]] (+0.60, fdr 7e-06), [[LSG1]] (+0.60, fdr 7e-06); moves opposite to [[LTA4H]] (-0.62, fdr 7e-06), [[TRIM36]] (-0.54, fdr 4e-05), [[SLC25A30]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.11×** | +17.4 | 0e+00 | 47/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +13.9 | 1e-41 | 44/48 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.63×** | +12.3 | 2e-32 | 42/48 (NCI-H1792, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.53×** | +12.1 | 9e-32 | 42/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +9.7 | 4e-20 | 44/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.63×** | +9.0 | 2e-17 | 39/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.62×** | +8.9 | 4e-17 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.52×** | +7.7 | 9e-13 | 36/48 (COLO 205, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +7.5 | 3e-12 | 37/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.5 | 3e-12 | 35/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +7.2 | 3e-11 | 40/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.46×** | +6.9 | 2e-10 | 31/48 (CFPAC-1, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.46×** | +6.7 | 7e-10 | 33/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.42×** | +6.4 | 6e-09 | 31/47 (SW480, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.4 | 6e-09 | 28/47 (Hs 766T, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 4e-05 | 28/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Oxaliplatin (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.041 | 7/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.057 | 11/48 (HCT15, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.063 | 9/48 (HT-29, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.843× | -10.8 | 2e-24 | 16/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.702×** | -8.8 | 3e-16 | 44/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.656×** | -7.8 | 2e-12 | 42/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.856× | -4.0 | 0.011 | 20/48 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.079 | 14/48 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.840× | -3.2 | 0.12 | 16/48 (H4, KATO III, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.786× | -3.2 | 0.12 | 9/48 (NCI-H2347, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.833× | -3.1 | 0.12 | 12/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.844× | -3.0 | 0.15 | 14/47 (AsPC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.845× | -3.0 | 0.15 | 17/47 (NCI-H23, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 63.5 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.47× (z +11.2) | — |
| [[SW480 (line)]] | alt | 49.2 | 7 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 40.9 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 8.13× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 29.0 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.17× (z +10.0) | — |
| [[RKO (line)]] | wt | 49.2 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.05× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 44.2 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.94× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 47.2 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 7.43× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.98× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.479× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 54.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.74× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.446× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 36.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.83× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0615× (z -9.9) |
| [[H4 (line)]] | wt | 52.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.4× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.65× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 48.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.78× (z +10.2) | — |
| [[KATO III (line)]] | alt | 37.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.41× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 55.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.20× (z +9.9) | — |
| [[A549 (line)]] | wt | 33.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[C32 (line)]] | wt | 42.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[COLO 205 (line)]] | alt | 49.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.5× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 52.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.01× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 51.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.67× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.74× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.38× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 77.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.49× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 44.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.89× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK11A]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Centrosome maturation; STRING 416; ⚠ same locus (43.4 kb, same strand: neighbours can correlate without regulation) |
| [[ZC3H18]] | +0.76 | +0.82 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[L3MBTL2]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LSG1]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NOM1]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[PPP6C]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PHF5A]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[GON4L]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[FBXL18]] | +0.57 | +0.64 / +0.49 | both halves | 1e-05 | pathway: G2/M Transition |
| [[TFCP2]] | +0.57 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[GLYR1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[SUPT6H]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTA4H]] | -0.62 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[TRIM36]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SLC25A30]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ATP6V1B2]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[NOTCH2NLR]] | -0.50 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ARL15]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[USP3]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LNX2]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZNF706]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZNF280C]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TEC]] | -0.48 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[ATP11B]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.203). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.4, 1.8); signed map (-4.2, -16.9). **Vector** length 94.0, 24.9% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +13.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +4.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.9 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 11B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,635,225-1,659,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDK11-p110, CDK11-p58, CDK11-p46; previously CDC2L1 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Reactome | 6 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; G2/M Transition |
| Matched by | ensembl_id |

**Function**, from UniProt [P21127](https://www.uniprot.org/uniprotkb/P21127) (Cyclin-dependent kinase 11B):

> Cyclin-dependent protein kinase that acts as a regulator of transcription and pre-mRNA splicing. Acts as a key regulator of pre-mRNA splicing by mediating phosphorylation of SF3B1, enabling the association between SF3B1 and U5 and U6 snRNAs in the activated spliceosome, thereby promoting spliceosome assembly. Also acts as a regulator of transcription by phosphorylating 'Ser-2' of the CTD (C-terminal domain) of the large subunit of RNA polymerase II (RNAP II) POLR2A. Involved in …

**Summary**, from NCBI Gene [984](https://www.ncbi.nlm.nih.gov/gene/984):

> This gene encodes a member of the serine/threonine protein kinase family. Members of this kinase family are known to be essential for eukaryotic cell cycle control. Due to a segmental duplication, this gene shares very high sequence identity with a neighboring gene. These two genes are frequently deleted or altered in neuroblastoma. The protein kinase encoded by this gene can be cleaved by caspases and may play a role in cell apoptosis. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:1729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1729) · Entrez [984](https://www.ncbi.nlm.nih.gov/gene/984) · UniProt [P21127](https://www.uniprot.org/uniprotkb/P21127) · Ensembl [ENSG00000248333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248333)

## Data

Gene col 14532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14532); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14532]; `tensor/DDL_lfc|DDL_z.npy` [14532]; `embed/gene_vectors.npy` [14532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14532 or target_col == 14532). Every well: [[CDK11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
