---
symbol: "MTBP"
type: "gene"
col: 10218
ensembl_id: "ENSG00000172167"
name: "MDM2 binding protein"
location: "8q24.12"
module: 71
arm: "+"
pooled_cpm: 40.61
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# MTBP

*MDM2 binding protein* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.63× (z +5.5, q 3e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.725× (z -9.6, q 3e-19, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF519]] (+0.86, fdr 7e-06), [[RFC3]] (+0.84, fdr 7e-06), [[ZGRF1]] (+0.83, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FBLN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +5.5 | 3e-05 | 22/48 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +5.3 | 4e-05 | 22/48 (RKO, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.9 | 1e-04 | 21/48 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.23×** | +4.5 | 1e-03 | 20/48 (NCI-H1792, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.23×** | +4.5 | 1e-03 | 21/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.22×** | +4.2 | 0.002 | 18/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.21×** | +3.9 | 0.007 | 16/46 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.8 | 0.009 | 17/48 (NCI-H2030, RKO, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.009 | 9/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.009 | 10/48 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.011 | 11/48 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.18× | +3.5 | 0.024 | 11/47 (SNU-1, C-33 A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.024 | 8/48 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.17× | +3.4 | 0.028 | 11/48 (J82, RKO, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.040 | 11/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -9.6 | 3e-19 | 29/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -9.2 | 1e-17 | 36/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -6.5 | 2e-08 | 25/48 (H4, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.743×** | -6.3 | 4e-08 | 25/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.767×** | -5.6 | 2e-06 | 25/46 (SK-MEL-2, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.772×** | -5.5 | 3e-06 | 24/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.757×** | -5.5 | 3e-06 | 24/44 (RKO, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.790×** | -5.0 | 4e-05 | 17/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.800×** | -4.8 | 1e-04 | 22/48 (NCI-H2030, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.804×** | -4.6 | 2e-04 | 23/48 (HCT15, SW 1271, …) | two highest doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.672×** | -4.4 | 5e-04 | 16/47 (KATO III, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -4.4 | 5e-04 | 19/47 (HS-578T, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.819×** | -4.3 | 9e-04 | 18/48 (A498, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.815×** | -4.2 | 0.001 | 19/38 (HEC-1-A, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.870× | -4.2 | 0.001 | 10/48 (LS 180, Hs 766T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.715×** | -3.7 | 0.007 | 16/48 (NCI-H1792, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.892× | -3.4 | 0.019 | 10/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.849× | -3.3 | 0.025 | 10/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.742×** | -3.3 | 0.026 | 9/46 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 0.849× | -3.3 | 0.027 | 10/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.752×** | -3.2 | 0.036 | 13/48 (HEC-1-A, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.867× | -3.0 | 0.056 | 12/48 (HCT15, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 69.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.454× (z -13.9) |
| [[A498 (line)]] | wt | 55.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.1) |
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.0) |
| [[H4 (line)]] | wt | 37.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.4) |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 45.6 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0647× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 57.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.4) |
| [[SHP-77 (line)]] | alt | 96.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.5) |
| [[A-427 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.5) |
| [[J82 (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -14.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 50.5 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.98× (z +9.0) | — |
| [[A-172 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF519]] | +0.86 | +0.80 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[RFC3]] | +0.84 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ZGRF1]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | STRING 642 |
| [[TOPBP1]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | STRING 866 |
| [[SPC25]] | +0.82 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[RAD51]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[SPC24]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.80 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[CENPO]] | +0.79 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[CENPK]] | +0.79 | +0.82 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBLN1]] | B | FBLN1 activity lowers MTBP's level | lines that do not express FBLN1 (20) vs lines expressing it (30) | 1.25× higher at baseline in the lines without FBLN1 | 0.059 | ⚠ within organs, on part of the lines; also absent: GJA1, PCSK1N, MLLT11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.870). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.4, -48.1); signed map (-40.7, -42.3). **Vector** length 121, 32.2% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.53 to 4); *IP6 and IP7 transport between cytosol and nucleus* (reactome, mean cos +0.53 to 4); *IPs transport between nucleus and cytosol* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | +4.9 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.3 | +4.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.6 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.8 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.8 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.8 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | MDM2 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:120,445,400-120,542,133 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 9 pathways, smallest: Degradation of CDH1; Regulation of CDH1 Function; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DY7](https://www.uniprot.org/uniprotkb/Q96DY7) (Mdm2-binding protein):

> Inhibits cell migration in vitro and suppresses the invasive behavior of tumor cells (By similarity). May play a role in MDM2-dependent p53/TP53 homeostasis in unstressed cells. Inhibits autoubiquitination of MDM2, thereby enhancing MDM2 stability. This promotes MDM2-mediated ubiquitination of p53/TP53 and its subsequent degradation.

**Summary**, from NCBI Gene [27085](https://www.ncbi.nlm.nih.gov/gene/27085):

> This gene encodes a protein that interacts with the oncoprotein mouse double minute 2. The encoded protein regulates progression through the cell cycle and may be involved in tumor formation. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:7417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7417) · Entrez [27085](https://www.ncbi.nlm.nih.gov/gene/27085) · UniProt [Q96DY7](https://www.uniprot.org/uniprotkb/Q96DY7) · Ensembl [ENSG00000172167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172167)

## Data

Gene col 10218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10218); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10218]; `tensor/DDL_lfc|DDL_z.npy` [10218]; `embed/gene_vectors.npy` [10218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10218 or target_col == 10218). Every well: [[MTBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
