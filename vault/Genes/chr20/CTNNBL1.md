---
symbol: "CTNNBL1"
type: "gene"
col: 5372
ensembl_id: "ENSG00000132792"
name: "catenin beta like 1"
location: "20q11.23"
module: 199
arm: "+"
pooled_cpm: 117.36
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# CTNNBL1

*catenin beta like 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.48× (z +15.1, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.651× (z -14.1, q 4e-42, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FTO]] (+0.69, fdr 1e-05), [[GTF2E2]] (+0.67, fdr 1e-05), [[TAF5L]] (+0.66, fdr 8e-05); moves opposite to [[THAP2]] (-0.66, fdr 3e-05), [[GALNT7-DT]] (-0.66, fdr 5e-04), [[FAM200B]] (-0.65, fdr 4e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDC123]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.48×** | +15.1 | 0e+00 | 45/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +14.2 | 5e-43 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.98×** | +13.2 | 2e-37 | 43/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +12.7 | 7e-35 | 47/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +11.6 | 4e-29 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +11.3 | 8e-28 | 45/48 (Hs 766T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +8.8 | 7e-17 | 41/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +8.1 | 3e-14 | 41/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.9 | 3e-07 | 29/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.1 | 2e-05 | 29/45 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.5 | 4e-04 | 20/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.006 | 18/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.17× | +3.6 | 0.013 | 18/48 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.027 | 19/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.4 | 0.029 | 16/38 (NCI-H23, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | 1.15× | +3.0 | 0.075 | 9/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.097 | 6/49 (J82, NCI-H2030, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.100 | 10/48 (SW1417, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -14.1 | 4e-42 | 41/49 (NCI-H1792, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -11.6 | 7e-29 | 36/48 (NCI-H1792, J82, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -10.4 | 4e-23 | 34/49 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -9.7 | 3e-20 | 35/44 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -9.3 | 2e-18 | 40/47 (RPMI-7951, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.768×** | -5.9 | 4e-07 | 29/48 (J82, AsPC-1, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.776×** | -5.4 | 4e-06 | 24/45 (RKO, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -4.2 | 0.002 | 15/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.892× | -3.7 | 0.011 | 12/49 (NCI-H1792, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.853× | -3.7 | 0.013 | 17/49 (NCI-H1792, J82, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.864× | -3.4 | 0.035 | 14/48 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.865× | -3.4 | 0.037 | 11/48 (HEC-1-A, hTERT-HPNE, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.870× | -3.2 | 0.052 | 15/48 (NCI-H1792, SK-MEL-2, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.872× | -3.2 | 0.058 | 16/48 (SNU-423, SW 1271, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.873× | -3.1 | 0.063 | 12/48 (NCI-H1792, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 130 | 5 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -15.5) |
| [[SW480 (line)]] | alt | 109 | 8 | 0 | [[TAK-901 (drug)]] 5 µM 6.71× (z +17.9) | — |
| [[J82 (line)]] | alt | 167 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -24.3) |
| [[C32 (line)]] | wt | 150 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 304 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -24.6) |
| [[RKO (line)]] | wt | 150 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.55× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -18.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 127 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 4.86× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.7) |
| [[CFPAC-1 (line)]] | alt | 112 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.552× (z -12.1) |
| [[Hs 766T (line)]] | wt | 148 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 219 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 71.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 80.7 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 3.63× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -11.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.524× (z -11.2) |
| [[SNU-423 (line)]] | alt | 136 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -21.0) |
| [[A498 (line)]] | wt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.9) |
| [[KATO III (line)]] | alt | 119 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 5.38× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -9.7) |
| [[LoVo (line)]] | wt | 74.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 120 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.36× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 99.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -11.4) |
| [[A-172 (line)]] | wt | 95.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.4) |
| [[A549 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 107 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 66.0 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.7) |
| [[HS-578T (line)]] | alt | 135 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.2) |
| [[HT-29 (line)]] | alt | 74.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 57.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 73.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.48× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 224 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 89.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.12× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -13.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 76.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.57× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -15.4) |
| [[SNU-1 (line)]] | wt | 146 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.350× (z -13.7) |
| [[SW48 (line)]] | wt | 71.0 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 4.76× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.1) |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.8) |
| [[COLO 205 (line)]] | alt | 72.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.67× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 213 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.83× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -8.6) |
| [[SW 900 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTO]] | +0.69 | +0.69 / +0.56 | both halves | 1e-05 | STRING 450 |
| [[GTF2E2]] | +0.67 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.66 | +0.74 / +0.37 | both halves | 8e-05 |  |
| [[NEIL2]] | +0.66 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[MKRN2]] | +0.64 | +0.70 / +0.26 | both halves | 4e-04 |  |
| [[ATG5]] | +0.64 | +0.71 / +0.39 | both halves | 6e-05 |  |
| [[PDCD10]] | +0.63 | +0.71 / +0.29 | both halves | 3e-04 |  |
| [[WASF3]] | +0.62 | +0.62 / +0.28 | both halves | 3e-04 |  |
| [[USP35]] | +0.62 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[ESS2]] | +0.61 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[RNF216P1]] | +0.61 | +0.68 / +0.32 | both halves | 2e-04 |  |
| [[SERGEF]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.66 | -0.64 / -0.44 | both halves | 3e-05 | STRING 424 |
| [[GALNT7-DT]] | -0.66 | -0.69 / -0.23 | both halves | 5e-04 |  |
| [[FAM200B]] | -0.65 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.64 | -0.65 / -0.32 | both halves | 1e-04 |  |
| [[LGALSL-DT]] | -0.63 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[THAP9]] | -0.62 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[UNK]] | -0.62 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[NDUFA6-DT]] | -0.62 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[LINC01004]] | -0.61 | -0.58 / -0.26 | both halves | 3e-04 |  |
| [[APLF]] | -0.60 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[ZBED5]] | -0.60 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[KDSR]] | -0.60 | -0.61 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC123]] | C | CDC123's natural level strengthens CTNNBL1's drug response | CDC123's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.25; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.0, 11.7); signed map (-40.5, -8.9). **Vector** length 128, 41.8% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +9.6 | +14.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.5 | +12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.5 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +11.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +13.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.9 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.4 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | catenin beta like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,694,030-37,872,129 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21108, P14L, P14, NAP, NYD-SP19; previously C20orf33 |
| Gene groups (HGNC) | NineTeen complex; Armadillo like helical domain containing; Spliceosomal C complex |
| Reactome | 11 pathways, smallest: Somatic hypermutation of immunoglobulin genes; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYA6](https://www.uniprot.org/uniprotkb/Q8WYA6) (Beta-catenin-like protein 1):

> Component of the PRP19-CDC5L complex that forms an integral part of the spliceosome and is required for activating pre-mRNA splicing. Participates in AID/AICDA-mediated somatic hypermutation (SHM) and class-switch recombination (CSR), 2 processes resulting in the production of high-affinity, mutated isotype-switched antibodies.

**Summary**, from NCBI Gene [56259](https://www.ncbi.nlm.nih.gov/gene/56259):

> The protein encoded by this gene is a component of the pre-mRNA-processing factor 19-cell division cycle 5-like (PRP19-CDC5L) protein complex, which activates pre-mRNA splicing and is an integral part of the spliceosome. The encoded protein is also a nuclear localization sequence binding protein, and binds to activation-induced deaminase and is important for antibody diversification. This gene may also be associated with the development of obesity. Alternative splicing results in multiple …

**Accessions** — [HGNC:15879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15879) · Entrez [56259](https://www.ncbi.nlm.nih.gov/gene/56259) · UniProt [Q8WYA6](https://www.uniprot.org/uniprotkb/Q8WYA6) · Ensembl [ENSG00000132792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132792)

## Data

Gene col 5372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5372); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5372]; `tensor/DDL_lfc|DDL_z.npy` [5372]; `embed/gene_vectors.npy` [5372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5372 or target_col == 5372). Every well: [[CTNNBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
