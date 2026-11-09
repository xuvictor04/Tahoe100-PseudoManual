---
symbol: "ADAMTS10"
type: "gene"
col: 6615
ensembl_id: "ENSG00000142303"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 10"
location: "19p13.2"
module: 128
arm: "+"
pooled_cpm: 4.94
n_lines_expressing: 23
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 17
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# ADAMTS10

*ADAM metallopeptidase with thrombospondin type 1 motif 10* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.54× (z +9.5, q 1e-18, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.72× (z +5.8, q 1e-06, up in 4 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.401× (z -9.7, q 3e-19, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYS1]] (+0.61, fdr 2e-05), [[PAX2]] (+0.58, fdr 2e-05), [[VSTM4]] (+0.57, fdr 1e-05); moves opposite to [[ANXA3]] (-0.52, fdr 1e-05), [[NEFM]] (-0.52, fdr 2e-05), [[ANK3]] (-0.50, fdr 3e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SSC5D]] → it (grade B ⚠); 17 go from it, the strongest it → [[SSC5D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +9.5 | 1e-18 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +7.2 | 2e-10 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +5.8 | 1e-06 | 4/18 (SHP-77, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 1e-05 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.72×** | +4.1 | 0.005 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.015 | 4/17 (A-427, A-172, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.015 | 1/12 (HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.017 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.027 | 3/18 (A-427, SW 900, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.2 | 0.071 | 0/8 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.401×** | -9.7 | 3e-19 | 18/20 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -7.2 | 2e-10 | 10/15 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.511×** | -7.1 | 2e-10 | 14/19 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.548×** | -6.3 | 3e-08 | 10/18 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.569×** | -5.9 | 3e-07 | 16/19 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.676×** | -5.8 | 5e-07 | 14/14 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.571×** | -5.7 | 1e-06 | 10/15 (A-172, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.593×** | -5.5 | 3e-06 | 13/19 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.609×** | -5.2 | 1e-05 | 13/19 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.624×** | -5.0 | 4e-05 | 10/20 (CHP-212, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.643×** | -4.7 | 2e-04 | 13/20 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.633×** | -4.6 | 2e-04 | 12/17 (A498, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.655×** | -4.5 | 4e-04 | 14/20 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.489×** | -4.0 | 0.003 | 11/18 (A498, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.700×** | -3.6 | 0.011 | 13/20 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.626×** | -3.5 | 0.014 | 8/19 (A498, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.540×** | -3.4 | 0.020 | 11/16 (A498, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.727×** | -3.4 | 0.021 | 1/19 (C-33 A) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.730×** | -3.1 | 0.054 | 3/19 (CHP-212, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 41.7 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0555× (z -20.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0731× (z -9.6) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -18.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0607× (z -16.6) |
| [[A549 (line)]] | wt | 21.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0516× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 6.64 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0734× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 7.00 | 0 | 2 (1 ⚠) | — | [[Arbutin (drug)]] 0.05 µM 0.0666× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.36 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0815× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 4.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -10.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.58 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0372× (z -11.8) ⚠ cell-cycle shift, explains ~67% of this change |
| [[PANC-1 (line)]] | alt | 2.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.105× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.895 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYS1]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[PAX2]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[VSTM4]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LRRC4B]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[KIRREL3]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ADAMTS2]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 | same gene group; pathway: Defective B3GALTL causes PpS |
| [[FAM20C]] | +0.52 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[MRC2]] | +0.51 | +0.63 / +0.32 | both halves | 2e-04 |  |
| [[EVC2]] | +0.50 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[MIR493HG]] | +0.50 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[SPANXA2-OT1]] | +0.50 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TSHZ3-AS1]] | +0.50 | +0.60 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA3]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[NEFM]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 | **novel candidate** |
| [[ANK3]] | -0.50 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[SYK]] | -0.50 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[ABO]] | -0.48 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[PROM1]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SAMD12-AS1]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[DENND1A]] | -0.45 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RFLNB]] | -0.44 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[TMEM45B]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ALDH1L1]] | -0.44 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[SLC28A3]] | -0.43 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity raises ADAMTS10's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without SSC5D | 0.017 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[MPZL2]] | B | MPZL2 activity lowers ADAMTS10's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 2.43× higher at baseline in the lines without MPZL2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[C1orf116]] | B | C1orf116 activity lowers ADAMTS10's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.44× higher at baseline in the lines without C1orf116 | 0.057 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CHROMR]] | B | CHROMR activity raises ADAMTS10's level | lines that do not express CHROMR (12) vs lines expressing it (38) | 2.58× lower at baseline in the lines without CHROMR | 0.091 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: CCDC88A, LARP6, DLK2; maybe low, not absent |
| [[MACC1]] | B | MACC1 activity lowers ADAMTS10's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.28× higher at baseline in the lines without MACC1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[PAX2]] | C | PAX2 activity raises ADAMTS10's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without PAX2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |
| [[RFLNB]] | C | RFLNB activity raises ADAMTS10's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 2.53× lower at baseline in the lines without RFLNB | 0.082 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1; co-absent with the target |
| [[KIRREL3]] | C | KIRREL3 activity raises ADAMTS10's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 3.08× lower at baseline in the lines without KIRREL3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; co-absent with the target |
| [[LINC03041]] | C | LINC03041 activity raises ADAMTS10's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.69× lower at baseline in the lines without LINC03041 | 0.095 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 8, C 9. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | ADAMTS10 activity raises SSC5D's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without ADAMTS10 | 0.012 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[CHROMR]] | B | ADAMTS10 activity raises CHROMR's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without ADAMTS10 | 0.032 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[PRRT2]] | B | ADAMTS10 activity raises PRRT2's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 1.86× lower at baseline in the lines without ADAMTS10 | 0.057 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[KHDC1-AS1]] | B | ADAMTS10 activity raises KHDC1-AS1's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without ADAMTS10 | 0.071 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| cells under [[Binimetinib (drug)]] 0.05 µM | B | ADAMTS10 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 0.89× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| cells under [[XRK3F2 (drug)]] 0.5 µM | B | ADAMTS10 activity raises the cells' numbers under XRK3F2 0.5 µM (protects the cells) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 0.88× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| cells under [[HI-TOPK-032 (drug)]] 0.05 µM | B | ADAMTS10 activity lowers the cells' numbers under HI-TOPK-032 0.05 µM (makes them more sensitive) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 1.41× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| cells under [[Afatinib (drug)]] 0.05 µM | B | ADAMTS10 activity raises the cells' numbers under Afatinib 0.05 µM (protects the cells) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 0.92× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[RFLNB]] | C | ADAMTS10 activity raises RFLNB's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 3.62× lower at baseline in the lines without ADAMTS10 | 0.010 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |
| [[TSHZ3]] | C | ADAMTS10 activity raises TSHZ3's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 6.24× lower at baseline in the lines without ADAMTS10 | 0.021 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |
| [[TSHZ3-AS1]] | C | ADAMTS10 activity raises TSHZ3-AS1's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 3.31× lower at baseline in the lines without ADAMTS10 | 0.031 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |
| [[KIRREL3]] | C | ADAMTS10 activity raises KIRREL3's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 4.43× lower at baseline in the lines without ADAMTS10 | 0.038 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.2, 38.8); signed map (23.7, 28.6). **Vector** length 53.9, 14.1% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +1.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.1 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +0.9 | -3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.7 | +1.6 |
|  | [[MK-3903 (drug)]] 5 µM |  | +0.7 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -1.5 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.5 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,580,240-8,610,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADAM-TS10 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H324](https://www.uniprot.org/uniprotkb/Q9H324) (A disintegrin and metalloproteinase with thrombospondin motifs 10):

> Metalloprotease that participate in microfibrils assembly. Microfibrils are extracellular matrix components occurring independently or along with elastin in the formation of elastic tissues.

**Summary**, from NCBI Gene [81794](https://www.ncbi.nlm.nih.gov/gene/81794):

> This gene belongs to the ADAMTS (a disintegrin and metalloproteinase domain with thrombospondin type-1 motifs) family of zinc-dependent proteases. ADAMTS proteases are complex secreted enzymes containing a prometalloprotease domain of the reprolysin type attached to an ancillary domain with a highly conserved structure that includes at least one thrombospondin type 1 repeat. They have been demonstrated to have important roles in connective tissue organization, coagulation, inflammation, …

**Accessions** — [HGNC:13201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13201) · Entrez [81794](https://www.ncbi.nlm.nih.gov/gene/81794) · UniProt [Q9H324](https://www.uniprot.org/uniprotkb/Q9H324) · Ensembl [ENSG00000142303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142303)

## Data

Gene col 6615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6615); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6615]; `tensor/DDL_lfc|DDL_z.npy` [6615]; `embed/gene_vectors.npy` [6615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6615 or target_col == 6615). Every well: [[ADAMTS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
