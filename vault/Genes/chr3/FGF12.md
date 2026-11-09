---
symbol: "FGF12"
type: "gene"
col: 3536
ensembl_id: "ENSG00000114279"
name: "fibroblast growth factor 12"
location: "3q28-q29"
module: 26
arm: "+"
pooled_cpm: 19.73
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 19
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FGF12

*fibroblast growth factor 12* — 3q28-q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +21.4, q 0e+00, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.517× (z -11.0, q 2e-25, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPK2-DT]] (+0.63, fdr 1e-05), [[LINC00240]] (+0.63, fdr 4e-05), [[CFAP418-AS1]] (+0.63, fdr 1e-05); moves opposite to [[FAM118A]] (-0.56, fdr 9e-05), [[CPSF4]] (-0.55, fdr 6e-05), [[CCDC134]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 3 go from it, the strongest it → [[MB21D2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +21.4 | 0e+00 | 30/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +18.5 | 0e+00 | 33/42 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.45×** | +14.8 | 0e+00 | 36/43 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +11.2 | 3e-27 | 28/41 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.4 | 2e-23 | 29/44 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +6.8 | 1e-09 | 23/42 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +6.5 | 6e-09 | 17/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.53×** | +5.5 | 3e-06 | 17/43 (A-172, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 8e-06 | 17/44 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 2e-05 | 8/44 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.7 | 1e-04 | 13/43 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 3e-04 | 14/42 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 4e-04 | 11/43 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +4.3 | 8e-04 | 13/41 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.2 | 9e-04 | 13/42 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3536.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.517×** | -11.0 | 2e-25 | 29/43 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.497×** | -10.2 | 5e-22 | 28/39 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.578×** | -9.2 | 1e-17 | 28/42 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -6.8 | 1e-09 | 20/43 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.704×** | -5.9 | 5e-07 | 15/43 (J82, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.713×** | -5.6 | 2e-06 | 23/41 (J82, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.748×** | -4.8 | 1e-04 | 16/44 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.760×** | -4.6 | 3e-04 | 14/43 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.006 | 8/43 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.767×** | -3.9 | 0.006 | 17/40 (H4, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.010 | 11/43 (HS-578T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.802×** | -3.7 | 0.011 | 18/43 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.780×** | -3.7 | 0.011 | 14/44 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.785×** | -3.6 | 0.013 | 14/43 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.785×** | -3.6 | 0.013 | 4/43 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.015 | 17/43 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.692×** | -3.2 | 0.041 | 6/43 (NCI-H661, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.706×** | -3.0 | 0.067 | 4/41 (COLO 205, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.879× | -3.0 | 0.067 | 5/44 (LOX-IMVI, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.1 | 6 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 37.4× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -13.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 17.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 26.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.19× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.242× (z -8.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 11.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +16.5) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 39.7 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 60.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.63× (z +8.7) | [[Lonafarnib (drug)]] 5 µM 0.0988× (z -10.5) ⚠ toxic |
| [[A549 (line)]] | wt | 32.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.280× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 15.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0939× (z -9.2) ⚠ toxic |
| [[H4 (line)]] | wt | 37.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 6.72 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +12.8) | — |
| [[J82 (line)]] | alt | 57.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.6) | [[Digitoxin (drug)]] 0.5 µM 0.334× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +15.9) | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.1) | — |
| [[A-427 (line)]] | wt | 9.90 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.75× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 7.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0623× (z -11.9) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 84.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0715× (z -9.3) |
| [[SHP-77 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 9.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 12.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.72× (z +14.9) | — |
| [[SW480 (line)]] | alt | 9.37 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.30× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | +0.63 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.63 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[CFAP418-AS1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CHODL]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.60 | +0.66 / +0.43 | both halves | 4e-05 |  |
| [[HULC]] | +0.60 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NEB]] | +0.60 | +0.64 / +0.40 | both halves | 5e-05 | pathway: Muscle contraction |
| [[RAP2C-AS1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[UNC79]] | +0.59 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[DYNLRB2-AS1]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[F8]] | +0.59 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[SYNPO2]] | +0.59 | +0.68 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.56 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[CPSF4]] | -0.55 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[CCDC134]] | -0.53 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[L2HGDH]] | -0.52 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[GLMN]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CKLF]] | -0.51 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[XYLT2]] | -0.51 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[ANKS6]] | -0.51 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[GRAMD4]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[TMEM242]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers FGF12's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[DSE]] | B | DSE activity raises FGF12's level | lines that do not express DSE (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without DSE | 0.090 | ⚠ within organs, on part of the lines; also absent: SGCE, WDR17, LRP12; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MB21D2]] | C | FGF12 activity raises MB21D2's level | lines that do not express FGF12 (4) vs lines expressing it (46) | 2.59× lower at baseline in the lines without FGF12 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM182B, ENSG00000261341, WDR35; maybe low, not absent |
| [[COQ5]] | C | FGF12 activity raises COQ5's level | lines that do not express FGF12 (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without FGF12 | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM182B, ENSG00000261341, WDR35; maybe low, not absent |
| [[SSPN]] | C | FGF12 activity raises SSPN's level | lines that do not express FGF12 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without FGF12 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM182B, ENSG00000261341, WDR35; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.4, 16.7); signed map (28.4, -8.9). **Vector** length 91.8, 19.0% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +18.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.0 | +21.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.9 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +4.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -9.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.2 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.0 | -10.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -3.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q28-q29 — chr3:192,139,390-192,767,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FHF1; previously FGF12B |
| Gene groups (HGNC) | Fibroblast growth factor family |
| Reactome | 3 pathways, smallest: Phase 0 - rapid depolarisation; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P61328](https://www.uniprot.org/uniprotkb/P61328) (Fibroblast growth factor 12):

> Involved in nervous system development and function. Involved in the positive regulation of voltage-gated sodium channel activity. Promotes neuronal excitability by elevating the voltage dependence of neuronal sodium channel SCN8A fast inactivation.

**Summary**, from NCBI Gene [2257](https://www.ncbi.nlm.nih.gov/gene/2257):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth, and invasion. This growth factor lacks the N-terminal signal sequence present in most of the FGF family members, but it contains clusters of basic residues that have been demonstrated to act …

**Accessions** — [HGNC:3668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3668) · Entrez [2257](https://www.ncbi.nlm.nih.gov/gene/2257) · UniProt [P61328](https://www.uniprot.org/uniprotkb/P61328) · Ensembl [ENSG00000114279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114279)

## Data

Gene col 3536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3536); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3536]; `tensor/DDL_lfc|DDL_z.npy` [3536]; `embed/gene_vectors.npy` [3536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3536 or target_col == 3536). Every well: [[FGF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
