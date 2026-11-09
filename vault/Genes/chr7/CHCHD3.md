---
symbol: "CHCHD3"
type: "gene"
col: 2775
ensembl_id: "ENSG00000106554"
name: "coiled-coil-helix-coiled-coil-helix domain containing 3"
location: "7q32.3-q33"
module: 4
arm: "+"
pooled_cpm: 147.45
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CHCHD3

*coiled-coil-helix-coiled-coil-helix domain containing 3* — 7q32.3-q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +18.9, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.02× (z +18.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.846× (z -4.3, q 0.009, down in 20 of 49 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.814× (z -3.8, q 0.040, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.317×, NCI-H23 0.570×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.808×; ⚠ position not correctable); [[Docetaxel (drug)]] 0.05 µM in 1 line (RPMI-7951 0.456×; ⚠ transcription drop; cell-cycle shift, explains ~22% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.522×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIPR1]] (+0.69, fdr 7e-06), [[TMEM33]] (+0.68, fdr 7e-06), [[SPATA5]] (+0.68, fdr 7e-06); moves opposite to [[RSRP1]] (-0.68, fdr 1e-05), [[KDM5B]] (-0.66, fdr 7e-06), [[KATNA1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OVOL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.09×** | +18.9 | 0e+00 | 47/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.02×** | +18.0 | 0e+00 | 48/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.92×** | +16.7 | 0e+00 | 47/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.86×** | +15.9 | 0e+00 | 46/48 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +15.7 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.80×** | +15.1 | 0e+00 | 45/48 (C32, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.73×** | +14.1 | 6e-43 | 48/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +13.9 | 3e-42 | 36/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +10.7 | 7e-25 | 38/47 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +10.1 | 5e-22 | 31/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +9.4 | 4e-19 | 33/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +8.2 | 9e-15 | 38/48 (C32, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +8.0 | 6e-14 | 35/49 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.39×** | +7.8 | 3e-13 | 32/45 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +7.6 | 1e-12 | 41/45 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +7.6 | 1e-12 | 32/48 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.5 | 2e-12 | 33/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.4 | 3e-12 | 31/48 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +7.1 | 3e-11 | 33/48 (SNU-423, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +6.7 | 6e-10 | 41/48 (C32, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +6.3 | 6e-09 | 39/48 (PANC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +6.0 | 4e-08 | 33/48 (PANC-1, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.317×, NCI-H23 0.570×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.808×; ⚠ position not correctable); [[Docetaxel (drug)]] 0.05 µM in 1 line (RPMI-7951 0.456×; ⚠ transcription drop; cell-cycle shift, explains ~22% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.522×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.846× | -4.3 | 0.009 | 20/49 (C32, A-172, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.814×** | -3.8 | 0.040 | 21/48 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.840× | -3.2 | 0.23 | 14/47 (SW 1271, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 100 | 15 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +15.5) | — |
| [[NCI-H460 (line)]] | wt | 153 | 14 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +26.3) | — |
| [[A-172 (line)]] | wt | 94.0 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +23.5) | — |
| [[C32 (line)]] | wt | 330 | 11 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.16× (z +15.9) | — |
| [[SNU-423 (line)]] | alt | 113 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +21.3) | — |
| [[HS-578T (line)]] | alt | 136 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.6) | — |
| [[SW480 (line)]] | alt | 191 | 10 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +15.5) | — |
| [[A549 (line)]] | wt | 102 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +12.1) | — |
| [[J82 (line)]] | alt | 167 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +21.2) | — |
| [[LoVo (line)]] | wt | 205 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.59× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 8 (5 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.68× (z +12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 112 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 117 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.7) | — |
| [[A498 (line)]] | wt | 243 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +14.6) | — |
| [[H4 (line)]] | wt | 114 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.72× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 130 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 239 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.570× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 107 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.9) | [[Docetaxel (drug)]] 0.05 µM 0.456× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[SK-MEL-2 (line)]] | alt | 152 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.03× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 127 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.44× (z +14.3) | — |
| [[hTERT-HPNE (line)]] | wt | 97.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 247 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 230 | 5 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 89.0 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 77.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 155 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.19× (z +13.5) | — |
| [[RKO (line)]] | wt | 268 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 77.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 94.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.10× (z +9.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 154 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[LS 180 (line)]] | wt | 107 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 61.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 283 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[KATO III (line)]] | alt | 153 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.522× (z -9.1) |
| [[A-427 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIPR1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.68 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.68 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[HERC2]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CCT5]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[CCT3]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[CCT2]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[TMX3]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 | same gene group |
| [[VTI1A]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 | same gene group |
| [[LRPPRC]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.68 | -0.49 / -0.75 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[KATNA1]] | -0.65 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.64 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[KLHL28]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.61 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[ACAP1]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[CCS]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | -0.60 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 | same gene group |
| [[MINDY2]] | -0.59 | -0.68 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity lowers CHCHD3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.23× higher at baseline in the lines without OVOL1 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TNFRSF10C]] | B | TNFRSF10C activity lowers CHCHD3's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.40× higher at baseline in the lines without TNFRSF10C | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.0, -35.7); signed map (-12.9, -47.2). **Vector** length 110, 37.4% of its response variance represented; |z| ≥ 3 in 1,561 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.55 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.50 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.1 | +14.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.3 | +18.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +15.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.4 | +7.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.7 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.9 | +5.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.3 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | +13.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.3-q33 — chr7:132,784,870-133,082,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20420, MINOS3, PPP1R22, Mic19, MICOS19 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins; Protein phosphatase 1 regulatory subunits; Mitochondrial contact site and cristae organizing system subunits; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Cristae formation; Mitochondrial protein import; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX63](https://www.uniprot.org/uniprotkb/Q9NX63) (MICOS complex subunit MIC19):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane. Plays an important role in the maintenance of the MICOS complex stability and the mitochondrial cristae morphology. Has also been shown to function as a transcription factor which binds to the BAG1 promoter and represses BAG1 transcription.

**Summary**, from NCBI Gene [54927](https://www.ncbi.nlm.nih.gov/gene/54927):

> The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:21906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21906) · Entrez [54927](https://www.ncbi.nlm.nih.gov/gene/54927) · UniProt [Q9NX63](https://www.uniprot.org/uniprotkb/Q9NX63) · Ensembl [ENSG00000106554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106554)

## Data

Gene col 2775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2775); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2775]; `tensor/DDL_lfc|DDL_z.npy` [2775]; `embed/gene_vectors.npy` [2775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2775 or target_col == 2775). Every well: [[CHCHD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
