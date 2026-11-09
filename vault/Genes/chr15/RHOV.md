---
symbol: "RHOV"
type: "gene"
col: 2419
ensembl_id: "ENSG00000104140"
name: "ras homolog family member V"
location: "15q15.1"
module: 14
arm: "+"
pooled_cpm: 12.25
n_lines_expressing: 27
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 26
direction_downstream: 42
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RHOV

*ras homolog family member V* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.31× (z +9.0, q 2e-16, up in 20 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.527× (z -4.8, q 7e-04, down in 18 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 5 lines (CFPAC-1 0.152×, HCT15 0.0587×, NCI-H23 0.0853×, Panc 03.27 0.187×, …); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 0.218×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.164×; ⚠ cell-cycle shift, would explain all of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.171×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELF3]] (+0.66, fdr 7e-06), [[BCL3]] (+0.64, fdr 7e-06), [[CGN]] (+0.64, fdr 1e-05); moves opposite to [[DPP9]] (-0.54, fdr 6e-05), [[TMEM181]] (-0.53, fdr 5e-05), [[SEC14L1]] (-0.51, fdr 7e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[P2RY6]] → it (grade B ⚠); 42 go from it, the strongest it → [[USP43]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +9.0 | 2e-16 | 20/24 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.74×** | +7.3 | 6e-11 | 21/23 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +7.2 | 9e-11 | 15/23 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +5.6 | 3e-06 | 19/24 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.4 | 9e-06 | 14/22 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +4.7 | 3e-04 | 8/20 (BT-474, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.6 | 3e-04 | 6/22 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +4.3 | 0.001 | 15/23 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.046 | 5/23 (HCT15, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2419.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 5 lines (CFPAC-1 0.152×, HCT15 0.0587×, NCI-H23 0.0853×, Panc 03.27 0.187×, …); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 0.218×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.164×; ⚠ cell-cycle shift, would explain all of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.171×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -4.8 | 7e-04 | 18/23 (CFPAC-1, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.592×** | -4.0 | 0.021 | 14/23 (SNU-423, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 5 (3 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.218× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 42.1 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.93× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.152× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 3.34 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 51.9 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +8.8) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 12.1 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.03× (z +9.3) ⚠ position not correctable | [[Auranofin (drug)]] 5 µM 0.0853× (z -9.4) |
| [[A549 (line)]] | wt | 6.35 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0732× (z -9.0) |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -9.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0587× (z -10.0) |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.177× (z -8.5) |
| [[KATO III (line)]] | alt | 3.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +8.7) | — |
| [[LoVo (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.71× (z +8.9) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.187× (z -9.0) |
| [[SW1417 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.1) | — |
| [[A-172 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF3]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[BCL3]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CGN]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[MAP3K8]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[GALT]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PIM3]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ODF3B]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CX3CL1]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[NFKBIA]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[DECR2]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.57 | +0.50 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.54 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[TMEM181]] | -0.53 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SEC14L1]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[FUBP3]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[TIMM23B-AGAP6]] | -0.48 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[PIGG]] | -0.48 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[ZNF731P]] | -0.47 | -0.32 / -0.57 | both halves | 1e-04 |  |
| [[CUL4A]] | -0.47 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[CARS2]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[MCM3AP]] | -0.47 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 7, C 19. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RY6]] | B | P2RY6 activity raises RHOV's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without P2RY6 | 0.017 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[PTGES]] | B | PTGES activity raises RHOV's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.16× lower at baseline in the lines without PTGES | 0.026 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[TYMP]] | B | TYMP activity raises RHOV's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.17× lower at baseline in the lines without TYMP | 0.052 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[GBP2]] | B | GBP2 activity raises RHOV's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without GBP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[SLC2A6]] | B | SLC2A6 activity lowers RHOV's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 2.49× higher at baseline in the lines without SLC2A6 | 0.079 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[USP43]] | B | USP43 activity raises RHOV's level | lines that do not express USP43 (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without USP43 | 0.093 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[CXXC4]] | B | CXXC4 activity raises RHOV's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without CXXC4 | 0.095 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1 |
| [[LINC02967]] | C | LINC02967 activity raises RHOV's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 5.13× lower at baseline in the lines without LINC02967 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises RHOV's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 5.32× lower at baseline in the lines without STEAP4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[ELF3]] | C | ELF3 activity raises RHOV's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.59× lower at baseline in the lines without ELF3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises RHOV's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.49× lower at baseline in the lines without LCN2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[XDH]] | C | XDH activity raises RHOV's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.97× lower at baseline in the lines without XDH | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 26, C 16. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP43]] | B | RHOV activity raises USP43's level | lines that do not express RHOV (23) vs lines expressing it (27) | 3.54× lower at baseline in the lines without RHOV | 0.007 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[ETV7]] | B | RHOV activity raises ETV7's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without RHOV | 0.008 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[RSPH1]] | B | RHOV activity raises RSPH1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without RHOV | 0.011 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[HLA-F]] | B | RHOV activity raises HLA-F's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without RHOV | 0.015 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[IRF1]] | B | RHOV activity raises IRF1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without RHOV | 0.020 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[MAP3K8]] | B | RHOV activity raises MAP3K8's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without RHOV | 0.021 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[TUFT1]] | B | RHOV activity raises TUFT1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without RHOV | 0.024 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[RAB9A]] | B | RHOV activity raises RAB9A's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without RHOV | 0.025 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[CCNL1]] | B | RHOV activity raises CCNL1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.25× lower at baseline in the lines without RHOV | 0.027 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[MVP-DT]] | B | RHOV activity raises MVP-DT's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without RHOV | 0.043 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[RND1]] | B | RHOV activity raises RND1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.29× lower at baseline in the lines without RHOV | 0.043 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[PIM3]] | B | RHOV activity raises PIM3's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without RHOV | 0.044 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 4.1); signed map (46.5, 6.0). **Vector** length 73.8, 23.3% of its response variance represented; |z| ≥ 3 in 503 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -1.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,872,214-40,874,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Chp, WRCH2; previously ARHV |
| Gene groups (HGNC) | Rho family GTPases |
| Reactome | 4 pathways, smallest: RHOV GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L33](https://www.uniprot.org/uniprotkb/Q96L33) (Rho-related GTP-binding protein RhoV):

> Plays a role in the control of the actin cytoskeleton via activation of the JNK pathway.

**Summary**, from NCBI Gene [171177](https://www.ncbi.nlm.nih.gov/gene/171177):

> Predicted to enable GTP binding activity; GTPase activity; and protein kinase binding activity. Predicted to be involved in several processes, including actin filament organization; endocytosis; and establishment of cell polarity. Predicted to be located in endosome membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18313) · Entrez [171177](https://www.ncbi.nlm.nih.gov/gene/171177) · UniProt [Q96L33](https://www.uniprot.org/uniprotkb/Q96L33) · Ensembl [ENSG00000104140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104140)

## Data

Gene col 2419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2419); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2419]; `tensor/DDL_lfc|DDL_z.npy` [2419]; `embed/gene_vectors.npy` [2419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2419 or target_col == 2419). Every well: [[RHOV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
