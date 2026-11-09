---
symbol: "DGKB"
type: "gene"
col: 5846
ensembl_id: "ENSG00000136267"
name: "diacylglycerol kinase beta"
location: "7p21.2"
module: 9
arm: "+"
pooled_cpm: 9.08
n_lines_expressing: 27
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 20
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DGKB

*diacylglycerol kinase beta* — 7p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.45× (z +27.3, q 0e+00, up in 13 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.658× (z -4.0, q 0.035, down in 10 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.170×, A498 0.219×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.249×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.143×; ⚠ cell-cycle shift, explains ~23% of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (C32 0.0889×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NELL1]] (+0.79, fdr 7e-06), [[AGMO]] (+0.76, fdr 7e-06), [[LINC00578]] (+0.70, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.45×** | +27.3 | 0e+00 | 13/18 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.46×** | +14.3 | 4e-44 | 17/22 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.81×** | +12.8 | 2e-35 | 9/14 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +11.7 | 3e-29 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +9.3 | 2e-18 | 6/18 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +8.2 | 3e-14 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.5 | 4e-12 | 9/23 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +6.9 | 5e-10 | 8/16 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +6.6 | 2e-09 | 6/17 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.4 | 8e-09 | 7/24 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.5 | 4e-04 | 1/13 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.4 | 5e-04 | 1/12 (A-172) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.003 | 7/22 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.9 | 0.004 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.8 | 0.005 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.008 | 7/19 (A498, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.010 | 7/21 (A-172, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5846.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.170×, A498 0.219×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.249×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.143×; ⚠ cell-cycle shift, explains ~23% of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (C32 0.0889×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.658×** | -4.0 | 0.035 | 10/23 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.781× | -3.4 | 0.22 | 3/22 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.726× | -3.1 | 0.38 | 7/23 (SHP-77, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 283 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.0) |
| [[A-172 (line)]] | wt | 4.62 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 171× (z +20.5) | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.4) |
| [[C32 (line)]] | wt | 26.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0889× (z -9.1) |
| [[HS-578T (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +8.5) | — |
| [[KATO III (line)]] | alt | 3.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 2.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +10.0) | — |
| [[SW480 (line)]] | alt | 2.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +10.3) | — |
| [[A-427 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NELL1]] | +0.79 | +0.72 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[AGMO]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | STRING 732 |
| [[LINC00578]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[GRIK1]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[LRFN2]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[RIT2]] | +0.65 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[NYAP2]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[UNC80]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[XIRP2]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LINC01287]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DGKB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RIT2]] | B | RIT2 activity raises DGKB's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.43× lower at baseline in the lines without RIT2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[PRUNE2]] | B | PRUNE2 activity raises DGKB's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without PRUNE2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[CGA]] | B | CGA activity raises DGKB's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.37× lower at baseline in the lines without CGA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[CDH8]] | B | CDH8 activity raises DGKB's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without CDH8 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent |
| [[CALCA]] | C | CALCA activity raises DGKB's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.64× lower at baseline in the lines without CALCA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises DGKB's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.72× lower at baseline in the lines without SYT4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[AGMO]] | C | AGMO activity raises DGKB's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without AGMO | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises DGKB's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.00× lower at baseline in the lines without KCNB2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises DGKB's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.17× lower at baseline in the lines without AK4P3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises DGKB's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.56× lower at baseline in the lines without RUNX1T1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises DGKB's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without ASCL1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | DGKB activity raises SEMA6D's level | lines that do not express DGKB (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without DGKB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[CRB1]] | B | DGKB activity raises CRB1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without DGKB | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[COL21A1]] | B | DGKB activity raises COL21A1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without DGKB | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[GRIA4]] | B | DGKB activity raises GRIA4's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.57× lower at baseline in the lines without DGKB | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[UNC80]] | B | DGKB activity raises UNC80's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without DGKB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[SOX5]] | B | DGKB activity raises SOX5's level | lines that do not express DGKB (23) vs lines expressing it (27) | 3.34× lower at baseline in the lines without DGKB | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[SORCS1]] | B | DGKB activity raises SORCS1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without DGKB | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[DACH1]] | B | DGKB activity raises DACH1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without DGKB | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[RALYL]] | B | DGKB activity raises RALYL's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.74× lower at baseline in the lines without DGKB | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[MAP3K7CL]] | B | DGKB activity raises MAP3K7CL's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without DGKB | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[AGMO]] | C | DGKB activity raises AGMO's level | lines that do not express DGKB (23) vs lines expressing it (27) | 3.08× lower at baseline in the lines without DGKB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent; co-absent with the target |
| [[TSHZ2]] | C | DGKB activity raises TSHZ2's level | lines that do not express DGKB (23) vs lines expressing it (27) | 3.19× lower at baseline in the lines without DGKB | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.8, 38.2); signed map (45.5, 33.1). **Vector** length 49.8, 11.1% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +27.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.2 — chr7:14,145,049-14,974,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0718, DGK, DGK-BETA; previously DAGK2 |
| Gene groups (HGNC) | EF-hand domain containing; Diacylglycerol kinase family |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6T7](https://www.uniprot.org/uniprotkb/Q9Y6T7) (Diacylglycerol kinase beta):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes (Probable). Has a higher activity with long-chain diacylglycerols like 1,2-di-(9Z-octadecenoyl)-sn-glycerol compared to 1,2-didecanoyl-sn-glycerol …

**Summary**, from NCBI Gene [1607](https://www.ncbi.nlm.nih.gov/gene/1607):

> Diacylglycerol kinases (DGKs) are regulators of the intracellular concentration of the second messenger diacylglycerol (DAG) and thus play a key role in cellular processes. Nine mammalian isotypes have been identified, which are encoded by separate genes. Mammalian DGK isozymes contain a conserved catalytic (kinase) domain and a cysteine-rich domain (CRD). The protein encoded by this gene is a diacylglycerol kinase, beta isotype. Several alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:2850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2850) · Entrez [1607](https://www.ncbi.nlm.nih.gov/gene/1607) · UniProt [Q9Y6T7](https://www.uniprot.org/uniprotkb/Q9Y6T7) · Ensembl [ENSG00000136267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136267)

## Data

Gene col 5846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5846); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5846]; `tensor/DDL_lfc|DDL_z.npy` [5846]; `embed/gene_vectors.npy` [5846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5846 or target_col == 5846). Every well: [[DGKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
