---
symbol: "ADAM7-AS1"
type: "gene"
col: 14811
ensembl_id: "ENSG00000253535"
name: "ADAM7, ADAMDEC1 and ADAM28 antisense RNA 1"
location: "8p21.2"
module: 61
arm: "+"
pooled_cpm: 19.29
n_lines_expressing: 27
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ADAM7-AS1

*ADAM7, ADAMDEC1 and ADAM28 antisense RNA 1* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +15.8, q 0e+00, up in 9 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.674× (z -5.3, q 6e-05, down in 11 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTF3]] (+0.60, fdr 1e-05), [[SPTBN4]] (+0.60, fdr 1e-05), [[RTN4RL2]] (+0.60, fdr 2e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DNAH17]] → it (grade B ⚠); 11 go from it, the strongest it → [[HMGN2P46]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +15.8 | 0e+00 | 9/24 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +14.3 | 4e-44 | 19/25 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +11.2 | 5e-27 | 22/24 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +10.8 | 7e-25 | 4/23 (Hs 766T, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +10.7 | 1e-24 | 9/24 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.06×** | +9.7 | 2e-20 | 12/23 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.0 | 1e-13 | 5/18 (RPMI-7951, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +7.4 | 1e-11 | 2/20 (SW1417, RPMI-7951) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.35×** | +6.0 | 1e-07 | 12/23 (NCI-H460, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.66×** | +4.9 | 7e-05 | 7/24 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 5e-04 | 3/25 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 8e-04 | 2/23 (H4, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.003 | 5/25 (NCI-H460, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.012 | 11/24 (H4, RPMI-7951, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.012 | 9/23 (NCI-H23, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.014 | 12/25 (A-172, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.016 | 4/24 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.017 | 6/24 (SW1417, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -5.3 | 6e-05 | 11/23 (NCI-H23, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -4.7 | 9e-04 | 14/25 (A-172, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.733×** | -4.2 | 0.006 | 13/24 (NCI-H23, A498, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -4.1 | 0.006 | 8/23 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.809×** | -4.0 | 0.006 | 8/25 (A549, CHP-212, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.7 | 0.023 | 2/26 (SHP-77, SW1417) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.775×** | -3.4 | 0.048 | 5/24 (A549, SW 900, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.784×** | -3.3 | 0.071 | 15/23 (NCI-H23, Panc 03.27, …) | all doses, flat |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.843× | -3.3 | 0.071 | 4/26 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.790×** | -3.2 | 0.081 | 6/23 (RPMI-7951, hTERT-HPNE, …) | two highest doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.847× | -3.2 | 0.081 | 7/24 (RPMI-7951, Hs 766T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 131 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -25.7) |
| [[A-172 (line)]] | wt | 172 | 2 (1 ⚠) | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.73× (z +11.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0827× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 19.5 | 1 | 6 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.37× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0459× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~2% of this change |
| [[NCI-H1573 (line)]] | alt | 36.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -18.0) |
| [[A549 (line)]] | wt | 22.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.13× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0361× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 5.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 15.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.42× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +15.7) | — |
| [[hTERT-HPNE (line)]] | wt | 98.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0304× (z -14.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 46.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.33× (z +9.0) ⚠ unreliable plate only | — |
| [[SHP-77 (line)]] | alt | 8.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0667× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTF3]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SPTBN4]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[RTN4RL2]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CRTAC1]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GSDME]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SCG3]] | +0.55 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[RPLP0P2]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[GABRG3]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[OR9Q1]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH17]] | B | DNAH17 activity raises ADAM7-AS1's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without DNAH17 | 0.089 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[MSC-AS1]] | C | MSC-AS1 activity raises ADAM7-AS1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.12× lower at baseline in the lines without MSC-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[NTF3]] | C | NTF3 activity raises ADAM7-AS1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 3.02× lower at baseline in the lines without NTF3 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[KCNMA1]] | C | KCNMA1 activity raises ADAM7-AS1's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 4.38× lower at baseline in the lines without KCNMA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN; co-absent with the target |
| [[LINC00536]] | C | LINC00536 activity raises ADAM7-AS1's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without LINC00536 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN2P46]] | B | ADAM7-AS1 activity raises HMGN2P46's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 3.39× lower at baseline in the lines without ADAM7-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[NEURL3]] | B | ADAM7-AS1 activity raises NEURL3's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without ADAM7-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[EPHB1]] | B | ADAM7-AS1 activity raises EPHB1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without ADAM7-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[TTC23L]] | B | ADAM7-AS1 activity raises TTC23L's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without ADAM7-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[SLC8A1-AS1]] | B | ADAM7-AS1 activity raises SLC8A1-AS1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.42× lower at baseline in the lines without ADAM7-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[CHMP1B-AS1]] | B | ADAM7-AS1 activity raises CHMP1B-AS1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without ADAM7-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[MSC-AS1]] | C | ADAM7-AS1 activity raises MSC-AS1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 5.68× lower at baseline in the lines without ADAM7-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent; co-absent with the target |
| [[OR9Q1]] | C | ADAM7-AS1 activity raises OR9Q1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 2.85× lower at baseline in the lines without ADAM7-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent; co-absent with the target |
| [[IL1A]] | C | ADAM7-AS1 activity raises IL1A's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 2.90× lower at baseline in the lines without ADAM7-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent; co-absent with the target |
| [[NTF3]] | C | ADAM7-AS1 activity raises NTF3's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 2.46× lower at baseline in the lines without ADAM7-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent; co-absent with the target |
| [[KCNMA1]] | C | ADAM7-AS1 activity raises KCNMA1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 6.88× lower at baseline in the lines without ADAM7-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, 0.0); signed map (26.6, 18.9). **Vector** length 65.1, 15.1% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.6 | -4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM7, ADAMDEC1 and ADAM28 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p21.2 — chr8:24,295,814-24,912,073 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56152) · Entrez [101929294](https://www.ncbi.nlm.nih.gov/gene/101929294) · Ensembl [ENSG00000253535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253535)

## Data

Gene col 14811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14811); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14811]; `tensor/DDL_lfc|DDL_z.npy` [14811]; `embed/gene_vectors.npy` [14811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14811 or target_col == 14811). Every well: [[ADAM7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
