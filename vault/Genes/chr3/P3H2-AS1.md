---
symbol: "P3H2-AS1"
type: "gene"
col: 13483
ensembl_id: "ENSG00000225764"
name: "P3H2 antisense RNA 1"
location: "3q28"
module: 19
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 20
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# P3H2-AS1

*P3H2 antisense RNA 1* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.79× (z +11.3, q 6e-27, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.22× (z +8.1, q 8e-14, up in 6 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.541× (z -4.2, q 0.016, down in 9 of 16 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Berberine (chloride hydrate) (drug)]] 5 µM: 0.714× (z -3.5, q 0.097, down in 1 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0430×, NCI-H460 0.0932×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.0832×, LoVo 0.130×; ⚠ cell-cycle shift, explains ~47% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.149×, A549 0.0402×; ⚠ cell-cycle shift, explains ~77% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.275×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPDYE10]] (+0.74, fdr 7e-06), [[GTF2I-AS1]] (+0.71, fdr 7e-06), [[NCKAP5-AS2]] (+0.68, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[P3H2]] → it (grade C ⚠); 9 go from it, the strongest it → [[PCOLCE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.79×** | +11.3 | 6e-27 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.98×** | +11.2 | 2e-26 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +8.1 | 8e-14 | 6/13 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +6.2 | 7e-08 | 7/16 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +5.3 | 1e-05 | 1/6 (A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +5.0 | 6e-05 | 1/7 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +4.7 | 3e-04 | 2/5 (LoVo, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.30×** | +4.3 | 0.001 | 2/7 (LoVo, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.29×** | +4.3 | 0.001 | 1/6 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.006 | 1/16 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.7 | 0.011 | 1/7 (A549) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.014 | 4/14 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.63×** | +3.5 | 0.018 | 3/8 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +3.5 | 0.019 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.019 | 1/15 (A-427) | top dose only | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.62×** | +3.5 | 0.019 | 1/7 (A549) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +3.4 | 0.021 | 3/8 (LoVo, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.048 | 0/9 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.049 | 3/10 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +2.9 | 0.091 | 4/13 (PANC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13483.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0430×, NCI-H460 0.0932×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.0832×, LoVo 0.130×; ⚠ cell-cycle shift, explains ~47% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.149×, A549 0.0402×; ⚠ cell-cycle shift, explains ~77% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.275×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.541×** | -4.2 | 0.016 | 9/16 (NCI-H460, A498, …) | two highest doses |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.714×** | -3.5 | 0.097 | 1/16 (PANC-1) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.621×** | -3.5 | 0.097 | 8/16 (A549, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.6) |
| [[LoVo (line)]] | wt | 7.08 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0430× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 8.07 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -8.8) ⚠ toxic |
| [[A549 (line)]] | wt | 2.85 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0402× (z -9.2) ⚠ cell-cycle shift, explains ~77% of this change |
| [[PANC-1 (line)]] | alt | 3.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0365× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.505 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPDYE10]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GTF2I-AS1]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 | same gene group |
| [[NCKAP5-AS2]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 | same gene group |
| [[P3H2]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GLP2R]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.64 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[PAX7]] | +0.62 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[COL4A6]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CHL1]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SLITRK4]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[PDE1A]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[BASP1-AS1]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 | same gene group |
| [[LINC03000]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H2]] | C | P3H2 activity raises P3H2-AS1's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without P3H2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises P3H2-AS1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.44× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[SCARA5]] | C | SCARA5 activity raises P3H2-AS1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.52× lower at baseline in the lines without SCARA5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises P3H2-AS1's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without COL5A2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[CDH19]] | C | CDH19 activity raises P3H2-AS1's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 2.09× lower at baseline in the lines without CDH19 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises P3H2-AS1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without GLP2R | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises P3H2-AS1's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without NCKAP5-AS2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises P3H2-AS1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.94× lower at baseline in the lines without GTF2I-AS1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises P3H2-AS1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.60× lower at baseline in the lines without GSG1L2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises P3H2-AS1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.12× lower at baseline in the lines without LINC03000 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises P3H2-AS1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 1.73× lower at baseline in the lines without C5orf46 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises P3H2-AS1's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 2.29× lower at baseline in the lines without LINC01508 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCOLCE2]] | B | P3H2-AS1 activity raises PCOLCE2's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.71× lower at baseline in the lines without P3H2-AS1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3 |
| [[DCLK2]] | B | P3H2-AS1 activity raises DCLK2's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without P3H2-AS1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3 |
| [[CYP1B1-AS1]] | B | P3H2-AS1 activity raises CYP1B1-AS1's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without P3H2-AS1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3 |
| [[P3H2]] | C | P3H2-AS1 activity raises P3H2's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 6.62× lower at baseline in the lines without P3H2-AS1 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[SPINK13]] | C | P3H2-AS1 activity raises SPINK13's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without P3H2-AS1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[COL5A2]] | C | P3H2-AS1 activity raises COL5A2's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 3.34× lower at baseline in the lines without P3H2-AS1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[LRRC63]] | C | P3H2-AS1 activity raises LRRC63's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without P3H2-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[BASP1-AS1]] | C | P3H2-AS1 activity raises BASP1-AS1's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without P3H2-AS1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[RSPO3]] | C | P3H2-AS1 activity raises RSPO3's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without P3H2-AS1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, 37.0); signed map (42.1, 43.7). **Vector** length 37.3, 9.41% of its response variance represented; |z| ≥ 3 in 366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -1.2 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.0 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | P3H2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q28 — chr3:190,120,944-190,150,162 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LEPREL1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40886) · Entrez [101929152](https://www.ncbi.nlm.nih.gov/gene/101929152) · Ensembl [ENSG00000225764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225764)

## Data

Gene col 13483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13483); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13483]; `tensor/DDL_lfc|DDL_z.npy` [13483]; `embed/gene_vectors.npy` [13483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13483 or target_col == 13483). Every well: [[P3H2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P3H2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
