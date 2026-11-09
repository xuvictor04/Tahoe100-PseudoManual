---
symbol: "GOLM1"
type: "gene"
col: 5643
ensembl_id: "ENSG00000135052"
name: "golgi membrane protein 1"
location: "9q21.33"
module: 29
arm: "+"
pooled_cpm: 86.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GOLM1

*golgi membrane protein 1* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.45× (z +21.0, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +17.6, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -17.1, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUCA2]] (+0.64, fdr 1e-05), [[APP]] (+0.63, fdr 1e-05), [[LAPTM4B]] (+0.62, fdr 7e-06); moves opposite to [[DNTTIP1]] (-0.56, fdr 1e-05), [[RGP1]] (-0.56, fdr 2e-05), [[TARS2]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +21.0 | 0e+00 | 45/49 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +17.6 | 0e+00 | 44/49 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +17.6 | 0e+00 | 38/43 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +11.7 | 2e-29 | 36/45 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +10.4 | 3e-23 | 34/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.2 | 5e-11 | 32/47 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.7 | 2e-09 | 27/50 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 5e-05 | 24/49 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.5 | 5e-04 | 22/47 (A549, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.2 | 0.002 | 16/48 (HOP62, SNU-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.0 | 0.003 | 16/38 (SNU-423, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.9 | 0.004 | 13/48 (NCI-H1573, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.009 | 14/47 (A549, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 21/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.018 | 18/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.023 | 12/47 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.062 | 10/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -17.1 | 0e+00 | 38/48 (AN3 CA, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -9.8 | 4e-20 | 32/48 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -9.4 | 1e-18 | 36/48 (AN3 CA, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -6.9 | 9e-10 | 4/50 (AsPC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.875× | -4.4 | 0.001 | 8/48 (SNU-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.877× | -4.4 | 0.001 | 14/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.1 | 0.003 | 19/48 (RKO, LoVo, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.853× | -3.8 | 0.012 | 17/47 (C-33 A, HCT15, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.896× | -3.7 | 0.016 | 1/48 (H4) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.016 | 21/49 (LoVo, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.858× | -3.6 | 0.016 | 12/47 (BT-474, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.857× | -3.5 | 0.021 | 20/48 (A-172, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 59.0 | 7 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +17.1) | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.6) |
| [[J82 (line)]] | alt | 108 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -12.0) |
| [[A-172 (line)]] | wt | 150 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 71.7 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.66× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.2) |
| [[HS-578T (line)]] | alt | 56.0 | 4 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 86.4 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.03× (z +14.8) | — |
| [[SNU-423 (line)]] | alt | 91.7 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -8.6) |
| [[A498 (line)]] | wt | 101 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 102 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -11.8) |
| [[BT-474 (line)]] | alt | 68.8 | 0 | 4 (3 ⚠) | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.207× (z -11.5) |
| [[C-33 A (line)]] | alt | 138 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.7) |
| [[HCT15 (line)]] | alt | 99.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 63.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -10.2) |
| [[SW 900 (line)]] | alt | 108 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.7) | — |
| [[SW480 (line)]] | alt | 63.1 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +17.3) | — |
| [[A-427 (line)]] | wt | 45.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.5) |
| [[C32 (line)]] | wt | 60.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 39.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 100 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 55.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +15.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 188 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 63.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 60.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 74.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 94.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.8) |
| [[CHP-212 (line)]] | wt | 73.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.8) |
| [[H4 (line)]] | wt | 67.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.3) |
| [[Hs 766T (line)]] | wt | 45.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.1) |
| [[KATO III (line)]] | alt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -18.2) |
| [[LoVo (line)]] | wt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 38.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Peretinoin (drug)]] 5 µM 3.41× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 45.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 85.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.6) |
| [[SW48 (line)]] | wt | 111 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.25× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 180 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -17.1) |
| [[SHP-77 (line)]] | alt | 96.6 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.06× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -20.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 63.4 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.102× (z -9.3) |
| [[COLO 205 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUCA2]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 488 |
| [[APP]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation |
| [[LAPTM4B]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[IL13RA1]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CMPK1]] | +0.60 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[SCARB2]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[STT3B]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TMX1]] | +0.58 | +0.59 / +0.49 | both halves | 2e-05 |  |
| [[CNN3]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[DSG2]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP1]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RGP1]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TARS2]] | -0.56 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[NT5C]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ENDOV]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ZBTB48]] | -0.54 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[MTRES1]] | -0.53 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[RNF166]] | -0.53 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[CROCCP2-1]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[POLM]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[NFKBIL1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ENKD1]] | -0.53 | -0.31 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GOLM1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KCNIP3]] | B | KCNIP3 activity raises GOLM1's level | lines that do not express KCNIP3 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without KCNIP3 | 0.068 | ⚠ within organs, on part of the lines; also absent: MCF2L2, GOLGA2P5-1, DMBX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.6, -21.6); signed map (-22.4, -38.3). **Vector** length 115, 31.2% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.4 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +21.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -17.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | golgi membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:86,026,146-86,100,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GP73, FLJ23608, bA379P1.3; previously GOLPH2, C9orf155 |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBJ4](https://www.uniprot.org/uniprotkb/Q8NBJ4) (Golgi membrane protein 1):

> Unknown. Cellular response protein to viral infection.

**Summary**, from NCBI Gene [51280](https://www.ncbi.nlm.nih.gov/gene/51280):

> The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is a type II Golgi transmembrane protein. It processes proteins synthesized in the rough endoplasmic reticulum and assists in the transport of protein cargo through the Golgi apparatus. The expression of this gene has been observed to be upregulated in response to viral infection. Alternatively spliced transcript variants encoding the same …

**Accessions** — [HGNC:15451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15451) · Entrez [51280](https://www.ncbi.nlm.nih.gov/gene/51280) · UniProt [Q8NBJ4](https://www.uniprot.org/uniprotkb/Q8NBJ4) · Ensembl [ENSG00000135052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135052)

## Data

Gene col 5643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5643); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5643]; `tensor/DDL_lfc|DDL_z.npy` [5643]; `embed/gene_vectors.npy` [5643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5643 or target_col == 5643). Every well: [[GOLM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
