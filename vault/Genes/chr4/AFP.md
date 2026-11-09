---
symbol: "AFP"
type: "gene"
col: 1304
ensembl_id: "ENSG00000081051"
name: "alpha fetoprotein"
location: "4q13.3"
module: 8
arm: "+"
pooled_cpm: 11.63
n_lines_expressing: 5
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# AFP

*alpha fetoprotein* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.92× (z +10.7, q 4e-24, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.91× (z +9.8, q 2e-20, up in 1 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.104×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0581×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0817×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.178×).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOB]] (+0.79, fdr 7e-06), [[ALB]] (+0.78, fdr 7e-06, ⚠ same locus), [[APOA2]] (+0.71, fdr 7e-06), [[AHSG]] (+0.69, fdr 7e-06); moves opposite to [[RFFL]] (-0.39, fdr 5e-04), [[SMG9]] (-0.38, fdr 0.002, ⚠ not reproduced), [[AFG3L1P]] (-0.38, fdr 3e-04), [[GAS8]] (-0.37, fdr 4e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PEG3]] → it (grade C ⚠); 14 go from it, the strongest it → [[APOD]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.92×** | +10.7 | 4e-24 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.91×** | +9.8 | 2e-20 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.55×** | +9.2 | 5e-18 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.18×** | +6.7 | 2e-09 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +5.2 | 2e-05 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +4.8 | 2e-04 | 0/1 | top dose only | cell-cycle shift (explains ~22% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.27×** | +4.4 | 7e-04 | 1/1 (HepG2/C3A) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.041 | 1/3 (HepG2/C3A) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.90×** | +3.3 | 0.066 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.89×** | +3.2 | 0.066 | 0/1 | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.38×** | +3.1 | 0.084 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.84×** | +3.1 | 0.089 | 0/2 | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.29× | +3.0 | 0.11 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1304.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.104×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0581×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0817×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.178×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.497× | -3.3 | 0.33 | 0/1 | inconsistent across doses | position effect removed |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.640× | -3.2 | 0.33 | 0/3 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 917 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0581× (z -16.1) |
| [[A-172 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 23 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOB]] | +0.79 | +0.86 / +0.62 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 844 |
| [[ALB]] | +0.78 | +0.79 / +0.90 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 927; ⚠ same locus (9.7 kb, same strand: neighbours can correlate without regulation) |
| [[APOA2]] | +0.71 | +0.88 / +0.67 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 905 |
| [[AHSG]] | +0.69 | +0.87 / +0.83 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 920 |
| [[PEG3]] | +0.62 | +0.78 / +0.06 | ⚠ one half (not replicated) | 0.004 |  |
| [[ITIH2]] | +0.59 | +0.51 / +0.71 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation; STRING 582 |
| [[AMBP]] | +0.54 | +0.64 / +0.55 | both halves | 1e-05 | STRING 823 |
| [[FGL1]] | +0.53 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[LYZ]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[APOA1]] | +0.51 | +0.83 / +0.69 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 721 |
| [[AZGP1]] | +0.48 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[RNF128]] | +0.48 | +0.53 / +0.24 | both halves | 5e-04 |  |
| [[CFI]] | +0.45 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[PLA2G2A]] | +0.45 | +0.55 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFFL]] | -0.39 | -0.24 / -0.28 | both halves | 5e-04 |  |
| [[SMG9]] | -0.38 | -0.26 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[AFG3L1P]] | -0.38 | -0.29 / -0.29 | both halves | 3e-04 |  |
| [[GAS8]] | -0.37 | -0.25 / -0.29 | both halves | 4e-04 |  |
| [[NSRP1]] | -0.37 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[INO80E]] | -0.37 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[GLRX2]] | -0.37 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[NME6]] | -0.37 | -0.26 / -0.32 | both halves | 4e-04 |  |
| [[DNAJC2]] | -0.37 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[TATDN1]] | -0.37 | -0.24 / -0.34 | both halves | 5e-04 |  |
| [[PLEKHN1]] | -0.37 | -0.24 / -0.25 | both halves | 4e-04 |  |
| [[VPS29]] | -0.37 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[CCDC137]] | -0.36 | -0.31 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEG3]] | C | PEG3 activity raises AFP's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 3.31× lower at baseline in the lines without PEG3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises AFP's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.72× lower at baseline in the lines without SERPINF1 | 0.040 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[APOB]] | C | APOB activity raises AFP's level | lines that do not express APOB (47) vs lines expressing it (3) | 26.65× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[APOA2]] | C | APOA2 activity raises AFP's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 13.37× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOD]] | C | AFP, [[ALB]] activity raises APOD's level | lines that do not express AFP, ALB (45) vs lines expressing them (5) | 1.72× lower at baseline in the lines without AFP, ALB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[NKD1]] | C | AFP activity raises NKD1's level | lines that do not express AFP (45) vs lines expressing it (5) | 5.60× lower at baseline in the lines without AFP | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[AZGP1]] | C | AFP, [[AHSG]], [[ALB]] activity raises AZGP1's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 2.62× lower at baseline in the lines without AFP, AHSG, ALB | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[LGR5]] | C | AFP activity raises LGR5's level | lines that do not express AFP (45) vs lines expressing it (5) | 3.26× lower at baseline in the lines without AFP | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[LYZ]] | C | AFP, [[AHSG]], [[ALB]] activity raises LYZ's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 3.22× lower at baseline in the lines without AFP, AHSG, ALB | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[APOB]] | C | AFP, [[ALB]] activity raises APOB's level | lines that do not express AFP, ALB (45) vs lines expressing them (5) | 10.19× lower at baseline in the lines without AFP, ALB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[PEG3]] | C | AFP activity raises PEG3's level | lines that do not express AFP (45) vs lines expressing it (5) | 11.03× lower at baseline in the lines without AFP | 0.061 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[PLA2G2A]] | C | AFP activity raises PLA2G2A's level | lines that do not express AFP (45) vs lines expressing it (5) | 4.09× lower at baseline in the lines without AFP | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[PCK1]] | C | AFP activity raises PCK1's level | lines that do not express AFP (45) vs lines expressing it (5) | 2.95× lower at baseline in the lines without AFP | 0.073 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[TF]] | C | AFP activity raises TF's level | lines that do not express AFP (45) vs lines expressing it (5) | 7.87× lower at baseline in the lines without AFP | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[VIL1]] | C | AFP activity raises VIL1's level | lines that do not express AFP (45) vs lines expressing it (5) | 2.79× lower at baseline in the lines without AFP | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[SLC6A14]] | C | AFP activity raises SLC6A14's level | lines that do not express AFP (45) vs lines expressing it (5) | 4.92× lower at baseline in the lines without AFP | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.231). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, 54.6); signed map (66.3, 19.9). **Vector** length 5.42, 2.14% of its response variance represented; |z| ≥ 3 in 22 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.4 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.2 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.1 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.1 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.1 | +0.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.1 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.2 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.2 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.2 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.2 | -0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.1 | -0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | alpha fetoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,431,138-73,456,174 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FETA; previously HPAFP |
| Gene groups (HGNC) | Albuminoid family |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P02771](https://www.uniprot.org/uniprotkb/P02771) (Alpha-fetoprotein):

> Binds copper, nickel, and fatty acids as well as, and bilirubin less well than, serum albumin. Only a small percentage (less than 2%) of the human AFP shows estrogen-binding properties.

**Summary**, from NCBI Gene [174](https://www.ncbi.nlm.nih.gov/gene/174):

> This gene encodes alpha-fetoprotein, a major plasma protein produced by the yolk sac and the liver during fetal life. Alpha-fetoprotein expression in adults is often associated with hepatocarcinoma and with teratoma, and has prognostic value for managing advanced gastric cancer. However, hereditary persistance of alpha-fetoprotein may also be found in individuals with no obvious pathology. The protein is thought to be the fetal counterpart of serum albumin, and the alpha-fetoprotein and albumin …

**Accessions** — [HGNC:317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:317) · Entrez [174](https://www.ncbi.nlm.nih.gov/gene/174) · UniProt [P02771](https://www.uniprot.org/uniprotkb/P02771) · Ensembl [ENSG00000081051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081051)

## Data

Gene col 1304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1304); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1304]; `tensor/DDL_lfc|DDL_z.npy` [1304]; `embed/gene_vectors.npy` [1304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1304 or target_col == 1304). Every well: [[AFP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
