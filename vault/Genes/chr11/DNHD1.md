---
symbol: "DNHD1"
type: "gene"
col: 11040
ensembl_id: "ENSG00000179532"
name: "dynein heavy chain domain 1"
location: "11p15.4"
module: 37
arm: "+"
pooled_cpm: 50.9
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DNHD1

*dynein heavy chain domain 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.58× (z +21.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.570× (z -6.6, q 3e-08, down in 30 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.787× (z -4.0, q 0.005, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 0.151×, NCI-H1573 0.118×, HepG2/C3A 0.0861×, KATO III 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.134×, KATO III 0.230×, NCI-H1573 0.217×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (BT-474 0.259×, KATO III 0.247×, PANC-1 0.289×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.378×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2]] (+0.76, fdr 7e-06), [[TNXB]] (+0.71, fdr 7e-06), [[GOSR2]] (+0.70, fdr 7e-06); moves opposite to [[GNPTAB]] (-0.55, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.58×** | +21.0 | 0e+00 | 47/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +12.4 | 1e-32 | 47/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.51×** | +10.7 | 1e-24 | 43/48 (SW480, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +9.2 | 5e-18 | 41/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +8.3 | 9e-15 | 39/49 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +7.4 | 1e-11 | 40/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +7.0 | 2e-10 | 38/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.9 | 5e-10 | 35/48 (SW1417, A-172, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.48×** | +6.5 | 7e-09 | 39/48 (A549, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 9e-06 | 28/47 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.5 | 4e-04 | 30/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.99×** | +4.2 | 0.001 | 32/47 (MIA PaCa-2, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.007 | 24/49 (A549, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.008 | 28/48 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +3.7 | 0.009 | 24/48 (AsPC-1, BT-474, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.011 | 27/48 (SNU-423, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11040.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 0.151×, NCI-H1573 0.118×, HepG2/C3A 0.0861×, KATO III 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.134×, KATO III 0.230×, NCI-H1573 0.217×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (BT-474 0.259×, KATO III 0.247×, PANC-1 0.289×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.378×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.570×** | -6.6 | 3e-08 | 30/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.412×** | -5.4 | 2e-05 | 35/47 (RKO, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.645×** | -5.1 | 6e-05 | 29/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.675×** | -4.6 | 6e-04 | 30/47 (COLO 205, PANC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.675×** | -4.4 | 0.001 | 29/48 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.687×** | -4.4 | 0.001 | 25/48 (A549, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.681×** | -4.2 | 0.003 | 24/44 (NCI-H23, C32, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.005 | 25/48 (HEC-1-A, RPMI-7951, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.713×** | -3.8 | 0.009 | 23/40 (PANC-1, HT-29, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.768× | -3.1 | 0.12 | 19/48 (PANC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 58.2 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +17.6) | — |
| [[PANC-1 (line)]] | alt | 103 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -16.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 36.2 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 105 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -10.6) ⚠ cell-cycle shift, explains ~86% of this change |
| [[C32 (line)]] | wt | 25.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 64.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 59.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +15.9) | — |
| [[KATO III (line)]] | alt | 35.3 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 66.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 52.7 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -14.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 24.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +17.7) | — |
| [[J82 (line)]] | alt | 60.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 42.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +14.7) | [[Lonafarnib (drug)]] 5 µM 0.0808× (z -10.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 38.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.118× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 34.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 76.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0956× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 70.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[HepG2_C3A (line)]] | wt | 32.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.0861× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 78.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 66.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 35.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.206× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 22.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +14.1) | — |
| [[SW 900 (line)]] | alt | 17.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +11.8) | — |
| [[A498 (line)]] | wt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[A549 (line)]] | wt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +15.7) | — |
| [[C-33 A (line)]] | alt | 58.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +14.7) | — |
| [[HCT15 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 38.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +15.2) | — |
| [[HS-578T (line)]] | alt | 43.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 54.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +13.9) | — |
| [[RKO (line)]] | wt | 49.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 84.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.43× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 59.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 61.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.9) | — |
| [[SW48 (line)]] | wt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +12.6) | — |
| [[A-427 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2]] | +0.76 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TNXB]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.70 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[APRG1]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[NPIPB11]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[UBAP1L]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[WDR49]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[EOLA2-DT]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[PELO-AS1]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPTAB]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNHD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, -19.5); signed map (10.7, 7.2). **Vector** length 122, 41.0% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.1 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +21.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +12.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +8.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.3 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +3.2 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -7.0 | -4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.5 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | dynein heavy chain domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,497,260-6,593,758 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32752, FLJ46184, FLJ35709, DKFZp686J0796; previously DHCD1, C11orf47, DNHD1L, CCDC35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M86](https://www.uniprot.org/uniprotkb/Q96M86) (Dynein heavy chain domain-containing protein 1):

> Essential for the normal assembly and function of sperm flagella axonemes.

**Summary**, from NCBI Gene [144132](https://www.ncbi.nlm.nih.gov/gene/144132):

> Predicted to enable dynein intermediate chain binding activity; dynein light intermediate chain binding activity; and minus-end-directed microtubule motor activity. Involved in sperm flagellum assembly. Located in sperm annulus and sperm midpiece. Implicated in spermatogenic failure 65. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26532) · Entrez [144132](https://www.ncbi.nlm.nih.gov/gene/144132) · UniProt [Q96M86](https://www.uniprot.org/uniprotkb/Q96M86) · Ensembl [ENSG00000179532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179532)

## Data

Gene col 11040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11040); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11040]; `tensor/DDL_lfc|DDL_z.npy` [11040]; `embed/gene_vectors.npy` [11040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11040 or target_col == 11040). Every well: [[DNHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
