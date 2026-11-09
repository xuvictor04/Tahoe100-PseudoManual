---
symbol: "GABBR1"
type: "gene"
col: 12912
ensembl_id: "ENSG00000204681"
name: "gamma-aminobutyric acid type B receptor subunit 1"
location: "6p22.1"
module: 57
arm: "-"
pooled_cpm: 38.21
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# GABBR1

*gamma-aminobutyric acid type B receptor subunit 1* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +10.3, q 5e-22, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.647× (z -7.9, q 2e-12, down in 26 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.513× (z -6.8, q 2e-09, down in 24 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.118×, A-427 0.233×, hTERT-HPNE 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.229×, SHP-77 0.127×, RPMI-7951 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.240×, A-172 0.354×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (LOX-IMVI 0.125×); [[Harringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.327×); [[Budesonide (drug)]] 0.5 µM in 1 line (NCI-H1573 0.389×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT3]] (+0.58, fdr 3e-05), [[STX11]] (+0.56, fdr 3e-05), [[ELFN1]] (+0.54, fdr 3e-05); moves opposite to [[LONP2]] (-0.56, fdr 1e-05), [[SEPTIN7P14]] (-0.53, fdr 4e-05), [[SNRPC]] (-0.48, fdr 3e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CX3CL1]] → it (grade B ⚠); 5 go from it, the strongest it → [[ALG5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +10.3 | 5e-22 | 31/41 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +8.5 | 7e-15 | 32/41 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.4 | 3e-08 | 23/41 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +5.0 | 6e-05 | 20/41 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.9 | 1e-04 | 20/41 (BT-474, J82, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +4.7 | 2e-04 | 20/40 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.3 | 0.001 | 1/41 (SW 1271) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.002 | 19/40 (CFPAC-1, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +4.2 | 0.002 | 17/41 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.008 | 12/41 (CFPAC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.012 | 13/40 (NCI-H2030, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +3.7 | 0.012 | 12/41 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.014 | 13/41 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Hydroxyurea (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.021 | 11/41 (A-172, NCI-H460, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.034 | 8/40 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.041 | 3/41 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.044 | 7/41 (HOP62, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.046 | 10/41 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.076 | 10/41 (CFPAC-1, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12912.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.118×, A-427 0.233×, hTERT-HPNE 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.229×, SHP-77 0.127×, RPMI-7951 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.240×, A-172 0.354×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (LOX-IMVI 0.125×); [[Harringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.327×); [[Budesonide (drug)]] 0.5 µM in 1 line (NCI-H1573 0.389×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.647×** | -7.9 | 2e-12 | 26/39 (SK-MEL-2, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.672×** | -7.8 | 2e-12 | 23/41 (SK-MEL-2, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -6.8 | 2e-09 | 24/41 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -5.0 | 7e-05 | 19/41 (SW480, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -4.6 | 4e-04 | 20/41 (LOX-IMVI, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.789×** | -4.4 | 8e-04 | 19/41 (J82, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.807×** | -4.0 | 0.004 | 18/36 (SK-MEL-2, A-427, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.675×** | -4.0 | 0.004 | 17/40 (MIA PaCa-2, A549, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.837× | -3.5 | 0.031 | 14/41 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | 0.839× | -3.3 | 0.055 | 18/40 (C32, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.088 | 16/41 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.855× | -3.1 | 0.10 | 7/41 (SNU-423, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 93.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.125× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 96.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 54.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.52× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H2347 (line)]] | alt | 18.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.05× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 24.1 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.89× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 40.3 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.57× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 99.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.78× (z +11.0) | [[Lonafarnib (drug)]] 5 µM 0.109× (z -9.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 37.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.28× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 40.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.27× (z +12.3) | — |
| [[J82 (line)]] | alt | 53.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[A-427 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~70% of this change |
| [[HepG2_C3A (line)]] | wt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 42.9 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.389× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0685× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 41.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.32× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 32.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 24.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.97× (z +9.2) | — |
| [[A498 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT3]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[STX11]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ELFN1]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[NFATC1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[DENND5A]] | +0.54 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[OLFM2]] | +0.53 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[UST]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZBTB46]] | +0.52 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ERF]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ARHGEF40]] | +0.51 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[EBF4]] | +0.51 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[PTCHD1]] | +0.50 | +0.29 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LONP2]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SNRPC]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TSN]] | -0.46 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[OXNAD1]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ALG5]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ANAPC10]] | -0.44 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[MIGA1]] | -0.44 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TIMM21]] | -0.44 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TOPBP1]] | -0.44 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TMED10]] | -0.43 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[SLC25A14]] | -0.43 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CX3CL1]] | B | CX3CL1 activity strengthens GABBR1's drug response | lines that do not express CX3CL1 (24) vs lines expressing it (17) | the lines without CX3CL1 respond 0.75× as strongly (z diff +0.68); strongest at Homoharringtonine 5 µM: 0.96x vs 1.99x (z diff +6.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB; target measured in part of the lines; both ways; artifact flags |
| [[SLC35F1]] | B | SLC35F1 activity raises GABBR1's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 3.50× lower at baseline in the lines without SLC35F1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[PPP1R18]] | B | PPP1R18 activity raises GABBR1's level | lines that do not express PPP1R18 (5) vs lines expressing it (45) | 3.29× lower at baseline in the lines without PPP1R18 | 0.092 | ⚠ within organs, on part of the lines; also absent: PER3, VIM-AS1, UPP1; maybe low, not absent |
| [[SRCIN1]] | B | SRCIN1 activity raises GABBR1's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without SRCIN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[NPHS1]] | C | NPHS1 activity raises GABBR1's level | lines that do not express NPHS1 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without NPHS1 | 0.018 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALG5]] | B | GABBR1 activity lowers ALG5's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 1.87× higher at baseline in the lines without GABBR1 | 0.045 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[S1PR2]] | B | GABBR1 activity raises S1PR2's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 2.33× lower at baseline in the lines without GABBR1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[EPOP]] | B | GABBR1 activity raises EPOP's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without GABBR1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[NTN1]] | B | GABBR1 activity raises NTN1's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without GABBR1 | 0.061 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[AKT3]] | B | GABBR1 activity raises AKT3's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 9.14× lower at baseline in the lines without GABBR1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.384). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (26.0, -2.4); signed map (24.5, 22.0). **Vector** length 96.9, 22.3% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.9 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -6.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type B receptor subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:29,555,629-29,633,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hGB1a, GPRC3A |
| Gene groups (HGNC) | Gamma-aminobutyric acid type B receptor subunits; Sushi domain containing |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 16 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); Activation of G protein gated Potassium channels; G protein gated Potassium channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBS5](https://www.uniprot.org/uniprotkb/Q9UBS5) (Gamma-aminobutyric acid type B receptor subunit 1):

> Component of a heterodimeric G protein-coupled receptor for GABA, formed by GABBR1 and GABBR2. Within the heterodimeric GABA receptor, only GABBR1 seems to bind agonists, while GABBR2 mediates coupling to G proteins. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors, such as adenylate cyclase. Signaling inhibits adenylate cyclase, stimulates phospholipase A2, activates …

**Summary**, from NCBI Gene [2550](https://www.ncbi.nlm.nih.gov/gene/2550):

> This gene encodes a receptor for gamma-aminobutyric acid (GABA), which is the main inhibitory neurotransmitter in the mammalian central nervous system. This receptor functions as a heterodimer with GABA(B) receptor 2. Defects in this gene may underlie brain disorders such as schizophrenia and epilepsy. Alternative splicing generates multiple transcript variants, but the full-length nature of some of these variants has not been determined. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:4070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4070) · Entrez [2550](https://www.ncbi.nlm.nih.gov/gene/2550) · UniProt [Q9UBS5](https://www.uniprot.org/uniprotkb/Q9UBS5) · Ensembl [ENSG00000204681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204681)

## Data

Gene col 12912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12912); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12912]; `tensor/DDL_lfc|DDL_z.npy` [12912]; `embed/gene_vectors.npy` [12912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12912 or target_col == 12912). Every well: [[GABBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
