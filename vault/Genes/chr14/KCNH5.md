---
symbol: "KCNH5"
type: "gene"
col: 6367
ensembl_id: "ENSG00000140015"
name: "potassium voltage-gated channel subfamily H member 5"
location: "14q23.2"
module: 108
arm: "+"
pooled_cpm: 8.91
n_lines_expressing: 14
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 22
direction_downstream: 36
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# KCNH5

*potassium voltage-gated channel subfamily H member 5* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.96× (z +18.2, q 0e+00, up in 1 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.623× (z -4.4, q 0.005, down in 7 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 0.158×, C-33 A 0.128×, LOX-IMVI 0.188×, NCI-H1573 0.104×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0840×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.108×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.268×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.169×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF14]] (+0.76, fdr 7e-06), [[MGAT4C]] (+0.72, fdr 7e-06), [[CDH10]] (+0.70, fdr 7e-06).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 36 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.96×** | +18.2 | 0e+00 | 1/9 (NCI-H1573) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +11.1 | 5e-26 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.7 | 5e-20 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.92×** | +9.3 | 3e-18 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +8.2 | 3e-14 | 4/11 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.13×** | +7.1 | 2e-10 | 2/11 (AN3 CA, A-427) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +6.6 | 2e-09 | 5/10 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.6 | 2e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.4 | 5e-06 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.4 | 7e-04 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.007 | 2/10 (NCI-H1573, SHP-77) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.007 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.007 | 3/9 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.023 | 3/10 (H4, CHP-212, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.025 | 3/10 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.032 | 5/10 (SK-MEL-2, CHP-212, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.032 | 2/11 (NCI-H1573, SHP-77) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.047 | 0/9 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.073 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 0.158×, C-33 A 0.128×, LOX-IMVI 0.188×, NCI-H1573 0.104×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0840×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.108×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.268×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.169×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.623×** | -4.4 | 0.005 | 7/10 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.669×** | -3.8 | 0.046 | 8/10 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.680× | -3.3 | 0.16 | 0/10 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.24 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0797× (z -10.4) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.108× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 38.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.268× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0840× (z -13.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -10.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -8.6) |
| [[SHP-77 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF14]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MGAT4C]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MIR3171HG]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MIR99AHG]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ZFHX4]] | +0.65 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[CDH7]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SLITRK5]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 | pathway: Neuronal System |
| [[LINC02211]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ADGRB3]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SCN2A]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 2, C 20. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNH5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LSAMP]] | B | LSAMP activity raises KCNH5's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LSAMP | 0.077 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[CDH7]] | C | CDH7 activity raises KCNH5's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 6.23× lower at baseline in the lines without CDH7 | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises KCNH5's level | lines that do not express BCHE (35) vs lines expressing it (15) | 4.33× lower at baseline in the lines without BCHE | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises KCNH5's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 3.77× lower at baseline in the lines without CCDC144NL-AS1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[CADM2]] | C | CADM2 activity raises KCNH5's level | lines that do not express CADM2 (31) vs lines expressing it (19) | 4.33× lower at baseline in the lines without CADM2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000263551, KCNH5, KIF1A; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises KCNH5's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 6.41× lower at baseline in the lines without MIR99AHG | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[MIR4307HG]] | C | MIR4307HG activity raises KCNH5's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 2.70× lower at baseline in the lines without MIR4307HG | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[LINC02945]] | C | LINC02945 activity raises KCNH5's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 2.92× lower at baseline in the lines without LINC02945 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises KCNH5's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.75× lower at baseline in the lines without SRRM4 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises KCNH5's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 5.98× lower at baseline in the lines without ASCL1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[MARCHF1]] | C | MARCHF1 activity raises KCNH5's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 3.27× lower at baseline in the lines without MARCHF1 | 0.049 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 2, C 34. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | KCNH5 activity raises LSAMP's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.13× lower at baseline in the lines without KCNH5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D |
| [[MTMR7]] | B | KCNH5 activity raises MTMR7's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.47× lower at baseline in the lines without KCNH5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D |
| [[LIN28B]] | C | KCNH5 activity raises LIN28B's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 7.64× lower at baseline in the lines without KCNH5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[CADM2]] | C | KCNH5 activity raises CADM2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 8.60× lower at baseline in the lines without KCNH5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[NTNG1]] | C | KCNH5 activity raises NTNG1's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.38× lower at baseline in the lines without KCNH5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[ASXL3]] | C | KCNH5 activity raises ASXL3's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.68× lower at baseline in the lines without KCNH5 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[OR3A2]] | C | KCNH5 activity raises OR3A2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.53× lower at baseline in the lines without KCNH5 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[GABRG2]] | C | KCNH5 activity raises GABRG2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.54× lower at baseline in the lines without KCNH5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[CSMD3]] | C | KCNH5 activity raises CSMD3's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.48× lower at baseline in the lines without KCNH5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[CDH7]] | C | KCNH5 activity raises CDH7's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.91× lower at baseline in the lines without KCNH5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[DOK6]] | C | KCNH5 activity raises DOK6's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without KCNH5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[PAPPA2]] | C | KCNH5 activity raises PAPPA2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.96× lower at baseline in the lines without KCNH5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, 33.1); signed map (40.2, 36.7). **Vector** length 51.6, 22.4% of its response variance represented; |z| ≥ 3 in 269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +18.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily H member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:62,699,464-63,102,037 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv10.2, H-EAG2, eag2, hEAG2 |
| Gene groups (HGNC) | Potassium voltage-gated channels; PAS domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCM2](https://www.uniprot.org/uniprotkb/Q8NCM2) (Voltage-gated delayed rectifier potassium channel KCNH5):

> Pore-forming (alpha) subunit of a voltage-gated delayed rectifier potassium channel that mediates outward-rectifying potassium currents which, on depolarization, reaches a steady-state level and do not inactivate. The kinetic is characterized by a slow activation time course and a small voltage dependence of the activation time constants, therefore, starts to open at more negative voltages. The activation kinetics depend on the prepulse potential and external divalent cation concentration. The …

**Summary**, from NCBI Gene [27133](https://www.ncbi.nlm.nih.gov/gene/27133):

> This gene encodes a member of voltage-gated potassium channels. Members of this family have diverse functions, including regulating neurotransmitter and hormone release, cardiac function, and cell volume. This protein is an outward-rectifying, noninactivating channel. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:6254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6254) · Entrez [27133](https://www.ncbi.nlm.nih.gov/gene/27133) · UniProt [Q8NCM2](https://www.uniprot.org/uniprotkb/Q8NCM2) · Ensembl [ENSG00000140015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140015)

## Data

Gene col 6367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6367); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6367]; `tensor/DDL_lfc|DDL_z.npy` [6367]; `embed/gene_vectors.npy` [6367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6367 or target_col == 6367). Every well: [[KCNH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
