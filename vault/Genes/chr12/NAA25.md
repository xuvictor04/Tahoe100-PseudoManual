---
symbol: "NAA25"
type: "gene"
col: 3216
ensembl_id: "ENSG00000111300"
name: "N-alpha-acetyltransferase 25, NatB auxiliary subunit"
location: "12q24.13"
module: 4
arm: "+"
pooled_cpm: 99.08
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NAA25

*N-alpha-acetyltransferase 25, NatB auxiliary subunit* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.23× (z +26.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.675× (z -12.7, q 3e-34, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS27]] (+0.78, fdr 7e-06), [[VWA8]] (+0.76, fdr 7e-06), [[TSEN2]] (+0.76, fdr 7e-06); moves opposite to [[SHOC2]] (-0.65, fdr 7e-06), [[FAM117A]] (-0.63, fdr 8e-06), [[AAMDC]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.23×** | +26.7 | 0e+00 | 48/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.16×** | +26.2 | 0e+00 | 48/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.09×** | +24.3 | 0e+00 | 48/48 (HT-29, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.79×** | +15.9 | 0e+00 | 44/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +13.6 | 3e-40 | 46/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.17×** | +12.6 | 2e-34 | 46/49 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +11.5 | 1e-28 | 42/48 (A498, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +11.2 | 3e-27 | 39/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +11.0 | 2e-26 | 39/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +10.8 | 2e-25 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +9.6 | 3e-20 | 41/45 (SNU-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +9.6 | 4e-20 | 39/47 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.5 | 9e-20 | 36/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +8.8 | 4e-17 | 37/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +6.3 | 1e-08 | 26/48 (A549, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +5.7 | 4e-07 | 33/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +5.5 | 1e-06 | 32/48 (A498, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +5.1 | 1e-05 | 27/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.6 | 1e-04 | 21/49 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +4.5 | 2e-04 | 19/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -12.7 | 3e-34 | 31/49 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -6.6 | 1e-08 | 23/48 (A498, SW1417, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.3 | 2e-05 | 24/50 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -5.2 | 4e-05 | 27/49 (SW1417, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.824×** | -4.4 | 0.001 | 20/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.004 | 20/47 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.9 | 0.008 | 24/48 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.855× | -3.6 | 0.021 | 19/47 (HOP62, A549, …) | two highest doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.877× | -3.3 | 0.063 | 11/48 (SW48, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.870× | -3.2 | 0.076 | 17/48 (RKO, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.1 | 0.089 | 20/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.869× | -3.1 | 0.089 | 9/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Adenosine (drug)]] 5 µM |  | 0.910× | -3.1 | 0.091 | 3/48 (NCI-H661, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.831×** | -3.0 | 0.099 | 12/48 (NCI-H2347, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 132 | 8 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.08× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -11.1) |
| [[SW480 (line)]] | alt | 105 | 10 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.50× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 146 | 5 (1 ⚠) | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 133 | 8 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.37× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -11.3) |
| [[LS 180 (line)]] | wt | 93.9 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.60× (z +16.4) | — |
| [[NCI-H460 (line)]] | wt | 119 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.6) |
| [[HOP62 (line)]] | alt | 72.5 | 7 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.48× (z +21.7) | — |
| [[NCI-H1573 (line)]] | alt | 72.2 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.58× (z +16.1) | — |
| [[NCI-H23 (line)]] | alt | 143 | 6 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 63.2 | 7 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.25× (z +11.2) | — |
| [[A498 (line)]] | wt | 78.9 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.8) |
| [[A549 (line)]] | wt | 108 | 5 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.2) |
| [[HT-29 (line)]] | alt | 53.9 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.17× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 118 | 5 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.45× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 81.9 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.38× (z +15.1) | — |
| [[NCI-H2347 (line)]] | alt | 83.0 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +14.6) | — |
| [[SW 900 (line)]] | alt | 78.3 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 83.5 | 4 (1 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 4.10× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.5) |
| [[BT-474 (line)]] | alt | 170 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 99.4 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.33× (z +16.7) | — |
| [[HEC-1-A (line)]] | alt | 128 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[KATO III (line)]] | alt | 74.4 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.09× (z +15.1) | — |
| [[RKO (line)]] | wt | 164 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.34× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -21.4) |
| [[SW48 (line)]] | wt | 207 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.97× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 65.0 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.28× (z +16.1) | — |
| [[HepG2_C3A (line)]] | wt | 94.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.34× (z +15.3) | — |
| [[SHP-77 (line)]] | alt | 165 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.68× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 69.9 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.38× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -14.5) |
| [[SNU-1 (line)]] | wt | 150 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -8.8) |
| [[SW1417 (line)]] | alt | 108 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.59× (z +11.4) | — |
| [[A-172 (line)]] | wt | 54.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.88× (z +13.7) | — |
| [[A-427 (line)]] | wt | 127 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 156 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 63.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.49× (z +15.4) | — |
| [[COLO 205 (line)]] | alt | 49.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.6× (z +16.5) | — |
| [[H4 (line)]] | wt | 86.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.62× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 39.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.04× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 56.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.99× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 49.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.90× (z +14.5) | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.37× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 54.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +15.5) | — |
| [[J82 (line)]] | alt | 79.4 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.9) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.0) |
| [[CHP-212 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS27]] | +0.78 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[VWA8]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | same gene group |
| [[TSEN2]] | +0.76 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[TCERG1]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[NAA15]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | same gene group; STRING 993 |
| [[NOL10]] | +0.75 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[LTV1]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[BYSL]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[PHF14]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[DDX31]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHOC2]] | -0.65 | -0.67 / -0.64 | both halves | 7e-06 | same gene group |
| [[FAM117A]] | -0.63 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[AAMDC]] | -0.61 | -0.61 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.6, -34.2); signed map (-11.0, -48.8). **Vector** length 125, 44.3% of its response variance represented; |z| ≥ 3 in 1,539 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA Aminoacylation* (reactome, mean cos +0.50 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.58 to 8); *tRNA processing* (reactome, mean cos +0.58 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.6 | +26.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.5 | +24.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +26.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +11.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.7 | +9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.7 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +15.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.5 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +5.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -12.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | +11.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 25, NatB auxiliary subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,026,689-112,108,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13089; previously C12orf30 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CX7](https://www.uniprot.org/uniprotkb/Q14CX7) (N-alpha-acetyltransferase 25, NatB auxiliary subunit):

> Non-catalytic subunit of the NatB complex which catalyzes acetylation of the N-terminal methionine residues of peptides beginning with Met-Asp, Met-Glu, Met-Asn and Met-Gln. May play a role in normal cell-cycle progression.

**Summary**, from NCBI Gene [80018](https://www.ncbi.nlm.nih.gov/gene/80018):

> This gene encodes the auxiliary subunit of the heteromeric N-terminal acetyltransferase B complex. This complex acetylates methionine residues that are followed by acidic or asparagine residues.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:25783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25783) · Entrez [80018](https://www.ncbi.nlm.nih.gov/gene/80018) · UniProt [Q14CX7](https://www.uniprot.org/uniprotkb/Q14CX7) · Ensembl [ENSG00000111300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111300)

## Data

Gene col 3216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3216); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3216]; `tensor/DDL_lfc|DDL_z.npy` [3216]; `embed/gene_vectors.npy` [3216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3216 or target_col == 3216). Every well: [[NAA25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
