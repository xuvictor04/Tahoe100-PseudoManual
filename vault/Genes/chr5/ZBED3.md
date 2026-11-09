---
symbol: "ZBED3"
type: "gene"
col: 5384
ensembl_id: "ENSG00000132846"
name: "zinc finger BED-type containing 3"
location: "5q13.3"
module: 133
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# ZBED3

*zinc finger BED-type containing 3* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.72× (z +5.8, q 5e-06, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.327× (z -11.9, q 6e-30, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM268]] (+0.76, fdr 7e-06), [[SLC3A2]] (+0.72, fdr 7e-06), [[BLTP3A]] (+0.70, fdr 7e-06); moves opposite to [[CAP1]] (-0.59, fdr 4e-05), [[EHBP1L1]] (-0.58, fdr 3e-05), [[CD59]] (-0.56, fdr 9e-06).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 11 go from it, the strongest it → [[RAVER2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +5.8 | 5e-06 | 28/44 (LoVo, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.0 | 1e-04 | 19/36 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.002 | 11/43 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.3 | 0.002 | 13/44 (Panc 03.27, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.004 | 14/40 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.5 | 0.042 | 4/18 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.046 | 12/44 (SW 900, LS 180, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.79×** | +3.3 | 0.080 | 3/35 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.2 | 0.083 | 12/44 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.77×** | +3.2 | 0.084 | 7/41 (LoVo, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +3.1 | 0.100 | 8/42 (RKO, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.11 | 8/42 (RKO, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.30× | +3.0 | 0.11 | 6/44 (NCI-H2347, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.327×** | -11.9 | 6e-30 | 31/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.372×** | -10.6 | 1e-23 | 32/43 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.403×** | -9.7 | 7e-20 | 32/44 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.620×** | -5.1 | 5e-05 | 23/44 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -5.0 | 5e-05 | 18/43 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -4.1 | 0.004 | 19/43 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -3.8 | 0.010 | 19/41 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.714×** | -3.6 | 0.023 | 15/44 (PANC-1, RKO, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -3.5 | 0.028 | 13/43 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -3.4 | 0.040 | 21/42 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.573×** | -3.1 | 0.099 | 13/38 (SW48, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.752× | -3.0 | 0.11 | 5/43 (PANC-1, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.46 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.148× (z -9.9) |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -11.3) |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[SW480 (line)]] | alt | 7.41 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.142× (z -10.9) |
| [[RKO (line)]] | wt | 14.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -9.2) |
| [[A-427 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[C32 (line)]] | wt | 6.78 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0712× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -8.5) |
| [[KATO III (line)]] | alt | 19.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -10.7) |
| [[LS 180 (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 4.20 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0706× (z -8.5) |
| [[SW1417 (line)]] | alt | 7.48 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.229× (z -9.2) |
| [[SW48 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM268]] | +0.76 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SLC3A2]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[BLTP3A]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[HOXD3]] | +0.65 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[MTO1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[C10orf95-AS1]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[SIAH1]] | +0.60 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[MIA2]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[HDDC2]] | +0.59 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[DIS3L]] | +0.59 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[ATF5]] | +0.59 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAP1]] | -0.59 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[EHBP1L1]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CD59]] | -0.56 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[DIAPH1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[EHD4]] | -0.55 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[TGM2]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ARPC2]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TMEM92]] | -0.51 | -0.57 / -0.20 | both halves | 7e-04 |  |
| [[TPM3]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PCMT1]] | -0.51 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[RASA1]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MYO1E]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity weakens ZBED3's drug response | lines that do not express F3 (24) vs lines expressing it (20) | the lines without F3 respond 1.03× as strongly (z diff -0.34); strongest at Digitoxin 0.5 µM: 0.50x vs 0.76x (z diff -2.0) | 0.020 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; target measured in part of the lines; both ways; artifact flags |
| [[HOXB9]] | B | HOXB9 activity raises ZBED3's level | lines that do not express HOXB9 (17) vs lines expressing it (33) | 1.27× lower at baseline in the lines without HOXB9 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises ZBED3's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.41× lower at baseline in the lines without ANK2 | 0.096 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[MYADM]] | C | MYADM activity lowers ZBED3's level | lines that do not express MYADM (3) vs lines expressing it (47) | 3.67× higher at baseline in the lines without MYADM | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAVER2]] | C | ZBED3 activity raises RAVER2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[SMAD1]] | C | ZBED3 activity raises SMAD1's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.50× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[BLTP3A]] | C | ZBED3 activity raises BLTP3A's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[GNAI2]] | C | ZBED3 activity lowers GNAI2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.15× higher at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[PIGB]] | C | ZBED3 activity raises PIGB's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[SLC3A2]] | C | ZBED3 activity raises SLC3A2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[SLC2A11]] | C | ZBED3 activity raises SLC2A11's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without ZBED3 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent |
| [[C10orf95-AS1]] | C | ZBED3 activity raises C10orf95-AS1's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[ZNF32]] | C | ZBED3 activity raises ZNF32's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[ARPC2]] | C | ZBED3 activity lowers ARPC2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.76× higher at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[PAIP1]] | C | ZBED3 activity raises PAIP1's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.4, 46.4); signed map (-12.3, 21.7). **Vector** length 89.7, 19.1% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.9 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -11.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -5.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.8 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | +0.1 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:77,072,072-77,087,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15435 |
| Gene groups (HGNC) | Zinc fingers BED-type; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IU2](https://www.uniprot.org/uniprotkb/Q96IU2) (Zinc finger BED domain-containing protein 3):

> Acts as a positive regulator in the activation of the canonical Wnt/beta-catenin signaling pathway by stabilizing cytoplasmic beta-catenin (By similarity). Involved in transcription activation of Wnt target gene expression (By similarity). Plays a role in symmetric division of blastomeres in the early stages of embryogenesis via regulation of mitotic spindle central positioning and organization of the F-actin filament network (By similarity).

**Summary**, from NCBI Gene [84327](https://www.ncbi.nlm.nih.gov/gene/84327):

> This gene belongs to a class of genes that arose through hAT DNA transposition and that encode regulatory proteins. This gene is upregulated in lung cancer tissues, where the encoded protein causes an accumulation of beta-catenin and enhanced lung cancer cell invasion. In addition, the encoded protein can be secreted and be involved in resistance to insulin. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:20711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20711) · Entrez [84327](https://www.ncbi.nlm.nih.gov/gene/84327) · UniProt [Q96IU2](https://www.uniprot.org/uniprotkb/Q96IU2) · Ensembl [ENSG00000132846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132846)

## Data

Gene col 5384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5384); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5384]; `tensor/DDL_lfc|DDL_z.npy` [5384]; `embed/gene_vectors.npy` [5384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5384 or target_col == 5384). Every well: [[ZBED3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
