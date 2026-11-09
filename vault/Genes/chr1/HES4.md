---
symbol: "HES4"
type: "gene"
col: 11998
ensembl_id: "ENSG00000188290"
name: "hes family bHLH transcription factor 4"
location: "1p36.33"
module: 4
arm: "-"
pooled_cpm: 15.36
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 18
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HES4

*hes family bHLH transcription factor 4* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.52× (z +7.0, q 1e-09, up in 32 of 44 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.32× (z +4.5, q 9e-04, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.241× (z -4.0, q 0.031, down in 29 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.203×; ⚠ cell-cycle shift, explains ~84% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 0.0931×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISG15]] (+0.68, fdr 7e-06, ⚠ same locus), [[PIM3]] (+0.68, fdr 7e-06), [[NEURL3]] (+0.67, fdr 7e-06), [[MIEN1]] (+0.65, fdr 1e-05); moves opposite to [[NUP155]] (-0.62, fdr 1e-05), [[TIMM21]] (-0.59, fdr 1e-05), [[CNOT7]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 18 go from it, the strongest it → [[SSBP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.52×** | +7.0 | 1e-09 | 32/44 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.25×** | +6.1 | 3e-07 | 35/43 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.85×** | +5.7 | 3e-06 | 37/41 (NCI-H460, SNU-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **2.37×** | +4.5 | 9e-04 | 33/41 (NCI-H460, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.32×** | +4.5 | 9e-04 | 32/43 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.20×** | +4.2 | 0.003 | 25/33 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.09×** | +4.0 | 0.006 | 28/43 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.017 | 25/44 (hTERT-HPNE, C-33 A, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.55×** | +3.6 | 0.020 | 34/42 (SNU-423, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.90×** | +3.3 | 0.049 | 16/27 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.203×; ⚠ cell-cycle shift, explains ~84% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 0.0931×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.241×** | -4.0 | 0.031 | 29/42 (C-33 A, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.517×** | -3.6 | 0.091 | 29/43 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.636×** | -3.5 | 0.091 | 24/44 (MIA PaCa-2, HCT15, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.554× | -3.2 | 0.18 | 25/43 (NCI-H460, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.341× | -3.1 | 0.22 | 21/43 (C-33 A, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.559× | -3.0 | 0.22 | 22/43 (HepG2/C3A, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.6 | 10 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 19.1× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 12.0× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +10.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H1573 (line)]] | alt | 4.08 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +11.4) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A498 (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +8.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +13.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0931× (z -8.8) |
| [[COLO 205 (line)]] | alt | 5.03 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +9.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[Hs 766T (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +9.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[LS 180 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.2) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.203× (z -9.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[Panc 03.27 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW1417 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +9.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A-172 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISG15]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 | ⚠ same locus (1.0 kb: neighbours can correlate without regulation) |
| [[PIM3]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.67 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[JUND]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.60 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RNF114]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[C15orf48]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[IER5L]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[HLA-B]] | +0.58 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PSME2]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RNF223]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SNHG9]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[TIMM21]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CNOT7]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ZNF384]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SUPT16H]] | -0.54 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[GFM2]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TSN]] | -0.53 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[IPO8]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[RNPS1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DNAAF5]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SMU1]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSBP3]] | C | HES4 activity strengthens SSBP3's drug response | lines that do not express HES4 (4) vs lines expressing it (43) | the lines without HES4 respond 0.51× as strongly (z diff +1.80); strongest at Belinostat 5 µM: 0.90x vs 2.09x (z diff +5.8) | 0.010 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5; target measured in part of the lines; artifact flags |
| cells under [[IQ 1 (drug)]] 5 µM | C | HES4 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.71× the cells of the other lines | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[AT7519 (drug)]] 5 µM | C | HES4 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.51× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | HES4 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.71× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Piroxicam (drug)]] 0.05 µM | C | HES4 activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.75× the cells of the other lines | 0.027 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Neratinib (drug)]] 0.05 µM | C | HES4 activity lowers the cells' numbers under Neratinib 0.05 µM (makes them more sensitive) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 1.36× the cells of the other lines | 0.046 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | HES4 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.79× the cells of the other lines | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[TUBB2B]] | C | HES4 activity lowers TUBB2B's level | lines that do not express HES4 (4) vs lines expressing it (46) | 4.61× higher at baseline in the lines without HES4 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[SSBP3]] | C | HES4 activity lowers SSBP3's level | lines that do not express HES4 (4) vs lines expressing it (46) | 2.23× higher at baseline in the lines without HES4 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | HES4 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.77× the cells of the other lines | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Sulfatinib (drug)]] 5 µM | C | HES4 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.74× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| cells under [[Bortezomib (drug)]] 0.5 µM | C | HES4 activity raises the cells' numbers under Bortezomib 0.5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.77× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (24.0, -2.6); signed map (-3.7, 13.9). **Vector** length 90.8, 28.9% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.7 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.7 | +6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.4 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -4.0 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | hes family bHLH transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:998,962-1,000,172 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHb42 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCC6](https://www.uniprot.org/uniprotkb/Q9HCC6) (Transcription factor HES-4):

> Transcriptional repressor. Binds DNA on N-box motifs: 5'-CACNAG-3' (By similarity).

**Summary**, from NCBI Gene [57801](https://www.ncbi.nlm.nih.gov/gene/57801):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in anterior/posterior pattern specification and negative regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24149) · Entrez [57801](https://www.ncbi.nlm.nih.gov/gene/57801) · UniProt [Q9HCC6](https://www.uniprot.org/uniprotkb/Q9HCC6) · Ensembl [ENSG00000188290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188290)

## Data

Gene col 11998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11998); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11998]; `tensor/DDL_lfc|DDL_z.npy` [11998]; `embed/gene_vectors.npy` [11998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11998 or target_col == 11998). Every well: [[HES4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HES4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
