---
symbol: "TLR1"
type: "gene"
col: 10462
ensembl_id: "ENSG00000174125"
name: "toll like receptor 1"
location: "4p14"
module: 117
arm: "+"
pooled_cpm: 6.67
n_lines_expressing: 35
n_dd_up: 15
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 21
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TLR1

*toll like receptor 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +7.4, q 7e-11, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.394× (z -9.7, q 2e-19, down in 21 of 32 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 0.5 µM: 0.678× (z -4.1, q 0.003, down in 15 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLR6]] (+0.90, fdr 7e-06, ⚠ same locus), [[CAPS2]] (+0.70, fdr 1e-05), [[EGF]] (+0.63, fdr 1e-05), [[LINC02328]] (+0.63, fdr 1e-05); moves opposite to [[NPHP4]] (-0.57, fdr 3e-05), [[TBC1D16]] (-0.57, fdr 4e-05), [[ZDHHC9]] (-0.56, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); 21 go from it, the strongest it → [[MOB3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +7.4 | 7e-11 | 17/30 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +6.6 | 1e-08 | 19/32 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.4 | 1e-05 | 14/30 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +5.1 | 6e-05 | 16/32 (A498, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.0 | 7e-05 | 12/31 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +4.9 | 8e-05 | 13/32 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.58×** | +4.5 | 7e-04 | 12/31 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +4.4 | 9e-04 | 11/31 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.001 | 11/32 (C32, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.34×** | +4.3 | 0.001 | 10/32 (AsPC-1, A-172, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.007 | 12/32 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.013 | 6/33 (C32, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.016 | 7/32 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.046 | 6/33 (A498, A-172, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.051 | 8/32 (RPMI-7951, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.394×** | -9.7 | 2e-19 | 21/32 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.472×** | -7.8 | 1e-12 | 19/32 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.524×** | -6.7 | 3e-09 | 16/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.562×** | -5.8 | 1e-06 | 18/30 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.591×** | -5.5 | 5e-06 | 18/32 (NCI-H1573, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.618×** | -5.0 | 5e-05 | 14/31 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.654×** | -4.4 | 8e-04 | 12/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.678×** | -4.1 | 0.003 | 15/32 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.674×** | -4.0 | 0.005 | 15/32 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.692×** | -3.8 | 0.007 | 13/30 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.777×** | -3.7 | 0.010 | 12/33 (NCI-H1792, CHP-212, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.702×** | -3.7 | 0.011 | 14/32 (SNU-423, H4, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.729×** | -3.3 | 0.042 | 13/30 (H4, PANC-1, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.057 | 9/32 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.739×** | -3.2 | 0.060 | 6/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.742×** | -3.1 | 0.064 | 9/32 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.064 | 12/32 (A498, SK-MEL-2, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.675×** | -2.9 | 0.096 | 8/29 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.749×** | -2.9 | 0.096 | 8/33 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.758×** | -2.9 | 0.096 | 12/31 (RPMI-7951, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -17.0) |
| [[RKO (line)]] | wt | 12.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +15.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.4) ⚠ cell-cycle shift, explains ~96% of this change |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Darinaparsin (drug)]] 0.5 µM 0.0697× (z -8.7) |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0315× (z -14.4) |
| [[A-172 (line)]] | wt | 7.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.108× (z -10.4) |
| [[C32 (line)]] | wt | 5.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 4.25 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0725× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 2.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 9.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.80 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0612× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0748× (z -8.5) |
| [[A-427 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.627 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR6]] | +0.90 | +0.91 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CAPS2]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[EGF]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LINC02328]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[DOCK10]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[LRP1B]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CARD6]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ABCC9]] | +0.59 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[ALOX12P2-1]] | +0.59 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[SLAMF7]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 | same gene group |
| [[FYB1]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 418 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TBC1D16]] | -0.57 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZDHHC9]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[CTXN1]] | -0.55 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[SNX25]] | -0.54 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SH2B2]] | -0.53 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[MLXIP]] | -0.53 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ERGIC1]] | -0.52 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[WDR5]] | -0.52 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[ZHX3]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PACSIN2]] | -0.52 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[CYTH3]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity weakens TLR1's drug response | lines that do not express NMRAL2P-1 (10) vs lines expressing it (22) | the lines without NMRAL2P-1 respond 1.03× as strongly (z diff -0.09); strongest at Homoharringtonine 5 µM: 5.05x vs 1.21x (z diff -6.2) | 0.059 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1; target measured in part of the lines; both ways; artifact flags |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises TLR1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without NMRAL2P-1 | 0.068 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[LINC02328]] | B | LINC02328 activity raises TLR1's level | lines that do not express LINC02328 (14) vs lines expressing it (36) | 2.14× lower at baseline in the lines without LINC02328 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, PDE4B; maybe low, not absent |
| [[TLR6]] | C | TLR6 activity raises TLR1's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 4.28× lower at baseline in the lines without TLR6 | 1e-03 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent; co-absent with the target |
| [[NALCN]] | C | NALCN activity raises TLR1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without NALCN | 0.090 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MOB3C]] | B | TLR1 activity raises MOB3C's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without TLR1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[RIPK2-DT]] | B | TLR1 activity raises RIPK2-DT's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without TLR1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[TSEN54]] | B | TLR1 activity lowers TSEN54's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.72× higher at baseline in the lines without TLR1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[DGKI]] | B | TLR1 activity raises DGKI's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without TLR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| cells under [[Cobimetinib (drug)]] 5 µM | B | TLR1 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express TLR1 (15) vs lines expressing it (33) | the lines without TLR1: 1.23× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[MR1]] | B | TLR1 activity raises MR1's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without TLR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[LINC00944]] | B | TLR1 activity raises LINC00944's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 3.79× lower at baseline in the lines without TLR1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[CARD6]] | B | TLR1 activity raises CARD6's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without TLR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[SAMD1]] | B | TLR1 activity lowers SAMD1's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.60× higher at baseline in the lines without TLR1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[ZNF267]] | B | TLR1 activity raises ZNF267's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without TLR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[LINC02605]] | B | TLR1 activity raises LINC02605's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.08× lower at baseline in the lines without TLR1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | TLR1 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express TLR1 (15) vs lines expressing it (33) | the lines without TLR1: 1.27× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.1, 48.1); signed map (50.0, -8.2). **Vector** length 75.6, 17.1% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.9 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.4 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.9 | -7.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | toll like receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:38,790,677-38,856,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | rsc786, KIAA0012, CD281 |
| Gene groups (HGNC) | CD molecules; Toll like receptors |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE |
| Reactome | 23 pathways, smallest: Defensins; Antimicrobial peptides; MyD88 deficiency (TLR2/4) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15399](https://www.uniprot.org/uniprotkb/Q15399) (Toll-like receptor 1):

> Participates in the innate immune response to microbial agents. Specifically recognizes diacylated and triacylated lipopeptides. Cooperates with TLR2 to mediate the innate immune response to bacterial lipoproteins or lipopeptides. Forms the activation cluster TLR2:TLR1:CD14 in response to triacylated lipopeptides, this cluster triggers signaling from the cell surface and subsequently is targeted to the Golgi in a lipid-raft dependent pathway. Acts via MYD88 and TRAF6, leading to NF-kappa-B …

**Summary**, from NCBI Gene [7096](https://www.ncbi.nlm.nih.gov/gene/7096):

> The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. TLRs are highly conserved from Drosophila to humans and share structural and functional similarities. They recognize pathogen-associated molecular patterns (PAMPs) that are expressed on infectious agents, and mediate the production of cytokines necessary for the development of effective immunity. The various TLRs exhibit …

**Accessions** — [HGNC:11847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11847) · Entrez [7096](https://www.ncbi.nlm.nih.gov/gene/7096) · UniProt [Q15399](https://www.uniprot.org/uniprotkb/Q15399) · Ensembl [ENSG00000174125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174125)

## Data

Gene col 10462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10462); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10462]; `tensor/DDL_lfc|DDL_z.npy` [10462]; `embed/gene_vectors.npy` [10462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10462 or target_col == 10462). Every well: [[TLR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
