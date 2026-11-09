---
symbol: "IL10RB"
type: "gene"
col: 14367
ensembl_id: "ENSG00000243646"
name: "interleukin 10 receptor subunit beta"
location: "21q22.11"
module: 20
arm: "-"
pooled_cpm: 44.83
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IL10RB

*interleukin 10 receptor subunit beta* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.33× (z +4.0, q 0.037, up in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 2.66×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.391× (z -13.1, q 2e-36, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.442× (z -11.9, q 6e-30, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX2]] (+0.66, fdr 1e-05), [[IFI27L2]] (+0.66, fdr 1e-05), [[MRPS18C]] (+0.64, fdr 1e-05); moves opposite to [[FAM120A]] (-0.66, fdr 7e-06), [[RPSA]] (-0.64, fdr 1e-05), [[HNRNPA3]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 2.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.037 | 24/47 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.46 | 22/47 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.391×** | -13.1 | 2e-36 | 42/47 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -11.9 | 6e-30 | 39/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -10.0 | 3e-21 | 32/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.255×** | -9.8 | 1e-20 | 45/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.256×** | -9.8 | 1e-20 | 38/47 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -9.7 | 3e-20 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.522×** | -8.7 | 2e-16 | 29/39 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -8.0 | 1e-13 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.586×** | -7.8 | 6e-13 | 27/45 (COLO 205, HCT15, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.2 | 4e-08 | 31/48 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -6.0 | 1e-07 | 28/47 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -5.7 | 5e-07 | 30/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -5.4 | 3e-06 | 34/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.690×** | -5.4 | 3e-06 | 27/48 (A549, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -5.0 | 2e-05 | 30/48 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.767×** | -3.8 | 0.004 | 24/48 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.037 | 15/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -2.9 | 0.099 | 19/48 (Hs 766T, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.2 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.239× (z -14.6) |
| [[LoVo (line)]] | wt | 52.7 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -9.0) |
| [[LS 180 (line)]] | wt | 46.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 84.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 53.2 | 0 | 5 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0799× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 44.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.7) |
| [[COLO 205 (line)]] | alt | 82.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.3) |
| [[KATO III (line)]] | alt | 44.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 48.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.0) |
| [[A549 (line)]] | wt | 74.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 50.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 47.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 42.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 55.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.8) |
| [[A-172 (line)]] | wt | 87.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.2) |
| [[H4 (line)]] | wt | 66.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -9.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -9.6) |
| [[PANC-1 (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -10.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.401× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.4) |
| [[SNU-423 (line)]] | alt | 32.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.256× (z -10.9) |
| [[A-427 (line)]] | wt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0901× (z -19.7) |
| [[C32 (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.341× (z -9.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0961× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -11.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -11.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -11.4) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX2]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[IFI27L2]] | +0.66 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[MRPS18C]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[DCP1A]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[SUMO4]] | +0.62 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PIAS4]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[TRAFD1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[NKAP]] | +0.60 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[SIRT6]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TRAPPC5]] | +0.60 | +0.46 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120A]] | -0.66 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[RPSA]] | -0.64 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.64 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.62 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[IPO5]] | -0.60 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[BTBD1]] | -0.59 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[NUDT3]] | -0.58 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[ARHGAP4]] | -0.58 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[SLC38A1]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.56 | -0.43 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A6]] | B | SLC2A6 activity lowers IL10RB's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without SLC2A6 | 0.083 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, -12.3); signed map (-13.3, -3.5). **Vector** length 88.8, 23.5% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | -10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.2 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.8 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | -5.3 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.2 | -13.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 10 receptor subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,266,367-33,311,420 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRF2-4, CDW210B, IL-10R2; previously CRFB4, D21S58, D21S66 |
| Gene groups (HGNC) | CD molecules; Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 5 pathways, smallest: Interleukin-20 family signaling; Other interleukin signaling; Interleukin-10 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08334](https://www.uniprot.org/uniprotkb/Q08334) (Interleukin-10 receptor subunit beta):

> Shared cell surface receptor required for the activation of five class 2 cytokines: IL10, IL22, IL26, IL28, and IFNL1. The IFNLR1/IL10RB dimer is a receptor for the cytokine ligands IFNL2 and IFNL3 and mediates their antiviral activity. The ligand/receptor complex stimulate the activation of the JAK/STAT signaling pathway leading to the expression of IFN-stimulated genes (ISG), which contribute to the antiviral state.

**Summary**, from NCBI Gene [3588](https://www.ncbi.nlm.nih.gov/gene/3588):

> The protein encoded by this gene belongs to the cytokine receptor family. It is an accessory chain essential for the active interleukin 10 receptor complex. Coexpression of this and IL10RA proteins has been shown to be required for IL10-induced signal transduction. This gene and three other interferon receptor genes, IFAR2, IFNAR1, and IFNGR2, form a class II cytokine receptor gene cluster located in a small region on chromosome 21. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5965) · Entrez [3588](https://www.ncbi.nlm.nih.gov/gene/3588) · UniProt [Q08334](https://www.uniprot.org/uniprotkb/Q08334) · Ensembl [ENSG00000243646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243646)

## Data

Gene col 14367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14367); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14367]; `tensor/DDL_lfc|DDL_z.npy` [14367]; `embed/gene_vectors.npy` [14367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14367 or target_col == 14367). Every well: [[IL10RB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL10RB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
