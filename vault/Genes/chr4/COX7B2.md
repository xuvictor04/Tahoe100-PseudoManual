---
symbol: "COX7B2"
type: "gene"
col: 9967
ensembl_id: "ENSG00000170516"
name: "cytochrome c oxidase subunit 7B2"
location: "4p12"
module: 108
arm: "+"
pooled_cpm: 4.69
n_lines_expressing: 8
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 18
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# COX7B2

*cytochrome c oxidase subunit 7B2* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.51× (z +12.0, q 3e-30, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.99× (z +10.9, q 5e-25, up in 0 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.536× (z -4.0, q 0.043, down in 0 of 5 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0378×, SNU-423 0.220×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.101×, SNU-423 0.200×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.312×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF208]] (+0.79, fdr 7e-06), [[RNF17]] (+0.65, fdr 1e-05), [[LINC01446]] (+0.63, fdr 1e-05); moves opposite to [[WDR91]] (-0.39, fdr 4e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MSRB3-AS1]] → it (grade C ⚠); 18 go from it, the strongest it → [[DACH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.51×** | +12.0 | 3e-30 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +10.9 | 5e-25 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.91×** | +10.7 | 1e-24 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.23×** | +9.1 | 1e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.41×** | +8.7 | 3e-16 | 0/4 | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.78×** | +7.2 | 7e-11 | 0/5 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +5.6 | 1e-06 | 0/5 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.14×** | +5.3 | 8e-06 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 3/5 (A-172, SNU-423, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.56×** | +4.6 | 2e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.1 | 0.002 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.29×** | +4.1 | 0.002 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.77×** | +3.7 | 0.008 | 1/3 (SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.6 | 0.012 | 0/5 | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.66×** | +3.5 | 0.015 | 0/5 | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.99×** | +3.4 | 0.027 | 0/5 | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.039 | 0/5 | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.039 | 2/5 (A-172, SW1417) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.039 | 0/5 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.048 | 1/5 (A-172) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.048 | 2/5 (A-172, SNU-423) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.62×** | +3.1 | 0.056 | 0/5 | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.067 | 0/5 | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.81×** | +2.9 | 0.082 | 0/5 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.51×** | +2.9 | 0.082 | 0/5 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0378×, SNU-423 0.220×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.101×, SNU-423 0.200×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.312×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.536×** | -4.0 | 0.043 | 0/5 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0378× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -15.9) |
| [[SNU-423 (line)]] | alt | 72.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.9) |
| [[A-172 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.502 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF208]] | +0.79 | +0.63 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[RNF17]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LINC01446]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[LINC00879]] | +0.60 | +0.42 / +0.74 | both halves | 4e-05 | **novel candidate** |
| [[LINC02476]] | +0.59 | +0.40 / +0.73 | both halves | 5e-05 |  |
| [[LINC02377]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[LINC01242]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[KC6]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CCNYL2]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[LINC02335]] | +0.56 | +0.30 / +0.81 | both halves | 2e-04 |  |
| [[LINC02506]] | +0.55 | +0.15 / +0.63 | ⚠ one half (not replicated) | 0.001 |  |
| [[UBBP4-1]] | +0.53 | +0.24 / +0.56 | both halves | 5e-04 |  |
| [[LINC00383]] | +0.53 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR91]] | -0.39 | -0.26 / -0.30 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3-AS1]] | C | MSRB3-AS1 activity raises COX7B2's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 3.95× lower at baseline in the lines without MSRB3-AS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |
| [[LINC01205]] | C | LINC01205 activity raises COX7B2's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 3.02× lower at baseline in the lines without LINC01205 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises COX7B2's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 2.59× lower at baseline in the lines without LINC00648 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises COX7B2's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.38× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC02575]] | C | LINC02575 activity raises COX7B2's level | lines that do not express LINC02575 (32) vs lines expressing it (18) | 1.71× lower at baseline in the lines without LINC02575 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1; co-absent with the target |
| [[LINC00879]] | C | LINC00879 activity raises COX7B2's level | lines that do not express LINC00879 (46) vs lines expressing it (4) | 3.87× lower at baseline in the lines without LINC00879 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, ENSG00000234426, APOB; co-absent with the target; its own permutation p |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises COX7B2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.36× lower at baseline in the lines without CCDC144NL-AS1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises COX7B2's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without LINC01446 | 0.099 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 2, C 16. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DACH2]] | B | COX7B2 activity raises DACH2's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 1.21× lower at baseline in the lines without COX7B2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205 |
| cells under [[Futibatinib (drug)]] 0.5 µM | B | COX7B2 activity raises the cells' numbers under Futibatinib 0.5 µM (protects the cells) | lines that do not express COX7B2 (42) vs lines expressing it (6) | the lines without COX7B2: 0.78× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205 |
| [[LINC01205]] | C | COX7B2 activity raises LINC01205's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 4.93× lower at baseline in the lines without COX7B2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC00470]] | C | COX7B2 activity raises LINC00470's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 7.26× lower at baseline in the lines without COX7B2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[MIR548XHG]] | C | COX7B2 activity raises MIR548XHG's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 7.56× lower at baseline in the lines without COX7B2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC02476]] | C | COX7B2 activity raises LINC02476's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 6.44× lower at baseline in the lines without COX7B2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC00383]] | C | COX7B2 activity raises LINC00383's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 2.54× lower at baseline in the lines without COX7B2 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC02335]] | C | COX7B2 activity raises LINC02335's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 4.08× lower at baseline in the lines without COX7B2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[CCNYL2]] | C | COX7B2 activity raises CCNYL2's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 2.71× lower at baseline in the lines without COX7B2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC02575]] | C | COX7B2 activity raises LINC02575's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 3.88× lower at baseline in the lines without COX7B2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[CCNYL2-1]] | C | COX7B2 activity raises CCNYL2-1's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 2.06× lower at baseline in the lines without COX7B2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC02484]] | C | COX7B2 activity raises LINC02484's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 5.37× lower at baseline in the lines without COX7B2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.6, 27.5); signed map (32.9, 38.3). **Vector** length 16.4, 5.27% of its response variance represented; |z| ≥ 3 in 97 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +7.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.4 | +0.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.4 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +1.2 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.4 | -1.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 7B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:46,734,827-46,909,245 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF08](https://www.uniprot.org/uniprotkb/Q8TF08) (Cytochrome c oxidase subunit 7B2, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [170712](https://www.ncbi.nlm.nih.gov/gene/170712):

> Predicted to be involved in mitochondrial electron transport, cytochrome c to oxygen. Predicted to act upstream of or within spermatogenesis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24381) · Entrez [170712](https://www.ncbi.nlm.nih.gov/gene/170712) · UniProt [Q8TF08](https://www.uniprot.org/uniprotkb/Q8TF08) · Ensembl [ENSG00000170516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170516)

## Data

Gene col 9967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9967); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9967]; `tensor/DDL_lfc|DDL_z.npy` [9967]; `embed/gene_vectors.npy` [9967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9967 or target_col == 9967). Every well: [[COX7B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX7B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
