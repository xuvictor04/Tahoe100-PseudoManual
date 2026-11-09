---
symbol: "EGR3"
type: "gene"
col: 11027
ensembl_id: "ENSG00000179388"
name: "early growth response 3"
location: "8p21.3"
module: 109
arm: "+"
pooled_cpm: 11.31
n_lines_expressing: 41
n_dd_up: 13
n_dd_down: 43
n_dd_up_clean: 8
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 10
direction_downstream: 6
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# EGR3

*early growth response 3* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.81× (z +18.6, q 0e+00, up in 34 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.164× (z -13.1, q 1e-36, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR2]] (+0.92, fdr 7e-06), [[EGR1]] (+0.90, fdr 7e-06), [[IER2]] (+0.79, fdr 7e-06); moves opposite to [[FHIP2A]] (-0.66, fdr 7e-06), [[ZNF148]] (-0.62, fdr 1e-05), [[RWDD3]] (-0.62, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HAS2]] → it (grade B ⚠); 6 go from it, the strongest it → [[PHLDA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.81×** | +18.6 | 0e+00 | 34/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.62×** | +11.4 | 2e-27 | 28/38 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +6.1 | 2e-07 | 21/36 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.39×** | +6.0 | 4e-07 | 28/39 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +5.9 | 5e-07 | 30/39 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.18×** | +5.3 | 9e-06 | 13/26 (NCI-H460, CFPAC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.10×** | +5.1 | 3e-05 | 24/39 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +3.9 | 0.007 | 21/39 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.74×** | +3.7 | 0.016 | 5/16 (RPMI-7951, CFPAC-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.025 | 19/38 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.68×** | +3.3 | 0.049 | 5/19 (CFPAC-1, RPMI-7951, …) | all doses, flat | composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.073 | 10/39 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.086 | 15/39 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.164×** | -13.1 | 1e-36 | 36/39 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.154×** | -12.3 | 2e-32 | 36/37 (C32, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.201×** | -11.0 | 1e-25 | 36/39 (SW48, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.284×** | -10.7 | 2e-24 | 35/39 (SW480, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.199×** | -10.2 | 2e-22 | 35/38 (SW480, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.228×** | -9.7 | 2e-20 | 34/38 (SW48, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.399×** | -8.8 | 8e-17 | 33/39 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.416×** | -8.5 | 2e-15 | 30/39 (SW48, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.296×** | -8.3 | 5e-15 | 29/38 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.310×** | -8.0 | 7e-14 | 29/37 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.385×** | -7.7 | 6e-13 | 31/39 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.462×** | -6.5 | 3e-09 | 27/39 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.408×** | -6.1 | 4e-08 | 27/38 (hTERT-HPNE, NCI-H23, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.535×** | -6.0 | 7e-08 | 27/39 (C32, NCI-H23, …) | rises with dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.421×** | -5.9 | 1e-07 | 27/38 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.425×** | -5.8 | 2e-07 | 30/37 (H4, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 39.0 | 1 | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +10.9) | [[Cobimetinib (drug)]] 5 µM 0.0161× (z -17.6) |
| [[SW480 (line)]] | alt | 42.3 | 1 | 11 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +12.8) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0390× (z -17.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 3 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +16.9) | [[Adagrasib (drug)]] 0.05 µM 0.299× (z -17.4) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.0800× (z -10.6) |
| [[HOP62 (line)]] | alt | 18.6 | 2 | 7 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +15.4) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0498× (z -11.1) |
| [[SW48 (line)]] | wt | 86.7 | 0 | 7 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0141× (z -19.7) |
| [[NCI-H23 (line)]] | alt | 7.02 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.416× (z -9.4) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.0543× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 3.99 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 40.0× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 22.2 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +12.0) | [[Selinexor (drug)]] 5 µM 0.146× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0914× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 8.62× (z +8.5) | [[Cobimetinib (drug)]] 0.5 µM 0.0803× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 9.29 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +10.3) | [[Ponatinib (drug)]] 5 µM 0.0218× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 3 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0450× (z -10.2) |
| [[RKO (line)]] | wt | 22.6 | 0 | 3 | — | [[Cobimetinib (drug)]] 5 µM 0.0325× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 33.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +11.2) | [[Cobimetinib (drug)]] 5 µM 0.0285× (z -12.6) |
| [[H4 (line)]] | wt | 9.46 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0268× (z -9.9) |
| [[Hs 766T (line)]] | wt | 19.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.151× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 18.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +13.7) | — |
| [[LoVo (line)]] | wt | 12.0 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0988× (z -9.2) |
| [[SNU-423 (line)]] | alt | 7.43 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +13.4) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0541× (z -8.5) |
| [[SW 900 (line)]] | alt | 13.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +9.3) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0641× (z -9.0) |
| [[A-172 (line)]] | wt | 3.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +12.1) | — |
| [[A-427 (line)]] | wt | 4.67 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.0392× (z -9.0) |
| [[A549 (line)]] | wt | 6.34 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.112× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 3.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.1× (z +16.5) | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0330× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 9.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 10.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 13.7× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0779× (z -9.9) |
| [[A498 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR2]] | +0.92 | +0.91 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 987 |
| [[EGR1]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 876 |
| [[IER2]] | +0.79 | +0.82 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 560 |
| [[ASTL]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ERCC1]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.75 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[MCL1]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[PHLDA1]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DUSP6]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Nuclear Events (kinase and transcription factor activation); STRING 572 |
| [[HIVEP3]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 | same gene group |
| [[BCL2L12]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[BTBD19]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[ZNF148]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 | same gene group |
| [[RWDD3]] | -0.62 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[SNX4]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[RNPC3]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[FPGT]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NAPB]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[FBXO9]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.57 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[RTCA]] | -0.56 | -0.52 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAS2]] | B | HAS2 activity raises EGR3's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without HAS2 | 0.022 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[PLAT]] | B | PLAT activity raises EGR3's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without PLAT | 0.024 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[LINC01204]] | B | LINC01204 activity raises EGR3's level | lines that do not express LINC01204 (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without LINC01204 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC00460, WNT5A, LNCOG; maybe low, not absent |
| [[LINC00460]] | B | LINC00460 activity raises EGR3's level | lines that do not express LINC00460 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without LINC00460 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC02335, LINC01605, KISS1 |
| [[NPAS2]] | B | NPAS2 activity raises EGR3's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 3.26× lower at baseline in the lines without NPAS2 | 0.055 | ⚠ within organs, on part of the lines |
| [[LINC02454]] | B | LINC02454 activity raises EGR3's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without LINC02454 | 0.084 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[ETV1]] | B | ETV1 activity strengthens EGR3's drug response | lines that do not express ETV1 (10) vs lines expressing it (29) | the lines without ETV1 respond 0.72× as strongly (z diff +1.66); strongest at Trametinib 0.05 µM: 0.52x vs 0.33x (z diff +2.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EGR3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ASTL]] | B | ASTL activity raises EGR3's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without ASTL | 0.099 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[EPHA2]] | C | EPHA2 activity weakens EGR3's drug response | lines that do not express EPHA2 (10) vs lines expressing it (29) | the lines without EPHA2 respond 1.12× as strongly (z diff -1.58); strongest at Trametinib (DMSO_TF solvate) 5 µM: 0.14x vs 0.20x (z diff -2.7) | 0.096 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent; target measured in part of the lines; rests on the correction |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA1]] | B | EGR3 activity raises PHLDA1's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without EGR3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[CIAO2A]] | B | EGR3 activity lowers CIAO2A's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 1.38× higher at baseline in the lines without EGR3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[NPAS2]] | B | EGR3 activity raises NPAS2's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 3.17× lower at baseline in the lines without EGR3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[SPRED1]] | B | EGR3 activity raises SPRED1's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without EGR3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[EGR2]] | B | EGR3 activity raises EGR2's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 2.24× lower at baseline in the lines without EGR3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[VCL]] | B | EGR3 activity raises VCL's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without EGR3 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.915). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.6, -0.6); signed map (5.8, 29.7). **Vector** length 136, 39.9% of its response variance represented; |z| ≥ 3 in 1,381 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.6 | -13.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.1 | -10.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.1 | -11.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.8 | -12.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.7 | -9.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -7.5 | -10.2 |

