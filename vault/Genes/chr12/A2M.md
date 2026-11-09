---
symbol: "A2M"
type: "gene"
col: 10663
ensembl_id: "ENSG00000175899"
name: "alpha-2-macroglobulin"
location: "12p13.31"
module: 87
arm: "+"
pooled_cpm: 15.61
n_lines_expressing: 8
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 20
direction_downstream: 22
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# A2M

*alpha-2-macroglobulin* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.47× (z +11.2, q 2e-26, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +7.2, q 1e-10, up in 2 of 5 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.428× (z -5.6, q 1e-05, down in 4 of 4 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.0800×, HepG2/C3A 0.124×, RPMI-7951 0.138×, SK-MEL-2 0.167×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (C32 0.0730×, HepG2/C3A 0.134×, SK-MEL-2 0.151×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 0.142×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LHFPL3-AS1]] (+0.91, fdr 7e-06), [[SOX10]] (+0.87, fdr 7e-06), [[TF]] (+0.86, fdr 7e-06); moves opposite to [[PYDC2-AS1]] (-0.50, fdr 5e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[LINC02226]] → it (grade B ⚠); 22 go from it, the strongest it → [[DIRC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.47×** | +11.2 | 2e-26 | 2/4 (RPMI-7951, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.73×** | +9.9 | 2e-20 | 2/4 (HepG2/C3A, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +7.2 | 8e-11 | 2/4 (HepG2/C3A, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +7.2 | 1e-10 | 2/5 (HepG2/C3A, RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.07×** | +4.8 | 1e-04 | 2/3 (SK-MEL-2, HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +4.7 | 2e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.25×** | +3.6 | 0.028 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.0800×, HepG2/C3A 0.124×, RPMI-7951 0.138×, SK-MEL-2 0.167×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (C32 0.0730×, HepG2/C3A 0.134×, SK-MEL-2 0.151×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 0.142×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.428×** | -5.6 | 1e-05 | 4/4 (C32, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -4.2 | 0.009 | 3/4 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.610× | -3.3 | 0.19 | 1/5 (AN3 CA) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.635× | -3.0 | 0.36 | 2/4 (SK-MEL-2, C32) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 437 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -20.7) |
| [[HepG2_C3A (line)]] | wt | 477 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.3) |
| [[A-172 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHFPL3-AS1]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.87 | +0.79 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[TF]] | +0.86 | +0.90 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 820 |
| [[TYR]] | +0.83 | +0.85 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PI15]] | +0.77 | +0.65 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[FCRLA]] | +0.76 | +0.79 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[SAMMSON]] | +0.74 | +0.59 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CTTNBP2]] | +0.73 | +0.60 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[AEBP1]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LINC02941]] | +0.72 | +0.60 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[APOD]] | +0.70 | +0.89 / +0.22 | both halves | 6e-04 | STRING 574 |
| [[LEF1-AS1]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYDC2-AS1]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 1, C 19. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02226]] | B | LINC02226 activity raises A2M's level | lines that do not express LINC02226 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without LINC02226 | 0.099 | ⚠ within organs, on part of the lines; also absent: DPYSL4, MIR4458HG, ENSG00000256417; maybe low, not absent |
| [[RHOJ]] | C | RHOJ activity raises A2M's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 4.07× lower at baseline in the lines without RHOJ | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[TYR]] | C | TYR activity raises A2M's level | lines that do not express TYR (43) vs lines expressing it (7) | 10.24× lower at baseline in the lines without TYR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises A2M's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 9.73× lower at baseline in the lines without LHFPL3-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[TF]] | C | TF activity raises A2M's level | lines that do not express TF (41) vs lines expressing it (9) | 12.32× lower at baseline in the lines without TF | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises A2M's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.37× lower at baseline in the lines without AEBP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises A2M's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.34× lower at baseline in the lines without FCRLA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises A2M's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.29× lower at baseline in the lines without COL19A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises A2M's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 5.16× lower at baseline in the lines without TDRD9 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises A2M's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.85× lower at baseline in the lines without LOXL3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises A2M's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without IHO1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises A2M's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without FKBP9P1-1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 1, C 21. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | A2M activity raises DIRC3's level | lines that do not express A2M (42) vs lines expressing it (8) | 5.15× lower at baseline in the lines without A2M | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1 |
| [[GNAT3]] | C | A2M activity raises GNAT3's level | lines that do not express A2M (42) vs lines expressing it (8) | 1.18× lower at baseline in the lines without A2M | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[MIR3681HG]] | C | A2M activity raises MIR3681HG's level | lines that do not express A2M (42) vs lines expressing it (8) | 10.22× lower at baseline in the lines without A2M | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[AEBP1]] | C | A2M activity raises AEBP1's level | lines that do not express A2M (42) vs lines expressing it (8) | 6.53× lower at baseline in the lines without A2M | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[LHFPL3-AS1]] | C | A2M activity raises LHFPL3-AS1's level | lines that do not express A2M (42) vs lines expressing it (8) | 8.75× lower at baseline in the lines without A2M | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[TIMP3]] | C | A2M activity raises TIMP3's level | lines that do not express A2M (42) vs lines expressing it (8) | 8.88× lower at baseline in the lines without A2M | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[LOXL3]] | C | A2M activity raises LOXL3's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.75× lower at baseline in the lines without A2M | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[FCRLA]] | C | A2M activity raises FCRLA's level | lines that do not express A2M (42) vs lines expressing it (8) | 5.14× lower at baseline in the lines without A2M | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[SOX10]] | C | A2M activity raises SOX10's level | lines that do not express A2M (42) vs lines expressing it (8) | 6.59× lower at baseline in the lines without A2M | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[LEF1]] | C | A2M activity raises LEF1's level | lines that do not express A2M (42) vs lines expressing it (8) | 5.53× lower at baseline in the lines without A2M | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[DAAM2]] | C | A2M activity raises DAAM2's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.24× lower at baseline in the lines without A2M | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[CTTNBP2]] | C | A2M activity raises CTTNBP2's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.07× lower at baseline in the lines without A2M | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.0, 28.8); signed map (29.6, 39.7). **Vector** length 33.8, 19.9% of its response variance represented; |z| ≥ 3 in 114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.1 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.5 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.4 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.9 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | alpha-2-macroglobulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:9,067,664-9,116,229 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FWP007, S863-7, CPAMD5 |
| Gene groups (HGNC) | Alpha-2-macroglobulin family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, COAGULATION |
| Reactome | 13 pathways, smallest: Regulation of FXIIa and plasma kallikrein activity; HDL assembly; Plasma lipoprotein assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P01023](https://www.uniprot.org/uniprotkb/P01023) (Alpha-2-macroglobulin):

> Is able to inhibit all four classes of proteinases by a unique 'trapping' mechanism. This protein has a peptide stretch, called the 'bait region' which contains specific cleavage sites for different proteinases. When a proteinase cleaves the bait region, a conformational change is induced in the protein which traps the proteinase. The entrapped enzyme remains active against low molecular weight substrates (activity against high molecular weight substrates is greatly reduced). Following cleavage …

**Summary**, from NCBI Gene [2](https://www.ncbi.nlm.nih.gov/gene/2):

> The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer's disease (AD) due to its ability to mediate the clearance and degradation of A-beta, the major …

**Accessions** — [HGNC:7](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7) · Entrez [2](https://www.ncbi.nlm.nih.gov/gene/2) · UniProt [P01023](https://www.uniprot.org/uniprotkb/P01023) · Ensembl [ENSG00000175899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175899)

## Data

Gene col 10663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10663); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10663]; `tensor/DDL_lfc|DDL_z.npy` [10663]; `embed/gene_vectors.npy` [10663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10663 or target_col == 10663). Every well: [[A2M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A2M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
