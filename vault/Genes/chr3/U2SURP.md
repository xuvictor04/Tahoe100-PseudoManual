---
symbol: "U2SURP"
type: "gene"
col: 8763
ensembl_id: "ENSG00000163714"
name: "U2 snRNP associated SURP domain containing"
location: "3q23"
module: 1
arm: "+"
pooled_cpm: 186.23
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# U2SURP

*U2 snRNP associated SURP domain containing* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +23.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.802× (z -8.2, q 2e-13, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTIF2]] (+0.73, fdr 7e-06), [[HNRNPU]] (+0.70, fdr 7e-06), [[HNRNPM]] (+0.69, fdr 7e-06); moves opposite to [[GUK1]] (-0.71, fdr 7e-06), [[VKORC1]] (-0.68, fdr 7e-06), [[TMEM184B]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZCCHC24]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +23.9 | 0e+00 | 48/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +17.7 | 0e+00 | 48/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +16.9 | 0e+00 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +14.4 | 7e-45 | 46/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +14.2 | 1e-43 | 44/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +14.0 | 2e-42 | 47/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +12.4 | 3e-33 | 39/45 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +11.8 | 3e-30 | 47/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +10.7 | 5e-25 | 44/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +10.5 | 6e-24 | 44/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +10.2 | 1e-22 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +9.8 | 3e-21 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.35×** | +7.7 | 5e-13 | 31/49 (SW480, HT-29, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +7.7 | 6e-13 | 37/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +7.3 | 1e-11 | 31/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +7.1 | 3e-11 | 35/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +5.9 | 9e-08 | 31/48 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.5 | 1e-06 | 32/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.3 | 4e-04 | 9/49 (LOX-IMVI, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -8.2 | 2e-13 | 31/48 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.738×** | -8.0 | 4e-13 | 37/48 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.764×** | -7.1 | 3e-10 | 32/49 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.827×** | -5.0 | 8e-05 | 24/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.5 | 9e-04 | 21/48 (HOP62, SW480, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -4.4 | 1e-03 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -4.4 | 1e-03 | 19/48 (HOP62, SW480, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.8 | 0.009 | 13/48 (A-172, AsPC-1, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.863× | -3.7 | 0.012 | 12/49 (NCI-H1792, A549, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.875× | -3.5 | 0.024 | 11/47 (SK-MEL-2, Panc 03.27, …) | two highest doses | low cells (technical?) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.880× | -3.4 | 0.038 | 11/48 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.915× | -3.3 | 0.041 | 12/49 (RKO, A498, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.079 | 3/48 (Hs 766T, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 224 | 15 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +23.8) | [[Panobinostat (drug)]] 0.5 µM 0.650× (z -8.7) |
| [[SW480 (line)]] | alt | 224 | 13 (5 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +18.6) | [[Tucidinostat (drug)]] 0.5 µM 0.613× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 147 | 14 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 171 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +19.3) | — |
| [[KATO III (line)]] | alt | 198 | 9 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.566× (z -9.5) |
| [[LoVo (line)]] | wt | 149 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +15.2) | — |
| [[A-427 (line)]] | wt | 276 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +11.3) | — |
| [[A498 (line)]] | wt | 169 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.4) ⚠ cell-cycle shift, explains ~2% of this change |
| [[COLO 205 (line)]] | alt | 153 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +19.7) | — |
| [[HOP62 (line)]] | alt | 160 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.530× (z -11.2) |
| [[HT-29 (line)]] | alt | 144 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.0) | — |
| [[NCI-H23 (line)]] | alt | 264 | 7 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 206 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.0) | — |
| [[A-172 (line)]] | wt | 165 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +24.2) | — |
| [[A549 (line)]] | wt | 162 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +19.8) | — |
| [[AsPC-1 (line)]] | alt | 142 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.6) | — |
| [[J82 (line)]] | alt | 291 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 205 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.6) | — |
| [[Hs 766T (line)]] | wt | 120 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.47× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 186 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +12.3) | — |
| [[H4 (line)]] | wt | 203 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 258 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 174 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 222 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.58× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.98× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 136 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.4) | — |
| [[C32 (line)]] | wt | 119 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 178 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.556× (z -9.1) |
| [[HS-578T (line)]] | alt | 177 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.1) | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 179 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.4) | — |
| [[RKO (line)]] | wt | 268 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -9.9) ⚠ cell-cycle shift, explains ~2% of this change |
| [[RPMI-7951 (line)]] | alt | 176 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 178 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 205 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 208 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.8) | — |
| [[SW1417 (line)]] | alt | 247 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 140 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +16.1) | — |
| [[SW48 (line)]] | wt | 187 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 203 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTIF2]] | +0.73 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[HNRNPU]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 432 |
| [[HNRNPM]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 635 |
| [[ZNF326]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[EWSR1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | same gene group |
| [[RIF1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MATR3]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[UTP15]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[UTP20]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[FUBP1]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 | STRING 460 |
| [[TCERG1]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 741 |
| [[USP40]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUK1]] | -0.71 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[VKORC1]] | -0.68 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[TMEM184B]] | -0.68 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[MPG]] | -0.64 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[TRPT1]] | -0.64 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SSR4]] | -0.63 | -0.58 / -0.57 | both halves | 8e-06 |  |
| [[CIB1]] | -0.62 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.62 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[CIAO2B]] | -0.62 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[TMED9]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SLC35E1]] | -0.61 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[OST4]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCCHC24]] | B | ZCCHC24 activity weakens U2SURP's drug response | lines that do not express ZCCHC24 (5) vs lines expressing it (44) | the lines without ZCCHC24 respond 1.23× as strongly (z diff -1.35); strongest at Digitoxin 5 µM: 2.27x vs 1.63x (z diff -2.9) | 0.036 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises U2SURP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises U2SURP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.7, -25.3); signed map (13.3, -36.9). **Vector** length 95.0, 33.2% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +9.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +9.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +17.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.7 | +0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.9 | -1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | +10.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | +0.4 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | U2 snRNP associated SURP domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,964,497-143,060,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | fSAPa, SR140 |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal A complex; CTD interacting domain containing |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

UniProt [O15042](https://www.uniprot.org/uniprotkb/O15042) carries no function annotation.

**Summary**, from NCBI Gene [23350](https://www.ncbi.nlm.nih.gov/gene/23350):

> Enables RNA binding activity. Predicted to be involved in RNA processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30855) · Entrez [23350](https://www.ncbi.nlm.nih.gov/gene/23350) · UniProt [O15042](https://www.uniprot.org/uniprotkb/O15042) · Ensembl [ENSG00000163714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163714)

## Data

Gene col 8763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8763); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8763]; `tensor/DDL_lfc|DDL_z.npy` [8763]; `embed/gene_vectors.npy` [8763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8763 or target_col == 8763). Every well: [[U2SURP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/U2SURP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
