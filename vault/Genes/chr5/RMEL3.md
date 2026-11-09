---
symbol: "RMEL3"
type: "gene"
col: 14724
ensembl_id: "ENSG00000250961"
name: "enriched in melanoma 3"
location: "5q11.2"
module: 87
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 24
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# RMEL3

*enriched in melanoma 3* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.37× (z +19.5, q 0e+00, up in 6 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pexidartinib (hydrochloride) (drug)]] 5 µM: 0.479× (z -4.6, q 0.002, down in 4 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (C32 0.0506×); [[Panobinostat (drug)]] 5 µM in 1 line (C32 0.0644×; ⚠ cell-cycle shift, explains ~11% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMMSON]] (+0.73, fdr 7e-06), [[TYR]] (+0.73, fdr 7e-06), [[LHFPL3-AS1]] (+0.72, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[ITGA9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.37×** | +19.5 | 0e+00 | 6/10 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **15.4×** | +17.7 | 0e+00 | 10/11 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.99×** | +10.0 | 2e-21 | 2/2 (SNU-423, C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.96×** | +9.6 | 1e-19 | 1/3 (MIA PaCa-2) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.7 | 3e-16 | 4/13 (LoVo, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.72×** | +8.5 | 2e-15 | 7/12 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.54×** | +8.2 | 2e-14 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +6.7 | 1e-09 | 1/8 (LoVo) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.31×** | +5.4 | 4e-06 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +5.3 | 8e-06 | 2/9 (HS-578T, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.67×** | +4.5 | 3e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.92×** | +4.2 | 0.001 | 1/3 (MIA PaCa-2) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.0 | 0.003 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.8 | 0.005 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +3.8 | 0.006 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.009 | 4/14 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +3.5 | 0.017 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.024 | 4/15 (MIA PaCa-2, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.03×** | +3.3 | 0.030 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.050 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.94×** | +3.1 | 0.056 | 0/5 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.57×** | +2.9 | 0.086 | 0/5 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14724.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (C32 0.0506×); [[Panobinostat (drug)]] 5 µM in 1 line (C32 0.0644×; ⚠ cell-cycle shift, explains ~11% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.479×** | -4.6 | 0.002 | 4/13 (HT-29, SNU-1, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.707× | -3.2 | 0.34 | 3/16 (C32, SNU-1, …) | top dose only |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.603× | -3.1 | 0.34 | 1/12 (LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 65.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0506× (z -9.7) |
| [[A-172 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.735 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.601 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.735 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.688 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.704 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.618 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.582 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.487 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMMSON]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 | same gene group |
| [[TYR]] | +0.73 | +0.77 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LHFPL3-AS1]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CD96]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[LINC02941]] | +0.69 | +0.76 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[SOX10]] | +0.69 | +0.77 / +0.57 | both halves | 9e-06 |  |
| [[C10orf90]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[OBI1-AS1]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[A2M]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LINC02226]] | +0.65 | +0.63 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[TRPM8]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PI15]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RMEL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises RMEL3's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 4.40× lower at baseline in the lines without LHFPL3-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[TRPM8]] | C | TRPM8 activity raises RMEL3's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without TRPM8 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[TYR]] | C | TYR activity raises RMEL3's level | lines that do not express TYR (43) vs lines expressing it (7) | 3.90× lower at baseline in the lines without TYR | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises RMEL3's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.90× lower at baseline in the lines without FCRLA | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[SOX10]] | C | SOX10 activity raises RMEL3's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 6.37× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[COL19A1]] | C | COL19A1 activity raises RMEL3's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without COL19A1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[RHOJ]] | C | RHOJ activity raises RMEL3's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without RHOJ | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises RMEL3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 2.48× lower at baseline in the lines without AEBP1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LINC02941]] | C | LINC02941 activity raises RMEL3's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without LINC02941 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[APOD]] | C | APOD activity raises RMEL3's level | lines that do not express APOD (43) vs lines expressing it (7) | 3.41× lower at baseline in the lines without APOD | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA9]] | B | RMEL3 activity raises ITGA9's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without RMEL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[DPH6-DT]] | B | RMEL3 activity raises DPH6-DT's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without RMEL3 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[PKIA-AS1]] | B | RMEL3 activity raises PKIA-AS1's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without RMEL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[LINC01505]] | B | RMEL3 activity raises LINC01505's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without RMEL3 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[DAAM2]] | C | RMEL3 activity raises DAAM2's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.04× lower at baseline in the lines without RMEL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[MIR3681HG]] | C | RMEL3 activity raises MIR3681HG's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 3.52× lower at baseline in the lines without RMEL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[C10orf90]] | C | RMEL3 activity raises C10orf90's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without RMEL3 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | RMEL3 activity raises AEBP1's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.69× lower at baseline in the lines without RMEL3 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[COL19A1]] | C | RMEL3 activity raises COL19A1's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.36× lower at baseline in the lines without RMEL3 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[FCRLA]] | C | RMEL3 activity raises FCRLA's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without RMEL3 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[LHFPL3-AS1]] | C | RMEL3 activity raises LHFPL3-AS1's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without RMEL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[RHOJ]] | C | RMEL3 activity raises RHOJ's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without RMEL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.0, 29.2); signed map (29.9, 39.1). **Vector** length 27.7, 6.13% of its response variance represented; |z| ≥ 3 in 375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.4 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +19.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.1 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +3.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +0.4 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.4 | +0.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -0.7 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -3.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.6 | -0.5 |
|  | [[Neratinib (drug)]] 5 µM |  | -0.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | enriched in melanoma 3 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q11.2 — chr5:57,395,060-57,534,504 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53975) · Entrez [102724122](https://www.ncbi.nlm.nih.gov/gene/102724122) · Ensembl [ENSG00000250961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250961)

## Data

Gene col 14724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14724); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14724]; `tensor/DDL_lfc|DDL_z.npy` [14724]; `embed/gene_vectors.npy` [14724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14724 or target_col == 14724). Every well: [[RMEL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMEL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
