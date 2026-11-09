---
symbol: "BCHE"
type: "gene"
col: 3531
ensembl_id: "ENSG00000114200"
name: "butyrylcholinesterase"
location: "3q26.1"
module: 19
arm: "+"
pooled_cpm: 21.37
n_lines_expressing: 15
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 35
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# BCHE

*butyrylcholinesterase* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.34× (z +16.4, q 0e+00, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +11.6, q 1e-28, up in 12 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.723× (z -3.8, q 0.086, down in 3 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.125×; ⚠ cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0913×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.274×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.371×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 0.225×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRISPLD1]] (+0.65, fdr 7e-06), [[ASXL3]] (+0.65, fdr 2e-05), [[TENM1]] (+0.65, fdr 8e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MTMR7]] → it (grade B ⚠); 35 go from it, the strongest it → [[MEF2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.34×** | +16.4 | 0e+00 | 3/10 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +11.8 | 1e-29 | 4/13 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +11.6 | 1e-28 | 12/13 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.7 | 3e-16 | 1/13 (NCI-H1792) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.2 | 4e-14 | 3/11 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +7.0 | 3e-10 | 12/13 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.6 | 2e-06 | 4/13 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +5.5 | 2e-06 | 10/13 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.0 | 4e-05 | 1/13 (HS-578T) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.9 | 4e-05 | 3/12 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.9 | 6e-05 | 10/13 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.9 | 6e-05 | 5/9 (A-427, C32, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.53×** | +4.8 | 8e-05 | 0/13 | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 6/13 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.007 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.009 | 0/13 | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.022 | 0/13 | inconsistent across doses | noisy plate (z scaled) |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.023 | 0/13 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.026 | 0/13 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.035 | 5/11 (NCI-H1792, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.037 | 4/13 (SK-MEL-2, C32, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.125×; ⚠ cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0913×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.274×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.371×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 0.225×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -3.8 | 0.086 | 3/13 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.741× | -3.5 | 0.12 | 7/13 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.733× | -3.4 | 0.12 | 0/13 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.753× | -3.3 | 0.12 | 6/13 (NCI-H460, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.755× | -3.3 | 0.12 | 1/13 (HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 62.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.3) |
| [[A-427 (line)]] | wt | 603 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.371× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 2 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.225× (z -9.0) |
| [[C32 (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 54.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.14× (z +8.8) | — |
| [[A-172 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRISPLD1]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.65 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TENM1]] | +0.65 | +0.63 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[CSRNP3]] | +0.63 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Neuronal System |
| [[SLITRK4]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Neuronal System |
| [[CDH7]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SLITRK5]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[LINC01035]] | +0.60 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[LIN7A]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 | pathway: Neuronal System |
| [[WDR17]] | +0.58 | +0.36 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTMR7]] | B | MTMR7 activity raises BCHE's level | lines that do not express MTMR7 (16) vs lines expressing it (34) | 3.60× lower at baseline in the lines without MTMR7 | 0.052 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[TXLNGY]] | C | TXLNGY activity raises BCHE's level | lines that do not express TXLNGY (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without TXLNGY | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises BCHE's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.91× lower at baseline in the lines without PCDH18 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises BCHE's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 4.73× lower at baseline in the lines without CSMD3 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises BCHE's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.12× lower at baseline in the lines without EPHA5 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises BCHE's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without EPHA5-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[GASK1B]] | C | GASK1B activity raises BCHE's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without GASK1B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[CSRNP3]] | C | CSRNP3 activity raises BCHE's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without CSRNP3 | 0.041 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[NCAM2]] | C | NCAM2 activity raises BCHE's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 3.80× lower at baseline in the lines without NCAM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises BCHE's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.59× lower at baseline in the lines without LINC01885 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises BCHE's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 4.16× lower at baseline in the lines without CDH12 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises BCHE's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 4.21× lower at baseline in the lines without LIN7A | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 4, C 31. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | BCHE activity raises MEF2C's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.66× lower at baseline in the lines without BCHE | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[MTMR7]] | B | BCHE activity raises MTMR7's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.45× lower at baseline in the lines without BCHE | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[BCL11A]] | B | BCHE activity raises BCL11A's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without BCHE | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[SYT1]] | B | BCHE activity raises SYT1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without BCHE | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[PCDH9]] | C | BCHE activity raises PCDH9's level | lines that do not express BCHE (35) vs lines expressing it (15) | 6.09× lower at baseline in the lines without BCHE | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CSRNP3]] | C | BCHE activity raises CSRNP3's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.49× lower at baseline in the lines without BCHE | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[NCAM2]] | C | BCHE activity raises NCAM2's level | lines that do not express BCHE (35) vs lines expressing it (15) | 7.13× lower at baseline in the lines without BCHE | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[LINC01885]] | C | BCHE activity raises LINC01885's level | lines that do not express BCHE (35) vs lines expressing it (15) | 5.82× lower at baseline in the lines without BCHE | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[SLC6A15]] | C | BCHE activity raises SLC6A15's level | lines that do not express BCHE (35) vs lines expressing it (15) | 7.11× lower at baseline in the lines without BCHE | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[EPHA3]] | C | BCHE activity raises EPHA3's level | lines that do not express BCHE (35) vs lines expressing it (15) | 6.28× lower at baseline in the lines without BCHE | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[EPHA5]] | C | BCHE activity raises EPHA5's level | lines that do not express BCHE (35) vs lines expressing it (15) | 5.10× lower at baseline in the lines without BCHE | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[SNCA]] | C | BCHE activity raises SNCA's level | lines that do not express BCHE (35) vs lines expressing it (15) | 5.25× lower at baseline in the lines without BCHE | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.7, 35.2); signed map (42.1, 37.7). **Vector** length 48.7, 15.9% of its response variance represented; |z| ≥ 3 in 358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +5.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.7 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | butyrylcholinesterase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:165,772,904-165,837,462 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E1; previously CHE1, CHE2 |
| Gene groups (HGNC) | Cholinesterase family |
| Reactome | 11 pathways, smallest: Neurotransmitter clearance; Synthesis, secretion, and deacylation of Ghrelin; Aspirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P06276](https://www.uniprot.org/uniprotkb/P06276) (Cholinesterase):

> Esterase with broad substrate specificity. Contributes to the inactivation of the neurotransmitter acetylcholine. Can degrade neurotoxic organophosphate esters.

**Summary**, from NCBI Gene [590](https://www.ncbi.nlm.nih.gov/gene/590):

> This gene encodes a cholinesterase enzyme and member of the type-B carboxylesterase/lipase family of proteins. The encoded enzyme exhibits broad substrate specificity and is involved in the detoxification of poisons including organophosphate nerve agents and pesticides, and the metabolism of drugs including cocaine, heroin and aspirin. Humans homozygous for certain mutations in this gene exhibit prolonged apnea after administration of the muscle relaxant succinylcholine. [provided by RefSeq, …

**Accessions** — [HGNC:983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:983) · Entrez [590](https://www.ncbi.nlm.nih.gov/gene/590) · UniProt [P06276](https://www.uniprot.org/uniprotkb/P06276) · Ensembl [ENSG00000114200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114200)

## Data

Gene col 3531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3531); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3531]; `tensor/DDL_lfc|DDL_z.npy` [3531]; `embed/gene_vectors.npy` [3531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3531 or target_col == 3531). Every well: [[BCHE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCHE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
