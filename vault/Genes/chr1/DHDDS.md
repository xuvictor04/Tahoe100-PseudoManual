---
symbol: "DHDDS"
type: "gene"
col: 3941
ensembl_id: "ENSG00000117682"
name: "dehydrodolichyl diphosphate synthase subunit"
location: "1p36.11"
module: 56
arm: "+"
pooled_cpm: 61.55
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# DHDDS

*dehydrodolichyl diphosphate synthase subunit* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.65× (z +7.0, q 2e-09, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.446× (z -10.8, q 3e-24, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.581× (z -7.5, q 5e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC13]] (+0.83, fdr 7e-06), [[PMM2]] (+0.78, fdr 7e-06), [[NDEL1]] (+0.77, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.70, fdr 7e-06), [[DCUN1D1]] (-0.69, fdr 7e-06), [[KAT6A]] (-0.65, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +7.0 | 2e-09 | 37/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +6.2 | 2e-07 | 33/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.1 | 2e-07 | 35/48 (LOX-IMVI, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.4 | 1e-05 | 32/48 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.2 | 2e-05 | 31/48 (SNU-1, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +4.9 | 1e-04 | 30/48 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.0 | 0.006 | 24/48 (NCI-H2030, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.025 | 23/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.046 | 20/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.31× | +3.1 | 0.13 | 16/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.13 | 19/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -10.8 | 3e-24 | 36/43 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -10.1 | 2e-21 | 40/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.521×** | -8.7 | 6e-16 | 40/48 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -7.6 | 3e-12 | 34/43 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -7.5 | 5e-12 | 38/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.700×** | -5.9 | 3e-07 | 32/48 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.757×** | -5.0 | 4e-05 | 31/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.692×** | -4.9 | 6e-05 | 27/48 (J82, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.714×** | -4.7 | 2e-04 | 27/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.758×** | -3.8 | 0.007 | 24/47 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.763×** | -3.8 | 0.009 | 26/48 (LS 180, H4, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.021 | 20/47 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.787×** | -3.3 | 0.037 | 23/48 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.788×** | -3.3 | 0.037 | 22/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.790×** | -3.2 | 0.061 | 23/47 (NCI-H2347, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 84.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.8) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.352× (z -10.3) |
| [[HS-578T (line)]] | alt | 129 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.302× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 59.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.5) |
| [[J82 (line)]] | alt | 94.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.3) ⚠ cell-cycle shift, explains ~69% of this change |
| [[C-33 A (line)]] | alt | 51.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.6) | — |
| [[H4 (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 61.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[LOX-IMVI (line)]] | wt | 30.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 57.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 68.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.16× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.3 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[A549 (line)]] | wt | 56.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.258× (z -9.6) |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0701× (z -15.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.245× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC13]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PMM2]] | +0.78 | +0.82 / +0.83 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 410 |
| [[NDEL1]] | +0.77 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[COPA]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CYB561D2]] | +0.76 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[BET1L]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SGSM3]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ZCCHC17]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.74 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.73 | +0.76 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.70 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DCUN1D1]] | -0.69 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[KAT6A]] | -0.65 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.65 | -0.64 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DHDDS's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers DHDDS's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -32.4); signed map (-49.2, 8.3). **Vector** length 142, 47.6% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.63 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.63 to 16); *protein secretion* (hallmark, mean cos +0.60 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.1 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +5.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.8 | +2.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +3.6 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.6 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -10.1 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -9.2 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -7.2 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | dehydrodolichyl diphosphate synthase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,432,282-26,471,306 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDS, FLJ13102, DS, RP59, hCIT |
| Gene groups (HGNC) | Dehydrodolichyl diphosphate synthase |
| Reactome | 7 pathways, smallest: Synthesis of dolichyl-phosphate; Diseases associated with glycosylation precursor biosynthesis; Synthesis of substrates in N-glycan biosythesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SQ9](https://www.uniprot.org/uniprotkb/Q86SQ9) (Dehydrodolichyl diphosphate synthase complex subunit DHDDS):

> With NUS1, forms the dehydrodolichyl diphosphate synthase (DDS) complex, an essential component of the dolichol monophosphate (Dol-P) biosynthetic machinery. Both subunits contribute to enzymatic activity, i.e. condensation of multiple copies of isopentenyl pyrophosphate (IPP) to farnesyl pyrophosphate (FPP) to produce dehydrodolichyl diphosphate (Dedol-PP), a precursor of dolichol phosphate which is utilized as a sugar carrier in protein glycosylation in the endoplasmic reticulum (ER). …

**Summary**, from NCBI Gene [79947](https://www.ncbi.nlm.nih.gov/gene/79947):

> The protein encoded by this gene catalyzes cis-prenyl chain elongation to produce the polyprenyl backbone of dolichol, a glycosyl carrier lipid required for the biosynthesis of several classes of glycoproteins. Mutations in this gene are associated with retinitis pigmentosa type 59. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:20603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20603) · Entrez [79947](https://www.ncbi.nlm.nih.gov/gene/79947) · UniProt [Q86SQ9](https://www.uniprot.org/uniprotkb/Q86SQ9) · Ensembl [ENSG00000117682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117682)

## Data

Gene col 3941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3941); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3941]; `tensor/DDL_lfc|DDL_z.npy` [3941]; `embed/gene_vectors.npy` [3941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3941 or target_col == 3941). Every well: [[DHDDS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHDDS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
