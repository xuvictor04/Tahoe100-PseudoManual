---
symbol: "ABCB6"
type: "gene"
col: 3707
ensembl_id: "ENSG00000115657"
name: "ATP binding cassette subfamily B member 6 (LAN blood group)"
location: "2q35"
module: 103
arm: "+"
pooled_cpm: 12.64
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# ABCB6

*ATP binding cassette subfamily B member 6 (LAN blood group)* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +9.9, q 3e-20, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.433× (z -10.3, q 6e-22, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HA2]] (+0.72, fdr 7e-06), [[FAM219A]] (+0.66, fdr 7e-06), [[TUBA4A]] (+0.63, fdr 1e-05, ⚠ same locus), [[ENO2]] (+0.62, fdr 1e-05); moves opposite to [[NHLRC2]] (-0.60, fdr 4e-05), [[TMBIM4]] (-0.54, fdr 4e-05), [[NAB1]] (-0.53, fdr 2e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +9.9 | 3e-20 | 35/44 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +8.9 | 2e-16 | 37/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +6.1 | 2e-07 | 25/46 (PANC-1, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +5.5 | 5e-06 | 22/46 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.6 | 5e-04 | 21/47 (SHP-77, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +4.0 | 0.005 | 17/45 (A498, NCI-H460, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +3.9 | 0.007 | 18/45 (RKO, LS 180, …) | top dose only | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.011 | 13/46 (NCI-H2030, SW 900, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.020 | 13/46 (J82, NCI-H23, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.035 | 16/46 (SW48, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.29×** | +3.2 | 0.062 | 13/48 (SW480, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.433×** | -10.3 | 6e-22 | 36/46 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.585×** | -6.7 | 8e-09 | 30/44 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.723×** | -5.8 | 1e-06 | 24/44 (NCI-H2030, A-172, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -5.4 | 1e-05 | 20/46 (PANC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -5.1 | 4e-05 | 24/46 (SHP-77, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.683×** | -4.7 | 3e-04 | 19/43 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -4.3 | 0.001 | 16/37 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.2 | 0.002 | 16/42 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.700×** | -4.2 | 0.002 | 17/30 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.731×** | -4.0 | 0.004 | 22/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.746×** | -3.7 | 0.010 | 15/46 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.585×** | -3.5 | 0.021 | 11/44 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.778×** | -3.2 | 0.060 | 20/46 (C-33 A, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.776×** | -3.1 | 0.069 | 14/46 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -9.3) |
| [[C32 (line)]] | wt | 27.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.188× (z -10.2) |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 1 | — | [[(S)-Crizotinib (drug)]] 0.05 µM 0.0459× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0590× (z -10.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 8.50 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0437× (z -13.0) |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0751× (z -11.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 6.50 | 0 | 1 | — | [[Neratinib (maleate) (drug)]] 0.05 µM 0.0641× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0521× (z -11.5) |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.309× (z -8.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0786× (z -8.5) |
| [[PANC-1 (line)]] | alt | 9.63 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -9.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA2]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[FAM219A]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TUBA4A]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 | ⚠ same locus (30.7 kb, same strand: neighbours can correlate without regulation) |
| [[ENO2]] | +0.62 | +0.56 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[GYS1]] | +0.62 | +0.57 / +0.68 | both halves | 8e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[CTDP1]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[RELL2]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RNF122]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DDX41]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TPI1]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[ANKZF1]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; ⚠ same locus (10.8 kb: neighbours can correlate without regulation) |
| [[OGFOD2]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[GPR155]] | +0.58 | +0.42 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.60 | -0.41 / -0.70 | both halves | 4e-05 |  |
| [[TMBIM4]] | -0.54 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NAB1]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[YEATS4]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PEX1]] | -0.52 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[AASDHPPT]] | -0.50 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[TXNRD3]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[HDHD2]] | -0.49 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[C5orf63]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[GMFB]] | -0.49 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[SLC25A24]] | -0.49 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.49 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABCB6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC6A6]] | C | SLC6A6 activity raises ABCB6's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without SLC6A6 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.8, -16.2); signed map (-40.1, 29.8). **Vector** length 94.7, 20.0% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.1 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily B member 6 (LAN blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,209,772-219,218,994 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST45597, umat, MTABC3 |
| Gene groups (HGNC) | Blood group antigens; ATP binding cassette subfamily B |
| Hallmark sets | HEME_METABOLISM, GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Mitochondrial ABC transporters; ABC transporter disorders; ABC-family protein mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP58](https://www.uniprot.org/uniprotkb/Q9NP58) (ATP-binding cassette sub-family B member 6):

> ATP-dependent transporter that catalyzes the transport of a broad-spectrum of porphyrins from the cytoplasm to the extracellular space through the plasma membrane or into the vesicle lumen. May also function as an ATP-dependent importer of porphyrins from the cytoplasm into the mitochondria, in turn may participate in the de novo heme biosynthesis regulation and in the coordination of heme and iron homeostasis during phenylhydrazine stress. May also play a key role in the early steps of …

**Summary**, from NCBI Gene [10058](https://www.ncbi.nlm.nih.gov/gene/10058):

> This gene encodes a member of the ATP-binding cassette (ABC) transporter superfamily. ABC proteins transport various molecules across extra- and intra-cellular membranes. This protein is a member of the heavy metal importer subfamily and plays a role in porphyrin transport. This gene is the molecular basis of the Langereis (Lan) blood group antigen and mutations in this gene underlie familial pseudohyperkalemia and dyschromatosis universalis hereditaria. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:47](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:47) · Entrez [10058](https://www.ncbi.nlm.nih.gov/gene/10058) · UniProt [Q9NP58](https://www.uniprot.org/uniprotkb/Q9NP58) · Ensembl [ENSG00000115657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115657)

## Data

Gene col 3707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3707); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3707]; `tensor/DDL_lfc|DDL_z.npy` [3707]; `embed/gene_vectors.npy` [3707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3707 or target_col == 3707). Every well: [[ABCB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
