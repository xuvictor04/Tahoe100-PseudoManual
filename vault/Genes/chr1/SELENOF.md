---
symbol: "SELENOF"
type: "gene"
col: 11389
ensembl_id: "ENSG00000183291"
name: "selenoprotein F"
location: "1p22.3"
module: 29
arm: "+"
pooled_cpm: 99.22
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SELENOF

*selenoprotein F* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +23.3, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.723× (z -12.2, q 1e-31, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDOST]] (+0.62, fdr 1e-05), [[KARS1]] (+0.62, fdr 1e-05), [[AP2B1]] (+0.61, fdr 1e-05); moves opposite to [[MAP1S]] (-0.61, fdr 5e-05), [[KRI1]] (-0.58, fdr 4e-05), [[TUBB4B]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +23.3 | 0e+00 | 46/49 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +16.7 | 0e+00 | 44/49 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +16.5 | 0e+00 | 39/44 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +11.0 | 5e-26 | 36/45 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +10.8 | 6e-25 | 32/50 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +8.2 | 3e-14 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +6.8 | 8e-10 | 31/49 (Hs 766T, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.6 | 4e-09 | 30/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +5.5 | 2e-06 | 26/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.1 | 2e-05 | 16/48 (HOP62, A-172, …) | top dose only |  |
| [[Lopinavir (drug)]] 5 µM |  | 1.16× | +3.9 | 0.004 | 16/47 (LoVo, LOX-IMVI, …) | top dose only | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.094 | 8/47 (NCI-H2030, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.11 | 7/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.723×** | -12.2 | 1e-31 | 36/48 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.699×** | -9.6 | 3e-19 | 35/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.734×** | -8.3 | 2e-14 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.808×** | -5.7 | 2e-06 | 25/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.826×** | -5.1 | 3e-05 | 25/48 (RPMI-7951, LS 180, …) | inconsistent across doses | position effect removed |
| [[Cilostazol (drug)]] 5 µM |  | **0.827×** | -4.9 | 9e-05 | 22/48 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.849× | -4.4 | 9e-04 | 19/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.850× | -4.4 | 9e-04 | 20/48 (hTERT-HPNE, HS-578T, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -4.1 | 0.002 | 20/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | 0.859× | -4.1 | 0.002 | 19/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.860× | -4.0 | 0.003 | 17/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.862× | -4.0 | 0.003 | 19/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.902× | -3.9 | 0.004 | 3/48 (RKO, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.884× | -3.3 | 0.037 | 16/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Finasteride (drug)]] 5 µM |  | 0.883× | -3.2 | 0.049 | 8/48 (HS-578T, C-33 A, …) | top dose only | position effect removed |
| [[Resveratrol (drug)]] 0.5 µM |  | 0.896× | -3.0 | 0.096 | 11/49 (NCI-H1792, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 68.9 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +15.4) | — |
| [[LoVo (line)]] | wt | 109 | 3 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.520× (z -10.4) |
| [[SW480 (line)]] | alt | 103 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.562× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 97.3 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +19.1) | — |
| [[HS-578T (line)]] | alt | 132 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +13.7) | — |
| [[J82 (line)]] | alt | 94.8 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -9.8) |
| [[KATO III (line)]] | alt | 115 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.639× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 92.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 73.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 95.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 133 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +18.4) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 70.1 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -9.6) |
| [[PANC-1 (line)]] | alt | 111 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +19.3) | — |
| [[RKO (line)]] | wt | 96.2 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 107 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -10.1) |
| [[A-172 (line)]] | wt | 51.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +13.8) | — |
| [[A-427 (line)]] | wt | 76.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.24× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 158 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.636× (z -8.8) |
| [[A549 (line)]] | wt | 67.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +13.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.7) | — |
| [[H4 (line)]] | wt | 75.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 95.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.6) | [[OTS514 (drug)]] 5 µM 0.169× (z -9.2) |
| [[Hs 766T (line)]] | wt | 129 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 93.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.474× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 104 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +16.0) | [[Homoharringtonine (drug)]] 5 µM 0.637× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 76.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 119 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.6) |
| [[SW48 (line)]] | wt | 92.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 98.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 78.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 89.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.335× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[hTERT-HPNE (line)]] | wt | 100 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 97.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +13.5) | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0691× (z -12.4) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 121 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +15.7) | — |
| [[AN3 CA (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDOST]] | +0.62 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[KARS1]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[AP2B1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SDHD]] | +0.60 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TMED10]] | +0.60 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[STT3A]] | +0.59 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZNF75D]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PDIA3]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[COPB2]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TM9SF3]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[STRADB]] | +0.57 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[TMEM167A]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1S]] | -0.61 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[KRI1]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[TUBB4B]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ORAI1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PIAS4]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[MAP2K7]] | -0.55 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[LRRC8E]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZDHHC18]] | -0.54 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MIDN]] | -0.54 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[GGA1]] | -0.54 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ABCF1]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[SIGIRR]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SELENOF's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SELENOF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.2, -21.2); signed map (-20.1, -31.3). **Vector** length 122, 33.4% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +23.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +11.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.4 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.2 | +0.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | -5.5 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.1 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -4.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:86,862,445-86,914,424 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEP15 |
| Gene groups (HGNC) | Selenoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O60613](https://www.uniprot.org/uniprotkb/O60613) (Selenoprotein F):

> May be involved in redox reactions associated with the formation of disulfide bonds (By similarity). May contribute to the quality control of protein folding in the endoplasmic reticulum. May regulate protein folding by enhancing the catalytic activity of UGGT1/UGCGL1 and UGGT2/UGCGL2.

**Summary**, from NCBI Gene [9403](https://www.ncbi.nlm.nih.gov/gene/9403):

> The protein encoded by this gene belongs to the SEP15/selenoprotein M family. The exact function of this protein is not known; however, it has been found to associate with UDP-glucose:glycoprotein glucosyltransferase (UGTR), an endoplasmic reticulum(ER)-resident protein, which is involved in the quality control of protein folding. The association with UGTR retains this protein in the ER, where it may play a role in protein folding. It has also been suggested to have a role in cancer etiology. …

**Accessions** — [HGNC:17705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17705) · Entrez [9403](https://www.ncbi.nlm.nih.gov/gene/9403) · UniProt [O60613](https://www.uniprot.org/uniprotkb/O60613) · Ensembl [ENSG00000183291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183291)

## Data

Gene col 11389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11389); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11389]; `tensor/DDL_lfc|DDL_z.npy` [11389]; `embed/gene_vectors.npy` [11389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11389 or target_col == 11389). Every well: [[SELENOF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
