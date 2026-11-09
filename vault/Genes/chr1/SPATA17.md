---
symbol: "SPATA17"
type: "gene"
col: 8583
ensembl_id: "ENSG00000162814"
name: "spermatogenesis associated 17"
location: "1q41"
module: 10
arm: "+"
pooled_cpm: 9.37
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SPATA17

*spermatogenesis associated 17* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.42× (z +7.9, q 1e-12, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.247× (z -12.5, q 4e-33, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASC2]] (+0.70, fdr 7e-06), [[CCDC191]] (+0.65, fdr 7e-06), [[FAM174A-DT]] (+0.64, fdr 7e-06); moves opposite to [[EXTL3]] (-0.47, fdr 2e-04), [[POR]] (-0.47, fdr 2e-04), [[GLIPR2]] (-0.47, fdr 0.002, ⚠ one half only (not replicated)), [[SBK1]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CRB1]] → it (grade B ⚠); 10 go from it, the strongest it → [[CCDC40]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +7.9 | 1e-12 | 32/44 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.48×** | +5.0 | 1e-04 | 21/44 (Hs 766T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +4.9 | 1e-04 | 19/44 (BT-474, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.5 | 8e-04 | 7/16 (J82, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +4.4 | 0.001 | 17/43 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.004 | 19/44 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.022 | 13/41 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.035 | 11/41 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.035 | 9/43 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.061 | 8/44 (HOP62, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.061 | 11/44 (SHP-77, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.247×** | -12.5 | 4e-33 | 38/44 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.281×** | -11.4 | 2e-27 | 33/39 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.346×** | -9.5 | 4e-19 | 30/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.420×** | -7.8 | 1e-12 | 30/43 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.468×** | -6.8 | 1e-09 | 26/44 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.509×** | -5.8 | 6e-07 | 24/42 (HT-29, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.635×** | -5.7 | 8e-07 | 27/43 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.538×** | -5.5 | 2e-06 | 25/42 (KATO III, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.681×** | -4.9 | 7e-05 | 20/44 (HCT15, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.593×** | -4.7 | 2e-04 | 17/44 (NCI-H460, SHP-77, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.608×** | -4.5 | 4e-04 | 19/44 (RPMI-7951, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.628×** | -4.2 | 0.002 | 18/38 (HT-29, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.633×** | -4.1 | 0.002 | 19/42 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.423×** | -4.0 | 0.002 | 15/41 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.629×** | -4.0 | 0.003 | 18/43 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -4.0 | 0.003 | 19/40 (HS-578T, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.671×** | -3.6 | 0.012 | 19/43 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.573×** | -3.6 | 0.012 | 14/45 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.1 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0834× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0494× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -10.8) |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0518× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 8.15 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0716× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.113× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 7.37 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0766× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0299× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0711× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 9.99 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0174× (z -14.8) |
| [[SHP-77 (line)]] | alt | 40.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.7) |
| [[A498 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 4.36 | 0 | 1 | — | [[Erythromycin (drug)]] 0.5 µM 0.0586× (z -8.8) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -8.6) |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0594× (z -9.5) |
| [[J82 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 7.64 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0414× (z -12.0) |
| [[LoVo (line)]] | wt | 5.14 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0728× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 5.31 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 4.60 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0749× (z -8.6) |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC2]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CCDC191]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[FAM174A-DT]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TAPT1-AS1]] | +0.58 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[EFCAB6]] | +0.57 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[CARF]] | +0.56 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[ZRANB2-DT]] | +0.55 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[AK8]] | +0.54 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[PMFBP1]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MOK]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[C11orf65]] | +0.52 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[IQCH]] | +0.52 | +0.62 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXTL3]] | -0.47 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[POR]] | -0.47 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[GLIPR2]] | -0.47 | -0.12 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[SBK1]] | -0.47 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ARVCF]] | -0.46 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[LHX2]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PRRG1]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[C1GALT1]] | -0.44 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[ABHD3]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[CCDC69]] | -0.43 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[RPLP0P2]] | -0.43 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[TMEM184B]] | -0.43 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RELL1]] | -0.43 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[PPP1R21]] | -0.43 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRB1]] | B | CRB1 activity raises SPATA17's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without CRB1 | 0.023 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[PRKN]] | B | PRKN activity raises SPATA17's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without PRKN | 0.043 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[PMFBP1]] | B | PMFBP1 activity raises SPATA17's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.84× lower at baseline in the lines without PMFBP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[FBXO15]] | B | FBXO15 activity raises SPATA17's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without FBXO15 | 0.073 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC40]] | C | SPATA17 activity raises CCDC40's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.95× lower at baseline in the lines without SPATA17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[CCDC191]] | C | SPATA17 activity raises CCDC191's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.75× lower at baseline in the lines without SPATA17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[CCDC7]] | C | SPATA17 activity raises CCDC7's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without SPATA17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[DCDC1]] | C | SPATA17 activity raises DCDC1's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without SPATA17 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent |
| [[PMFBP1]] | C | SPATA17 activity raises PMFBP1's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 3.09× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[CASC2]] | C | SPATA17 activity raises CASC2's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[IQCH]] | C | SPATA17 activity raises IQCH's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[FAM227A]] | C | SPATA17 activity raises FAM227A's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[LINC00663]] | C | SPATA17 activity raises LINC00663's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[BACE1-AS]] | C | SPATA17 activity raises BACE1-AS's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.5, 27.6); signed map (3.1, 4.9). **Vector** length 65.4, 12.2% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -3.0 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.1 | +1.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.1 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:217,631,324-217,871,696 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IQCH, MOT17, FAP305, CFAP305 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

UniProt [Q96L03](https://www.uniprot.org/uniprotkb/Q96L03) carries no function annotation.

**Summary**, from NCBI Gene [128153](https://www.ncbi.nlm.nih.gov/gene/128153):

> Predicted to enable calmodulin binding activity. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25184) · Entrez [128153](https://www.ncbi.nlm.nih.gov/gene/128153) · UniProt [Q96L03](https://www.uniprot.org/uniprotkb/Q96L03) · Ensembl [ENSG00000162814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162814)

## Data

Gene col 8583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8583); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8583]; `tensor/DDL_lfc|DDL_z.npy` [8583]; `embed/gene_vectors.npy` [8583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8583 or target_col == 8583). Every well: [[SPATA17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
