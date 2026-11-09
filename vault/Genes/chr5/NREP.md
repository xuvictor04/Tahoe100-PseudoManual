---
symbol: "NREP"
type: "gene"
col: 5632
ensembl_id: "ENSG00000134986"
name: "neuronal regeneration related protein"
location: "5q22.1"
module: 152
arm: "+"
pooled_cpm: 33.9
n_lines_expressing: 37
n_dd_up: 21
n_dd_down: 37
n_dd_up_clean: 20
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 31
direction_downstream: 13
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# NREP

*neuronal regeneration related protein* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.58× (z +9.7, q 2e-19, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.254× (z -14.6, q 3e-45, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01013]] (+0.72, fdr 7e-06), [[UNC5C]] (+0.71, fdr 1e-05), [[ARHGAP28]] (+0.67, fdr 7e-06).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[AGBL4]] → it (grade B ⚠); 13 go from it, the strongest it → [[SLC8A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.58×** | +9.7 | 2e-19 | 32/34 (A498, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +8.0 | 5e-13 | 31/35 (A498, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.88×** | +6.5 | 2e-08 | 28/35 (hTERT-HPNE, H4, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.77×** | +6.2 | 1e-07 | 27/35 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +5.7 | 1e-06 | 24/35 (A-172, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 27/35 (NCI-H23, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 2e-05 | 26/35 (NCI-H23, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.80×** | +5.2 | 2e-05 | 28/34 (NCI-H23, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 9e-05 | 25/35 (NCI-H23, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 2e-04 | 23/35 (NCI-H23, hTERT-HPNE, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.59×** | +4.6 | 2e-04 | 26/35 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 3e-04 | 22/35 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 3e-04 | 19/35 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.61×** | +4.2 | 0.001 | 23/35 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 0.001 | 15/35 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.254×** | -14.6 | 3e-45 | 35/35 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.286×** | -13.3 | 6e-38 | 35/35 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.287×** | -13.2 | 9e-38 | 34/35 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.289×** | -13.2 | 2e-37 | 33/35 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.302×** | -12.7 | 5e-35 | 34/35 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.330×** | -11.8 | 4e-30 | 30/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -10.9 | 9e-26 | 25/35 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.356×** | -10.6 | 3e-24 | 28/35 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.375×** | -10.4 | 1e-23 | 32/35 (A-427, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.377×** | -10.0 | 1e-21 | 26/33 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.421×** | -8.7 | 2e-16 | 32/35 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.495×** | -6.3 | 1e-08 | 28/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.577×** | -5.8 | 2e-07 | 23/35 (CHP-212, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.517×** | -5.8 | 3e-07 | 18/35 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.590×** | -5.6 | 8e-07 | 25/35 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -5.4 | 2e-06 | 22/35 (C32, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.564×** | -5.2 | 8e-06 | 19/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.4 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -21.1) |
| [[SW480 (line)]] | alt | 23.4 | 0 | 13 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -15.2) |
| [[C32 (line)]] | wt | 99.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.4) |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -23.6) |
| [[A-427 (line)]] | wt | 66.9 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 31.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 37.6 | 1 (1 ⚠) | 7 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.89× (z +14.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0307× (z -31.7) |
| [[CHP-212 (line)]] | wt | 500 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.170× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 46.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 75.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -19.8) |
| [[AN3 CA (line)]] | alt | 65.0 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0933× (z -10.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -9.7) |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0700× (z -11.6) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.128× (z -9.3) |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -11.9) |
| [[SNU-423 (line)]] | alt | 122 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.317× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 25.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -11.4) |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0648× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 180 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.192× (z -11.9) |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.4) |
| [[A-172 (line)]] | wt | 36.7 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 3.61× (z +8.6) | — |
| [[A498 (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.8) |
| [[A549 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -15.6) |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 50.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.153× (z -9.6) |
| [[HS-578T (line)]] | alt | 140 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.108× (z -9.8) |
| [[J82 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01013]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[UNC5C]] | +0.71 | +0.52 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[ARHGAP28]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45A]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[COL11A1]] | +0.65 | +0.57 / +0.60 | both halves | 9e-06 | **novel candidate** |
| [[ATRNL1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[COL3A1]] | +0.64 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[NEGR1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[COL5A2]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NLGN1]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[LRP2]] | +0.62 | +0.55 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 21, C 10. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGBL4]] | B | AGBL4 activity raises NREP's level | lines that do not express AGBL4 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without AGBL4 | 0.009 | ⚠ within organs, on part of the lines; also absent: RBFOX1, ENSG00000248347; maybe low, not absent |
| [[CSGALNACT1]] | B | CSGALNACT1 activity raises NREP's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without CSGALNACT1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[COL3A1]] | B | COL3A1 activity raises NREP's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 3.77× lower at baseline in the lines without COL3A1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[NEGR1]] | B | NEGR1 activity raises NREP's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.80× lower at baseline in the lines without NEGR1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1 |
| [[TEX41]] | B | TEX41 activity raises NREP's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without TEX41 | 0.035 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[FBXL7]] | B | FBXL7 activity raises NREP's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.81× lower at baseline in the lines without FBXL7 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A |
| [[ATRNL1]] | B | ATRNL1 activity raises NREP's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.23× lower at baseline in the lines without ATRNL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[GXYLT2]] | B | GXYLT2 activity raises NREP's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.90× lower at baseline in the lines without GXYLT2 | 0.050 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[MEF2C-AS1]] | B | MEF2C-AS1 activity raises NREP's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without MEF2C-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[MSC-AS1]] | B | MSC-AS1 activity raises NREP's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.18× lower at baseline in the lines without MSC-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers NREP's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[SLC8A1]] | B | SLC8A1 activity raises NREP's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.59× lower at baseline in the lines without SLC8A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC8A1]] | B | NREP activity raises SLC8A1's level | lines that do not express NREP (13) vs lines expressing it (37) | 4.71× lower at baseline in the lines without NREP | 0.013 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[ATRNL1]] | B | NREP activity raises ATRNL1's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without NREP | 0.054 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[CDK15]] | B | NREP activity raises CDK15's level | lines that do not express NREP (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without NREP | 0.062 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[LINC01013]] | B | NREP activity raises LINC01013's level | lines that do not express NREP (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without NREP | 0.067 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[DIRC3]] | B | NREP activity raises DIRC3's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.16× lower at baseline in the lines without NREP | 0.072 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[PLOD2]] | B | NREP activity raises PLOD2's level | lines that do not express NREP (13) vs lines expressing it (37) | 5.20× lower at baseline in the lines without NREP | 0.072 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[POT1-AS1]] | B | NREP activity raises POT1-AS1's level | lines that do not express NREP (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without NREP | 0.086 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[SNAP25]] | C | NREP activity raises SNAP25's level | lines that do not express NREP (13) vs lines expressing it (37) | 4.96× lower at baseline in the lines without NREP | 0.020 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[PRKD1]] | C | NREP activity raises PRKD1's level | lines that do not express NREP (13) vs lines expressing it (37) | 6.11× lower at baseline in the lines without NREP | 0.027 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[KCTD16]] | C | NREP activity raises KCTD16's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without NREP | 0.028 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[GRIK2]] | C | NREP activity raises GRIK2's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.48× lower at baseline in the lines without NREP | 0.046 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[TMEM45A]] | C | NREP activity raises TMEM45A's level | lines that do not express NREP (13) vs lines expressing it (37) | 4.63× lower at baseline in the lines without NREP | 0.056 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.4, 30.5); signed map (37.2, 34.0). **Vector** length 101, 30.5% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.1 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.0 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +9.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +6.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.6 | -5.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | neuronal regeneration related protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.1 — chr5:111,662,621-111,997,464 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P311, D4S114, PRO1873, PTZ17, SEZ17; previously C5orf13 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16612](https://www.uniprot.org/uniprotkb/Q16612) (Neuronal regeneration-related protein):

> May have roles in neural function. Ectopic expression augments motility of gliomas. Also promotes axonal regeneration (By similarity). May also have functions in cellular differentiation (By similarity). Induces differentiation of fibroblast into myofibroblast and myofibroblast ameboid migration. Increases retinoic-acid regulation of lipid-droplet biogenesis (By similarity). Down-regulates the expression of TGFB1 and TGFB2 but not of TGFB3 (By similarity). May play a role in the regulation of …

**Summary**, from NCBI Gene [9315](https://www.ncbi.nlm.nih.gov/gene/9315):

> Predicted to be involved in axon regeneration; regulation of neuron differentiation; and regulation of transforming growth factor beta receptor signaling pathway. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16834) · Entrez [9315](https://www.ncbi.nlm.nih.gov/gene/9315) · UniProt [Q16612](https://www.uniprot.org/uniprotkb/Q16612) · Ensembl [ENSG00000134986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134986)

## Data

Gene col 5632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5632); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5632]; `tensor/DDL_lfc|DDL_z.npy` [5632]; `embed/gene_vectors.npy` [5632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5632 or target_col == 5632). Every well: [[NREP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NREP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
