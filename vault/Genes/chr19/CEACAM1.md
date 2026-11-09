---
symbol: "CEACAM1"
type: "gene"
col: 1254
ensembl_id: "ENSG00000079385"
name: "CEA cell adhesion molecule 1"
location: "19q13.2"
module: 31
arm: "+"
pooled_cpm: 37.23
n_lines_expressing: 23
n_dd_up: 5
n_dd_down: 40
n_dd_up_clean: 3
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 89
direction_downstream: 136
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CEACAM1

*CEA cell adhesion molecule 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.18× (z +8.3, q 7e-14, up in 2 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.45× (z +4.1, q 0.008, up in 12 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.238× (z -22.4, q 0e+00, down in 21 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA0040]] (+0.81, fdr 7e-06), [[INPP5D]] (+0.73, fdr 7e-06), [[B3GNT3]] (+0.69, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 89 arrows point to it, the strongest [[ZNF860]] → it (grade B ⚠); 136 go from it, the strongest it → [[TNFRSF21]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +8.3 | 7e-14 | 2/15 (A-172, HepG2/C3A) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.4 | 1e-05 | 0/21 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.008 | 12/20 (A549, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.0 | 0.010 | 6/20 (LoVo, C32, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.014 | 5/21 (Hs 766T, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.238×** | -22.4 | 0e+00 | 21/21 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.354×** | -11.0 | 1e-25 | 20/20 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -9.1 | 2e-17 | 20/20 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.483×** | -8.0 | 1e-13 | 20/20 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.499×** | -7.7 | 2e-12 | 16/20 (SK-MEL-2, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.525×** | -7.1 | 1e-10 | 20/20 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.538×** | -6.8 | 7e-10 | 18/20 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -5.8 | 4e-07 | 19/22 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.681×** | -5.6 | 2e-06 | 17/21 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.602×** | -5.5 | 2e-06 | 16/22 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.617×** | -5.3 | 5e-06 | 16/21 (C32, AsPC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -5.2 | 9e-06 | 17/20 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -5.1 | 1e-05 | 16/20 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.676×** | -5.1 | 1e-05 | 13/21 (C32, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.611×** | -5.0 | 2e-05 | 14/20 (C32, AsPC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -4.8 | 6e-05 | 17/20 (LoVo, C32, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.664×** | -4.5 | 2e-04 | 12/20 (C32, Hs 766T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 82.3 | 0 | 24 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0401× (z -24.1) |
| [[SW480 (line)]] | alt | 21.3 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.8) |
| [[KATO III (line)]] | alt | 185 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0212× (z -33.9) |
| [[LoVo (line)]] | wt | 60.7 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0344× (z -25.5) |
| [[AsPC-1 (line)]] | alt | 478 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0392× (z -35.8) |
| [[LS 180 (line)]] | wt | 65.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -21.0) |
| [[SW1417 (line)]] | alt | 65.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -23.3) |
| [[CFPAC-1 (line)]] | alt | 61.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0503× (z -30.8) |
| [[HT-29 (line)]] | alt | 130 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0877× (z -19.4) |
| [[COLO 205 (line)]] | alt | 70.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0612× (z -21.0) |
| [[Hs 766T (line)]] | wt | 72.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -20.3) |
| [[BT-474 (line)]] | alt | 38.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.0) |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0947× (z -13.6) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0696× (z -12.5) |
| [[A549 (line)]] | wt | 22.2 | 1 | 1 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 8.19× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.0697× (z -16.7) |
| [[HepG2_C3A (line)]] | wt | 52.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 51.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -22.0) |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -17.9) |
| [[A-427 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0040]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Cell surface interactions at the vascular wall |
| [[B3GNT3]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SDR16C5]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LEMD1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[BLACAT1]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[DSG3]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LAMA3]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SLC6A14]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MST1R]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 11, C 78. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | ZNF860 activity raises CEACAM1's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without ZNF860 | 0.024 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[MAP2K1]] | B | MAP2K1 activity raises CEACAM1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.8% of all compounds | 0.038 | ⚠ off-target possible; 4 compounds |
| [[IQANK1]] | B | IQANK1 activity raises CEACAM1's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.94× lower at baseline in the lines without IQANK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity lowers CEACAM1's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.65× higher at baseline in the lines without DCLK2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[KLF5]] | B | KLF5 activity raises CEACAM1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without KLF5 | 0.048 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises CEACAM1's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without SRMS | 0.052 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises CEACAM1's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.97× lower at baseline in the lines without TNFRSF21 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[B4GALNT3]] | B | B4GALNT3 activity raises CEACAM1's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without B4GALNT3 | 0.080 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[LGALS9]] | B | LGALS9 activity raises CEACAM1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.52× lower at baseline in the lines without LGALS9 | 0.087 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[PKP2]] | B | PKP2 activity raises CEACAM1's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without PKP2 | 0.088 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[ST3GAL1]] | B | ST3GAL1 activity raises CEACAM1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without ST3GAL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[CEACAM6]] | C | CEACAM6 activity raises CEACAM1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 7.35× lower at baseline in the lines without CEACAM6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |

