---
symbol: "ADGRG7"
type: "gene"
col: 6932
ensembl_id: "ENSG00000144820"
name: "adhesion G protein-coupled receptor G7"
location: "3q12.2"
module: 108
arm: "+"
pooled_cpm: 7.79
n_lines_expressing: 10
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 16
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# ADGRG7

*adhesion G protein-coupled receptor G7* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.27× (z +14.3, q 2e-43, up in 3 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.0904×, SK-MEL-2 0.328×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.137×, NCI-H1573 0.207×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.248×, SK-MEL-2 0.323×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1573 0.344×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02616]] (+0.62, fdr 7e-06), [[LINC01905]] (+0.59, fdr 2e-05), [[GPR141]] (+0.54, fdr 3e-05); moves opposite to [[NHLRC3]] (-0.38, fdr 3e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[PKIA-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.27×** | +14.3 | 2e-43 | 3/5 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.54×** | +8.8 | 5e-16 | 1/3 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +7.7 | 3e-12 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +7.1 | 1e-10 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +5.9 | 3e-07 | 3/6 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.4 | 8e-06 | 2/8 (HS-578T, hTERT-HPNE) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.15×** | +5.3 | 1e-05 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +4.9 | 7e-05 | 3/7 (H4, hTERT-HPNE, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +4.7 | 2e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.4 | 5e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +4.2 | 0.002 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.76×** | +3.9 | 0.004 | 0/6 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.69×** | +3.3 | 0.036 | 0/3 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.049 | 2/6 (HS-578T, RPMI-7951) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +3.1 | 0.072 | 1/2 (NCI-H1573) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6932.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.0904×, SK-MEL-2 0.328×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.137×, NCI-H1573 0.207×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.248×, SK-MEL-2 0.323×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1573 0.344×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.609× | -3.5 | 0.15 | 5/6 (SK-MEL-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.596× | -3.4 | 0.15 | 1/7 (AN3 CA) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 0.05 µM |  | 0.597× | -3.4 | 0.15 | 1/6 (hTERT-HPNE) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.614× | -3.2 | 0.21 | 0/6 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.621× | -3.1 | 0.22 | 2/7 (NCI-H1573, RPMI-7951) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 199 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.344× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 93.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -16.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 2.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +8.8) | — |
| [[A-172 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.953 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.791 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02616]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LINC01905]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GPR141]] | +0.54 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[MIR548XHG]] | +0.53 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[LINC02050]] | +0.52 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[ZIC1]] | +0.51 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[MAGEA4-AS1]] | +0.49 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[GABRG2]] | +0.48 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CD96]] | +0.48 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[LINC00383]] | +0.48 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[LINC02566]] | +0.48 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[NLGN4X]] | +0.47 | +0.40 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC3]] | -0.38 | -0.30 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADGRG7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02566]] | C | LINC02566 activity raises ADGRG7's level | lines that do not express LINC02566 (43) vs lines expressing it (7) | 5.73× lower at baseline in the lines without LINC02566 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000241168, LINC02327, ENSG00000289605; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises ADGRG7's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.43× lower at baseline in the lines without F11-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[MIR548XHG]] | C | MIR548XHG activity raises ADGRG7's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 3.17× lower at baseline in the lines without MIR548XHG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises ADGRG7's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 3.22× lower at baseline in the lines without LINC02616 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises ADGRG7's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without LINC00491 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises ADGRG7's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.77× lower at baseline in the lines without GPR141 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises ADGRG7's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without LINC01456 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises ADGRG7's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.70× lower at baseline in the lines without GABRG2 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises ADGRG7's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.66× lower at baseline in the lines without C2CD4A | 0.089 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 10, C 6. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIA-AS1]] | B | ADGRG7 activity raises PKIA-AS1's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 2.38× lower at baseline in the lines without ADGRG7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[LRP2BP]] | B | ADGRG7 activity raises LRP2BP's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.64× lower at baseline in the lines without ADGRG7 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[SLCO6A1]] | B | ADGRG7 activity raises SLCO6A1's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.95× lower at baseline in the lines without ADGRG7 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[FAM177B]] | B | ADGRG7 activity raises FAM177B's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.29× lower at baseline in the lines without ADGRG7 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[VPS39-DT]] | B | ADGRG7 activity raises VPS39-DT's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.07× lower at baseline in the lines without ADGRG7 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[XG]] | B | ADGRG7 activity raises XG's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 2.20× lower at baseline in the lines without ADGRG7 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[CCN4]] | B | ADGRG7 activity raises CCN4's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 3.38× lower at baseline in the lines without ADGRG7 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[LINC02362]] | B | ADGRG7 activity raises LINC02362's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.64× lower at baseline in the lines without ADGRG7 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[LINC01619]] | B | ADGRG7 activity raises LINC01619's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.64× lower at baseline in the lines without ADGRG7 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[CD200R1]] | B | ADGRG7 activity raises CD200R1's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.45× lower at baseline in the lines without ADGRG7 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[LINC02616]] | C | ADGRG7 activity raises LINC02616's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 5.49× lower at baseline in the lines without ADGRG7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172; co-absent with the target |
| [[LINC00491]] | C | ADGRG7 activity raises LINC00491's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 2.50× lower at baseline in the lines without ADGRG7 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, 40.5); signed map (49.2, 34.4). **Vector** length 19.3, 5.09% of its response variance represented; |z| ≥ 3 in 192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +3.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.6 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -2.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.5 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor G7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,609,601-100,695,479 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14454; previously GPR128 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily G |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K78](https://www.uniprot.org/uniprotkb/Q96K78) (Adhesion G protein-coupled receptor G7):

> Orphan receptor.

**Summary**, from NCBI Gene [84873](https://www.ncbi.nlm.nih.gov/gene/84873):

> Predicted to enable G protein-coupled receptor activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19241) · Entrez [84873](https://www.ncbi.nlm.nih.gov/gene/84873) · UniProt [Q96K78](https://www.uniprot.org/uniprotkb/Q96K78) · Ensembl [ENSG00000144820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144820)

## Data

Gene col 6932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6932); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6932]; `tensor/DDL_lfc|DDL_z.npy` [6932]; `embed/gene_vectors.npy` [6932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6932 or target_col == 6932). Every well: [[ADGRG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
