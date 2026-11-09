---
symbol: "NMNAT2"
type: "gene"
col: 8039
ensembl_id: "ENSG00000157064"
name: "nicotinamide nucleotide adenylyltransferase 2"
location: "1q25.3"
module: 13
arm: "+"
pooled_cpm: 14.88
n_lines_expressing: 31
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 4
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NMNAT2

*nicotinamide nucleotide adenylyltransferase 2* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.92× (z +19.9, q 0e+00, up in 22 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.595× (z -6.8, q 7e-09, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSMD2]] (+0.71, fdr 7e-06), [[NES]] (+0.69, fdr 7e-06), [[ADAMTS6]] (+0.68, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SEMA5A]] → it (grade B ⚠); 4 go from it, the strongest it → [[SEMA5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.92×** | +19.9 | 0e+00 | 22/27 (LS 180, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +13.4 | 2e-38 | 7/13 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +12.9 | 6e-36 | 9/19 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.63×** | +12.8 | 4e-35 | 21/25 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +11.5 | 1e-28 | 7/26 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +9.2 | 3e-18 | 19/29 (NCI-H2347, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +7.5 | 5e-12 | 17/28 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +7.3 | 2e-11 | 17/29 (NCI-H1573, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.63×** | +6.5 | 6e-09 | 16/27 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.3 | 2e-08 | 5/16 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.47×** | +6.2 | 3e-08 | 14/26 (NCI-H2347, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.44×** | +4.9 | 6e-05 | 10/27 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 9/25 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.20× | +3.4 | 0.031 | 3/27 (NCI-H2347, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.037 | 2/26 (HEC-1-A, HCT15) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.038 | 3/27 (CFPAC-1, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.061 | 4/25 (HEC-1-A, C32, …) | inconsistent across doses | low cells (technical?) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.084 | 2/28 (HS-578T, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -6.8 | 7e-09 | 16/26 (J82, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -5.0 | 2e-04 | 16/25 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.697×** | -4.7 | 5e-04 | 18/29 (A-427, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.714×** | -4.4 | 0.002 | 15/26 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.742×** | -3.9 | 0.012 | 4/26 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.017 | 11/28 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.5 | 0.033 | 6/29 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.064 | 5/27 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.840× | -3.2 | 0.093 | 9/27 (Hs 766T, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.792× | -3.0 | 0.14 | 11/27 (HOP62, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 89.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.317× (z -9.0) |
| [[A-427 (line)]] | wt | 22.2 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.12× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0683× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -8.6) |
| [[HOP62 (line)]] | alt | 60.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 27.6 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 21.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0540× (z -10.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0752× (z -9.2) |
| [[J82 (line)]] | alt | 57.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 41.3 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.36× (z +11.1) | — |
| [[A-172 (line)]] | wt | 48.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 8.22 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.24× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.38 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.75× (z +10.4) | [[Pemetrexed (drug)]] 0.5 µM 0.0607× (z -13.2) |
| [[C-33 A (line)]] | alt | 8.24 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0679× (z -8.6) ⚠ transcription drop; unreliable plate only |
| [[C32 (line)]] | wt | 3.87 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.5× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.53× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.11 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.00× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 8.34 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.21× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 5.82 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.13× (z +10.7) | — |
| [[A498 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSMD2]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NES]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[PODXL]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[COL15A1]] | +0.67 | +0.57 / +0.63 | both halves | 9e-06 | **novel candidate** |
| [[SPOCK1]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PPFIBP1]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DKK3]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MYO10]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CD44]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA5A]] | B | SEMA5A activity raises NMNAT2's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without SEMA5A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[CSMD2]] | B | CSMD2 activity raises NMNAT2's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without CSMD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[CDH13]] | B | CDH13 activity weakens NMNAT2's drug response | lines that do not express CDH13 (20) vs lines expressing it (9) | the lines without CDH13 respond 3.09× as strongly (z diff -2.51); strongest at Tucidinostat 0.5 µM: 3.88x vs 1.57x (z diff -5.0) | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; target measured in part of the lines; artifact flags |
| [[PKIA]] | B | PKIA activity raises NMNAT2's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.26× lower at baseline in the lines without PKIA | 0.044 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[ONECUT2]] | B | ONECUT2 activity lowers NMNAT2's level | lines that do not express ONECUT2 (10) vs lines expressing it (40) | 2.58× higher at baseline in the lines without ONECUT2 | 0.056 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANGPTL2]] | B | ANGPTL2 activity weakens NMNAT2's drug response | lines that do not express ANGPTL2 (17) vs lines expressing it (12) | the lines without ANGPTL2 respond 2.71× as strongly (z diff -2.34); strongest at Idarubicin (hydrochloride) 5 µM: 1.41x vs 0.63x (z diff -4.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[COL5A3]] | B | COL5A3 activity weakens NMNAT2's drug response | lines that do not express COL5A3 (14) vs lines expressing it (15) | the lines without COL5A3 respond 2.36× as strongly (z diff -2.14); strongest at Tucidinostat 0.5 µM: 3.93x vs 2.26x (z diff -3.7) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1; target measured in part of the lines; artifact flags |
| [[NTM]] | B | NTM activity weakens NMNAT2's drug response | lines that do not express NTM (17) vs lines expressing it (12) | the lines without NTM respond 2.19× as strongly (z diff -1.93); strongest at Tucidinostat 0.5 µM: 4.01x vs 1.97x (z diff -3.8) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; target measured in part of the lines; artifact flags |
| [[PDGFRB]] | B | PDGFRB activity raises NMNAT2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.94× lower at baseline in the lines without PDGFRB | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises NMNAT2's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without HS3ST3A1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[IL1B]] | B | IL1B activity raises NMNAT2's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without IL1B | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[SIRLNT]] | B | SIRLNT activity weakens NMNAT2's drug response | lines that do not express SIRLNT (18) vs lines expressing it (11) | the lines without SIRLNT respond 3.78× as strongly (z diff -2.71); strongest at Idarubicin (hydrochloride) 5 µM: 1.47x vs 0.54x (z diff -5.5) | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; target measured in part of the lines; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA5A]] | B | NMNAT2 activity raises SEMA5A's level | lines that do not express NMNAT2 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without NMNAT2 | 0.045 | ⚠ within organs, on part of the lines; also absent: NTF3, C7orf57, CELF2; maybe low, not absent |
| [[COL13A1]] | B | NMNAT2 activity raises COL13A1's level | lines that do not express NMNAT2 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without NMNAT2 | 0.068 | ⚠ within organs, on part of the lines; also absent: NTF3, C7orf57, CELF2; maybe low, not absent |
| [[DYNLT3]] | B | NMNAT2 activity raises DYNLT3's level | lines that do not express NMNAT2 (19) vs lines expressing it (31) | 1.62× lower at baseline in the lines without NMNAT2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NTF3, C7orf57, CELF2; maybe low, not absent |
| [[AMOTL1]] | C | NMNAT2 activity raises AMOTL1's level | lines that do not express NMNAT2 (19) vs lines expressing it (31) | 3.65× lower at baseline in the lines without NMNAT2 | 0.031 | ⚠ within organs, on part of the lines; also absent: NTF3, C7orf57, CELF2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.9, 15.0); signed map (21.6, 46.2). **Vector** length 71.4, 16.9% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen degradation* (reactome, mean cos +0.51 to 8); *Collagen chain trimerization* (reactome, mean cos +0.53 to 7); *NCAM1 interactions* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +19.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide nucleotide adenylyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,248,237-183,418,380 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0479, PNAT2; previously C1orf15 |
| Reactome | 6 pathways, smallest: Nicotinate metabolism; NAD+ and Sirtuins regulate the circadian clock; Regulation of the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZQ4](https://www.uniprot.org/uniprotkb/Q9BZQ4) (Nicotinamide/nicotinic acid mononucleotide adenylyltransferase 2):

> Nicotinamide/nicotinate-nucleotide adenylyltransferase that acts as an axon maintenance factor (By similarity). Axon survival factor required for the maintenance of healthy axons: acts by delaying Wallerian axon degeneration, an evolutionarily conserved process that drives the loss of damaged axons (By similarity). Catalyzes the formation of NAD(+) from nicotinamide mononucleotide (NMN) and ATP. Can also use the deamidated form; nicotinic acid mononucleotide (NaMN) as substrate but with a lower …

**Summary**, from NCBI Gene [23057](https://www.ncbi.nlm.nih.gov/gene/23057):

> This gene product belongs to the nicotinamide mononucleotide adenylyltransferase (NMNAT) enzyme family, members of which catalyze an essential step in NAD (NADP) biosynthetic pathway. Unlike the other human family member, which is localized to the nucleus, and is ubiquitously expressed; this enzyme is cytoplasmic, and is predominantly expressed in the brain. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16789) · Entrez [23057](https://www.ncbi.nlm.nih.gov/gene/23057) · UniProt [Q9BZQ4](https://www.uniprot.org/uniprotkb/Q9BZQ4) · Ensembl [ENSG00000157064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157064)

## Data

Gene col 8039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8039); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8039]; `tensor/DDL_lfc|DDL_z.npy` [8039]; `embed/gene_vectors.npy` [8039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8039 or target_col == 8039). Every well: [[NMNAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMNAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
