---
symbol: "ITGA8"
type: "gene"
col: 1201
ensembl_id: "ENSG00000077943"
name: "integrin subunit alpha 8"
location: "10p13"
module: 104
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 13
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# ITGA8

*integrin subunit alpha 8* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.09× (z +19.9, q 0e+00, up in 4 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGP]] (+0.64, fdr 1e-05), [[CCN4]] (+0.63, fdr 1e-05), [[DAAM2]] (+0.63, fdr 1e-05); moves opposite to [[SLAMF7]] (-0.43, fdr 2e-04), [[ANKRD30B]] (-0.42, fdr 1e-04), [[PSG4]] (-0.39, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.09×** | +19.9 | 0e+00 | 4/7 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.77×** | +12.1 | 3e-31 | 2/3 (HS-578T, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.22×** | +11.0 | 8e-26 | 1/3 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +9.6 | 1e-19 | 2/7 (NCI-H2030, Panc 03.27) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +9.3 | 2e-18 | 2/5 (HS-578T, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.2 | 7e-08 | 1/9 (A-172) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.34×** | +6.1 | 8e-08 | 0/8 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +5.7 | 9e-07 | 2/8 (hTERT-HPNE, RPMI-7951) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.20×** | +5.6 | 1e-06 | 2/8 (NCI-H2030, NCI-H23) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +5.5 | 2e-06 | 1/7 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.60×** | +4.8 | 7e-05 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +4.8 | 7e-05 | 1/9 (NCI-H2030) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +4.2 | 0.001 | 1/8 (NCI-H2030) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.2 | 0.001 | 0/7 | top dose only | cell-cycle shift (explains ~24% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.05×** | +3.7 | 0.009 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.67×** | +3.7 | 0.009 | 1/9 (Panc 03.27) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.023 | 0/9 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.025 | 0/7 | top dose only |  |
| [[Pioglitazone (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.038 | 0/7 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.040 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.52×** | +3.0 | 0.064 | 0/9 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.631 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGP]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[CCN4]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[DAAM2]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[DCN]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 | pathway: ECM proteoglycans |
| [[ADAMTS2]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SRPX]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[FN1]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 | pathway: ECM proteoglycans; STRING 976 |
| [[COL6A3]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 | pathway: ECM proteoglycans; STRING 752 |
| [[LOX]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 | pathway: Elastic fibre formation |
| [[TWIST1]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PDGFRA]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 | STRING 443 |
| [[ITGA4]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 | same gene group; pathway: Extracellular matrix organization; STRING 778 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAMF7]] | -0.43 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ANKRD30B]] | -0.42 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[PSG4]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[SSTR2]] | -0.39 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ITGA8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PXDN]] | C | PXDN activity raises ITGA8's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without PXDN | 0.032 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises ITGA8's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.92× lower at baseline in the lines without COL3A1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises ITGA8's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.13× lower at baseline in the lines without PDGFRB | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises ITGA8's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.72× lower at baseline in the lines without PSG4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[ANKRD30B]] | C | ANKRD30B activity raises ITGA8's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without ANKRD30B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises ITGA8's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 2.53× lower at baseline in the lines without LINC01615 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[CA12]] | C | CA12 activity raises ITGA8's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.09× lower at baseline in the lines without CA12 | 0.075 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[TEK]] | C | TEK activity raises ITGA8's level | lines that do not express TEK (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without TEK | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[ANPEP]] | C | ANPEP activity raises ITGA8's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.06× lower at baseline in the lines without ANPEP | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises ITGA8's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without TWIST1 | 0.097 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | ITGA8 activity raises CACNA1C's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 3.71× lower at baseline in the lines without ITGA8 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent |
| [[SVEP1]] | B | ITGA8 activity raises SVEP1's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 2.63× lower at baseline in the lines without ITGA8 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent |
| [[LINC02109]] | C | ITGA8 activity raises LINC02109's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 3.45× lower at baseline in the lines without ITGA8 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |
| [[CARMN]] | C | ITGA8 activity raises CARMN's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 4.26× lower at baseline in the lines without ITGA8 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |
| [[PXDN]] | C | ITGA8 activity raises PXDN's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 7.74× lower at baseline in the lines without ITGA8 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |
| [[TWIST1]] | C | ITGA8 activity raises TWIST1's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 4.78× lower at baseline in the lines without ITGA8 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |
| [[COL4A1]] | C | ITGA8 activity raises COL4A1's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 6.47× lower at baseline in the lines without ITGA8 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |
| [[PDGFRB]] | C | ITGA8 activity raises PDGFRB's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 6.88× lower at baseline in the lines without ITGA8 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.0, 23.2); signed map (24.4, 38.9). **Vector** length 23.6, 6.08% of its response variance represented; |z| ≥ 3 in 232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +19.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.8 | +0.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +0.8 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.5 | -2.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:15,513,954-15,719,922 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Integrin alpha subunits |
| Reactome | 10 pathways, smallest: Formation of the ureteric bud; Molecules associated with elastic fibres; Elastic fibre formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P53708](https://www.uniprot.org/uniprotkb/P53708) (Integrin alpha-8):

> Integrin alpha-8/beta-1 functions in the genesis of kidney and probably of other organs by regulating the recruitment of mesenchymal cells into epithelial structures. It recognizes the sequence R-G-D in a wide array of ligands including TNC, FN1, SPP1 TGFB1, TGFB3 and VTN. NPNT is probably its functional ligand in kidney genesis. Neuronal receptor for TNC it mediates cell-cell interactions and regulates neurite outgrowth of sensory and motor neurons.

**Summary**, from NCBI Gene [8516](https://www.ncbi.nlm.nih.gov/gene/8516):

> Integrins are heterodimeric transmembrane receptor proteins that mediate numerous cellular processes including cell adhesion, cytoskeletal rearrangement, and activation of cell signaling pathways. Integrins are composed of alpha and beta subunits. This gene encodes the alpha 8 subunit of the heterodimeric integrin alpha8beta1 protein. The encoded protein is a single-pass type 1 membrane protein that contains multiple FG-GAP repeats. This repeat is predicted to fold into a beta propeller …

**Accessions** — [HGNC:6144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6144) · Entrez [8516](https://www.ncbi.nlm.nih.gov/gene/8516) · UniProt [P53708](https://www.uniprot.org/uniprotkb/P53708) · Ensembl [ENSG00000077943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077943)

## Data

Gene col 1201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1201); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1201]; `tensor/DDL_lfc|DDL_z.npy` [1201]; `embed/gene_vectors.npy` [1201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1201 or target_col == 1201). Every well: [[ITGA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
