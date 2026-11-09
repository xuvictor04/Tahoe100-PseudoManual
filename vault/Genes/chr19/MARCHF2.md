---
symbol: "MARCHF2"
type: "gene"
col: 1809
ensembl_id: "ENSG00000099785"
name: "membrane associated ring-CH-type finger 2"
location: "19p13.2"
module: 136
arm: "+"
pooled_cpm: 9.87
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# MARCHF2

*membrane associated ring-CH-type finger 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.59× (z +10.8, q 2e-24, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.420× (z -9.9, q 2e-20, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TECPR1]] (+0.67, fdr 3e-05), [[CDKN2D]] (+0.66, fdr 1e-05), [[TMEM184B]] (+0.62, fdr 1e-04); moves opposite to [[NNT]] (-0.60, fdr 1e-05), [[FUCA2]] (-0.56, fdr 2e-05), [[TMX1]] (-0.55, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +10.8 | 2e-24 | 40/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +10.7 | 2e-24 | 37/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +9.6 | 2e-19 | 41/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +5.6 | 3e-06 | 24/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.010 | 15/44 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.8 | 0.013 | 12/32 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.022 | 7/38 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.034 | 12/42 (A498, H4, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.3 | 0.054 | 5/20 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.23×** | +3.2 | 0.066 | 16/43 (NCI-H2030, LoVo, …) | top dose only | composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.066 | 3/45 (A-427, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.076 | 7/48 (LOX-IMVI, NCI-H1573, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.12 | 8/47 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -9.9 | 2e-20 | 33/47 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -8.1 | 1e-13 | 28/46 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.510×** | -7.7 | 3e-12 | 33/47 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.635×** | -7.3 | 3e-11 | 28/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.525×** | -7.3 | 5e-11 | 28/47 (A498, C32, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -6.5 | 1e-08 | 24/40 (HS-578T, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -5.4 | 5e-06 | 23/46 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.650×** | -4.9 | 5e-05 | 20/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.459×** | -4.6 | 2e-04 | 22/37 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.003 | 12/45 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.008 | 20/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.724×** | -3.7 | 0.010 | 20/42 (HS-578T, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -3.6 | 0.014 | 17/46 (A-427, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -3.4 | 0.024 | 12/41 (Panc 03.27, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -3.2 | 0.055 | 14/45 (A498, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.595×** | -3.1 | 0.067 | 11/44 (SW 900, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.075 | 9/48 (BT-474, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.768×** | -3.0 | 0.075 | 17/47 (NCI-H460, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 18.1 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.162× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -8.7) |
| [[A549 (line)]] | wt | 13.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.162× (z -10.2) |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.217× (z -10.5) |
| [[A-427 (line)]] | wt | 15.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.253× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 5.18 | 0 | 2 (1 ⚠) | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0701× (z -9.5) |
| [[C32 (line)]] | wt | 20.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.0) ⚠ cell-cycle shift, explains ~17% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.136× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0613× (z -10.6) |
| [[A-172 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 12.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.162× (z -11.1) |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -8.8) |
| [[J82 (line)]] | alt | 12.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -9.9) |
| [[KATO III (line)]] | alt | 3.77 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0675× (z -8.6) |
| [[LoVo (line)]] | wt | 10.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +15.3) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[LOX-IMVI (line)]] | wt | 5.65 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +10.6) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +19.1) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[NCI-H23 (line)]] | alt | 9.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +9.6) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.65 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.162× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.2) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[SW480 (line)]] | alt | 3.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +13.4) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR1]] | +0.67 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[CDKN2D]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.62 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[NELFB]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.61 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[MIGA2]] | +0.61 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[FBXL18]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.59 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[MOB3A]] | +0.59 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[ASL]] | +0.58 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ETHE1]] | +0.57 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[ATG4B]] | +0.57 | +0.27 / +0.56 | both halves | 3e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[FUCA2]] | -0.56 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TMX1]] | -0.55 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[DECR1]] | -0.55 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[M6PR]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[HNRNPK]] | -0.54 | -0.29 / -0.58 | both halves | 3e-04 |  |
| [[ZNF300]] | -0.54 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[MBNL3]] | -0.54 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[CAPRIN1]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SNX5]] | -0.53 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.53 | -0.21 / -0.55 | both halves | 6e-04 |  |
| [[RCN1]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, 2.2); signed map (-28.0, 16.1). **Vector** length 84.0, 16.7% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -8.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,413,270-8,439,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC240, MARCH-II, RNF172; previously MARCH2 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0N8](https://www.uniprot.org/uniprotkb/Q9P0N8) (E3 ubiquitin-protein ligase MARCHF2):

> E3 ubiquitin-protein ligase that may mediate ubiquitination of TFRC and CD86, and promote their subsequent endocytosis and sorting to lysosomes via multivesicular bodies. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer the ubiquitin to targeted substrates. Together with GOPC/CAL mediates the ubiquitination and lysosomal degradation of CFTR. Ubiquitinates and therefore mediates the degradation of DLG1. Regulates …

**Summary**, from NCBI Gene [51257](https://www.ncbi.nlm.nih.gov/gene/51257):

> MARCH2 is a member of the MARCH family of membrane-bound E3 ubiquitin ligases (EC 6.3.2.19). MARCH enzymes add ubiquitin (see MIM 191339) to target lysines in substrate proteins, thereby signaling their vesicular transport between membrane compartments. MARCH2 reduces surface accumulation of several glycoproteins and appears to regulate early endosome-to-trans-Golgi network (TGN) trafficking (Bartee et al., 2004 [PubMed 14722266]; Nakamura et al., 2005 [PubMed 15689499]).[supplied by OMIM, Mar …

**Accessions** — [HGNC:28038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28038) · Entrez [51257](https://www.ncbi.nlm.nih.gov/gene/51257) · UniProt [Q9P0N8](https://www.uniprot.org/uniprotkb/Q9P0N8) · Ensembl [ENSG00000099785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099785)

## Data

Gene col 1809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1809); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1809]; `tensor/DDL_lfc|DDL_z.npy` [1809]; `embed/gene_vectors.npy` [1809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1809 or target_col == 1809). Every well: [[MARCHF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
