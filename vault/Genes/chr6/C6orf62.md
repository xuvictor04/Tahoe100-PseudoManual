---
symbol: "C6orf62"
type: "gene"
col: 3355
ensembl_id: "ENSG00000112308"
name: "chromosome 6 open reading frame 62"
location: "6p22.3"
module: 38
arm: "+"
pooled_cpm: 180.25
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# C6orf62

*chromosome 6 open reading frame 62* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +20.6, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.707× (z -7.5, q 5e-11, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.715× (z -7.2, q 2e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRIF1]] (+0.78, fdr 7e-06), [[MED29]] (+0.71, fdr 1e-05), [[GARIN1A]] (+0.70, fdr 9e-06); moves opposite to [[GCSH]] (-0.68, fdr 1e-05), [[FAM102B]] (-0.67, fdr 1e-05), [[KDM1A]] (-0.64, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Nimesulide (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +20.6 | 0e+00 | 42/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +13.6 | 6e-40 | 41/49 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +12.5 | 1e-33 | 43/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +8.3 | 2e-14 | 36/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.9 | 5e-10 | 37/50 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.3 | 3e-08 | 31/48 (C32, HT-29, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +5.8 | 6e-07 | 37/48 (A-427, Panc 03.27, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.1 | 2e-05 | 31/48 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.8 | 1e-04 | 24/44 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 2e-04 | 26/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 28/48 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.007 | 22/48 (HT-29, COLO 205, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.007 | 24/48 (A-172, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.18× | +3.6 | 0.012 | 24/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.031 | 19/48 (A-427, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -7.5 | 5e-11 | 37/48 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -7.2 | 2e-10 | 36/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -6.6 | 6e-09 | 37/48 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -6.6 | 6e-09 | 34/47 (NCI-H1792, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.594×** | -5.9 | 5e-07 | 28/38 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.843× | -5.1 | 3e-05 | 21/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.790×** | -5.1 | 3e-05 | 28/48 (CFPAC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.801×** | -4.8 | 1e-04 | 25/47 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.809×** | -4.6 | 3e-04 | 26/48 (NCI-H23, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.813×** | -4.5 | 5e-04 | 26/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.684×** | -4.3 | 1e-03 | 30/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.825×** | -4.2 | 0.002 | 26/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.826×** | -4.1 | 0.002 | 26/48 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.828×** | -4.1 | 0.002 | 24/48 (COLO 205, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.002 | 28/49 (NCI-H23, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.825×** | -4.0 | 0.002 | 22/49 (SNU-423, J82, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.887× | -3.5 | 0.012 | 15/49 (MIA PaCa-2, SK-MEL-2, …) | top dose only | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.846× | -3.5 | 0.015 | 20/49 (SW 900, A498, …) | top dose only | plate-row cell shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -3.1 | 0.050 | 23/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.867× | -3.1 | 0.050 | 14/48 (NCI-H2030, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 209 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +20.5) | [[Belinostat (drug)]] 5 µM 0.502× (z -10.2) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.517× (z -9.8) |
| [[HOP62 (line)]] | alt | 198 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +32.2) | [[Digitoxin (drug)]] 0.05 µM 0.552× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 241 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.426× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 121 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.2) | — |
| [[PANC-1 (line)]] | alt | 209 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.533× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 166 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +22.9) | [[Belumosudil (drug)]] 5 µM 0.476× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 163 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +22.0) | [[Lonafarnib (drug)]] 5 µM 0.128× (z -12.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 211 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +20.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.415× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 142 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +20.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 217 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 184 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +19.6) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 143 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +11.1) | — |
| [[A498 (line)]] | wt | 163 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +15.4) | — |
| [[C32 (line)]] | wt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +17.5) | — |
| [[H4 (line)]] | wt | 236 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.485× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 173 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.4) | — |
| [[J82 (line)]] | alt | 407 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.1) | [[Bortezomib (drug)]] 5 µM 0.316× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[LoVo (line)]] | wt | 185 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +22.2) | — |
| [[NCI-H2030 (line)]] | alt | 164 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.8) | [[Digitoxin (drug)]] 5 µM 0.486× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 123 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.244× (z -16.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 206 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.4) | — |
| [[KATO III (line)]] | alt | 301 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.488× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 205 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.4) | — |
| [[LS 180 (line)]] | wt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 185 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.426× (z -9.4) ⚠ toxic |
| [[RKO (line)]] | wt | 193 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 198 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 312 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +15.2) | [[Digitoxin (drug)]] 5 µM 0.419× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 149 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.7) | [[Digitoxin (drug)]] 0.05 µM 0.493× (z -8.5) |
| [[A-172 (line)]] | wt | 174 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.410× (z -8.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 178 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 160 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 211 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +13.5) | — |
| [[SNU-1 (line)]] | wt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.6) | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.162× (z -8.9) |
| [[SW 1271 (line)]] | alt | 271 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 147 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.6) | — |
| [[SW48 (line)]] | wt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.9) | — |
| [[A-427 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 162 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 91.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIF1]] | +0.78 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[MED29]] | +0.71 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.70 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[C3orf20]] | +0.69 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[RBBP6]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[BOLA1]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[BCL2L13]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[SLC22A1]] | +0.67 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[FAM151B]] | +0.67 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.67 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.66 | +0.72 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCSH]] | -0.68 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.67 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.64 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[METAP1]] | -0.64 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.64 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[SKP2]] | -0.63 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.63 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[BRAT1]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[HDAC1]] | -0.63 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[RAB4A]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C6orf62's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity raises C6orf62's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.10× lower at baseline in the lines without RNF103-CHMP3 | 0.080 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Nimesulide (drug)]] 5 µM | C | C6orf62's natural level raises the cells' numbers under Nimesulide 5 µM (protects the cells) | C6orf62's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.333 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -26.8); signed map (15.7, -3.9). **Vector** length 153, 52.0% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.8 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +20.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +8.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.0 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +6.2 | +3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.6 | +1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.5 | -7.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -7.2 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.2 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.0 | -6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.4 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 6 open reading frame 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,704,861-24,720,825 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12619, DKFZP564G182, XTP12 |
| Matched by | ensembl_id |

UniProt [Q9GZU0](https://www.uniprot.org/uniprotkb/Q9GZU0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20998) · Entrez [81688](https://www.ncbi.nlm.nih.gov/gene/81688) · UniProt [Q9GZU0](https://www.uniprot.org/uniprotkb/Q9GZU0) · Ensembl [ENSG00000112308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112308)

## Data

Gene col 3355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3355); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3355]; `tensor/DDL_lfc|DDL_z.npy` [3355]; `embed/gene_vectors.npy` [3355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3355 or target_col == 3355). Every well: [[C6orf62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C6orf62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
