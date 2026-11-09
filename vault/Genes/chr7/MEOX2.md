---
symbol: "MEOX2"
type: "gene"
col: 2768
ensembl_id: "ENSG00000106511"
name: "mesenchyme homeobox 2"
location: "7p21.2"
module: 9
arm: "+"
pooled_cpm: 4.0
n_lines_expressing: 14
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MEOX2

*mesenchyme homeobox 2* — 7p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.25× (z +11.2, q 1e-26, up in 1 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (AN3 CA 0.0233×, Hs 766T 0.122×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0314×, Hs 766T 0.157×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 0.00752×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.118×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH18]] (+0.56, fdr 1e-05), [[TET1]] (+0.54, fdr 2e-05), [[PDE3B]] (+0.52, fdr 4e-05); moves opposite to [[TMEM92-AS1]] (-0.37, fdr 2e-04), [[TMEM132B]] (-0.37, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC01203]] → it (grade C ⚠); 8 go from it, the strongest it → [[SYNGR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.25×** | +11.2 | 1e-26 | 1/5 (SW480) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.32×** | +9.5 | 6e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.51×** | +7.8 | 8e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +5.9 | 4e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.66×** | +4.7 | 3e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.0 | 0.007 | 1/7 (SNU-1) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.9 | 0.008 | 0/6 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.018 | 0/6 | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +3.5 | 0.028 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +3.3 | 0.057 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.58× | +3.1 | 0.11 | 0/6 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.88× | +3.0 | 0.11 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.56× | +3.0 | 0.12 | 0/8 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2768.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (AN3 CA 0.0233×, Hs 766T 0.122×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0314×, Hs 766T 0.157×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 0.00752×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.118×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.600× | -3.3 | 0.50 | 2/9 (AN3 CA, Hs 766T) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.608× | -3.1 | 0.50 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 556 | 0 | 16 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.00752× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.0233× (z -19.0) |
| [[Hs 766T (line)]] | wt | 45.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.122× (z -9.7) |
| [[SW480 (line)]] | alt | 3.06 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0934× (z -8.9) |
| [[A-172 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.841 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH18]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TET1]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PDE3B]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[NME4]] | +0.51 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[LINC01203]] | +0.51 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[DACH1]] | +0.51 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[CDH6]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[TRERF1]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SPOCK3]] | +0.48 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[SOBP]] | +0.48 | +0.32 / +0.38 | both halves | 2e-04 |  |
| [[PIAS2]] | +0.47 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[DOK5]] | +0.47 | +0.44 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM92-AS1]] | -0.37 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[TMEM132B]] | -0.37 | -0.27 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01203]] | C | LINC01203 activity raises MEOX2's level | lines that do not express LINC01203 (37) vs lines expressing it (13) | 2.94× lower at baseline in the lines without LINC01203 | 0.056 | ⚠ within organs, on part of the lines; also absent: SIM1, BMP10, LINC02643; maybe low, not absent; co-absent with the target |
| [[BMP10]] | C | BMP10 activity raises MEOX2's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 2.42× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[LINC02099]] | C | LINC02099 activity raises MEOX2's level | lines that do not express LINC02099 (46) vs lines expressing it (4) | 2.22× lower at baseline in the lines without LINC02099 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: BMP10, LINC00879, APOB; co-absent with the target; its own permutation p |
| [[SOX6]] | C | SOX6 activity raises MEOX2's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without SOX6 | 0.074 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent; co-absent with the target |
| [[DOK5]] | C | DOK5 activity raises MEOX2's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.51× lower at baseline in the lines without DOK5 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises MEOX2's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without AK4P3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[RHOJ]] | C | RHOJ activity raises MEOX2's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.58× lower at baseline in the lines without RHOJ | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[AGMO]] | C | AGMO activity raises MEOX2's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.21× lower at baseline in the lines without AGMO | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises MEOX2's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 1.35× lower at baseline in the lines without SLC14A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises MEOX2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.12× lower at baseline in the lines without FUT9 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNGR1]] | B | MEOX2 activity raises SYNGR1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without MEOX2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252 |
| [[HSF2]] | B | MEOX2 activity raises HSF2's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 1.56× lower at baseline in the lines without MEOX2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252 |
| [[DACH1]] | C | MEOX2 activity raises DACH1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 3.29× lower at baseline in the lines without MEOX2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[PCDH18]] | C | MEOX2 activity raises PCDH18's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without MEOX2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[RHOJ]] | C | MEOX2 activity raises RHOJ's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 2.67× lower at baseline in the lines without MEOX2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[COL11A1]] | C | MEOX2 activity raises COL11A1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 5.20× lower at baseline in the lines without MEOX2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[LINC01203]] | C | MEOX2 activity raises LINC01203's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without MEOX2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[RUNX1T1]] | C | MEOX2 activity raises RUNX1T1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 3.26× lower at baseline in the lines without MEOX2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.427). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, 39.7); signed map (35.2, 31.3). **Vector** length 21.9, 5.11% of its response variance represented; |z| ≥ 3 in 214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +1.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.5 | +1.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.5 | -1.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.5 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.4 | -0.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mesenchyme homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.2 — chr7:15,611,212-15,686,683 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOX2; previously GAX |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P50222](https://www.uniprot.org/uniprotkb/P50222) (Homeobox protein MOX-2):

> Mesodermal transcription factor that plays a key role in somitogenesis and somitogenesis and limb muscle differentiation (By similarity). Required during limb development for normal appendicular muscle formation and for the normal regulation of myogenic genes (By similarity). May have a regulatory role when quiescent vascular smooth muscle cells reenter the cell cycle (By similarity). Also acts as a negative regulator of angiogenesis. Activates expression of CDKN1A and CDKN2A in endothelial …

**Summary**, from NCBI Gene [4223](https://www.ncbi.nlm.nih.gov/gene/4223):

> This gene encodes a member of a subfamily of non-clustered, diverged, antennapedia-like homeobox-containing genes. The encoded protein may play a role in the regulation of vertebrate limb myogenesis. Mutations in the related mouse protein may be associated with craniofacial and/or skeletal abnormalities, in addition to neurovascular dysfunction observed in Alzheimer's disease. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7014) · Entrez [4223](https://www.ncbi.nlm.nih.gov/gene/4223) · UniProt [P50222](https://www.uniprot.org/uniprotkb/P50222) · Ensembl [ENSG00000106511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106511)

## Data

Gene col 2768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2768); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2768]; `tensor/DDL_lfc|DDL_z.npy` [2768]; `embed/gene_vectors.npy` [2768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2768 or target_col == 2768). Every well: [[MEOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
