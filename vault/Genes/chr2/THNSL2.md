---
symbol: "THNSL2"
type: "gene"
col: 6844
ensembl_id: "ENSG00000144115"
name: "threonine synthase like 2"
location: "2p11.2"
module: 10
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 31
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# THNSL2

*threonine synthase like 2* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +8.3, q 6e-14, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.55× (z +4.2, q 0.008, up in 7 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.257× (z -12.9, q 4e-35, down in 22 of 26 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF747]] (+0.68, fdr 1e-05), [[KRCC1]] (+0.68, fdr 1e-05), [[ANKRD31]] (+0.67, fdr 1e-05); moves opposite to [[KIAA1328]] (-0.57, fdr 9e-05), [[GNA12]] (-0.55, fdr 1e-04), [[AP3M2]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKRD20A21P]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZCWPW1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.3 | 6e-14 | 4/6 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +4.2 | 0.008 | 7/25 (A498, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.047 | 6/21 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.053 | 3/21 (A498, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.053 | 8/23 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.069 | 6/26 (A498, NCI-H2347, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.071 | 9/26 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.27×** | +3.2 | 0.091 | 2/28 (A-427, BT-474) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.39× | +3.1 | 0.11 | 6/17 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.85× | +3.1 | 0.13 | 1/9 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.37× | +3.0 | 0.13 | 6/13 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.257×** | -12.9 | 4e-35 | 22/26 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.308×** | -11.1 | 2e-26 | 20/29 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.349×** | -10.0 | 4e-21 | 19/28 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -9.5 | 4e-19 | 21/27 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.375×** | -9.3 | 2e-18 | 19/29 (PANC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.385×** | -9.0 | 2e-17 | 17/20 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.389×** | -8.9 | 3e-17 | 19/29 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.450×** | -7.6 | 3e-12 | 17/25 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.486×** | -6.4 | 8e-09 | 18/26 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.521×** | -6.2 | 4e-08 | 13/26 (PANC-1, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.296×** | -6.0 | 9e-08 | 18/25 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.616×** | -4.6 | 2e-04 | 13/21 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -4.5 | 2e-04 | 12/29 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -4.2 | 0.001 | 10/23 (NCI-H1573, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.632×** | -4.0 | 0.002 | 13/28 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -3.6 | 0.009 | 12/27 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.591×** | -3.5 | 0.012 | 6/26 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -3.5 | 0.015 | 8/29 (CHP-212, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.611×** | -3.3 | 0.026 | 6/29 (J82, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.703×** | -3.1 | 0.058 | 3/26 (NCI-H2347, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0878× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0963× (z -10.9) |
| [[PANC-1 (line)]] | alt | 7.26 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.172× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0556× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.160× (z -8.9) |
| [[HOP62 (line)]] | alt | 7.51 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.141× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.158× (z -11.3) |
| [[SW480 (line)]] | alt | 3.52 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0477× (z -13.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.122× (z -9.4) |
| [[A-427 (line)]] | wt | 4.66 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0886× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 6.72 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0613× (z -10.8) |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0756× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.102× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 3.87 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0409× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.154× (z -8.7) |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.322 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF747]] | +0.68 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[KRCC1]] | +0.68 | +0.56 / +0.51 | both halves | 1e-05 | STRING 420 |
| [[ANKRD31]] | +0.67 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ZNF818P]] | +0.65 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[HHLA3]] | +0.64 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TSGA10]] | +0.64 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[MYL5]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[F8]] | +0.63 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | +0.63 | +0.60 / +0.26 | both halves | 3e-04 |  |
| [[FAM227B]] | +0.63 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[C7orf25]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[RWDD2B]] | +0.62 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1328]] | -0.57 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[GNA12]] | -0.55 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[AP3M2]] | -0.54 | -0.39 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises THNSL2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without ANKRD20A21P | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[ERICH2-DT]] | B | ERICH2-DT activity raises THNSL2's level | lines that do not express ERICH2-DT (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without ERICH2-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: ERICH2, GAD1, ENSG00000256673; maybe low, not absent |
| [[HENMT1]] | B | HENMT1 activity raises THNSL2's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without HENMT1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCWPW1]] | B | THNSL2 activity raises ZCWPW1's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without THNSL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[ERICH2-DT]] | B | THNSL2 activity raises ERICH2-DT's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without THNSL2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[LINC01725]] | B | THNSL2 activity raises LINC01725's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without THNSL2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[DEDD]] | B | THNSL2 activity raises DEDD's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without THNSL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[SHROOM1]] | B | THNSL2 activity raises SHROOM1's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without THNSL2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.3, 13.5); signed map (26.6, -12.1). **Vector** length 47.0, 8.13% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +2.9 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.4 | -8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -12.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | threonine synthase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:88,170,295-88,186,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10916, TSH2, SOFAT |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YJ6](https://www.uniprot.org/uniprotkb/Q86YJ6) (Threonine synthase-like 2):

> [Isoform 1]: Acts as a catabolic phospho-lyase on both gamma- and beta-phosphorylated substrates. Degrades O-phospho-threonine (PThr) to alpha-ketobutyrate, ammonia and phosphate (By similarity).; [Isoform SOFAT]: Potent inducer of osteoblastic production of IL6. May act to exacerbate inflammation and/or bone turnover under inflammatory conditions.

**Summary**, from NCBI Gene [55258](https://www.ncbi.nlm.nih.gov/gene/55258):

> This gene encodes a threonine synthase-like protein. A similar enzyme in mouse can catalyze the degradation of O-phospho-homoserine to a-ketobutyrate, phosphate, and ammonia. This protein also has phospho-lyase activity on both gamma and beta phosphorylated substrates. In mouse an alternatively spliced form of this protein has been shown to act as a cytokine and can induce the production of the inflammatory cytokine IL6 in osteoblasts. Alternate splicing results in multiple transcript variants. …

**Accessions** — [HGNC:25602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25602) · Entrez [55258](https://www.ncbi.nlm.nih.gov/gene/55258) · UniProt [Q86YJ6](https://www.uniprot.org/uniprotkb/Q86YJ6) · Ensembl [ENSG00000144115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144115)

## Data

Gene col 6844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6844); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6844]; `tensor/DDL_lfc|DDL_z.npy` [6844]; `embed/gene_vectors.npy` [6844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6844 or target_col == 6844). Every well: [[THNSL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THNSL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
