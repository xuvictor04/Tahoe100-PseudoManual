---
symbol: "ZDHHC11"
type: "gene"
col: 12053
ensembl_id: "ENSG00000188818"
name: "zDHHC palmitoyltransferase 11"
location: "5p15.33"
module: 47
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# ZDHHC11

*zDHHC palmitoyltransferase 11* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +9.6, q 5e-19, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.614× (z -4.8, q 1e-03, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH8A1]] (+0.76, fdr 7e-06), [[PITRM1-AS1]] (+0.76, fdr 7e-06), [[MMP25]] (+0.75, fdr 7e-06); moves opposite to [[PEX2]] (-0.62, fdr 1e-05), [[USP30]] (-0.60, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[CHPT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +9.6 | 5e-19 | 36/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.5 | 6e-19 | 26/42 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.4 | 7e-15 | 25/41 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +7.0 | 5e-10 | 25/40 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.91×** | +6.3 | 3e-08 | 26/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.7 | 1e-06 | 20/44 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.81×** | +5.6 | 2e-06 | 20/40 (NCI-H460, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +5.3 | 7e-06 | 20/42 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.67×** | +5.0 | 3e-05 | 22/43 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.58×** | +4.3 | 0.001 | 19/42 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +4.1 | 0.002 | 10/23 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.52×** | +4.0 | 0.004 | 5/18 (J82, A498, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +3.9 | 0.004 | 10/41 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +3.8 | 0.006 | 11/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Cinacalcet (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.085 | 5/43 (BT-474, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.614×** | -4.8 | 1e-03 | 22/43 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -4.5 | 0.002 | 18/42 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.730×** | -4.4 | 0.002 | 17/43 (RKO, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -3.9 | 0.012 | 15/42 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.487×** | -3.7 | 0.025 | 13/38 (SW48, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.790×** | -3.3 | 0.099 | 18/43 (RKO, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.721× | -3.2 | 0.11 | 18/42 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.716× | -3.2 | 0.11 | 10/43 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.0 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +20.9) | — |
| [[SW480 (line)]] | alt | 22.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.244× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 11.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 4.69 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.80× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 8.67 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +11.1) | [[Canagliflozin (drug)]] 0.05 µM 0.0843× (z -9.7) |
| [[BT-474 (line)]] | alt | 28.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -8.7) |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0790× (z -9.4) |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0891× (z -11.0) |
| [[Hs 766T (line)]] | wt | 3.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0763× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH8A1]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[MMP25]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[MYH3]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[CHADL]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.73 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[STAC3]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[MPP4]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[USP30]] | -0.60 | -0.58 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZDHHC11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC26A4]] | B | SLC26A4 activity raises ZDHHC11's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without SLC26A4 | 0.030 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises ZDHHC11's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without ASGR1 | 0.061 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[LINC01250]] | B | LINC01250 activity raises ZDHHC11's level | lines that do not express LINC01250 (10) vs lines expressing it (40) | 1.94× lower at baseline in the lines without LINC01250 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises ZDHHC11's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without NEK10 | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[CFAP161]] | B | CFAP161 activity raises ZDHHC11's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without CFAP161 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[LINC02133]] | C | LINC02133 activity raises ZDHHC11's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without LINC02133 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |
| [[TRIM72]] | C | TRIM72 activity raises ZDHHC11's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without TRIM72 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[NECAB2]] | C | NECAB2 activity raises ZDHHC11's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without NECAB2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHPT1]] | C | ZDHHC11 activity raises CHPT1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[UCKL1-AS1]] | C | ZDHHC11 activity raises UCKL1-AS1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[NDFIP1]] | C | ZDHHC11 activity lowers NDFIP1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.33× higher at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[PDPK1]] | C | ZDHHC11 activity raises PDPK1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[ALDH8A1]] | C | ZDHHC11 activity raises ALDH8A1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.53× lower at baseline in the lines without ZDHHC11 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |
| [[CFAP161]] | C | ZDHHC11 activity raises CFAP161's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without ZDHHC11 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.2, -12.4); signed map (18.9, 11.1). **Vector** length 84.4, 17.3% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.2 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:795,605-858,973 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF399, FLJ13153 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 6 pathways, smallest: Maturation of spike protein_9694548; Translation of Structural Proteins_9694635; Late SARS-CoV-2 Infection Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8X9](https://www.uniprot.org/uniprotkb/Q9H8X9) (Palmitoyltransferase ZDHHC11):

> Endoplasmic reticulum-localized palmitoyltransferase that catalyzes the addition of palmitate onto protein substrates (By similarity). Palmitoylates NCDN and thus regulates its association with endosome membranes (By similarity). Also has a palmitoyltransferase activity-independent function in DNA virus-triggered and CGAS-mediated innate immune response. Functions as an adapter that recruits IRF3 to STING1 to promote the activation of that key transcriptional regulator of type I interferon …

**Summary**, from NCBI Gene [79844](https://www.ncbi.nlm.nih.gov/gene/79844):

> Enables signaling adaptor activity. Involved in antiviral innate immune response and positive regulation of defense response to virus by host. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19158) · Entrez [79844](https://www.ncbi.nlm.nih.gov/gene/79844) · UniProt [Q9H8X9](https://www.uniprot.org/uniprotkb/Q9H8X9) · Ensembl [ENSG00000188818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188818)

## Data

Gene col 12053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12053); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12053]; `tensor/DDL_lfc|DDL_z.npy` [12053]; `embed/gene_vectors.npy` [12053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12053 or target_col == 12053). Every well: [[ZDHHC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
