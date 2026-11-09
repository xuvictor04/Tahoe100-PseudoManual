---
symbol: "LRCH2"
type: "gene"
col: 5036
ensembl_id: "ENSG00000130224"
name: "leucine rich repeats and calponin homology domain containing 2"
location: "Xq23"
module: 9
arm: "+"
pooled_cpm: 7.86
n_lines_expressing: 23
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# LRCH2

*leucine rich repeats and calponin homology domain containing 2* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +12.7, q 3e-34, up in 18 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.105×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.162×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0617×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.155×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF1]] (+0.59, fdr 1e-05), [[WDR17]] (+0.59, fdr 1e-05), [[RTN4RL2]] (+0.58, fdr 1e-05); moves opposite to [[TIMM23B-AGAP6]] (-0.55, fdr 4e-05), [[ATR]] (-0.51, fdr 3e-05), [[ANKMY1]] (-0.50, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SFMBT2]] → it (grade B ⚠); 3 go from it, the strongest it → [[AGAP6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +12.7 | 3e-34 | 18/20 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.79×** | +11.3 | 3e-27 | 19/20 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +9.6 | 2e-19 | 10/18 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +7.2 | 1e-10 | 11/17 (C-33 A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.9 | 5e-10 | 1/11 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.4 | 1e-08 | 3/19 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +5.5 | 3e-06 | 11/20 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.4 | 4e-06 | 1/15 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.3 | 8e-06 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.53×** | +4.7 | 1e-04 | 7/20 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +4.4 | 6e-04 | 11/19 (NCI-H2347, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.3 | 9e-04 | 1/16 (HOP62) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +4.2 | 0.001 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 7/20 (A-427, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.0 | 0.003 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 1/19 (HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.015 | 7/20 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.063 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.068 | 0/20 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.068 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.071 | 0/19 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5036.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.105×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.162×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0617×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.716× | -3.7 | 0.12 | 9/20 (NCI-H2347, CHP-212, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | 0.805× | -3.4 | 0.19 | 5/20 (NCI-H2347, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.746× | -3.1 | 0.24 | 4/19 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.822× | -3.1 | 0.24 | 5/20 (HOP62, A-427, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.759× | -3.1 | 0.24 | 2/20 (C32, J82) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 58.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 21.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -11.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 3.43 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.71× (z +8.6) | — |
| [[A549 (line)]] | wt | 3.29 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.67× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0617× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 17.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 74.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.155× (z -8.7) |
| [[HOP62 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.38 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.90× (z +8.7) | — |
| [[A-172 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.609 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF1]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[WDR17]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[RTN4RL2]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RYBP]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC25A48]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RRAGD]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ASXL3]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[PPP1R3C]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[HMSD]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[DISC1FP1]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[GPM6A]] | +0.56 | +0.47 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ATR]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[TRAPPC10]] | -0.49 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[ARIH2]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[NPLOC4]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CDR2]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[AGAP6]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[THAP4]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[EHMT1]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MIATNB]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFMBT2]] | B | SFMBT2 activity raises LRCH2's level | lines that do not express SFMBT2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without SFMBT2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, GHR |
| [[LINC01518]] | C | LINC01518 activity raises LRCH2's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 4.06× lower at baseline in the lines without LINC01518 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGAP6]] | B | LRCH2 activity lowers AGAP6's level | lines that do not express LRCH2 (27) vs lines expressing it (23) | 1.29× higher at baseline in the lines without LRCH2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PDGFRA, ENSG00000263655, PCDH17 |
| [[ADM]] | B | LRCH2 activity raises ADM's level | lines that do not express LRCH2 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without LRCH2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PDGFRA, ENSG00000263655, PCDH17 |
| [[USP9Y]] | C | LRCH2 activity raises USP9Y's level | lines that do not express LRCH2 (27) vs lines expressing it (23) | 5.04× lower at baseline in the lines without LRCH2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PDGFRA, ENSG00000263655, PCDH17; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.3, 30.4); signed map (34.2, 31.9). **Vector** length 52.3, 12.9% of its response variance represented; |z| ≥ 3 in 510 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and calponin homology domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:115,110,616-115,234,096 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1495 |
| Gene groups (HGNC) | Leucine rich repeats and calponin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VUJ6](https://www.uniprot.org/uniprotkb/Q5VUJ6) (Leucine-rich repeat and calponin homology domain-containing protein 2):

> May play a role in the organization of the cytoskeleton.

**Summary**, from NCBI Gene [57631](https://www.ncbi.nlm.nih.gov/gene/57631):

> This gene encodes a member of the leucine-rich repeat and calponin homology domain-containing protein family. These family members contain multiple N-terminal leucine-rich repeats, in addition to a C-terminal calponin homology domain, a type of domain that mediates interactions with actin filaments. These proteins are conserved across animal species, and studies of a similar Drosophila protein indicate a function as a cytoskeletal scaffolding protein. Alternative splicing of this gene results …

**Accessions** — [HGNC:29292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29292) · Entrez [57631](https://www.ncbi.nlm.nih.gov/gene/57631) · UniProt [Q5VUJ6](https://www.uniprot.org/uniprotkb/Q5VUJ6) · Ensembl [ENSG00000130224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130224)

## Data

Gene col 5036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5036); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5036]; `tensor/DDL_lfc|DDL_z.npy` [5036]; `embed/gene_vectors.npy` [5036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5036 or target_col == 5036). Every well: [[LRCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
