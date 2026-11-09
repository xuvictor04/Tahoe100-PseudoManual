---
symbol: "STK32B"
type: "gene"
col: 7674
ensembl_id: "ENSG00000152953"
name: "serine/threonine kinase 32B"
location: "4p16.2"
module: 13
arm: "+"
pooled_cpm: 17.94
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 13
direction_downstream: 13
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# STK32B

*serine/threonine kinase 32B* — 4p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +13.9, q 6e-41, up in 6 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +6.8, q 1e-09, up in 10 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.606× (z -6.6, q 2e-08, down in 7 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSYN2B]] (+0.66, fdr 7e-06), [[EFR3B]] (+0.63, fdr 1e-05), [[COL19A1]] (+0.63, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ARNT2]] → it (grade B ⚠); 13 go from it, the strongest it → [[PCNX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +13.9 | 6e-41 | 6/19 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +10.0 | 4e-21 | 8/16 (RPMI-7951, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.8 | 2e-20 | 4/13 (SW 900, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.8 | 1e-09 | 10/23 (BT-474, Hs 766T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.3 | 4e-08 | 4/22 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +6.1 | 9e-08 | 12/19 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.6 | 2e-06 | 8/24 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.7 | 2e-04 | 9/19 (H4, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 7e-04 | 13/24 (A549, PANC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.20× | +3.7 | 0.014 | 4/24 (A549, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.021 | 10/23 (A549, BT-474, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.5 | 0.025 | 3/15 (PANC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.027 | 4/23 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.058 | 0/23 | inconsistent across doses |  |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.079 | 0/24 | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.095 | 2/24 (NCI-H460, H4) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.606×** | -6.6 | 2e-08 | 7/24 (SW 1088, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -6.0 | 4e-07 | 14/24 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.671×** | -5.9 | 9e-07 | 12/24 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.695×** | -5.0 | 8e-05 | 12/24 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.804×** | -4.4 | 0.001 | 10/24 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.778×** | -4.3 | 0.002 | 12/23 (Hs 766T, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.002 | 10/24 (HOP62, SNU-423, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.751×** | -4.1 | 0.003 | 14/24 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.777×** | -4.1 | 0.003 | 13/24 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.578×** | -4.1 | 0.003 | 5/23 (HOP62, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.004 | 13/24 (SK-MEL-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.013 | 15/24 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.025 | 13/21 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.787×** | -3.4 | 0.026 | 7/24 (HS-578T, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.810×** | -3.0 | 0.099 | 7/23 (H4, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 87.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -21.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -15.7) |
| [[PANC-1 (line)]] | alt | 77.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -28.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -21.0) |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 72.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -24.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.6) |
| [[HS-578T (line)]] | alt | 70.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 52.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.9) |
| [[HOP62 (line)]] | alt | 44.6 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.625× (z -11.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -8.5) |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0923× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.180× (z -9.3) |
| [[A549 (line)]] | wt | 43.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 8.45 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0600× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0957× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 5.95 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSYN2B]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[EFR3B]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[FRMD4A]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HS3ST3A1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[AFF3]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CNIH3]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DOCK2]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[EVC]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RHOJ]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[KCNQ5]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARNT2]] | B | ARNT2 activity raises STK32B's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without ARNT2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[ZNF704]] | B | ZNF704 activity raises STK32B's level | lines that do not express ZNF704 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without ZNF704 | 0.028 | ⚠ within organs, on part of the lines |
| [[RASA3]] | B | RASA3 activity raises STK32B's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without RASA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[PDE10A]] | B | PDE10A activity raises STK32B's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.53× lower at baseline in the lines without PDE10A | 0.063 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[TRIM9]] | C | TRIM9 activity raises STK32B's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 4.47× lower at baseline in the lines without TRIM9 | 0.002 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises STK32B's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 4.88× lower at baseline in the lines without C10orf90 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises STK32B's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.38× lower at baseline in the lines without FRMD4A | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[RNF182]] | C | RNF182 activity raises STK32B's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 4.31× lower at baseline in the lines without RNF182 | 0.025 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615; co-absent with the target |
| [[AFF3]] | C | AFF3 activity raises STK32B's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.46× lower at baseline in the lines without AFF3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX; co-absent with the target |
| [[SDC2]] | C | SDC2 activity raises STK32B's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 3.20× lower at baseline in the lines without SDC2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[CYGB]] | C | CYGB activity raises STK32B's level | lines that do not express CYGB (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without CYGB | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent; co-absent with the target |
| [[EHD3]] | C | EHD3 activity raises STK32B's level | lines that do not express EHD3 (14) vs lines expressing it (36) | 4.01× lower at baseline in the lines without EHD3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MAP9, EVC, AKR1B1; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCNX2]] | B | STK32B activity raises PCNX2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without STK32B | 0.042 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[TMSB15B]] | B | STK32B activity raises TMSB15B's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without STK32B | 0.048 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[RASA3]] | B | STK32B activity raises RASA3's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.63× lower at baseline in the lines without STK32B | 0.055 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[SYNJ2]] | B | STK32B activity raises SYNJ2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.54× lower at baseline in the lines without STK32B | 0.058 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[ARNT2]] | B | STK32B activity raises ARNT2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without STK32B | 0.073 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[SETBP1]] | C | STK32B activity raises SETBP1's level | lines that do not express STK32B (24) vs lines expressing it (26) | 5.19× lower at baseline in the lines without STK32B | 0.012 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[TRIM9]] | C | STK32B activity raises TRIM9's level | lines that do not express STK32B (24) vs lines expressing it (26) | 3.61× lower at baseline in the lines without STK32B | 0.043 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[MEG8]] | C | STK32B activity raises MEG8's level | lines that do not express STK32B (24) vs lines expressing it (26) | 3.93× lower at baseline in the lines without STK32B | 0.071 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[COL15A1]] | C | STK32B activity raises COL15A1's level | lines that do not express STK32B (24) vs lines expressing it (26) | 2.32× lower at baseline in the lines without STK32B | 0.077 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[EHD3]] | C | STK32B activity raises EHD3's level | lines that do not express STK32B (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without STK32B | 0.085 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[C10orf90]] | C | STK32B activity raises C10orf90's level | lines that do not express STK32B (24) vs lines expressing it (26) | 2.17× lower at baseline in the lines without STK32B | 0.088 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |
| [[TRPV2]] | C | STK32B activity raises TRPV2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without STK32B | 0.091 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.6, 27.5); signed map (21.0, 46.5). **Vector** length 75.6, 20.8% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.9 | +3.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 32B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.2 — chr4:5,051,480-5,500,994 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STKG6, YANK2, STK32, HSA250839 |
| Gene groups (HGNC) | Serine/threonine kinase 32 family |
| Matched by | ensembl_id |

UniProt [Q9NY57](https://www.uniprot.org/uniprotkb/Q9NY57) carries no function annotation.

**Summary**, from NCBI Gene [55351](https://www.ncbi.nlm.nih.gov/gene/55351):

> This gene encodes a serine-threonine protein kinase. Serine-threonine kinases transfer phosphate molecules to the oxygen atoms of serine and threonine. A genomic deletion affecting this gene has been associated with Ellis-van Creveld syndrome, an autosomal recessive skeletal dysplasia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:14217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14217) · Entrez [55351](https://www.ncbi.nlm.nih.gov/gene/55351) · UniProt [Q9NY57](https://www.uniprot.org/uniprotkb/Q9NY57) · Ensembl [ENSG00000152953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152953)

## Data

Gene col 7674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7674); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7674]; `tensor/DDL_lfc|DDL_z.npy` [7674]; `embed/gene_vectors.npy` [7674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7674 or target_col == 7674). Every well: [[STK32B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK32B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
