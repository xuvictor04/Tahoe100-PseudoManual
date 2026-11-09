---
symbol: "RAB18"
type: "gene"
col: 1784
ensembl_id: "ENSG00000099246"
name: "RAB18, member RAS oncogene family"
location: "10p12.1"
module: 30
arm: "+"
pooled_cpm: 119.24
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RAB18

*RAB18, member RAS oncogene family* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.73× (z +7.8, q 5e-12, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.608× (z -6.8, q 7e-09, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.734× (z -4.4, q 0.002, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTCA]] (+0.73, fdr 7e-06), [[OTULIN]] (+0.68, fdr 9e-06), [[STAM]] (+0.68, fdr 7e-06); moves opposite to [[THOC6]] (-0.65, fdr 2e-05), [[SKIL]] (-0.61, fdr 1e-05), [[SRCAP]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +7.8 | 5e-12 | 46/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +7.4 | 5e-11 | 41/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.6 | 9e-09 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +6.5 | 2e-08 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +5.7 | 1e-06 | 38/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +5.6 | 2e-06 | 39/48 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +5.6 | 2e-06 | 40/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +5.3 | 7e-06 | 37/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 39/49 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.4 | 6e-04 | 30/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.001 | 25/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.001 | 32/48 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.007 | 23/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.6 | 0.011 | 29/45 (RKO, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.017 | 28/49 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.020 | 27/48 (HT-29, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.034 | 26/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -6.8 | 7e-09 | 36/44 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.2 | 2e-07 | 35/49 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -4.6 | 9e-04 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.734×** | -4.4 | 0.002 | 39/48 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.747×** | -4.1 | 0.004 | 33/48 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.748×** | -4.1 | 0.004 | 34/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.015 | 32/48 (SNU-423, CHP-212, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.774×** | -3.6 | 0.018 | 29/48 (LOX-IMVI, H4, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -3.6 | 0.018 | 25/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.782×** | -3.5 | 0.028 | 30/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.835× | -3.4 | 0.035 | 23/49 (NCI-H460, A-172, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.791×** | -3.3 | 0.041 | 23/49 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.043 | 28/48 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.806×** | -3.1 | 0.088 | 21/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.807×** | -3.0 | 0.089 | 21/48 (SW480, HOP62, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.809×** | -3.0 | 0.089 | 22/49 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.089 | 18/49 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.813×** | -2.9 | 0.093 | 20/48 (SW 1088, A-172, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.814×** | -2.9 | 0.093 | 20/48 (H4, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.8 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.55× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +12.9) | — |
| [[LoVo (line)]] | wt | 87.1 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.31× (z +11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 150 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.3) ⚠ cell-cycle shift, explains ~8% of this change |
| [[AsPC-1 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 73.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 76.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.79× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW 900 (line)]] | alt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 89.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.0) | — |
| [[A-427 (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 238 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.5) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[CFPAC-1 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 102 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 95.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0861× (z -18.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 129 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 124 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 154 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[OTULIN]] | +0.68 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[STAM]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 | same gene group; pathway: COPI-independent Golgi-to-ER retrograde traffic; STRING 753 |
| [[MAX]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.64 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.64 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.64 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[DHRS1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.63 | +0.74 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.65 | -0.70 / -0.48 | both halves | 2e-05 |  |
| [[SKIL]] | -0.61 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.61 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[HES1]] | -0.57 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[PHF19]] | -0.57 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SP2]] | -0.57 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.57 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[EPC2]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[REXO1]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[EGR1]] | -0.56 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.56 | -0.64 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-5.6, -12.0); signed map (-34.2, -16.2). **Vector** length 101, 36.0% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -6.1 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.7 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Tirabrutinib (drug)]] 0.5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB18, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:27,504,174-27,543,207 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 10 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP72](https://www.uniprot.org/uniprotkb/Q9NP72) (Ras-related protein Rab-18):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB18 is required for the localization of ZFYVE1 to lipid droplets and for its function in mediating the formation of …

**Summary**, from NCBI Gene [22931](https://www.ncbi.nlm.nih.gov/gene/22931):

> The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:14244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14244) · Entrez [22931](https://www.ncbi.nlm.nih.gov/gene/22931) · UniProt [Q9NP72](https://www.uniprot.org/uniprotkb/Q9NP72) · Ensembl [ENSG00000099246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099246)

## Data

Gene col 1784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1784); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1784]; `tensor/DDL_lfc|DDL_z.npy` [1784]; `embed/gene_vectors.npy` [1784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1784 or target_col == 1784). Every well: [[RAB18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
