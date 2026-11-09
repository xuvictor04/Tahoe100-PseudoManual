---
symbol: "NPLOC4"
type: "gene"
col: 11286
ensembl_id: "ENSG00000182446"
name: "NPL4 homolog, ubiquitin recognition factor"
location: "17q25.3"
module: 36
arm: "+"
pooled_cpm: 115.94
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NPLOC4

*NPL4 homolog, ubiquitin recognition factor* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.19× (z +25.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.712× (z -7.6, q 6e-12, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC10]] (+0.72, fdr 7e-06), [[NDOR1]] (+0.68, fdr 7e-06), [[PSMB3]] (+0.68, fdr 7e-06); moves opposite to [[SNX2]] (-0.60, fdr 1e-05), [[NDUFA5]] (-0.57, fdr 1e-05), [[RYBP]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.19×** | +25.9 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.68×** | +22.0 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.64×** | +20.5 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +13.4 | 5e-39 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +11.4 | 3e-28 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +10.9 | 2e-25 | 40/49 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +10.8 | 4e-25 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +10.2 | 2e-22 | 43/48 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +10.1 | 4e-22 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +9.8 | 6e-21 | 37/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +9.5 | 8e-20 | 42/49 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.81×** | +9.4 | 2e-19 | 45/49 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +8.9 | 2e-17 | 39/45 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +8.5 | 1e-15 | 36/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.7 | 7e-13 | 36/50 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +7.2 | 3e-11 | 39/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +6.9 | 2e-10 | 29/48 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 3e-07 | 30/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.712×** | -7.6 | 6e-12 | 38/49 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -7.6 | 6e-12 | 28/49 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -7.6 | 6e-12 | 36/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -7.5 | 6e-12 | 32/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.743×** | -6.7 | 3e-09 | 35/48 (H4, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -6.1 | 1e-07 | 25/44 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.841× | -3.9 | 0.007 | 19/48 (KATO III, NCI-H1573, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.855× | -3.6 | 0.027 | 12/48 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.855× | -3.3 | 0.050 | 22/45 (SNU-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 0.865× | -3.3 | 0.050 | 17/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.866× | -3.3 | 0.050 | 10/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.866× | -3.3 | 0.050 | 14/48 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.3 | 0.050 | 19/49 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.869× | -3.2 | 0.058 | 15/48 (KATO III, A-172, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.771×** | -3.1 | 0.081 | 15/47 (BT-474, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.876× | -3.0 | 0.097 | 13/48 (NCI-H1573, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 112 | 14 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.29× (z +23.0) | — |
| [[COLO 205 (line)]] | alt | 83.4 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.83× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 94.1 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.26× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 123 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.42× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 137 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 134 | 7 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.41× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.535× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 122 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +18.0) | — |
| [[HOP62 (line)]] | alt | 116 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +17.6) | — |
| [[LoVo (line)]] | wt | 96.7 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +17.6) | — |
| [[SNU-423 (line)]] | alt | 105 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.49× (z +14.7) | — |
| [[C32 (line)]] | wt | 100 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.5) | — |
| [[HCT15 (line)]] | alt | 77.3 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.99× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 104 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.37× (z +21.9) | — |
| [[KATO III (line)]] | alt | 123 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.27× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 113 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +14.1) | [[Selinexor (drug)]] 5 µM 0.666× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 54.2 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.19× (z +15.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 123 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 99.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.1) | — |
| [[A-427 (line)]] | wt | 152 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +11.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 122 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.479× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 69.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +16.8) | — |
| [[HS-578T (line)]] | alt | 84.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 75.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +17.0) | — |
| [[Panc 03.27 (line)]] | alt | 140 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 121 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.59× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -18.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 136 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.57× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.472× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 138 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 129 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 137 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +12.1) | — |
| [[A498 (line)]] | wt | 128 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +13.7) | — |
| [[H4 (line)]] | wt | 80.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.88× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 96.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.07× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 270 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.02× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.539× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 75.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 107 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 155 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 58.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 94.3 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 118 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[RKO (line)]] | wt | 114 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC10]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[NDOR1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 543 |
| [[MEF2B]] | +0.66 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[TMEM11-DT]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[UFD1]] | +0.65 | +0.67 / +0.70 | both halves | 7e-06 | same gene group; pathway: Cellular response to chemical stress; STRING 999 |
| [[C1orf159]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.64 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 555 |
| [[ABCB8]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[VPS53]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SFXN5]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RYBP]] | -0.56 | -0.51 / -0.61 | both halves | 1e-05 | same gene group |
| [[IRF2BP2]] | -0.54 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ARL4A]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[EBAG9]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[NUDCD2]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ARHGAP12]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PRPF39]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[AMOT]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[NR1D1]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[PIP4P2]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-14.8, -8.6); signed map (-45.7, -22.4). **Vector** length 117, 40.8% of its response variance represented; |z| ≥ 3 in 1,451 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.2 | +25.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +20.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +22.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +9.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.9 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.1 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.3 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.1 | -7.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.0 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -0.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | NPL4 homolog, ubiquitin recognition factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,556,887-81,648,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NPL4, FLJ20657, KIAA1499 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; VCP-Ufd1-Npl4 complex subunits |
| Reactome | 15 pathways, smallest: Translesion Synthesis by POLH; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAT6](https://www.uniprot.org/uniprotkb/Q8TAT6) (Nuclear protein localization protein 4 homolog):

> The ternary complex containing UFD1, VCP and NPLOC4 binds ubiquitinated proteins and is necessary for the export of misfolded proteins from the ER to the cytoplasm, where they are degraded by the proteasome. The NPLOC4-UFD1-VCP complex regulates spindle disassembly at the end of mitosis and is necessary for the formation of a closed nuclear envelope (By similarity). Acts as a negative regulator of type I interferon production via the complex formed with VCP and UFD1, which binds to RIGI and …

**Summary**, from NCBI Gene [55666](https://www.ncbi.nlm.nih.gov/gene/55666):

> Predicted to enable ubiquitin binding activity and ubiquitin protein ligase binding activity. Predicted to contribute to K48-linked polyubiquitin modification-dependent protein binding activity and K63-linked polyubiquitin modification-dependent protein binding activity. Involved in negative regulation of RIG-I signaling pathway; negative regulation of type I interferon production; and protein catabolic process. Located in nucleoplasm. Part of UFD1-NPL4 complex and VCP-NPL4-UFD1 AAA ATPase …

**Accessions** — [HGNC:18261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18261) · Entrez [55666](https://www.ncbi.nlm.nih.gov/gene/55666) · UniProt [Q8TAT6](https://www.uniprot.org/uniprotkb/Q8TAT6) · Ensembl [ENSG00000182446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182446)

## Data

Gene col 11286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11286); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11286]; `tensor/DDL_lfc|DDL_z.npy` [11286]; `embed/gene_vectors.npy` [11286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11286 or target_col == 11286). Every well: [[NPLOC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPLOC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
