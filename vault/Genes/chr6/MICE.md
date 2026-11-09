---
symbol: "MICE"
type: "gene"
col: 15780
ensembl_id: "ENSG00000273340"
name: "MHC class I polypeptide-related sequence E (pseudogene)"
location: "6p22.1"
module: 183
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 36
n_dd_up: 2
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# MICE

*MHC class I polypeptide-related sequence E (pseudogene)* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +7.5, q 3e-11, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.456× (z -5.8, q 3e-06, down in 17 of 28 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.560× (z -4.5, q 0.002, down in 12 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.0622×, Panc 03.27 0.147×, Hs 766T 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.0701×, SW1417 0.0836×, NCI-H2347 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.0890×, NCI-H2347 0.0946×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-F-AS1]] (+0.74, fdr 7e-06, ⚠ same locus), [[CRYBB2P1]] (+0.62, fdr 1e-05), [[ATG9B]] (+0.60, fdr 7e-06), [[LINC02210-CRHR1]] (+0.60, fdr 1e-05); moves opposite to [[MED1]] (-0.53, fdr 1e-05), [[ATF1]] (-0.51, fdr 3e-05), [[ZC3H12C]] (-0.51, fdr 1e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); 13 go from it, the strongest it → [[HLA-F-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +7.5 | 3e-11 | 12/24 (NCI-H2030, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +4.7 | 9e-04 | 9/28 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.56× | +3.3 | 0.18 | 4/17 (SNU-423, SW480, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.33× | +3.1 | 0.19 | 4/31 (A498, NCI-H2030, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.49× | +3.1 | 0.19 | 5/30 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.19 | 4/19 (KATO III, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15780.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.0622×, Panc 03.27 0.147×, Hs 766T 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.0701×, SW1417 0.0836×, NCI-H2347 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.0890×, NCI-H2347 0.0946×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.456×** | -5.8 | 3e-06 | 17/28 (CFPAC-1, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -4.5 | 0.002 | 12/31 (NCI-H2347, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.598×** | -4.0 | 0.015 | 11/31 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.647× | -3.3 | 0.11 | 6/31 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.651× | -3.3 | 0.11 | 10/31 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.746× | -3.2 | 0.14 | 3/31 (J82, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.668× | -3.1 | 0.16 | 5/18 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 47.2 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -19.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 5.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-F-AS1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CRYBB2P1]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ATG9B]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LINC02210-CRHR1]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[EOLA2]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[IRF6]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[EOLA1]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[PMS2P3-1]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[VAMP1]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ZNF836]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[CEP295NL]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TIMM10B]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZFYVE27]] | +0.51 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | -0.53 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[ATF1]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ZC3H12C]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PBRM1]] | -0.50 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ZNF644]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[GPATCH8]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ZMYM4]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TASOR2]] | -0.49 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[CUX1]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[BPTF]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[POGZ]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CEBPZ]] | -0.48 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises MICE's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without IRF6 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MYO5B]] | B | MYO5B activity raises MICE's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.95× lower at baseline in the lines without MYO5B | 0.014 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[SEMA3B]] | B | SEMA3B activity raises MICE's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without SEMA3B | 0.024 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[HLA-K]] | B | HLA-K activity raises MICE's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without HLA-K | 0.070 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[TTC9]] | B | TTC9 activity raises MICE's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without TTC9 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | MICE activity raises HLA-F-AS1's level | lines that do not express MICE (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without MICE | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[NPTN]] | B | MICE activity raises NPTN's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without MICE | 0.019 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[CEP83]] | B | MICE activity lowers CEP83's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.45× higher at baseline in the lines without MICE | 0.021 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[UTP14A]] | B | MICE activity lowers UTP14A's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without MICE | 0.025 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[NDUFAF7]] | B | MICE activity lowers NDUFAF7's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.22× higher at baseline in the lines without MICE | 0.026 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[R3HDM2]] | B | MICE activity lowers R3HDM2's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.34× higher at baseline in the lines without MICE | 0.039 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[DDX10]] | B | MICE activity lowers DDX10's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.56× higher at baseline in the lines without MICE | 0.062 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[SENP1]] | B | MICE activity lowers SENP1's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without MICE | 0.066 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[IFI27L1]] | B | MICE activity raises IFI27L1's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without MICE | 0.083 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[LINC00674]] | B | MICE activity raises LINC00674's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.13× lower at baseline in the lines without MICE | 0.084 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[ERCC4]] | B | MICE activity lowers ERCC4's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without MICE | 0.089 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | MICE activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express MICE (14) vs lines expressing it (34) | the lines without MICE: 0.90× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.4, -22.8); signed map (-26.2, 26.5). **Vector** length 53.3, 9.96% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.6 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.7 | -5.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -0.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | MHC class I polypeptide-related sequence E (pseudogene) |
| Locus type | pseudogene |
| Location | 6p22.1 — chr6:29,741,731-29,748,969 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | dJ377H14.7, PERB11.5 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:7094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7094) · Entrez [4280](https://www.ncbi.nlm.nih.gov/gene/4280) · Ensembl [ENSG00000273340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273340)

## Data

Gene col 15780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15780); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15780]; `tensor/DDL_lfc|DDL_z.npy` [15780]; `embed/gene_vectors.npy` [15780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15780 or target_col == 15780). Every well: [[MICE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
