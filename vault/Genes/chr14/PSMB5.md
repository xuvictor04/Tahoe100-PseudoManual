---
symbol: "PSMB5"
type: "gene"
col: 2024
ensembl_id: "ENSG00000100804"
name: "proteasome 20S subunit beta 5"
location: "14q11.2"
module: 64
arm: "+"
pooled_cpm: 38.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 493
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMB5

*proteasome 20S subunit beta 5* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.21× (z +9.0, q 1e-16, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -7.5, q 4e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIRAP]] (+0.71, fdr 1e-05), [[MRPL18]] (+0.71, fdr 7e-06), [[PSMB4]] (+0.70, fdr 7e-06); moves opposite to [[JUNB]] (-0.62, fdr 1e-05), [[PICALM]] (-0.57, fdr 2e-05), [[LIMA1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 493 go from it, the strongest it → [[BTG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.21×** | +9.0 | 1e-16 | 44/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.05×** | +8.1 | 1e-13 | 44/48 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.16×** | +7.8 | 2e-12 | 45/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.4 | 2e-08 | 43/47 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.9 | 1e-04 | 29/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.56×** | +4.8 | 1e-04 | 31/45 (SK-MEL-2, NCI-H460, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.7 | 2e-04 | 1/48 (SW1417) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.49×** | +4.4 | 9e-04 | 23/41 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +3.5 | 0.024 | 24/48 (CFPAC-1, A549, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.76× | +3.0 | 0.13 | 18/43 (SHP-77, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -7.5 | 4e-11 | 40/48 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.527×** | -7.3 | 9e-11 | 43/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.561×** | -6.6 | 9e-09 | 39/48 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -6.2 | 1e-07 | 38/48 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.706×** | -5.6 | 2e-06 | 38/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.693×** | -4.2 | 0.003 | 30/48 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.723×** | -3.7 | 0.018 | 27/48 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.532×** | -3.4 | 0.041 | 24/48 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -3.4 | 0.041 | 24/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 21.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.15× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 37.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 45.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.10× (z +10.8) | — |
| [[A-172 (line)]] | wt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -8.6) |
| [[A-427 (line)]] | wt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.3) |
| [[A498 (line)]] | wt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.4) |
| [[AN3 CA (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.47× (z +9.1) ⚠ toxic | — |
| [[H4 (line)]] | wt | 58.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 98.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SW480 (line)]] | alt | 36.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.63× (z +9.2) | — |
| [[A549 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIRAP]] | +0.71 | +0.55 / +0.68 | both halves | 1e-05 | pathway: Antigen processing-Cross presentation |
| [[MRPL18]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PSMB4]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[MRPS15]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[RHBDD3]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[KEAP1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 647 |
| [[COA6]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PSMB6]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[BABAM1]] | +0.66 | +0.72 / +0.63 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PSMB3]] | +0.64 | +0.73 / +0.67 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[RCC1L]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PICALM]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[LIMA1]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[AMOT]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 | pathway: Adherens junctions interactions |
| [[ZMIZ2]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CSRP1]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PSMB5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PSMB5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*493 arrows, 493 of them with an alert ⚠; grade A 0, B 493, C 0. Shown: the 12 strongest; 481 more arrows (481 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTG2]] | B | PSMB5 activity raises BTG2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EMSY-DT]] | B | PSMB5 activity raises EMSY-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM200B]] | B | PSMB5 activity raises FAM200B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNAQ]] | B | PSMB5 activity lowers GNAQ's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPR37]] | B | PSMB5 activity raises GPR37's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ISYNA1]] | B | PSMB5 activity raises ISYNA1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MYRIP]] | B | PSMB5 activity raises MYRIP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NPTXR]] | B | PSMB5 activity raises NPTXR's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NT5C2]] | B | PSMB5 activity lowers NT5C2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PPIL2]] | B | PSMB5 activity lowers PPIL2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RFLNA]] | B | PSMB5 activity raises RFLNA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RUFY2]] | B | PSMB5 activity lowers RUFY2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-16.5, -10.1); signed map (-24.9, -25.1). **Vector** length 92.9, 28.5% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.0 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.2 | +9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.2 | +8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,016,543-23,035,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MB1 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28074](https://www.uniprot.org/uniprotkb/P28074) (Proteasome subunit beta type-5):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5693](https://www.ncbi.nlm.nih.gov/gene/5693):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9542) · Entrez [5693](https://www.ncbi.nlm.nih.gov/gene/5693) · UniProt [P28074](https://www.uniprot.org/uniprotkb/P28074) · Ensembl [ENSG00000100804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100804)

## Data

Gene col 2024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2024); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2024]; `tensor/DDL_lfc|DDL_z.npy` [2024]; `embed/gene_vectors.npy` [2024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2024 or target_col == 2024). Every well: [[PSMB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
