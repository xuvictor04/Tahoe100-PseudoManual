---
symbol: "FOXQ1"
type: "gene"
col: 8940
ensembl_id: "ENSG00000164379"
name: "forkhead box Q1"
location: "6p25.3"
module: 55
arm: "+"
pooled_cpm: 17.41
n_lines_expressing: 20
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 68
direction_downstream: 104
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# FOXQ1

*forkhead box Q1* — 6p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.69× (z +6.5, q 4e-08, up in 0 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +4.3, q 0.002, up in 10 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 8.69×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 7.48×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 4.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.373× (z -7.1, q 8e-10, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf132]] (+0.64, fdr 1e-05), [[SGPP2]] (+0.63, fdr 1e-05), [[BMP4]] (+0.62, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 68 arrows point to it, the strongest [[NOSTRIN]] → it (grade B ⚠); 104 go from it, the strongest it → [[KLF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8940.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 8.69×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 7.48×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 4.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +6.5 | 4e-08 | 0/14 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +6.3 | 1e-07 | 1/15 (A549) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +6.0 | 3e-07 | 1/13 (LS 180) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.3 | 0.002 | 10/17 (HT-29, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.009 | 1/17 (A549) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.8 | 0.012 | 1/17 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.5 | 0.040 | 6/17 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.56× | +3.2 | 0.11 | 8/17 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.55× | +3.1 | 0.11 | 7/17 (NCI-H1573, AsPC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.55× | +3.1 | 0.11 | 10/17 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.13 | 7/17 (Panc 03.27, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.373×** | -7.1 | 8e-10 | 17/17 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.450×** | -5.7 | 3e-06 | 17/17 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -5.2 | 5e-05 | 15/17 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.508×** | -4.9 | 2e-04 | 10/17 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.573×** | -3.7 | 0.024 | 5/17 (NCI-H1573, LoVo, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.595×** | -3.5 | 0.052 | 2/17 (COLO 205, LS 180) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -3.3 | 0.067 | 5/17 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -3.3 | 0.067 | 12/17 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.8 | 4 (2 ⚠) | 8 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.69× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.104× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.127× (z -12.5) |
| [[SW480 (line)]] | alt | 78.2 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0450× (z -18.4) |
| [[KATO III (line)]] | alt | 110 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0494× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0749× (z -14.5) |
| [[SW1417 (line)]] | alt | 68.1 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 66.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0679× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.195× (z -9.8) |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -8.6) |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0796× (z -11.3) |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.143× (z -8.9) |
| [[LoVo (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0442× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf132]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[BMP4]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TNS4]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.61 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[PHACTR3]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SLC6A14]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SKAP1]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[HSD17B2]] | +0.60 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[HNF4A]] | +0.60 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[ZFP36L2]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 3, C 65. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | NOSTRIN activity raises FOXQ1's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without NOSTRIN | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[PDE9A]] | B | PDE9A activity raises FOXQ1's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without PDE9A | 0.089 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[HDAC6]] | B | HDAC6 activity raises FOXQ1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises FOXQ1's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 6.63× lower at baseline in the lines without NPSR1-AS1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[S100P]] | C | S100P activity raises FOXQ1's level | lines that do not express S100P (34) vs lines expressing it (16) | 7.44× lower at baseline in the lines without S100P | 2e-04 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises FOXQ1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 6.40× lower at baseline in the lines without CLIC5 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[ANXA3]] | C | ANXA3 activity raises FOXQ1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 4.75× lower at baseline in the lines without ANXA3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises FOXQ1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 7.54× lower at baseline in the lines without PROM1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises FOXQ1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 8.26× lower at baseline in the lines without KRT23 | 0.001 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises FOXQ1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 6.69× lower at baseline in the lines without HSD17B2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises FOXQ1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 5.05× lower at baseline in the lines without TRIM29 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises FOXQ1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 5.60× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |

### Downstream of this gene

*104 arrows, 104 of them with an alert ⚠; grade A 0, B 36, C 68. Shown: the 12 strongest; 92 more arrows (92 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF3]] | B | FOXQ1 activity raises KLF3's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without FOXQ1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[EPS8L1]] | B | FOXQ1 activity raises EPS8L1's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 3.36× lower at baseline in the lines without FOXQ1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[PLEKHA7]] | B | FOXQ1 activity raises PLEKHA7's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without FOXQ1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[GAREM1]] | B | FOXQ1 activity raises GAREM1's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without FOXQ1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[BCL2L1-AS1]] | B | FOXQ1 activity raises BCL2L1-AS1's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without FOXQ1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[FAM83E]] | B | FOXQ1 activity raises FAM83E's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.88× lower at baseline in the lines without FOXQ1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | B | FOXQ1 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express FOXQ1 (30) vs lines expressing it (18) | the lines without FOXQ1: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[ITPKC]] | B | FOXQ1 activity raises ITPKC's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without FOXQ1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[NUDT4]] | B | FOXQ1 activity raises NUDT4's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without FOXQ1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[TMC6]] | B | FOXQ1 activity raises TMC6's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 3.17× lower at baseline in the lines without FOXQ1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[NOSTRIN]] | B | FOXQ1 activity raises NOSTRIN's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without FOXQ1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[ZFP36L2]] | B | FOXQ1 activity raises ZFP36L2's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.26× lower at baseline in the lines without FOXQ1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.0, 44.6); signed map (59.7, 11.1). **Vector** length 71.2, 25.5% of its response variance represented; |z| ≥ 3 in 510 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +6.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | -7.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -3.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box Q1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.3 — chr6:1,312,098-1,314,758 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HFH1 |
| Gene groups (HGNC) | Forkhead boxes |
| Reactome | 9 pathways, smallest: Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C009](https://www.uniprot.org/uniprotkb/Q9C009) (Forkhead box protein Q1):

> Plays a role in hair follicle differentiation.

**Summary**, from NCBI Gene [94234](https://www.ncbi.nlm.nih.gov/gene/94234):

> FOXQ1 is a member of the FOX gene family, which is characterized by a conserved 110-amino acid DNA-binding motif called the forkhead or winged helix domain. FOX genes are involved in embryonic development, cell cycle regulation, tissue-specific gene expression, cell signaling, and tumorigenesis (Bieller et al., 2001 [PubMed 11747606]).[supplied by OMIM, May 2009]

**Accessions** — [HGNC:20951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20951) · Entrez [94234](https://www.ncbi.nlm.nih.gov/gene/94234) · UniProt [Q9C009](https://www.uniprot.org/uniprotkb/Q9C009) · Ensembl [ENSG00000164379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164379)

## Data

Gene col 8940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8940); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8940]; `tensor/DDL_lfc|DDL_z.npy` [8940]; `embed/gene_vectors.npy` [8940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8940 or target_col == 8940). Every well: [[FOXQ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXQ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
