---
symbol: "MTX2"
type: "gene"
col: 4909
ensembl_id: "ENSG00000128654"
name: "metaxin 2"
location: "2q31.1"
module: 65
arm: "+"
pooled_cpm: 87.21
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# MTX2

*metaxin 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.28× (z +6.7, q 1e-08, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.17× (z +4.2, q 0.004, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.425× (z -15.5, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.652× (z -8.1, q 9e-14, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMC1]] (+0.84, fdr 7e-06), [[ANAPC4]] (+0.78, fdr 7e-06), [[FIP1L1]] (+0.74, fdr 7e-06); moves opposite to [[CYTH2]] (-0.63, fdr 1e-05), [[FER1L4]] (-0.60, fdr 9e-06), [[KPNA4]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.28×** | +6.7 | 1e-08 | 33/48 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +5.3 | 3e-05 | 26/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.004 | 18/48 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.004 | 32/49 (SNU-423, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.7 | 0.023 | 23/48 (COLO 205, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.425×** | -15.5 | 0e+00 | 40/44 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.477×** | -12.9 | 1e-35 | 41/45 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.506×** | -12.8 | 2e-35 | 47/49 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.676×** | -10.4 | 4e-23 | 37/48 (SNU-423, NCI-H1792, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -8.1 | 9e-14 | 41/48 (SW480, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.654×** | -8.0 | 1e-13 | 31/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -7.8 | 7e-13 | 38/49 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.666×** | -7.6 | 2e-12 | 28/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -7.6 | 3e-12 | 40/49 (J82, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -6.4 | 1e-08 | 34/48 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.749×** | -5.4 | 3e-06 | 32/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.754×** | -5.3 | 5e-06 | 26/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.760×** | -5.0 | 3e-05 | 27/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -4.1 | 0.001 | 27/48 (SW48, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **0.821×** | -3.7 | 0.008 | 25/48 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.019 | 21/48 (SNU-1, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 101 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -17.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 102 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -16.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 63.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.246× (z -8.6) |
| [[SW1417 (line)]] | alt | 89.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -13.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 112 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.370× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 76.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 100 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -18.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 88.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 99.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -15.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 89.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.142× (z -9.0) |
| [[HCT15 (line)]] | alt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 66.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -12.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 96.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.447× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -23.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 98.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -21.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 58.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -21.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 78.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.1) |
| [[A498 (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A549 (line)]] | wt | 91.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 86.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.410× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 62.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 81.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 79.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 89.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -12.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 69.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[hTERT-HPNE (line)]] | wt | 56.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H1792 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -18.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 86.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 86.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMC1]] | +0.84 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ANAPC4]] | +0.78 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[FIP1L1]] | +0.74 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[MRPL39]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[LRIG2]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TUBE1]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[TADA1]] | +0.65 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ALG9]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MRS2]] | +0.64 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NDUFV2]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 465 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[FER1L4]] | -0.60 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[KPNA4]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[PPP1R10]] | -0.56 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[DMPK]] | -0.56 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[SYS1-DBNDD2]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TUT7]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[DDX5]] | -0.54 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[NID1]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CSNK1A1]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.53 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SP2]] | -0.53 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.2, -9.9); signed map (-30.3, -13.1). **Vector** length 110, 32.6% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +8.2 | +6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -12.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.8 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -8.1 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | metaxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:176,269,395-176,338,025 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Metaxins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Cristae formation; Mitochondrial protein import; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75431](https://www.uniprot.org/uniprotkb/O75431) (Metaxin-2):

> Involved in transport of proteins into the mitochondrion.

**Summary**, from NCBI Gene [10651](https://www.ncbi.nlm.nih.gov/gene/10651):

> The protein encoded by this gene is highly similar to the metaxin 2 protein from mouse, which has been shown to interact with the mitochondrial membrane protein metaxin 1. Because of this similarity, it is thought that the encoded protein is peripherally associated with the cytosolic face of the outer mitochondrial membrane, and that it is involved in the import of proteins into the mitochondrion. Alternative splicing results in multiple transcript variants. A related pseudogene has been …

**Accessions** — [HGNC:7506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7506) · Entrez [10651](https://www.ncbi.nlm.nih.gov/gene/10651) · UniProt [O75431](https://www.uniprot.org/uniprotkb/O75431) · Ensembl [ENSG00000128654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128654)

## Data

Gene col 4909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4909); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4909]; `tensor/DDL_lfc|DDL_z.npy` [4909]; `embed/gene_vectors.npy` [4909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4909 or target_col == 4909). Every well: [[MTX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
