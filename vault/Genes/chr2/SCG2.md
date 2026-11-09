---
symbol: "SCG2"
type: "gene"
col: 10188
ensembl_id: "ENSG00000171951"
name: "secretogranin II"
location: "2q36.1"
module: 9
arm: "+"
pooled_cpm: 17.34
n_lines_expressing: 24
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 14
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SCG2

*secretogranin II* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.60× (z +15.0, q 0e+00, up in 11 of 14 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.86× (z +7.6, q 3e-12, up in 11 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.566× (z -4.6, q 0.003, down in 6 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.205×, CHP-212 0.303×; ⚠ cell-cycle shift, explains ~44% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.285×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.244×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0685×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0870×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADARB2]] (+0.63, fdr 7e-06), [[GRIK1]] (+0.62, fdr 1e-05), [[SCN3A]] (+0.59, fdr 1e-05); moves opposite to [[SVIL-AS1-1]] (-0.51, fdr 4e-05), [[ELMOD3]] (-0.47, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[OFCC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **5.60×** | +15.0 | 0e+00 | 11/14 (HS-578T, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.66×** | +12.0 | 7e-31 | 11/17 (C32, HS-578T, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.10×** | +11.8 | 6e-30 | 8/11 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +10.0 | 3e-21 | 10/12 (hTERT-HPNE, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +7.6 | 3e-12 | 11/20 (C32, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.44×** | +7.5 | 8e-12 | 11/19 (NCI-H460, C32, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.92×** | +5.7 | 1e-06 | 10/21 (C32, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.89×** | +5.5 | 2e-06 | 10/19 (C32, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.85×** | +5.4 | 5e-06 | 8/18 (C32, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.8 | 8e-05 | 7/19 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.006 | 9/19 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.007 | 6/20 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.53×** | +3.7 | 0.009 | 5/19 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.7 | 0.009 | 2/9 (HOP62, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.020 | 9/21 (SHP-77, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.100 | 8/22 (NCI-H23, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10188.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.205×, CHP-212 0.303×; ⚠ cell-cycle shift, explains ~44% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.285×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.244×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0685×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0870×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.566×** | -4.6 | 0.003 | 6/21 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.647×** | -4.0 | 0.017 | 11/22 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.662×** | -3.6 | 0.063 | 3/20 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.662× | -3.3 | 0.13 | 1/20 (hTERT-HPNE) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.766× | -3.3 | 0.13 | 7/19 (KATO III, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.692× | -3.2 | 0.13 | 12/21 (SHP-77, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 433 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -13.7) |
| [[C32 (line)]] | wt | 4.84 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 49.0× (z +15.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HS-578T (line)]] | alt | 10.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0685× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.22× (z +10.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[CHP-212 (line)]] | wt | 251 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +10.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 5.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADARB2]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[GRIK1]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SCN3A]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PCSK1]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 | STRING 645 |
| [[PLEKHG2]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[FGF14]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PDE4B]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PCDH9]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SLITRK6]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[LYPD1]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NTRK3]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[UNC13A]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SVIL-AS1-1]] | -0.51 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[ELMOD3]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SCG2's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds |
| [[OFCC1]] | B | OFCC1 activity raises SCG2's level | lines that do not express OFCC1 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without OFCC1 | 0.090 | ⚠ within organs, on part of the lines; also absent: PDLIM3, CAMK4, GLRB; maybe low, not absent |
| [[PCSK1]] | C | PCSK1 activity raises SCG2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.59× lower at baseline in the lines without PCSK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises SCG2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.88× lower at baseline in the lines without CALCA | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[HGF]] | C | HGF activity raises SCG2's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.99× lower at baseline in the lines without HGF | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises SCG2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 7.44× lower at baseline in the lines without SYT4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises SCG2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.36× lower at baseline in the lines without RIT2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[CGA]] | C | CGA activity raises SCG2's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.69× lower at baseline in the lines without CGA | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises SCG2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.68× lower at baseline in the lines without KCNB2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises SCG2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 3.37× lower at baseline in the lines without CSMD3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises SCG2's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without RGS4 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[FRMPD4]] | C | FRMPD4 activity raises SCG2's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without FRMPD4 | 0.079 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OFCC1]] | B | SCG2 activity raises OFCC1's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without SCG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG |
| [[FRMPD4]] | C | SCG2 activity raises FRMPD4's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without SCG2 | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |
| [[NRXN1]] | C | SCG2 activity raises NRXN1's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without SCG2 | 0.037 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |
| [[PCSK1]] | C | SCG2 activity raises PCSK1's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without SCG2 | 0.042 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |
| [[GRIK2]] | C | SCG2 activity raises GRIK2's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.98× lower at baseline in the lines without SCG2 | 0.044 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |
| [[LINC02930]] | C | SCG2 activity raises LINC02930's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.51× lower at baseline in the lines without SCG2 | 0.065 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |
| [[CHGB]] | C | SCG2 activity raises CHGB's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without SCG2 | 0.085 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.0, 34.9); signed map (42.7, 31.9). **Vector** length 49.8, 11.6% of its response variance represented; |z| ≥ 3 in 476 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.8 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +5.7 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.7 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | secretogranin II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:223,596,940-223,602,361 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHGC, SgII, SN |
| Gene groups (HGNC) | Granins |
| Hallmark sets | HEDGEHOG_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P13521](https://www.uniprot.org/uniprotkb/P13521) (Secretogranin-2):

> Neuroendocrine protein of the granin family that regulates the biogenesis of secretory granules.

**Summary**, from NCBI Gene [7857](https://www.ncbi.nlm.nih.gov/gene/7857):

> The protein encoded by this gene is a member of the chromogranin/secretogranin family of neuroendocrine secretory proteins. Studies in rodents suggest that the full-length protein, secretogranin II, is involved in the packaging or sorting of peptide hormones and neuropeptides into secretory vesicles. The full-length protein is cleaved to produce the active peptide secretoneurin, which exerts chemotaxic effects on specific cell types, and EM66, whose function is unknown. [provided by RefSeq, Jul …

**Accessions** — [HGNC:10575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10575) · Entrez [7857](https://www.ncbi.nlm.nih.gov/gene/7857) · UniProt [P13521](https://www.uniprot.org/uniprotkb/P13521) · Ensembl [ENSG00000171951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171951)

## Data

Gene col 10188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10188); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10188]; `tensor/DDL_lfc|DDL_z.npy` [10188]; `embed/gene_vectors.npy` [10188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10188 or target_col == 10188). Every well: [[SCG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
