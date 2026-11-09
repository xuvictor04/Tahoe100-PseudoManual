---
symbol: "FOXO4"
type: "gene"
col: 11542
ensembl_id: "ENSG00000184481"
name: "forkhead box O4"
location: "Xq13.1"
module: 76
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 23
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# FOXO4

*forkhead box O4* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.54× (z +9.6, q 3e-19, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +6.2, q 1e-07, up in 16 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.417× (z -9.3, q 6e-18, down in 32 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.463× (z -8.2, q 4e-14, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALCOCO1]] (+0.70, fdr 7e-06), [[UBXN6]] (+0.65, fdr 1e-05), [[YPEL3]] (+0.65, fdr 7e-06); moves opposite to [[METTL2B]] (-0.55, fdr 1e-05), [[ST3GAL3]] (-0.54, fdr 3e-05), [[TANGO6]] (-0.53, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABCG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +9.6 | 3e-19 | 5/7 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.4 | 1e-14 | 17/23 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.2 | 1e-07 | 16/40 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +5.7 | 2e-06 | 21/46 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.43×** | +5.5 | 5e-06 | 10/45 (LS 180, COLO 205, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.2 | 2e-05 | 5/11 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +4.9 | 1e-04 | 16/46 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 4e-04 | 10/44 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.1 | 0.002 | 5/27 (NCI-H1792, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.0 | 0.003 | 10/46 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.003 | 12/39 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.004 | 10/34 (NCI-H460, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 14/46 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 6/44 (NCI-H460, KATO III, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.62×** | +3.7 | 0.009 | 4/37 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.046 | 1/36 (SW480) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.046 | 1/24 (Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.048 | 13/46 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.050 | 5/41 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.051 | 3/45 (KATO III, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.417×** | -9.3 | 6e-18 | 32/46 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.430×** | -9.0 | 8e-17 | 29/47 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.447×** | -8.6 | 2e-15 | 18/33 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.463×** | -8.2 | 4e-14 | 29/45 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.533×** | -6.7 | 3e-09 | 23/46 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.648×** | -6.5 | 7e-09 | 22/38 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -6.4 | 1e-08 | 20/38 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.566×** | -6.0 | 1e-07 | 23/44 (HT-29, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.567×** | -6.0 | 1e-07 | 23/45 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -5.2 | 1e-05 | 18/45 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.408×** | -5.0 | 3e-05 | 12/36 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.412×** | -4.9 | 4e-05 | 16/44 (LoVo, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.423×** | -4.8 | 7e-05 | 19/38 (SW480, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.442×** | -4.5 | 2e-04 | 13/35 (HT-29, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.649×** | -4.4 | 4e-04 | 17/43 (COLO 205, HT-29, …) | two highest doses | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -4.1 | 0.001 | 14/42 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.480×** | -4.1 | 0.001 | 18/38 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.590×** | -4.0 | 0.002 | 8/46 (BT-474, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.694×** | -3.7 | 0.007 | 13/45 (SW48, SW480, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.697×** | -3.6 | 0.008 | 11/45 (Hs 766T, A-427, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.577×** | -3.1 | 0.055 | 11/27 (LoVo, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 11.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0919× (z -11.9) |
| [[SW480 (line)]] | alt | 7.25 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.208× (z -8.6) |
| [[COLO 205 (line)]] | alt | 9.54 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0974× (z -8.6) |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0646× (z -8.9) |
| [[LS 180 (line)]] | wt | 7.27 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0657× (z -10.2) |
| [[SW1417 (line)]] | alt | 5.69 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -8.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCOCO1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[UBXN6]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[YPEL3]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CTDSP2]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[WDTC1]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[YPEL2]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[PAIP2B]] | +0.59 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ASS1]] | +0.59 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[FKBP8]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 | pathway: Deubiquitination |
| [[CDK5RAP3]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TCP11L2]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL2B]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ST3GAL3]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TANGO6]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[LARS2]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.50 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[NOC3L]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[BICD1]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PCOLCE2]] | -0.49 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[TAS2R14]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[METTL8]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCG1]] | B | ABCG1 activity raises FOXO4's level | lines that do not express ABCG1 (15) vs lines expressing it (35) | 1.11× lower at baseline in the lines without ABCG1 | 0.088 | ⚠ within organs, on part of the lines; also absent: RSPH1, OLFM1, PDK4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.1, -46.6); signed map (-17.4, 9.2). **Vector** length 61.1, 8.87% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.2 | +5.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -9.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box O4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,095,851-71,103,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AFX1; previously MLLT7 |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | MYOGENESIS |
| Reactome | 15 pathways, smallest: AKT phosphorylates targets in the nucleus; Regulation of FOXO transcriptional activity by acetylation; Regulation of localization of FOXO transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P98177](https://www.uniprot.org/uniprotkb/P98177) (Forkhead box protein O4):

> Transcription factor involved in the regulation of the insulin signaling pathway. Binds to insulin-response elements (IREs) and can activate transcription of IGFBP1. Down-regulates expression of HIF1A and suppresses hypoxia-induced transcriptional activation of HIF1A-modulated genes. Also involved in negative regulation of the cell cycle. Involved in increased proteasome activity in embryonic stem cells (ESCs) by activating expression of PSMD11 in ESCs, leading to enhanced assembly of the 26S …

**Summary**, from NCBI Gene [4303](https://www.ncbi.nlm.nih.gov/gene/4303):

> This gene encodes a member of the O class of winged helix/forkhead transcription factor family. Proteins encoded by this class are regulated by factors involved in growth and differentiation indicating they play a role in these processes. A translocation involving this gene on chromosome X and the homolog of the Drosophila trithorax gene, encoding a DNA binding protein, located on chromosome 11 is associated with leukemia. Multiple transcript variants encoding different isoforms have been found …

**Accessions** — [HGNC:7139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7139) · Entrez [4303](https://www.ncbi.nlm.nih.gov/gene/4303) · UniProt [P98177](https://www.uniprot.org/uniprotkb/P98177) · Ensembl [ENSG00000184481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184481)

## Data

Gene col 11542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11542); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11542]; `tensor/DDL_lfc|DDL_z.npy` [11542]; `embed/gene_vectors.npy` [11542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11542 or target_col == 11542). Every well: [[FOXO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
