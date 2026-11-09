---
symbol: "GRIN2A"
type: "gene"
col: 11404
ensembl_id: "ENSG00000183454"
name: "glutamate ionotropic receptor NMDA type subunit 2A"
location: "16p13.2"
module: 13
arm: "+"
pooled_cpm: 25.33
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 8
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GRIN2A

*glutamate ionotropic receptor NMDA type subunit 2A* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.33× (z +17.7, q 0e+00, up in 8 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.649× (z -4.5, q 0.003, down in 6 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN6]] (+0.72, fdr 7e-06), [[SLC14A2]] (+0.67, fdr 7e-06), [[EML1]] (+0.66, fdr 9e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 8 go from it, the strongest it → [[CADM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.33×** | +17.7 | 0e+00 | 8/9 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +16.4 | 0e+00 | 1/9 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +10.6 | 4e-24 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +10.5 | 2e-23 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +8.2 | 3e-14 | 2/9 (C32, SK-MEL-2) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.6 | 4e-12 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +4.6 | 4e-04 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.002 | 0/9 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 2/9 (C32, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.008 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.029 | 2/9 (C32, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.034 | 4/9 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.2 | 0.067 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.1 | 0.080 | 1/5 (HS-578T) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.35× | +3.0 | 0.10 | 3/9 (HS-578T, H4, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.649×** | -4.5 | 0.003 | 6/9 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.655×** | -4.4 | 0.003 | 6/9 (H4, SNU-423, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.680×** | -4.0 | 0.011 | 3/9 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.692×** | -3.8 | 0.019 | 7/9 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.788×** | -3.5 | 0.048 | 1/9 (SW 1088) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.048 | 7/9 (SNU-423, H4, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.051 | 7/9 (H4, SNU-423, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.705×** | -3.4 | 0.055 | 6/8 (SNU-423, H4, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.056 | 7/9 (SNU-423, PANC-1, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.732×** | -3.2 | 0.064 | 6/9 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.720×** | -3.2 | 0.064 | 0/9 | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.723×** | -3.2 | 0.070 | 0/9 | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.733×** | -3.1 | 0.081 | 7/9 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Phenytoin (sodium) (drug)]] 0.5 µM |  | **0.743×** | -3.1 | 0.081 | 0/8 | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.746×** | -3.0 | 0.087 | 4/9 (H4, SK-MEL-2, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.747×** | -3.0 | 0.087 | 0/9 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 816 | 0 | 18 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0418× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -20.9) |
| [[PANC-1 (line)]] | alt | 86.7 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 44.3 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0357× (z -13.4) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0754× (z -10.4) |
| [[H4 (line)]] | wt | 14.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +12.7) | [[Dexamethasone (drug)]] 5 µM 0.0212× (z -11.8) |
| [[HS-578T (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.0× (z +21.0) | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0873× (z -9.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.110× (z -9.3) |
| [[A-172 (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN6]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SLC14A2]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[EML1]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 | **novel candidate** |
| [[ABI3BP]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC02968]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LINC01435]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LINC01411]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[AFF3]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SLC8A1]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[VSTM4]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CSF1R]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers GRIN2A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[P2RX7]] | B | P2RX7 activity raises GRIN2A's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without P2RX7 | 0.079 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[COL5A1]] | C | COL5A1 activity raises GRIN2A's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without COL5A1 | 0.038 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises GRIN2A's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without COL7A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises GRIN2A's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.46× lower at baseline in the lines without INSYN2B | 0.061 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[MEG3]] | C | MEG3 activity raises GRIN2A's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.62× lower at baseline in the lines without MEG3 | 0.075 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[MXRA5]] | C | MXRA5 activity raises GRIN2A's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.92× lower at baseline in the lines without MXRA5 | 0.078 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises GRIN2A's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.79× lower at baseline in the lines without MIR493HG | 0.089 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM1]] | B | GRIN2A activity raises CADM1's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 7.29× lower at baseline in the lines without GRIN2A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[LINC01500]] | B | GRIN2A activity raises LINC01500's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 2.51× lower at baseline in the lines without GRIN2A | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[SYNJ2]] | B | GRIN2A activity raises SYNJ2's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without GRIN2A | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[CPQ]] | B | GRIN2A activity raises CPQ's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 4.52× lower at baseline in the lines without GRIN2A | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[P2RX7]] | B | GRIN2A activity raises P2RX7's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 3.47× lower at baseline in the lines without GRIN2A | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[ARHGEF6]] | C | GRIN2A activity raises ARHGEF6's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 2.96× lower at baseline in the lines without GRIN2A | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH; co-absent with the target |
| [[TIMP3]] | C | GRIN2A activity raises TIMP3's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 9.13× lower at baseline in the lines without GRIN2A | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH; co-absent with the target |
| [[ZNF439]] | C | GRIN2A activity raises ZNF439's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 3.36× lower at baseline in the lines without GRIN2A | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 18.6); signed map (28.8, 47.0). **Vector** length 52.3, 20.9% of its response variance represented; |z| ≥ 3 in 356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +8.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.0 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | -0.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor NMDA type subunit 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:9,753,404-10,182,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluN2A, NR2A; previously NMDAR2A |
| Gene groups (HGNC) | Glutamate ionotropic receptor NMDA type subunits |
| Reactome | 14 pathways, smallest: MECP2 regulates neuronal receptors and channels; Synaptic adhesion-like molecules; Unblocking of NMDA receptors, glutamate binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12879](https://www.uniprot.org/uniprotkb/Q12879) (Glutamate receptor ionotropic, NMDA 2A):

> Component of N-methyl-D-aspartate (NMDA) receptors (NMDARs) that function as heterotetrameric, ligand-gated cation channels with high calcium permeability and voltage-dependent block by Mg(2+). NMDARs participate in synaptic plasticity for learning and memory formation by contributing to the slow phase of excitatory postsynaptic current, long-term synaptic potentiation, and learning (By similarity). Channel activation requires binding of the neurotransmitter L-glutamate to the GluN2 subunit, …

**Summary**, from NCBI Gene [2903](https://www.ncbi.nlm.nih.gov/gene/2903):

> This gene encodes a member of the glutamate-gated ion channel protein family. The encoded protein is an N-methyl-D-aspartate (NMDA) receptor subunit. NMDA receptors are both ligand-gated and voltage-dependent, and are involved in long-term potentiation, an activity-dependent increase in the efficiency of synaptic transmission thought to underlie certain kinds of memory and learning. These receptors are permeable to calcium ions, and activation results in a calcium influx into post-synaptic …

**Accessions** — [HGNC:4585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4585) · Entrez [2903](https://www.ncbi.nlm.nih.gov/gene/2903) · UniProt [Q12879](https://www.uniprot.org/uniprotkb/Q12879) · Ensembl [ENSG00000183454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183454)

## Data

Gene col 11404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11404); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11404]; `tensor/DDL_lfc|DDL_z.npy` [11404]; `embed/gene_vectors.npy` [11404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11404 or target_col == 11404). Every well: [[GRIN2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIN2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
