---
symbol: "SEMA4G"
type: "gene"
col: 1747
ensembl_id: "ENSG00000095539"
name: "semaphorin 4G"
location: "10q24.31"
module: 55
arm: "+"
pooled_cpm: 4.49
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 22
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SEMA4G

*semaphorin 4G* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +6.8, q 6e-09, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.42× (z +3.7, q 0.036, up in 6 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.202× (z -16.2, q 0e+00, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGFR4]] (+0.69, fdr 7e-06), [[SORL1]] (+0.65, fdr 1e-05), [[HNF4A]] (+0.65, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[RNF128]] → it (grade B ⚠); 22 go from it, the strongest it → cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.8 | 6e-09 | 2/8 (HepG2/C3A, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.52×** | +6.3 | 9e-08 | 9/38 (RKO, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.036 | 6/33 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.39×** | +3.5 | 0.061 | 7/36 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.36× | +3.3 | 0.11 | 4/32 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.54× | +3.2 | 0.11 | 0/14 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.15 | 5/40 (HT-29, SW48, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.34× | +3.0 | 0.18 | 12/32 (SW1417, HOP62, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1747.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.202×** | -16.2 | 0e+00 | 32/37 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.326×** | -11.8 | 9e-30 | 24/32 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -10.1 | 2e-21 | 27/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.397×** | -9.7 | 3e-20 | 28/37 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.412×** | -9.3 | 1e-18 | 23/37 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.545×** | -9.0 | 2e-17 | 22/33 (HT-29, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -8.4 | 4e-15 | 16/26 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -7.4 | 1e-11 | 24/35 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.579×** | -5.8 | 6e-07 | 15/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.644×** | -4.6 | 2e-04 | 11/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -4.5 | 3e-04 | 14/32 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.749×** | -4.3 | 9e-04 | 11/37 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.476×** | -4.1 | 0.002 | 10/33 (SHP-77, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.709×** | -3.5 | 0.021 | 11/38 (C-33 A, NCI-H2030, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.683×** | -3.4 | 0.026 | 8/37 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -3.2 | 0.048 | 11/37 (LS 180, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -3.0 | 0.087 | 12/37 (HT-29, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.5 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0235× (z -20.6) |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0238× (z -22.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Peretinoin (drug)]] 0.5 µM 0.110× (z -9.4) |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -16.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0792× (z -12.2) |
| [[SW480 (line)]] | alt | 8.68 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0808× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -9.8) |
| [[PANC-1 (line)]] | alt | 2.79 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0648× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0718× (z -10.9) |
| [[SW1417 (line)]] | alt | 8.22 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0223× (z -17.6) |
| [[A549 (line)]] | wt | 4.40 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0194× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 5.51 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0424× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0980× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 5.68 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0850× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 3.24 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0547× (z -10.8) |
| [[A-427 (line)]] | wt | 4.94 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0567× (z -11.2) |
| [[KATO III (line)]] | alt | 7.09 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0751× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 4.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0970× (z -8.5) |
| [[RKO (line)]] | wt | 8.38 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0627× (z -10.8) |
| [[A-172 (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGFR4]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SORL1]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[HNF4A]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 | same gene group |
| [[USH1C]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[EDAR]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[VILL]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[GPX2]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[BMP4]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PROM1]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF128]] | B | RNF128 activity raises SEMA4G's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without RNF128 | 0.012 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[GPX2]] | B | GPX2 activity raises SEMA4G's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.48× lower at baseline in the lines without GPX2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[SORL1]] | B | SORL1 activity raises SEMA4G's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.85× lower at baseline in the lines without SORL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[CLDN3]] | B | CLDN3 activity raises SEMA4G's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 1.73× lower at baseline in the lines without CLDN3 | 0.054 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[LARGE2]] | B | LARGE2 activity raises SEMA4G's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without LARGE2 | 0.069 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[FGD3]] | B | FGD3 activity raises SEMA4G's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without FGD3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[MUC3A]] | B | MUC3A activity raises SEMA4G's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without MUC3A | 0.072 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[REG4]] | B | REG4 activity raises SEMA4G's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.07× lower at baseline in the lines without REG4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM | C | SEMA4G activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.82× the cells of the other lines | 0.013 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Aliskiren (drug)]] 0.5 µM | C | SEMA4G activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.70× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Clotrimazole (drug)]] 0.5 µM | C | SEMA4G activity raises the cells' numbers under Clotrimazole 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.79× the cells of the other lines | 0.017 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Adenosine (drug)]] 5 µM | C | SEMA4G activity raises the cells' numbers under Adenosine 5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.85× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Erdafitinib (drug)]] 5 µM | C | SEMA4G activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.81× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Ritonavir (drug)]] 0.5 µM | C | SEMA4G activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.82× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | C | SEMA4G activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.37× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 0.05 µM | C | SEMA4G activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.23× the cells of the other lines | 0.037 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Ralimetinib dimesylate (drug)]] 5 µM | C | SEMA4G activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.77× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Oxaliplatin (drug)]] 0.05 µM | C | SEMA4G activity lowers the cells' numbers under Oxaliplatin 0.05 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.26× the cells of the other lines | 0.045 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[ULK-101 (drug)]] 5 µM | C | SEMA4G activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.28× the cells of the other lines | 0.050 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 0.5 µM | C | SEMA4G activity raises the cells' numbers under Trifluridine 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.80× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.5, 46.6); signed map (62.2, 11.6). **Vector** length 67.1, 11.9% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +2.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | -0.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | +1.2 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 4G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,969,504-100,985,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20590, KIAA1619 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Semaphorins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTN9](https://www.uniprot.org/uniprotkb/Q9NTN9) (Semaphorin-4G):

> Cell surface receptor for PLXNB2. May play a role in axon guidance (By similarity).

**Summary**, from NCBI Gene [57715](https://www.ncbi.nlm.nih.gov/gene/57715):

> Semaphorins are a large family of conserved secreted and membrane associated proteins which possess a semaphorin (Sema) domain and a PSI domain (found in plexins, semaphorins and integrins) in the N-terminal extracellular portion. Based on sequence and structural similarities, semaphorins are put into eight classes: invertebrates contain classes 1 and 2, viruses have class V, and vertebrates contain classes 3-7. Semaphorins serve as axon guidance ligands via multimeric receptor complexes, some …

**Accessions** — [HGNC:10735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10735) · Entrez [57715](https://www.ncbi.nlm.nih.gov/gene/57715) · UniProt [Q9NTN9](https://www.uniprot.org/uniprotkb/Q9NTN9) · Ensembl [ENSG00000095539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095539)

## Data

Gene col 1747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1747); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1747]; `tensor/DDL_lfc|DDL_z.npy` [1747]; `embed/gene_vectors.npy` [1747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1747 or target_col == 1747). Every well: [[SEMA4G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA4G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
