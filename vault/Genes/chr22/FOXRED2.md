---
symbol: "FOXRED2"
type: "gene"
col: 1936
ensembl_id: "ENSG00000100350"
name: "FAD dependent oxidoreductase domain containing 2"
location: "22q12.3"
module: 51
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# FOXRED2

*FAD dependent oxidoreductase domain containing 2* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.96× (z +12.5, q 5e-33, up in 14 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +7.5, q 5e-12, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.762× (z -4.7, q 7e-04, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5RL]] (+0.70, fdr 7e-06), [[DGAT2]] (+0.57, fdr 1e-05), [[CLN6]] (+0.56, fdr 2e-05); moves opposite to [[C9orf24]] (-0.58, fdr 3e-05), [[TPTEP2-CSNK1E]] (-0.55, fdr 3e-05), [[RHCE]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 4 go from it, the strongest it → [[ALDH5A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.96×** | +12.5 | 5e-33 | 14/18 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.71×** | +12.2 | 1e-31 | 25/29 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.56×** | +11.5 | 3e-28 | 32/44 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.43×** | +10.8 | 4e-25 | 32/43 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.12×** | +8.5 | 3e-15 | 15/23 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.5 | 5e-12 | 28/44 (LoVo, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +6.9 | 3e-10 | 22/42 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.77×** | +6.6 | 3e-09 | 19/36 (HCT15, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.69×** | +6.4 | 1e-08 | 24/44 (SW480, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +5.4 | 3e-06 | 22/42 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +5.3 | 5e-06 | 18/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 20/45 (HOP62, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +5.1 | 2e-05 | 21/44 (HT-29, C32, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 10/45 (HEC-1-A, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.97×** | +4.3 | 6e-04 | 10/35 (SNU-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 10/44 (KATO III, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.002 | 14/43 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 15/42 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.005 | 10/45 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.023 | 8/43 (A-172, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.037 | 12/43 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.077 | 2/42 (HT-29, C32) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.7 | 7e-04 | 22/42 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -4.7 | 7e-04 | 18/43 (KATO III, HT-29, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.053 | 8/43 (H4, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.584×** | -3.4 | 0.080 | 11/28 (NCI-H2030, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.21 | 11/44 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.782× | -3.0 | 0.23 | 12/43 (SNU-423, SW480, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 14.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.07× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 13.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -12.3) |
| [[PANC-1 (line)]] | alt | 9.04 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.9) |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0834× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.186× (z -9.6) |
| [[A-172 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5RL]] | +0.70 | +0.77 / +0.68 | both halves | 7e-06 | same gene group |
| [[DGAT2]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CLN6]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[ACBD6]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[THOP1]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CDK4]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[COQ2]] | +0.54 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[CHIC1]] | +0.54 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[PRRC2A]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MLST8]] | +0.53 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[DHRS4L2]] | +0.53 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[C2CD5]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf24]] | -0.58 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RHCE]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[TAX1BP1]] | -0.53 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[SELENOK]] | -0.52 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ZNHIT1]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PNPLA8]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NMRK1]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[IFT20]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RAB4B]] | -0.49 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[NOXRED1]] | -0.48 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[WDR49]] | -0.48 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises FOXRED2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LRRCC1]] | C | LRRCC1 activity strengthens FOXRED2's drug response | lines that do not express LRRCC1 (4) vs lines expressing it (41) | the lines without LRRCC1 respond the other way (z diff +2.93); strongest at Dinaciclib 5 µM: 0.82x vs 2.92x (z diff +6.0) | 0.059 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LRRCC1]] | C | LRRCC1 activity lowers FOXRED2's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 2.62× higher at baseline in the lines without LRRCC1 | 0.085 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH5A1]] | C | FOXRED2 activity raises ALDH5A1's level | lines that do not express FOXRED2 (3) vs lines expressing it (47) | 4.22× lower at baseline in the lines without FOXRED2 | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[C2CD5]] | C | FOXRED2 activity strengthens C2CD5's drug response | lines that do not express FOXRED2 (3) vs lines expressing it (45) | the lines without FOXRED2 respond 0.63× as strongly (z diff +2.32); strongest at Digitoxin 5 µM: 0.56x vs 0.33x (z diff +3.7) | 0.021 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CYB5RL]] | C | FOXRED2 activity raises CYB5RL's level | lines that do not express FOXRED2 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without FOXRED2 | 0.049 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[WWOX]] | C | FOXRED2 activity raises WWOX's level | lines that do not express FOXRED2 (3) vs lines expressing it (47) | 3.12× lower at baseline in the lines without FOXRED2 | 0.052 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-12.1, 30.0); signed map (5.9, -39.1). **Vector** length 75.2, 14.6% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.8 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.5 | +12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.0 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Afatinib (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | FAD dependent oxidoreductase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,487,190-36,507,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23322, ERFAD |
| Gene groups (HGNC) | Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWF2](https://www.uniprot.org/uniprotkb/Q8IWF2) (FAD-dependent oxidoreductase domain-containing protein 2):

> Probable flavoprotein which may function in endoplasmic reticulum associated degradation (ERAD). May bind non-native proteins in the endoplasmic reticulum and target them to the ubiquitination machinery for subsequent degradation.

**Summary**, from NCBI Gene [80020](https://www.ncbi.nlm.nih.gov/gene/80020):

> Enables flavin adenine dinucleotide binding activity. Involved in ERAD pathway. Located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26264) · Entrez [80020](https://www.ncbi.nlm.nih.gov/gene/80020) · UniProt [Q8IWF2](https://www.uniprot.org/uniprotkb/Q8IWF2) · Ensembl [ENSG00000100350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100350)

## Data

Gene col 1936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1936); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1936]; `tensor/DDL_lfc|DDL_z.npy` [1936]; `embed/gene_vectors.npy` [1936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1936 or target_col == 1936). Every well: [[FOXRED2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXRED2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
