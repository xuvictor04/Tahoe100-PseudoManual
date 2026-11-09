---
symbol: "AP1G2"
type: "gene"
col: 13157
ensembl_id: "ENSG00000213983"
name: "adaptor related protein complex 1 subunit gamma 2"
location: "14q11.2"
module: 96
arm: "+"
pooled_cpm: 16.44
n_lines_expressing: 42
n_dd_up: 1
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 14
direction_downstream: 11
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# AP1G2

*adaptor related protein complex 1 subunit gamma 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.26× (z +4.1, q 0.023, up in 17 of 40 measured lines) ⚠ cell-cycle shift, explains ~91% of this change.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.477× (z -12.9, q 5e-35, down in 34 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPIN3]] (+0.66, fdr 7e-06), [[DMTN]] (+0.64, fdr 9e-06), [[PRR36]] (+0.64, fdr 7e-06); moves opposite to [[TSHZ3]] (-0.53, fdr 3e-05), [[SLC2A13]] (-0.48, fdr 8e-05), [[CCM2]] (-0.48, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[RORC]] → it (grade B ⚠); 11 go from it, the strongest it → [[PICK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.26×** | +4.1 | 0.023 | 17/40 (LoVo, MIA PaCa-2, …) | rises with dose | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.40× | +3.5 | 0.14 | 14/38 (LoVo, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.477×** | -12.9 | 5e-35 | 34/38 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.401×** | -11.2 | 1e-26 | 33/38 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.410×** | -10.9 | 2e-25 | 36/39 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.536×** | -10.8 | 5e-25 | 30/40 (MIA PaCa-2, NCI-H2347, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.433×** | -10.3 | 1e-22 | 32/39 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.437×** | -10.2 | 3e-22 | 35/40 (HCT15, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.441×** | -10.1 | 7e-22 | 33/39 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.457×** | -9.6 | 5e-20 | 35/39 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.479×** | -9.0 | 1e-17 | 30/39 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.507×** | -8.3 | 5e-15 | 31/37 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.487×** | -7.4 | 6e-12 | 29/39 (COLO 205, SK-MEL-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -7.4 | 7e-12 | 25/39 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.573×** | -6.8 | 4e-10 | 26/38 (SW480, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -6.0 | 1e-07 | 23/39 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -5.7 | 4e-07 | 25/40 (SW 900, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -4.5 | 3e-04 | 18/37 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.7 | 0.005 | 17/39 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.765×** | -3.3 | 0.027 | 9/39 (SW1417, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.755×** | -3.2 | 0.029 | 18/38 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.604×** | -3.2 | 0.029 | 11/40 (CFPAC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.771×** | -3.0 | 0.061 | 7/40 (SW 1088, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.841× | -3.0 | 0.062 | 4/40 (J82, SNU-423, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -3.0 | 0.066 | 13/39 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.760×** | -2.8 | 0.088 | 9/39 (SW48, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 39.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.9) |
| [[SW480 (line)]] | alt | 31.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -10.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.7) |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -17.1) |
| [[HOP62 (line)]] | alt | 10.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -11.3) |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -14.2) |
| [[KATO III (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 34.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.279× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.1) |
| [[SW48 (line)]] | wt | 18.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.3) |
| [[A-427 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0945× (z -11.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -8.6) |
| [[LoVo (line)]] | wt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 9.51 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.7) |
| [[RKO (line)]] | wt | 6.95 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0775× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -14.2) |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.5) |
| [[A-172 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPIN3]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[DMTN]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[PRR36]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PIGO]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[PRSS16]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[WDR6]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.54 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[NEIL1]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[MED16]] | +0.53 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TMEM184A]] | +0.53 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[DCTN1]] | +0.53 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PICK1]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSHZ3]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SLC2A13]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[CCM2]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[DNAAF9]] | -0.47 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[PRR16]] | -0.47 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[LRRC8C]] | -0.47 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[RABGEF1P1]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[MRPL36]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TUBB6]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[IQCJ-SCHIP1]] | -0.45 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[SPCS1]] | -0.45 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[HS3ST3A1]] | -0.45 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RORC]] | B | RORC activity raises AP1G2's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without RORC | 0.003 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[ERBB3]] | B | ERBB3 activity raises AP1G2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without ERBB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[OCLN]] | B | OCLN activity raises AP1G2's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without OCLN | 0.014 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[SCNN1A]] | B | SCNN1A activity raises AP1G2's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without SCNN1A | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[TESMIN]] | B | TESMIN activity raises AP1G2's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without TESMIN | 0.037 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[FRK]] | B | FRK activity raises AP1G2's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without FRK | 0.057 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[DMTN]] | B | DMTN activity raises AP1G2's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without DMTN | 0.065 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[MUC1]] | B | MUC1 activity raises AP1G2's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without MUC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[RORC]] | B | RORC activity strengthens AP1G2's drug response | lines that do not express RORC (23) vs lines expressing it (17) | the lines without RORC respond 0.70× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 0.57x vs 0.41x (z diff +3.4) | 0.081 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; target measured in part of the lines; artifact flags |
| [[CST6]] | B | CST6 activity raises AP1G2's level | lines that do not express CST6 (42) vs lines expressing it (8) | 2.24× lower at baseline in the lines without CST6 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[EPS8L3]] | B | EPS8L3 activity raises AP1G2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.18× lower at baseline in the lines without EPS8L3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[CD24]] | B | CD24 activity raises AP1G2's level | lines that do not express CD24 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without CD24 | 0.097 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PICK1]] | B | AP1G2 activity raises PICK1's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 2.46× lower at baseline in the lines without AP1G2 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[BCL2L11]] | B | AP1G2 activity raises BCL2L11's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without AP1G2 | 0.040 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[KIAA1549L]] | B | AP1G2 activity lowers KIAA1549L's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 3.40× higher at baseline in the lines without AP1G2 | 0.041 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[OCLN]] | B | AP1G2 activity raises OCLN's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 5.35× lower at baseline in the lines without AP1G2 | 0.053 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[MIR3936HG]] | B | AP1G2 activity raises MIR3936HG's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without AP1G2 | 0.070 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[FRK]] | B | AP1G2 activity raises FRK's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 4.27× lower at baseline in the lines without AP1G2 | 0.071 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[TESMIN]] | B | AP1G2 activity raises TESMIN's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without AP1G2 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[ERBB3]] | B | AP1G2 activity raises ERBB3's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 3.98× lower at baseline in the lines without AP1G2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[HS3ST3A1]] | B | AP1G2 activity lowers HS3ST3A1's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 5.17× higher at baseline in the lines without AP1G2 | 0.082 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[LRRC8C]] | B | AP1G2 activity lowers LRRC8C's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 2.19× higher at baseline in the lines without AP1G2 | 0.093 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[CCDC120]] | C | AP1G2 activity raises CCDC120's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 3.17× lower at baseline in the lines without AP1G2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.5, 31.4); signed map (-5.0, 17.6). **Vector** length 73.1, 15.3% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +4.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -12.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.1 | -11.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.1 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.8 | -6.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,559,565-23,568,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G2AD |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 1 |
| Reactome | 4 pathways, smallest: Lysosome Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O75843](https://www.uniprot.org/uniprotkb/O75843) (AP-1 complex subunit gamma-like 2):

> May function in protein sorting in late endosomes or multivesucular bodies (MVBs).; (Microbial infection) Involved in MVB-assisted maturation of hepatitis B virus (HBV).

**Summary**, from NCBI Gene [8906](https://www.ncbi.nlm.nih.gov/gene/8906):

> Adaptins are important components of clathrin-coated vesicles transporting ligand-receptor complexes from the plasma membrane or from the trans-Golgi network to lysosomes. The adaptin family of proteins is composed of four classes of molecules named alpha, beta-, beta prime- and gamma- adaptins. Adaptins, together with medium and small subunits, form a heterotetrameric complex called an adaptor, whose role is to promote the formation of clathrin-coated pits and vesicles. The protein encoded by …

**Accessions** — [HGNC:556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:556) · Entrez [8906](https://www.ncbi.nlm.nih.gov/gene/8906) · UniProt [O75843](https://www.uniprot.org/uniprotkb/O75843) · Ensembl [ENSG00000213983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213983)

## Data

Gene col 13157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13157); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13157]; `tensor/DDL_lfc|DDL_z.npy` [13157]; `embed/gene_vectors.npy` [13157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13157 or target_col == 13157). Every well: [[AP1G2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1G2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
