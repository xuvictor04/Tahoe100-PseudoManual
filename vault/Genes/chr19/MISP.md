---
symbol: "MISP"
type: "gene"
col: 1815
ensembl_id: "ENSG00000099812"
name: "mitotic spindle positioning"
location: "19p13.3"
module: 31
arm: "+"
pooled_cpm: 16.2
n_lines_expressing: 27
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 62
direction_downstream: 81
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MISP

*mitotic spindle positioning* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.57× (z +5.7, q 8e-06, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.494× (z -12.6, q 7e-34, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf116]] (+0.67, fdr 7e-06), [[PLCD3]] (+0.65, fdr 7e-06), [[ABHD11]] (+0.64, fdr 1e-05); moves opposite to [[IKBIP]] (-0.50, fdr 3e-05), [[TCTN3]] (-0.46, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[BICDL2]] → it (grade B ⚠); 81 go from it, the strongest it → [[EZR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 8e-06 | 17/25 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 3e-05 | 16/25 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +3.8 | 0.019 | 11/23 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.019 | 13/25 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +3.8 | 0.019 | 7/21 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.020 | 6/25 (SW480, A498, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.4 | 0.049 | 7/25 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.092 | 10/25 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 5/25 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -12.6 | 7e-34 | 20/24 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -7.3 | 1e-10 | 20/25 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.669×** | -7.2 | 1e-10 | 15/25 (LoVo, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.611×** | -6.0 | 3e-07 | 17/25 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -5.7 | 1e-06 | 16/25 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.648×** | -5.5 | 4e-06 | 14/25 (LoVo, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.653×** | -5.4 | 5e-06 | 14/25 (LoVo, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.668×** | -5.1 | 2e-05 | 15/25 (LoVo, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.662×** | -4.9 | 6e-05 | 12/25 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.717×** | -3.9 | 0.005 | 14/25 (LoVo, A549, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 5 µM |  | 0.630× | -3.1 | 0.11 | 4/25 (A-172, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 86.4 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -31.3) |
| [[SW480 (line)]] | alt | 31.4 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -21.2) |
| [[HT-29 (line)]] | alt | 45.2 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -22.5) |
| [[LS 180 (line)]] | wt | 75.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 41.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 9.04 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.125× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.1) |
| [[KATO III (line)]] | alt | 33.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 7.48 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.167× (z -9.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW48 (line)]] | wt | 20.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0923× (z -14.3) |
| [[A498 (line)]] | wt | 6.19 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 9.23 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -14.6) |
| [[SW1417 (line)]] | alt | 47.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.2) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf116]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PLCD3]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ABHD11]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KLF3]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[HR]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MYH14]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[EZR]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 | STRING 582 |
| [[EPS8L1]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PPL]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PKP3]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKBIP]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TCTN3]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 12, C 50. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICDL2]] | B | BICDL2 activity raises MISP's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.07× lower at baseline in the lines without BICDL2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises MISP's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.23× lower at baseline in the lines without EPS8L1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MYH14]] | B | MYH14 activity raises MISP's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 3.29× lower at baseline in the lines without MYH14 | 0.012 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[LSMEM2]] | B | LSMEM2 activity raises MISP's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 3.14× lower at baseline in the lines without LSMEM2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[STON2]] | B | STON2 activity raises MISP's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.64× lower at baseline in the lines without STON2 | 0.031 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[HR]] | B | HR activity raises MISP's level | lines that do not express HR (23) vs lines expressing it (27) | 2.83× lower at baseline in the lines without HR | 0.043 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[SEMA3B]] | B | SEMA3B activity raises MISP's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without SEMA3B | 0.044 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises MISP's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.98× lower at baseline in the lines without HTR1D | 0.060 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[FLRT3]] | B | FLRT3 activity raises MISP's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without FLRT3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[LMO7]] | B | LMO7 activity raises MISP's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without LMO7 | 0.065 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity raises MISP's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 3.99× lower at baseline in the lines without NOXA1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MISP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 37, C 44. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EZR]] | B | MISP activity raises EZR's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without MISP | 1e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[LINC00592]] | B | MISP activity raises LINC00592's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.93× lower at baseline in the lines without MISP | 3e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[SH3D19]] | B | MISP activity raises SH3D19's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without MISP | 5e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[ARHGAP27]] | B | MISP activity raises ARHGAP27's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without MISP | 6e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[ADAP1]] | B | MISP activity raises ADAP1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.94× lower at baseline in the lines without MISP | 0.002 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[TMEM184A]] | B | MISP activity raises TMEM184A's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.85× lower at baseline in the lines without MISP | 0.002 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[TICAM1]] | B | MISP activity raises TICAM1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without MISP | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[PLCD3]] | B | MISP activity raises PLCD3's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without MISP | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[LMO7]] | B | MISP activity raises LMO7's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.71× lower at baseline in the lines without MISP | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[UNC13D]] | B | MISP activity raises UNC13D's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.80× lower at baseline in the lines without MISP | 0.007 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[NOXA1]] | B | MISP activity raises NOXA1's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without MISP | 0.007 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[EPS8L1]] | B | MISP activity raises EPS8L1's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.24× lower at baseline in the lines without MISP | 0.008 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, 57.1); signed map (52.4, 9.0). **Vector** length 78.1, 22.8% of its response variance represented; |z| ≥ 3 in 577 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.2 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mitotic spindle positioning |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:751,112-764,318 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686H18209, Caprice, MISP1; previously C19orf21 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVT2](https://www.uniprot.org/uniprotkb/Q8IVT2) (Mitotic interactor and substrate of PLK1):

> Plays a role in mitotic spindle orientation and mitotic progression. Regulates the distribution of dynactin at the cell cortex in a PLK1-dependent manner, thus stabilizing cortical and astral microtubule attachments required for proper mitotic spindle positioning. May link microtubules to the actin cytospkeleton and focal adhesions. May be required for directed cell migration and centrosome orientation. May also be necessary for proper stacking of the Golgi apparatus.

**Summary**, from NCBI Gene [126353](https://www.ncbi.nlm.nih.gov/gene/126353):

> The protein encoded by this gene is an actin-bundling protein involved in determining cell morphology and mitotic progression. The encoded protein is required for the proper positioning of the mitotic spindle. Two transcript variants, one protein-coding and the other non-protein coding, have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:27000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27000) · Entrez [126353](https://www.ncbi.nlm.nih.gov/gene/126353) · UniProt [Q8IVT2](https://www.uniprot.org/uniprotkb/Q8IVT2) · Ensembl [ENSG00000099812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099812)

## Data

Gene col 1815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1815); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1815]; `tensor/DDL_lfc|DDL_z.npy` [1815]; `embed/gene_vectors.npy` [1815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1815 or target_col == 1815). Every well: [[MISP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MISP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
