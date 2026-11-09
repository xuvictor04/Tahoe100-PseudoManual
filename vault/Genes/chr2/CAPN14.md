---
symbol: "CAPN14"
type: "gene"
col: 13215
ensembl_id: "ENSG00000214711"
name: "calpain 14"
location: "2p23.1"
module: 27
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 34
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CAPN14

*calpain 14* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.65× (z +13.0, q 1e-35, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +6.1, q 2e-07, up in 8 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.562× (z -5.1, q 2e-04, down in 14 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (HCT15 0.0181×, HEC-1-A 0.193×, LS 180 0.0831×); [[Harringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.0171×, LS 180 0.0572×; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.0375×, LoVo 0.0270×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0188×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.242×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED2]] (+0.57, fdr 2e-05), [[CHST9]] (+0.57, fdr 2e-05), [[GPR35]] (+0.56, fdr 2e-05); moves opposite to [[EIF2B4]] (-0.42, fdr 1e-04), [[SNX21]] (-0.42, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GALNT14]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMC3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.65×** | +13.0 | 1e-35 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +8.7 | 9e-16 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.4 | 3e-11 | 2/6 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.1 | 2e-07 | 8/26 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.8 | 6e-07 | 3/16 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.32×** | +5.3 | 1e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.0 | 0.005 | 1/13 (NCI-H2030) | inconsistent across doses |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.005 | 2/17 (LoVo, A-172) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.35×** | +3.9 | 0.006 | 0/6 | rises with dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.8 | 0.008 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.008 | 2/16 (SHP-77, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.008 | 0/26 | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.009 | 2/17 (A-427, CFPAC-1) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.53×** | +3.6 | 0.015 | 0/7 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.031 | 3/14 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Apalutamide (drug)]] 0.05 µM |  | **1.52×** | +3.2 | 0.049 | 2/18 (NCI-H1573, PANC-1) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.051 | 2/22 (HCT15, RPMI-7951) | top dose only | cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.051 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.058 | 1/17 (NCI-H460) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13215.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (HCT15 0.0181×, HEC-1-A 0.193×, LS 180 0.0831×); [[Harringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.0171×, LS 180 0.0572×; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.0375×, LoVo 0.0270×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0188×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.242×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -5.1 | 2e-04 | 14/27 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.688× | -3.3 | 0.26 | 2/25 (A549, Panc 03.27) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.710× | -3.0 | 0.33 | 8/19 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.712× | -3.0 | 0.33 | 10/22 (A-427, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0373× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0188× (z -21.1) |
| [[HCT15 (line)]] | alt | 8.32 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0181× (z -11.5) |
| [[LS 180 (line)]] | wt | 6.02 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0572× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0831× (z -8.5) |
| [[A-427 (line)]] | wt | 3.23 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0610× (z -8.8) |
| [[LoVo (line)]] | wt | 1.65 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0270× (z -9.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 0.860 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.633 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.689 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.640 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.633 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.698 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.295 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED2]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 | **novel candidate** |
| [[CHST9]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[GPR35]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[POU3F3]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[DANT1]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[ZNF385B]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[NPSR1-AS1]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LINC02999]] | +0.54 | +0.36 / +0.65 | both halves | 1e-04 | **novel candidate** |
| [[SYT13]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[TRPM2-AS]] | +0.53 | +0.55 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[NOSTRIN]] | +0.52 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[XACT]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B4]] | -0.42 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SNX21]] | -0.42 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT14]] | B | GALNT14 activity raises CAPN14's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without GALNT14 | 0.030 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TRPM2-AS]] | B | TRPM2-AS activity raises CAPN14's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without TRPM2-AS | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[CHST9]] | B | CHST9 activity raises CAPN14's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without CHST9 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises CAPN14's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 1.78× lower at baseline in the lines without PLEKHG1 | 0.073 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SLC44A3]] | B | SLC44A3 activity raises CAPN14's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without SLC44A3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[LINC01456]] | B | LINC01456 activity raises CAPN14's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 2.22× lower at baseline in the lines without LINC01456 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8 |
| [[XACT]] | B | XACT activity raises CAPN14's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without XACT | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC3-AS1]] | B | CAPN14 activity raises TMC3-AS1's level | lines that do not express CAPN14 (16) vs lines expressing it (34) | 1.43× lower at baseline in the lines without CAPN14 | 0.012 | ⚠ within organs, on part of the lines; also absent: CFAP46, EBF2, GAS7; maybe low, not absent |
| [[RGS6]] | B | CAPN14 activity raises RGS6's level | lines that do not express CAPN14 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without CAPN14 | 0.051 | ⚠ within organs, on part of the lines; also absent: CFAP46, EBF2, GAS7; maybe low, not absent |
| [[HSPA12A]] | B | CAPN14 activity raises HSPA12A's level | lines that do not express CAPN14 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CAPN14 | 0.055 | ⚠ within organs, on part of the lines; also absent: CFAP46, EBF2, GAS7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.251). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.6, 41.7); signed map (50.5, 36.1). **Vector** length 40.2, 6.89% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | -0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +0.4 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -0.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | calpain 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:31,173,056-31,233,858 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing; Calpains |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MX76](https://www.uniprot.org/uniprotkb/A8MX76) (Calpain-14):

> Calcium-regulated non-lysosomal thiol-protease.

**Summary**, from NCBI Gene [440854](https://www.ncbi.nlm.nih.gov/gene/440854):

> Calpains are a family of cytosolic calcium-activated cysteine proteases involved in a variety of cellular processes including apoptosis, cell division, modulation of integrin-cytoskeletal interactions, and synaptic plasticity (Dear et al., 2000 [PubMed 10964513]). CAPN14 belongs to the calpain large subunit family.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16664) · Entrez [440854](https://www.ncbi.nlm.nih.gov/gene/440854) · UniProt [A8MX76](https://www.uniprot.org/uniprotkb/A8MX76) · Ensembl [ENSG00000214711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214711)

## Data

Gene col 13215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13215); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13215]; `tensor/DDL_lfc|DDL_z.npy` [13215]; `embed/gene_vectors.npy` [13215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13215 or target_col == 13215). Every well: [[CAPN14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
