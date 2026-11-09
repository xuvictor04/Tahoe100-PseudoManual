---
symbol: "RANBP17"
type: "gene"
col: 12918
ensembl_id: "ENSG00000204764"
name: "RAN binding protein 17"
location: "5q35.1"
module: 36
arm: "+"
pooled_cpm: 107.1
n_lines_expressing: 40
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# RANBP17

*RAN binding protein 17* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.39× (z +4.4, q 0.005, up in 26 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.441× (z -15.6, q 0e+00, down in 36 of 38 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.196× (z -11.5, q 6e-28, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGGT2]] (+0.66, fdr 7e-06), [[DOCK1]] (+0.64, fdr 8e-06), [[SIMC1]] (+0.64, fdr 7e-06); moves opposite to [[BPNT1]] (-0.66, fdr 1e-05), [[ETFRF1]] (-0.55, fdr 3e-05), [[COG4]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[DOCK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 0.005 | 26/38 (NCI-H2347, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.5 | 0.12 | 19/38 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.26× | +3.2 | 0.29 | 19/38 (NCI-H460, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.441×** | -15.6 | 0e+00 | 36/38 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.196×** | -11.5 | 6e-28 | 39/39 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.423×** | -11.1 | 2e-26 | 34/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.332×** | -7.7 | 1e-12 | 31/38 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.595×** | -7.0 | 4e-10 | 30/38 (NCI-H460, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.604×** | -6.8 | 1e-09 | 29/38 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -6.3 | 3e-08 | 23/39 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.664×** | -5.5 | 3e-06 | 26/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -5.5 | 3e-06 | 20/34 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -5.1 | 2e-05 | 24/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.687×** | -5.0 | 2e-05 | 29/38 (SW 900, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -4.4 | 5e-04 | 24/38 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -4.3 | 9e-04 | 21/36 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.721×** | -4.2 | 0.001 | 24/38 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.754×** | -3.8 | 0.006 | 22/38 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.007 | 24/38 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.791×** | -3.1 | 0.058 | 16/38 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.800×** | -3.0 | 0.091 | 18/38 (HEC-1-A, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 225 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -35.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.214× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 202 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -27.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0587× (z -17.0) |
| [[J82 (line)]] | alt | 192 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -22.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.172× (z -9.6) |
| [[A-427 (line)]] | wt | 256 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -19.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.142× (z -13.4) |
| [[A549 (line)]] | wt | 164 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.137× (z -10.2) |
| [[LoVo (line)]] | wt | 193 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -24.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.127× (z -13.3) |
| [[C32 (line)]] | wt | 215 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.268× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 209 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.131× (z -11.7) |
| [[RKO (line)]] | wt | 116 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.146× (z -9.9) |
| [[AN3 CA (line)]] | alt | 521 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.297× (z -8.6) |
| [[HS-578T (line)]] | alt | 158 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -18.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.138× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -19.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 264 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0555× (z -31.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.167× (z -10.5) |
| [[HOP62 (line)]] | alt | 94.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -23.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0919× (z -11.2) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.105× (z -10.1) |
| [[SW 900 (line)]] | alt | 304 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.272× (z -12.2) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.111× (z -10.8) |
| [[SW480 (line)]] | alt | 118 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.194× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 85.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 57.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -30.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.139× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 91.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.268× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 80.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[KATO III (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 109 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.118× (z -9.0) |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.146× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 1271 (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.77 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGGT2]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.64 | +0.68 / +0.58 | both halves | 8e-06 | same gene group |
| [[SIMC1]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TTL]] | +0.63 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MFSD14CP-1]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SPECC1L]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FANCC]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[HERC2]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TTC7B]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.58 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT1]] | -0.66 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.55 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[COG4]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[THAP8]] | -0.53 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[FAM117A]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF490]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZNF44]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[FBXO8]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ECH1]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[PEX13]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK1]] | B | RANBP17 activity raises DOCK1's level | lines that do not express RANBP17 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without RANBP17 | 0.026 | ⚠ within organs, on part of the lines |
| [[FBXO8]] | B | RANBP17 activity raises FBXO8's level | lines that do not express RANBP17 (10) vs lines expressing it (40) | 1.08× lower at baseline in the lines without RANBP17 | 0.055 | ⚠ within organs, on part of the lines |
| [[TMTC4]] | B | RANBP17 activity lowers TMTC4's level | lines that do not express RANBP17 (10) vs lines expressing it (40) | 1.10× higher at baseline in the lines without RANBP17 | 0.064 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-4.3, -34.4); signed map (-17.5, -52.0). **Vector** length 112, 35.5% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.5 | -15.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.5 | -5.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:170,861,870-171,300,015 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2T7](https://www.uniprot.org/uniprotkb/Q9H2T7) (Ran-binding protein 17):

> May function as a nuclear transport receptor.

**Summary**, from NCBI Gene [64901](https://www.ncbi.nlm.nih.gov/gene/64901):

> The transport of protein and large RNAs through the nuclear pore complexes (NPC) is an energy-dependent and regulated process. The import of proteins with a nuclear localization signal (NLS) is accomplished by recognition of one or more clusters of basic amino acids by the importin-alpha/beta complex; see MIM 600685 and MIM 602738. The small GTPase RAN (MIM 601179) plays a key role in NLS-dependent protein import. RAN-binding protein-17 is a member of the importin-beta superfamily of nuclear …

**Accessions** — [HGNC:14428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14428) · Entrez [64901](https://www.ncbi.nlm.nih.gov/gene/64901) · UniProt [Q9H2T7](https://www.uniprot.org/uniprotkb/Q9H2T7) · Ensembl [ENSG00000204764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204764)

## Data

Gene col 12918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12918); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12918]; `tensor/DDL_lfc|DDL_z.npy` [12918]; `embed/gene_vectors.npy` [12918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12918 or target_col == 12918). Every well: [[RANBP17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
