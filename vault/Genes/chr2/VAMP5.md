---
symbol: "VAMP5"
type: "gene"
col: 9719
ensembl_id: "ENSG00000168899"
name: "vesicle associated membrane protein 5"
location: "2p11.2"
module: 23
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 37
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# VAMP5

*vesicle associated membrane protein 5* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.11× (z +7.2, q 3e-10, up in 20 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.419× (z -8.3, q 5e-14, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MR1]] (+0.64, fdr 3e-05), [[C3orf38]] (+0.64, fdr 4e-05), [[VAMP8]] (+0.62, fdr 1e-05, ⚠ same locus), [[BTN2A1]] (+0.61, fdr 3e-05); moves opposite to [[R3HDM1]] (-0.55, fdr 3e-05), [[HERC2]] (-0.53, fdr 6e-05), [[SERBP1]] (-0.53, fdr 8e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VAMP8]] → it (grade B ⚠); 10 go from it, the strongest it → [[VAMP8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +7.2 | 3e-10 | 20/34 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.0 | 5e-07 | 14/22 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.3 | 2e-05 | 5/12 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.3 | 0.002 | 11/25 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 12/31 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.2 | 0.002 | 12/26 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.70× | +3.1 | 0.14 | 3/31 (A-172, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | 1.84× | +3.1 | 0.14 | 1/28 (A-172) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.37× | +3.1 | 0.14 | 6/31 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.68× | +3.0 | 0.15 | 4/32 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.419×** | -8.3 | 5e-14 | 28/35 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.426×** | -8.1 | 1e-13 | 26/35 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -6.9 | 1e-09 | 20/34 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -5.6 | 4e-06 | 16/33 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.597×** | -4.9 | 1e-04 | 11/34 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -4.5 | 6e-04 | 14/34 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -4.4 | 8e-04 | 14/34 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -4.4 | 8e-04 | 16/35 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -4.1 | 0.003 | 10/34 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -4.1 | 0.003 | 11/34 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -3.4 | 0.039 | 10/35 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.693×** | -3.3 | 0.039 | 11/34 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -3.1 | 0.082 | 8/34 (KATO III, A498, …) | rises with dose |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **0.711×** | -3.1 | 0.091 | 4/35 (A-172, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.176× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 5.63 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0568× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.161× (z -8.9) |
| [[C32 (line)]] | wt | 7.59 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0801× (z -8.5) |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -9.0) |
| [[HT-29 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 5.84 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -11.4) |
| [[A-427 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MR1]] | +0.64 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[C3orf38]] | +0.64 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[VAMP8]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 771; ⚠ same locus (2.4 kb, same strand: neighbours can correlate without regulation) |
| [[BTN2A1]] | +0.61 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[COPZ2]] | +0.61 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[N4BP2L1]] | +0.60 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[CCDC59]] | +0.60 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[KLC4]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MOB4]] | +0.58 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[IST1]] | +0.57 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[HOXA-AS2]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R42]] | +0.57 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[WHAMM]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM1]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[HERC2]] | -0.53 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[SERBP1]] | -0.53 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[GMDS]] | -0.52 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[TTLL12]] | -0.51 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[PRKDC]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[CEP83]] | -0.51 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[EFTUD2]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SMYD3]] | -0.51 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[POLD2]] | -0.50 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[CORO1C]] | -0.49 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[RUVBL1]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP8]] | B | VAMP8 activity raises VAMP5's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without VAMP8 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[C1R]] | B | C1R activity raises VAMP5's level | lines that do not express C1R (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without C1R | 0.087 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[PRRG4]] | C | PRRG4 activity raises VAMP5's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without PRRG4 | 0.094 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP8]] | B | VAMP5 activity raises VAMP8's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 3.21× lower at baseline in the lines without VAMP5 | 0.002 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[EFTUD2]] | B | VAMP5 activity lowers EFTUD2's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.33× higher at baseline in the lines without VAMP5 | 0.008 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[PRKDC]] | B | VAMP5 activity lowers PRKDC's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.63× higher at baseline in the lines without VAMP5 | 0.033 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[R3HDM1]] | B | VAMP5 activity lowers R3HDM1's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without VAMP5 | 0.039 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[SERBP1]] | B | VAMP5 activity lowers SERBP1's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without VAMP5 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[CEP83]] | B | VAMP5 activity lowers CEP83's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.44× higher at baseline in the lines without VAMP5 | 0.068 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[MYLK3]] | B | VAMP5 activity lowers MYLK3's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.69× higher at baseline in the lines without VAMP5 | 0.068 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| cells under [[Trifluridine (drug)]] 5 µM | B | VAMP5 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express VAMP5 (13) vs lines expressing it (35) | the lines without VAMP5: 0.88× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | VAMP5 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express VAMP5 (13) vs lines expressing it (35) | the lines without VAMP5: 0.88× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[PRRG4]] | C | VAMP5 activity raises PRRG4's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 3.45× lower at baseline in the lines without VAMP5 | 0.030 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511; co-absent with the target |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (2.6, 25.4); signed map (23.2, -12.2). **Vector** length 49.7, 8.50% of its response variance represented; |z| ≥ 3 in 572 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.7 | -8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,584,431-85,593,406 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Vesicle associated membrane proteins |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [O95183](https://www.uniprot.org/uniprotkb/O95183) (Vesicle-associated membrane protein 5):

> May participate in trafficking events that are associated with myogenesis, such as myoblast fusion and/or GLUT4 trafficking.

**Summary**, from NCBI Gene [10791](https://www.ncbi.nlm.nih.gov/gene/10791):

> Synaptobrevins/VAMPs, syntaxins, and the 25-kD synaptosomal-associated protein are the main components of a protein complex involved in the docking and/or fusion of vesicles and cell membranes. The VAMP5 gene is a member of the vesicle-associated membrane protein (VAMP)/synaptobrevin family and the SNARE superfamily. This VAMP family member may participate in vesicle trafficking events that are associated with myogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12646) · Entrez [10791](https://www.ncbi.nlm.nih.gov/gene/10791) · UniProt [O95183](https://www.uniprot.org/uniprotkb/O95183) · Ensembl [ENSG00000168899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168899)

## Data

Gene col 9719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9719); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9719]; `tensor/DDL_lfc|DDL_z.npy` [9719]; `embed/gene_vectors.npy` [9719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9719 or target_col == 9719). Every well: [[VAMP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