### Downstream of this gene

*136 arrows, 136 of them with an alert ⚠; grade A 0, B 57, C 79. Shown: the 12 strongest; 124 more arrows (124 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF21]] | B | CEACAM1 activity raises TNFRSF21's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 4.52× lower at baseline in the lines without CEACAM1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[ABHD17C]] | B | CEACAM1 activity raises ABHD17C's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.57× lower at baseline in the lines without CEACAM1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[KIF13B]] | B | CEACAM1 activity raises KIF13B's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[KLF5]] | B | CEACAM1 activity raises KLF5's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.72× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[PTK2B]] | B | CEACAM1 activity raises PTK2B's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[PLEKHM1P1]] | B | CEACAM1 activity raises PLEKHM1P1's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.51× lower at baseline in the lines without CEACAM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[PTK6]] | B | CEACAM1 activity raises PTK6's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without CEACAM1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[LGALS9]] | B | CEACAM1 activity raises LGALS9's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without CEACAM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[SDCBP2]] | B | CEACAM1 activity raises SDCBP2's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.22× lower at baseline in the lines without CEACAM1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[TLDC2]] | B | CEACAM1 activity raises TLDC2's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without CEACAM1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[SNRK]] | B | CEACAM1 activity raises SNRK's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without CEACAM1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[SOX13]] | B | CEACAM1 activity raises SOX13's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without CEACAM1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 53.1); signed map (59.4, 10.5). **Vector** length 112, 43.5% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.5 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -5.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | CEA cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,507,304-42,561,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BGP1, CD66a; previously BGP |
| Gene groups (HGNC) | CD molecules; V-set domain containing; CEA cell adhesion molecule family |
| Reactome | 9 pathways, smallest: Regulation of MITF-M dependent genes involved in invasion; Fibronectin matrix formation; Cell surface interactions at the vascular wall |
| Matched by | ensembl_id |

**Function**, from UniProt [P13688](https://www.uniprot.org/uniprotkb/P13688) (Cell adhesion molecule CEACAM1):

> [Isoform 1]: Cell adhesion protein that mediates homophilic cell adhesion in a calcium-independent manner (By similarity). Plays a role as coinhibitory receptor in immune response, insulin action and also functions as an activator during angiogenesis. Its coinhibitory receptor function is phosphorylation- and PTPN6 -dependent, which in turn, suppress signal transduction of associated receptors by dephosphorylation of their downstream effectors. Plays a role in immune response, of T cells, …

**Summary**, from NCBI Gene [634](https://www.ncbi.nlm.nih.gov/gene/634):

> This gene encodes a member of the carcinoembryonic antigen (CEA) gene family, which belongs to the immunoglobulin superfamily. Two subgroups of the CEA family, the CEA cell adhesion molecules and the pregnancy-specific glycoproteins, are located within a 1.2 Mb cluster on the long arm of chromosome 19. Eleven pseudogenes of the CEA cell adhesion molecule subgroup are also found in the cluster. The encoded protein was originally described in bile ducts of liver as biliary glycoprotein. …

**Accessions** — [HGNC:1814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1814) · Entrez [634](https://www.ncbi.nlm.nih.gov/gene/634) · UniProt [P13688](https://www.uniprot.org/uniprotkb/P13688) · Ensembl [ENSG00000079385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079385)

## Data

Gene col 1254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1254); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1254]; `tensor/DDL_lfc|DDL_z.npy` [1254]; `embed/gene_vectors.npy` [1254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1254 or target_col == 1254). Every well: [[CEACAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEACAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
