---
symbol: "TMEM178A"
type: "gene"
col: 7598
ensembl_id: "ENSG00000152154"
name: "transmembrane protein 178A"
location: "2p22.1"
module: 37
arm: "+"
pooled_cpm: 2.84
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TMEM178A

*transmembrane protein 178A* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.05× (z +9.9, q 2e-20, up in 22 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -10.8, q 2e-24, down in 26 of 30 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.467× (z -7.4, q 2e-11, down in 23 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02656]] (+0.65, fdr 7e-06), [[GRK3]] (+0.57, fdr 3e-05), [[MAP4K3-DT]] (+0.55, fdr 3e-05, ⚠ read-through risk), [[KAZN]] (+0.53, fdr 2e-04); moves opposite to [[PEX14]] (-0.52, fdr 6e-05), [[MCRS1]] (-0.51, fdr 1e-04), [[INTS14]] (-0.51, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CREG2]] → it (grade B ⚠); 2 go from it, the strongest it → [[MAP4K3-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +9.9 | 2e-20 | 22/39 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.6 | 8e-12 | 13/31 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +7.5 | 1e-11 | 25/36 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +6.6 | 8e-09 | 18/41 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +6.5 | 9e-09 | 17/41 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +6.0 | 1e-07 | 9/27 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +4.4 | 7e-04 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.004 | 10/41 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.9 | 0.006 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.035 | 5/44 (LS 180, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.045 | 5/35 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | 1.36× | +3.0 | 0.11 | 6/40 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.456×** | -10.8 | 2e-24 | 26/30 (SW 900, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.380×** | -9.4 | 1e-18 | 27/43 (SW480, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.467×** | -7.4 | 2e-11 | 23/41 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.474×** | -7.3 | 5e-11 | 23/39 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.504×** | -6.7 | 3e-09 | 21/41 (SW 900, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.509×** | -6.6 | 5e-09 | 21/38 (SW480, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.519×** | -6.4 | 1e-08 | 17/36 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.519×** | -6.4 | 1e-08 | 20/38 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -6.3 | 2e-08 | 21/31 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.479×** | -6.3 | 2e-08 | 20/36 (A498, SW 900, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.527×** | -6.2 | 3e-08 | 15/23 (SW 900, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.299×** | -6.1 | 4e-08 | 19/31 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.577×** | -5.0 | 2e-05 | 14/36 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -4.7 | 9e-05 | 15/19 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.425×** | -4.3 | 5e-04 | 16/34 (COLO 205, A498, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.486×** | -3.7 | 0.007 | 7/27 (A498, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.023 | 11/38 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -3.2 | 0.038 | 7/32 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.557×** | -3.0 | 0.074 | 2/27 (A498, LoVo) | inconsistent across doses | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.074 | 2/43 (HCT15, Panc 03.27) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.35 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0226× (z -15.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 8.21 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -12.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 4.20 | 0 | 1 | — | [[Rucaparib (phosphate) (drug)]] 0.05 µM 0.0570× (z -8.5) |
| [[COLO 205 (line)]] | alt | 9.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -12.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 4.88 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0766× (z -10.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02656]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[GRK3]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[MAP4K3-DT]] | +0.55 | +0.46 / +0.62 | both halves | 3e-05 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of MAP4K3-DT on the same strand (can correlate by spillover, not regulation) |
| [[KAZN]] | +0.53 | +0.30 / +0.62 | both halves | 2e-04 |  |
| [[LINC02940]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PPP1R32]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[HBG2]] | +0.52 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[LINC02036]] | +0.51 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[PLAC1]] | +0.51 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[LINC00595]] | +0.50 | +0.23 / +0.59 | both halves | 5e-04 |  |
| [[CLEC4A]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[LINC02885]] | +0.49 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[NME9]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX14]] | -0.52 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[MCRS1]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[INTS14]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[DHX30]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SMARCB1]] | -0.50 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[CPLANE1]] | -0.50 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[POLR3F]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[EPC2]] | -0.47 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[RIF1]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[WDR82]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NOL9]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PRORP]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREG2]] | B | CREG2 activity raises TMEM178A's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.47× lower at baseline in the lines without CREG2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TMEM178A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MAP4K3-DT]] | C | MAP4K3-DT's natural level strengthens TMEM178A's drug response | MAP4K3-DT's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.27; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP4K3-DT]] | C | TMEM178A activity raises MAP4K3-DT's level | lines that do not express TMEM178A (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without TMEM178A | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MPP4, B4GALT1, LCA5; maybe low, not absent |
| [[DLG5]] | C | TMEM178A activity raises DLG5's level | lines that do not express TMEM178A (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without TMEM178A | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MPP4, B4GALT1, LCA5; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.365). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.0, 33.1); signed map (7.1, 7.1). **Vector** length 51.6, 7.17% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.9 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.8 | -10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.7 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -6.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -5.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -6.4 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 178A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:39,664,982-39,717,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33926; previously TMEM178 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBL3](https://www.uniprot.org/uniprotkb/Q8NBL3) (Transmembrane protein 178A):

> Acts as a negative regulator of osteoclast differentiation in basal and inflammatory conditions by regulating TNFSF11-induced Ca (2+) fluxes, thereby controlling the induction of NFATC1.

**Summary**, from NCBI Gene [130733](https://www.ncbi.nlm.nih.gov/gene/130733):

> Predicted to be involved in negative regulation of osteoclast differentiation and regulation of cytosolic calcium ion concentration. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28517) · Entrez [130733](https://www.ncbi.nlm.nih.gov/gene/130733) · UniProt [Q8NBL3](https://www.uniprot.org/uniprotkb/Q8NBL3) · Ensembl [ENSG00000152154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152154)

## Data

Gene col 7598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7598); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7598]; `tensor/DDL_lfc|DDL_z.npy` [7598]; `embed/gene_vectors.npy` [7598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7598 or target_col == 7598). Every well: [[TMEM178A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM178A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
