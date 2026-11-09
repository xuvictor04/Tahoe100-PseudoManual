---
symbol: "MAPK1IP1L"
type: "gene"
col: 9609
ensembl_id: "ENSG00000168175"
name: "mitogen-activated protein kinase 1 interacting protein 1 like"
location: "14q22.3"
module: 11
arm: "+"
pooled_cpm: 99.84
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MAPK1IP1L

*mitogen-activated protein kinase 1 interacting protein 1 like* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +26.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.618× (z -18.3, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A8]] (+0.75, fdr 7e-06), [[ZC3HC1]] (+0.75, fdr 7e-06), [[ZNF518A]] (+0.71, fdr 1e-05); moves opposite to [[KDELR1]] (-0.67, fdr 1e-05), [[STRAP]] (-0.67, fdr 1e-05), [[SETD3]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +26.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.46×** | +24.0 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +17.5 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +17.4 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +14.5 | 1e-45 | 46/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +11.7 | 2e-29 | 42/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +11.5 | 9e-29 | 41/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +10.0 | 2e-21 | 41/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.37×** | +8.6 | 4e-16 | 40/49 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +8.4 | 3e-15 | 30/48 (LS 180, MIA PaCa-2, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +7.8 | 3e-13 | 37/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +7.7 | 4e-13 | 34/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +7.2 | 2e-11 | 0/50 | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +6.1 | 4e-08 | 26/48 (SW480, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +4.6 | 1e-04 | 19/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 1.10× | +3.7 | 0.008 | 2/48 (CHP-212, AN3 CA) | inconsistent across doses | position effect removed |
| [[Tubulin inhibitor 6 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.019 | 10/48 (HCT15, RPMI-7951, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -18.3 | 0e+00 | 46/49 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -16.0 | 0e+00 | 48/48 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.566×** | -15.8 | 0e+00 | 47/48 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -14.6 | 0e+00 | 46/48 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.668×** | -11.3 | 3e-27 | 46/48 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.716×** | -9.3 | 1e-18 | 41/48 (J82, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.738×** | -8.4 | 2e-15 | 32/49 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.775×** | -6.8 | 6e-10 | 24/44 (NCI-H23, CHP-212, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.771×** | -6.7 | 1e-09 | 30/45 (NCI-H23, HEC-1-A, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -6.0 | 1e-07 | 35/49 (J82, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.850× | -4.4 | 7e-04 | 22/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.871× | -3.7 | 0.010 | 18/50 (Panc 03.27, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.883× | -3.5 | 0.021 | 9/48 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.888× | -3.3 | 0.038 | 6/48 (SW48, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 118 | 7 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +23.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 102 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +22.0) | [[Belinostat (drug)]] 5 µM 0.420× (z -11.8) |
| [[J82 (line)]] | alt | 105 | 3 | 6 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +18.2) | [[Belinostat (drug)]] 5 µM 0.328× (z -15.9) |
| [[SW480 (line)]] | alt | 119 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +23.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -16.6) |
| [[A498 (line)]] | wt | 58.7 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.7) |
| [[A549 (line)]] | wt | 108 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 106 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 119 | 4 | 4 | [[Harringtonine (drug)]] 5 µM 2.61× (z +13.7) | [[Belinostat (drug)]] 5 µM 0.482× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 209 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -28.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.547× (z -10.4) |
| [[PANC-1 (line)]] | alt | 67.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +21.2) | — |
| [[SW1417 (line)]] | alt | 103 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 123 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 132 | 5 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +14.8) | [[Belinostat (drug)]] 5 µM 0.479× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 92.4 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.532× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 150 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -13.6) |
| [[A-172 (line)]] | wt | 55.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +17.3) | — |
| [[HOP62 (line)]] | alt | 97.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 75.4 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.3) |
| [[KATO III (line)]] | alt | 99.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 87.9 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.6) |
| [[LS 180 (line)]] | wt | 93.1 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.0) |
| [[SHP-77 (line)]] | alt | 129 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.5) |
| [[SW48 (line)]] | wt | 107 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 90.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 91.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 83.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -11.8) |
| [[BT-474 (line)]] | alt | 94.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -8.5) |
| [[C32 (line)]] | wt | 88.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 98.5 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 2.70× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -8.6) |
| [[H4 (line)]] | wt | 113 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.67× (z +9.8) | [[Bortezomib (drug)]] 5 µM 0.140× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~4% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.4) |
| [[Hs 766T (line)]] | wt | 73.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.2) |
| [[HS-578T (line)]] | alt | 58.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.4) | — |
| [[LoVo (line)]] | wt | 110 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 90.2 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.34× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 80.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.2) |
| [[SW 900 (line)]] | alt | 97.7 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.46× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 79.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 89.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.58× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.43× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 99.5 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.46× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.452× (z -8.6) |
| [[C-33 A (line)]] | alt | 103 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.426× (z -9.1) |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.238× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 110 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.20× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | +0.75 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.75 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ZNF518A]] | +0.71 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PNRC2]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ZNF606]] | +0.68 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZNF441]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[METTL18]] | +0.68 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[SDSL]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR1]] | -0.67 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[STRAP]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SETD3]] | -0.66 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[GRB2]] | -0.64 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MLEC]] | -0.63 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[COG5]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ALKBH5]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[C2CD2L]] | -0.61 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[GLRX5]] | -0.61 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.61 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[WASF3]] | -0.60 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MAPK1IP1L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-26.9, 10.4); signed map (7.3, -19.8). **Vector** length 123, 37.4% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +12.7 | +17.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.7 | +24.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +11.4 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.0 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +10.1 | +11.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.5 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +6.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.0 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.9 | -9.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -16.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -18.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.4 | +0.3 |
|  | [[Pimozide (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 1 interacting protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,051,647-55,070,194 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf32 |
| Matched by | ensembl_id |

UniProt [Q8NDC0](https://www.uniprot.org/uniprotkb/Q8NDC0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19840) · Entrez [93487](https://www.ncbi.nlm.nih.gov/gene/93487) · UniProt [Q8NDC0](https://www.uniprot.org/uniprotkb/Q8NDC0) · Ensembl [ENSG00000168175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168175)

## Data

Gene col 9609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9609); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9609]; `tensor/DDL_lfc|DDL_z.npy` [9609]; `embed/gene_vectors.npy` [9609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9609 or target_col == 9609). Every well: [[MAPK1IP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK1IP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
