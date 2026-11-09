---
symbol: "SUCNR1"
type: "gene"
col: 12695
ensembl_id: "ENSG00000198829"
name: "succinate receptor 1"
location: "3q25.1"
module: 13
arm: "+"
pooled_cpm: 9.05
n_lines_expressing: 6
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SUCNR1

*succinate receptor 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 10.2× (z +11.5, q 1e-27, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +5.5, q 5e-06, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.108×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A-172 0.0858×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIRAS3]] (+0.68, fdr 7e-06), [[TEK]] (+0.55, fdr 3e-05), [[LNCAROD]] (+0.48, fdr 1e-04); moves opposite to [[IRAK1]] (-0.39, fdr 2e-04), [[MROH1]] (-0.37, fdr 3e-04), [[PINX1-1]] (-0.36, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF736P9Y]] → it (grade C ⚠); 9 go from it, the strongest it → [[ZNF736P9Y]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.2×** | +11.5 | 1e-27 | 2/2 (A-172, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.08×** | +10.0 | 3e-21 | 1/3 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.93×** | +8.4 | 6e-15 | 1/3 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +5.5 | 5e-06 | 0/3 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.83×** | +5.1 | 3e-05 | 0/4 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +4.8 | 2e-04 | 0/4 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.4 | 0.001 | 0/4 | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **2.33×** | +4.3 | 0.001 | 2/4 (CFPAC-1, NCI-H1792) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +4.0 | 0.003 | 1/4 (NCI-H1792) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.008 | 1/4 (NCI-H460) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.7 | 0.010 | 0/4 | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.7 | 0.010 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.88×** | +3.6 | 0.012 | 1/3 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.021 | 2/4 (NCI-H460, CFPAC-1) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +3.4 | 0.025 | 0/4 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.049 | 3/4 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.056 | 0/4 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.81×** | +3.0 | 0.068 | 0/4 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12695.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.108×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A-172 0.0858×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.492× | -3.4 | 0.26 | 0/4 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.509× | -3.2 | 0.26 | 0/4 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.515× | -3.2 | 0.26 | 0/4 | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | 0.550× | -3.1 | 0.26 | 0/4 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.659× | -3.0 | 0.26 | 2/4 (A-172, NCI-H460) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 317 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -12.6) |
| [[A-427 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.395 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 10 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIRAS3]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TEK]] | +0.55 | +0.65 / +0.43 | both halves | 3e-05 | **novel candidate** |
| [[LNCAROD]] | +0.48 | +0.33 / +0.39 | both halves | 1e-04 |  |
| [[LMO2]] | +0.47 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[VSTM4]] | +0.47 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CCDC33]] | +0.47 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[SCN3A]] | +0.46 | +0.23 / +0.52 | both halves | 5e-04 |  |
| [[PRSS23]] | +0.46 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[DKK3]] | +0.45 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[LRRC17]] | +0.43 | +0.62 / +0.25 | both halves | 4e-04 |  |
| [[FZD8]] | +0.43 | +0.39 / +0.45 | both halves | 5e-05 | pathway: GPCR ligand binding |
| [[COL8A1]] | +0.42 | +0.45 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK1]] | -0.39 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[MROH1]] | -0.37 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[PINX1-1]] | -0.36 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[SNHG29]] | -0.36 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[NADSYN1]] | -0.36 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[PCBP4]] | -0.35 | -0.14 / -0.44 | ⚠ not reproduced | 0.002 |  |
| [[CMTM4]] | -0.35 | -0.21 / -0.36 | both halves | 6e-04 |  |
| [[MACROD1]] | -0.35 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[SGSH]] | -0.34 | -0.28 / -0.31 | both halves | 3e-04 |  |
| [[DUSP22]] | -0.34 | -0.21 / -0.38 | both halves | 6e-04 |  |
| [[PAM16]] | -0.33 | -0.31 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[UBE2D4]] | -0.33 | -0.26 / -0.34 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises SUCNR1's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.55× lower at baseline in the lines without ZNF736P9Y | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[PLAT]] | C | PLAT activity raises SUCNR1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.67× lower at baseline in the lines without PLAT | 0.018 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF736P9Y]] | C | SUCNR1 activity raises ZNF736P9Y's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 5.46× lower at baseline in the lines without SUCNR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[CACNA2D3]] | C | SUCNR1 activity raises CACNA2D3's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 8.39× lower at baseline in the lines without SUCNR1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[SHC4]] | C | SUCNR1 activity raises SHC4's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 4.71× lower at baseline in the lines without SUCNR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[PLAT]] | C | SUCNR1 activity raises PLAT's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 6.03× lower at baseline in the lines without SUCNR1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[COL8A1]] | C | SUCNR1 activity raises COL8A1's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 7.11× lower at baseline in the lines without SUCNR1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[TBXT]] | C | SUCNR1 activity raises TBXT's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 4.11× lower at baseline in the lines without SUCNR1 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[GREM2]] | C | SUCNR1 activity raises GREM2's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 3.82× lower at baseline in the lines without SUCNR1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[SALL1]] | C | SUCNR1 activity raises SALL1's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 3.46× lower at baseline in the lines without SUCNR1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[ADAMTS6]] | C | SUCNR1 activity raises ADAMTS6's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 5.07× lower at baseline in the lines without SUCNR1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.338). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (57.3, 19.2); signed map (27.7, 51.6). **Vector** length 17.0, 6.07% of its response variance represented; |z| ≥ 3 in 119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +0.7 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.5 | +0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.4 | +2.0 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.3 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.5 | -0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.5 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -0.5 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.4 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | succinate receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:151,873,643-151,884,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPR91 |
| Gene groups (HGNC) | Succinate receptor |
| Reactome | 5 pathways, smallest: Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXA5](https://www.uniprot.org/uniprotkb/Q9BXA5) (Succinate receptor 1):

> G protein-coupled receptor for succinate able to mediate signaling through Gq/GNAQ or Gi/GNAI second messengers depending on the cell type and the processes regulated (By similarity). Succinate-SUCNR1 signaling serves as a link between metabolic stress, inflammation and energy homeostasis. In macrophages, plays a range of immune-regulatory roles. During inflammation, succinate-SUCNR1 signaling may act as an anti-inflammatory mediator or boost inflammation depending on the inflammatory status of …

**Summary**, from NCBI Gene [56670](https://www.ncbi.nlm.nih.gov/gene/56670):

> This gene encodes a G-protein-coupled receptor for succinate, an intermediate molecule of the citric acid cycle. It is involved in the promotion of hematopoietic progenitor cell development, and it has a potential role in renovascular hypertension which has known correlations to renal failure, diabetes and atherosclerosis. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:4542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4542) · Entrez [56670](https://www.ncbi.nlm.nih.gov/gene/56670) · UniProt [Q9BXA5](https://www.uniprot.org/uniprotkb/Q9BXA5) · Ensembl [ENSG00000198829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198829)

## Data

Gene col 12695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12695); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12695]; `tensor/DDL_lfc|DDL_z.npy` [12695]; `embed/gene_vectors.npy` [12695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12695 or target_col == 12695). Every well: [[SUCNR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUCNR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
