---
symbol: "NRAS"
type: "gene"
col: 13094
ensembl_id: "ENSG00000213281"
name: "NRAS proto-oncogene, GTPase"
location: "1p13.2"
module: 25
arm: "+"
pooled_cpm: 43.36
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# NRAS

*NRAS proto-oncogene, GTPase* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +11.2, q 2e-26, up in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.70× (z +10.5, q 2e-23, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.606× (z -7.7, q 6e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B4]] (+0.81, fdr 7e-06), [[ZNF460]] (+0.81, fdr 7e-06), [[LIN7C]] (+0.79, fdr 7e-06); moves opposite to [[COX5A]] (-0.75, fdr 7e-06, ⚠ COX5A in the vector space only through flagged drug-doses), [[RPL36]] (-0.71, fdr 1e-05), [[LAMTOR5]] (-0.69, fdr 1e-05), [[TMEM258]] (-0.69, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLS3]] → it (grade C ⚠); 2 go from it, the strongest it → [[SRP19]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +11.2 | 2e-26 | 41/46 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +10.5 | 2e-23 | 46/48 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +9.1 | 2e-17 | 32/43 (J82, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +8.5 | 3e-15 | 37/42 (A-427, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +7.0 | 2e-10 | 40/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.8 | 8e-10 | 40/48 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.4 | 7e-06 | 0/48 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.1 | 2e-05 | 32/48 (LoVo, KATO III, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.2 | 0.001 | 26/47 (A-172, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.9 | 0.005 | 26/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +3.6 | 0.015 | 19/48 (HCT15, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.606×** | -7.7 | 6e-12 | 37/48 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.611×** | -7.6 | 7e-12 | 34/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -7.6 | 7e-12 | 37/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -7.1 | 2e-10 | 34/48 (RPMI-7951, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.688×** | -5.8 | 9e-07 | 34/48 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -5.3 | 1e-05 | 32/48 (HS-578T, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.724×** | -5.0 | 5e-05 | 28/48 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.737×** | -4.7 | 2e-04 | 29/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.758×** | -4.1 | 0.003 | 24/48 (NCI-H460, SW48, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.810×** | -3.2 | 0.063 | 21/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.063 | 19/48 (SNU-423, NCI-H2030, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.747×** | -3.2 | 0.064 | 15/48 (RKO, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.856× | -3.0 | 0.11 | 14/48 (SK-MEL-2, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 37.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 46.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.383× (z -8.5) |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0791× (z -10.2) |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0755× (z -9.9) |
| [[J82 (line)]] | alt | 57.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 52.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.24× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 50.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 44.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.87× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 55.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.5) |
| [[SNU-423 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 37.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.42× (z +8.5) | — |
| [[A549 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B4]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.79 | +0.62 / +0.78 | both halves | 7e-06 | pathway: Activation of NMDA receptors and postsynaptic events |
| [[PRELID3B]] | +0.74 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[GMFB]] | +0.72 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[SMU1]] | +0.71 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[PEX19]] | +0.71 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[MAPRE1]] | +0.70 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.70 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[TWF1]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.69 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SSU72]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX5A]] ⚠ | -0.75 | -0.63 / -0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.71 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.69 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.69 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | -0.68 | -0.53 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | -0.67 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[COX6B1]] | -0.67 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[SNHG9]] | -0.67 | -0.50 / -0.72 | both halves | 1e-05 |  |
| [[RPS29]] | -0.67 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.66 | -0.44 / -0.69 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC107]] | -0.66 | -0.36 / -0.65 | both halves | 9e-05 |  |
| [[PTMAP2]] ⚠ | -0.66 | -0.47 / -0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA1]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ATP5MK]] | -0.66 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[LSM2]] | -0.65 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[C4orf48]] | -0.65 | -0.40 / -0.65 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3]] | C | PLS3 activity strengthens NRAS's drug response | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3 respond 0.50× as strongly (z diff +1.57); strongest at Idarubicin (hydrochloride) 5 µM: 1.04x vs 0.67x (z diff +3.6) | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRP19]] | C | NRAS activity raises SRP19's level | recorded gain-of-function mutation of NRAS in 7 lines vs 43 not recorded | 1.32× higher at baseline in the NRAS-altered lines | 0.311 over the table, 0.058 within its group | ⚠ within its group only (a lead); within organs, on part of the lines |
| [[MEI1]] | C | NRAS activity raises MEI1's level | recorded gain-of-function mutation of NRAS in 7 lines vs 43 not recorded | 2.63× higher at baseline in the NRAS-altered lines | 0.499 over the table, 0.062 within its group | ⚠ within its group only (a lead); within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.4, -20.6); signed map (-15.8, -36.8). **Vector** length 120, 33.3% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +11.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.2 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -5.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | NRAS proto-oncogene, GTPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:114,704,469-114,716,771 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N-ras |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 137 pathways, smallest: RAS GTPase cycle mutants; Signaling by RAS GAP mutants; Signaling by RAS GTPase mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P01111](https://www.uniprot.org/uniprotkb/P01111) (GTPase NRas):

> Signal transducer in the Ras-MAPK signaling pathway that regulates cell proliferation and survival. Ras proteins bind GDP/GTP and possess intrinsic GTPase activity. Recognized by LZTR1 that mediates its ubiquitination by a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [4893](https://www.ncbi.nlm.nih.gov/gene/4893):

> This is an N-ras oncogene encoding a membrane protein that shuttles between the Golgi apparatus and the plasma membrane. This shuttling is regulated through palmitoylation and depalmitoylation by the ZDHHC9-GOLGA7 complex. The encoded protein, which has intrinsic GTPase activity, is activated by a guanine nucleotide-exchange factor and inactivated by a GTPase activating protein. Mutations in this gene have been associated with somatic rectal cancer, follicular thyroid cancer, autoimmune …

**Accessions** — [HGNC:7989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7989) · Entrez [4893](https://www.ncbi.nlm.nih.gov/gene/4893) · UniProt [P01111](https://www.uniprot.org/uniprotkb/P01111) · Ensembl [ENSG00000213281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213281)

## Data

Gene col 13094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13094); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13094]; `tensor/DDL_lfc|DDL_z.npy` [13094]; `embed/gene_vectors.npy` [13094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13094 or target_col == 13094). Every well: [[NRAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
