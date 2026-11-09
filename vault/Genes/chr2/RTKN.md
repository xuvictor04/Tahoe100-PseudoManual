---
symbol: "RTKN"
type: "gene"
col: 3610
ensembl_id: "ENSG00000114993"
name: "rhotekin"
location: "2p13.1"
module: 5
arm: "+"
pooled_cpm: 23.41
n_lines_expressing: 45
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RTKN

*rhotekin* — 2p13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 7.03×, AsPC-1 3.36×, HEC-1-A 2.29×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (PANC-1 9.12×, NCI-H1573 3.14×, AsPC-1 4.32×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 3.35×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.612× (z -7.6, q 9e-12, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF443]] (+0.58, fdr 1e-05), [[ZNF799]] (+0.55, fdr 2e-05), [[PLEKHG3]] (+0.54, fdr 2e-05); moves opposite to [[ZCRB1]] (-0.44, fdr 1e-04), [[GABARAPL2]] (-0.42, fdr 2e-04), [[UBE2B]] (-0.42, fdr 6e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PRSS22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 7.03×, AsPC-1 3.36×, HEC-1-A 2.29×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (PANC-1 9.12×, NCI-H1573 3.14×, AsPC-1 4.32×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 3.35×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.083 | 14/40 (NCI-H1573, AsPC-1, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.63 | 5/43 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -7.6 | 9e-12 | 30/43 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -7.6 | 9e-12 | 26/43 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.631×** | -7.2 | 1e-10 | 26/43 (COLO 205, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.679×** | -6.0 | 3e-07 | 20/42 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -5.9 | 5e-07 | 22/40 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -5.8 | 6e-07 | 19/41 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.673×** | -5.6 | 1e-06 | 22/36 (A-427, SW480, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -5.4 | 4e-06 | 21/41 (HT-29, A-427, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.710×** | -5.3 | 6e-06 | 21/41 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.715×** | -5.2 | 1e-05 | 18/41 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -4.7 | 2e-04 | 17/42 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.829×** | -4.1 | 0.002 | 13/42 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.785×** | -3.8 | 0.007 | 17/40 (hTERT-HPNE, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.780×** | -3.7 | 0.008 | 17/38 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.789×** | -3.7 | 0.009 | 16/43 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.021 | 14/41 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.743×** | -3.3 | 0.033 | 9/42 (SW1417, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.054 | 13/41 (HEC-1-A, NCI-H1573, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.064 | 12/41 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.823×** | -3.0 | 0.067 | 16/41 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.076 | 8/43 (hTERT-HPNE, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.90 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.251× (z -9.1) |
| [[PANC-1 (line)]] | alt | 21.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +26.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +11.5) | — |
| [[SW480 (line)]] | alt | 49.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.317× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -8.8) |
| [[A-427 (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 27.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 43.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.14× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.103× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HCT15 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 35.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.252× (z -9.5) |
| [[LoVo (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0885× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 47.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF443]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF799]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHG3]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[PALD1]] | +0.52 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZNF816]] | +0.50 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[FOXP4-AS1]] | +0.50 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[HR]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[ZNF574]] | +0.50 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[SLC5A6]] | +0.48 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[SHH]] | +0.48 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[NACC1]] | +0.47 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[GEMIN4]] | +0.47 | +0.30 / +0.56 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCRB1]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[GABARAPL2]] | -0.42 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[UBE2B]] | -0.42 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[RPS6]] ⚠ | -0.41 | -0.36 / -0.40 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[STAG3L4-1]] | -0.41 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[TBC1D23]] | -0.40 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[UBE2Q2P2]] | -0.40 | -0.21 / -0.46 | both halves | 7e-04 |  |
| [[PNPLA8]] | -0.40 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[OAZ1]] | -0.40 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[TOMM20]] | -0.40 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[CAPN7]] | -0.40 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[NSA2]] | -0.39 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[ECT2L]] | -0.39 | -0.28 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS22]] | B | PRSS22 activity raises RTKN's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without PRSS22 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[SLC52A3]] | B | SLC52A3 activity raises RTKN's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without SLC52A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[LAD1]] | B | LAD1 activity raises RTKN's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without LAD1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[BAIAP2L2]] | B | BAIAP2L2 activity raises RTKN's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without BAIAP2L2 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC52A3]] | B | SLC52A3 activity strengthens RTKN's drug response | lines that do not express SLC52A3 (24) vs lines expressing it (19) | the lines without SLC52A3 respond 0.83× as strongly (z diff +0.14); strongest at Dinaciclib 0.5 µM: 0.82x vs 0.49x (z diff +3.8) | 0.076 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.302). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.7, -41.6); signed map (21.9, -45.9). **Vector** length 78.4, 15.8% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.4 | -1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.9 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | rhotekin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,425,835-74,442,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B5, RTKN-1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 8 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; RHOB GTPase cycle; RHOC GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BST9](https://www.uniprot.org/uniprotkb/Q9BST9) (Rhotekin):

> Mediates Rho signaling to activate NF-kappa-B and may confer increased resistance to apoptosis to cells in gastric tumorigenesis. May play a novel role in the organization of septin structures.

**Summary**, from NCBI Gene [6242](https://www.ncbi.nlm.nih.gov/gene/6242):

> This gene encodes a scaffold protein that interacts with GTP-bound Rho proteins. Binding of this protein inhibits the GTPase activity of Rho proteins. This protein may interfere with the conversion of active, GTP-bound Rho to the inactive GDP-bound form by RhoGAP. Rho proteins regulate many important cellular processes, including cytokinesis, transcription, smooth muscle contraction, cell growth and transformation. Dysregulation of the Rho signal transduction pathway has been implicated in many …

**Accessions** — [HGNC:10466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10466) · Entrez [6242](https://www.ncbi.nlm.nih.gov/gene/6242) · UniProt [Q9BST9](https://www.uniprot.org/uniprotkb/Q9BST9) · Ensembl [ENSG00000114993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114993)

## Data

Gene col 3610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3610); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3610]; `tensor/DDL_lfc|DDL_z.npy` [3610]; `embed/gene_vectors.npy` [3610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3610 or target_col == 3610). Every well: [[RTKN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTKN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
