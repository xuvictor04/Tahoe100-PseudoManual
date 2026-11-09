---
symbol: "IREB2"
type: "gene"
col: 5859
ensembl_id: "ENSG00000136381"
name: "iron responsive element binding protein 2"
location: "15q25.1"
module: 89
arm: "+"
pooled_cpm: 92.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# IREB2

*iron responsive element binding protein 2* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.30× (z +7.3, q 1e-10, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (HT-29 1.66×; ⚠ cell-cycle shift, explains ~60% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -14.3, q 1e-43, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.432× (z -8.6, q 1e-15, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3F]] (+0.70, fdr 7e-06), [[RCC1L]] (+0.68, fdr 1e-05), [[PPP1R8]] (+0.67, fdr 7e-06); moves opposite to [[FOXO6]] (-0.60, fdr 2e-05), [[USP2]] (-0.54, fdr 4e-05), [[JUNB]] (-0.53, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5859.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (HT-29 1.66×; ⚠ cell-cycle shift, explains ~60% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.30×** | +7.3 | 1e-10 | 35/48 (HT-29, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +4.3 | 0.004 | 29/48 (A-172, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.23×** | +4.1 | 0.006 | 26/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.21×** | +3.6 | 0.046 | 20/48 (A-172, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -14.3 | 1e-43 | 40/44 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.497×** | -13.6 | 1e-39 | 44/49 (C-33 A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.523×** | -12.1 | 1e-31 | 47/47 (COLO 205, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.592×** | -10.2 | 3e-22 | 39/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.617×** | -9.0 | 2e-17 | 32/48 (SNU-1, LS 180, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -8.6 | 1e-15 | 41/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.691×** | -7.2 | 6e-11 | 29/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.719×** | -6.4 | 1e-08 | 34/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.719×** | -6.4 | 1e-08 | 33/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.704×** | -6.3 | 2e-08 | 26/45 (C32, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -5.3 | 7e-06 | 25/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.789×** | -4.6 | 2e-04 | 28/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.801×** | -4.3 | 8e-04 | 29/48 (SW 1088, SW1417, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -4.1 | 0.002 | 26/48 (NCI-H2030, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.834× | -3.5 | 0.017 | 21/48 (NCI-H460, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 114 | 0 | 10 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.417× (z -13.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HOP62 (line)]] | alt | 70.4 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 100 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.282× (z -9.7) |
| [[AN3 CA (line)]] | alt | 109 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0871× (z -15.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 127 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 88.5 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.393× (z -11.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 96.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 106 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -18.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.281× (z -8.8) |
| [[LoVo (line)]] | wt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 82.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 97.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -29.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 99.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 63.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.318× (z -11.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 99.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.203× (z -15.9) ⚠ toxic |
| [[H4 (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 90.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -14.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.66× (z +9.2) ⚠ cell-cycle shift, explains ~60% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.508× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 70.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 72.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 66.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.359× (z -10.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 71.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 86.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.477× (z -8.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.472× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 92.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 83.5 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0825× (z -9.2) |
| [[SW 1271 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0909× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3F]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RCC1L]] | +0.68 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R8]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[UQCC1]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[PRR14L]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NSUN3]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PSMB5]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GPATCH2]] | +0.60 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[RPAP1]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MTG2]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[TIRAP]] | +0.58 | +0.60 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO6]] | -0.60 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[USP2]] | -0.54 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[JUNB]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[AFDN]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[HMGN3]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[STARD5]] | -0.51 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[ADGRB2]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GRHL1]] | -0.50 | -0.19 / -0.58 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NR4A1]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[TMOD2]] | -0.50 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[CD83]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ATP1A3]] | -0.50 | -0.20 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[BCAM]] | -0.49 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[C12orf75]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers IREB2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.0, 18.0); signed map (-7.7, -17.6). **Vector** length 103, 28.4% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +7.5 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.4 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | +7.2 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.2 | -14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -8.1 | -13.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.3 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -6.4 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | iron responsive element binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,437,431-78,501,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IRP2 |
| Reactome | 2 pathways, smallest: Iron uptake and transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P48200](https://www.uniprot.org/uniprotkb/P48200) (Iron-responsive element-binding protein 2):

> RNA-binding protein that binds to iron-responsive elements (IRES), which are stem-loop structures found in the 5'-UTR of ferritin, and delta aminolevulinic acid synthase mRNAs, and in the 3'-UTR of transferrin receptor mRNA. Binding to the IRE element in ferritin results in the repression of its mRNA translation. Binding of the protein to the transferrin receptor mRNA inhibits the degradation of this otherwise rapidly degraded mRNA.

**Summary**, from NCBI Gene [3658](https://www.ncbi.nlm.nih.gov/gene/3658):

> The protein encoded by this gene is an RNA-binding protein that acts to regulate iron levels in the cells by regulating the translation and stability of mRNAs that affect iron homeostasis under conditions when iron is depleted. When iron levels are low, this protein binds to iron-responsive elements (IRES), stem-loop structures located either in the 5' or 3' UTRs. Binding to the 5' UTR represses translation, while binding to the 3' UTR inhibits mRNA degradation. When iron is found in the cell, …

**Accessions** — [HGNC:6115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6115) · Entrez [3658](https://www.ncbi.nlm.nih.gov/gene/3658) · UniProt [P48200](https://www.uniprot.org/uniprotkb/P48200) · Ensembl [ENSG00000136381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136381)

## Data

Gene col 5859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5859); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5859]; `tensor/DDL_lfc|DDL_z.npy` [5859]; `embed/gene_vectors.npy` [5859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5859 or target_col == 5859). Every well: [[IREB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IREB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
