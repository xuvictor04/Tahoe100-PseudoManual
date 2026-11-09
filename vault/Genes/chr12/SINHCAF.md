---
symbol: "SINHCAF"
type: "gene"
col: 6264
ensembl_id: "ENSG00000139146"
name: "SIN3-HDAC complex associated factor"
location: "12p11.21"
module: 56
arm: "+"
pooled_cpm: 108.34
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SINHCAF

*SIN3-HDAC complex associated factor* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +16.6, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.820× (z -5.0, q 3e-04, down in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 4 lines (SHP-77 0.421×, HT-29 0.441×, NCI-H23 0.550×, HCT15 0.420×); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.358×, Panc 03.27 0.376×, HEC-1-A 0.424×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.582×, SHP-77 0.511×; ⚠ cell-cycle shift, explains ~43% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP1]] (+0.56, fdr 1e-05), [[RNF138]] (+0.55, fdr 1e-05), [[SLC12A2-DT]] (+0.55, fdr 3e-05); moves opposite to [[MKNK1]] (-0.61, fdr 1e-05), [[PCYT1A]] (-0.59, fdr 1e-05), [[TVP23C-CDRT4]] (-0.59, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +16.6 | 0e+00 | 38/48 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.88×** | +14.7 | 0e+00 | 40/47 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +13.0 | 3e-36 | 42/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +11.9 | 1e-30 | 26/47 (CFPAC-1, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +11.7 | 1e-29 | 32/46 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +10.7 | 1e-24 | 33/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +10.4 | 2e-23 | 31/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +10.1 | 4e-22 | 33/47 (A549, SW 900, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +9.7 | 3e-20 | 30/46 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +8.4 | 3e-15 | 30/46 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +8.0 | 7e-14 | 29/47 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.34×** | +7.7 | 4e-13 | 29/46 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +7.0 | 1e-10 | 27/47 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.9 | 2e-07 | 19/49 (HOP62, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +5.5 | 2e-06 | 18/47 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.8 | 6e-05 | 13/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.8 | 6e-05 | 13/47 (AsPC-1, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +4.2 | 8e-04 | 11/47 (C32, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.008 | 11/46 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.070 | 2/47 (Panc 03.27, hTERT-HPNE) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.11× | +2.9 | 0.086 | 9/46 (BT-474, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6264.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 4 lines (SHP-77 0.421×, HT-29 0.441×, NCI-H23 0.550×, HCT15 0.420×); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.358×, Panc 03.27 0.376×, HEC-1-A 0.424×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.582×, SHP-77 0.511×; ⚠ cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.820×** | -5.0 | 3e-04 | 19/46 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.832×** | -4.9 | 3e-04 | 21/47 (SHP-77, HT-29, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -3.9 | 0.020 | 13/43 (H4, A549, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.868× | -3.8 | 0.022 | 10/46 (SW 900, SW48, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.903× | -3.6 | 0.033 | 6/47 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -3.5 | 0.037 | 2/49 (MIA PaCa-2, SW 1271) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.045 | 16/46 (A-427, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 5 µM |  | 0.882× | -3.2 | 0.099 | 7/48 (A-427, BT-474, …) | top dose only |  |
| [[Nimesulide (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.889× | -3.1 | 0.11 | 3/46 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | 0.801× | -3.1 | 0.12 | 12/44 (RPMI-7951, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 75.9 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.29× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 143 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.7) | — |
| [[A549 (line)]] | wt | 91.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +19.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.22× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 175 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.30× (z +12.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.54× (z +10.4) | — |
| [[A498 (line)]] | wt | 83.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +18.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.34× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 62.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +22.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 81.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +15.7) | — |
| [[NCI-H1792 (line)]] | alt | 56.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 114 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.51× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 396 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -9.7) |
| [[SW480 (line)]] | alt | 165 | 3 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.93× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -10.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[J82 (line)]] | alt | 57.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +17.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 64.5 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.46× (z +12.8) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 90.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 119 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.6) | — |
| [[A-172 (line)]] | wt | 35.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.3) | — |
| [[A-427 (line)]] | wt | 135 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.87× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 96.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +12.9) | — |
| [[H4 (line)]] | wt | 54.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 169 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.85× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 78.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.5) | — |
| [[LoVo (line)]] | wt | 138 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 170 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H23 (line)]] | alt | 215 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.548× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.550× (z -9.3) |
| [[SW48 (line)]] | wt | 149 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.58× (z +11.8) | — |
| [[C32 (line)]] | wt | 46.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 10.0× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.266× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 103 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -8.6) |
| [[Hs 766T (line)]] | wt | 47.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 225 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.441× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 91.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.86× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 53.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 70.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 53.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 125 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP1]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RNF138]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[MAP3K1]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[THAP12]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[USP6NL]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TAPT1]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[UCK2]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MBNL3]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SLC35F2]] | +0.51 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SMAD6]] | +0.50 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[TMEM64]] | +0.50 | +0.58 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK1]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PCYT1A]] | -0.59 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[TVP23C-CDRT4]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[CDRT4]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[DHDDS]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[POFUT2]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[COPE]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[AP1G1]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[YKT6]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SAMD4B]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ACOX3]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[GDI1]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction -0.386). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, -34.1); signed map (27.3, -35.5). **Vector** length 110, 30.3% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +16.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +11.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +14.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -3.3 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | SIN3-HDAC complex associated factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:31,280,584-31,327,058 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TERA; previously C12orf14, FAM60A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP50](https://www.uniprot.org/uniprotkb/Q9NP50) (SIN3-HDAC complex-associated factor):

> Subunit of the Sin3 deacetylase complex (Sin3/HDAC), this subunit is important for the repression of genes encoding components of the TGF-beta signaling pathway. Core component of a SIN3A complex (composed of at least SINHCAF, SIN3A, HDAC1, SAP30, RBBP4, OGT and TET1) present in embryonic stem (ES) cells. Promotes the stability of SIN3A and its presence on chromatin and is essential for maintaining the potential of ES cells to proliferate rapidly, while ensuring a short G1-phase of the cell …

**Summary**, from NCBI Gene [58516](https://www.ncbi.nlm.nih.gov/gene/58516):

> Involved in negative regulation of cell migration. Part of Sin3-type complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30702) · Entrez [58516](https://www.ncbi.nlm.nih.gov/gene/58516) · UniProt [Q9NP50](https://www.uniprot.org/uniprotkb/Q9NP50) · Ensembl [ENSG00000139146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139146)

## Data

Gene col 6264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6264); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6264]; `tensor/DDL_lfc|DDL_z.npy` [6264]; `embed/gene_vectors.npy` [6264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6264 or target_col == 6264). Every well: [[SINHCAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SINHCAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
