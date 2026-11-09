---
symbol: "PHF14"
type: "gene"
col: 2760
ensembl_id: "ENSG00000106443"
name: "PHD finger protein 14"
location: "7p21.3"
module: 1
arm: "+"
pooled_cpm: 222.79
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PHF14

*PHD finger protein 14* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.32× (z +5.2, q 1e-04, up in 31 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.34× (z +4.9, q 3e-04, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.454× (z -14.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA25]] (+0.73, fdr 7e-06), [[PUM3]] (+0.72, fdr 7e-06), [[COX10]] (+0.72, fdr 7e-06); moves opposite to [[WDTC1]] (-0.59, fdr 1e-05), [[PRKACA]] (-0.58, fdr 1e-05), [[PJA2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.2 | 1e-04 | 31/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +4.9 | 3e-04 | 32/48 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.63×** | +4.8 | 4e-04 | 36/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.004 | 28/47 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +4.0 | 0.006 | 17/48 (NCI-H2347, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.21× | +3.3 | 0.11 | 20/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.11 | 17/48 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.21× | +3.2 | 0.11 | 20/48 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.16 | 15/48 (SW48, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -14.7 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.598×** | -13.5 | 3e-39 | 40/48 (PANC-1, SW1417, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.507×** | -12.6 | 2e-34 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -11.1 | 1e-26 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.579×** | -10.2 | 4e-22 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -9.4 | 3e-19 | 37/49 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -8.2 | 2e-14 | 45/49 (PANC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.669×** | -7.2 | 4e-11 | 37/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.680×** | -7.2 | 5e-11 | 35/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -6.5 | 5e-09 | 41/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.742×** | -5.5 | 2e-06 | 33/48 (LOX-IMVI, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.762×** | -4.9 | 6e-05 | 29/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.784×** | -4.5 | 3e-04 | 32/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -4.0 | 0.002 | 33/48 (SW48, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.787×** | -4.0 | 0.002 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.831×** | -3.4 | 0.019 | 24/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.831×** | -3.4 | 0.019 | 22/48 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.837× | -3.2 | 0.042 | 19/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Auranofin (drug)]] 5 µM |  | 0.850× | -3.0 | 0.061 | 20/48 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.845× | -3.0 | 0.061 | 19/48 (SW 900, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 323 | 0 | 12 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -15.3) |
| [[PANC-1 (line)]] | alt | 453 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -23.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -20.9) |
| [[KATO III (line)]] | alt | 340 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 259 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -16.6) |
| [[SW480 (line)]] | alt | 397 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -21.3) |
| [[LOX-IMVI (line)]] | wt | 311 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -14.8) |
| [[SW48 (line)]] | wt | 453 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -11.6) |
| [[A-427 (line)]] | wt | 301 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -28.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 234 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -15.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.438× (z -11.2) |
| [[RKO (line)]] | wt | 242 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -18.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.5) |
| [[SW1417 (line)]] | alt | 270 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -19.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -15.7) |
| [[BT-474 (line)]] | alt | 148 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -15.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.293× (z -12.8) |
| [[H4 (line)]] | wt | 447 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 265 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -15.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 162 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -10.6) |
| [[AN3 CA (line)]] | alt | 359 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.298× (z -10.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.0) |
| [[C-33 A (line)]] | alt | 277 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.466× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.517× (z -8.5) |
| [[HOP62 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -10.1) |
| [[LS 180 (line)]] | wt | 157 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -12.4) |
| [[SHP-77 (line)]] | alt | 353 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.452× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.508× (z -9.4) |
| [[SW 900 (line)]] | alt | 128 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -11.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.404× (z -9.2) |
| [[A-172 (line)]] | wt | 157 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.0) ⚠ cell-cycle shift, explains ~69% of this change | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 228 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -18.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 175 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -14.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.0) |
| [[COLO 205 (line)]] | alt | 182 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -11.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.2) |
| [[HCT15 (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 167 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -9.5) |
| [[HS-578T (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0829× (z -13.3) ⚠ toxic |
| [[J82 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -8.8) |
| [[LoVo (line)]] | wt | 271 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.476× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 245 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.425× (z -10.0) |
| [[CHP-212 (line)]] | wt | 244 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 133 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.411× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 81.5 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.27× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[RPMI-7951 (line)]] | alt | 232 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.470× (z -8.5) |
| [[SNU-1 (line)]] | wt | 285 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW 1088 (line)]] | alt | 199 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.149× (z -9.2) |
| [[SW 1271 (line)]] | alt | 253 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 150 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA25]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[PUM3]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[COX10]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[LTV1]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[UTP20]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TTC27]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[DDX10]] | +0.70 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[THADA]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[DPH6]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[DHX37]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[NOP16]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDTC1]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PJA2]] | -0.57 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[APAF1]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.0, -33.8); signed map (5.9, -42.7). **Vector** length 122, 45.7% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.8 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +6.7 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.8 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.2 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.0 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.0 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -9.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.6 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:10,973,336-11,169,623 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0783 |
| Gene groups (HGNC) | PHD finger proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O94880](https://www.uniprot.org/uniprotkb/O94880) (PHD finger protein 14):

> Histone-binding protein. Binds preferentially to unmodified histone H3 but can also bind to a lesser extent to histone H3 trimethylated at 'Lys-9' (H3K9me3) as well as to histone H3 monomethylated at 'Lys-27' (H3K27ac) and trimethylated at 'Lys-27' (H3K27me3) (By similarity). Represses PDGFRA expression, thus playing a role in regulation of mesenchymal cell proliferation (By similarity). Suppresses the expression of CDKN1A/p21 by reducing the level of trimethylation of histone H3 'Lys-4', …

**Summary**, from NCBI Gene [9678](https://www.ncbi.nlm.nih.gov/gene/9678):

> Enables histone binding activity. Predicted to be involved in several processes, including germinal center B cell differentiation; negative regulation of mesenchymal cell proliferation involved in lung development; and negative regulation of platelet-derived growth factor receptor-alpha signaling pathway. Located in chromatin; cytoplasm; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22203) · Entrez [9678](https://www.ncbi.nlm.nih.gov/gene/9678) · UniProt [O94880](https://www.uniprot.org/uniprotkb/O94880) · Ensembl [ENSG00000106443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106443)

## Data

Gene col 2760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2760); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2760]; `tensor/DDL_lfc|DDL_z.npy` [2760]; `embed/gene_vectors.npy` [2760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2760 or target_col == 2760). Every well: [[PHF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
