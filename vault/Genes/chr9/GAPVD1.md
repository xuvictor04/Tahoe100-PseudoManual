---
symbol: "GAPVD1"
type: "gene"
col: 9089
ensembl_id: "ENSG00000165219"
name: "GTPase activating protein and VPS9 domains 1"
location: "9q33.3"
module: 169
arm: "+"
pooled_cpm: 130.06
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# GAPVD1

*GTPase activating protein and VPS9 domains 1* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.27× (z +17.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.563× (z -16.1, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.204×, NCI-H460 0.345×, SK-MEL-2 0.309×, SNU-1 0.284×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-1 0.0978×, HEC-1-A 0.280×, LS 180 0.183×, NCI-H2347 0.397×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.327×, KATO III 0.349×, NCI-H2347 0.426×; ⚠ toxic; transcription drop); [[Monocrotaline (drug)]] 5 µM in 1 line (SW 1088 0.0841×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1088 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC24B]] (+0.70, fdr 7e-06), [[PPP2R5E]] (+0.69, fdr 7e-06), [[ASB7]] (+0.67, fdr 1e-05); moves opposite to [[PHF19]] (-0.63, fdr 3e-05), [[IER2]] (-0.63, fdr 7e-06), [[SRSF6]] (-0.58, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.27×** | +17.3 | 0e+00 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +17.2 | 0e+00 | 47/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +12.4 | 7e-33 | 43/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +11.8 | 5e-30 | 42/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +9.7 | 3e-20 | 39/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +9.5 | 3e-19 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +9.1 | 1e-17 | 43/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +9.0 | 1e-17 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +7.9 | 2e-13 | 37/48 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +7.9 | 2e-13 | 33/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.8 | 4e-13 | 35/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +7.2 | 3e-11 | 29/47 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +6.7 | 1e-09 | 28/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.5 | 4e-09 | 32/45 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +6.0 | 6e-08 | 27/48 (LoVo, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +5.4 | 3e-06 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 19/49 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.8 | 0.004 | 5/49 (A549, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9089.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.204×, NCI-H460 0.345×, SK-MEL-2 0.309×, SNU-1 0.284×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-1 0.0978×, HEC-1-A 0.280×, LS 180 0.183×, NCI-H2347 0.397×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.327×, KATO III 0.349×, NCI-H2347 0.426×; ⚠ toxic; transcription drop); [[Monocrotaline (drug)]] 5 µM in 1 line (SW 1088 0.0841×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1088 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.563×** | -16.1 | 0e+00 | 44/49 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -13.6 | 1e-39 | 35/44 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.707×** | -9.0 | 4e-17 | 32/45 (C32, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -7.5 | 7e-12 | 0/50 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.852× | -4.5 | 7e-04 | 19/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.856× | -4.2 | 0.002 | 20/47 (J82, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.872× | -3.6 | 0.030 | 10/47 (A549, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.887× | -3.3 | 0.081 | 14/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.893× | -3.2 | 0.088 | 4/47 (HS-578T, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 94.1 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +14.3) | — |
| [[LoVo (line)]] | wt | 124 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.564× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 150 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -18.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 129 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +17.8) | — |
| [[BT-474 (line)]] | alt | 178 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +15.8) | — |
| [[HEC-1-A (line)]] | alt | 167 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.46× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -19.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 205 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 138 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 168 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 124 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 119 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 129 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.36× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.430× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 242 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -24.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 188 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.79× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.576× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -13.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 151 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.74× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 151 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 178 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 57.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.56× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 155 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 98.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.01× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -15.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0978× (z -25.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 112 | 0 | 2 | — | [[Monocrotaline (drug)]] 5 µM 0.0841× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.5) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[HS-578T (line)]] | alt | 97.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.43× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 130 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.526× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 171 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24B]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[PPP2R5E]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ASB7]] | +0.67 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[BMT2]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TRPC4AP]] | +0.65 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[CLPP]] | +0.63 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RELCH]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TENT2]] | +0.60 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[DEXI]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[LAMTOR2]] | +0.59 | +0.64 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF19]] | -0.63 | -0.73 / -0.43 | both halves | 3e-05 |  |
| [[IER2]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[SRSF6]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SFR1]] | -0.58 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[JUNB]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[THOC6]] | -0.58 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[HUS1]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[LINC00460]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[MMRN2]] | -0.56 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[CD22]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[CELSR3]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZNF641]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.8, -8.9); signed map (-35.3, -7.0). **Vector** length 93.3, 26.5% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.1 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +11.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.5 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | +2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | GTPase activating protein and VPS9 domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:125,261,794-125,367,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434C212, KIAA1521 |
| Gene groups (HGNC) | VPS9 domain containing |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 5 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14C86](https://www.uniprot.org/uniprotkb/Q14C86) (GTPase-activating protein and VPS9 domain-containing protein 1):

> Acts both as a GTPase-activating protein (GAP) and a guanine nucleotide exchange factor (GEF), and participates in various processes such as endocytosis, insulin receptor internalization or LC2A4/GLUT4 trafficking. Acts as a GEF for the Ras-related protein RAB31 by exchanging bound GDP for free GTP, leading to regulate LC2A4/GLUT4 trafficking. In the absence of insulin, it maintains RAB31 in an active state and promotes a futile cycle between LC2A4/GLUT4 storage vesicles and early endosomes, …

**Summary**, from NCBI Gene [26130](https://www.ncbi.nlm.nih.gov/gene/26130):

> Enables GTPase activating protein binding activity and guanyl-nucleotide exchange factor activity. Involved in regulation of protein transport. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23375) · Entrez [26130](https://www.ncbi.nlm.nih.gov/gene/26130) · UniProt [Q14C86](https://www.uniprot.org/uniprotkb/Q14C86) · Ensembl [ENSG00000165219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165219)

## Data

Gene col 9089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9089); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9089]; `tensor/DDL_lfc|DDL_z.npy` [9089]; `embed/gene_vectors.npy` [9089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9089 or target_col == 9089). Every well: [[GAPVD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAPVD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
