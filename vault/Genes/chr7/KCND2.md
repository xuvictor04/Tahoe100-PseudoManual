---
symbol: "KCND2"
type: "gene"
col: 11533
ensembl_id: "ENSG00000184408"
name: "potassium voltage-gated channel subfamily D member 2"
location: "7q31.31"
module: 9
arm: "+"
pooled_cpm: 15.11
n_lines_expressing: 18
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 15
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KCND2

*potassium voltage-gated channel subfamily D member 2* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 16.7× (z +36.3, q 0e+00, up in 13 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.190×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.198×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.232×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.383×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01695]] (+0.74, fdr 7e-06), [[GRIK1]] (+0.66, fdr 1e-05), [[RALYL]] (+0.66, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC02492]] → it (grade B ⚠); 15 go from it, the strongest it → [[CACNG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **16.7×** | +36.3 | 0e+00 | 13/14 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.16×** | +23.5 | 0e+00 | 9/13 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.75×** | +20.1 | 0e+00 | 10/15 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.68×** | +14.1 | 5e-43 | 10/14 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.87×** | +13.9 | 6e-42 | 11/14 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.45×** | +13.6 | 3e-40 | 8/13 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.23×** | +10.7 | 7e-25 | 11/15 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +10.6 | 4e-24 | 3/7 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +9.4 | 3e-19 | 4/8 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.50×** | +8.4 | 3e-15 | 7/14 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.7 | 1e-04 | 8/14 (A498, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 3e-04 | 5/14 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.0 | 0.003 | 2/14 (BT-474, SW 900) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.005 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.7 | 0.010 | 1/5 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.010 | 5/14 (A498, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +3.6 | 0.010 | 6/15 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.011 | 4/15 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.013 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.013 | 7/14 (SHP-77, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11533.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.190×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.198×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.232×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.383×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.690× | -3.4 | 0.41 | 4/15 (SHP-77, C32, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 5 µM |  | 0.786× | -3.1 | 0.56 | 2/15 (hTERT-HPNE, SHP-77) | rises with dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 114× (z +28.4) | — |
| [[SHP-77 (line)]] | alt | 607 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -11.8) |
| [[A-172 (line)]] | wt | 7.10 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 255× (z +20.5) | — |
| [[C32 (line)]] | wt | 4.80 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 128× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 9.92 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 8.76 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 4.39 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 26.5× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 3.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +8.7) | — |
| [[A-427 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01695]] | +0.74 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.66 | +0.65 / +0.51 | both halves | 1e-05 | pathway: Neuronal System |
| [[RALYL]] | +0.66 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[KHDRBS2]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[LRFN2]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 | pathway: Neuronal System |
| [[ABCA13]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SCN2A]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 | pathway: Cardiac conduction; STRING 607 |
| [[SYT4]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NAALADL2-AS2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[VENTXP1]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SRRM4]] | +0.60 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[GLRA3]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 | pathway: Neuronal System |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02492]] | B | LINC02492 activity raises KCND2's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without LINC02492 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[CALCA]] | C | CALCA activity raises KCND2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 5.78× lower at baseline in the lines without CALCA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises KCND2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.48× lower at baseline in the lines without SYT4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[PRUNE2]] | C | PRUNE2 activity raises KCND2's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PRUNE2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises KCND2's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 3.28× lower at baseline in the lines without LINC01320 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[PDZRN3]] | C | PDZRN3 activity raises KCND2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.60× lower at baseline in the lines without PDZRN3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises KCND2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.08× lower at baseline in the lines without RIT2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[H19]] | C | H19 activity raises KCND2's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.50× lower at baseline in the lines without H19 | 0.020 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises KCND2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.27× lower at baseline in the lines without KCNB2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises KCND2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.89× lower at baseline in the lines without ASCL1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[CGA]] | C | CGA activity raises KCND2's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.17× lower at baseline in the lines without CGA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises KCND2's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.91× lower at baseline in the lines without AK4P3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG2]] | B | KCND2 activity raises CACNG2's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 2.05× lower at baseline in the lines without KCND2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[LINC00578]] | B | KCND2 activity raises LINC00578's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.45× lower at baseline in the lines without KCND2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[SLC7A8]] | B | KCND2 activity raises SLC7A8's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without KCND2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[PPARGC1A]] | B | KCND2 activity raises PPARGC1A's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without KCND2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[XKR4]] | B | KCND2 activity raises XKR4's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without KCND2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[GRIA4]] | B | KCND2 activity raises GRIA4's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.64× lower at baseline in the lines without KCND2 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[UNC80]] | B | KCND2 activity raises UNC80's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.61× lower at baseline in the lines without KCND2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[NAALADL2-AS2]] | C | KCND2 activity raises NAALADL2-AS2's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without KCND2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |
| [[PDZRN3]] | C | KCND2 activity raises PDZRN3's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 2.47× lower at baseline in the lines without KCND2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |
| [[PCSK1]] | C | KCND2 activity raises PCSK1's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.96× lower at baseline in the lines without KCND2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |
| [[LINC01320]] | C | KCND2 activity raises LINC01320's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.96× lower at baseline in the lines without KCND2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |
| [[PRUNE2]] | C | KCND2 activity raises PRUNE2's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without KCND2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.5, 35.4); signed map (43.3, 33.0). **Vector** length 46.8, 13.7% of its response variance represented; |z| ≥ 3 in 336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +20.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +36.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily D member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:120,273,175-120,750,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv4.2, RK5, KIAA1044 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 6 pathways, smallest: Phase 1 - inactivation of fast Na+ channels; Voltage gated Potassium channels; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZV8](https://www.uniprot.org/uniprotkb/Q9NZV8) (A-type voltage-gated potassium channel KCND2):

> Voltage-gated potassium channel that mediates transmembrane potassium transport in excitable membranes, primarily in the brain. Mediates the major part of the dendritic A-type current I(SA) in brain neurons (By similarity). This current is activated at membrane potentials that are below the threshold for action potentials. It regulates neuronal excitability, prolongs the latency before the first spike in a series of action potentials, regulates the frequency of repetitive action potential …

**Summary**, from NCBI Gene [3751](https://www.ncbi.nlm.nih.gov/gene/3751):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. Four sequence-related potassium channel genes - shaker, shaw, shab, and shal - have been identified in Drosophila, and each has been shown to have …

**Accessions** — [HGNC:6238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6238) · Entrez [3751](https://www.ncbi.nlm.nih.gov/gene/3751) · UniProt [Q9NZV8](https://www.uniprot.org/uniprotkb/Q9NZV8) · Ensembl [ENSG00000184408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184408)

## Data

Gene col 11533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11533); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11533]; `tensor/DDL_lfc|DDL_z.npy` [11533]; `embed/gene_vectors.npy` [11533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11533 or target_col == 11533). Every well: [[KCND2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCND2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
