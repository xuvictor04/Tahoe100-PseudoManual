---
symbol: "PDE4DIP"
type: "gene"
col: 10897
ensembl_id: "ENSG00000178104"
name: "phosphodiesterase 4D interacting protein"
location: "1q21.2"
module: 56
arm: "+"
pooled_cpm: 33.18
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PDE4DIP

*phosphodiesterase 4D interacting protein* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 2.11× (z +14.0, q 5e-42, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.492× (z -13.3, q 1e-37, down in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.553× (z -11.1, q 3e-26, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE4DIPP2]] (+0.77, fdr 7e-06), [[LINC02693]] (+0.68, fdr 9e-06), [[ENTPD7]] (+0.65, fdr 1e-05); moves opposite to [[TCF12]] (-0.56, fdr 3e-05), [[GTF3C6]] (-0.56, fdr 2e-04), [[VPS35L]] (-0.56, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PDE4DIPP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +14.0 | 5e-42 | 38/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +13.8 | 5e-41 | 38/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +13.2 | 2e-37 | 38/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +13.0 | 3e-36 | 36/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +9.3 | 1e-18 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +8.5 | 2e-15 | 31/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +7.0 | 2e-10 | 32/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.027 | 10/46 (LOX-IMVI, A498, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +3.3 | 0.059 | 7/48 (SHP-77, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.060 | 15/48 (NCI-H2347, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -13.3 | 1e-37 | 35/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -11.1 | 3e-26 | 31/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.588×** | -10.0 | 4e-21 | 36/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -9.7 | 3e-20 | 29/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.700×** | -9.5 | 3e-19 | 27/47 (HOP62, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.615×** | -8.8 | 1e-16 | 28/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.685×** | -7.1 | 9e-11 | 25/42 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -6.5 | 5e-09 | 30/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -6.4 | 9e-09 | 19/36 (A498, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -5.3 | 8e-06 | 19/47 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.756×** | -5.1 | 2e-05 | 14/31 (A498, NCI-H1792, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.771×** | -4.9 | 4e-05 | 24/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -4.9 | 4e-05 | 19/41 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.628×** | -4.6 | 2e-04 | 16/44 (NCI-H23, A549, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.792×** | -4.4 | 5e-04 | 19/46 (A549, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.805×** | -3.9 | 0.004 | 15/47 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.810×** | -3.8 | 0.004 | 17/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.707×** | -3.4 | 0.018 | 12/45 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.837× | -3.2 | 0.033 | 21/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.045 | 14/48 (H4, KATO III, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.844× | -3.1 | 0.049 | 6/48 (HOP62, AsPC-1, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | 0.899× | -2.8 | 0.096 | 7/48 (SW 1271, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 141 | 0 | 29 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.527× (z -19.5) ⚠ position not correctable · without an alert: [[Budesonide (drug)]] 0.05 µM 0.242× (z -12.1) |
| [[A498 (line)]] | wt | 53.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.402× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 19.4 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.10× (z +8.5) | [[Homoharringtonine (drug)]] 0.05 µM 0.212× (z -12.6) |
| [[PANC-1 (line)]] | alt | 14.4 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.41× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 68.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 18.5 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.172× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -8.6) |
| [[HT-29 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.4) | — |
| [[A549 (line)]] | wt | 9.76 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0248× (z -23.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.386× (z -8.5) |
| [[SW48 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE4DIPP2]] | +0.77 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[LINC02693]] | +0.68 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[ENTPD7]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SEC22B]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PJA2]] | +0.60 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[ZNF526]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.59 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PRRC1]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ERLEC1]] | +0.57 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[SGSM1]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SLC31A1]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SUCO]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF12]] | -0.56 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[GTF3C6]] | -0.56 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[VPS35L]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[KDM3B]] | -0.51 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[KIAA0825]] | -0.51 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[TRAPPC8]] | -0.51 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ITPA]] | -0.50 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.50 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[QTRT1]] | -0.50 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ZFX]] | -0.50 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[MRPS7]] | -0.49 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[DLG5]] | -0.49 | -0.40 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4DIPP2]] | B | PDE4DIPP2 activity raises PDE4DIP's level | lines that do not express PDE4DIPP2 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without PDE4DIPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: INTS6L, IQCJ-SCHIP1; maybe low, not absent |
| [[LINC00632]] | B | LINC00632 activity raises PDE4DIP's level | lines that do not express LINC00632 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without LINC00632 | 0.056 | ⚠ within organs, on part of the lines; also absent: CCBE1, EPHA5-AS1, PAPPA |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PDE4DIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PDE4DIP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WDFY2]] | C | WDFY2's natural level strengthens PDE4DIP's drug response | WDFY2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.12; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, -32.5); signed map (-50.9, 6.9). **Vector** length 103, 24.8% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +13.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.2 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 4D interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:148,808,140-149,048,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0477, KIAA0454, MMGL; previously CMYA2 |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VU43](https://www.uniprot.org/uniprotkb/Q5VU43) (Myomegalin):

> Functions as an anchor sequestering components of the cAMP-dependent pathway to Golgi and/or centrosomes (By similarity).; [Isoform 13]: Participates in microtubule dynamics, promoting microtubule assembly. Depending upon the cell context, may act at the level of the Golgi apparatus or that of the centrosome. In complex with AKAP9, recruits CAMSAP2 to the Golgi apparatus and tethers non-centrosomal minus-end microtubules to the Golgi, an important step for polarized cell movement. In complex …

**Summary**, from NCBI Gene [9659](https://www.ncbi.nlm.nih.gov/gene/9659):

> The protein encoded by this gene serves to anchor phosphodiesterase 4D to the Golgi/centrosome region of the cell. Defects in this gene may be a cause of myeloproliferative disorder (MBD) associated with eosinophilia. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:15580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15580) · Entrez [9659](https://www.ncbi.nlm.nih.gov/gene/9659) · UniProt [Q5VU43](https://www.uniprot.org/uniprotkb/Q5VU43) · Ensembl [ENSG00000178104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178104)

## Data

Gene col 10897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10897); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10897]; `tensor/DDL_lfc|DDL_z.npy` [10897]; `embed/gene_vectors.npy` [10897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10897 or target_col == 10897). Every well: [[PDE4DIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE4DIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
