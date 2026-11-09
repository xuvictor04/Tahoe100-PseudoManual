---
symbol: "SRGAP2D"
type: "gene"
col: 15674
ensembl_id: "ENSG00000270872"
name: "SLIT-ROBO Rho GTPase activating protein 2D (pseudogene)"
location: "1q21.1"
module: 16
arm: "-"
pooled_cpm: 8.5
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SRGAP2D

*SLIT-ROBO Rho GTPase activating protein 2D (pseudogene)* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +8.2, q 1e-13, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.445× (z -10.6, q 3e-23, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP2B]] (+0.74, fdr 7e-06), [[MAP3K3]] (+0.72, fdr 7e-06), [[CMC2]] (+0.72, fdr 7e-06); moves opposite to [[ZXDB]] (-0.63, fdr 1e-05), [[KICS2]] (-0.63, fdr 1e-05), [[SYNE1]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.2 | 1e-13 | 23/35 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +8.1 | 1e-13 | 29/39 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +7.3 | 7e-11 | 21/33 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +6.9 | 6e-10 | 24/38 (CFPAC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +6.7 | 2e-09 | 26/39 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.3 | 3e-08 | 22/39 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.9 | 3e-07 | 18/34 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 11/38 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.014 | 4/32 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.021 | 7/38 (NCI-H2347, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.069 | 7/37 (A549, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.079 | 7/37 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.445×** | -10.6 | 3e-23 | 26/35 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.446×** | -10.1 | 1e-21 | 27/38 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.606×** | -9.2 | 6e-18 | 24/37 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.502×** | -9.0 | 4e-17 | 25/38 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.513×** | -8.7 | 4e-16 | 21/27 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.625×** | -6.1 | 9e-08 | 22/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.604×** | -6.1 | 1e-07 | 15/20 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.734×** | -5.7 | 1e-06 | 24/39 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -5.5 | 2e-06 | 18/37 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -5.2 | 1e-05 | 20/39 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -4.8 | 7e-05 | 11/16 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.692×** | -4.8 | 8e-05 | 17/37 (H4, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -4.8 | 8e-05 | 17/37 (C32, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -4.6 | 1e-04 | 13/39 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.708×** | -4.1 | 0.001 | 15/32 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.011 | 10/38 (SNU-423, A549, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **0.742×** | -3.6 | 0.012 | 11/33 (A549, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.612×** | -3.3 | 0.027 | 14/38 (A-172, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.4 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.211× (z -10.2) |
| [[A549 (line)]] | wt | 9.74 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.0) |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -11.4) |
| [[A-427 (line)]] | wt | 23.3 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.164× (z -12.4) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.6) |
| [[A498 (line)]] | wt | 7.35 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0777× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0518× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.71 | 0 | 2 (1 ⚠) | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.101× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -12.8) |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -16.4) |
| [[C32 (line)]] | wt | 9.99 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.108× (z -9.6) |
| [[H4 (line)]] | wt | 9.63 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.0841× (z -8.6) |
| [[Hs 766T (line)]] | wt | 5.59 | 0 | 1 | — | [[ERK5-IN-2 (drug)]] 0.05 µM 0.0592× (z -9.9) |
| [[HS-578T (line)]] | alt | 9.29 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0594× (z -13.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0784× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.269× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 5.52 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.110× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 7.23 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.290× (z -9.0) |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.235× (z -12.0) |
| [[SW1417 (line)]] | alt | 7.91 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2B]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[CMC2]] | +0.72 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SRGAP2C]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[POC1A]] | +0.66 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TUBD1]] | +0.64 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[CSNK1G2]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TAF5]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ANKRD13D]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[UBE2D2]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.63 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[KICS2]] | -0.63 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SYNE1]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ANKEF1]] | -0.62 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[USP40]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PARP3]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[POLR2M]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.61 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF252P-1]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[TCTN1]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CFL2]] | -0.59 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ZNF260]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.6, -50.5); signed map (-43.4, 1.3). **Vector** length 74.4, 14.2% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.4 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | SLIT-ROBO Rho GTPase activating protein 2D (pseudogene) |
| Locus type | pseudogene |
| Location | 1q21.1 — chr1:143,975,087-144,068,350 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100996712](https://www.ncbi.nlm.nih.gov/gene/100996712):

> This locus encodes a member of the SLIT-ROBO Rho GTPase activating protein family. This human-specific locus resulted from segmental duplication of the SLIT-ROBO Rho GTPase activating protein 2B locus. This duplicated locus lacks an internal exon, and thus this gene copy may not be functional. Expression of this locus appears to be much lower than the similar SLIT-ROBO Rho GTPase activating protein 2C (SRGAP2C) locus. The SRGAP2C locus has been shown to encode a protein that functions …

**Accessions** — [HGNC:43932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43932) · Entrez [100996712](https://www.ncbi.nlm.nih.gov/gene/100996712) · Ensembl [ENSG00000270872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270872)

## Data

Gene col 15674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15674); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15674]; `tensor/DDL_lfc|DDL_z.npy` [15674]; `embed/gene_vectors.npy` [15674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15674 or target_col == 15674). Every well: [[SRGAP2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGAP2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
