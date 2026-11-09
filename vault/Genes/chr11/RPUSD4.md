---
symbol: "RPUSD4"
type: "gene"
col: 9140
ensembl_id: "ENSG00000165526"
name: "RNA pseudouridine synthase D4"
location: "11q24.2"
module: 18
arm: "+"
pooled_cpm: 20.32
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RPUSD4

*RNA pseudouridine synthase D4* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.73× (z +11.1, q 8e-26, up in 39 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.69× (z +10.6, q 1e-23, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.557× (z -11.4, q 4e-27, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADPGK]] (+0.68, fdr 7e-06), [[LYRM4]] (+0.68, fdr 7e-06), [[HEATR1]] (+0.68, fdr 7e-06); moves opposite to [[PIM3]] (-0.60, fdr 7e-06), [[EMC9]] (-0.60, fdr 1e-05), [[H3-3B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANKRD20A9P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.73×** | +11.1 | 8e-26 | 39/47 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +10.6 | 1e-23 | 33/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +8.0 | 2e-13 | 33/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +7.7 | 2e-12 | 27/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.6 | 2e-12 | 25/47 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.7 | 2e-09 | 23/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.3 | 2e-08 | 24/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 3e-08 | 22/47 (HOP62, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +5.5 | 2e-06 | 19/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.2 | 1e-05 | 18/47 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +5.0 | 3e-05 | 13/48 (SK-MEL-2, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +4.7 | 1e-04 | 13/45 (H4, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.003 | 12/44 (MIA PaCa-2, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.003 | 7/48 (PANC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.004 | 16/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.015 | 7/48 (HT-29, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.015 | 4/48 (LOX-IMVI, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.040 | 12/44 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -11.4 | 4e-27 | 32/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.708×** | -9.9 | 1e-20 | 30/47 (RKO, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.699×** | -7.2 | 8e-11 | 29/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -7.1 | 2e-10 | 25/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.766×** | -5.4 | 9e-06 | 22/47 (RKO, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -5.3 | 9e-06 | 21/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.825×** | -3.9 | 0.009 | 15/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.2 | 0.088 | 12/46 (RKO, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.740×** | -3.2 | 0.090 | 8/45 (Hs 766T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.856× | -3.1 | 0.090 | 8/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.090 | 9/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.854× | -3.1 | 0.10 | 15/47 (C32, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.1 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +11.9) | [[Harringtonine (drug)]] 5 µM 0.336× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 31.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +11.7) | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 32.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -13.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.403× (z -9.7) |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.108× (z -9.2) |
| [[C32 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 18.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.139× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.292× (z -9.5) |
| [[KATO III (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 22.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.377× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.77× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPGK]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[LYRM4]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 | pathway: rRNA processing |
| [[AHSA1]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[URB1]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[DDX54]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[COX10]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RBM19]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PPT1]] | +0.63 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[LIG3]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[POLR3E]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | -0.60 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[EMC9]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.59 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[SAV1]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NFKBIE]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[GORAB]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[LMNA]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SRSF9]] ⚠ | -0.54 | -0.45 / -0.60 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[METTL25B]] | -0.54 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A9P]] | B | ANKRD20A9P activity raises RPUSD4's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 1.32× lower at baseline in the lines without ANKRD20A9P | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RPUSD4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.5, -32.6); signed map (-1.4, -51.5). **Vector** length 90.1, 17.9% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +8.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.5 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.9 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA pseudouridine synthase D4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,202,096-126,211,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14494 |
| Gene groups (HGNC) | RNA pseudouridylate synthase domain containing; Pseudouridine synthases |
| Reactome | 5 pathways, smallest: rRNA modification in the mitochondrion; Mitochondrial mRNA modification; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CM3](https://www.uniprot.org/uniprotkb/Q96CM3) (Pseudouridylate synthase RPUSD4, mitochondrial):

> Catalyzes uridine to pseudouridine isomerization (pseudouridylation) of different mitochondrial RNA substrates. Acts on position 1397 in 16S mitochondrial ribosomal RNA (16S mt-rRNA). This modification is required for the assembly of 16S mt-rRNA into a functional mitochondrial ribosome. As a component of a functional protein-RNA module, consisting of RCC1L, NGRN, RPUSD3, RPUSD4, TRUB2, FASTKD2 and 16S mt-rRNA, controls 16S mt-rRNA abundance and is required for intra-mitochondrial translation. …

**Summary**, from NCBI Gene [84881](https://www.ncbi.nlm.nih.gov/gene/84881):

> Enables mitochondrial ribosomal large subunit rRNA binding activity; pseudouridine synthase activity; and tRNA binding activity. Involved in positive regulation of mitochondrial translation and pseudouridine synthesis. Located in mitochondrial matrix and ribonucleoprotein granule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25898) · Entrez [84881](https://www.ncbi.nlm.nih.gov/gene/84881) · UniProt [Q96CM3](https://www.uniprot.org/uniprotkb/Q96CM3) · Ensembl [ENSG00000165526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165526)

## Data

Gene col 9140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9140); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9140]; `tensor/DDL_lfc|DDL_z.npy` [9140]; `embed/gene_vectors.npy` [9140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9140 or target_col == 9140). Every well: [[RPUSD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPUSD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
