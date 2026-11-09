---
symbol: "MARK4"
type: "gene"
col: 135
ensembl_id: "ENSG00000007047"
name: "microtubule affinity regulating kinase 4"
location: "19q13.32"
module: 3
arm: "+"
pooled_cpm: 106.66
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MARK4

*microtubule affinity regulating kinase 4* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +22.4, q 0e+00, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.612× (z -15.3, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.675× (z -12.2, q 7e-32, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK1G2]] (+0.72, fdr 7e-06), [[TMEM38A]] (+0.70, fdr 7e-06), [[BAHD1]] (+0.69, fdr 1e-05); moves opposite to [[NBN]] (-0.68, fdr 1e-05), [[GMFB]] (-0.66, fdr 2e-05), [[IMPACT]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC8B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +22.4 | 0e+00 | 43/49 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +17.1 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +16.8 | 0e+00 | 45/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +16.2 | 0e+00 | 47/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +11.1 | 1e-26 | 40/49 (HEC-1-A, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +10.4 | 3e-23 | 38/48 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +9.4 | 3e-19 | 33/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +7.4 | 7e-12 | 31/48 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +7.1 | 9e-11 | 26/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +7.0 | 2e-10 | 27/48 (HEC-1-A, COLO 205, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | **1.25×** | +6.5 | 3e-09 | 26/47 (HT-29, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +6.3 | 2e-08 | 23/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +5.5 | 2e-06 | 30/49 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.19× | +5.1 | 1e-05 | 22/48 (SW48, HOP62, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +5.1 | 1e-05 | 20/48 (A498, HS-578T, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 5e-05 | 21/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.020 | 8/49 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.027 | 9/48 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.057 | 9/48 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -15.3 | 0e+00 | 44/49 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -14.3 | 1e-43 | 34/44 (HCT15, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -12.2 | 7e-32 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -10.7 | 2e-24 | 39/48 (A-427, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -10.7 | 2e-24 | 34/48 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.740×** | -8.7 | 5e-16 | 27/45 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -6.4 | 1e-08 | 25/48 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -5.3 | 8e-06 | 25/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | 0.857× | -4.6 | 3e-04 | 19/47 (LOX-IMVI, C32, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.761×** | -4.4 | 5e-04 | 21/49 (HS-578T, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | 0.878× | -4.0 | 0.003 | 12/48 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.917× | -3.8 | 0.006 | 6/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.919× | -3.7 | 0.008 | 11/48 (AsPC-1, J82, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.895× | -3.4 | 0.024 | 14/49 (LoVo, C32, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.932× | -3.1 | 0.073 | 4/48 (RPMI-7951, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 307 | 5 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.99× (z +13.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.510× (z -13.0) |
| [[SW480 (line)]] | alt | 90.5 | 7 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +15.3) | [[Harringtonine (drug)]] 0.5 µM 0.574× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 194 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.71× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -19.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 91.7 | 4 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.535× (z -9.6) |
| [[HS-578T (line)]] | alt | 121 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.09× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.466× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.556× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 99.0 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.472× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.565× (z -8.9) |
| [[Hs 766T (line)]] | wt | 81.1 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 88.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 129 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.37× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 146 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 103 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -28.7) |
| [[A549 (line)]] | wt | 88.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +16.3) | — |
| [[HCT15 (line)]] | alt | 151 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0521× (z -31.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 93.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 94.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -22.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 64.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -16.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.447× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 70.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 99.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 88.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.3) | [[Harringtonine (drug)]] 0.5 µM 0.500× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 70.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.469× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 111 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +9.1) | — |
| [[RKO (line)]] | wt | 117 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 92.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 75.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.95× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 92.9 | 0 | 2 | — | [[Roxadustat (drug)]] 0.5 µM 0.0867× (z -9.3) |
| [[A-172 (line)]] | wt | 68.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -12.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +15.2) | — |
| [[AN3 CA (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 94.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 67.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 79.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.6) | — |
| [[J82 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.470× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.488× (z -8.5) |
| [[PANC-1 (line)]] | alt | 60.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +14.8) | — |
| [[SW 1271 (line)]] | alt | 91.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 125 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.3) | — |
| [[SW48 (line)]] | wt | 117 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G2]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TMEM38A]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[BAHD1]] | +0.69 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[SLC35E1]] | +0.68 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[RAB43]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PTOV1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.66 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[SEZ6L2]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.66 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBN]] | -0.68 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[GMFB]] | -0.66 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[IMPACT]] | -0.65 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.64 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[C12orf29]] | -0.62 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[GUF1]] | -0.62 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.61 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.61 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.61 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[TAF9]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[KICS2]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8B]] | B | LRRC8B activity lowers MARK4's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.07× higher at baseline in the lines without LRRC8B | 0.059 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.7, -3.5); signed map (-41.0, 3.2). **Vector** length 125, 36.5% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +22.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.0 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +11.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.6 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +7.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.5 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.2 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.9 | -10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.7 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.5 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -2.6 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | microtubule affinity regulating kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,079,288-45,305,284 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nbla00650, FLJ90097, KIAA1860, PAR-1D; previously MARKL1 |
| Gene groups (HGNC) | Microtubule affinity regulating kinases |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L34](https://www.uniprot.org/uniprotkb/Q96L34) (MAP/microtubule affinity-regulating kinase 4):

> Serine/threonine-protein kinase. Phosphorylates the microtubule-associated protein MAPT/TAU. Also phosphorylates the microtubule-associated proteins MAP2 and MAP4. Involved in regulation of the microtubule network, causing reorganization of microtubules into bundles. Required for the initiation of axoneme extension during cilium assembly. Regulates the centrosomal location of ODF2 and phosphorylates ODF2 in vitro. Plays a role in cell cycle progression, specifically in the G1/S checkpoint. …

**Summary**, from NCBI Gene [57787](https://www.ncbi.nlm.nih.gov/gene/57787):

> This gene encodes a member of the microtubule affinity-regulating kinase family. These protein kinases phosphorylate microtubule-associated proteins and regulate the transition between stable and dynamic microtubules. The encoded protein is associated with the centrosome throughout mitosis and may be involved in cell cycle control. Expression of this gene is a potential marker for cancer, and the encoded protein may also play a role in Alzheimer's disease. Pseudogenes of this gene are located …

**Accessions** — [HGNC:13538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13538) · Entrez [57787](https://www.ncbi.nlm.nih.gov/gene/57787) · UniProt [Q96L34](https://www.uniprot.org/uniprotkb/Q96L34) · Ensembl [ENSG00000007047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007047)

## Data

Gene col 135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 135); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 135]; `tensor/DDL_lfc|DDL_z.npy` [135]; `embed/gene_vectors.npy` [135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 135 or target_col == 135). Every well: [[MARK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
