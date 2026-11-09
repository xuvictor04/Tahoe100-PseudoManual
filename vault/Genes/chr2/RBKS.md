---
symbol: "RBKS"
type: "gene"
col: 10068
ensembl_id: "ENSG00000171174"
name: "ribokinase"
location: "2p23.2"
module: 159
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 44
n_dd_up: 26
n_dd_down: 35
n_dd_up_clean: 22
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# RBKS

*ribokinase* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +14.1, q 2e-42, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.450× (z -10.4, q 2e-22, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNISR-AS1]] (+0.62, fdr 2e-05), [[TAPBPL]] (+0.61, fdr 4e-05), [[PLS3-AS1]] (+0.60, fdr 2e-04); moves opposite to [[KIF21B]] (-0.61, fdr 3e-05), [[AP3M2]] (-0.59, fdr 6e-05), [[LYPLA1]] (-0.58, fdr 5e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PBX4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +14.1 | 2e-42 | 24/36 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.72×** | +6.8 | 3e-09 | 25/37 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +6.4 | 3e-08 | 18/37 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 2e-07 | 22/40 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +6.1 | 2e-07 | 20/42 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.9 | 3e-07 | 17/41 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +5.5 | 3e-06 | 22/41 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +5.2 | 2e-05 | 18/42 (MIA PaCa-2, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 3e-05 | 14/37 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.48×** | +4.9 | 5e-05 | 17/38 (HepG2/C3A, A-172, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 5e-05 | 18/41 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.8 | 8e-05 | 9/34 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 2e-04 | 9/40 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 2e-04 | 16/40 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 10/36 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 3e-04 | 13/42 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.450×** | -10.4 | 2e-22 | 32/39 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.470×** | -9.8 | 3e-20 | 33/42 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.511×** | -8.4 | 9e-15 | 25/33 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.599×** | -6.7 | 4e-09 | 25/38 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.614×** | -6.3 | 3e-08 | 20/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.721×** | -6.0 | 2e-07 | 25/41 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.662×** | -5.4 | 7e-06 | 21/41 (NCI-H23, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.663×** | -5.3 | 7e-06 | 20/41 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.673×** | -5.1 | 2e-05 | 20/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.677×** | -5.1 | 2e-05 | 21/39 (SNU-423, C32, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -5.0 | 3e-05 | 14/39 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.691×** | -4.8 | 8e-05 | 19/41 (C32, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.699×** | -4.6 | 1e-04 | 18/40 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -4.5 | 3e-04 | 16/36 (A549, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -4.5 | 3e-04 | 15/41 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.788×** | -4.4 | 4e-04 | 22/41 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.704×** | -4.4 | 4e-04 | 15/39 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.719×** | -4.3 | 5e-04 | 18/38 (SHP-77, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.735×** | -3.8 | 0.003 | 11/40 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.004 | 14/41 (NCI-H1792, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.006 | 15/41 (CFPAC-1, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.008 | 15/36 (CFPAC-1, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 7 (4 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.144× (z -11.3) |
| [[A-172 (line)]] | wt | 6.83 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +13.3) | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.251× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.212× (z -10.9) ⚠ cell-cycle shift, explains ~97% of this change |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.237× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 14.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0733× (z -15.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.257× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0595× (z -10.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 8.28 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.117× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.300× (z -9.1) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A-427 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR-AS1]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TAPBPL]] | +0.61 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[PLS3-AS1]] | +0.60 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[TET2]] | +0.60 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[KMO]] | +0.59 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[LGALS8]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LMLN]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[MFF-DT]] | +0.55 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[RBM48]] | +0.55 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[SNHG31]] | +0.55 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[MED28-DT]] | +0.55 | +0.60 / +0.22 | both halves | 6e-04 |  |
| [[ZNF563]] | +0.55 | +0.55 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF21B]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.59 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[LYPLA1]] | -0.58 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[GNA12]] | -0.57 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[PACC1]] | -0.55 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[TOR4A]] | -0.55 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[RALGPS1]] | -0.55 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[INPP4A]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MICAL2]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[BCR]] | -0.54 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[RSU1]] | -0.54 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PCMT1]] | -0.54 | -0.46 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBKS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers RBKS's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBX4]] | B | RBKS activity raises PBX4's level | lines that do not express RBKS (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without RBKS | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SNHG31]] | B | RBKS activity raises SNHG31's level | lines that do not express RBKS (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without RBKS | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TNK2]] | B | RBKS activity raises TNK2's level | lines that do not express RBKS (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without RBKS | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction -0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 3.9); signed map (23.2, -16.6). **Vector** length 95.3, 21.8% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.2 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.4 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.2 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ribokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:27,781,379-27,890,681 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686G13268, RBSK |
| Gene groups (HGNC) | Carbohydrate kinases |
| Reactome | 2 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H477](https://www.uniprot.org/uniprotkb/Q9H477) (Ribokinase):

> Catalyzes the phosphorylation of ribose at O-5 in a reaction requiring ATP and magnesium. The resulting D-ribose-5-phosphate can then be used either for sythesis of nucleotides, histidine, and tryptophan, or as a component of the pentose phosphate pathway.

**Summary**, from NCBI Gene [64080](https://www.ncbi.nlm.nih.gov/gene/64080):

> This gene encodes a member of the carbohydrate kinase PfkB family. The encoded protein phosphorylates ribose to form ribose-5-phosphate in the presence of ATP and magnesium as a first step in ribose metabolism. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:30325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30325) · Entrez [64080](https://www.ncbi.nlm.nih.gov/gene/64080) · UniProt [Q9H477](https://www.uniprot.org/uniprotkb/Q9H477) · Ensembl [ENSG00000171174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171174)

## Data

Gene col 10068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10068); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10068]; `tensor/DDL_lfc|DDL_z.npy` [10068]; `embed/gene_vectors.npy` [10068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10068 or target_col == 10068). Every well: [[RBKS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBKS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