## What is on record

|  |  |
|---|---|
| Name | early growth response 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,687,659-22,693,480 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PILOT |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Early growth response family |
| Hallmark sets | APOPTOSIS, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06889](https://www.uniprot.org/uniprotkb/Q06889) (Early growth response protein 3):

> Probable transcription factor involved in muscle spindle development.

**Summary**, from NCBI Gene [1960](https://www.ncbi.nlm.nih.gov/gene/1960):

> This gene encodes a transcriptional regulator that belongs to the EGR family of C2H2-type zinc-finger proteins. It is an immediate-early growth response gene which is induced by mitogenic stimulation. The protein encoded by this gene participates in the transcriptional regulation of genes in controling biological rhythm. It may also play a role in a wide variety of processes including muscle development, lymphocyte development, endothelial cell growth and migration, and neuronal development. …

**Accessions** — [HGNC:3240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3240) · Entrez [1960](https://www.ncbi.nlm.nih.gov/gene/1960) · UniProt [Q06889](https://www.uniprot.org/uniprotkb/Q06889) · Ensembl [ENSG00000179388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179388)

## Data

Gene col 11027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11027); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11027]; `tensor/DDL_lfc|DDL_z.npy` [11027]; `embed/gene_vectors.npy` [11027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11027 or target_col == 11027). Every well: [[EGR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
