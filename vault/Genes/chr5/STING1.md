---
symbol: "STING1"
type: "gene"
col: 11554
ensembl_id: "ENSG00000184584"
name: "stimulator of interferon response cGAMP interactor 1"
location: "5q31.2"
module: 70
arm: "+"
pooled_cpm: 8.63
n_lines_expressing: 33
n_dd_up: 2
n_dd_down: 42
n_dd_up_clean: 2
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 13
direction_downstream: 15
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# STING1

*stimulator of interferon response cGAMP interactor 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Estrone sulfate (potassium) (drug)]] 5 µM: 1.46× (z +3.8, q 0.064, up in 10 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.285× (z -17.4, q 0e+00, down in 27 of 29 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFSF10]] (+0.57, fdr 1e-05), [[PLAAT4]] (+0.54, fdr 5e-05), [[ETV6]] (+0.54, fdr 1e-04); moves opposite to [[NLN]] (-0.44, fdr 1e-04), [[ZSWIM7]] (-0.42, fdr 5e-05), [[METTL5]] (-0.40, fdr 2e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ECSCR]] → it (grade B ⚠); 15 go from it, the strongest it → [[UBA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.064 | 10/30 (Hs 766T, Panc 03.27, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.064 | 10/28 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.65× | +3.4 | 0.14 | 7/28 (LOX-IMVI, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.285×** | -17.4 | 0e+00 | 27/29 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.231×** | -14.4 | 3e-44 | 30/30 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.233×** | -14.3 | 8e-44 | 29/30 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.250×** | -13.6 | 9e-40 | 29/30 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.320×** | -11.1 | 9e-27 | 29/30 (H4, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.356×** | -10.1 | 5e-22 | 25/29 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.413×** | -8.6 | 5e-16 | 21/30 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.415×** | -8.6 | 6e-16 | 26/30 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.447×** | -7.9 | 2e-13 | 22/29 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -7.4 | 7e-12 | 21/29 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.480×** | -7.2 | 4e-11 | 22/30 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.489×** | -7.0 | 1e-10 | 22/30 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -6.4 | 6e-09 | 20/29 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.520×** | -6.1 | 3e-08 | 22/29 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.536×** | -6.1 | 5e-08 | 17/30 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -5.5 | 2e-06 | 13/29 (LOX-IMVI, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.561×** | -5.4 | 2e-06 | 17/30 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.6 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.4) |
| [[Hs 766T (line)]] | wt | 92.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.6) |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0378× (z -22.4) |
| [[H4 (line)]] | wt | 15.0 | 0 | 5 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0222× (z -14.1) |
| [[A-172 (line)]] | wt | 24.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0513× (z -18.7) |
| [[COLO 205 (line)]] | alt | 7.53 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -11.0) |
| [[SHP-77 (line)]] | alt | 8.66 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0659× (z -10.2) |
| [[A498 (line)]] | wt | 18.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.5) |
| [[C32 (line)]] | wt | 15.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -10.8) |
| [[HCT15 (line)]] | alt | 7.54 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -10.8) |
| [[HS-578T (line)]] | alt | 5.48 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0715× (z -9.9) |
| [[LS 180 (line)]] | wt | 5.78 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0338× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 6.55 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0430× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 5.33 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.0304× (z -10.7) |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 5.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -9.1) |
| [[HT-29 (line)]] | alt | 6.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.4) |
| [[LoVo (line)]] | wt | 6.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -9.5) |
| [[SW480 (line)]] | alt | 2.86 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -9.4) |
| [[A-427 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.635 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFSF10]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PLAAT4]] | +0.54 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[ETV6]] | +0.54 | +0.32 / +0.60 | both halves | 1e-04 |  |
| [[MILR1]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[UBA7]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[APOBEC3G]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[LRG1]] | +0.51 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[SCIN]] | +0.51 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[MX2]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[ECSCR]] | +0.50 | +0.51 / +0.45 | both halves | 3e-05 | STRING 434; ⚠ same locus (12.8 kb, same strand: neighbours can correlate without regulation) |
| [[GASAL1]] | +0.50 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[AIM2]] | +0.49 | +0.46 / +0.51 | both halves | 2e-05 | pathway: Cytosolic sensors of pathogen-associated DNA; STRING 582 |
| [[CASP10]] | +0.49 | +0.24 / +0.55 | both halves | 4e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLN]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ZSWIM7]] | -0.42 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[METTL5]] | -0.40 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ECSCR]] | B | ECSCR activity raises STING1's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 3.68× lower at baseline in the lines without ECSCR | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent |
| [[MMP14]] | B | MMP14 activity raises STING1's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 2.85× lower at baseline in the lines without MMP14 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[SAMD3]] | B | SAMD3 activity raises STING1's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without SAMD3 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[ENKUR]] | B | ENKUR activity raises STING1's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without ENKUR | 0.026 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[CD74]] | B | CD74 activity raises STING1's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without CD74 | 0.026 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[UBA7]] | B | UBA7 activity raises STING1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.92× lower at baseline in the lines without UBA7 | 0.034 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises STING1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without PLAAT4 | 0.086 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IKZF2]] | B | IKZF2 activity raises STING1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without IKZF2 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[XAF1]] | B | XAF1 activity raises STING1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without XAF1 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[SETBP1]] | B | SETBP1 activity raises STING1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without SETBP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[STS]] | B | STS activity raises STING1's level | lines that do not express STS (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without STS | 0.096 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[MILR1]] | C | MILR1 activity raises STING1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.16× lower at baseline in the lines without MILR1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 11, C 4. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBA7]] | B | STING1 activity raises UBA7's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without STING1 | 0.010 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[SAMD3]] | B | STING1 activity raises SAMD3's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without STING1 | 0.034 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[AIM2]] | B | STING1 activity raises AIM2's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.75× lower at baseline in the lines without STING1 | 0.036 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[IKBKE]] | B | STING1 activity raises IKBKE's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without STING1 | 0.038 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[ETV6]] | B | STING1 activity raises ETV6's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without STING1 | 0.040 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[CTHRC1]] | B | STING1 activity raises CTHRC1's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without STING1 | 0.048 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[IFITM1]] | B | STING1 activity raises IFITM1's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without STING1 | 0.048 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[CD74]] | B | STING1 activity raises CD74's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without STING1 | 0.057 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[METTL5]] | B | STING1 activity lowers METTL5's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.21× higher at baseline in the lines without STING1 | 0.071 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[ANGPTL2]] | B | STING1 activity raises ANGPTL2's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without STING1 | 0.075 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[ECSCR]] | B | STING1 activity raises ECSCR's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without STING1 | 0.095 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[EVA1A]] | C | STING1 activity raises EVA1A's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without STING1 | 0.005 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.4, 50.9); signed map (58.5, 31.1). **Vector** length 73.8, 18.0% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -8.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | stimulator of interferon response cGAMP interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,475,533-139,482,935 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38577, NET23, ERIS, MPYS, STING, MITA; previously TMEM173 |
| Reactome | 18 pathways, smallest: STAT6-mediated induction of chemokines; IRF3-mediated induction of type I IFN; Regulation of innate immune responses to cytosolic DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WV6](https://www.uniprot.org/uniprotkb/Q86WV6) (Stimulator of interferon genes protein):

> Key innate immune signaling adapter that promotes the production of type I interferon (IFN-alpha and IFN-beta) in response to the presence of DNA from bacteria and viruses in the cytosol. Innate immune response is triggered by non-CpG double-stranded DNA from viruses and bacteria delivered to the cytoplasm, which induces production of cyclic dinucleotides that bind and activate STING1: STING1 recognizes and binds cyclic di-GMP (c-di-GMP), a second messenger produced by bacteria, cyclic UMP-AMP …

**Summary**, from NCBI Gene [340061](https://www.ncbi.nlm.nih.gov/gene/340061):

> This gene encodes a five transmembrane protein that functions as a major regulator of the innate immune response to viral and bacterial infections. The encoded protein is a pattern recognition receptor that detects cytosolic nucleic acids and transmits signals that activate type I interferon responses. The encoded protein has also been shown to play a role in apoptotic signaling by associating with type II major histocompatibility complex. Mutations in this gene are the cause of infantile-onset …

**Accessions** — [HGNC:27962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27962) · Entrez [340061](https://www.ncbi.nlm.nih.gov/gene/340061) · UniProt [Q86WV6](https://www.uniprot.org/uniprotkb/Q86WV6) · Ensembl [ENSG00000184584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184584)

## Data

Gene col 11554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11554); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11554]; `tensor/DDL_lfc|DDL_z.npy` [11554]; `embed/gene_vectors.npy` [11554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11554 or target_col == 11554). Every well: [[STING1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STING1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
