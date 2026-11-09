---
symbol: "ALB"
type: "gene"
col: 8737
ensembl_id: "ENSG00000163631"
name: "albumin"
location: "4q13.3"
module: 8
arm: "+"
pooled_cpm: 11.82
n_lines_expressing: 5
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ALB

*albumin* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 11.2× (z +12.7, q 5e-34, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.65× (z +11.4, q 1e-27, up in 1 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.180×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.138×; ⚠ cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.157×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSG]] (+0.92, fdr 7e-06), [[AFP]] (+0.78, fdr 7e-06, ⚠ same locus), [[AMBP]] (+0.67, fdr 7e-06), [[APOA1]] (+0.63, fdr 7e-06); moves opposite to [[MRPS16]] (-0.49, fdr 2e-04), [[RFFL]] (-0.48, fdr 5e-04), [[SMG9]] (-0.47, fdr 0.003, ⚠ not reproduced), [[CCDC137]] (-0.45, fdr 6e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[MIS18A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **11.2×** | +12.7 | 5e-34 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.65×** | +11.4 | 1e-27 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.44×** | +8.5 | 3e-15 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.22×** | +7.0 | 4e-10 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +6.3 | 3e-08 | 1/1 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.17×** | +5.7 | 1e-06 | 0/1 | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.65×** | +4.9 | 8e-05 | 1/1 (HepG2/C3A) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.94×** | +4.9 | 8e-05 | 1/1 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +4.7 | 2e-04 | 1/3 (HepG2/C3A) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.18×** | +4.1 | 0.002 | 1/2 (HepG2/C3A) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +4.1 | 0.002 | 0/1 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.09×** | +3.9 | 0.006 | 1/2 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +3.4 | 0.033 | 0/1 | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.053 | 0/2 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.28×** | +3.1 | 0.079 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8737.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.180×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.138×; ⚠ cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.157×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.502× | -3.4 | 0.36 | 0/2 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 925 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.157× (z -8.8) |
| [[A-172 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSG]] | +0.92 | +0.95 / +0.93 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 999 |
| [[AFP]] | +0.78 | +0.79 / +0.90 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 927; ⚠ same locus (9.7 kb, same strand: neighbours can correlate without regulation) |
| [[AMBP]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 970 |
| [[APOA1]] | +0.63 | +0.67 / +0.78 | both halves | 7e-06 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 998 |
| [[YBX1]] | +0.54 | +0.21 / +0.46 | both halves | 7e-04 |  |
| [[PIGR]] | +0.54 | +0.36 / +0.34 | both halves | 1e-04 | STRING 662 |
| [[APOH]] | +0.54 | +0.60 / +0.70 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 933 |
| [[BSG]] | +0.53 | +0.49 / +0.36 | both halves | 9e-05 | pathway: Aspirin ADME |
| [[PDIA3]] | +0.53 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[LYZ]] | +0.52 | +0.54 / +0.46 | both halves | 2e-05 | STRING 685 |
| [[ATP6AP2]] | +0.50 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[AGT]] | +0.50 | +0.46 / +0.53 | both halves | 2e-05 | STRING 868 |
| [[ITIH2]] | +0.49 | +0.42 / +0.68 | both halves | 4e-05 | pathway: Post-translational protein phosphorylation; STRING 832 |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS16]] | -0.49 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[RFFL]] | -0.48 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[SMG9]] | -0.47 | -0.46 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[CCDC137]] | -0.45 | -0.51 / -0.21 | both halves | 6e-04 |  |
| [[NSRP1]] | -0.45 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[INO80E]] | -0.45 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[NSUN5]] | -0.44 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[EXOC8]] | -0.44 | -0.36 / -0.26 | both halves | 4e-04 |  |
| [[TATDN1]] | -0.44 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[PHF5A]] | -0.44 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[GLRX2]] | -0.44 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[SDHAF2]] | -0.43 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[RNF166]] | -0.43 | -0.44 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALB's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PIGR]] | C | PIGR activity raises ALB's level | lines that do not express PIGR (45) vs lines expressing it (5) | 2.00× lower at baseline in the lines without PIGR | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises ALB's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.77× lower at baseline in the lines without SERPINF1 | 0.036 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[APOB]] | C | APOB activity raises ALB's level | lines that do not express APOB (47) vs lines expressing it (3) | 26.84× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[APOA2]] | C | APOA2 activity raises ALB's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 13.82× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[APOD]] | C | APOD activity raises ALB's level | lines that do not express APOD (43) vs lines expressing it (7) | 1.61× lower at baseline in the lines without APOD | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIS18A]] | B | [[AHSG]], ALB activity lowers MIS18A's level | lines that do not express AHSG, ALB (45) vs lines expressing them (5) | 1.27× higher at baseline in the lines without AHSG, ALB | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent genes |
| [[APOD]] | C | [[AFP]], ALB activity raises APOD's level | lines that do not express AFP, ALB (45) vs lines expressing them (5) | 1.72× lower at baseline in the lines without AFP, ALB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[AZGP1]] | C | [[AFP]], [[AHSG]], ALB activity raises AZGP1's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 2.62× lower at baseline in the lines without AFP, AHSG, ALB | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[LYZ]] | C | [[AFP]], [[AHSG]], ALB activity raises LYZ's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 3.22× lower at baseline in the lines without AFP, AHSG, ALB | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[APOB]] | C | [[AFP]], ALB activity raises APOB's level | lines that do not express AFP, ALB (45) vs lines expressing them (5) | 10.19× lower at baseline in the lines without AFP, ALB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[APOA2]] | C | [[AFP]], [[AHSG]], ALB activity raises APOA2's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 7.34× lower at baseline in the lines without AFP, AHSG, ALB | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.233). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, 54.9); signed map (66.7, 20.0). **Vector** length 4.41, 1.38% of its response variance represented; |z| ≥ 3 in 24 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.4 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.3 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.3 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.1 | +0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.1 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.1 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.1 | +4.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.2 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -0.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.2 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.1 | -0.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.1 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | albumin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,397,114-73,421,482 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Albuminoid family |
| Hallmark sets | PEROXISOME |
| Reactome | 30 pathways, smallest: Ciprofloxacin ADME; Prednisone ADME; Scavenging of heme from plasma |
| Matched by | ensembl_id |

**Function**, from UniProt [P02768](https://www.uniprot.org/uniprotkb/P02768) (Albumin):

> Binds water, Ca(2+), Na(+), K(+), fatty acids, hormones, bilirubin and drugs (Probable). Its main function is the regulation of the colloidal osmotic pressure of blood (Probable). Major zinc transporter in plasma, typically binds about 80% of all plasma zinc. Major calcium and magnesium transporter in plasma, binds approximately 45% of circulating calcium and magnesium in plasma (By similarity). Potentially has more than two calcium-binding sites and might additionally bind calcium in a …

**Summary**, from NCBI Gene [213](https://www.ncbi.nlm.nih.gov/gene/213):

> This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded preproprotein is proteolytically processed to generate the mature protein. A peptide derived from …

**Accessions** — [HGNC:399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:399) · Entrez [213](https://www.ncbi.nlm.nih.gov/gene/213) · UniProt [P02768](https://www.uniprot.org/uniprotkb/P02768) · Ensembl [ENSG00000163631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163631)

## Data

Gene col 8737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8737); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8737]; `tensor/DDL_lfc|DDL_z.npy` [8737]; `embed/gene_vectors.npy` [8737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8737 or target_col == 8737). Every well: [[ALB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
