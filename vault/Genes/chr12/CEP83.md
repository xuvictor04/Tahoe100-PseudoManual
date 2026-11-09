---
symbol: "CEP83"
type: "gene"
col: 10406
ensembl_id: "ENSG00000173588"
name: "centrosomal protein 83"
location: "12q22"
module: 1
arm: "+"
pooled_cpm: 85.26
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CEP83

*centrosomal protein 83* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +13.1, q 3e-36, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.612× (z -15.0, q 0e+00, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMSS1]] (+0.80, fdr 7e-06), [[NOC3L]] (+0.74, fdr 7e-06), [[SERBP1]] (+0.72, fdr 7e-06); moves opposite to [[TSC22D4]] (-0.70, fdr 7e-06), [[TMEM59]] (-0.66, fdr 7e-06), [[MXD1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EIF4G3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +13.1 | 3e-36 | 39/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +12.3 | 3e-32 | 42/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +7.8 | 1e-12 | 33/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.5 | 7e-12 | 28/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +7.2 | 6e-11 | 29/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +7.0 | 3e-10 | 27/48 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +5.6 | 2e-06 | 33/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +4.8 | 1e-04 | 25/48 (J82, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +4.4 | 6e-04 | 21/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.22×** | +4.3 | 1e-03 | 23/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.002 | 17/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.21×** | +4.1 | 0.002 | 21/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.20×** | +4.0 | 0.003 | 21/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.21×** | +3.9 | 0.004 | 21/47 (RPMI-7951, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.006 | 19/48 (A498, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.012 | 14/49 (A-172, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.052 | 16/48 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.052 | 9/48 (SW 900, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.1 | 0.052 | 16/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.10× | +3.0 | 0.068 | 4/48 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.082 | 9/48 (hTERT-HPNE, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.082 | 10/48 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.082 | 3/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -15.0 | 0e+00 | 37/49 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -8.6 | 3e-15 | 33/48 (LoVo, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -5.3 | 2e-05 | 27/50 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.796×** | -4.9 | 1e-04 | 23/47 (PANC-1, NCI-H23, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.735×** | -4.8 | 2e-04 | 27/48 (LoVo, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -4.2 | 0.002 | 24/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.827×** | -4.1 | 0.003 | 26/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.886× | -3.7 | 0.015 | 16/48 (A498, LS 180, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.043 | 16/48 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.877× | -3.2 | 0.085 | 9/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.817×** | -3.1 | 0.093 | 15/48 (SNU-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.869× | -3.1 | 0.11 | 15/48 (AN3 CA, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 113 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +30.4) | — |
| [[NCI-H460 (line)]] | wt | 102 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 72.1 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 157 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -27.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -15.7) |
| [[RKO (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~69% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.333× (z -11.6) |
| [[SW 900 (line)]] | alt | 69.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +19.3) | — |
| [[A-172 (line)]] | wt | 30.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +17.2) | — |
| [[A-427 (line)]] | wt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -11.9) |
| [[C-33 A (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.5) |
| [[C32 (line)]] | wt | 87.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 41.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +23.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 133 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 26.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +20.9) | — |
| [[A498 (line)]] | wt | 79.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.3) |
| [[A549 (line)]] | wt | 91.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.4) |
| [[HOP62 (line)]] | alt | 64.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.5) |
| [[Hs 766T (line)]] | wt | 49.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.7) | — |
| [[J82 (line)]] | alt | 76.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.3) | — |
| [[LoVo (line)]] | wt | 165 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.366× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 94.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 37.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -16.5) |
| [[SNU-423 (line)]] | alt | 65.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.7) |
| [[SW1417 (line)]] | alt | 57.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.1) |
| [[CHP-212 (line)]] | wt | 66.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.132× (z -10.0) |
| [[COLO 205 (line)]] | alt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +12.0) | — |
| [[H4 (line)]] | wt | 74.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 90.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.6) |
| [[HS-578T (line)]] | alt | 48.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -13.3) |
| [[HT-29 (line)]] | alt | 61.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 70.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 59.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.5) |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.114× (z -9.2) |
| [[SW48 (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.2) |
| [[AN3 CA (line)]] | alt | 118 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 67.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMSS1]] | +0.80 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[NOC3L]] | +0.74 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[SERBP1]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[DDX10]] | +0.72 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[NAA15]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.67 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.67 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[PNO1]] | +0.65 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[JPH1]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | -0.70 | -0.64 / -0.70 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.66 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[MXD1]] | -0.64 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[MKRN1]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[MTCH1]] | -0.62 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[RAB5B]] | -0.62 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[TMUB2]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ZNF394]] | -0.60 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[MYL6B]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[HINFP]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[BSDC1]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity weakens CEP83's drug response | lines that do not express TERT (13) vs lines expressing it (37) | the lines without TERT respond 1.29× as strongly (z diff -0.54); strongest at Homoharringtonine 0.5 µM: 2.38x vs 1.40x (z diff -3.4) | 0.009 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS; both ways; artifact flags |
| [[TERT]] | B | TERT activity raises CEP83's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without TERT | 0.017 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[MICE]] | B | MICE activity lowers CEP83's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.45× higher at baseline in the lines without MICE | 0.021 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises CEP83's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without FAM78B | 0.035 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[TOP2A]] | B | TOP2A activity raises CEP83's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[VAMP5]] | B | VAMP5 activity lowers CEP83's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.44× higher at baseline in the lines without VAMP5 | 0.068 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[JPH1]] | B | JPH1 activity strengthens CEP83's drug response | lines that do not express JPH1 (15) vs lines expressing it (35) | the lines without JPH1 respond 0.83× as strongly (z diff +0.65); strongest at Harringtonine 5 µM: 1.16x vs 1.73x (z diff +3.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: UGT8, CADPS2, PTPRE; artifact flags |
| [[CCL20]] | B | CCL20 activity lowers CEP83's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.34× higher at baseline in the lines without CCL20 | 0.0995 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[USP31]] | C | USP31 activity raises CEP83's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.44× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[SLC35F2]] | C | SLC35F2 activity raises CEP83's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without SLC35F2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF4G3]] | C | CEP83's natural level strengthens EIF4G3's drug response | CEP83's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.01; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.0, -42.7); signed map (-6.2, -48.5). **Vector** length 124, 35.9% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.2 | +12.3 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +7.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -15.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.7 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -5.1 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 83 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:94,306,449-94,459,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-58, NPHP18; previously CCDC41 |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y592](https://www.uniprot.org/uniprotkb/Q9Y592) (Centrosomal protein of 83 kDa):

> Component of the distal appendage region of the centriole involved in the initiation of primary cilium assembly. May collaborate with IFT20 in the trafficking of ciliary membrane proteins from the Golgi complex to the cilium during the initiation of primary cilium assembly.

**Summary**, from NCBI Gene [51134](https://www.ncbi.nlm.nih.gov/gene/51134):

> The protein encoded by this gene is a centriolar protein involved in primary cilium assembly. Defects in this gene have been associated with infantile nephronophthisis and intellectual disability. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:17966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17966) · Entrez [51134](https://www.ncbi.nlm.nih.gov/gene/51134) · UniProt [Q9Y592](https://www.uniprot.org/uniprotkb/Q9Y592) · Ensembl [ENSG00000173588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173588)

## Data

Gene col 10406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10406); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10406]; `tensor/DDL_lfc|DDL_z.npy` [10406]; `embed/gene_vectors.npy` [10406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10406 or target_col == 10406). Every well: [[CEP83 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP83.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
