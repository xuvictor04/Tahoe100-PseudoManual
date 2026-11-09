---
symbol: "EXOC6"
type: "gene"
col: 6142
ensembl_id: "ENSG00000138190"
name: "exocyst complex component 6"
location: "10q23.33"
module: 169
arm: "+"
pooled_cpm: 90.59
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# EXOC6

*exocyst complex component 6* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +14.3, q 2e-43, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.442× (z -22.0, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF12A]] (+0.56, fdr 1e-05), [[CAAP1]] (+0.56, fdr 1e-05), [[GOLT1A]] (+0.54, fdr 2e-05); moves opposite to [[ARHGEF7]] (-0.57, fdr 7e-06), [[ZNF75D]] (-0.56, fdr 1e-05), [[RPL34-DT]] (-0.56, fdr 7e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +14.3 | 2e-43 | 34/46 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +12.3 | 5e-32 | 35/46 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +10.1 | 2e-21 | 33/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +9.9 | 9e-21 | 31/46 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +8.6 | 8e-16 | 33/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +5.7 | 1e-06 | 25/46 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +5.1 | 3e-05 | 22/46 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.20×** | +5.0 | 5e-05 | 22/46 (A498, A-172, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.4 | 8e-04 | 18/46 (SW 900, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +4.1 | 0.003 | 19/47 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +4.0 | 0.003 | 15/46 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.9 | 0.005 | 16/46 (KATO III, HS-578T, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.09× | +3.4 | 0.033 | 3/47 (HepG2/C3A, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.442×** | -22.0 | 0e+00 | 42/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -20.8 | 0e+00 | 38/47 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.254×** | -19.3 | 0e+00 | 44/47 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.378×** | -13.7 | 1e-40 | 36/46 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -13.4 | 7e-39 | 34/43 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -13.0 | 2e-36 | 30/47 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.750×** | -10.9 | 7e-26 | 35/46 (SW480, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -10.8 | 4e-25 | 32/42 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -8.3 | 5e-15 | 28/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -8.2 | 2e-14 | 30/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.741×** | -8.1 | 4e-14 | 30/45 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.578×** | -7.7 | 5e-13 | 26/41 (Hs 766T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.745×** | -7.5 | 4e-12 | 29/46 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -7.3 | 1e-11 | 25/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -7.1 | 4e-11 | 23/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.9 | 1e-10 | 25/45 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.874× | -3.5 | 0.013 | 15/47 (HOP62, NCI-H2122, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.027 | 9/46 (KATO III, A549, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.858× | -2.9 | 0.066 | 10/47 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.927× | -2.9 | 0.079 | 7/47 (A549, CFPAC-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.891× | -2.9 | 0.079 | 8/45 (CHP-212, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 149 | 0 | 16 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.113× (z -19.8) |
| [[SW480 (line)]] | alt | 160 | 0 | 12 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.211× (z -27.3) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 11 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.291× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 154 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -25.2) |
| [[HOP62 (line)]] | alt | 60.9 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.387× (z -10.6) |
| [[RKO (line)]] | wt | 119 | 0 | 8 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0706× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 87.3 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -12.9) |
| [[A-172 (line)]] | wt | 53.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 6 | — | [[Auranofin (drug)]] 5 µM 0.329× (z -17.9) |
| [[LoVo (line)]] | wt | 79.3 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.19× (z +9.8) | [[TAK-901 (drug)]] 5 µM 0.178× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -15.4) |
| [[A498 (line)]] | wt | 25.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 170 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.396× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 79.5 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.235× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 71.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -12.4) |
| [[A-427 (line)]] | wt | 127 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.9) |
| [[C32 (line)]] | wt | 52.7 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.44× (z +8.5) | [[Binimetinib (drug)]] 0.5 µM 0.301× (z -9.9) |
| [[HT-29 (line)]] | alt | 100 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -13.8) |
| [[LS 180 (line)]] | wt | 93.4 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.184× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 74.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.533× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.5) |
| [[SNU-1 (line)]] | wt | 109 | 0 | 4 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0640× (z -12.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.9) |
| [[SW1417 (line)]] | alt | 99.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -12.4) |
| [[A549 (line)]] | wt | 119 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.6) |
| [[HCT15 (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.359× (z -10.9) |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.134× (z -9.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.480× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 63.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.9) |
| [[SHP-77 (line)]] | alt | 80.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 86.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.170× (z -9.9) |
| [[SW 900 (line)]] | alt | 89.7 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.287× (z -13.2) |
| [[BT-474 (line)]] | alt | 97.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.5) |
| [[Hs 766T (line)]] | wt | 81.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.3) |
| [[J82 (line)]] | alt | 60.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.476× (z -10.6) |
| [[SW48 (line)]] | wt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.2) |
| [[KATO III (line)]] | alt | 82.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.164× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 62.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.337× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.227× (z -9.9) |
| [[SNU-423 (line)]] | alt | 56.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 173 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CAAP1]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[GOLT1A]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CEP135]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[PFN1]] | +0.53 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[UQCC2]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[TAF1B]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TIPRL]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TCAF1]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SMG9]] | +0.51 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[LINC00973]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.50 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | -0.57 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[ZNF75D]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RPL34-DT]] | -0.56 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[APH1A]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PRDX6]] | -0.54 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[DERL1]] | -0.54 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.53 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[GLUD1P3]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GHITM]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[GUCD1]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SLC39A6]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NUCB1]] | -0.52 | -0.55 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EXOC6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction -0.392). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, 1.5); signed map (13.3, -48.0). **Vector** length 129, 40.1% of its response variance represented; |z| ≥ 3 in 1,340 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.0 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -20.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.0 | -22.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.0 | -10.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.3 | -19.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.8 | -13.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -7.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:92,826,831-93,059,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEC15L, FLJ1125, DKFZp761I2124, MGC33397, Sec15, EXOC6A; previously SEC15L1 |
| Gene groups (HGNC) | Exocyst complex |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAG9](https://www.uniprot.org/uniprotkb/Q8TAG9) (Exocyst complex component 6):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane. Together with RAB11A, RAB3IP, RAB8A, PARD3, PRKCI, ANXA2, CDC42 and DNMBP promotes transcytosis of PODXL to the apical membrane initiation sites (AMIS), apical surface formation and lumenogenesis (By similarity).

**Summary**, from NCBI Gene [54536](https://www.ncbi.nlm.nih.gov/gene/54536):

> The protein encoded by this gene is highly similar to the Saccharomyces cerevisiae SEC15 gene product, which is essential for vesicular traffic from the Golgi apparatus to the cell surface in yeast. It is one of the components of a multiprotein complex required for exocytosis. The 5' portion of this gene and two neighboring cytochrome p450 genes are included in a deletion that results in an autosomal-dominant form of nonsyndromic optic nerve aplasia (ONA). Alternative splicing and the use of …

**Accessions** — [HGNC:23196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23196) · Entrez [54536](https://www.ncbi.nlm.nih.gov/gene/54536) · UniProt [Q8TAG9](https://www.uniprot.org/uniprotkb/Q8TAG9) · Ensembl [ENSG00000138190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138190)

## Data

Gene col 6142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6142); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6142]; `tensor/DDL_lfc|DDL_z.npy` [6142]; `embed/gene_vectors.npy` [6142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6142 or target_col == 6142). Every well: [[EXOC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
