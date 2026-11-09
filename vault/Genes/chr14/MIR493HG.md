---
symbol: "MIR493HG"
type: "gene"
col: 15099
ensembl_id: "ENSG00000258399"
name: "MIR493 cluster host gene"
location: "14q32.31"
module: 13
arm: "+"
pooled_cpm: 3.98
n_lines_expressing: 14
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 24
direction_downstream: 28
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MIR493HG

*MIR493 cluster host gene* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.28× (z +10.7, q 6e-24, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.40× (z +4.4, q 0.001, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Benproperine (phosphate) (drug)]] 0.05 µM: 0.439× (z -3.8, q 0.069, down in 2 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEG3]] (+0.89, fdr 7e-06, ⚠ same locus), [[MEG8]] (+0.81, fdr 7e-06, ⚠ same locus), [[PLEKHG4B]] (+0.70, fdr 7e-06), [[VSTM4]] (+0.63, fdr 1e-05), [[KCNK3]] (+0.62, fdr 1e-05); moves opposite to [[SRGN]] (-0.57, fdr 1e-05), [[MAP3K1]] (-0.46, fdr 1e-04), [[DERA]] (-0.46, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[MEG3]] → it (grade C ⚠); 28 go from it, the strongest it → [[SSC5D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.28×** | +10.7 | 6e-24 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.40×** | +8.4 | 1e-14 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.54×** | +7.0 | 6e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +4.4 | 0.001 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +4.4 | 0.001 | 2/10 (SNU-423, NCI-H1573) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +4.3 | 0.002 | 6/11 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.97×** | +3.4 | 0.051 | 2/7 (SNU-423, NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.4 | 0.051 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.96×** | +3.4 | 0.051 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.53×** | +3.3 | 0.054 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 2.36× | +3.1 | 0.11 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 2.35× | +3.0 | 0.11 | 0/8 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.439×** | -3.8 | 0.069 | 2/10 (SW 1088, CHP-212) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.457×** | -3.6 | 0.069 | 1/11 (SNU-423) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.469×** | -3.5 | 0.069 | 0/10 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -3.5 | 0.069 | 10/11 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.518×** | -3.3 | 0.090 | 1/11 (CHP-212) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.519×** | -3.3 | 0.090 | 3/10 (A549, HOP62, …) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.524× | -3.0 | 0.19 | 1/11 (AN3 CA) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.551× | -3.0 | 0.19 | 8/11 (HOP62, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.2 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0765× (z -21.3) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0547× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -12.6) |
| [[A-172 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.263 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEG3]] | +0.89 | +0.86 / +0.86 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MEG8]] | +0.81 | +0.73 / +0.83 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PLEKHG4B]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[VSTM4]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[KCNK3]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[KCNMA1]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[LINC01705]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[PGF]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLIT3]] | +0.58 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[CYS1]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[EVC2]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[AGPAT4]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[LINC01411]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LINC01119]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MAP3K1]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[DERA]] | -0.46 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[ANK3]] | -0.46 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEG3]] | C | MEG3 activity raises MIR493HG's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 6.02× lower at baseline in the lines without MEG3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[MEG8]] | C | MEG8 activity raises MIR493HG's level | lines that do not express MEG8 (32) vs lines expressing it (18) | 4.53× lower at baseline in the lines without MEG8 | 0.003 | ⚠ within organs, on part of the lines; also absent: MEG3, MIR493HG, MXRA8; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises MIR493HG's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without EVC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[GREM1]] | C | GREM1 activity raises MIR493HG's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.25× lower at baseline in the lines without GREM1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises MIR493HG's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.81× lower at baseline in the lines without GDNF | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises MIR493HG's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.96× lower at baseline in the lines without INSYN2B | 0.013 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[DENND2A]] | C | DENND2A activity raises MIR493HG's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without DENND2A | 0.020 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises MIR493HG's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.09× lower at baseline in the lines without SPOCK1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[SYNDIG1]] | C | SYNDIG1 activity raises MIR493HG's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.61× lower at baseline in the lines without SYNDIG1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises MIR493HG's level | lines that do not express SRGN (30) vs lines expressing it (20) | 2.78× lower at baseline in the lines without SRGN | 0.036 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises MIR493HG's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.91× lower at baseline in the lines without PLEKHG4B | 0.039 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[ADAMTS10]] | C | ADAMTS10 activity raises MIR493HG's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 2.87× lower at baseline in the lines without ADAMTS10 | 0.043 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 8, C 20. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | MIR493HG activity raises SSC5D's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 1.76× lower at baseline in the lines without MIR493HG | 0.011 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[LINC01119]] | B | MIR493HG activity raises LINC01119's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.13× lower at baseline in the lines without MIR493HG | 0.017 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[EML1]] | B | MIR493HG activity raises EML1's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 3.21× lower at baseline in the lines without MIR493HG | 0.029 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[SMTN]] | B | MIR493HG activity raises SMTN's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 1.60× lower at baseline in the lines without MIR493HG | 0.048 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[LINC01119]] | B | MIR493HG activity strengthens LINC01119's drug response | lines that do not express MIR493HG (31) vs lines expressing it (12) | the lines without MIR493HG respond 0.65× as strongly (z diff +1.22); strongest at Panobinostat 0.5 µM: 0.57x vs 0.22x (z diff +4.0) | 0.060 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; target measured in part of the lines; artifact flags |
| [[TRIM9]] | B | MIR493HG activity raises TRIM9's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without MIR493HG | 0.084 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[AGPAT4]] | B | MIR493HG activity raises AGPAT4's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.16× lower at baseline in the lines without MIR493HG | 0.093 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| cells under [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM | B | MIR493HG activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (makes them more sensitive) | lines that do not express MIR493HG (36) vs lines expressing it (12) | the lines without MIR493HG: 1.23× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[MEG3]] | C | MIR493HG activity raises MEG3's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 13.62× lower at baseline in the lines without MIR493HG | 3e-05 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[MEG8]] | C | MIR493HG activity raises MEG8's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 10.43× lower at baseline in the lines without MIR493HG | 3e-04 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[DENND2A]] | C | MIR493HG activity raises DENND2A's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without MIR493HG | 0.007 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[EVC2]] | C | MIR493HG activity raises EVC2's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 4.45× lower at baseline in the lines without MIR493HG | 0.022 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.5, 15.9); signed map (22.7, 48.5). **Vector** length 38.8, 12.1% of its response variance represented; |z| ≥ 3 in 328 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -1.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | MIR493 cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q32.31 — chr14:100,836,269-100,947,194 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55978) · Entrez [123466208](https://www.ncbi.nlm.nih.gov/gene/123466208) · Ensembl [ENSG00000258399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258399)

## Data

Gene col 15099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15099); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15099]; `tensor/DDL_lfc|DDL_z.npy` [15099]; `embed/gene_vectors.npy` [15099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15099 or target_col == 15099). Every well: [[MIR493HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR493HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
