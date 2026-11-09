---
symbol: "LNC-LBCS"
type: "gene"
col: 13642
ensembl_id: "ENSG00000228412"
name: "lncRNA bladder and prostate cancer suppressor, hnRNPK interacting"
location: "6p22.3"
module: 10
arm: "+"
pooled_cpm: 15.79
n_lines_expressing: 37
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LNC-LBCS

*lncRNA bladder and prostate cancer suppressor, hnRNPK interacting* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.05× (z +14.3, q 8e-44, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.648× (z -3.9, q 0.015, down in 16 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STPG2]] (+0.66, fdr 1e-05), [[AGA-DT]] (+0.61, fdr 1e-05), [[RIMS2]] (+0.59, fdr 1e-05); moves opposite to [[KLHL8]] (-0.56, fdr 3e-05), [[SLX9]] (-0.55, fdr 4e-05), [[ANKS6]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[ID2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +14.3 | 8e-44 | 27/32 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +9.8 | 4e-20 | 21/34 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +8.6 | 2e-15 | 25/35 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +8.2 | 3e-14 | 2/14 (SW1417, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +7.4 | 1e-11 | 24/33 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +7.3 | 4e-11 | 11/24 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +7.2 | 6e-11 | 8/21 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.6 | 2e-09 | 19/35 (LS 180, SW1417, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +6.4 | 9e-09 | 21/34 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +6.1 | 6e-08 | 17/35 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +5.9 | 2e-07 | 16/34 (J82, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.6 | 2e-04 | 15/35 (LS 180, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.005 | 13/34 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +3.6 | 0.011 | 13/35 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.030 | 10/35 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.030 | 12/34 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.043 | 15/35 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.063 | 11/35 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -3.9 | 0.015 | 16/34 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.015 | 18/35 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.436×** | -3.9 | 0.015 | 14/29 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -3.6 | 0.042 | 14/34 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.683×** | -3.5 | 0.059 | 9/34 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.059 | 17/35 (NCI-H1573, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.522× | -3.1 | 0.15 | 12/33 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.15 | 10/34 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.529× | -3.0 | 0.16 | 12/35 (SHP-77, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 70.8 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.120× (z -11.3) |
| [[A549 (line)]] | wt | 23.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0873× (z -10.3) |
| [[J82 (line)]] | alt | 4.11 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.0) | [[Rutin (trihydrate) (drug)]] 5 µM 0.0553× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 4.22 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.11× (z +10.3) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.100× (z -10.3) |
| [[AN3 CA (line)]] | alt | 378 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0437× (z -13.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 4.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +9.8) | — |
| [[LoVo (line)]] | wt | 4.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.23× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 5.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.72× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.155× (z -8.9) |
| [[A-172 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 175 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STPG2]] | +0.66 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[AGA-DT]] | +0.61 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[RIMS2]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GPR137C]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ID4]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DRAIC]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 | same gene group |
| [[LINC01116]] | +0.58 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PDCL3P4]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZIC1]] | +0.57 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SPAG17]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PACRG]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[CRB1]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SLX9]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ANKS6]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GTF2H2]] | -0.52 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[NBPF3]] | -0.51 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ZNF692]] | -0.50 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[HDHD5]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[GK5]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[PEX7]] | -0.49 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[XYLT2]] | -0.49 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[KNOP1]] | -0.49 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[PAX9]] | -0.49 | -0.41 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LNC-LBCS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GNG4]] | B | GNG4 activity raises LNC-LBCS's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without GNG4 | 0.055 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[ID2-AS1]] | B | ID2-AS1 activity raises LNC-LBCS's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 3.18× lower at baseline in the lines without ID2-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[ID4]] | C | ID4 activity raises LNC-LBCS's level | lines that do not express ID4 (25) vs lines expressing it (25) | 4.08× lower at baseline in the lines without ID4 | 0.007 | ⚠ within organs, on part of the lines; also absent: CCDC144NL-AS1, ENSG00000264660, ENSG00000289911; co-absent with the target |
| [[SAMD11]] | C | SAMD11 activity raises LNC-LBCS's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 3.23× lower at baseline in the lines without SAMD11 | 0.097 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | LNC-LBCS activity raises ID2-AS1's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without LNC-LBCS | 0.006 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[KRBA2]] | B | LNC-LBCS activity raises KRBA2's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without LNC-LBCS | 0.019 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[ZNF692]] | B | LNC-LBCS activity raises ZNF692's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without LNC-LBCS | 0.044 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[ACYP2]] | B | LNC-LBCS activity raises ACYP2's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without LNC-LBCS | 0.063 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[ANKS6]] | B | LNC-LBCS activity raises ANKS6's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.18× lower at baseline in the lines without LNC-LBCS | 0.082 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[CCDC3]] | B | LNC-LBCS activity lowers CCDC3's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.12× higher at baseline in the lines without LNC-LBCS | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[TUG1]] | B | LNC-LBCS activity weakens TUG1's drug response | lines that do not express LNC-LBCS (13) vs lines expressing it (36) | the lines without LNC-LBCS respond 1.39× as strongly (z diff -0.91); strongest at Idarubicin (hydrochloride) 5 µM: 1.83x vs 1.42x (z diff -2.4) | 0.097 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SAMD11]] | C | LNC-LBCS activity raises SAMD11's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without LNC-LBCS | 0.013 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; co-absent with the target |
| [[ANKS1B]] | C | LNC-LBCS activity raises ANKS1B's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 3.57× lower at baseline in the lines without LNC-LBCS | 0.021 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; co-absent with the target |
| [[ID4]] | C | LNC-LBCS activity raises ID4's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 3.63× lower at baseline in the lines without LNC-LBCS | 0.052 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (19.1, 19.7); signed map (53.1, 19.9). **Vector** length 76.3, 16.6% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA bladder and prostate cancer suppressor, hnRNPK interacting |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.3 — chr6:19,323,428-19,839,080 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LBCS |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54418) · Entrez [100506885](https://www.ncbi.nlm.nih.gov/gene/100506885) · Ensembl [ENSG00000228412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228412)

## Data

Gene col 13642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13642); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13642]; `tensor/DDL_lfc|DDL_z.npy` [13642]; `embed/gene_vectors.npy` [13642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13642 or target_col == 13642). Every well: [[LNC-LBCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNC-LBCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
