---
symbol: "FZD4"
type: "gene"
col: 10529
ensembl_id: "ENSG00000174804"
name: "frizzled class receptor 4"
location: "11q14.2"
module: 97
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 41
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# FZD4

*frizzled class receptor 4* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.26× (z +17.0, q 0e+00, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.611× (z -5.8, q 5e-06, down in 13 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRSS23-AS1]] (+0.74, fdr 7e-06, ⚠ same locus), [[MPV17L]] (+0.53, fdr 4e-05), [[CBX2]] (+0.53, fdr 3e-05), [[AMPH]] (+0.52, fdr 7e-05); moves opposite to [[CLIP1]] (-0.49, fdr 8e-05), [[HDAC2-AS2]] (-0.47, fdr 2e-04), [[ACTR3C]] (-0.47, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[UNC13A]] → it (grade B ⚠); 5 go from it, the strongest it → [[SNX30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.26×** | +17.0 | 0e+00 | 29/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.08×** | +13.2 | 2e-37 | 28/38 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.00×** | +12.9 | 8e-36 | 27/37 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +10.6 | 3e-24 | 21/38 (J82, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.19×** | +9.2 | 4e-18 | 24/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +6.3 | 2e-08 | 13/38 (J82, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.8 | 6e-07 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.34×** | +5.2 | 1e-05 | 8/36 (PANC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.5 | 4e-04 | 7/32 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 0.002 | 10/37 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 10/29 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.006 | 5/34 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.010 | 5/37 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.010 | 6/29 (RPMI-7951, LS 180, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.37×** | +3.6 | 0.011 | 4/20 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.013 | 8/37 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.018 | 7/37 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10529.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -5.8 | 5e-06 | 13/38 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.724×** | -5.3 | 3e-05 | 14/38 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.649×** | -5.0 | 9e-05 | 7/31 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.881× | -5.0 | 1e-04 | 14/39 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -4.7 | 3e-04 | 10/37 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.690×** | -4.3 | 0.001 | 6/38 (NCI-H460, SNU-423, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -4.0 | 0.006 | 9/37 (RPMI-7951, SNU-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -3.5 | 0.031 | 16/37 (A-427, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.741×** | -3.5 | 0.031 | 10/38 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.820×** | -3.3 | 0.064 | 3/39 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.767×** | -3.1 | 0.099 | 6/38 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.768×** | -3.1 | 0.099 | 10/38 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | 0.696× | -3.0 | 0.11 | 5/38 (MIA PaCa-2, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 5 µM 0.228× (z -8.5) |
| [[Hs 766T (line)]] | wt | 79.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.213× (z -9.6) |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS23-AS1]] | +0.74 | +0.61 / +0.77 | both halves | 7e-06 | ⚠ same locus (20.6 kb, same strand: neighbours can correlate without regulation) |
| [[MPV17L]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[CBX2]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[AMPH]] | +0.52 | +0.38 / +0.53 | both halves | 7e-05 | pathway: Clathrin-mediated endocytosis |
| [[UNC13A]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[RHOBTB2]] | +0.51 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[SH3RF3]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TOX2]] | +0.51 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[FAM102B]] | +0.51 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[JCAD]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TBC1D8]] | +0.50 | +0.41 / +0.38 | both halves | 7e-05 |  |
| [[SLC4A11]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SLC20A1]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIP1]] | -0.49 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[HDAC2-AS2]] | -0.47 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ACTR3C]] | -0.47 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[TMEM217]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.45 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[MED13]] | -0.45 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[AP4S1]] | -0.45 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[PSMD6-AS2]] | -0.43 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[NOXRED1]] | -0.43 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[LINC01829]] | -0.42 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[NMNAT1]] | -0.42 | -0.31 / -0.24 | both halves | 5e-04 |  |
| [[FNBP4]] | -0.42 | -0.38 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC13A]] | B | UNC13A activity raises FZD4's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without UNC13A | 0.029 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[RTN1]] | B | RTN1 activity raises FZD4's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without RTN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530 |
| [[NR3C1]] | B | NR3C1 activity raises FZD4's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ACTR3C]] | B | ACTR3C activity lowers FZD4's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.97× higher at baseline in the lines without ACTR3C | 0.059 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[RIPK4]] | B | RIPK4 activity lowers FZD4's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.77× higher at baseline in the lines without RIPK4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[SLC4A11]] | C | SLC4A11's natural level weakens FZD4's drug response | SLC4A11's natural level across 35 lines (lineage-adjusted; a glimpse) | r -0.74, reverse -0.49; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PRSS23-AS1]] | C | PRSS23-AS1's natural level weakens FZD4's drug response | PRSS23-AS1's natural level across 34 lines (lineage-adjusted; a glimpse) | r -0.75, reverse -0.72; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX30]] | B | FZD4 activity raises SNX30's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without FZD4 | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FOXK1]] | B | FZD4 activity raises FOXK1's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without FZD4 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PODXL2]] | B | FZD4 activity raises PODXL2's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 2.12× lower at baseline in the lines without FZD4 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC00571]] | B | FZD4 activity lowers LINC00571's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.69× higher at baseline in the lines without FZD4 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANKRD28]] | B | FZD4 activity raises ANKRD28's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without FZD4 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 15.3); signed map (18.0, 36.5). **Vector** length 56.5, 8.41% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +17.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +12.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +13.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +10.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.9 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +0.8 | +1.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:86,945,679-86,955,395 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD344; previously EVR1 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled; CD molecules |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 18 pathways, smallest: Signaling by RNF43 mutants; WNT5A-dependent internalization of FZD4; Regulation of FZD by ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULV1](https://www.uniprot.org/uniprotkb/Q9ULV1) (Frizzled-4):

> Receptor for Wnt proteins. Most frizzled receptors are coupled to the beta-catenin (CTNNB1) canonical signaling pathway, which leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin (CTNNB1) and activation of Wnt target genes. Plays a critical role in retinal vascularization by acting as a receptor for Wnt proteins and norrin (NDP) (By similarity). In retina, it can be activated by Wnt protein-binding and also by Wnt-independent …

**Summary**, from NCBI Gene [8322](https://www.ncbi.nlm.nih.gov/gene/8322):

> This gene is a member of the frizzled gene family. Members of this family encode seven-transmembrane domain proteins that are receptors for the Wingless type MMTV integration site family of signaling proteins. Most frizzled receptors are coupled to the beta-catenin canonical signaling pathway. This protein may play a role as a positive regulator of the Wingless type MMTV integration site signaling pathway. A transcript variant retaining intronic sequence and encoding a shorter isoform has been …

**Accessions** — [HGNC:4042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4042) · Entrez [8322](https://www.ncbi.nlm.nih.gov/gene/8322) · UniProt [Q9ULV1](https://www.uniprot.org/uniprotkb/Q9ULV1) · Ensembl [ENSG00000174804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174804)

## Data

Gene col 10529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10529); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10529]; `tensor/DDL_lfc|DDL_z.npy` [10529]; `embed/gene_vectors.npy` [10529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10529 or target_col == 10529). Every well: [[FZD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
