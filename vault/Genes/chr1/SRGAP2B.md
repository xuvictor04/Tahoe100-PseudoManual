---
symbol: "SRGAP2B"
type: "gene"
col: 12190
ensembl_id: "ENSG00000196369"
name: "SLIT-ROBO Rho GTPase activating protein 2B"
location: "1q21.1"
module: 145
arm: "+"
pooled_cpm: 29.79
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 29
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# SRGAP2B

*SLIT-ROBO Rho GTPase activating protein 2B* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +9.5, q 1e-18, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.479× (z -11.9, q 5e-30, down in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.518× (z -11.1, q 5e-26, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP2]] (+0.92, fdr 7e-06), [[SRGAP2C]] (+0.88, fdr 7e-06), [[SRGAP2D]] (+0.74, fdr 7e-06); moves opposite to [[POLR2M]] (-0.58, fdr 1e-05), [[NUDT9]] (-0.57, fdr 1e-05), [[GTF2H3]] (-0.57, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +9.5 | 1e-18 | 35/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +7.9 | 1e-12 | 37/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +7.1 | 2e-10 | 33/48 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 7e-09 | 29/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.4 | 2e-08 | 28/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +4.2 | 0.003 | 22/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.005 | 19/48 (LoVo, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.006 | 12/46 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.012 | 17/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.014 | 16/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.4 | 0.033 | 12/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.057 | 14/47 (NCI-H23, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.479×** | -11.9 | 5e-30 | 30/39 (SHP-77, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -11.1 | 5e-26 | 34/47 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -10.8 | 4e-25 | 33/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -9.5 | 4e-19 | 25/33 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.579×** | -8.3 | 9e-15 | 25/43 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.584×** | -8.2 | 2e-14 | 28/48 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.727×** | -7.9 | 3e-13 | 27/47 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -7.8 | 6e-13 | 31/47 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -7.6 | 2e-12 | 31/47 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -7.5 | 3e-12 | 27/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -6.3 | 2e-08 | 29/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -6.2 | 2e-08 | 26/48 (Panc 03.27, SNU-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.547×** | -5.5 | 1e-06 | 20/33 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.3 | 4e-06 | 25/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -4.9 | 4e-05 | 23/43 (NCI-H1573, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -4.6 | 2e-04 | 23/48 (SK-MEL-2, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -4.5 | 2e-04 | 21/48 (A-427, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -4.4 | 3e-04 | 17/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.619×** | -4.4 | 3e-04 | 17/48 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.629×** | -4.2 | 6e-04 | 19/46 (A498, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.634×** | -4.2 | 8e-04 | 20/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.641×** | -4.1 | 0.001 | 16/46 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.9 | 2 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.200× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.345× (z -9.2) |
| [[A498 (line)]] | wt | 40.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -11.4) |
| [[PANC-1 (line)]] | alt | 32.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 60.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.372× (z -9.3) |
| [[A-172 (line)]] | wt | 44.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.280× (z -9.3) |
| [[A549 (line)]] | wt | 25.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0945× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -12.5) |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0520× (z -17.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.259× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 55.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 66.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.250× (z -11.0) |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.251× (z -9.7) |
| [[C32 (line)]] | wt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -11.6) |
| [[LoVo (line)]] | wt | 14.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.9) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -8.7) |
| [[SW 900 (line)]] | alt | 49.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -10.2) |
| [[KATO III (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -8.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0764× (z -19.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -11.1) |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2]] | +0.92 | +0.90 / +0.89 | both halves | 7e-06 | same gene group |
| [[SRGAP2C]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | same gene group; STRING 639 |
| [[SRGAP2D]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[POC1A]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.59 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SLC25A5]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[GNB2]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[UBL5]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CMC2]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RPS6KA5]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SNTB2]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2M]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NUDT9]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[GTF2H3]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[C17orf75]] | -0.56 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[GDAP1]] | -0.55 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[TCTN1]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SLC16A9]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RBBP9]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZBED9]] | -0.54 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[GUF1]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[TRUB1]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[KCTD14]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SRGAP2B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.9, -51.0); signed map (-51.4, -25.5). **Vector** length 89.2, 20.6% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | -0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +3.9 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.0 | -11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.6 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.1 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -7.0 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SLIT-ROBO Rho GTPase activating protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:144,887,265-145,095,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SRGAP2P2 |
| Gene groups (HGNC) | F-BAR domain containing; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DMP2](https://www.uniprot.org/uniprotkb/P0DMP2) (SLIT-ROBO Rho GTPase-activating protein 2B):

> May regulate cell migration and differentiation through interaction with and inhibition of SRGAP2. In contrast to SRGAP2C, it is not able to induce long-lasting changes in synaptic density throughout adulthood.

**Summary**, from NCBI Gene [647135](https://www.ncbi.nlm.nih.gov/gene/647135):

> This locus encodes a member of the SLIT-ROBO Rho GTPase activating protein family. This human-specific locus resulted from incomplete segmental duplication of the SLIT-ROBO Rho GTPase activating protein 2 locus. The encoded protein lacks the GTPase activating protein domain compared to proteins encoded by SLIT-ROBO Rho GTPase activating protein 2. The functionality of the protein encoded by this locus has been questioned, as several normal individuals with homozygous deletions for this locus …

**Accessions** — [HGNC:35237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35237) · Entrez [647135](https://www.ncbi.nlm.nih.gov/gene/647135) · UniProt [P0DMP2](https://www.uniprot.org/uniprotkb/P0DMP2) · Ensembl [ENSG00000196369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196369)

## Data

Gene col 12190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12190); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12190]; `tensor/DDL_lfc|DDL_z.npy` [12190]; `embed/gene_vectors.npy` [12190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12190 or target_col == 12190). Every well: [[SRGAP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGAP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
