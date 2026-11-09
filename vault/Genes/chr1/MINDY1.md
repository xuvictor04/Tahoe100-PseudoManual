---
symbol: "MINDY1"
type: "gene"
col: 6738
ensembl_id: "ENSG00000143409"
name: "MINDY lysine 48 deubiquitinase 1"
location: "1q21.3"
module: 29
arm: "+"
pooled_cpm: 5.68
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MINDY1

*MINDY lysine 48 deubiquitinase 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.90× (z +11.1, q 7e-26, up in 29 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 1.28× (z +4.2, q 0.003, up in 8 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.362× (z -12.4, q 1e-32, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN6]] (+0.62, fdr 1e-05), [[LPIN3]] (+0.60, fdr 1e-05), [[HFE]] (+0.60, fdr 2e-05); moves opposite to [[CCM2]] (-0.62, fdr 1e-05), [[TUBB6]] (-0.60, fdr 1e-05), [[MPP3]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MICAL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.90×** | +11.1 | 7e-26 | 29/45 (RKO, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +7.0 | 7e-10 | 13/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.7 | 5e-09 | 5/10 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.003 | 8/45 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.006 | 9/45 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.9 | 0.008 | 9/28 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.011 | 8/45 (SW 900, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.013 | 7/44 (MIA PaCa-2, LOX-IMVI, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.021 | 3/44 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.33×** | +3.5 | 0.030 | 7/43 (AsPC-1, HCT15, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.362×** | -12.4 | 1e-32 | 32/45 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.623×** | -8.2 | 1e-13 | 26/38 (NCI-H460, CFPAC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.514×** | -8.1 | 1e-13 | 25/44 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.539×** | -7.5 | 7e-12 | 26/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -7.0 | 3e-10 | 21/38 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.639×** | -5.4 | 5e-06 | 14/44 (H4, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -4.8 | 1e-04 | 16/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.678×** | -4.7 | 2e-04 | 13/41 (HT-29, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.666×** | -4.7 | 2e-04 | 19/43 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.700×** | -4.3 | 8e-04 | 14/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.703×** | -4.3 | 9e-04 | 15/43 (NCI-H460, A-427, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -4.1 | 0.002 | 12/43 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.719×** | -4.0 | 0.003 | 11/44 (A-427, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.726×** | -3.8 | 0.007 | 13/29 (SW1417, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.740×** | -3.7 | 0.009 | 15/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.014 | 13/43 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.018 | 8/43 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.033 | 15/44 (H4, SW 900, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.616×** | -3.1 | 0.045 | 6/40 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.710×** | -3.0 | 0.060 | 10/41 (LoVo, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.636×** | -2.9 | 0.074 | 9/37 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | **0.789×** | -2.9 | 0.074 | 10/42 (SNU-1, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.01 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -15.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0923× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0795× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 5.28 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0690× (z -9.2) |
| [[SW480 (line)]] | alt | 10.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -12.4) |
| [[BT-474 (line)]] | alt | 5.90 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0817× (z -8.7) |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0764× (z -10.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[Hs 766T (line)]] | wt | 5.07 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0666× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 9.94 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0682× (z -12.7) |
| [[SHP-77 (line)]] | alt | 6.86 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0343× (z -11.7) |
| [[SW 900 (line)]] | alt | 5.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0909× (z -9.2) |
| [[A-172 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.587 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN6]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LPIN3]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[HFE]] | +0.60 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[BPNT1]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CIPC]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ATP6V1A]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HINT3]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.57 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[TSPYL4]] | +0.57 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[POMK]] | +0.56 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[MED12]] | +0.56 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[SH3BGRL]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCM2]] | -0.62 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TUBB6]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MPP3]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[KLF16]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[FBXL18]] | -0.54 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[IL9RP3]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SPIRE1]] | -0.53 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DAP3]] | -0.53 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[ATP8B5P-1]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[ATAD3B]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LMBR1]] | -0.51 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[WNT2B]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICAL2]] | B | MICAL2 activity raises MINDY1's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without MICAL2 | 0.063 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[HNMT]] | B | HNMT activity raises MINDY1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without HNMT | 0.078 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[NEIL1]] | B | NEIL1 activity raises MINDY1's level | lines that do not express NEIL1 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without NEIL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ANO7, PM20D2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-21.1, 27.0); signed map (-8.6, -30.4). **Vector** length 61.4, 9.05% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.9 | +11.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +3.0 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.9 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -12.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -7.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | MINDY lysine 48 deubiquitinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,996,549-151,008,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11280, MINDY-1; previously FAM63A |
| Gene groups (HGNC) | MINDY deubiquitinases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5J2](https://www.uniprot.org/uniprotkb/Q8N5J2) (Ubiquitin carboxyl-terminal hydrolase MINDY-1):

> Hydrolase that can specifically remove 'Lys-48'-linked conjugated ubiquitin from proteins. Has exodeubiquitinase activity and has a preference for long polyubiquitin chains. May play a regulatory role at the level of protein turnover.

**Summary**, from NCBI Gene [55793](https://www.ncbi.nlm.nih.gov/gene/55793):

> Enables K48-linked deubiquitinase activity; K48-linked polyubiquitin modification-dependent protein binding activity; and cysteine-type carboxypeptidase activity. Predicted to be involved in proteolysis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25648) · Entrez [55793](https://www.ncbi.nlm.nih.gov/gene/55793) · UniProt [Q8N5J2](https://www.uniprot.org/uniprotkb/Q8N5J2) · Ensembl [ENSG00000143409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143409)

## Data

Gene col 6738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6738); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6738]; `tensor/DDL_lfc|DDL_z.npy` [6738]; `embed/gene_vectors.npy` [6738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6738 or target_col == 6738). Every well: [[MINDY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINDY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
