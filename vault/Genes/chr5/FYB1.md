---
symbol: "FYB1"
type: "gene"
col: 1334
ensembl_id: "ENSG00000082074"
name: "FYN binding protein 1"
location: "5p13.1"
module: 166
arm: "+"
pooled_cpm: 6.13
n_lines_expressing: 18
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 25
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# FYB1

*FYN binding protein 1* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.56× (z +20.9, q 0e+00, up in 12 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.635× (z -3.6, q 0.089, down in 6 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.136×, A549 0.332×; ⚠ cell-cycle shift, explains ~65% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.318×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.150×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0811×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP15]] (+0.64, fdr 1e-05), [[GBP5]] (+0.63, fdr 7e-06), [[IDO1]] (+0.63, fdr 5e-05); moves opposite to [[ERGIC1]] (-0.56, fdr 4e-05), [[NPHP4]] (-0.52, fdr 1e-04), [[ZHX3]] (-0.52, fdr 6e-05).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 25 go from it, the strongest it → [[APOL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.56×** | +20.9 | 0e+00 | 12/14 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.60×** | +12.0 | 9e-31 | 3/9 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +11.8 | 8e-30 | 8/14 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +10.5 | 2e-23 | 2/5 (Hs 766T, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.54×** | +8.8 | 2e-16 | 2/6 (SNU-423, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.82×** | +8.1 | 4e-14 | 7/15 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +7.5 | 6e-12 | 9/14 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.5 | 6e-12 | 9/15 (J82, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +6.5 | 7e-09 | 6/15 (CFPAC-1, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.4 | 7e-04 | 1/14 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +4.0 | 0.003 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.9 | 0.005 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.9 | 0.005 | 2/13 (SNU-423, J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 3/14 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.6 | 0.011 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +3.5 | 0.019 | 4/15 (BT-474, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.029 | 7/14 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.068 | 6/15 (A549, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.0 | 0.068 | 4/11 (HS-578T, A549, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.072 | 5/15 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.136×, A549 0.332×; ⚠ cell-cycle shift, explains ~65% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.318×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.150×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0811×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.635×** | -3.6 | 0.089 | 6/15 (Hs 766T, NCI-H1573, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.089 | 7/15 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.650× | -3.4 | 0.12 | 8/15 (SK-MEL-2, C32, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.761× | -3.1 | 0.28 | 2/15 (C32, SNU-423) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -12.6) |
| [[A549 (line)]] | wt | 174 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -12.7) |
| [[HS-578T (line)]] | alt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.748 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP15]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[GBP5]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[IDO1]] | +0.63 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[LINC01828]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[EDIL3-DT]] | +0.62 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[LINC02968]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[CNTN6]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[COL24A1]] | +0.61 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[LINC00536]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[LINC00504]] | +0.60 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[GBP4]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CASC15]] | +0.59 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NPHP4]] | -0.52 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[ZHX3]] | -0.52 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[TBC1D16]] | -0.51 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FYB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01285]] | B | LINC01285 activity raises FYB1's level | lines that do not express LINC01285 (21) vs lines expressing it (29) | 1.58× lower at baseline in the lines without LINC01285 | 0.080 | ⚠ within organs, on part of the lines; also absent: HNF1A, SLC22A3, LINC01819; maybe low, not absent |
| [[MSC]] | C | MSC activity raises FYB1's level | lines that do not express MSC (34) vs lines expressing it (16) | 2.54× lower at baseline in the lines without MSC | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[LINC02968]] | C | LINC02968 activity raises FYB1's level | lines that do not express LINC02968 (27) vs lines expressing it (23) | 1.92× lower at baseline in the lines without LINC02968 | 0.036 | ⚠ within organs, on part of the lines; also absent: LCP1, OR9Q1, IL11; co-absent with the target |
| [[CFH]] | C | CFH activity raises FYB1's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without CFH | 0.044 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[TP63]] | C | TP63 activity raises FYB1's level | lines that do not express TP63 (39) vs lines expressing it (11) | 3.08× lower at baseline in the lines without TP63 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, ENSG00000241168, TYR; co-absent with the target |
| [[NRP2]] | C | NRP2 activity raises FYB1's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without NRP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[MAF]] | C | MAF activity raises FYB1's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without MAF | 0.081 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; co-absent with the target |
| [[SAMD9L]] | C | SAMD9L activity raises FYB1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without SAMD9L | 0.087 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22; co-absent with the target |
| [[GBP4]] | C | GBP4 activity raises FYB1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without GBP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 14, C 11. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL3]] | B | FYB1 activity raises APOL3's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.68× lower at baseline in the lines without FYB1 | 0.003 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[GBP2]] | B | FYB1 activity raises GBP2's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 3.68× lower at baseline in the lines without FYB1 | 0.004 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[XAF1]] | B | FYB1 activity raises XAF1's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.90× lower at baseline in the lines without FYB1 | 0.014 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[GBP3]] | B | FYB1 activity raises GBP3's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without FYB1 | 0.023 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[ESR1]] | B | FYB1 activity raises ESR1's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without FYB1 | 0.027 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[LINC02605]] | B | FYB1 activity raises LINC02605's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.40× lower at baseline in the lines without FYB1 | 0.028 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[KCNIP4]] | B | FYB1 activity raises KCNIP4's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without FYB1 | 0.044 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[HLA-F]] | B | FYB1 activity raises HLA-F's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.08× lower at baseline in the lines without FYB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[SAMD9]] | B | FYB1 activity raises SAMD9's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.85× lower at baseline in the lines without FYB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[IL7]] | B | FYB1 activity raises IL7's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without FYB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[CTSS]] | B | FYB1 activity raises CTSS's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.04× lower at baseline in the lines without FYB1 | 0.063 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[SLFN5]] | B | FYB1 activity raises SLFN5's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without FYB1 | 0.066 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, 22.6); signed map (40.7, 22.1). **Vector** length 40.3, 10.0% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +20.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | FYN binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:39,105,252-39,274,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLAP-130, FYB-120/130, ADAP; previously FYB |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: Signal regulatory protein family interactions; Generation of second messenger molecules; TCR signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O15117](https://www.uniprot.org/uniprotkb/O15117) (FYN-binding protein 1):

> Acts as an adapter protein of the FYN and LCP2 signaling cascades in T-cells (By similarity). May play a role in linking T-cell signaling to remodeling of the actin cytoskeleton. Modulates the expression of IL2 (By similarity). Involved in platelet activation (By similarity). Prevents the degradation of SKAP1 and SKAP2. May be involved in high affinity immunoglobulin epsilon receptor signaling in mast cells (By similarity).

**Summary**, from NCBI Gene [2533](https://www.ncbi.nlm.nih.gov/gene/2533):

> The protein encoded by this gene is an adapter for the FYN protein and LCP2 signaling cascades in T-cells. The encoded protein is involved in platelet activation and controls the expression of interleukin-2. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:4036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4036) · Entrez [2533](https://www.ncbi.nlm.nih.gov/gene/2533) · UniProt [O15117](https://www.uniprot.org/uniprotkb/O15117) · Ensembl [ENSG00000082074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082074)

## Data

Gene col 1334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1334); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1334]; `tensor/DDL_lfc|DDL_z.npy` [1334]; `embed/gene_vectors.npy` [1334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1334 or target_col == 1334). Every well: [[FYB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FYB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
