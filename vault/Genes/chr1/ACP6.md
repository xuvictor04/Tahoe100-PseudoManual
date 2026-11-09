---
symbol: "ACP6"
type: "gene"
col: 8587
ensembl_id: "ENSG00000162836"
name: "acid phosphatase 6, lysophosphatidic"
location: "1q21.2"
module: 201
arm: "+"
pooled_cpm: 16.73
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 34
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# ACP6

*acid phosphatase 6, lysophosphatidic* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +13.5, q 1e-38, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.247× (z -24.6, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLK1]] (+0.64, fdr 1e-05), [[HOXA3]] (+0.59, fdr 3e-05), [[HELZ]] (+0.58, fdr 3e-05); moves opposite to [[IPO9]] (-0.53, fdr 3e-05), [[STRIP2]] (-0.52, fdr 3e-05), [[PEPD]] (-0.48, fdr 8e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NADK2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +13.5 | 1e-38 | 35/43 (HEC-1-A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +8.2 | 6e-14 | 33/45 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.33×** | +7.1 | 3e-10 | 21/45 (LS 180, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.6 | 3e-06 | 21/43 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 3e-06 | 19/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +5.0 | 4e-05 | 15/44 (KATO III, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.31×** | +4.8 | 1e-04 | 16/44 (H4, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.4 | 1e-03 | 16/43 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.087 | 7/45 (HOP62, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.247×** | -24.6 | 0e+00 | 45/45 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.336×** | -19.2 | 0e+00 | 41/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.368×** | -17.6 | 0e+00 | 39/43 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.376×** | -17.2 | 0e+00 | 42/44 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.508×** | -11.9 | 1e-30 | 33/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.680×** | -9.6 | 1e-19 | 26/44 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -9.4 | 6e-19 | 32/45 (COLO 205, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -9.4 | 6e-19 | 25/39 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.608×** | -8.7 | 2e-16 | 29/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.615×** | -8.2 | 1e-14 | 24/43 (SK-MEL-2, A-172, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -7.7 | 7e-13 | 27/44 (SW480, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -6.8 | 6e-10 | 23/41 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.685×** | -6.6 | 1e-09 | 21/43 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.690×** | -6.5 | 3e-09 | 23/44 (COLO 205, SW480, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.770×** | -6.5 | 3e-09 | 17/45 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -5.8 | 2e-07 | 23/44 (SW480, AN3 CA, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -5.5 | 9e-07 | 21/43 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.589×** | -4.9 | 3e-05 | 18/42 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.805×** | -3.8 | 0.003 | 14/42 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.007 | 14/44 (BT-474, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -16.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.8) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -13.0) |
| [[SW480 (line)]] | alt | 25.5 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -18.1) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.131× (z -13.1) |
| [[SHP-77 (line)]] | alt | 23.7 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -13.8) |
| [[LoVo (line)]] | wt | 15.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.178× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.178× (z -11.6) |
| [[A498 (line)]] | wt | 8.74 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -11.7) |
| [[A549 (line)]] | wt | 11.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.178× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -10.0) |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -11.2) |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -9.0) |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.220× (z -9.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.1) |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -13.8) |
| [[LS 180 (line)]] | wt | 20.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.246× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0939× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 39.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.155× (z -8.5) |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -10.4) |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0531× (z -9.5) |
| [[COLO 205 (line)]] | alt | 23.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.7) |
| [[H4 (line)]] | wt | 9.98 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0530× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.107× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 6.31 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0631× (z -8.7) |
| [[J82 (line)]] | alt | 9.45 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0998× (z -11.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 13.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.111× (z -8.5) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK1]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[HOXA3]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[HELZ]] | +0.58 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[CDK7]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[TIAL1]] | +0.57 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[MBIP]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[RCHY1]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LNX2]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TGDS]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[MBLAC2]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ATP6V0D1-DT]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[STRIP2]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[PEPD]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ATXN7L3]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TAF1B]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[GALNS]] | -0.47 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[HEG1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PITPNB]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 | pathway: Glycerophospholipid biosynthesis |
| [[RAB10]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[RRP7A]] | -0.46 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[STK38L]] | -0.46 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[DYNLT1]] | -0.46 | -0.38 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ACP6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NADK2]] | C | ACP6 activity weakens NADK2's drug response | lines that do not express ACP6 (3) vs lines expressing it (45) | the lines without ACP6 respond 1.37× as strongly (z diff -1.61); strongest at Digitoxin 0.5 µM: 0.29x vs 0.56x (z diff -4.7) | 0.061 | ⚠ few lines (3 vs 47); across organs; also absent: DBNDD1, CDKL5, ERO1B; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.3, 26.6); signed map (-14.3, 1.9). **Vector** length 71.2, 13.7% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +13.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.2 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +8.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +5.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | -17.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -17.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.2 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -24.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | acid phosphatase 6, lysophosphatidic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:147,629,652-147,670,524 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPAP, ACPL1 |
| Gene groups (HGNC) | Acid phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPH0](https://www.uniprot.org/uniprotkb/Q9NPH0) (Lysophosphatidic acid phosphatase type 6):

> Hydrolyzes lysophosphatidic acid (LPA) containing a medium length fatty acid chain to the corresponding monoacylglycerol. Has highest activity with lysophosphatidic acid containing myristate (C14:0), monounsaturated oleate (C18:1) or palmitate (C16:0), and lower activity with C18:0 and C6:0 lysophosphatidic acid.

**Summary**, from NCBI Gene [51205](https://www.ncbi.nlm.nih.gov/gene/51205):

> This gene encodes a member of the histidine acid phosphatase protein family. The encoded protein hydrolyzes lysophosphatidic acid, which is involved in G protein-coupled receptor signaling, lipid raft modulation, and in balancing lipid composition within the cell. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:29609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29609) · Entrez [51205](https://www.ncbi.nlm.nih.gov/gene/51205) · UniProt [Q9NPH0](https://www.uniprot.org/uniprotkb/Q9NPH0) · Ensembl [ENSG00000162836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162836)

## Data

Gene col 8587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8587); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8587]; `tensor/DDL_lfc|DDL_z.npy` [8587]; `embed/gene_vectors.npy` [8587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8587 or target_col == 8587). Every well: [[ACP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
