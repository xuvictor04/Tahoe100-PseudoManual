---
symbol: "EVC2"
type: "gene"
col: 10332
ensembl_id: "ENSG00000173040"
name: "EvC ciliary complex subunit 2"
location: "4p16.2"
module: 13
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 16
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 43
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# EVC2

*EvC ciliary complex subunit 2* — 4p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.76× (z +12.9, q 2e-35, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +6.2, q 1e-07, up in 0 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.572× (z -5.6, q 9e-06, down in 9 of 13 measured lines) ⚠ cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A-427 0.0898×, hTERT-HPNE 0.168×, NCI-H1792 0.144×, HOP62 0.227×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.140×, hTERT-HPNE 0.0914×, HOP62 0.140×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0450×, HOP62 0.158×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.153×, AN3 CA 0.240×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.295×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPPA]] (+0.71, fdr 7e-06), [[MIR137HG]] (+0.68, fdr 7e-06), [[PLEKHG4B]] (+0.68, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[PLEKHG4B]] → it (grade C ⚠); 43 go from it, the strongest it → [[OR9Q1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +12.9 | 2e-35 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.6 | 2e-19 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +8.4 | 1e-14 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.2 | 1e-07 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.80×** | +4.3 | 0.002 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.052 | 0/13 | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.072 | 1/13 (NCI-H1792) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.2 | 0.099 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.35× | +3.1 | 0.14 | 2/13 (NCI-H23, A-427) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10332.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A-427 0.0898×, hTERT-HPNE 0.168×, NCI-H1792 0.144×, HOP62 0.227×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.140×, hTERT-HPNE 0.0914×, HOP62 0.140×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0450×, HOP62 0.158×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.153×, AN3 CA 0.240×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.295×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.572×** | -5.6 | 9e-06 | 9/13 (HOP62, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.712× | -3.4 | 0.17 | 10/13 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.729× | -3.2 | 0.26 | 10/13 (hTERT-HPNE, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 63.4 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0450× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.5) |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0980× (z -13.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0318× (z -16.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -8.7) |
| [[AN3 CA (line)]] | alt | 74.5 | 0 | 3 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0850× (z -9.8) |
| [[A-427 (line)]] | wt | 22.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0898× (z -14.1) |
| [[A549 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 4.87 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0482× (z -9.4) |
| [[A-172 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPPA]] | +0.71 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[MIR137HG]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PLEKHG4B]] | +0.68 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PRRX1]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[APCDD1L-DT]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZNF667]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[OR9Q1]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[EVC]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 | same gene group; pathway: Activation of SMO; STRING 999; ⚠ same locus (1.7 kb: neighbours can correlate without regulation) |
| [[LINC02377]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[MIR493HG]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ARMCX2]] | +0.57 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG4B]] | C | PLEKHG4B activity raises EVC2's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 4.04× lower at baseline in the lines without PLEKHG4B | 0.006 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[GREM1]] | C | GREM1 activity raises EVC2's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 4.67× lower at baseline in the lines without GREM1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises EVC2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.30× lower at baseline in the lines without LAYN | 0.012 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[MME]] | C | MME activity raises EVC2's level | lines that do not express MME (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without MME | 0.013 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises EVC2's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 4.45× lower at baseline in the lines without MIR493HG | 0.022 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[FBXL7]] | C | FBXL7 activity raises EVC2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.58× lower at baseline in the lines without FBXL7 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[MEG3]] | C | MEG3 activity raises EVC2's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 3.91× lower at baseline in the lines without MEG3 | 0.026 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises EVC2's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without TCF4 | 0.030 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises EVC2's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.27× lower at baseline in the lines without PAPPA | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises EVC2's level | lines that do not express CARMN (40) vs lines expressing it (10) | 3.18× lower at baseline in the lines without CARMN | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises EVC2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without LINC01411 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[WNT5B]] | C | WNT5B activity raises EVC2's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 3.53× lower at baseline in the lines without WNT5B | 0.051 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 6, C 37. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OR9Q1]] | B | EVC2 activity strengthens OR9Q1's drug response | lines that do not express EVC2 (11) vs lines expressing it (10) | the lines without EVC2 respond 0.97× as strongly (z diff +0.09); strongest at Panobinostat 0.5 µM: 0.39x vs 0.13x (z diff +5.7) | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; target measured in part of the lines; artifact flags |
| [[COL23A1]] | B | EVC2 activity raises COL23A1's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without EVC2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[EVC]] | B | EVC2 activity raises EVC's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.60× lower at baseline in the lines without EVC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[GSDME]] | B | EVC2 activity raises GSDME's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without EVC2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[ARHGAP22]] | B | EVC2 activity raises ARHGAP22's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.58× lower at baseline in the lines without EVC2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| cells under [[Peretinoin (drug)]] 5 µM | B | EVC2 activity lowers the cells' numbers under Peretinoin 5 µM (makes them more sensitive) | lines that do not express EVC2 (34) vs lines expressing it (14) | the lines without EVC2: 1.23× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[GREM1]] | C | EVC2 activity raises GREM1's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.33× lower at baseline in the lines without EVC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[OR9Q1]] | C | EVC2 activity raises OR9Q1's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.61× lower at baseline in the lines without EVC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[LAYN]] | C | EVC2 activity raises LAYN's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without EVC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[LINC01098]] | C | EVC2 activity raises LINC01098's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.32× lower at baseline in the lines without EVC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[MME]] | C | EVC2 activity raises MME's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 7.22× lower at baseline in the lines without EVC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[MEG3]] | C | EVC2 activity raises MEG3's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.99× lower at baseline in the lines without EVC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.4, 18.9); signed map (27.5, 48.2). **Vector** length 40.1, 11.2% of its response variance represented; |z| ≥ 3 in 327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EvC ciliary complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.2 — chr4:5,542,772-5,709,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LBN |
| Gene groups (HGNC) | EvC complex subunits |
| Reactome | 3 pathways, smallest: Activation of SMO; Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UK5](https://www.uniprot.org/uniprotkb/Q86UK5) (Limbin):

> Component of the EvC complex that positively regulates ciliary Hedgehog (Hh) signaling. Plays a critical role in bone formation and skeletal development. May be involved in early embryonic morphogenesis.

**Summary**, from NCBI Gene [132884](https://www.ncbi.nlm.nih.gov/gene/132884):

> This gene encodes a protein that functions in bone formation and skeletal development. Mutations in this gene, as well as in a neighboring gene that lies in a head-to-head configuration, cause Ellis-van Creveld syndrome, an autosomal recessive skeletal dysplasia that is also known as chondroectodermal dysplasia. Mutations in this gene also cause acrofacial dysostosis Weyers type, also referred to as Curry-Hall syndrome, a disease that combines limb and facial abnormalities. Alternative splicing …

**Accessions** — [HGNC:19747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19747) · Entrez [132884](https://www.ncbi.nlm.nih.gov/gene/132884) · UniProt [Q86UK5](https://www.uniprot.org/uniprotkb/Q86UK5) · Ensembl [ENSG00000173040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173040)

## Data

Gene col 10332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10332); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10332]; `tensor/DDL_lfc|DDL_z.npy` [10332]; `embed/gene_vectors.npy` [10332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10332 or target_col == 10332). Every well: [[EVC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
