---
symbol: "TRABD2B"
type: "gene"
col: 15614
ensembl_id: "ENSG00000269113"
name: "TraB domain containing 2B"
location: "1p33"
module: 5
arm: "+"
pooled_cpm: 14.57
n_lines_expressing: 31
n_dd_up: 6
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRABD2B

*TraB domain containing 2B* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +5.0, q 3e-04, up in 12 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.306× (z -15.7, q 0e+00, down in 22 of 26 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.210× (z -14.6, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS9]] (+0.56, fdr 3e-05), [[PRRC2B]] (+0.55, fdr 3e-05), [[PXYLP1]] (+0.55, fdr 1e-05); moves opposite to [[DBP]] (-0.58, fdr 3e-05), [[ATP8B1]] (-0.50, fdr 3e-05), [[PGPEP1]] (-0.49, fdr 9e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PTGFRN]] → it (grade B ⚠); 9 go from it, the strongest it → [[GSAP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-04 | 12/28 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 0.003 | 14/28 (NCI-H1792, SK-MEL-2, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.013 | 11/28 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.68×** | +3.9 | 0.013 | 12/28 (NCI-H1792, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.014 | 14/28 (NCI-H1792, SK-MEL-2, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.022 | 14/28 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.306×** | -15.7 | 0e+00 | 22/26 (SK-MEL-2, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.210×** | -14.6 | 0e+00 | 26/28 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.218×** | -14.3 | 4e-44 | 26/28 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.223×** | -14.1 | 6e-43 | 28/28 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.270×** | -12.3 | 1e-32 | 27/28 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.330×** | -10.4 | 3e-23 | 25/28 (LoVo, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.381×** | -8.7 | 3e-16 | 23/27 (C32, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.412×** | -8.3 | 6e-15 | 19/26 (A549, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.414×** | -8.3 | 9e-15 | 24/28 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.429×** | -7.9 | 1e-13 | 20/28 (BT-474, C-33 A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.438×** | -7.7 | 6e-13 | 23/28 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.429×** | -7.6 | 1e-12 | 19/26 (SW48, RKO, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.496×** | -6.6 | 2e-09 | 21/28 (BT-474, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -5.3 | 6e-06 | 17/28 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.475×** | -5.3 | 6e-06 | 17/28 (A549, C32, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.413×** | -4.3 | 5e-04 | 14/27 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -4.3 | 6e-04 | 16/27 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -3.8 | 0.004 | 13/28 (SK-MEL-2, C32, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.679×** | -3.6 | 0.008 | 13/28 (J82, C32, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.676×** | -3.5 | 0.011 | 8/28 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.788×** | -3.1 | 0.037 | 10/28 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.054 | 10/28 (RKO, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -2.9 | 0.079 | 11/28 (C32, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.89 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 39.8 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -18.7) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0698× (z -15.2) |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0366× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 60.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -20.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0581× (z -18.2) |
| [[SW48 (line)]] | wt | 22.4 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0479× (z -11.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0632× (z -10.5) |
| [[A-172 (line)]] | wt | 104 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0552× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0781× (z -10.2) |
| [[C32 (line)]] | wt | 68.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -15.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.117× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.150× (z -11.5) |
| [[J82 (line)]] | alt | 23.2 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.151× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.102× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 36.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -16.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.103× (z -11.2) |
| [[LoVo (line)]] | wt | 17.9 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.101× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.176× (z -9.5) |
| [[SW480 (line)]] | alt | 8.09 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0458× (z -15.4) |
| [[RKO (line)]] | wt | 11.1 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0815× (z -10.5) |
| [[A-427 (line)]] | wt | 24.3 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0867× (z -14.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.218× (z -9.2) |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0938× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.114× (z -9.5) |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 3 (1 ⚠) | — | [[Simotinib (drug)]] 0.05 µM 0.0713× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 13.2 | 1 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 6.14× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.0974× (z -10.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.122× (z -10.4) |
| [[A498 (line)]] | wt | 11.1 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0430× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 5.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 8.48 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0721× (z -10.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AsPC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS9]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PRRC2B]] | +0.55 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[PXYLP1]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LDLRAD3]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MAP3K6]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[UTP4]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[APBA2]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SIRPA]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[AP5B1]] | +0.52 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[PTPRG]] | +0.52 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[TSR1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | -0.58 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ATP8B1]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PGPEP1]] | -0.49 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[MOSPD2]] | -0.48 | -0.32 / -0.45 | both halves | 1e-04 |  |
| [[AFTPH]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[PURA]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CCDC127]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[TBC1D17]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[KIF16B]] | -0.45 | -0.36 / -0.32 | both halves | 1e-04 |  |
| [[AKAP9]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[TESK2]] | -0.44 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[INIP]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGFRN]] | B | PTGFRN activity raises TRABD2B's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 3.06× lower at baseline in the lines without PTGFRN | 0.064 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[FAXC]] | B | FAXC activity raises TRABD2B's level | lines that do not express FAXC (11) vs lines expressing it (39) | 3.35× lower at baseline in the lines without FAXC | 0.078 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[SERPINA3]] | B | SERPINA3 activity raises TRABD2B's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.13× lower at baseline in the lines without SERPINA3 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5 |
| [[NR3C1]] | B | NR3C1 activity raises TRABD2B's level | compounds that target NR3C1: 2 of 3 raise it (Betamethasone dipropionate, Budesonide) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[ULK2]] | C | ULK2 activity raises TRABD2B's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 3.32× lower at baseline in the lines without ULK2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2; co-absent with the target |
| [[HSF2BP]] | C | HSF2BP activity raises TRABD2B's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 3.80× lower at baseline in the lines without HSF2BP | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSAP]] | B | TRABD2B activity raises GSAP's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without TRABD2B | 0.010 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[KTN1-AS1]] | B | TRABD2B activity raises KTN1-AS1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without TRABD2B | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[GABARAP]] | B | TRABD2B activity lowers GABARAP's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.21× higher at baseline in the lines without TRABD2B | 0.061 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[MARVELD1]] | B | TRABD2B activity raises MARVELD1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without TRABD2B | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[RAP1GDS1]] | B | TRABD2B activity raises RAP1GDS1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without TRABD2B | 0.076 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[TEAD4]] | B | TRABD2B activity raises TEAD4's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without TRABD2B | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[ASMTL-AS1]] | B | TRABD2B activity raises ASMTL-AS1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without TRABD2B | 0.083 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[FAXC]] | B | TRABD2B activity raises FAXC's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without TRABD2B | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[PTGFRN]] | B | TRABD2B activity raises PTGFRN's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without TRABD2B | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (32.4, 14.4); signed map (15.9, 22.7). **Vector** length 84.6, 21.3% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.4 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | -0.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.4 | +1.7 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -14.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -14.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TraB domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:47,760,528-47,997,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIKI2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NFA1](https://www.uniprot.org/uniprotkb/A6NFA1) (Metalloprotease TIKI2):

> Metalloprotease that acts as a negative regulator of the Wnt signaling pathway by mediating the cleavage of the 8 N-terminal residues of a subset of Wnt proteins. Following cleavage, Wnt proteins become oxidized and form large disulfide-bond oligomers, leading to their inactivation. Able to cleave WNT3A, WNT5, but not WNT11.

**Summary**, from NCBI Gene [388630](https://www.ncbi.nlm.nih.gov/gene/388630):

> Enables Wnt-protein binding activity and metalloendopeptidase activity. Involved in negative regulation of Wnt signaling pathway; positive regulation of protein-containing complex assembly; and proteolysis. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:44200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44200) · Entrez [388630](https://www.ncbi.nlm.nih.gov/gene/388630) · UniProt [A6NFA1](https://www.uniprot.org/uniprotkb/A6NFA1) · Ensembl [ENSG00000269113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269113)

## Data

Gene col 15614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15614); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15614]; `tensor/DDL_lfc|DDL_z.npy` [15614]; `embed/gene_vectors.npy` [15614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15614 or target_col == 15614). Every well: [[TRABD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRABD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
