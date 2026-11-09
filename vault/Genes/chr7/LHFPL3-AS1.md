---
symbol: "LHFPL3-AS1"
type: "gene"
col: 13559
ensembl_id: "ENSG00000226869"
name: "LHFPL3 antisense RNA 1"
location: "7q22.2"
module: 87
arm: "+"
pooled_cpm: 47.88
n_lines_expressing: 6
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 30
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# LHFPL3-AS1

*LHFPL3 antisense RNA 1* — 7q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.45× (z +10.1, q 2e-21, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0914×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 0.0885×); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 0.0894×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYR]] (+0.94, fdr 7e-06), [[A2M]] (+0.91, fdr 7e-06), [[SOX10]] (+0.89, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[RHOJ]] → it (grade C ⚠); 30 go from it, the strongest it → [[OBI1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.45×** | +10.1 | 2e-21 | 0/3 | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +9.7 | 9e-20 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +6.6 | 8e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +6.1 | 2e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **2.45×** | +6.0 | 2e-07 | 2/4 (C32, SK-MEL-2) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **2.12×** | +6.0 | 2e-07 | 3/5 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **2.08×** | +5.0 | 4e-05 | 2/4 (C32, SK-MEL-2) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +4.6 | 3e-04 | 0/3 | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +4.5 | 4e-04 | 2/3 (AN3 CA, C32) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **2.10×** | +4.4 | 7e-04 | 2/5 (SK-MEL-2, C32) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +4.1 | 0.002 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +3.7 | 0.010 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.38×** | +3.6 | 0.016 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **1.81×** | +3.2 | 0.062 | 1/3 (AN3 CA) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **2.15×** | +3.1 | 0.062 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.76×** | +3.0 | 0.093 | 0/2 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0914×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 0.0885×); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 0.0894×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.581× | -3.2 | 0.73 | 1/3 (SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 2,277 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0914× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 272 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -8.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A-172 (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYR]] | +0.94 | +0.95 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[TF]] | +0.83 | +0.85 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LINC02941]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[PI15]] | +0.78 | +0.70 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[CTTNBP2]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[RMEL3]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SAMMSON]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC02226]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC02566]] | +0.68 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[EDNRB]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOJ]] | C | RHOJ activity raises LHFPL3-AS1's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 3.09× lower at baseline in the lines without RHOJ | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises LHFPL3-AS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.99× lower at baseline in the lines without COL19A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[TYR]] | C | TYR activity raises LHFPL3-AS1's level | lines that do not express TYR (43) vs lines expressing it (7) | 11.78× lower at baseline in the lines without TYR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[A2M]] | C | A2M activity raises LHFPL3-AS1's level | lines that do not express A2M (42) vs lines expressing it (8) | 8.75× lower at baseline in the lines without A2M | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises LHFPL3-AS1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without EDNRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises LHFPL3-AS1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 6.33× lower at baseline in the lines without FCRLA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[TF]] | C | TF activity raises LHFPL3-AS1's level | lines that do not express TF (41) vs lines expressing it (9) | 7.11× lower at baseline in the lines without TF | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises LHFPL3-AS1's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 3.62× lower at baseline in the lines without IHO1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[APOD]] | C | APOD activity raises LHFPL3-AS1's level | lines that do not express APOD (43) vs lines expressing it (7) | 10.45× lower at baseline in the lines without APOD | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises LHFPL3-AS1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.02× lower at baseline in the lines without AEBP1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises LHFPL3-AS1's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 3.62× lower at baseline in the lines without TDRD9 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises LHFPL3-AS1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without TTTY10 | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 3, C 27. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OBI1-AS1]] | B | LHFPL3-AS1 activity raises OBI1-AS1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 2.62× lower at baseline in the lines without LHFPL3-AS1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1 |
| [[PLEKHS1]] | B | LHFPL3-AS1 activity raises PLEKHS1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 2.88× lower at baseline in the lines without LHFPL3-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1 |
| [[LINC01505]] | B | LHFPL3-AS1 activity raises LINC01505's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 4.08× lower at baseline in the lines without LHFPL3-AS1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1 |
| [[TF]] | C | LHFPL3-AS1 activity raises TF's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 3.17× lower at baseline in the lines without LHFPL3-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[SOX10]] | C | LHFPL3-AS1 activity raises SOX10's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 10.42× lower at baseline in the lines without LHFPL3-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[A2M]] | C | LHFPL3-AS1 activity raises A2M's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 9.73× lower at baseline in the lines without LHFPL3-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[TYR]] | C | LHFPL3-AS1 activity raises TYR's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.82× lower at baseline in the lines without LHFPL3-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[FCRLA]] | C | LHFPL3-AS1 activity raises FCRLA's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.79× lower at baseline in the lines without LHFPL3-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[C10orf90]] | C | LHFPL3-AS1 activity raises C10orf90's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 7.64× lower at baseline in the lines without LHFPL3-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[LEF1-AS1]] | C | LHFPL3-AS1 activity raises LEF1-AS1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 5.26× lower at baseline in the lines without LHFPL3-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[MIR3681HG]] | C | LHFPL3-AS1 activity raises MIR3681HG's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 15.88× lower at baseline in the lines without LHFPL3-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[RHOJ]] | C | LHFPL3-AS1 activity raises RHOJ's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 5.34× lower at baseline in the lines without LHFPL3-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.8, 29.0); signed map (29.9, 39.6). **Vector** length 32.0, 24.0% of its response variance represented; |z| ≥ 3 in 89 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.0 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.9 | +6.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.8 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.7 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.5 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.5 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.4 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.6 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.5 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.5 | -1.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.5 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LHFPL3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q22.2 — chr7:104,738,597-104,804,107 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40341) · Entrez [645591](https://www.ncbi.nlm.nih.gov/gene/645591) · Ensembl [ENSG00000226869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226869)

## Data

Gene col 13559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13559); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13559]; `tensor/DDL_lfc|DDL_z.npy` [13559]; `embed/gene_vectors.npy` [13559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13559 or target_col == 13559). Every well: [[LHFPL3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHFPL3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
