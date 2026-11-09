---
symbol: "NECTIN2"
type: "gene"
col: 5032
ensembl_id: "ENSG00000130202"
name: "nectin cell adhesion molecule 2"
location: "19q13.32"
module: 160
arm: "+"
pooled_cpm: 119.43
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# NECTIN2

*nectin cell adhesion molecule 2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.59× (z +4.6, q 0.002, up in 24 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.438× (z -15.7, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK2]] (+0.68, fdr 7e-06), [[SLC66A2]] (+0.64, fdr 2e-05), [[FBXO46]] (+0.62, fdr 3e-05); moves opposite to [[NT5DC1]] (-0.60, fdr 7e-06), [[TRUB1]] (-0.55, fdr 1e-05), [[DPH5]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF391]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +4.6 | 0.002 | 24/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.017 | 23/48 (NCI-H460, CHP-212, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.017 | 21/48 (NCI-H2030, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.8 | 0.017 | 22/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.6 | 0.043 | 0/50 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.438×** | -15.7 | 0e+00 | 42/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.699×** | -9.6 | 2e-19 | 34/48 (NCI-H1792, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.608×** | -9.5 | 6e-19 | 37/49 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -9.3 | 2e-18 | 34/44 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -9.2 | 3e-18 | 39/48 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.656×** | -8.0 | 1e-13 | 38/48 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -7.9 | 3e-13 | 36/47 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.684×** | -7.2 | 4e-11 | 33/48 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.766×** | -7.2 | 5e-11 | 28/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.683×** | -7.0 | 2e-10 | 37/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -6.7 | 1e-09 | 34/48 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -6.3 | 1e-08 | 30/50 (HT-29, C-33 A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.711×** | -6.0 | 1e-07 | 25/45 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -5.3 | 4e-06 | 28/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.778×** | -4.8 | 7e-05 | 26/48 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -4.7 | 9e-05 | 21/48 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.781×** | -4.7 | 9e-05 | 30/48 (KATO III, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.782×** | -4.7 | 9e-05 | 28/48 (SW 1271, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.841× | -4.6 | 1e-04 | 18/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 532 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 168 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 80.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 52.9 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +13.7) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.77× (z +11.9) | — |
| [[A-427 (line)]] | wt | 96.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -10.4) |
| [[KATO III (line)]] | alt | 161 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.8) |
| [[LS 180 (line)]] | wt | 121 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -13.3) |
| [[LoVo (line)]] | wt | 105 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 177 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -13.6) |
| [[C-33 A (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.5) |
| [[COLO 205 (line)]] | alt | 141 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.5) |
| [[HCT15 (line)]] | alt | 99.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 78.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -14.2) |
| [[PANC-1 (line)]] | alt | 72.2 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.0) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.04× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -9.7) |
| [[A-172 (line)]] | wt | 61.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.359× (z -10.6) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.562× (z -8.8) |
| [[A498 (line)]] | wt | 128 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.567× (z -10.8) |
| [[HOP62 (line)]] | alt | 421 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -12.5) |
| [[Hs 766T (line)]] | wt | 124 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.5) |
| [[SW 900 (line)]] | alt | 143 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -11.4) |
| [[SW480 (line)]] | alt | 96.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -9.7) |
| [[A549 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -11.5) |
| [[C32 (line)]] | wt | 55.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -18.4) |
| [[CHP-212 (line)]] | wt | 92.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.204× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -10.6) |
| [[J82 (line)]] | alt | 97.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.442× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 99.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +12.4) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[NCI-H2347 (line)]] | alt | 83.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -9.0) |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.135× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.541× (z -9.0) |
| [[SNU-1 (line)]] | wt | 82.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -9.4) |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0787× (z -8.5) |
| [[SW1417 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -8.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SLC66A2]] | +0.64 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[FBXO46]] | +0.62 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[PRKD2]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CYTH1]] | +0.60 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[LUZP1]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[DCUN1D3]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[FBXO11]] | +0.57 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A25]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[DNM2]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 | pathway: Adherens junctions interactions |
| [[ABCA7]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[PITPNA]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5DC1]] | -0.60 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TRUB1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DPH5]] | -0.54 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MTX3]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ZFR]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[DCAF17]] | -0.52 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NELFCD]] | -0.51 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[RAB11FIP2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MBLAC2]] | -0.50 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[DNAJC13]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ACAT1]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CDC16]] | -0.50 | -0.33 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF391]] | B | ZNF391 activity lowers NECTIN2's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.99× higher at baseline in the lines without ZNF391 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[TMEM92]] | B | TMEM92 activity raises NECTIN2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.37× lower at baseline in the lines without TMEM92 | 0.063 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CYP46A1]] | B | CYP46A1 activity lowers NECTIN2's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.81× higher at baseline in the lines without CYP46A1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.785). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.3, 0.3); signed map (-25.3, 29.3). **Vector** length 132, 42.4% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.7 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.2 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.2 | -4.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.8 | -15.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.7 | -8.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.5 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -7.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | nectin cell adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,846,175-44,889,223 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PVRR2, PRR2, CD112, Nectin-2; previously HVEB, PVRL2 |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 7 pathways, smallest: Nectin/Necl  trans heterodimerization; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adherens junctions interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92692](https://www.uniprot.org/uniprotkb/Q92692) (Nectin-2):

> Modulator of T-cell signaling. Can be either a costimulator of T-cell function, or a coinhibitor, depending on the receptor it binds to. Upon binding to CD226, stimulates T-cell proliferation and cytokine production, including that of IL2, IL5, IL10, IL13, and IFNG. Upon interaction with PVRIG, inhibits T-cell proliferation. These interactions are competitive. Probable cell adhesion protein.; (Microbial infection) Acts as a receptor for herpes simplex virus 1 (HHV-1) mutant Rid1, herpes simplex …

**Summary**, from NCBI Gene [5819](https://www.ncbi.nlm.nih.gov/gene/5819):

> This gene encodes a single-pass type I membrane glycoprotein with two Ig-like C2-type domains and an Ig-like V-type domain. This protein is one of the plasma membrane components of adherens junctions. It also serves as an entry for certain mutant strains of herpes simplex virus and pseudorabies virus, and it is involved in cell to cell spreading of these viruses. Variations in this gene have been associated with differences in the severity of multiple sclerosis. Alternate transcriptional splice …

**Accessions** — [HGNC:9707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9707) · Entrez [5819](https://www.ncbi.nlm.nih.gov/gene/5819) · UniProt [Q92692](https://www.uniprot.org/uniprotkb/Q92692) · Ensembl [ENSG00000130202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130202)

## Data

Gene col 5032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5032); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5032]; `tensor/DDL_lfc|DDL_z.npy` [5032]; `embed/gene_vectors.npy` [5032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5032 or target_col == 5032). Every well: [[NECTIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECTIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
