---
symbol: "EPHA5"
type: "gene"
col: 6967
ensembl_id: "ENSG00000145242"
name: "EPH receptor A5"
location: "4q13.1-q13.2"
module: 9
arm: "+"
pooled_cpm: 24.8
n_lines_expressing: 20
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 23
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# EPHA5

*EPH receptor A5* — 4q13.1-q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.07× (z +13.3, q 1e-37, up in 3 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +12.5, q 2e-33, up in 13 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.290×, NCI-H2030 0.377×, NCI-H460 0.316×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.0822×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.198×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.321×); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.352×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA5-AS1]] (+0.78, fdr 7e-06, ⚠ same locus), [[CDH10]] (+0.72, fdr 7e-06), [[CRISPLD1]] (+0.72, fdr 7e-06), [[PCDH9]] (+0.69, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TENM3-AS1]] → it (grade B ⚠); 23 go from it, the strongest it → [[SYT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +13.3 | 1e-37 | 3/14 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +12.5 | 2e-33 | 13/18 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.5 | 2e-28 | 5/17 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +10.5 | 2e-23 | 12/18 (NCI-H1792, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +10.0 | 1e-21 | 2/11 (J82, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.4 | 6e-15 | 9/16 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +6.2 | 3e-08 | 9/17 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 5e-08 | 10/18 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.0 | 1e-07 | 2/13 (HS-578T, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +5.8 | 4e-07 | 13/18 (J82, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +5.3 | 6e-06 | 10/16 (A-427, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.55×** | +5.0 | 3e-05 | 12/18 (hTERT-HPNE, C32, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.9 | 4e-05 | 1/18 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +4.7 | 1e-04 | 10/18 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 1e-04 | 8/18 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +4.6 | 2e-04 | 10/18 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +4.4 | 4e-04 | 8/16 (NCI-H23, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.001 | 9/16 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.003 | 8/17 (hTERT-HPNE, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.003 | 7/18 (NCI-H460, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.290×, NCI-H2030 0.377×, NCI-H460 0.316×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.0822×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.198×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.321×); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.352×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.721× | -3.6 | 0.19 | 1/17 (CHP-212) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.773× | -3.1 | 0.64 | 6/17 (NCI-H23, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 314 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0822× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 64.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 70.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[C32 (line)]] | wt | 8.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +11.8) | — |
| [[H4 (line)]] | wt | 60.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +14.2) | — |
| [[HS-578T (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +11.9) | — |
| [[J82 (line)]] | alt | 9.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.26× (z +10.3) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.3) |
| [[SW 1088 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA5-AS1]] | +0.78 | +0.74 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CDH10]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CRISPLD1]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[PCDH9]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[DMD]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NCAM2]] | +0.68 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MIR99AHG]] | +0.67 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[UNC5C]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[CTNNA2]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ERBB4]] | +0.64 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[FMN2]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises EPHA5's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without TENM3-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises EPHA5's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 7.30× lower at baseline in the lines without EPHA5-AS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises EPHA5's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 6.73× lower at baseline in the lines without TRPC4 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises EPHA5's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 6.21× lower at baseline in the lines without SCN3A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[HMCN1]] | C | HMCN1 activity raises EPHA5's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 5.38× lower at baseline in the lines without HMCN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[FAM133A]] | C | FAM133A activity raises EPHA5's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 5.35× lower at baseline in the lines without FAM133A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises EPHA5's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 6.75× lower at baseline in the lines without CDH10 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises EPHA5's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.35× lower at baseline in the lines without FMN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises EPHA5's level | lines that do not express BCHE (35) vs lines expressing it (15) | 5.10× lower at baseline in the lines without BCHE | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[ROBO2]] | C | ROBO2 activity raises EPHA5's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.44× lower at baseline in the lines without ROBO2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[TMEM47]] | C | TMEM47 activity raises EPHA5's level | lines that do not express TMEM47 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without TMEM47 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNE4, ENSG00000280241, ENSG00000225649; co-absent with the target |
| [[CACNB2]] | C | CACNB2 activity raises EPHA5's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 4.33× lower at baseline in the lines without CACNB2 | 0.037 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 1, C 22. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT1]] | B | EPHA5 activity raises SYT1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without EPHA5 | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4 |
| [[EPHA5-AS1]] | C | EPHA5 activity raises EPHA5-AS1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 3.30× lower at baseline in the lines without EPHA5 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[TRPC4]] | C | EPHA5 activity raises TRPC4's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.83× lower at baseline in the lines without EPHA5 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[HMCN1]] | C | EPHA5 activity raises HMCN1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 5.58× lower at baseline in the lines without EPHA5 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[ANGPT1]] | C | EPHA5 activity raises ANGPT1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.50× lower at baseline in the lines without EPHA5 | 0.011 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CACNB2]] | C | EPHA5 activity raises CACNB2's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without EPHA5 | 0.030 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[BCHE]] | C | EPHA5 activity raises BCHE's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.12× lower at baseline in the lines without EPHA5 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CD36]] | C | EPHA5 activity raises CD36's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without EPHA5 | 0.033 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CPED1]] | C | EPHA5 activity raises CPED1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without EPHA5 | 0.034 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[PCDH9]] | C | EPHA5 activity raises PCDH9's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.39× lower at baseline in the lines without EPHA5 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[TMEM47]] | C | EPHA5 activity raises TMEM47's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without EPHA5 | 0.039 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[SNCA]] | C | EPHA5 activity raises SNCA's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 5.58× lower at baseline in the lines without EPHA5 | 0.040 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, 32.9); signed map (40.4, 35.0). **Vector** length 67.6, 22.1% of its response variance represented; |z| ≥ 3 in 520 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +12.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.1-q13.2 — chr4:65,319,563-65,670,495 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hek7, TYRO4, CEK7, EHK1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P54756](https://www.uniprot.org/uniprotkb/P54756) (Ephrin type-A receptor 5):

> Receptor tyrosine kinase which binds promiscuously GPI-anchored ephrin-A family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Among GPI-anchored ephrin-A ligands, EFNA5 most probably constitutes the cognate/functional ligand for EPHA5. Functions as …

**Summary**, from NCBI Gene [2044](https://www.ncbi.nlm.nih.gov/gene/2044):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their …

**Accessions** — [HGNC:3389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3389) · Entrez [2044](https://www.ncbi.nlm.nih.gov/gene/2044) · UniProt [P54756](https://www.uniprot.org/uniprotkb/P54756) · Ensembl [ENSG00000145242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145242)

## Data

Gene col 6967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6967); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6967]; `tensor/DDL_lfc|DDL_z.npy` [6967]; `embed/gene_vectors.npy` [6967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6967 or target_col == 6967). Every well: [[EPHA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
