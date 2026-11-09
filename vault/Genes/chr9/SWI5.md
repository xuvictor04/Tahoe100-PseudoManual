---
symbol: "SWI5"
type: "gene"
col: 10656
ensembl_id: "ENSG00000175854"
name: "SWI5 homologous recombination repair protein"
location: "9q34.11"
module: 56
arm: "+"
pooled_cpm: 27.84
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SWI5

*SWI5 homologous recombination repair protein* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.32× (z +13.2, q 7e-37, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.493× (z -11.0, q 2e-25, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BET1L]] (+0.72, fdr 7e-06), [[TULP3]] (+0.72, fdr 7e-06), [[DHDDS]] (+0.70, fdr 8e-06); moves opposite to [[PARD3B]] (-0.64, fdr 3e-05), [[HNRNPK]] (-0.62, fdr 1e-05), [[TULP4]] (-0.60, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FBXO16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +13.2 | 7e-37 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +12.3 | 3e-32 | 44/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +10.6 | 4e-24 | 38/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.0 | 2e-17 | 30/47 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.6 | 3e-06 | 25/43 (AsPC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.9 | 8e-05 | 22/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 2e-04 | 23/48 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.3 | 0.001 | 17/32 (CFPAC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 20/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.002 | 16/47 (SNU-423, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.9 | 0.005 | 11/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.006 | 20/47 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.011 | 16/48 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.17× | +3.5 | 0.017 | 18/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.2 | 0.053 | 9/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.072 | 8/48 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.493×** | -11.0 | 2e-25 | 42/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.645×** | -9.7 | 1e-19 | 32/47 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -8.5 | 3e-15 | 36/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -8.4 | 4e-15 | 34/47 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -6.6 | 6e-09 | 25/47 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.662×** | -6.4 | 1e-08 | 35/48 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -6.2 | 4e-08 | 30/46 (J82, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -6.0 | 1e-07 | 27/46 (hTERT-HPNE, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -5.5 | 2e-06 | 25/48 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.725×** | -4.8 | 8e-05 | 20/47 (HS-578T, A498, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.010 | 18/48 (J82, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -3.6 | 0.016 | 18/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -3.5 | 0.024 | 13/30 (H4, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.802×** | -3.4 | 0.026 | 17/48 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.038 | 17/47 (SW480, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.363× (z -8.7) |
| [[H4 (line)]] | wt | 49.3 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.106× (z -13.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.9) |
| [[SW480 (line)]] | alt | 32.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.7 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -12.6) |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -10.5) |
| [[HS-578T (line)]] | alt | 32.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.2) |
| [[J82 (line)]] | alt | 40.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -8.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -9.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 20.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.8) | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -10.7) |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -8.5) |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 19.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -8.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 18.1 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0885× (z -10.4) |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1L]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TULP3]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.70 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[SRP54]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[RARS2]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[COPA]] | +0.67 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA2]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[COG6]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TMED9]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ZNF841]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SGSM3]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARD3B]] | -0.64 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.62 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TULP4]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.59 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO16]] | B | FBXO16 activity lowers SWI5's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without FBXO16 | 0.040 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[SNHG18]] | B | SNHG18 activity raises SWI5's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without SNHG18 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[ARHGAP1]] | C | ARHGAP1's natural level strengthens SWI5's drug response | ARHGAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.17; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.7, -34.1); signed map (-46.6, 12.4). **Vector** length 96.4, 23.7% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +12.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +13.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +2.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.6 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.3 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | SWI5 homologous recombination repair protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,275,379-128,316,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA395P17.9, SAE3; previously C9orf119 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q1ZZU3](https://www.uniprot.org/uniprotkb/Q1ZZU3) (DNA repair protein SWI5 homolog):

> Component of the SWI5-SFR1 complex, a complex required for double-strand break repair via homologous recombination.

**Summary**, from NCBI Gene [375757](https://www.ncbi.nlm.nih.gov/gene/375757):

> Involved in cellular response to ionizing radiation and double-strand break repair via homologous recombination. Located in nucleoplasm. Part of Swi5-Sfr1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31412) · Entrez [375757](https://www.ncbi.nlm.nih.gov/gene/375757) · UniProt [Q1ZZU3](https://www.uniprot.org/uniprotkb/Q1ZZU3) · Ensembl [ENSG00000175854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175854)

## Data

Gene col 10656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10656); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10656]; `tensor/DDL_lfc|DDL_z.npy` [10656]; `embed/gene_vectors.npy` [10656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10656 or target_col == 10656). Every well: [[SWI5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SWI5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
