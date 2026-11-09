---
symbol: "RAI1"
type: "gene"
col: 2965
ensembl_id: "ENSG00000108557"
name: "retinoic acid induced 1"
location: "17p11.2"
module: 5
arm: "+"
pooled_cpm: 92.74
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RAI1

*retinoic acid induced 1* — 17p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 2.76×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.272× (z -23.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP5]] (+0.60, fdr 7e-06), [[GSE1]] (+0.58, fdr 2e-05), [[SMAD6]] (+0.55, fdr 4e-05); moves opposite to [[DYNC1I2]] (-0.57, fdr 4e-05), [[KIFAP3]] (-0.52, fdr 3e-05), [[ZMYM6]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2965.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 2.76×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Posaconazole (drug)]] 5 µM |  | 1.23× | +3.4 | 0.36 | 19/48 (CFPAC-1, SW1417, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.272×** | -23.3 | 0e+00 | 48/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.280×** | -22.8 | 0e+00 | 48/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.379×** | -17.4 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -14.4 | 1e-44 | 39/48 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.454×** | -13.1 | 2e-37 | 34/44 (Panc 03.27, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.510×** | -12.0 | 3e-31 | 42/49 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -10.8 | 2e-25 | 41/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.548×** | -9.9 | 2e-21 | 35/45 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -6.7 | 2e-09 | 31/47 (MIA PaCa-2, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -6.5 | 5e-09 | 34/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.677×** | -6.5 | 5e-09 | 33/48 (C32, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.680×** | -6.4 | 7e-09 | 33/50 (C32, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.797×** | -5.7 | 5e-07 | 29/49 (PANC-1, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -5.6 | 1e-06 | 28/48 (C32, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.814×** | -5.2 | 9e-06 | 26/48 (C32, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -5.1 | 1e-05 | 30/49 (NCI-H23, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -5.0 | 2e-05 | 27/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.782×** | -4.4 | 4e-04 | 27/48 (LS 180, LOX-IMVI, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -3.7 | 0.006 | 26/48 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.023 | 18/48 (Panc 03.27, CFPAC-1, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.023 | 23/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.025 | 19/47 (BT-474, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 296 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -24.3) |
| [[PANC-1 (line)]] | alt | 148 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -23.6) |
| [[MIA PaCa-2 (line)]] | alt | 88.7 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -19.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -16.3) |
| [[A-172 (line)]] | wt | 74.6 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.231× (z -16.1) |
| [[A498 (line)]] | wt | 122 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 82.8 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0700× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.234× (z -13.3) |
| [[J82 (line)]] | alt | 65.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.5) |
| [[C-33 A (line)]] | alt | 188 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -23.2) |
| [[Hs 766T (line)]] | wt | 107 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -13.7) |
| [[HT-29 (line)]] | alt | 126 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 65.0 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.3) |
| [[RKO (line)]] | wt | 88.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -14.1) |
| [[SW1417 (line)]] | alt | 59.8 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -12.4) |
| [[A-427 (line)]] | wt | 64.0 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.185× (z -17.1) |
| [[BT-474 (line)]] | alt | 135 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -16.9) |
| [[CHP-212 (line)]] | wt | 117 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.157× (z -11.3) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.247× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -20.4) |
| [[HOP62 (line)]] | alt | 113 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -14.7) |
| [[LS 180 (line)]] | wt | 157 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -19.3) |
| [[SNU-423 (line)]] | alt | 54.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.1) |
| [[SW480 (line)]] | alt | 85.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 54.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.1) |
| [[KATO III (line)]] | alt | 162 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -15.2) |
| [[LoVo (line)]] | wt | 71.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 42.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 59.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 61.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -13.8) |
| [[SHP-77 (line)]] | alt | 203 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -11.3) |
| [[SW48 (line)]] | wt | 119 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -14.8) |
| [[A549 (line)]] | wt | 74.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -10.0) |
| [[AN3 CA (line)]] | alt | 112 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 58.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.3) |
| [[HS-578T (line)]] | alt | 59.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 52.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 36.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -9.9) |
| [[SW 900 (line)]] | alt | 156 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.5) |
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.8) |
| [[H4 (line)]] | wt | 65.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 142 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 43.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.353× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 58.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -8.6) |
| [[SNU-1 (line)]] | wt | 81.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2122 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP5]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GSE1]] | +0.58 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SMAD6]] | +0.55 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[MIRLET7BHG]] | +0.53 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[RXRA]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 | pathway: Circadian clock |
| [[FAM53B]] ⚠ | +0.51 | +0.41 / +0.43 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RCC2]] | +0.51 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[MACROD1]] | +0.50 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[PTPA]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[KMT2D]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 | same gene group |
| [[PRDM15]] | +0.49 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[PATZ1]] | +0.49 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[ABCC1]] | +0.48 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1I2]] | -0.57 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[KIFAP3]] | -0.52 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZMYM6]] | -0.48 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[FAM149B1]] | -0.48 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TBC1D23]] | -0.48 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[STAM2]] | -0.47 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ACTR10]] | -0.47 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[FAM114A2]] | -0.45 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[CDKL5]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RGS9]] | -0.44 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[CSGALNACT2]] | -0.44 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[ABI1]] | -0.43 | -0.21 / -0.42 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises RAI1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.40× lower at baseline in the lines without WNK2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (20.5, -2.6); signed map (29.2, -36.9). **Vector** length 92.1, 26.4% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.0 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | -0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +0.6 |
|  | [[Artesunate (drug)]] 0.05 µM |  | +1.8 | +2.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | retinoic acid induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,681,458-17,811,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434A139, SMS, KIAA1820, MGC12824; previously SMCR |
| Gene groups (HGNC) | PHD finger proteins; TCF20 family |
| Reactome | 5 pathways, smallest: Expression of BMAL (ARNTL), CLOCK, and NPAS2; Heme signaling; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5J4](https://www.uniprot.org/uniprotkb/Q7Z5J4) (Retinoic acid-induced protein 1):

> Transcriptional regulator of the circadian clock components: CLOCK, BMAL1, BMAL2, PER1/3, CRY1/2, NR1D1/2 and RORA/C. Positively regulates the transcriptional activity of CLOCK a core component of the circadian clock. Regulates transcription through chromatin remodeling by interacting with other proteins in chromatin as well as proteins in the basic transcriptional machinery. May be important for embryonic and postnatal development. May be involved in neuronal differentiation.

**Summary**, from NCBI Gene [10743](https://www.ncbi.nlm.nih.gov/gene/10743):

> This gene is located within the Smith-Magenis syndrome region on chromosome 17. It is highly similar to its mouse counterpart and is expressed at high levels mainly in neuronal tissues. The protein encoded by this gene includes a polymorphic polyglutamine tract in the N-terminal domain. Expression of the mouse counterpart in neurons is induced by retinoic acid. This gene is associated with both the severity of the phenotype and the response to medication in schizophrenic patients. [provided by …

**Accessions** — [HGNC:9834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9834) · Entrez [10743](https://www.ncbi.nlm.nih.gov/gene/10743) · UniProt [Q7Z5J4](https://www.uniprot.org/uniprotkb/Q7Z5J4) · Ensembl [ENSG00000108557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108557)

## Data

Gene col 2965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2965); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2965]; `tensor/DDL_lfc|DDL_z.npy` [2965]; `embed/gene_vectors.npy` [2965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2965 or target_col == 2965). Every well: [[RAI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
