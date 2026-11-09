---
symbol: "PHF20L1"
type: "gene"
col: 4962
ensembl_id: "ENSG00000129292"
name: "PHD finger protein 20 like 1"
location: "8q24.22"
module: 209
arm: "+"
pooled_cpm: 119.85
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# PHF20L1

*PHD finger protein 20 like 1* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +36.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.606× (z -8.2, q 2e-13, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 2 lines (LOX-IMVI 0.322×, SNU-1 0.134×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.293×; ⚠ toxic); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.352×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.546×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RO60]] (+0.64, fdr 1e-05), [[XIAP]] (+0.55, fdr 5e-05), [[PPP3CB]] (+0.55, fdr 3e-05); moves opposite to [[PTK7]] (-0.52, fdr 2e-05), [[VASH2]] (-0.50, fdr 4e-04), [[ZFP64]] (-0.50, fdr 2e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +36.8 | 0e+00 | 45/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +29.8 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +22.1 | 0e+00 | 46/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +20.9 | 0e+00 | 47/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +17.3 | 0e+00 | 43/48 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +15.1 | 0e+00 | 38/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +13.7 | 6e-41 | 35/49 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +13.4 | 3e-39 | 39/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +12.6 | 2e-34 | 41/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +10.6 | 1e-24 | 36/48 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +9.2 | 2e-18 | 35/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.32×** | +8.3 | 6e-15 | 29/47 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +8.0 | 8e-14 | 35/50 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +7.7 | 7e-13 | 28/48 (RKO, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.27×** | +7.0 | 1e-10 | 26/49 (A-172, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +6.4 | 6e-09 | 28/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +5.5 | 1e-06 | 20/48 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +5.2 | 7e-06 | 18/49 (NCI-H2347, RKO, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.09× | +3.7 | 0.005 | 3/48 (HOP62, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4962.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 2 lines (LOX-IMVI 0.322×, SNU-1 0.134×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.293×; ⚠ toxic); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.352×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.546×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.606×** | -8.2 | 2e-13 | 35/48 (LOX-IMVI, SNU-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.830×** | -5.8 | 2e-06 | 21/49 (H4, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.828×** | -5.6 | 3e-06 | 23/47 (C-33 A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.738×** | -4.9 | 1e-04 | 24/49 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.914× | -3.9 | 0.008 | 14/48 (AsPC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.915× | -3.9 | 0.008 | 4/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.008 | 16/48 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.903× | -3.2 | 0.099 | 8/48 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.823×** | -3.2 | 0.099 | 16/45 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.904× | -3.1 | 0.099 | 8/48 (HCT15, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 82.5 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +22.1) | — |
| [[COLO 205 (line)]] | alt | 93.7 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +29.0) | — |
| [[LS 180 (line)]] | wt | 109 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.4) | — |
| [[SW480 (line)]] | alt | 99.8 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +24.3) | — |
| [[LOX-IMVI (line)]] | wt | 156 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +22.8) | [[PH-797804 (drug)]] 5 µM 0.322× (z -9.9) |
| [[HOP62 (line)]] | alt | 114 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +23.0) | — |
| [[Hs 766T (line)]] | wt | 132 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +23.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 74.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +25.8) | — |
| [[NCI-H1573 (line)]] | alt | 191 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +28.5) | — |
| [[NCI-H23 (line)]] | alt | 177 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +26.5) | — |
| [[RKO (line)]] | wt | 177 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +18.4) | — |
| [[A498 (line)]] | wt | 172 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +15.7) | — |
| [[HT-29 (line)]] | alt | 319 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +21.3) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +19.5) | — |
| [[A-172 (line)]] | wt | 86.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 92.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 175 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +15.2) | — |
| [[hTERT-HPNE (line)]] | wt | 97.7 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 146 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 65.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.6) | — |
| [[C32 (line)]] | wt | 101 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.4) | — |
| [[J82 (line)]] | alt | 111 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.2) | — |
| [[NCI-H1792 (line)]] | alt | 94.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 131 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.8) | — |
| [[A-427 (line)]] | wt | 91.8 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 88.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.293× (z -11.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 71.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.9) | — |
| [[HCT15 (line)]] | alt | 84.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.3) | — |
| [[LoVo (line)]] | wt | 92.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +17.8) | — |
| [[NCI-H2030 (line)]] | alt | 89.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 108 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +15.6) | [[TAK-901 (drug)]] 5 µM 0.352× (z -10.4) |
| [[SNU-1 (line)]] | wt | 90.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.4) | [[PH-797804 (drug)]] 5 µM 0.134× (z -9.5) |
| [[SW 1088 (line)]] | alt | 90.9 | 0 | 3 | — | [[Saquinavir (drug)]] 0.05 µM 0.0911× (z -8.9) |
| [[SW1417 (line)]] | alt | 164 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 165 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +14.6) | — |
| [[H4 (line)]] | wt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 63.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.9) | — |
| [[KATO III (line)]] | alt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.4) | — |
| [[Panc 03.27 (line)]] | alt | 107 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.02× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 123 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 92.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +18.8) | — |
| [[SW48 (line)]] | wt | 66.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 188 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.3) |
| [[A549 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[XIAP]] | +0.55 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[PPP3CB]] | +0.55 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[CC2D1B]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[DMTF1]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RPAP2]] | +0.50 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ERCC6L2]] | +0.50 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[ZNF337-AS1]] | +0.50 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[BCAP29]] | +0.50 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[SMC6]] | +0.50 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[C6orf89]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[N4BP2]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTK7]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[VASH2]] | -0.50 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[ZFP64]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ADAM22]] | -0.48 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[RAB20]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[EEF2K]] | -0.48 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[RAB39A]] | -0.47 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[CACYBP]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[FGFR4]] | -0.47 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[KCNAB2]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[FOXK1]] | -0.47 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[SKP2]] | -0.46 | -0.61 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHF20L1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.0797). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.6, -0.2); signed map (4.9, -12.4). **Vector** length 107, 31.2% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +29.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +9.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.8 | +7.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +3.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -9.4 | -8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.8 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -3.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.3 | -3.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | -5.1 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 20 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:132,775,358-132,848,807 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-72, FLJ13649, MGC64923, FLJ21615, TDRD20B |
| Gene groups (HGNC) | PHD finger proteins; Tudor domain containing |
| Reactome | 3 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MW92](https://www.uniprot.org/uniprotkb/A8MW92) (PHD finger protein 20-like protein 1):

> Is a negative regulator of proteasomal degradation of a set of methylated proteins, including DNMT1 and SOX2. Involved in the maintainance of embryonic stem cells pluripotency, through the regulation of SOX2 levels (By similarity).

**Summary**, from NCBI Gene [51105](https://www.ncbi.nlm.nih.gov/gene/51105):

> Enables methylation-dependent protein binding activity. Involved in negative regulation of proteasomal ubiquitin-dependent protein catabolic process. Predicted to be located in nucleoplasm. Predicted to be part of NSL complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24280) · Entrez [51105](https://www.ncbi.nlm.nih.gov/gene/51105) · UniProt [A8MW92](https://www.uniprot.org/uniprotkb/A8MW92) · Ensembl [ENSG00000129292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129292)

## Data

Gene col 4962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4962); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4962]; `tensor/DDL_lfc|DDL_z.npy` [4962]; `embed/gene_vectors.npy` [4962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4962 or target_col == 4962). Every well: [[PHF20L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF20L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
