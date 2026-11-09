---
symbol: "GRB7"
type: "gene"
col: 6570
ensembl_id: "ENSG00000141738"
name: "growth factor receptor bound protein 7"
location: "17q12"
module: 8
arm: "+"
pooled_cpm: 31.34
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 32
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 32
direction_downstream: 59
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GRB7

*growth factor receptor bound protein 7* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.04× (z +8.1, q 3e-13, up in 15 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.90× (z +5.2, q 5e-05, up in 12 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.343× (z -12.2, q 2e-31, down in 23 of 23 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.530× (z -6.9, q 1e-09, down in 20 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUP]] (+0.65, fdr 7e-06), [[SPINT1]] (+0.65, fdr 7e-06), [[TJP2]] (+0.64, fdr 7e-06); moves opposite to [[CLPB]] (-0.59, fdr 2e-05), [[RPTOR]] (-0.58, fdr 1e-05), [[TAS2R30]] (-0.54, fdr 9e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 59 go from it, the strongest it → [[CCDC120]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +8.1 | 3e-13 | 15/23 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +5.2 | 5e-05 | 12/23 (AsPC-1, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.5 | 0.001 | 14/22 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.015 | 10/23 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.034 | 11/23 (SW1417, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.041 | 11/24 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.10 | 10/23 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.32× | +3.0 | 0.17 | 16/24 (NCI-H2030, CFPAC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.343×** | -12.2 | 2e-31 | 23/23 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.530×** | -6.9 | 1e-09 | 20/23 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.579×** | -6.2 | 1e-07 | 21/23 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.606×** | -5.3 | 2e-05 | 12/23 (HCT15, LoVo, …) | all doses, flat | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.351×** | -4.9 | 1e-04 | 18/23 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -4.8 | 2e-04 | 18/23 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.655×** | -4.6 | 3e-04 | 15/23 (LoVo, CFPAC-1, …) | all doses, flat | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.386×** | -4.5 | 6e-04 | 17/23 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.696×** | -4.1 | 0.002 | 10/23 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.699×** | -4.1 | 0.003 | 16/23 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.688×** | -4.0 | 0.003 | 20/23 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.697×** | -3.9 | 0.004 | 17/18 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.440×** | -3.8 | 0.005 | 20/23 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.719×** | -3.8 | 0.007 | 15/23 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.631×** | -3.7 | 0.007 | 14/23 (CFPAC-1, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.633×** | -3.7 | 0.007 | 14/23 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.483×** | -3.4 | 0.021 | 17/23 (SW1417, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.730×** | -3.3 | 0.027 | 8/23 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.3 | 0.028 | 16/23 (CFPAC-1, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.028 | 8/24 (LoVo, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -3.2 | 0.033 | 15/23 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 13 (10 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.146× (z -18.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 60.8 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -19.8) ⚠ unreliable plate only · without an alert: [[Belumosudil (drug)]] 5 µM 0.324× (z -9.3) |
| [[COLO 205 (line)]] | alt | 50.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -9.0) |
| [[SW480 (line)]] | alt | 28.5 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -13.3) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 33.1 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.110× (z -13.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -10.8) |
| [[HCT15 (line)]] | alt | 51.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -11.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -8.9) |
| [[HT-29 (line)]] | alt | 42.2 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.117× (z -15.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 24.5 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.116× (z -15.0) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -11.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 68.6 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -11.3) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 67.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -16.9) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 37.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.134× (z -16.1) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -9.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.181× (z -8.9) |
| [[KATO III (line)]] | alt | 33.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0631× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SW48 (line)]] | wt | 25.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.118× (z -9.2) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +15.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 579 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -9.3) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.128× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -8.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUP]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[SPINT1]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[TJP2]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.61 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[NECTIN4]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[YPEL3]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PIM1]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FBXO33]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[USP6NL]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[RNF39]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[MXD1]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPB]] | -0.59 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[RPTOR]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TAS2R30]] | -0.54 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[MCM3AP]] | -0.54 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[L3HYPDH]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PTPN11]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 622 |
| [[ABCF2]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[MRPS27]] | -0.51 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[CPQ]] | -0.51 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ABCE1]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SUCLG2]] | -0.50 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 4, C 28. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises GRB7's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without SEMA3B | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises GRB7's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 4.36× lower at baseline in the lines without CCDC120 | 0.026 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[TMC6]] | B | TMC6 activity raises GRB7's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 4.55× lower at baseline in the lines without TMC6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[PRSS8]] | B | PRSS8 activity strengthens GRB7's drug response | lines that do not express PRSS8 (8) vs lines expressing it (15) | the lines without PRSS8 respond 0.77× as strongly (z diff +1.41); strongest at c-Kit-IN-1 0.05 µM: 0.27x vs 0.17x (z diff +3.9) | 0.084 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; target measured in part of the lines; artifact flags |
| [[INAVA]] | C | INAVA activity raises GRB7's level | lines that do not express INAVA (29) vs lines expressing it (21) | 5.27× lower at baseline in the lines without INAVA | 7e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[MPZL3]] | C | MPZL3 activity raises GRB7's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 6.26× lower at baseline in the lines without MPZL3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises GRB7's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 8.14× lower at baseline in the lines without PRSS8 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |
| [[IRF6]] | C | IRF6 activity raises GRB7's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 7.22× lower at baseline in the lines without IRF6 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises GRB7's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 8.05× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises GRB7's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 6.60× lower at baseline in the lines without MPZL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[ERBB3]] | C | ERBB3 activity raises GRB7's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 6.07× lower at baseline in the lines without ERBB3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; co-absent with the target |
| [[TMC4]] | C | TMC4 activity raises GRB7's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 5.06× lower at baseline in the lines without TMC4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 32, C 27. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | GRB7 activity raises CCDC120's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without GRB7 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[PARD6B]] | B | GRB7 activity raises PARD6B's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.49× lower at baseline in the lines without GRB7 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[TMC6]] | B | GRB7 activity raises TMC6's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 4.09× lower at baseline in the lines without GRB7 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[RAB11FIP1]] | B | GRB7 activity raises RAB11FIP1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without GRB7 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[RHPN2]] | B | GRB7 activity raises RHPN2's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.10× lower at baseline in the lines without GRB7 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[BAIAP2L1]] | B | GRB7 activity raises BAIAP2L1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without GRB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[RASSF7]] | B | GRB7 activity raises RASSF7's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.42× lower at baseline in the lines without GRB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[PTK2B]] | B | GRB7 activity raises PTK2B's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.18× lower at baseline in the lines without GRB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[SEMA3B]] | B | GRB7 activity raises SEMA3B's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without GRB7 | 0.006 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[ABL1]] | B | GRB7 activity lowers ABL1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.67× higher at baseline in the lines without GRB7 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[USP6NL]] | B | GRB7 activity raises USP6NL's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without GRB7 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[FNBP1L]] | B | GRB7 activity raises FNBP1L's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without GRB7 | 0.012 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.1, 57.8); signed map (55.4, 9.4). **Vector** length 96.3, 34.6% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.2 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.0 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +5.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +3.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -12.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | growth factor receptor bound protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,737,927-39,747,291 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; Growth factor receptor bound protein 7 family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 16 pathways, smallest: GRB7 events in ERBB2 signaling; Tie2 Signaling; Downstream signal transduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14451](https://www.uniprot.org/uniprotkb/Q14451) (Growth factor receptor-bound protein 7):

> Adapter protein that interacts with the cytoplasmic domain of numerous receptor kinases and modulates down-stream signaling. Promotes activation of down-stream protein kinases, including STAT3, AKT1, MAPK1 and/or MAPK3. Promotes activation of HRAS. Plays a role in signal transduction in response to EGF. Plays a role in the regulation of cell proliferation and cell migration. Plays a role in the assembly and stability of RNA stress granules. Binds to the 5'UTR of target mRNA molecules and …

**Summary**, from NCBI Gene [2886](https://www.ncbi.nlm.nih.gov/gene/2886):

> The product of this gene belongs to a small family of adapter proteins that are known to interact with a number of receptor tyrosine kinases and signaling molecules. This gene encodes a growth factor receptor-binding protein that interacts with epidermal growth factor receptor (EGFR) and ephrin receptors. The protein plays a role in the integrin signaling pathway and cell migration by binding with focal adhesion kinase (FAK). Several transcript variants encoding two different isoforms have been …

**Accessions** — [HGNC:4567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4567) · Entrez [2886](https://www.ncbi.nlm.nih.gov/gene/2886) · UniProt [Q14451](https://www.uniprot.org/uniprotkb/Q14451) · Ensembl [ENSG00000141738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141738)

## Data

Gene col 6570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6570); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6570]; `tensor/DDL_lfc|DDL_z.npy` [6570]; `embed/gene_vectors.npy` [6570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6570 or target_col == 6570). Every well: [[GRB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
