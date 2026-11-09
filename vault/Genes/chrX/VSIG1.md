---
symbol: "VSIG1"
type: "gene"
col: 2175
ensembl_id: "ENSG00000101842"
name: "V-set and immunoglobulin domain containing 1"
location: "Xq22.3"
module: 34
arm: "+"
pooled_cpm: 2.53
n_lines_expressing: 17
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 16
direction_downstream: 15
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# VSIG1

*V-set and immunoglobulin domain containing 1* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.78× (z +12.3, q 6e-32, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.24× (z +7.6, q 6e-12, up in 13 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Medroxyprogesterone acetate (drug)]] 0.05 µM: 0.528× (z -4.4, q 0.007, down in 4 of 14 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM163]] (+0.72, fdr 1e-05), [[IL19]] (+0.68, fdr 7e-06), [[EPHB6]] (+0.67, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ICAM2]] → it (grade B ⚠); 15 go from it, the strongest it → [[ABCC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.78×** | +12.3 | 6e-32 | 3/3 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.53×** | +11.4 | 1e-27 | 5/8 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.12×** | +10.1 | 1e-21 | 5/6 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +7.6 | 6e-12 | 13/14 (SW480, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.26×** | +5.4 | 8e-06 | 1/6 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.3 | 1e-05 | 0/13 | top dose only | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.2 | 1e-05 | 2/11 (NCI-H1573, NCI-H2347) | top dose only | cell-cycle shift (explains ~7% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.00×** | +5.2 | 1e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +5.1 | 3e-05 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.9 | 5e-05 | 6/14 (HOP62, SW480, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.05×** | +4.5 | 3e-04 | 0/11 | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +4.5 | 4e-04 | 8/14 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.56×** | +4.4 | 4e-04 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.4 | 4e-04 | 0/11 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +4.2 | 1e-03 | 0/10 | top dose only | cell-cycle shift (explains ~13% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.13×** | +3.6 | 0.012 | 1/9 (NCI-H2347) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +3.1 | 0.054 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.0 | 0.071 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.0 | 0.075 | 1/11 (NCI-H1792) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +2.9 | 0.084 | 0/13 | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.090 | 0/12 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.528×** | -4.4 | 0.007 | 4/14 (NCI-H2347, HOP62, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.539×** | -3.9 | 0.026 | 2/14 (SW480, HEC-1-A) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.559×** | -3.8 | 0.026 | 6/14 (SW480, BT-474, …) | inconsistent across doses | position effect removed |
| [[Asciminib (drug)]] 0.5 µM |  | **0.562×** | -3.7 | 0.026 | 2/14 (A549, NCI-H2347) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.590×** | -3.7 | 0.026 | 5/14 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.605×** | -3.4 | 0.054 | 1/14 (NCI-H2347) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.594×** | -3.3 | 0.068 | 4/14 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.5 µM |  | 0.521× | -3.2 | 0.11 | 2/14 (NCI-H2347, KATO III) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.735× | -3.0 | 0.15 | 6/14 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.626× | -3.0 | 0.15 | 2/13 (NCI-H460, HOP62) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.48 | 0 | 12 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0269× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 6.46 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.191 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.725 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.678 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.273 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM163]] | +0.72 | +0.77 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[IL19]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[EPHB6]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LAMA3]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[LINC00460]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SCAT1]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC02964]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LCK]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DIO3OS]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[FGF19]] | +0.60 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[TNFRSF6B]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[LINC02842]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM2]] | B | ICAM2 activity raises VSIG1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without ICAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[LAMA3]] | B | LAMA3 activity raises VSIG1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without LAMA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[ABCC3]] | B | ABCC3 activity raises VSIG1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without ABCC3 | 0.037 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[TGFA]] | B | TGFA activity raises VSIG1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without TGFA | 0.057 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[HLA-K]] | B | HLA-K activity raises VSIG1's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.69× lower at baseline in the lines without HLA-K | 0.059 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[ACSL5]] | B | ACSL5 activity raises VSIG1's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.38× lower at baseline in the lines without ACSL5 | 0.062 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[LINC02320]] | B | LINC02320 activity raises VSIG1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without LINC02320 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[LEMD1]] | B | LEMD1 activity raises VSIG1's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without LEMD1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[IL19]] | B | IL19 activity raises VSIG1's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without IL19 | 0.090 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[GTF2IP7]] | C | GTF2IP7 activity raises VSIG1's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without GTF2IP7 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises VSIG1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without TINAGL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises VSIG1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without TNNT2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | VSIG1 activity raises ABCC3's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without VSIG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[LINC02842]] | B | VSIG1 activity raises LINC02842's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.67× lower at baseline in the lines without VSIG1 | 0.031 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[CEMIP]] | B | VSIG1 activity raises CEMIP's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without VSIG1 | 0.036 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[TESC]] | B | VSIG1 activity weakens TESC's drug response | lines that do not express VSIG1 (17) vs lines expressing it (8) | the lines without VSIG1 respond 1.35× as strongly (z diff -1.12); strongest at Panobinostat 0.5 µM: 1.96x vs 0.87x (z diff -3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; target measured in part of the lines; artifact flags |
| [[IL19]] | B | VSIG1 activity raises IL19's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.24× lower at baseline in the lines without VSIG1 | 0.072 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[SPTBN5]] | B | VSIG1 activity raises SPTBN5's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.24× lower at baseline in the lines without VSIG1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[SCAT1]] | B | VSIG1 activity raises SCAT1's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.59× lower at baseline in the lines without VSIG1 | 0.081 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[CMTM1]] | B | VSIG1 activity strengthens CMTM1's drug response | lines that do not express VSIG1 (33) vs lines expressing it (14) | the lines without VSIG1 respond 0.68× as strongly (z diff +0.97); strongest at Harringtonine 5 µM: 0.59x vs 0.37x (z diff +2.5) | 0.090 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; target measured in part of the lines; artifact flags |
| [[GTF2IP7]] | C | VSIG1 activity raises GTF2IP7's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without VSIG1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |
| [[PWWP3B]] | C | VSIG1 activity raises PWWP3B's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without VSIG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |
| [[TINAGL1]] | C | VSIG1 activity raises TINAGL1's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 2.32× lower at baseline in the lines without VSIG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |
| [[LINC02964]] | C | VSIG1 activity raises LINC02964's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.16× lower at baseline in the lines without VSIG1 | 0.079 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.0, 7.4); signed map (10.5, 52.7). **Vector** length 32.8, 7.12% of its response variance represented; |z| ≥ 3 in 406 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.7 | +3.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | V-set and immunoglobulin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:108,044,970-108,079,184 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC44287, GPA34 |
| Gene groups (HGNC) | V-set domain containing; IgCAM CXADR-related subfamily |
| Matched by | ensembl_id |

UniProt [Q86XK7](https://www.uniprot.org/uniprotkb/Q86XK7) carries no function annotation.

**Summary**, from NCBI Gene [340547](https://www.ncbi.nlm.nih.gov/gene/340547):

> This gene encodes a member of the junctional adhesion molecule (JAM) family. The encoded protein contains multiple glycosylation sites at the N-terminal region, and multiple phosphorylation sites and glutamic acid/proline (EP) repeats at the C-terminal region. The gene is expressed in normal stomach and testis, as well as in gastric, esophageal and ovarian cancers. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:28675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28675) · Entrez [340547](https://www.ncbi.nlm.nih.gov/gene/340547) · UniProt [Q86XK7](https://www.uniprot.org/uniprotkb/Q86XK7) · Ensembl [ENSG00000101842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101842)

## Data

Gene col 2175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2175); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2175]; `tensor/DDL_lfc|DDL_z.npy` [2175]; `embed/gene_vectors.npy` [2175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2175 or target_col == 2175). Every well: [[VSIG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSIG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
