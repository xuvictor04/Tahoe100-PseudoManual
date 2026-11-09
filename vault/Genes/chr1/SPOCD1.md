---
symbol: "SPOCD1"
type: "gene"
col: 5586
ensembl_id: "ENSG00000134668"
name: "SPOC domain containing 1"
location: "1p35.2"
module: 13
arm: "+"
pooled_cpm: 15.17
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 36
direction_downstream: 38
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SPOCD1

*SPOC domain containing 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 5 µM: 1.43× (z +4.8, q 9e-04, up in 13 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.547× (z -8.0, q 5e-13, down in 19 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR68]] (+0.73, fdr 7e-06), [[APCDD1L]] (+0.73, fdr 7e-06), [[CSF1R]] (+0.73, fdr 7e-06); moves opposite to [[SRGN]] (-0.52, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[GPR68]] → it (grade B ⚠); 38 go from it, the strongest it → [[GPR68]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **1.43×** | +4.8 | 9e-04 | 13/22 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +4.6 | 9e-04 | 9/23 (A-172, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.6 | 9e-04 | 2/19 (A498, SNU-423) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.6 | 0.047 | 0/15 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.086 | 7/22 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.086 | 8/21 (Hs 766T, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.547×** | -8.0 | 5e-13 | 19/22 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -6.3 | 1e-07 | 20/22 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.521×** | -6.1 | 2e-07 | 21/22 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.525×** | -6.1 | 2e-07 | 19/22 (RKO, CFPAC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.526×** | -6.1 | 2e-07 | 19/23 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.533×** | -5.9 | 3e-07 | 21/23 (RKO, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.558×** | -5.5 | 3e-06 | 17/23 (SW 900, H4, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -5.0 | 4e-05 | 15/22 (LOX-IMVI, H4, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.577×** | -4.8 | 9e-05 | 12/21 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -4.8 | 9e-05 | 16/23 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.709×** | -4.6 | 2e-04 | 14/22 (Hs 766T, H4, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.622×** | -4.5 | 4e-04 | 14/23 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.626×** | -4.4 | 4e-04 | 17/23 (H4, A498, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.628×** | -4.4 | 5e-04 | 11/22 (H4, CFPAC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.645×** | -4.1 | 0.001 | 13/22 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.656×** | -4.0 | 0.003 | 14/22 (A498, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.647×** | -3.9 | 0.003 | 14/22 (H4, Hs 766T, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -3.8 | 0.005 | 16/22 (NCI-H2347, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 40.0 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0649× (z -19.4) |
| [[RKO (line)]] | wt | 83.1 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -24.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 43.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -20.0) |
| [[SNU-423 (line)]] | alt | 41.7 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0874× (z -14.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 56.3 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -14.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 53.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0728× (z -14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -20.6) |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.5) |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.2) |
| [[HS-578T (line)]] | alt | 61.1 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -12.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.3) |
| [[A-172 (line)]] | wt | 9.35 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0717× (z -12.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 14.4 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.204× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.1) |
| [[J82 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.5) |
| [[A-427 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR68]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CSF1R]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[NLRP1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TMEM200A]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L-DT]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP22]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 | STRING 415 |
| [[ITGA11]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[NAV1]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 8, C 28. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR68]] | B | GPR68 activity raises SPOCD1's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without GPR68 | 0.025 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises SPOCD1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.26× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.035 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[ANXA10]] | B | ANXA10 activity raises SPOCD1's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.38× lower at baseline in the lines without ANXA10 | 0.051 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[HAS2]] | B | HAS2 activity raises SPOCD1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without HAS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[NR3C1]] | B | NR3C1 activity lowers SPOCD1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises SPOCD1's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.58× lower at baseline in the lines without EVA1A-AS | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[NEBL]] | B | NEBL activity lowers SPOCD1's level | lines that do not express NEBL (17) vs lines expressing it (33) | 2.71× higher at baseline in the lines without NEBL | 0.086 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[HRH1]] | B | HRH1 activity raises SPOCD1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.57× lower at baseline in the lines without HRH1 | 0.095 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[EDNRA]] | C | EDNRA activity raises SPOCD1's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 5.77× lower at baseline in the lines without EDNRA | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises SPOCD1's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 5.27× lower at baseline in the lines without FGF5 | 0.001 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[ADAMTS16]] | C | ADAMTS16 activity raises SPOCD1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 4.96× lower at baseline in the lines without ADAMTS16 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises SPOCD1's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 4.32× lower at baseline in the lines without RFX8 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 13, C 25. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR68]] | B | SPOCD1 activity raises GPR68's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without SPOCD1 | 0.019 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[NOTCH2NLA]] | B | SPOCD1 activity raises NOTCH2NLA's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without SPOCD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[KLF7]] | B | SPOCD1 activity strengthens KLF7's drug response | lines that do not express SPOCD1 (16) vs lines expressing it (21) | the lines without SPOCD1 respond 0.64× as strongly (z diff +2.66); strongest at Belinostat 5 µM: 0.74x vs 0.36x (z diff +5.7) | 0.034 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; target measured in part of the lines; artifact flags |
| [[ARL10]] | B | SPOCD1 activity raises ARL10's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without SPOCD1 | 0.056 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[MYO10]] | B | SPOCD1 activity raises MYO10's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without SPOCD1 | 0.066 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[FAM20C]] | B | SPOCD1 activity strengthens FAM20C's drug response | lines that do not express SPOCD1 (13) vs lines expressing it (16) | the lines without SPOCD1 respond 0.64× as strongly (z diff +2.23); strongest at Ixazomib citrate 5 µM: 0.53x vs 0.21x (z diff +4.0) | 0.069 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; target measured in part of the lines; artifact flags |
| [[ARL10]] | B | SPOCD1 activity strengthens ARL10's drug response | lines that do not express SPOCD1 (25) vs lines expressing it (23) | the lines without SPOCD1 respond 0.75× as strongly (z diff +0.39); strongest at Homoharringtonine 5 µM: 0.74x vs 0.31x (z diff +3.9) | 0.076 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; target measured in part of the lines; both ways; artifact flags |
| [[PINLYP]] | B | SPOCD1 activity raises PINLYP's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without SPOCD1 | 0.076 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[CSF1R]] | B | SPOCD1 activity raises CSF1R's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without SPOCD1 | 0.078 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[GDNF-AS1]] | B | SPOCD1 activity raises GDNF-AS1's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without SPOCD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[RGMB]] | B | SPOCD1 activity raises RGMB's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without SPOCD1 | 0.086 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[SH2B3]] | B | SPOCD1 activity raises SH2B3's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.30× lower at baseline in the lines without SPOCD1 | 0.089 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.0, 14.6); signed map (21.3, 47.9). **Vector** length 90.3, 30.0% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.53 to 11); *Collagen degradation* (reactome, mean cos +0.53 to 8); *Collagen chain trimerization* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Triamcinolone (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SPOC domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,790,422-31,816,022 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25348, PPP1R146 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by Piwi-interacting RNAs (piRNAs); Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMY3](https://www.uniprot.org/uniprotkb/Q6ZMY3) (SPOC domain-containing protein 1):

> Protein adapter that acts as an essential executor of PIWIL4-piRNA pathway directed transposon DNA methylation and silencing in the male embryonic germ cells. Recruited to young transposons, which are specifically marked with histone H3 trimethylated at both 'Lys-4' and 'Lys-9' (H3K4me3K9me3), via its association with SPIN1 chromatin reader, and associates with the de novo DNA methylation machinery and repressive chromatin remodeling complexes (By similarity). Following this, PIWIL4 engages …

**Summary**, from NCBI Gene [90853](https://www.ncbi.nlm.nih.gov/gene/90853):

> This gene encodes a protein that belongs to the TFIIS family of transcription factors. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:26338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26338) · Entrez [90853](https://www.ncbi.nlm.nih.gov/gene/90853) · UniProt [Q6ZMY3](https://www.uniprot.org/uniprotkb/Q6ZMY3) · Ensembl [ENSG00000134668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134668)

## Data

Gene col 5586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5586); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5586]; `tensor/DDL_lfc|DDL_z.npy` [5586]; `embed/gene_vectors.npy` [5586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5586 or target_col == 5586). Every well: [[SPOCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
