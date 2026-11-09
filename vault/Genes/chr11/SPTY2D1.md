---
symbol: "SPTY2D1"
type: "gene"
col: 11002
ensembl_id: "ENSG00000179119"
name: "SPT2 chromatin protein domain containing 1"
location: "11p15.1"
module: 41
arm: "+"
pooled_cpm: 99.65
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SPTY2D1

*SPT2 chromatin protein domain containing 1* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +12.8, q 2e-34, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.483× (z -9.1, q 5e-17, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.746× (z -3.8, q 0.020, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW48 0.112×, AN3 CA 0.0813×, A498 0.316×, NCI-H1573 0.301×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (H4 0.142×, A498 0.399×, hTERT-HPNE 0.257×, SW 1088 0.0682×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.173×, HS-578T 0.333×; ⚠ toxic; transcription drop); [[Amsacrine (drug)]] 0.5 µM in 1 line (CHP-212 0.0556×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0696×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF5]] (+0.84, fdr 7e-06), [[ACBD3]] (+0.83, fdr 7e-06), [[TMF1]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SEC23IP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +12.8 | 2e-34 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +10.9 | 5e-25 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +9.8 | 2e-20 | 41/48 (BT-474, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +8.6 | 1e-15 | 43/49 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.77×** | +7.5 | 1e-11 | 38/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.4 | 1e-11 | 37/49 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.65×** | +6.5 | 5e-09 | 35/48 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.61×** | +6.2 | 3e-08 | 35/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.55×** | +5.7 | 7e-07 | 33/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +5.2 | 1e-05 | 29/48 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.42×** | +4.4 | 5e-04 | 29/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.8 | 0.006 | 28/47 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +3.5 | 0.019 | 29/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.021 | 24/48 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.19× | +3.2 | 0.047 | 22/48 (SW1417, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.059 | 23/48 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 1.18× | +3.1 | 0.059 | 19/49 (NCI-H2347, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW48 0.112×, AN3 CA 0.0813×, A498 0.316×, NCI-H1573 0.301×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (H4 0.142×, A498 0.399×, hTERT-HPNE 0.257×, SW 1088 0.0682×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.173×, HS-578T 0.333×; ⚠ toxic; transcription drop); [[Amsacrine (drug)]] 0.5 µM in 1 line (CHP-212 0.0556×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -9.1 | 5e-17 | 39/44 (SW48, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.574×** | -7.2 | 1e-10 | 37/49 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -5.0 | 9e-05 | 28/45 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.746×** | -3.8 | 0.020 | 31/48 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.754×** | -3.5 | 0.048 | 29/48 (AsPC-1, HCT15, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.781× | -3.2 | 0.13 | 28/49 (LS 180, A549, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.849× | -3.0 | 0.21 | 19/48 (AsPC-1, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.8 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 68.3 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 65.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.0) | — |
| [[BT-474 (line)]] | alt | 64.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.57× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 122 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 89.9 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 76.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.4) | — |
| [[SW480 (line)]] | alt | 118 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.81× (z +9.5) | — |
| [[A-427 (line)]] | wt | 55.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.6) | — |
| [[C32 (line)]] | wt | 70.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 69.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 86.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 72.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 96.6 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.67× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.4× (z +8.6) | — |
| [[A498 (line)]] | wt | 232 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -12.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 207 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 94.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 135 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 63.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 90.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0813× (z -14.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 75.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 48.9 | 0 | 1 | — | [[Amsacrine (drug)]] 0.5 µM 0.0556× (z -12.0) |
| [[COLO 205 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.5) | — |
| [[H4 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -13.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0682× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 96.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0696× (z -11.9) |
| [[SW48 (line)]] | wt | 69.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF5]] | +0.84 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ACBD3]] | +0.83 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[TMF1]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SRP54]] | +0.79 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.77 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[OSBP]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[DIS3]] | +0.77 | +0.86 / +0.66 | both halves | 7e-06 |  |
| [[ARF4]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[PGM3]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC23IP]] | C | SEC23IP's natural level weakens SPTY2D1's drug response | SEC23IP's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.04; direction clear | 0.027 | ⚠ tissue can mimic it; precision caveat |
| [[ELP5]] | C | ELP5's natural level weakens SPTY2D1's drug response | ELP5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.23; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.874). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.3, -36.9); signed map (-50.9, 14.0). **Vector** length 123, 46.8% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.58 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.60 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SPT2 chromatin protein domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,606,403-18,634,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39441, DKFZp686I068, Spt2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68D10](https://www.uniprot.org/uniprotkb/Q68D10) (Protein SPT2 homolog):

> Histone chaperone that stabilizes pre-existing histone tetramers and regulates replication-independent histone exchange on chromatin. Required for normal chromatin refolding in the coding region of transcribed genes, and for the suppression of spurious transcription. Binds DNA and histones and promotes nucleosome assembly (in vitro). Facilitates formation of tetrameric histone complexes containing histone H3 and H4. Modulates RNA polymerase 1-mediated transcription (By similarity). Binds DNA, …

**Summary**, from NCBI Gene [144108](https://www.ncbi.nlm.nih.gov/gene/144108):

> Enables DNA binding activity; histone binding activity; and histone chaperone activity. Involved in heterochromatin formation; nucleosome assembly; and regulation of DNA-templated transcription. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26818) · Entrez [144108](https://www.ncbi.nlm.nih.gov/gene/144108) · UniProt [Q68D10](https://www.uniprot.org/uniprotkb/Q68D10) · Ensembl [ENSG00000179119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179119)

## Data

Gene col 11002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11002); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11002]; `tensor/DDL_lfc|DDL_z.npy` [11002]; `embed/gene_vectors.npy` [11002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11002 or target_col == 11002). Every well: [[SPTY2D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTY2D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
