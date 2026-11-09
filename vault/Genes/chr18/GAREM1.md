---
symbol: "GAREM1"
type: "gene"
col: 6519
ensembl_id: "ENSG00000141441"
name: "GRB2 associated regulator of MAPK1 subtype 1"
location: "18q12.1"
module: 106
arm: "+"
pooled_cpm: 96.1
n_lines_expressing: 40
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 56
direction_downstream: 19
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# GAREM1

*GRB2 associated regulator of MAPK1 subtype 1* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +9.3, q 7e-18, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.650× (z -8.4, q 2e-14, down in 27 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8]] (+0.71, fdr 7e-06), [[TC2N]] (+0.63, fdr 1e-05), [[FGD4]] (+0.62, fdr 1e-05); moves opposite to [[ST3GAL3]] (-0.47, fdr 6e-05), [[NHSL1-AS1]] (-0.46, fdr 3e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[TMEM45B]] → it (grade B ⚠); 19 go from it, the strongest it → [[SCNN1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.3 | 7e-18 | 24/38 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +8.9 | 2e-16 | 23/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +8.8 | 2e-16 | 22/38 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.38×** | +8.8 | 2e-16 | 23/38 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 4e-11 | 22/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +6.5 | 7e-09 | 22/37 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.3 | 2e-08 | 18/38 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 1e-05 | 19/39 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.28×** | +4.8 | 1e-04 | 19/38 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +4.7 | 1e-04 | 15/38 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +4.6 | 2e-04 | 17/39 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 13/38 (AsPC-1, A549, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 14/39 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.005 | 13/38 (A549, AsPC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.008 | 17/37 (NCI-H460, SW480, …) | rises with dose | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.022 | 14/37 (A549, AsPC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.024 | 11/40 (AsPC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.3 | 0.024 | 11/38 (A549, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -8.4 | 2e-14 | 27/38 (SHP-77, SW1417, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.524×** | -6.6 | 1e-08 | 25/38 (SW1417, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -5.6 | 4e-06 | 23/35 (KATO III, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -5.0 | 6e-05 | 23/39 (HT-29, SHP-77, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.613×** | -5.0 | 6e-05 | 24/38 (SW1417, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.776×** | -5.0 | 6e-05 | 24/38 (KATO III, Panc 03.27, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.631×** | -4.7 | 2e-04 | 20/38 (SW1417, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.643×** | -4.5 | 4e-04 | 19/38 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.803×** | -4.1 | 0.002 | 19/33 (Panc 03.27, KATO III, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.817×** | -4.0 | 0.004 | 20/38 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.823×** | -3.8 | 0.007 | 21/38 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.008 | 17/38 (SW1417, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.029 | 12/38 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.848× | -3.3 | 0.043 | 12/38 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.728×** | -3.3 | 0.043 | 14/30 (HT-29, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.898× | -3.0 | 0.086 | 7/39 (NCI-H1573, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 321 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.313× (z -11.5) |
| [[SW1417 (line)]] | alt | 214 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -12.7) |
| [[HT-29 (line)]] | alt | 315 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.185× (z -12.6) |
| [[COLO 205 (line)]] | alt | 276 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -8.8) |
| [[KATO III (line)]] | alt | 192 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 33.9 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +13.0) | — |
| [[SW48 (line)]] | wt | 158 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.187× (z -11.8) |
| [[BT-474 (line)]] | alt | 138 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.01× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 363 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 50.9 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.410× (z -9.1) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 293 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 116 | 2 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.63× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 2.70× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.329× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 64.1 | 3 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.33× (z +10.1) | — |
| [[A549 (line)]] | wt | 50.7 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.49× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 196 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.393× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 64.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 54.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 58.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.303× (z -9.1) |
| [[SW480 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.76× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 177 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[FGD4]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[SGPP2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[PELI1]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PDK4]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[PELI2]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DNAJC15]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[FOXO1]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[KIF13B]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GCNT3]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[LINC00511]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.47 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[NHSL1-AS1]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 55, C 1. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM45B]] | B | TMEM45B activity raises GAREM1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.03× lower at baseline in the lines without TMEM45B | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TOX3]] | B | TOX3 activity raises GAREM1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.54× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[JUP]] | B | JUP activity raises GAREM1's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.09× lower at baseline in the lines without JUP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises GAREM1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.37× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ST14]] | B | ST14 activity raises GAREM1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.22× lower at baseline in the lines without ST14 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises GAREM1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.51× lower at baseline in the lines without ARHGEF38 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[ITGB6]] | B | ITGB6 activity raises GAREM1's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.29× lower at baseline in the lines without ITGB6 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[CDH1]] | B | CDH1 activity raises GAREM1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.40× lower at baseline in the lines without CDH1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[C1orf116]] | B | C1orf116 activity raises GAREM1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without C1orf116 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CD24]] | B | CD24 activity raises GAREM1's level | lines that do not express CD24 (24) vs lines expressing it (26) | 2.95× lower at baseline in the lines without CD24 | 0.007 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises GAREM1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.38× lower at baseline in the lines without TMPRSS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[CAPN8]] | B | CAPN8 activity raises GAREM1's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.32× lower at baseline in the lines without CAPN8 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCNN1A]] | B | GAREM1 activity raises SCNN1A's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 4.42× lower at baseline in the lines without GAREM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[FGD4]] | B | GAREM1 activity raises FGD4's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without GAREM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[PLEKHA7]] | B | GAREM1 activity raises PLEKHA7's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without GAREM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[FOXO1]] | B | GAREM1 activity raises FOXO1's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.61× lower at baseline in the lines without GAREM1 | 0.035 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[PPL]] | B | GAREM1 activity raises PPL's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without GAREM1 | 0.039 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[LIPH]] | B | GAREM1 activity raises LIPH's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 3.99× lower at baseline in the lines without GAREM1 | 0.044 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[PERP]] | B | GAREM1 activity raises PERP's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without GAREM1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[PLEKHG6]] | B | GAREM1 activity raises PLEKHG6's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without GAREM1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[CDH1]] | B | GAREM1 activity raises CDH1's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 4.51× lower at baseline in the lines without GAREM1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[BRSK1]] | B | GAREM1 activity lowers BRSK1's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 1.88× higher at baseline in the lines without GAREM1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[TC2N]] | B | GAREM1 activity raises TC2N's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 4.54× lower at baseline in the lines without GAREM1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[C1orf116]] | B | GAREM1 activity raises C1orf116's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 3.27× lower at baseline in the lines without GAREM1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.7, 43.9); signed map (52.1, 11.6). **Vector** length 122, 34.6% of its response variance represented; |z| ≥ 3 in 1,364 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +8.1 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.7 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +8.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.2 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.6 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | GRB2 associated regulator of MAPK1 subtype 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:32,124,877-32,470,882 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21610; previously C18orf11, FAM59A, GAREM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H706](https://www.uniprot.org/uniprotkb/Q9H706) (GRB2-associated and regulator of MAPK protein 1):

> [Isoform 1]: Acts as an adapter protein that plays a role in intracellular signaling cascades triggered either by the cell surface activated epidermal growth factor receptor and/or cytoplasmic protein tyrosine kinases. Promotes activation of the MAPK/ERK signaling pathway. Plays a role in the regulation of cell proliferation.

**Summary**, from NCBI Gene [64762](https://www.ncbi.nlm.nih.gov/gene/64762):

> This gene encodes an adaptor protein which functions in the epidermal growth factor (EGF) receptor-mediated signaling pathway. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:26136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26136) · Entrez [64762](https://www.ncbi.nlm.nih.gov/gene/64762) · UniProt [Q9H706](https://www.uniprot.org/uniprotkb/Q9H706) · Ensembl [ENSG00000141441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141441)

## Data

Gene col 6519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6519); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6519]; `tensor/DDL_lfc|DDL_z.npy` [6519]; `embed/gene_vectors.npy` [6519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6519 or target_col == 6519). Every well: [[GAREM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAREM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
