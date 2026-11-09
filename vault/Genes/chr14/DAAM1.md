---
symbol: "DAAM1"
type: "gene"
col: 1993
ensembl_id: "ENSG00000100592"
name: "dishevelled associated activator of morphogenesis 1"
location: "14q23.1"
module: 59
arm: "+"
pooled_cpm: 109.45
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 8
n_dd_up_clean: 31
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# DAAM1

*dishevelled associated activator of morphogenesis 1* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.65× (z +47.8, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.569× (z -13.6, q 2e-39, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 0.848× (z -4.1, q 0.003, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKAP2]] (+0.63, fdr 7e-06), [[JUND]] (+0.62, fdr 7e-06), [[OPTN]] (+0.61, fdr 1e-05); moves opposite to [[NSUN2]] (-0.60, fdr 1e-05), [[EFTUD2]] (-0.59, fdr 7e-06), [[DCTD]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SOX4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 8 with an alert ⚠; shown: the 15 strongest. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.65×** | +47.8 | 0e+00 | 43/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.96×** | +28.3 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.73×** | +26.3 | 0e+00 | 46/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.69×** | +25.9 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +23.2 | 0e+00 | 40/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +16.8 | 0e+00 | 35/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +16.4 | 0e+00 | 44/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +13.1 | 4e-37 | 39/47 (J82, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.48×** | +12.0 | 3e-31 | 43/48 (SW480, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +11.2 | 4e-27 | 26/48 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +11.1 | 1e-26 | 34/47 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +9.9 | 2e-21 | 29/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +9.9 | 2e-21 | 31/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.5 | 6e-20 | 28/47 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.4 | 2e-19 | 29/49 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -13.6 | 2e-39 | 32/44 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.665×** | -10.7 | 4e-24 | 29/48 (COLO 205, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -8.3 | 3e-14 | 31/46 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.584×** | -7.1 | 2e-10 | 26/37 (HS-578T, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.766×** | -6.7 | 2e-09 | 23/42 (SHP-77, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.848× | -4.1 | 0.003 | 15/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.856× | -4.1 | 0.003 | 18/47 (NCI-H1792, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.897× | -4.0 | 0.003 | 14/47 (Panc 03.27, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.738×** | -4.0 | 0.003 | 20/48 (Panc 03.27, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.003 | 16/47 (NCI-H1792, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.860× | -4.0 | 0.004 | 20/47 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.010 | 19/47 (RPMI-7951, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.883× | -3.3 | 0.046 | 13/47 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.889× | -3.1 | 0.081 | 9/47 (NCI-H1792, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 53.6 | 19 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +34.2) | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 86.9 | 14 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +26.8) | [[Lonafarnib (drug)]] 5 µM 0.190× (z -9.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 104 | 12 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +25.9) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 52.5 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +24.4) | — |
| [[COLO 205 (line)]] | alt | 163 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +28.3) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -19.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 41.7 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +28.2) | — |
| [[J82 (line)]] | alt | 84.3 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +24.6) | — |
| [[SW480 (line)]] | alt | 107 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +34.9) | — |
| [[SW48 (line)]] | wt | 177 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -13.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 194 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +20.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -17.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.542× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 46.2 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.7) | — |
| [[LS 180 (line)]] | wt | 183 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +24.1) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 191 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +24.5) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -14.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 188 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.9) | [[Selinexor (drug)]] 5 µM 0.587× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.266× (z -9.0) |
| [[RKO (line)]] | wt | 53.5 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +22.2) | — |
| [[A-427 (line)]] | wt | 69.9 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +19.2) | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -21.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 67.3 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +20.4) | — |
| [[NCI-H1792 (line)]] | alt | 308 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 155 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 75.7 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.1) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 129 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +26.0) | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 158 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.1) |
| [[SW1417 (line)]] | alt | 106 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +20.2) | — |
| [[A498 (line)]] | wt | 63.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 142 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 99.8 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.3) | [[Lonafarnib (drug)]] 5 µM 0.153× (z -11.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.479× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +22.9) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 107 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +21.4) | — |
| [[PANC-1 (line)]] | alt | 75.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +14.8) | — |
| [[H4 (line)]] | wt | 49.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 245 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -9.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 119 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 67.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +18.6) | — |
| [[SNU-423 (line)]] | alt | 92.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +13.4) | — |
| [[A-172 (line)]] | wt | 42.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +19.7) | — |
| [[BT-474 (line)]] | alt | 207 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +20.5) | — |
| [[HCT15 (line)]] | alt | 80.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 179 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 198 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 187 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.2) | — |
| [[SW 1088 (line)]] | alt | 99.0 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0931× (z -8.9) |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKAP2]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[JUND]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[OPTN]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[SHOC2]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[KMT2A]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[GABARAP]] ⚠ | +0.57 | +0.60 / +0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HDAC5]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GABARAPL2]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FNBP1]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 | pathway: CDC42 GTPase cycle; STRING 656 |
| [[ARID4A]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SOX4]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 | pathway: Signaling by WNT |
| [[GPX4]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN2]] | -0.60 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.59 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[DCTD]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ALG8]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SPTBN2]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NUP155]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[EEF1AKMT1]] | -0.55 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TRNT1]] | -0.55 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[RPSA]] | -0.55 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[DNAAF5]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX4]] | B | SOX4 activity raises DAAM1's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without SOX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |
| [[BACH2]] | B | BACH2 activity raises DAAM1's level | lines that do not express BACH2 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without BACH2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |
| [[MEF2A]] | C | MEF2A's natural level weakens DAAM1's drug response | MEF2A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74, reverse +0.32; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.4, -43.1); signed map (-9.8, 13.5). **Vector** length 125, 40.4% of its response variance represented; |z| ≥ 3 in 1,707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.5 | +9.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.3 | +8.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.2 | +8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.0 | +5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.0 | +9.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.3 | +4.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -6.7 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dishevelled associated activator of morphogenesis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:59,188,646-59,371,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0666 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 12 pathways, smallest: RHOB GTPase cycle; RHOC GTPase cycle; PCP/CE pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4D1](https://www.uniprot.org/uniprotkb/Q9Y4D1) (Disheveled-associated activator of morphogenesis 1):

> Binds to disheveled (Dvl) and Rho, and mediates Wnt-induced Dvl-Rho complex formation. May play a role as a scaffolding protein to recruit Rho-GDP and Rho-GEF, thereby enhancing Rho-GTP formation. Can direct nucleation and elongation of new actin filaments. Involved in building functional cilia. Involved in the organization of the subapical actin network in multiciliated epithelial cells (By similarity). Together with DAAM2, required for myocardial maturation and sarcomere assembly (By …

**Summary**, from NCBI Gene [23002](https://www.ncbi.nlm.nih.gov/gene/23002):

> Cell motility, adhesion, cytokinesis, and other functions of the cell cortex are mediated by reorganization of the actin cytoskeleton and several formin homology (FH) proteins have been associated with these processes. The protein encoded by this gene contains two FH domains and belongs to a novel FH protein subfamily implicated in cell polarity. A key regulator of cytoskeletal architecture, the small GTPase Rho, is activated during development by Wnt/Fz signaling to control cell polarity and …

**Accessions** — [HGNC:18142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18142) · Entrez [23002](https://www.ncbi.nlm.nih.gov/gene/23002) · UniProt [Q9Y4D1](https://www.uniprot.org/uniprotkb/Q9Y4D1) · Ensembl [ENSG00000100592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100592)

## Data

Gene col 1993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1993); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1993]; `tensor/DDL_lfc|DDL_z.npy` [1993]; `embed/gene_vectors.npy` [1993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1993 or target_col == 1993). Every well: [[DAAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
