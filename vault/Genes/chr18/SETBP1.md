---
symbol: "SETBP1"
type: "gene"
col: 7602
ensembl_id: "ENSG00000152217"
name: "SET binding protein 1"
location: "18q12.3"
module: 13
arm: "+"
pooled_cpm: 47.4
n_lines_expressing: 31
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 38
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SETBP1

*SET binding protein 1* — 18q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +10.2, q 8e-22, up in 14 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.474× (z -8.9, q 5e-16, down in 25 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDGA2]] (+0.70, fdr 7e-06), [[AIM2]] (+0.69, fdr 7e-06), [[COL15A1]] (+0.69, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[ZNF521]] → it (grade B ⚠); 19 go from it, the strongest it → [[GLIS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +10.2 | 8e-22 | 14/30 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.1 | 2e-07 | 13/29 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.009 | 12/30 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.016 | 15/29 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.023 | 12/30 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.039 | 17/29 (RPMI-7951, CHP-212, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.31× | +3.2 | 0.10 | 10/29 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.32× | +3.2 | 0.10 | 5/30 (SW1417, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.474×** | -8.9 | 5e-16 | 25/29 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -7.4 | 6e-11 | 24/29 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.546×** | -7.2 | 1e-10 | 19/29 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.549×** | -7.1 | 2e-10 | 24/28 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.565×** | -6.5 | 8e-09 | 18/29 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -6.5 | 8e-09 | 20/29 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -6.1 | 1e-07 | 23/29 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -5.8 | 5e-07 | 20/27 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -5.7 | 8e-07 | 20/29 (C32, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.622×** | -5.6 | 1e-06 | 20/29 (C32, A-172, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.632×** | -5.4 | 3e-06 | 19/29 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -5.4 | 3e-06 | 22/28 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -5.2 | 9e-06 | 17/27 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -5.0 | 3e-05 | 16/29 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.747×** | -4.9 | 4e-05 | 19/30 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.689×** | -4.4 | 4e-04 | 12/27 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.679×** | -4.3 | 5e-04 | 19/28 (C32, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.701×** | -4.2 | 8e-04 | 14/28 (A-172, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 753 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 93.0 | 0 | 9 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.258× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 68.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.216× (z -11.3) |
| [[HOP62 (line)]] | alt | 122 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 49.1 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -13.1) |
| [[H4 (line)]] | wt | 127 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0732× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -12.4) |
| [[A-172 (line)]] | wt | 31.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0863× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.113× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 216 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.176× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 44.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -10.3) |
| [[SHP-77 (line)]] | alt | 159 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.391× (z -9.1) |
| [[BT-474 (line)]] | alt | 40.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +14.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 43.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.287× (z -10.0) |
| [[SW 1088 (line)]] | alt | 237 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0841× (z -8.8) ⚠ toxic · without an alert: [[Pioglitazone (drug)]] 0.5 µM 0.0865× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 45.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -8.6) |
| [[CHP-212 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0768× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HEC-1-A (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +8.6) | — |
| [[A-427 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.94 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDGA2]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[AIM2]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[COL15A1]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ADAM12]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CTHRC1]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[DOCK2]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PTPRD]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SDC2]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[NAV1]] | +0.65 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[MIR3681HG]] | +0.63 | +0.57 / +0.63 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 14, C 24. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF521]] | B | ZNF521 activity raises SETBP1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without ZNF521 | 0.014 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |
| [[SGIP1]] | B | SGIP1 activity raises SETBP1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 4.04× lower at baseline in the lines without SGIP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[IGFBP5]] | B | IGFBP5 activity raises SETBP1's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 5.36× lower at baseline in the lines without IGFBP5 | 0.031 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[NRN1]] | B | NRN1 activity raises SETBP1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 2.09× lower at baseline in the lines without NRN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises SETBP1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without FKBP9P1-1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[SEMA5A]] | B | SEMA5A activity raises SETBP1's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 3.19× lower at baseline in the lines without SEMA5A | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[FZD1]] | B | FZD1 activity raises SETBP1's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 4.95× lower at baseline in the lines without FZD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[HTR1F]] | B | HTR1F activity raises SETBP1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 4.84× lower at baseline in the lines without HTR1F | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[GDNF]] | B | GDNF activity raises SETBP1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.12× lower at baseline in the lines without GDNF | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[MIR3681HG]] | B | MIR3681HG activity raises SETBP1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 4.16× lower at baseline in the lines without MIR3681HG | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[MILR1]] | B | MILR1 activity raises SETBP1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.84× lower at baseline in the lines without MILR1 | 0.083 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[HAS2]] | B | HAS2 activity raises SETBP1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without HAS2 | 0.088 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIS3]] | B | SETBP1 activity raises GLIS3's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.66× lower at baseline in the lines without SETBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[COL13A1]] | B | SETBP1 activity raises COL13A1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.75× lower at baseline in the lines without SETBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[PLXNA4]] | B | SETBP1 activity raises PLXNA4's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without SETBP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[STING1]] | B | SETBP1 activity raises STING1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without SETBP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[TMEM178B]] | C | SETBP1 activity raises TMEM178B's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.05× lower at baseline in the lines without SETBP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[HTR7]] | C | SETBP1 activity raises HTR7's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.70× lower at baseline in the lines without SETBP1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[PRICKLE2]] | C | SETBP1 activity raises PRICKLE2's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 4.80× lower at baseline in the lines without SETBP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[ITGB3]] | C | SETBP1 activity raises ITGB3's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 5.11× lower at baseline in the lines without SETBP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[CLDN14-AS1]] | C | SETBP1 activity raises CLDN14-AS1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.39× lower at baseline in the lines without SETBP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[FRMPD4]] | C | SETBP1 activity raises FRMPD4's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.54× lower at baseline in the lines without SETBP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[MSC-AS1]] | C | SETBP1 activity raises MSC-AS1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 7.02× lower at baseline in the lines without SETBP1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[OR9Q1]] | C | SETBP1 activity raises OR9Q1's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.16× lower at baseline in the lines without SETBP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.5, 18.1); signed map (27.9, 42.2). **Vector** length 104, 35.2% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.5 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | +6.8 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.6 | -4.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | SET binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3 — chr18:44,680,173-45,068,510 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEB, KIAA0437 |
| Matched by | ensembl_id |

UniProt [Q9Y6X0](https://www.uniprot.org/uniprotkb/Q9Y6X0) carries no function annotation.

**Summary**, from NCBI Gene [26040](https://www.ncbi.nlm.nih.gov/gene/26040):

> This gene encodes a protein which contains a several motifs including a ski homology region and a SET-binding region in addition to three nuclear localization signals. The encoded protein has been shown to bind the SET nuclear oncogene which is involved in DNA replication. Mutations in this gene are associated with Schinzel-Giedion midface retraction syndrome. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:15573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15573) · Entrez [26040](https://www.ncbi.nlm.nih.gov/gene/26040) · UniProt [Q9Y6X0](https://www.uniprot.org/uniprotkb/Q9Y6X0) · Ensembl [ENSG00000152217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152217)

## Data

Gene col 7602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7602); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7602]; `tensor/DDL_lfc|DDL_z.npy` [7602]; `embed/gene_vectors.npy` [7602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7602 or target_col == 7602). Every well: [[SETBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
