---
symbol: "ATP8B2"
type: "gene"
col: 6763
ensembl_id: "ENSG00000143515"
name: "ATPase phospholipid transporting 8B2"
location: "1q21.3"
module: 208
arm: "+"
pooled_cpm: 16.62
n_lines_expressing: 40
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# ATP8B2

*ATPase phospholipid transporting 8B2* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.48× (z +6.6, q 2e-08, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.613× (z -8.3, q 4e-14, down in 20 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.635× (z -7.7, q 2e-12, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAB2]] (+0.58, fdr 1e-05), [[CDR2L]] (+0.55, fdr 1e-05), [[GPR173]] (+0.55, fdr 3e-05); moves opposite to [[ENOSF1]] (-0.51, fdr 5e-05), [[CRADD]] (-0.43, fdr 3e-04), [[STAMBPL1]] (-0.42, fdr 2e-04).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGEF6]] → it (grade B ⚠); 2 go from it, the strongest it → [[RHOQ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.48×** | +6.6 | 2e-08 | 21/37 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.5 | 2e-08 | 19/36 (BT-474, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +6.5 | 2e-08 | 23/37 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 2e-04 | 16/38 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.014 | 7/38 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +3.6 | 0.026 | 9/38 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.034 | 11/38 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 1.43× | +3.2 | 0.10 | 7/32 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.13 | 9/38 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.15 | 10/38 (NCI-H460, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.613×** | -8.3 | 4e-14 | 20/34 (NCI-H2030, SW 900, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.619×** | -8.2 | 9e-14 | 22/38 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.631×** | -7.8 | 8e-13 | 20/38 (SW 900, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.635×** | -7.7 | 2e-12 | 20/36 (MIA PaCa-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.660×** | -7.1 | 2e-10 | 21/38 (A-172, SW 900, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.665×** | -7.0 | 3e-10 | 20/38 (SW 900, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -6.9 | 3e-10 | 19/38 (A-172, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.801×** | -5.4 | 6e-06 | 14/36 (HS-578T, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.737×** | -4.8 | 9e-05 | 15/35 (hTERT-HPNE, A-172, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.829×** | -4.5 | 3e-04 | 14/38 (HS-578T, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.759×** | -4.5 | 3e-04 | 14/38 (A-172, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.770×** | -4.5 | 4e-04 | 10/37 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.770×** | -4.4 | 4e-04 | 8/38 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.783×** | -4.2 | 0.001 | 14/38 (HS-578T, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -4.1 | 0.001 | 15/31 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.803×** | -3.8 | 0.006 | 8/38 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.810×** | -3.4 | 0.022 | 9/38 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.043 | 9/38 (NCI-H23, A498, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.715×** | -3.0 | 0.077 | 5/37 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 37.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.436× (z -9.6) |
| [[A-172 (line)]] | wt | 56.7 | 1 | 4 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.78× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.345× (z -10.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.372× (z -9.4) |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 34.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 14.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 5.99× (z +10.6) | — |
| [[H4 (line)]] | wt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~94% of this change |
| [[HepG2_C3A (line)]] | wt | 9.74 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0767× (z -8.6) |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.168× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -8.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.36 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAB2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CDR2L]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GPR173]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SNHG18]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[PTPRN]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ATOSB]] | +0.50 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[NRSN2]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[LTBP4]] | +0.48 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[MAST1]] | +0.48 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[TMOD1]] | +0.47 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[USP35]] | +0.46 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[TTLL7]] | +0.46 | +0.36 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOSF1]] | -0.51 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[CRADD]] | -0.43 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[STAMBPL1]] | -0.42 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[PARP4]] | -0.42 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[NT5DC1]] | -0.41 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[MCTP1]] | -0.41 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NFYC]] | -0.41 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[ATXN7L1]] | -0.41 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[SLC20A2]] | -0.40 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[RGS5]] | -0.39 | -0.40 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF6]] | B | ARHGEF6 activity raises ATP8B2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.86× lower at baseline in the lines without ARHGEF6 | 0.073 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ATP8B2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ATP8B2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOQ]] | B | ATP8B2 activity raises RHOQ's level | lines that do not express ATP8B2 (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without ATP8B2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: CRIP2, NRSN2, TTC28 |
| [[ASAP3]] | B | ATP8B2 activity raises ASAP3's level | lines that do not express ATP8B2 (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without ATP8B2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: CRIP2, NRSN2, TTC28 |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (58.1, 16.6); signed map (-14.9, 51.4). **Vector** length 79.5, 15.5% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.1 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | -7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -6.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 8B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,325,525-154,351,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPID, KIAA1137 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P98198](https://www.uniprot.org/uniprotkb/P98198) (Phospholipid-transporting ATPase ID):

> Catalytic component of P4-ATPase flippase complex, which catalyzes the hydrolysis of ATP coupled to the transport of phosphatidylcholine (PC) from the outer to the inner leaflet of the plasma membrane. May contribute to the maintenance of membrane lipid asymmetry.

**Summary**, from NCBI Gene [57198](https://www.ncbi.nlm.nih.gov/gene/57198):

> The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of aminophospholipid-transporting ATPases. The aminophospholipid translocases transport phosphatidylserine and phosphatidylethanolamine from one side of a bilayer to another. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13534) · Entrez [57198](https://www.ncbi.nlm.nih.gov/gene/57198) · UniProt [P98198](https://www.uniprot.org/uniprotkb/P98198) · Ensembl [ENSG00000143515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143515)

## Data

Gene col 6763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6763); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6763]; `tensor/DDL_lfc|DDL_z.npy` [6763]; `embed/gene_vectors.npy` [6763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6763 or target_col == 6763). Every well: [[ATP8B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
