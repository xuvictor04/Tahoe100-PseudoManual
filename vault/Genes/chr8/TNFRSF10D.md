---
symbol: "TNFRSF10D"
type: "gene"
col: 10397
ensembl_id: "ENSG00000173530"
name: "TNF receptor superfamily member 10d"
location: "8p21.3"
module: 105
arm: "+"
pooled_cpm: 89.54
n_lines_expressing: 39
n_dd_up: 22
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# TNFRSF10D

*TNF receptor superfamily member 10d* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +13.1, q 2e-36, up in 34 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.374× (z -9.8, q 6e-20, down in 33 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.595× (z -5.2, q 3e-05, down in 30 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSCN1]] (+0.68, fdr 7e-06), [[POM121C]] (+0.66, fdr 1e-05), [[GTF2B]] (+0.63, fdr 7e-06); moves opposite to [[TRIM37]] (-0.53, fdr 3e-05), [[AIFM1]] (-0.51, fdr 2e-05), [[ANAPC7]] (-0.51, fdr 5e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Tucidinostat (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +13.1 | 2e-36 | 34/38 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +8.3 | 4e-14 | 36/37 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.29×** | +7.9 | 4e-13 | 36/38 (A498, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.95×** | +7.0 | 5e-10 | 32/37 (HS-578T, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.81×** | +6.2 | 8e-08 | 28/37 (LoVo, AsPC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.79×** | +6.1 | 1e-07 | 29/37 (HS-578T, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.03×** | +6.0 | 1e-07 | 36/37 (LS 180, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +6.0 | 1e-07 | 28/37 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.77×** | +5.9 | 2e-07 | 29/37 (HS-578T, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 5e-05 | 30/38 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.6 | 2e-04 | 27/37 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.51×** | +4.1 | 0.002 | 25/39 (NCI-H460, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 22/37 (SNU-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.48×** | +4.1 | 0.002 | 21/37 (KATO III, SW480, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.12×** | +4.1 | 0.002 | 31/37 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 21/37 (SNU-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.046 | 22/37 (SW480, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.374×** | -9.8 | 6e-20 | 33/37 (SNU-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -8.1 | 2e-13 | 27/34 (NCI-H23, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.497×** | -7.3 | 7e-11 | 25/37 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.595×** | -5.2 | 3e-05 | 30/37 (HOP62, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.605×** | -4.8 | 2e-04 | 27/37 (NCI-H1792, SW 900, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.722×** | -4.7 | 2e-04 | 25/37 (HOP62, SW 900, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.641×** | -4.6 | 3e-04 | 25/37 (HOP62, KATO III, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.632×** | -4.6 | 3e-04 | 29/37 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.652×** | -4.4 | 6e-04 | 26/38 (HOP62, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -4.2 | 0.001 | 6/39 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.671×** | -4.1 | 0.002 | 23/39 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.679×** | -4.0 | 0.003 | 25/37 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.679×** | -4.0 | 0.003 | 28/37 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.731×** | -3.8 | 0.005 | 24/37 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.689×** | -3.7 | 0.008 | 24/37 (HOP62, SW 900, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.780×** | -3.5 | 0.015 | 21/38 (HOP62, SW480, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.713×** | -3.5 | 0.015 | 19/37 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.724×** | -3.3 | 0.026 | 22/37 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.737×** | -3.2 | 0.044 | 20/38 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.737×** | -3.2 | 0.044 | 21/38 (SW48, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 43.3 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +13.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 171 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 152 | 0 | 4 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.609× (z -15.4) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.332× (z -9.3) |
| [[LoVo (line)]] | wt | 81.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 96.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.3) | [[Adagrasib (drug)]] 0.05 µM 0.665× (z -11.5) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 28.2 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.8) | — |
| [[A549 (line)]] | wt | 182 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +12.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -10.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 146 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 109 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -12.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 275 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 101 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +12.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -12.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 83.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +12.3) | — |
| [[A498 (line)]] | wt | 88.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 210 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -9.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 56.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -11.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 98.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 82.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -17.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 108 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.341× (z -9.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -10.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 68.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +16.5) | — |
| [[SW48 (line)]] | wt | 61.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +13.5) | — |
| [[A-172 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.89 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSCN1]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[POM121C]] | +0.66 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GLRX]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PPIL3]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MED26]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MAP2K1]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ELL]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[KCNMB4]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[WRAP53]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM37]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[AIFM1]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[BAZ1B]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MTOR]] | -0.50 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[GFM1]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CPLANE1]] | -0.49 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[PSMD11]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TNFRSF10D's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL13A1]] | B | COL13A1 activity raises TNFRSF10D's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without COL13A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[MAP2K1]] | B | MAP2K1 activity raises TNFRSF10D's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[SLC2A3]] | B | SLC2A3 activity lowers TNFRSF10D's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.02× higher at baseline in the lines without SLC2A3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[ITGA5]] | B | ITGA5 activity raises TNFRSF10D's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without ITGA5 | 0.098 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[TNFRSF10A]] | C | TNFRSF10A activity raises TNFRSF10D's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 4.38× lower at baseline in the lines without TNFRSF10A | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1; co-absent with the target |
| [[FSCN1]] | C | FSCN1 activity raises TNFRSF10D's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tucidinostat (drug)]] 5 µM | C | TNFRSF10D activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.89× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |
| cells under [[Ixazomib citrate (drug)]] 0.5 µM | C | TNFRSF10D activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.78× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | TNFRSF10D activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.60× the cells of the other lines | 0.084 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |
| cells under [[NG25 (drug)]] 5 µM | C | TNFRSF10D activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.71× the cells of the other lines | 0.088 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, -20.6); signed map (-41.1, 21.5). **Vector** length 126, 40.0% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.6 | -9.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.9 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 10d |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,135,588-23,164,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DcR2, TRUNDD, TRAILR4, CD264 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Reactome | 7 pathways, smallest: TRAIL  signaling; TP53 Regulates Transcription of Death Receptors and Ligands; TP53 Regulates Transcription of Cell Death Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBN6](https://www.uniprot.org/uniprotkb/Q9UBN6) (Tumor necrosis factor receptor superfamily member 10D):

> Receptor for the cytotoxic ligand TRAIL. Contains a truncated death domain and hence is not capable of inducing apoptosis but protects against TRAIL-mediated apoptosis. Reports are contradictory with regards to its ability to induce the NF-kappa-B pathway. According to PubMed:9382840, it cannot but according to PubMed:9430226, it can induce the NF-kappa-B pathway.

**Summary**, from NCBI Gene [8793](https://www.ncbi.nlm.nih.gov/gene/8793):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor contains an extracellular TRAIL-binding domain, a transmembrane domain, and a truncated cytoplamic death domain. This receptor does not induce apoptosis, and has been shown to play an inhibitory role in TRAIL-induced cell apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11907) · Entrez [8793](https://www.ncbi.nlm.nih.gov/gene/8793) · UniProt [Q9UBN6](https://www.uniprot.org/uniprotkb/Q9UBN6) · Ensembl [ENSG00000173530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173530)

## Data

Gene col 10397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10397); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10397]; `tensor/DDL_lfc|DDL_z.npy` [10397]; `embed/gene_vectors.npy` [10397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10397 or target_col == 10397). Every well: [[TNFRSF10D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF10D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
