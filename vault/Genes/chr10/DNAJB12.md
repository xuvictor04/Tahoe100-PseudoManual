---
symbol: "DNAJB12"
type: "gene"
col: 7309
ensembl_id: "ENSG00000148719"
name: "DnaJ heat shock protein family (Hsp40) member B12"
location: "10q22.1"
module: 7
arm: "+"
pooled_cpm: 29.42
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DNAJB12

*DnaJ heat shock protein family (Hsp40) member B12* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.83× (z +10.5, q 4e-23, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.430× (z -14.6, q 1e-45, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LANCL2]] (+0.74, fdr 1e-05), [[FEM1A]] (+0.73, fdr 1e-05), [[SNAPC5]] (+0.72, fdr 3e-05); moves opposite to [[NBPF3]] (-0.68, fdr 1e-05), [[ARL3]] (-0.64, fdr 2e-05), [[GMCL1]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +10.5 | 4e-23 | 41/47 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.026 | 15/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.036 | 18/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.038 | 8/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.038 | 15/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.038 | 17/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.038 | 18/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.040 | 15/48 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.3 | 0.066 | 11/48 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.10 | 18/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.11 | 14/48 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.430×** | -14.6 | 1e-45 | 45/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -14.2 | 1e-43 | 47/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.465×** | -13.3 | 6e-38 | 47/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -9.9 | 8e-21 | 42/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -8.0 | 1e-13 | 41/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -8.0 | 2e-13 | 37/47 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -5.7 | 9e-07 | 25/46 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.730×** | -5.4 | 4e-06 | 30/48 (CHP-212, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.552×** | -5.4 | 4e-06 | 27/48 (A498, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.742×** | -5.0 | 4e-05 | 23/47 (NCI-H23, A-427, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.755×** | -4.7 | 1e-04 | 23/47 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.766×** | -4.4 | 4e-04 | 21/47 (C-33 A, A498, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.846× | -4.1 | 0.002 | 16/48 (NCI-H460, SK-MEL-2, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.764×** | -4.0 | 0.003 | 20/48 (AN3 CA, HCT15, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.807×** | -3.6 | 0.013 | 21/48 (AN3 CA, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 43.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 25.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0984× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.351× (z -9.0) |
| [[PANC-1 (line)]] | alt | 37.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.2) |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.118× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -12.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.230× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -10.6) |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.220× (z -10.0) |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -9.0) |
| [[COLO 205 (line)]] | alt | 33.9 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.262× (z -9.1) |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -9.7) |
| [[LoVo (line)]] | wt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -10.3) |
| [[SW480 (line)]] | alt | 32.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.42× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.434× (z -8.9) |
| [[A-427 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[C32 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[H4 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0693× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.218× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -10.6) |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -10.9) |
| [[A-172 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL2]] | +0.74 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.72 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[TRMO]] | +0.71 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ZFX]] | +0.71 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PEF1]] | +0.71 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ZNF830]] | +0.70 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[NUBP1]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ZNF189]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CENPBD1P]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[ARL3]] | -0.64 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.63 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[HDAC3]] | -0.63 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PCTP]] | -0.62 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.62 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[TMEM65]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ORC4]] | -0.61 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PPP1R2]] | -0.61 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.61 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[RAB8B]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.61 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DNAJB12's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-23.4, 11.2); signed map (12.3, -29.7). **Vector** length 103, 23.7% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.3 | -14.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,332,830-72,355,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ10, FLJ20027 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXW2](https://www.uniprot.org/uniprotkb/Q9NXW2) (DnaJ homolog subfamily B member 12):

> Acts as a co-chaperone with HSPA8/Hsc70; required to promote protein folding and trafficking, prevent aggregation of client proteins, and promote unfolded proteins to endoplasmic reticulum-associated degradation (ERAD) pathway. Acts by determining HSPA8/Hsc70's ATPase and polypeptide-binding activities. Can also act independently of HSPA8/Hsc70: together with DNAJB14, acts as a chaperone that promotes maturation of potassium channels KCND2 and KCNH2 by stabilizing nascent channel subunits and …

**Summary**, from NCBI Gene [54788](https://www.ncbi.nlm.nih.gov/gene/54788):

> DNAJB12 belongs to the evolutionarily conserved DNAJ/HSP40 family of proteins, which regulate molecular chaperone activity by stimulating ATPase activity. DNAJ proteins may have up to 3 distinct domains: a conserved 70-amino acid J domain, usually at the N terminus; a glycine/phenylalanine (G/F)-rich region; and a cysteine-rich domain containing 4 motifs resembling a zinc finger domain (Ohtsuka and Hata, 2000 [PubMed 11147971]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14891) · Entrez [54788](https://www.ncbi.nlm.nih.gov/gene/54788) · UniProt [Q9NXW2](https://www.uniprot.org/uniprotkb/Q9NXW2) · Ensembl [ENSG00000148719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148719)

## Data

Gene col 7309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7309); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7309]; `tensor/DDL_lfc|DDL_z.npy` [7309]; `embed/gene_vectors.npy` [7309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7309 or target_col == 7309). Every well: [[DNAJB12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
