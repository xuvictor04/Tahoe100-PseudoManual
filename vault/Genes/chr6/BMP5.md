---
symbol: "BMP5"
type: "gene"
col: 3330
ensembl_id: "ENSG00000112175"
name: "bone morphogenetic protein 5"
location: "6p12.1"
module: 9
arm: "+"
pooled_cpm: 20.71
n_lines_expressing: 12
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 19
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# BMP5

*bone morphogenetic protein 5* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +7.9, q 1e-12, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.73× (z +6.5, q 1e-08, up in 7 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.590× (z -6.2, q 2e-07, down in 7 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP25]] (+0.75, fdr 7e-06), [[KLRC4-KLRK1]] (+0.73, fdr 7e-06), [[CDH10]] (+0.71, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 20 go from it, the strongest it → [[ADGRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +7.9 | 1e-12 | 1/8 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.0 | 5e-10 | 1/9 (NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +6.5 | 1e-08 | 7/10 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.68×** | +6.1 | 1e-07 | 2/10 (PANC-1, SW1417) | top dose only | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.77×** | +5.6 | 2e-06 | 8/10 (NCI-H23, PANC-1, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.00×** | +5.6 | 2e-06 | 8/10 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.4 | 4e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +5.4 | 4e-06 | 3/9 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.002 | 6/10 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.005 | 6/10 (NCI-H23, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +3.8 | 0.007 | 5/10 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.7 | 0.009 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.009 | 5/10 (NCI-H23, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.011 | 4/10 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.5 | 0.020 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.023 | 8/10 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.033 | 2/10 (SW1417, NCI-H1573) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.590×** | -6.2 | 2e-07 | 7/10 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -5.1 | 1e-04 | 6/10 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.591×** | -4.4 | 0.002 | 6/10 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.611×** | -4.1 | 0.006 | 1/10 (SHP-77) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.580×** | -4.0 | 0.007 | 5/10 (SW480, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.622×** | -3.9 | 0.008 | 7/10 (SW480, SHP-77, …) | two highest doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.628×** | -3.9 | 0.009 | 5/10 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.643×** | -3.7 | 0.016 | 7/10 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.624×** | -3.6 | 0.018 | 1/10 (PANC-1) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.659×** | -3.5 | 0.028 | 0/10 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.632×** | -3.4 | 0.036 | 7/10 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.633×** | -3.4 | 0.036 | 8/10 (SW480, SHP-77, …) | two highest doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.659×** | -3.3 | 0.036 | 5/10 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.636×** | -3.3 | 0.036 | 4/10 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.670×** | -3.1 | 0.075 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 160 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 110 | 2 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.58× (z +13.8) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 7.89× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -9.7) |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0972× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.137× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -14.5) |
| [[PANC-1 (line)]] | alt | 12.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +11.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.5× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.108× (z -12.0) |
| [[A-172 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP25]] | +0.75 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[KLRC4-KLRK1]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[CDH10]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[KLRC3]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[KLRC2]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ADARB2]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CSRNP3]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[RMST]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SEMA3D]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CRISPLD1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers BMP5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[MLPH]] | B | MLPH activity lowers BMP5's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.65× higher at baseline in the lines without MLPH | 0.070 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ADGRL2]] | B | ADGRL2 activity raises BMP5's level | lines that do not express ADGRL2 (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without ADGRL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAM23, SCN9A, WDR17 |
| [[NELL2]] | C | NELL2 activity raises BMP5's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 3.01× lower at baseline in the lines without NELL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises BMP5's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 4.47× lower at baseline in the lines without CDH10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[RAB3C]] | C | RAB3C activity raises BMP5's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without RAB3C | 0.012 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[LINC02211]] | C | LINC02211 activity raises BMP5's level | lines that do not express LINC02211 (38) vs lines expressing it (12) | 3.84× lower at baseline in the lines without LINC02211 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02945, LINC01035, PSG5; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises BMP5's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 3.63× lower at baseline in the lines without PHYHIPL | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[ADARB2]] | C | ADARB2 activity raises BMP5's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 4.21× lower at baseline in the lines without ADARB2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises BMP5's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.80× lower at baseline in the lines without JAKMIP2-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[SNCA]] | C | SNCA activity raises BMP5's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.73× lower at baseline in the lines without SNCA | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[NOTUM]] | C | NOTUM activity raises BMP5's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without NOTUM | 0.035 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 2, C 18. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRL2]] | B | BMP5 activity raises ADGRL2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 4.01× lower at baseline in the lines without BMP5 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3 |
| [[KCNMB2]] | B | BMP5 activity raises KCNMB2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without BMP5 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3 |
| [[NELL2]] | C | BMP5 activity raises NELL2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 3.89× lower at baseline in the lines without BMP5 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[ADARB2]] | C | BMP5 activity raises ADARB2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 5.12× lower at baseline in the lines without BMP5 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[RAB3C]] | C | BMP5 activity raises RAB3C's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 3.07× lower at baseline in the lines without BMP5 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[CTNNA2]] | C | BMP5 activity raises CTNNA2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 6.31× lower at baseline in the lines without BMP5 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[CARD18]] | C | BMP5 activity raises CARD18's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 3.52× lower at baseline in the lines without BMP5 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[PCSK1]] | C | BMP5 activity raises PCSK1's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.77× lower at baseline in the lines without BMP5 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[PHYHIPL]] | C | BMP5 activity raises PHYHIPL's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.46× lower at baseline in the lines without BMP5 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[RMST]] | C | BMP5 activity raises RMST's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without BMP5 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[GABRG2]] | C | BMP5 activity raises GABRG2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without BMP5 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[LINC02211]] | C | BMP5 activity raises LINC02211's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 1.68× lower at baseline in the lines without BMP5 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, 34.1); signed map (45.8, 35.7). **Vector** length 62.9, 29.0% of its response variance represented; |z| ≥ 3 in 384 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.1 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +5.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.3 | -6.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -4.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:55,753,653-55,875,590 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P22003](https://www.uniprot.org/uniprotkb/P22003) (Bone morphogenetic protein 5):

> Growth factor of the TGF-beta superfamily that plays essential roles in many developmental processes, including cartilage and bone formation or neurogenesis. Initiates the canonical BMP signaling cascade by associating with type I receptor BMPR1A and type II receptor BMPR2. In turn, BMPR1A propagates signal by phosphorylating SMAD1/5/8 that travel to the nucleus and act as activators and repressors of transcription of target genes. Can also signal through non-canonical pathway such as MAPK p38 …

**Summary**, from NCBI Gene [653](https://www.ncbi.nlm.nih.gov/gene/653):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer, which plays a role in bone and cartilage development. Polymorphisms in this gene may be associated with …

**Accessions** — [HGNC:1072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1072) · Entrez [653](https://www.ncbi.nlm.nih.gov/gene/653) · UniProt [P22003](https://www.uniprot.org/uniprotkb/P22003) · Ensembl [ENSG00000112175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112175)

## Data

Gene col 3330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3330); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3330]; `tensor/DDL_lfc|DDL_z.npy` [3330]; `embed/gene_vectors.npy` [3330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3330 or target_col == 3330). Every well: [[BMP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
