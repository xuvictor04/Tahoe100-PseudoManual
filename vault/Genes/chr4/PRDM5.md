---
symbol: "PRDM5"
type: "gene"
col: 6222
ensembl_id: "ENSG00000138738"
name: "PR/SET domain 5"
location: "4q27"
module: 124
arm: "+"
pooled_cpm: 14.11
n_lines_expressing: 37
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 15
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# PRDM5

*PR/SET domain 5* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +9.4, q 4e-18, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.183× (z -20.1, q 0e+00, down in 34 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENOX2]] (+0.71, fdr 1e-05), [[MSANTD2]] (+0.71, fdr 2e-05), [[SPOPL-DT]] (+0.69, fdr 1e-05); moves opposite to [[CFD]] (-0.71, fdr 4e-05), [[SLC27A1]] (-0.68, fdr 3e-05), [[RHPN2]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PYGO1]] → it (grade B ⚠); 15 go from it, the strongest it → [[ARHGAP31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.4 | 4e-18 | 24/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.55×** | +5.2 | 5e-05 | 18/34 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +5.0 | 1e-04 | 12/34 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.008 | 10/35 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.41×** | +3.9 | 0.010 | 16/33 (NCI-H460, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.013 | 17/34 (C-33 A, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.032 | 13/33 (NCI-H460, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.40×** | +3.2 | 0.085 | 4/34 (HT-29, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.183×** | -20.1 | 0e+00 | 34/35 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.202×** | -18.9 | 0e+00 | 34/35 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.275×** | -15.3 | 0e+00 | 31/34 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.508×** | -8.0 | 2e-13 | 28/35 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.632×** | -7.7 | 2e-12 | 26/35 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.319×** | -7.1 | 2e-10 | 24/34 (RKO, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.666×** | -6.8 | 1e-09 | 21/35 (NCI-H1573, J82, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.591×** | -6.2 | 3e-08 | 22/33 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.596×** | -6.1 | 6e-08 | 23/33 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -6.0 | 1e-07 | 21/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.390×** | -5.8 | 3e-07 | 23/35 (NCI-H23, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -5.8 | 3e-07 | 20/33 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -5.7 | 4e-07 | 20/33 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.425×** | -5.3 | 5e-06 | 22/33 (LOX-IMVI, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.683×** | -4.3 | 6e-04 | 15/32 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -4.0 | 0.002 | 16/34 (A-427, BT-474, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.551×** | -3.7 | 0.008 | 13/34 (RKO, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 77.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -17.0) |
| [[J82 (line)]] | alt | 27.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.172× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 16.4 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.167× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -14.1) |
| [[A-172 (line)]] | wt | 25.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -12.1) |
| [[A-427 (line)]] | wt | 32.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.5) |
| [[HOP62 (line)]] | alt | 22.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 8.04 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0590× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -10.9) |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -18.1) |
| [[A549 (line)]] | wt | 19.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0926× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -13.4) |
| [[A498 (line)]] | wt | 13.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -9.9) |
| [[BT-474 (line)]] | alt | 9.74 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0881× (z -9.8) |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -9.0) |
| [[C32 (line)]] | wt | 6.02 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0752× (z -8.7) |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -9.2) |
| [[HS-578T (line)]] | alt | 9.52 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -9.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 5.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 9.98 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0820× (z -11.7) |
| [[AN3 CA (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | +0.71 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.71 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SPOPL-DT]] | +0.69 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[HDGFL3]] | +0.69 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AVEN]] | +0.69 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CRPPA]] | +0.69 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[NSD1]] | +0.68 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PYCR2]] | +0.67 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CPSF2]] | +0.67 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.67 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[ARSB]] | +0.67 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CSTF3]] | +0.66 | +0.50 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | -0.71 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[SLC27A1]] | -0.68 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RHPN2]] | -0.65 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.64 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.64 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PLD3]] | -0.63 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[MGST3]] | -0.63 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FHIP1A]] | -0.63 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[CARHSP1]] | -0.62 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[TBC1D17]] | -0.62 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[HDAC5]] | -0.62 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[RNASE4]] | -0.61 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGO1]] | B | PYGO1 activity raises PRDM5's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.59× lower at baseline in the lines without PYGO1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[RNF217]] | B | RNF217 activity raises PRDM5's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 4.00× lower at baseline in the lines without RNF217 | 0.026 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[TOP2A]] | B | TOP2A activity lowers PRDM5's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers PRDM5's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ARHGAP31]] | B | ARHGAP31 activity raises PRDM5's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without ARHGAP31 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP31]] | B | PRDM5 activity raises ARHGAP31's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without PRDM5 | 0.015 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | PRDM5 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PRDM5 (13) vs lines expressing it (35) | the lines without PRDM5: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[IRAK1]] | B | PRDM5 activity raises IRAK1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.15× lower at baseline in the lines without PRDM5 | 0.021 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[AKAP7]] | B | PRDM5 activity raises AKAP7's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without PRDM5 | 0.046 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[RNF217]] | B | PRDM5 activity raises RNF217's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 3.16× lower at baseline in the lines without PRDM5 | 0.054 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[LRRK1]] | B | PRDM5 activity raises LRRK1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without PRDM5 | 0.071 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[PSMD6-AS1]] | B | PRDM5 activity raises PSMD6-AS1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.04× lower at baseline in the lines without PRDM5 | 0.074 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[CTNND1]] | B | PRDM5 activity raises CTNND1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.21× lower at baseline in the lines without PRDM5 | 0.074 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | PRDM5 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express PRDM5 (13) vs lines expressing it (35) | the lines without PRDM5: 1.23× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[SYT11]] | B | PRDM5 activity raises SYT11's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without PRDM5 | 0.082 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[RGS20]] | B | PRDM5 activity raises RGS20's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without PRDM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[NSD1]] | B | PRDM5 activity raises NSD1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without PRDM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.4, -6.6); signed map (23.0, -28.7). **Vector** length 91.5, 24.0% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.3 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +0.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.4 | -15.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -20.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -8.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -18.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:120,684,919-120,922,870 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PFM2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQX1](https://www.uniprot.org/uniprotkb/Q9NQX1) (PR domain zinc finger protein 5):

> Sequence-specific DNA-binding transcription factor. Represses transcription at least in part by recruitment of the histone methyltransferase EHMT2/G9A and histone deacetylases such as HDAC1. Regulates hematopoiesis-associated protein-coding and microRNA (miRNA) genes. May regulate the expression of proteins involved in extracellular matrix development and maintenance, including fibrillar collagens, such as COL4A1 and COL11A1, connective tissue components, such as HAPLN1, and molecules …

**Summary**, from NCBI Gene [11107](https://www.ncbi.nlm.nih.gov/gene/11107):

> The protein encoded by this gene is a transcription factor of the PR-domain protein family. It contains a PR-domain and multiple zinc finger motifs. Transcription factors of the PR-domain family are known to be involved in cell differentiation and tumorigenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9349) · Entrez [11107](https://www.ncbi.nlm.nih.gov/gene/11107) · UniProt [Q9NQX1](https://www.uniprot.org/uniprotkb/Q9NQX1) · Ensembl [ENSG00000138738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138738)

## Data

Gene col 6222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6222); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6222]; `tensor/DDL_lfc|DDL_z.npy` [6222]; `embed/gene_vectors.npy` [6222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6222 or target_col == 6222). Every well: [[PRDM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
